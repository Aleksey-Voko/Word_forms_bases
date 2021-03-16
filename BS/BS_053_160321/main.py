from BS.utils import get_string_list_from_file, read_src_socket_bs, save_socket_bs_dicts_to_txt, read_src_bs, \
    save_bs_dicts_to_txt, save_list_to_file


def change_bg_abbreviation():
    abbreviation_bg = sorted(list(set(get_string_list_from_file(
        'src_dict/Аббревиатура. БГ.txt'))))
    capital_letter_bg = sorted(list(set(get_string_list_from_file(
        'src_dict/Большая буква. БГ.txt'))))

    socket_group_list = list(read_src_socket_bs('src_dict/БГ 15.03.21.txt'))

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if not word_form.invisible:
                    if (
                            str(word_form) in abbreviation_bg
                            or str(word_form) in capital_letter_bg
                    ):
                        word_form.name = word_form.name.lower()

    save_socket_bs_dicts_to_txt(socket_group_list, 'out/БГ 16.03.21.txt')


def change_bs_abbreviation():
    abbreviation_bs = list(get_string_list_from_file(
        'src_dict/Аббревиатура. БС.txt'))
    capital_letter_bs = list(get_string_list_from_file(
        'src_dict/Большая буква. БС.txt'))

    word_forms_bases = list(read_src_bs('src_dict/БС 15.03.21.txt'))

    for group in word_forms_bases:
        title_form = group.title_word_form
        if (
                str(title_form) in abbreviation_bs
                or str(title_form) in capital_letter_bs
        ):
            title_form.name = title_form.name.lower()
            for word_form in group.word_forms:
                word_form.name = word_form.name.lower()

    save_bs_dicts_to_txt(sorted(word_forms_bases), 'out/БС 16.03.21.txt')


def check_bg_islower():
    socket_group_list = read_src_socket_bs('out/БГ 16.03.21.txt')

    bg_islower_list = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                check_form = ' '.join(filter(None, [
                    word_form.invisible,
                    word_form.name,
                    word_form.root_index,
                    word_form.note,
                    word_form.etml_note,
                    word_form.spec_note,
                ]))
                check_form = check_form.replace('I', '')
                check_form = check_form.replace('V', '')
                if not check_form.islower():
                    print(check_form)
                    bg_islower_list.append(str(word_form))

    save_list_to_file(bg_islower_list, 'out/БГ ЕСТЬ большие буквы.txt')


def check_bs_islower():
    word_forms_bases = list(read_src_bs('out/БС 16.03.21.txt'))

    bs_islower_list = []

    for group in word_forms_bases:
        title_form = group.title_word_form
        check_form = ' '.join(filter(None, [
            title_form.name,
            title_form.note,
        ]))
        check_form = check_form.replace('I', '')
        check_form = check_form.replace('V', '')
        if not check_form.islower():
            print(check_form)
            bs_islower_list.append(str(title_form))

    save_list_to_file(bs_islower_list, 'out/БС ЕСТЬ большие буквы.txt')


if __name__ == '__main__':
    check_bs_islower()
