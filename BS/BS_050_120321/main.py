from BS.utils import read_src_socket_bs, save_list_to_file, read_src_bs

CYRILLIC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def get_bg_abbreviation():
    socket_group_list = read_src_socket_bs('src_dict/БГ 09.03.21.txt')

    abbreviation_bg = []
    capital_letter_bg = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if not word_form.invisible:
                    form_name = word_form.name.replace('*', '')
                    chars = set(form_name[:2])
                    if all(map(lambda x: x in CYRILLIC, chars)):
                        abbreviation_bg.append(str(word_form))
                    elif form_name[0] in CYRILLIC:
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
    word_forms_bases = read_src_bs('src_dict/БС 09.03.21.txt')

    abbreviation_bs = []
    capital_letter_bs = []

    for group in word_forms_bases:
        title_form = group.title_word_form
        form_name = title_form.name.replace('*', '')
        chars = set(form_name[:2])
        if all(map(lambda x: x in CYRILLIC, chars)):
            abbreviation_bs.append(str(title_form))
        elif form_name[0] in CYRILLIC:
            capital_letter_bs.append(str(title_form))

    save_list_to_file(
        sorted(abbreviation_bs, key=lambda x: x.replace('*', '')),
        'out/Аббревиатура. БС.txt'
    )

    save_list_to_file(
        sorted(capital_letter_bs, key=lambda x: x.replace('*', '')),
        'out/Большая буква. БС.txt'
    )


if __name__ == '__main__':
    get_bs_abbreviation()
