from BS.utils import (get_string_list_from_file, get_bs_title_word_form,
                      get_socket_word_form, save_list_to_file)


def compare_replays_in_groups():
    homonyms_bs = get_string_list_from_file('src_dict/Омонимы БС.txt')

    bs_str_forms = []

    for homonym in homonyms_bs:
        title_form = get_bs_title_word_form(homonym)
        string_form = ' '.join(filter(
            None,
            [
                title_form.name,
                title_form.idf,
                ' '.join(title_form.info),
                title_form.note.replace('.*', '').strip()
            ]))
        bs_str_forms.append(string_form)

    relevant = []
    not_relevant = []

    with open('src_dict/Повторы в группах.txt', encoding='utf-8') as f_in:
        groups = (x.strip() for x in f_in.read().split('\n\n'))
        for group in groups:
            for line in group.split('\n')[1:]:
                if not line.startswith('!'):
                    word_form = get_socket_word_form(line)
                    line_form = ' '.join(filter(None, [
                        word_form.name,
                        word_form.idf,
                        ' '.join(word_form.info),
                        word_form.note.replace('*', '').strip(),
                    ]))
                    if line_form in bs_str_forms:
                        relevant.append(line)
                    else:
                        not_relevant.append(line)

    save_list_to_file(
        sorted(relevant, key=lambda x: x.replace('*', '').strip().lower()),
        'out/19.1 Совпадающие.txt'
    )

    save_list_to_file(
        sorted(not_relevant, key=lambda x: x.replace('*', '').strip().lower()),
        'out/19.1 Не совпадающие.txt'
    )


if __name__ == '__main__':
    compare_replays_in_groups()
