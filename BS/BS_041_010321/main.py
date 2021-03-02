from collections import Counter

from BS.utils import (get_string_list_from_file, get_bs_title_word_form,
                      get_socket_word_form, save_list_to_file,
                      read_src_socket_bs)


def compare_homonyms_spec_note():
    homonyms_bg = get_string_list_from_file('src_dict/Омонимы БГ.txt')

    homonyms_bg_str_form = []

    for homonyms in homonyms_bg:
        socket_form = get_socket_word_form(homonyms)

        spec_note = socket_form.spec_note.replace('< ', '')
        spec_note_socket_form = get_socket_word_form(spec_note)
        spec_note = ' '.join(filter(None, [
            spec_note_socket_form.invisible,
            spec_note_socket_form.name,
            spec_note_socket_form.root_index,
            spec_note_socket_form.idf,
            ' '.join(spec_note_socket_form.info),
            spec_note_socket_form.note,
        ]))

        string_form = ' '.join(filter(
            None, [
                socket_form.name,
                socket_form.idf,
                ' '.join(socket_form.info),
                spec_note,
            ]
        ))
        homonyms_bg_str_form.append(string_form)

    homonyms_spec_note = get_string_list_from_file(
        'src_dict/О-мы БС спец. прим. не совпадают с Повторами.txt')

    homonyms_spec_note_relevant = []
    homonyms_spec_note_not_relevant = []

    for homonym in homonyms_spec_note:
        title_form = get_bs_title_word_form(homonym)
        string_form = ' '.join(filter(
            None,
            [
                title_form.name,
                title_form.idf,
                ' '.join(title_form.info),
                title_form.note.replace('.* < ', ''),
            ]
        ))
        if string_form in homonyms_bg_str_form:
            homonyms_spec_note_relevant.append(homonym)
        else:
            homonyms_spec_note_not_relevant.append(homonym)

    save_list_to_file(homonyms_spec_note_relevant,
                      'out/О-мы БС спец. прим. совпадают с О-мами БГ.txt')
    save_list_to_file(homonyms_spec_note_not_relevant,
                      'out/О-мы БС спец. прим. не совпадают с О-мами БГ.txt')


def compare_homonyms():
    homonyms_bg = get_string_list_from_file('src_dict/Омонимы БГ.txt')

    homonyms_bg_str_form = []

    for homonyms in homonyms_bg:
        socket_form = get_socket_word_form(homonyms)
        string_form = ' '.join(filter(
            None, [
                socket_form.name,
                socket_form.idf,
                ' '.join(socket_form.info),
                socket_form.note
            ]
        ))
        homonyms_bg_str_form.append(string_form)

    homonyms_bs = get_string_list_from_file(
        'src_dict/О-мы БС не совпадают с Повторами.txt')

    homonyms_bs_relevant = []
    homonyms_bs_not_relevant = []

    for homonym in homonyms_bs:
        title_form = get_bs_title_word_form(homonym)
        string_form = ' '.join(filter(
            None,
            [
                title_form.name,
                title_form.idf,
                ' '.join(title_form.info),
                title_form.note.replace('.* ', '* '),
            ]
        ))
        if string_form in homonyms_bg_str_form:
            homonyms_bs_relevant.append(homonym)
        else:
            homonyms_bs_not_relevant.append(homonym)

    save_list_to_file(homonyms_bs_relevant,
                      'out/О-мы БС совпадают с О-мами БГ.txt')
    save_list_to_file(homonyms_bs_not_relevant,
                      'out/О-мы БС не совпадают с О-мами БГ.txt')


def get_multirooted_homonyms():
    socket_group_list = list(read_src_socket_bs(
        'src_dict/БГ 23.02.21.txt'))

    socket_names = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if not word_form.invisible:
                    socket_names.append(
                        word_form.name.replace('*', '').strip()
                    )

    socket_names = [x for x, y in Counter(socket_names).items() if y > 1]
    socket_names = sorted(list(set(socket_names)))

    multirooted_homonyms = []

    for socket_name in socket_names:
        multirooted = []
        single_root = []

        for socket_group in socket_group_list:
            for sub_group in socket_group.sub_groups:
                sub_group_title_form = sub_group.title_word_form
                for word_form in sub_group.socket_word_forms:
                    if word_form.name == socket_name:
                        word_form.sub_group_title_form = sub_group_title_form
                        if word_form.root_index:
                            multirooted.append(word_form)
                        else:
                            single_root.append(word_form)

        if multirooted and single_root:
            for item in multirooted:
                multirooted_homonyms.append(
                    ' < '.join([str(item), str(item.sub_group_title_form)]),
                )
            for item in single_root:
                multirooted_homonyms.append(
                    ' < '.join([str(item), str(item.sub_group_title_form)]),
                )

    multirooted_homonyms = sorted(
        multirooted_homonyms, key=lambda x: x.lower())

    save_list_to_file(multirooted_homonyms,
                      'out/Омонимы - многокорневые и немногокорневые.txt')


if __name__ == '__main__':
    compare_homonyms_spec_note()
