from BS.utils import (read_src_socket_bs, get_dicts_from_csv_file,
                      get_socket_word_form, get_string_list_from_file,
                      save_list_to_file, read_src_bs)


def ordinary_words_bg():
    socket_group_list = list(read_src_socket_bs(
        'src_dict/БГ 01.03.21.txt'))

    exclusion_list = []

    # Многокорневые слова
    multi_root_words = get_dicts_from_csv_file(
        'src_dict/Многокорневые слова.csv')
    multi_root_bg_forms = []

    for multi_root_word in multi_root_words:
        for root_index_key in list(multi_root_word)[1:]:
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
    word_forms_bases = read_src_bs('src_dict/БС 02.03.21.txt')
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
    exclusion_list += remaining_repetitions

    # Обычные слова БС
    ordinary_words_bs_list = []

    for bs_str_form in bs_word_forms:
        if bs_str_form not in exclusion_list:
            ordinary_words_bs_list.append(bs_str_form)
            print(bs_str_form)

    save_list_to_file(ordinary_words_bs_list, 'out/Обычные слова БС.txt')


if __name__ == '__main__':
    ordinary_words_bs()
