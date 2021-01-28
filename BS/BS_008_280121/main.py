from BS.utils import (read_src_socket_bs, get_string_list_from_file,
                      save_list_to_file, save_socket_bs_dicts_to_txt)


def remove_from_bg():
    """
    9. Для всех слов из док-та "Удалить из БГ.txt" сделать следующее:
    9.1. найти такое слово в док-те "БГ 27.01.21.txt" и,
    9.2.1. если оно является ЗС ПОДгруппы - вставить его
    в отдельно созданный док-т "ЗС подгруппы.txt"
    9.2.2. если оно НЕ является ЗС ПОДгруппы - удалить его
    из док-та "БГ 27.01.21.txt"
    """
    remove_bg_list = get_string_list_from_file('src_dict/Удалить из БГ.txt')
    socket_group_word_form_list = list(
        read_src_socket_bs('src_dict/БГ 27.01.21.txt'))

    title_form_list = []
    deleted_list = []

    for remove_bg in sorted(remove_bg_list):
        for group in socket_group_word_form_list:
            for sub_group in group.sub_groups:
                title_word_form = sub_group.title_word_form
                for word_form in sub_group.socket_word_forms[:]:
                    if remove_bg == word_form.name:
                        print(word_form)
                        if remove_bg == title_word_form.name:
                            title_form_list.append(str(word_form))
                        else:
                            deleted_list.append(str(word_form))
                            sub_group.socket_word_forms.remove(word_form)

    save_list_to_file(sorted(title_form_list, key=str.lower),
                      'out/ЗС подгруппы.txt')
    save_list_to_file(sorted(deleted_list, key=str.lower),
                      'out/удалённые из БГ.txt')
    save_socket_bs_dicts_to_txt(socket_group_word_form_list,
                                'out/БГ 28.01.21.txt')


if __name__ == '__main__':
    remove_from_bg()
