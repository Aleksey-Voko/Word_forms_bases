from BS.utils import (get_string_list_from_file, get_bs_title_word_form,
                      get_socket_word_form, save_list_to_file)


def get_homonyms_bs():
    replays_in_groups_spec_note = []  # (".* <")
    replays_in_groups = []  # (".*")

    with open('src_dict/Повторы в группах.txt', encoding='utf-8') as f_in:
        groups = (x.strip() for x in f_in.read().split('\n\n'))
        for group in groups:
            for line in group.split('\n')[1:]:
                if line.startswith('!'):
                    title_word_sub_group = line
                    title_name_sub_group = str(get_socket_word_form(
                        title_word_sub_group.replace('!', '').strip()))
                else:
                    word_form = get_socket_word_form(line)
                    replays_in_groups_spec_note.append(
                        ' '.join(filter(None, [
                            word_form.name,
                            word_form.idf,
                            ' '.join(word_form.info),
                            title_name_sub_group,
                        ]))
                    )
                    replays_in_groups.append(
                        ' '.join(filter(None, [
                            word_form.name,
                            word_form.idf,
                            ' '.join(word_form.info),
                            word_form.note.replace('*', '').strip(),
                        ]))
                    )

    homonyms_bs = get_string_list_from_file('src_dict/Омонимы БС.txt')

    homonyms_spec_note_relevant = []
    homonyms_spec_note_not_relevant = []
    homonyms_relevant = []
    homonyms_not_relevant = []

    for homonym in homonyms_bs:
        title_form = get_bs_title_word_form(homonym)

        # имеющие специальное примечание (".* <")
        if title_form.note.startswith('.* <'):
            string_form = ' '.join(filter(
                None,
                [
                    title_form.name,
                    title_form.idf,
                    ' '.join(title_form.info),
                    title_form.note.replace('.* <', '').strip()
                ]))
            if string_form in replays_in_groups_spec_note:
                homonyms_spec_note_relevant.append(homonym)
            else:
                homonyms_spec_note_not_relevant.append(homonym)

        # НЕ имеющие специальное примечание (".* <")
        else:
            string_form = ' '.join(filter(
                None,
                [
                    title_form.name,
                    title_form.idf,
                    ' '.join(title_form.info),
                    title_form.note.replace('.*', '').strip()
                ]))
            if string_form in replays_in_groups:
                homonyms_relevant.append(homonym)
            else:
                homonyms_not_relevant.append(homonym)

    save_list_to_file(homonyms_spec_note_relevant,
                      'out/О-мы БС спец. прим. совпадают с Повторами.txt')
    save_list_to_file(homonyms_spec_note_not_relevant,
                      'out/О-мы БС спец. прим. не совпадают с Повторами.txt')
    save_list_to_file(homonyms_relevant,
                      'out/О-мы БС совпадают с Повторами.txt')
    save_list_to_file(homonyms_not_relevant,
                      'out/О-мы БС не совпадают с Повторами.txt')


if __name__ == '__main__':
    get_homonyms_bs()
