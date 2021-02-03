from BS.utils import (read_src_bs, save_bs_dicts_to_txt,
                      read_src_socket_bs,
                      save_socket_bs_dicts_to_txt)


def add_groups_to_bs():
    """
    11. Соблюдая алфавитный порядок ЗС в БС, добавить в док-т БС 31.01.txt
    группы из док-та Добавить группы в БС. Глаголы изм.txt .
    """
    word_forms_bases = list(read_src_bs('src_dict/БС 31.01.txt'))
    verbs = list(read_src_bs(
        'src_dict/Добавить группы в БС. Глаголы изм.txt', encoding='utf-8'))
    word_forms_bases += verbs
    save_bs_dicts_to_txt(sorted(word_forms_bases), 'out/БС 03.02.21.txt')


def add_spec_info_to_bg():
    """
    12. Для всех ЗС групп из док-та Добавить группы в БС. Глаголы изм.txt
    сделать следующее:
    12.1. скопировать ВСЮ спец. информацию у такого ЗС группы,
    12.2. найти такое слово в док-те БГ 30.01.21.txt и
    12.3. добавить скопированную спец. информацию к найденному слову.
    """
    socket_group_word_form_list = list(
        read_src_socket_bs('src_dict/БГ 30.01.21.txt'))

    verbs = list(read_src_bs(
        'src_dict/Добавить группы в БС. Глаголы изм.txt', encoding='utf-8'))

    for verb in verbs:
        title_word_form = verb.title_word_form
        idf = title_word_form.idf
        info = title_word_form.info
        for socket_group_word_form in socket_group_word_form_list:
            for socket_word_form in socket_group_word_form.socket_word_forms:
                s_socket_name = socket_word_form.name.replace('*', '').strip()
                s_title_name = title_word_form.name.replace('*', '').strip()
                if s_socket_name == s_title_name:
                    print(socket_word_form.name)
                    socket_word_form.idf = idf
                    socket_word_form.info = info

    save_socket_bs_dicts_to_txt(socket_group_word_form_list,
                                'out/БГ 03.02.21.txt')


if __name__ == '__main__':
    add_spec_info_to_bg()
