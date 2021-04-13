from BS.utils import (get_string_list_from_file, get_bs_title_word_form,
                      save_list_to_file)


def get_homonyms_bs():
    homonymous_repetitions = list(get_string_list_from_file(
        'src_dict/Слова, омонимичные повторам в группе.txt'))
    homonyms_bs = get_string_list_from_file('src_dict/Омонимы БС.txt')

    homonyms_spec_note_relevant = []
    homonyms_spec_note_not_relevant = []
    homonyms_relevant = []
    homonyms_not_relevant = []

    for homonym in homonyms_bs:
        title_form = get_bs_title_word_form(homonym)

        # без примечаний
        if not title_form.note:
            string_form = ' '.join(filter(
                None,
                [
                    title_form.name,
                    title_form.idf,
                    ' '.join(title_form.info),
                    title_form.note.replace('.*', '').strip()
                ]))
            if string_form in homonymous_repetitions:
                homonyms_relevant.append(homonym)
            else:
                homonyms_not_relevant.append(homonym)

        else:
            # имеющие специальное примечание (".* <")
            if title_form.note.startswith('.* <'):
                string_form = ' '.join(filter(
                    None,
                    [
                        title_form.name,
                        title_form.idf,
                        ' '.join(title_form.info),
                        title_form.note.replace('.* <', '<').strip()
                    ]))
                if string_form in homonymous_repetitions:
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
                        title_form.note.replace('.*', '*').strip()
                    ]))
                if string_form in homonymous_repetitions:
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
