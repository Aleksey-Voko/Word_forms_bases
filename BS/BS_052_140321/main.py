import string

from BS.utils import (read_src_socket_bs, save_list_to_file, read_src_bs,
                      get_string_list_from_file,  get_socket_word_form,
                      get_bs_title_word_form)

CYRILLIC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ALPHABET = CYRILLIC + string.ascii_uppercase


def get_bg_abbreviation():
    socket_group_list = read_src_socket_bs('src_dict/БГ 13.03.21.txt')

    abbreviation_bg = []
    capital_letter_bg = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if not word_form.invisible:
                    form_name = word_form.name.replace('*', '')
                    chars = set(form_name[:2])
                    if all(map(lambda x: x in ALPHABET, chars)):
                        abbreviation_bg.append(str(word_form))
                    elif form_name[0] in ALPHABET:
                        capital_letter_bg.append(str(word_form))

    save_list_to_file(
        sorted(abbreviation_bg, key=lambda x: x.replace('*', '')),
        'out/Аббревиатура. БГ.txt'
    )

    save_list_to_file(
        sorted(capital_letter_bg, key=lambda x: x.replace('*', '')),
        'out/Большая буква. БГ.txt'
    )


def get_bs_abbreviation():
    word_forms_bases = read_src_bs('src_dict/БС 13.03.21.txt')

    abbreviation_bs = []
    capital_letter_bs = []

    for group in word_forms_bases:
        title_form = group.title_word_form
        form_name = title_form.name.replace('*', '')
        chars = set(form_name[:2])
        if all(map(lambda x: x in ALPHABET, chars)):
            abbreviation_bs.append(str(title_form))
        elif form_name[0] in ALPHABET:
            capital_letter_bs.append(str(title_form))

    save_list_to_file(
        sorted(abbreviation_bs, key=lambda x: x.replace('*', '')),
        'out/Аббревиатура. БС.txt'
    )

    save_list_to_file(
        sorted(capital_letter_bs, key=lambda x: x.replace('*', '')),
        'out/Большая буква. БС.txt'
    )


def get_bg_abbreviation_homonyms():
    abbreviation_bg = get_string_list_from_file(
        'out/Аббревиатура. БГ.txt')
    abbreviation_bg = sorted(list(set(abbreviation_bg)))

    socket_group_list = list(read_src_socket_bs('src_dict/БГ 13.03.21.txt'))

    bg_abbreviation_homonyms = []

    for abbreviation in abbreviation_bg:
        abbreviation_name = get_socket_word_form(abbreviation).name
        word_form_list = []
        for socket_group in socket_group_list:
            for sub_group in socket_group.sub_groups:
                for word_form in sub_group.socket_word_forms:
                    if not word_form.invisible:
                        form_name = word_form.name.replace('*', '')
                        if form_name == abbreviation_name.lower():
                            print(form_name)
                            word_form_list.append(str(word_form))
        if word_form_list:
            bg_abbreviation_homonyms.append(abbreviation)
            bg_abbreviation_homonyms += word_form_list
            bg_abbreviation_homonyms.append('')

    save_list_to_file(bg_abbreviation_homonyms[:-1],
                      'out/Аббревиатура. БГ. Омонимы.txt')


def get_bs_abbreviation_homonyms():
    abbreviation_bs = get_string_list_from_file(
        'out/Аббревиатура. БС.txt')

    word_forms_bases = read_src_bs('src_dict/БС 13.03.21.txt')
    title_forms = [str(x.title_word_form) for x in word_forms_bases]

    bs_abbreviation_homonyms = []

    for abbreviation in abbreviation_bs:
        abbreviation_name = get_bs_title_word_form(abbreviation).name
        title_form_list = []
        for title_form in title_forms:
            form_name = get_bs_title_word_form(title_form).name.replace('*', '')
            if form_name == abbreviation_name.lower():
                print(title_form)
                title_form_list.append(title_form)

        if title_form_list:
            bs_abbreviation_homonyms.append(abbreviation)
            bs_abbreviation_homonyms += title_form_list
            bs_abbreviation_homonyms.append('')

    save_list_to_file(bs_abbreviation_homonyms[:-1],
                      'out/Аббревиатура. БС. Омонимы.txt')


def get_capital_letter_bg():
    capital_letter_bg = list(get_string_list_from_file(
        'out/Большая буква. БГ.txt'))
    socket_group_list = list(read_src_socket_bs('src_dict/БГ 13.03.21.txt'))

    capital_letter_bg_homonyms = []

    for capital_word in capital_letter_bg:
        capital_word_name = get_socket_word_form(capital_word).name
        word_form_list = []
        for socket_group in socket_group_list:
            for sub_group in socket_group.sub_groups:
                for word_form in sub_group.socket_word_forms:
                    if not word_form.invisible:
                        form_name = word_form.name.replace('*', '')
                        if form_name == capital_word_name.lower():
                            print(word_form)
                            word_form_list.append(str(word_form))

        if word_form_list:
            capital_letter_bg_homonyms.append(capital_word)
            capital_letter_bg_homonyms += word_form_list
            capital_letter_bg_homonyms.append('')

    save_list_to_file(capital_letter_bg_homonyms[:-1],
                      'out/Большая буква. БГ. Омонимы.txt')


def get_capital_letter_bs():
    capital_letter_bs = list(get_string_list_from_file(
        'out/Большая буква. БС.txt'))

    word_forms_bases = read_src_bs('src_dict/БС 13.03.21.txt')
    title_forms = [str(x.title_word_form) for x in word_forms_bases]

    capital_letter_bs_homonyms = []

    for capital_word in capital_letter_bs:
        capital_word_name = get_bs_title_word_form(capital_word).name
        title_form_list = []
        for title_form in title_forms:
            form_name = get_bs_title_word_form(title_form).name.replace('*', '')
            if form_name == capital_word_name.lower():
                print(title_form)
                title_form_list.append(title_form)

        if title_form_list:
            capital_letter_bs_homonyms.append(capital_word)
            capital_letter_bs_homonyms += title_form_list
            capital_letter_bs_homonyms.append('')

    save_list_to_file(capital_letter_bs_homonyms[:-1],
                      'out/Большая буква. БС. Омонимы.txt')


if __name__ == '__main__':
    get_capital_letter_bs()
