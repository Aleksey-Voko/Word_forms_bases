from BS.utils import (read_src_bs, save_bs_dicts_to_txt,
                      read_src_socket_bs,
                      save_socket_bs_dicts_to_txt)


def add_groups_to_bs():
    """
    7. Соблюдая алфавитный порядок ЗС в БС,
    добавить в док-т БС 24.01.21.txt группы из док-та
    Добавить группы в БС. Прил-ные.txt .
    """
    word_forms_bases = list(read_src_bs('src_dict/БС 24.01.21.txt'))
    adjectives = list(read_src_bs(
        'src_dict/Добавить группы в БС. Прил-ные.txt', encoding='utf-8'))
    word_forms_bases += adjectives
    save_bs_dicts_to_txt(sorted(word_forms_bases), 'out/БС 27.01.21.txt')


def add_spec_info_to_bg():
    """
    8. Для всех ЗС групп из док-та Добавить группы в БС. Прил-ные.txt
    сделать следующее:
    8.1. скопировать ВСЮ спец. информацию у такого ЗС группы,
    8.2. найти такое слово в док-те БГ 24.01.21.txt и
    8.3. добавить скопированную спец. информацию к найденному слову.
    """
    socket_group_word_form_list = list(
        read_src_socket_bs('src_dict/БГ 24.01.21.txt'))

    adjectives = list(read_src_bs(
        'src_dict/Добавить группы в БС. Прил-ные.txt', encoding='utf-8'))

    for adj in adjectives:
        title_word_form = adj.title_word_form
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
                                'out/БГ 27.01.21.txt')


if __name__ == '__main__':
    add_spec_info_to_bg()
