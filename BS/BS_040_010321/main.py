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
        print(title_form.name, title_form.note)
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


def get_homonyms_bg():
    socket_group_list = list(read_src_socket_bs(
        'src_dict/БГ 23.02.21.txt'))

    socket_names = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if (
                        not word_form.invisible
                        and not word_form.root_index
                ):
                    socket_names.append(
                        word_form.name.replace('*', '').strip()
                    )

    socket_names = [x for x, y in Counter(socket_names).items() if y > 1]
    socket_names = sorted(list(set(socket_names)))

    homonyms = []

    for socket_group in socket_group_list:
        group_names = [
            x.name.replace('*', '').strip()
            for x in socket_group.socket_word_forms if not x.invisible
        ]

        for sub_group in socket_group.sub_groups:
            title_word_form = sub_group.title_word_form
            for word_form in sub_group.socket_word_forms:
                if (
                        not word_form.invisible
                        and not word_form.root_index
                ):
                    raw_name = word_form.name.replace('*', '').strip()
                    if (
                            group_names.count(raw_name) == 1
                            and raw_name in socket_names):
                        if str(word_form) == str(title_word_form):
                            homonyms.append(str(word_form))
                        else:
                            homonyms.append(' < '.join([
                                str(word_form),
                                str(title_word_form),
                            ]))

    sort_homonyms = sorted(homonyms,
                           key=lambda x: x.replace('*', '').strip().lower())
    save_list_to_file(sort_homonyms, 'out/Омонимы БГ.txt')


def get_multirooted_homonyms():
    homonyms = list(get_string_list_from_file('out/Омонимы БГ.txt'))

    homonym_names = []

    for homonym in homonyms:
        socket_form = get_socket_word_form(homonym)
        homonym_names.append(socket_form.name)

    homonym_names = sorted(list(set(homonym_names)), key=lambda x: x.lower())

    multirooted_homonyms = []

    for name in homonym_names:
        socket_forms = []
        for homonym in homonyms:
            socket_form = get_socket_word_form(homonym)
            if socket_form.name == name:
                socket_forms.append(socket_form)

        for form in socket_forms:
            multirooted = []
            single_root = []

            if form.root_index:
                multirooted.append(form)
            else:
                single_root.append(form)

            if multirooted and single_root:
                for item in multirooted:
                    multirooted_homonyms.append(str(item))
                for item in single_root:
                    multirooted_homonyms.append(str(item))

    multirooted_homonyms = sorted(
        multirooted_homonyms, key=lambda x: x.lower())
    save_list_to_file(multirooted_homonyms,
                      'out/Омонимы - многокорневые и немногокорневые.txt')


if __name__ == '__main__':
    get_multirooted_homonyms()
