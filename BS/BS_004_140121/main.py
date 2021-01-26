from pprint import pprint

from BS.tmpl_nouns_plurl import get_plurl_word_forms
from BS.tmpl_nouns_singl import get_singl_word_forms
from BS.utils import (get_dicts_from_csv_file, save_bs_dicts_to_txt,
                      read_src_bs)
from BS.word_form import GroupWordForm, TitleWordForm


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
            plurl_word_forms = get_plurl_word_forms(
                src_dict, singl_word_forms)
            word_forms += plurl_word_forms
    elif src_dict['Inf_4']:
        plurl_word_forms = get_plurl_word_forms(src_dict, [])
        word_forms += plurl_word_forms

    pprint(word_forms)

    title_word_form = TitleWordForm(name, word_forms[0].idf, info, '')
    return GroupWordForm(title_word_form, word_forms[1:])


def save_groups_to_bs():
    """Ещё раз, пож-ста, п. 3.
    3. Используя списки на вкладке "Добавить группы в БС"
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


if __name__ == '__main__':
    save_groups_to_bs()
