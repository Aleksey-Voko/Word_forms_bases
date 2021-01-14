from BS.tmpl_nouns_plurl import get_plurl_word_forms
from BS.tmpl_nouns_singl import get_singl_word_forms
from BS.utils import (read_src_bs, save_bs_dicts_to_txt,
                      get_dicts_from_csv_file)
from BS.word_form import GroupWordForm, TitleWordForm


def alphabetical_order():
    """Теперь нужно только расположить группы в док-те Кунсткамера2.txt
    в соответствии с алфавитным порядком ЗС.
    Поэтому высылаю док-т Кунсткамера2.txt"""
    kunstkamera_2 = read_src_bs('src_dict/Кунсткамера2.txt', encoding='utf-8')
    save_bs_dicts_to_txt(sorted(kunstkamera_2), 'out/Кунсткамера2.txt',
                         encoding='utf-8')


def add_groups_to_bs():
    """3. Используя списки на вкладке "Добавить группы в БС"
    док-та Существительные.xlsx ,
    а также шаблоны, приведённые на вкладках "ШАБЛОНЫ ед.ч." и "ШАБЛОНЫ мн.ч."
    того же док-та,
    создать док-т Добавить группы в БС. Сущ-ные.txt ."""
    src_groups = get_dicts_from_csv_file('Добавить группы в БС.csv')
    add_groups_to_bs_list = []

    for src_dict in src_groups:
        add_groups_to_bs_list.append(get_group_word_form(src_dict))

    save_bs_dicts_to_txt(sorted(add_groups_to_bs_list),
                         'out/Добавить группы в БС. Сущ-ные.txt',
                         encoding='utf-8')

    word_forms_bases = list(read_src_bs('src_dict/БС 13.12.20.txt'))
    word_forms_bases += add_groups_to_bs_list
    save_bs_dicts_to_txt(sorted(word_forms_bases), 'out/БС 14.12.20.txt')


def get_group_word_form(src_dict: dict) -> GroupWordForm:

    name = src_dict['name']
    info = [src_dict['Inf_0']]
    if src_dict['Inf_1']:
        info.append(''.join(list(filter(None, [
            src_dict['Inf_1'],
            src_dict['Inf_2'],
            src_dict['Inf_3']]))))
    if src_dict['Inf_4']:
        info.append(''.join(list(filter(None, [
            src_dict['Inf_4'],
            src_dict['Inf_5'],
            src_dict['Inf_6']]))))

    word_forms = []
    if src_dict['Inf_1']:
        singl_word_forms = get_singl_word_forms(src_dict)
        word_forms += singl_word_forms
        if src_dict['Inf_4']:
            plurl_word_forms = get_plurl_word_forms(src_dict, singl_word_forms)
            word_forms += plurl_word_forms
    elif src_dict['Inf_4']:
        plurl_word_forms = get_plurl_word_forms(src_dict, [])
        word_forms += plurl_word_forms

    title_word_form = TitleWordForm(name, word_forms[0].idf, info, '')
    return GroupWordForm(title_word_form, word_forms[1:])


if __name__ == '__main__':
    add_groups_to_bs()
