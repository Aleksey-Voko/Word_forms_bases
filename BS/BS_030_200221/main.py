from pprint import pprint

from BS.utils import read_src_bs, get_string_list_from_file, get_socket_word_form, save_list_to_file


def check_unique_strings():
    word_forms_bases = read_src_bs('src_dict/БС 20.02.21.txt')
    bs_title_forms = [x.title_word_form for x in word_forms_bases]
    bs_title_str_forms = [
        ' '.join(filter(None, [
            x.name,
            x.idf,
            ' '.join(x.info),
        ]))
        for x in bs_title_forms
    ]

    # Повторяющиеся строки
    repeating_lines = get_string_list_from_file(
        'src_dict/Повторы в группах. Повторяющиеся строки.txt')

    r_lines_resp = []
    r_lines_not_resp = []

    for line in repeating_lines:
        socket_form = get_socket_word_form(line)
        str_form = ' '.join(filter(None, [
            socket_form.name,
            socket_form.idf,
            ' '.join(socket_form.info),
        ]))
        if bs_title_str_forms.count(str_form) == 1:
            r_lines_resp.append(line)
        else:
            r_lines_not_resp.append(line)

    save_list_to_file(
        r_lines_resp,
        'out/Повторы в группах. Повторяющиеся строки. П.4 Правил соблюдается.txt'
    )

    save_list_to_file(
        r_lines_not_resp,
        'out/Повторы в группах. Повторяющиеся строки. П.4 Правил не соблюдается.txt'
    )

    # Уникальные строки
    unique_lines = get_string_list_from_file(
        'src_dict/Повторы в группах. Уникальные строки.txt')

    u_lines_resp = []
    u_lines_not_resp = []

    for line in unique_lines:
        socket_form = get_socket_word_form(line)
        str_form = ' '.join(filter(None, [
            socket_form.name,
            socket_form.idf,
            ' '.join(socket_form.info),
        ]))
        if bs_title_str_forms.count(str_form) == 1:
            u_lines_resp.append(line)
        else:
            u_lines_not_resp.append(line)

    save_list_to_file(
        u_lines_resp,
        'out/Повторы в группах. Уникальные строки. П.4 Правил соблюдается.txt'
    )

    save_list_to_file(
        u_lines_not_resp,
        'out/Повторы в группах. Уникальные строки. П.4 Правил не соблюдается.txt'
    )


if __name__ == '__main__':
    check_unique_strings()
