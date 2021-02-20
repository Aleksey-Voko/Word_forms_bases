from BS.utils import read_src_socket_bs, save_list_to_file


def get_bg_note():
    socket_group_list = read_src_socket_bs('src_dict/БГ 17.02.21.txt')

    bg_notes = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms[1:]:
                if word_form.note:
                    print(word_form)
                    bg_notes.append(str(word_form))

    save_list_to_file(bg_notes, 'out/Пояснительные примечания.txt')


if __name__ == '__main__':
    get_bg_note()
