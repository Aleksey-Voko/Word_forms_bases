from BS.utils import (get_string_list_from_file, get_bs_title_word_form,
                      get_socket_word_form, save_list_to_file)


def get_diff_lists():
    ordinary_words_bs_list = get_string_list_from_file(
        'src_dict/Обычные слова БС.txt')
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
        'src_dict/Обычные слова БГ.txt')
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
