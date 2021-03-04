from BS.tmpl_nouns_plurl import get_plurl_word_forms
from BS.tmpl_nouns_singl import get_singl_word_forms
from BS.utils import (get_dicts_from_csv_file, save_bs_dicts_to_txt,
                      read_src_bs, read_src_socket_bs,
                      get_string_list_from_file, get_socket_word_form,
                      save_list_to_file, get_bs_title_word_form)
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

    title_word_form = TitleWordForm(name, word_forms[0].idf, info, '')
    return GroupWordForm(title_word_form, word_forms[1:])


def save_groups_to_bs():
    src_groups = get_dicts_from_csv_file('Добавить группы в БС.csv')
    add_groups_to_bs_list = []

    for src_dict in src_groups:
        add_groups_to_bs_list.append(get_group_word_form(src_dict))

    save_bs_dicts_to_txt(sorted(add_groups_to_bs_list),
                         'out/Добавить группы в БС. Сущ-ные.txt',
                         encoding='utf-8')


def add_groups_to_bs():
    word_forms_bases = list(read_src_bs('src_dict/БС 04.03.21.txt'))

    nouns_2 = list(read_src_bs('out/Добавить группы в БС. Сущ-ные.txt',
                               encoding='utf-8'))

    word_forms_bases += nouns_2

    save_bs_dicts_to_txt(sorted(word_forms_bases), 'out/БС 04.03.21.txt')


def ordinary_words_bg():
    socket_group_list = list(read_src_socket_bs(
        'src_dict/БГ 04.03.21.txt'))

    exclusion_list = []

    # Многокорневые слова
    multi_root_words = get_dicts_from_csv_file(
        'src_dict/Многокорневые слова.csv')
    multi_root_bg_forms = []

    for multi_root_word in multi_root_words:
        for root_index_key in list(multi_root_word):
            if multi_root_word[root_index_key]:
                multi_root_bg_forms.append(multi_root_word[root_index_key])

    exclusion_list += multi_root_bg_forms

    # Повторы в группах
    replays_in_groups = []

    with open('src_dict/Повторы в группах.txt', encoding='utf-8') as f_in:
        groups = (x.strip() for x in f_in.read().split('\n\n'))
        for group in groups:
            for line in group.split('\n')[1:]:
                if not line.startswith('!'):
                    replays_in_groups.append(line)

    exclusion_list += replays_in_groups

    # Омонимы БГ
    homonyms_bg = get_string_list_from_file('src_dict/Омонимы БГ.txt')
    homonyms_bg_str_form = []

    for homonym in homonyms_bg:
        socket_form = get_socket_word_form(homonym)
        string_form = ' '.join(filter(
            None, [
                socket_form.invisible,
                socket_form.name,
                socket_form.root_index,
                socket_form.idf,
                ' '.join(socket_form.info),
                socket_form.note,
                socket_form.etml_note,
            ]
        ))
        homonyms_bg_str_form.append(string_form)

    exclusion_list += homonyms_bg_str_form

    # Слова, омонимичные многокорневым
    homonymous_words = get_string_list_from_file(
        'src_dict/Слова, омонимичные многокорневым словам.txt')
    homonymous_words_str_form = []

    for word in homonymous_words:
        socket_form = get_socket_word_form(word)
        string_form = ' '.join(filter(
            None, [
                socket_form.invisible,
                socket_form.name,
                socket_form.root_index,
                socket_form.idf,
                ' '.join(socket_form.info),
                socket_form.note,
                socket_form.etml_note,
            ]
        ))
        homonymous_words_str_form.append(string_form)

    exclusion_list += homonymous_words_str_form

    # Обычные слова БГ
    ordinary_words_bg_list = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if not word_form.invisible:
                    if str(word_form) not in exclusion_list:
                        ordinary_words_bg_list.append(word_form)

    ordinary_words_bg_list = [str(x) for x in sorted(ordinary_words_bg_list)]

    save_list_to_file(ordinary_words_bg_list, 'out/Обычные слова БГ.txt')


def ordinary_words_bs():
    word_forms_bases = read_src_bs('out/БС 04.03.21.txt')
    bs_word_forms = [str(x.title_word_form) for x in word_forms_bases]

    exclusion_list = []

    # Многокорневые слова БС
    multi_root_bs_forms = get_string_list_from_file(
        'src_dict/Многокорневые слова БС.txt')
    exclusion_list += multi_root_bs_forms

    # Омонимы БС
    homonyms_bs = get_string_list_from_file('src_dict/Омонимы БС.txt')
    exclusion_list += homonyms_bs

    # Повторы ост. совпадает с БС
    remaining_repetitions = get_string_list_from_file(
        'src_dict/Повторы ост. совпадает с БС.txt')
    remaining_repetitions = [str(get_bs_title_word_form(x))
                             for x in remaining_repetitions]
    exclusion_list += remaining_repetitions

    # Обычные слова БС
    ordinary_words_bs_list = []

    for bs_str_form in bs_word_forms:
        if bs_str_form not in exclusion_list:
            ordinary_words_bs_list.append(bs_str_form)

    save_list_to_file(ordinary_words_bs_list, 'out/Обычные слова БС.txt')


def get_diff_lists():
    ordinary_words_bs_list = get_string_list_from_file(
        'out/Обычные слова БС.txt')
    ordinary_words_bs_list = [
        get_bs_title_word_form(x)
        for x in ordinary_words_bs_list
    ]
    ordinary_words_bs_list = [
        ' '.join(filter(None, [
            x.name,
            x.idf,
            ' '.join(x.info),
            x.note.replace('.*', '').strip(),
        ]))
        for x in ordinary_words_bs_list
    ]

    ordinary_words_bg_list = get_string_list_from_file(
        'out/Обычные слова БГ.txt')
    ordinary_words_bg_list = [
        get_socket_word_form(x)
        for x in ordinary_words_bg_list
    ]
    ordinary_words_bg_list = [
        ' '.join(filter(None, [
            x.name,
            x.idf,
            ' '.join(x.info),
            x.note[2:],
        ]))
        for x in ordinary_words_bg_list
    ]

    matching_src = list(set(ordinary_words_bs_list)
                        & set(ordinary_words_bg_list))
    unique_src_bs = list(set(ordinary_words_bs_list)
                         - set(ordinary_words_bg_list))
    unique_src_bg = list(set(ordinary_words_bg_list)
                         - set(ordinary_words_bs_list))

    matching_forms = []
    unique_bs_forms = []
    unique_bg_forms = []

    for word in ordinary_words_bs_list:
        title_form = get_bs_title_word_form(word)
        str_form = ' '.join(filter(None, [
            title_form.name,
            title_form.idf,
            ' '.join(title_form.info),
            title_form.note.replace('.*', '').strip(),
        ]))
        if str_form in matching_src:
            matching_forms.append(title_form)
        elif str_form in unique_src_bs:
            unique_bs_forms.append(title_form)

    for word in ordinary_words_bg_list:
        socket_form = get_socket_word_form(word)
        str_form = ' '.join(filter(None, [
            socket_form.name,
            socket_form.idf,
            ' '.join(socket_form.info),
            socket_form.note[2:],
        ]))
        if str_form in unique_src_bg:
            unique_bg_forms.append(socket_form)

    save_list_to_file(matching_forms, 'out/Строки совпадают.txt')
    save_list_to_file(unique_bs_forms, 'out/Уникальные строки БС.txt')
    save_list_to_file(unique_bg_forms, 'out/Уникальные строки БГ.txt')


if __name__ == '__main__':
    get_diff_lists()
