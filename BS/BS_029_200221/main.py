from BS.utils import get_socket_word_form, save_list_to_file


def parsing_replays_in_groups():
    word_forms = []

    with open('src_dict/Повторы в группах.txt', encoding='utf-8') as f_in:
        groups = (x.strip() for x in f_in.read().split('\n\n'))
        for group in groups:
            for line in group.split('\n')[1:]:
                if not line.startswith('!'):
                    word_forms.append(
                        get_socket_word_form(line)
                    )

    clear_lines = [
        ' '.join(filter(None, [
            x.name,
            x.idf,
            ' '.join(x.info)
        ]))
        for x in word_forms
    ]

    repeating_clear_lines = [x for x in clear_lines
                             if clear_lines.count(x) > 1]

    repeating_lines = []
    unique_lines = []

    for form in word_forms:
        clear_form = ' '.join(filter(None, [
            form.name,
            form.idf,
            ' '.join(form.info)
        ]))
        if clear_form in repeating_clear_lines:
            repeating_lines.append(str(form))
        else:
            unique_lines.append(str(form))

    save_list_to_file(
        sorted(repeating_lines,
               key=lambda x: x.replace('*', '').strip().lower()),
        'out/Повторы в группах. Повторяющиеся строки.txt'
    )

    save_list_to_file(
        sorted(unique_lines,
               key=lambda x: x.replace('*', '').strip().lower()),
        'out/Повторы в группах. Уникальные строки.txt'
    )


if __name__ == '__main__':
    parsing_replays_in_groups()
