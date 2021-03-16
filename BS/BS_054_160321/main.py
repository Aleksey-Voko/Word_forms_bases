from BS.utils import read_src_socket_bs, read_src_bs, save_list_to_file


CYRILLIC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def check_bg_islower():
    socket_group_list = read_src_socket_bs('src_dict/БГ 16.03.21 изм.txt')

    bg_islower_name_list = []
    bg_islower_note_list = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if not word_form.invisible:

                    if not word_form.name.islower():
                        print(word_form)
                        bg_islower_name_list.append(str(word_form))

                    note_form = ' '.join(filter(None, [
                        word_form.note,
                        word_form.etml_note,
                        word_form.spec_note,
                    ]))

                    if any(map(lambda x: x in CYRILLIC, note_form)):
                        print(note_form)
                        bg_islower_note_list.append(str(word_form))

    save_list_to_file(bg_islower_name_list, 'out/БГ ЕСТЬ большие буквы СЛОВО.txt')
    save_list_to_file(bg_islower_note_list, 'out/БГ ЕСТЬ большие буквы ПРИМЕЧАНИЯ.txt')


def check_bs_islower():
    word_forms_bases = list(read_src_bs('src_dict/БС 16.03.21 изм.txt'))

    bs_islower_name_list = []
    bs_islower_note_list = []

    for group in word_forms_bases:
        title_form = group.title_word_form

        if not title_form.name.islower():
            print(title_form)
            bs_islower_name_list.append(str(title_form))

        if any(map(lambda x: x in CYRILLIC, title_form.note)):
            print(title_form)
            bs_islower_note_list.append(str(title_form))

    save_list_to_file(bs_islower_name_list, 'out/БС ЕСТЬ большие буквы СЛОВО.txt')
    save_list_to_file(bs_islower_note_list, 'out/БС ЕСТЬ большие буквы ПРИМЕЧАНИЯ.txt')


if __name__ == '__main__':
    check_bs_islower()
