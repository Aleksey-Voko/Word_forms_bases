from BS.utils import (get_string_list_from_file, get_bs_title_word_form,
                      get_socket_word_form, save_list_to_file)


def compare_homonyms_spec_note():
    homonyms_bg = get_string_list_from_file(
        'src_dict/Омонимы БГ без этим. примечаний.txt')

    homonyms_bg_str_form = []

    for homonyms in homonyms_bg:
        socket_form = get_socket_word_form(homonyms)
        string_form = ' '.join(filter(
            None, [
                socket_form.name,
                socket_form.idf,
                ' '.join(socket_form.info),
                socket_form.spec_note.replace('< ', '')
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
    homonyms_bg = get_string_list_from_file(
        'src_dict/Омонимы БГ без этим. примечаний.txt')

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


if __name__ == '__main__':
    compare_homonyms()
