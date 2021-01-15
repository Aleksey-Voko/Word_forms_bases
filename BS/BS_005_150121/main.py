from BS.tmpl_nouns_plurl import get_plurl_word_forms
from BS.tmpl_nouns_singl import get_singl_word_forms
from BS.utils import (read_src_bs, save_bs_dicts_to_txt,
                      get_dicts_from_csv_file, get_string_list_from_file)
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
            plurl_word_forms = get_plurl_word_forms(src_dict,
                                                    singl_word_forms)
            word_forms += plurl_word_forms
    elif src_dict['Inf_4']:
        plurl_word_forms = get_plurl_word_forms(src_dict, [])
        word_forms += plurl_word_forms

    title_word_form = TitleWordForm(name, word_forms[0].idf, info, '')
    return GroupWordForm(title_word_form, word_forms[1:])


def add_groups_to_bs():
    """
    2 (продолжение).
    Соблюдая алфавитный порядок ЗС в док-те БС 15.01.21.txt,
    добавить в док-т БС 15.01.21.txt
    одиночки из док-та Добавить одиночки в БС 2.txt .

    4. Соблюдая алфавитный порядок ЗС в БС, добавить в БС группы
    из док-тов Добавить группы в БС. Сущ-ные изм.txt
    и Добавить группы в БС. Сущ-ные 2.txt .
    """
    word_forms_bases = list(read_src_bs('src_dict/БС 15.01.21.txt'))

    loners = get_string_list_from_file(
        'src_dict/Добавить одиночки в БС 2.txt')
    loners_list = []
    for loner in loners:
        title_word_form = TitleWordForm(loner, '', [], '')
        group_word_form = GroupWordForm(title_word_form, [])
        loners_list.append(group_word_form)

    modified_nouns = list(read_src_bs(
        'src_dict/Добавить группы в БС. Сущ-ные изм.txt'))
    nouns_2 = list(read_src_bs('src_dict/Добавить группы в БС. Сущ-ные 2.txt',
                               encoding='utf-8'))

    word_forms_bases += loners_list
    word_forms_bases += modified_nouns
    word_forms_bases += nouns_2

    save_bs_dicts_to_txt(sorted(word_forms_bases), 'out/БС 15.01.21.txt')


if __name__ == '__main__':
    add_groups_to_bs()
