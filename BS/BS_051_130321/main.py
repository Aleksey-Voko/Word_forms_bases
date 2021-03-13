from BS.utils import (get_string_list_from_file, read_src_socket_bs,
                      get_socket_word_form, save_list_to_file, read_src_bs,
                      get_bs_title_word_form)


def get_bg_abbreviation_homonyms():
    abbreviation_bg = get_string_list_from_file(
        'src_dict/Аббревиатура. БГ.txt')
    abbreviation_bg = sorted(list(set(abbreviation_bg)))

    socket_group_list = list(read_src_socket_bs('src_dict/БГ 09.03.21.txt'))

    bg_abbreviation_homonyms = []

    for abbreviation in abbreviation_bg:
        abbreviation_name = get_socket_word_form(abbreviation).name
        for socket_group in socket_group_list:
            for sub_group in socket_group.sub_groups:
                for word_form in sub_group.socket_word_forms:
                    if not word_form.invisible:
                        form_name = word_form.name.replace('*', '')
                        if form_name == abbreviation_name.lower():
                            bg_abbreviation_homonyms.append(str(word_form))

    save_list_to_file(
        sorted(bg_abbreviation_homonyms, key=lambda x: x.replace('*', '')),
        'out/Аббревиатура. БГ. Омонимы.txt'
    )


def get_bs_abbreviation_homonyms():
    abbreviation_bs = get_string_list_from_file(
        'src_dict/Аббревиатура. БС.txt')

    word_forms_bases = read_src_bs('src_dict/БС 09.03.21.txt')
    title_forms = [str(x.title_word_form) for x in word_forms_bases]

    bs_abbreviation_homonyms = []

    for abbreviation in abbreviation_bs:
        abbreviation_name = get_bs_title_word_form(abbreviation).name
        for title_form in title_forms:
            form_name = get_bs_title_word_form(title_form).name.replace('*', '')
            if form_name == abbreviation_name.lower():
                print(title_form)
                bs_abbreviation_homonyms.append(title_form)

    save_list_to_file(
        sorted(bs_abbreviation_homonyms, key=lambda x: x.replace('*', '')),
        'out/Аббревиатура. БС. Омонимы.txt'
    )


def get_capital_letter_bg():
    capital_letter_bg = list(get_string_list_from_file(
        'src_dict/Большая буква. БГ.txt'))
    socket_group_list = list(read_src_socket_bs('src_dict/БГ 09.03.21.txt'))

    capital_letter_bg_homonyms = []

    for capital_word in capital_letter_bg:
        capital_word_name = get_socket_word_form(capital_word).name
        for socket_group in socket_group_list:
            for sub_group in socket_group.sub_groups:
                for word_form in sub_group.socket_word_forms:
                    if not word_form.invisible:
                        form_name = word_form.name.replace('*', '')
                        if form_name == capital_word_name.lower():
                            print(word_form)
                            capital_letter_bg_homonyms.append(str(word_form))

    save_list_to_file(
        sorted(capital_letter_bg_homonyms, key=lambda x: x.replace('*', '')),
        'out/Большая буква. БГ. Омонимы.txt'
    )


def get_capital_letter_bs():
    capital_letter_bs = list(get_string_list_from_file(
        'src_dict/Большая буква. БС.txt'))

    word_forms_bases = read_src_bs('src_dict/БС 09.03.21.txt')
    title_forms = [str(x.title_word_form) for x in word_forms_bases]

    capital_letter_bs_homonyms = []

    for capital_word in capital_letter_bs:
        capital_word_name = get_bs_title_word_form(capital_word).name
        for title_form in title_forms:
            form_name = get_bs_title_word_form(title_form).name.replace('*', '')
            if form_name == capital_word_name.lower():
                print(title_form)
                capital_letter_bs_homonyms.append(title_form)

    save_list_to_file(
        sorted(capital_letter_bs_homonyms, key=lambda x: x.replace('*', '')),
        'out/Большая буква. БС. Омонимы.txt'
    )


if __name__ == '__main__':
    get_capital_letter_bs()
