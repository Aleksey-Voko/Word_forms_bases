from BS.utils import (read_src_bs, save_list_to_file, read_src_socket_bs,
                      get_socket_word_form)


def get_spec_note():
    word_forms_bases = list(read_src_bs('src_dict/БС 23.02.21.txt'))

    spec_note_bs = []

    for title_form in [x.title_word_form for x in word_forms_bases]:
        title_note = title_form.note
        if title_note:
            if title_note.startswith('.* <'):
                if ' ' not in title_note[5:]:
                    spec_note_bs.append(str(title_form))

    save_list_to_file(spec_note_bs, 'out/Спец. прим. БС. 1 слово.txt')


def get_replays_in_groups():
    socket_group_list = read_src_socket_bs(
        'src_dict/БГ 23.02.21.txt')

    replays_in_groups = []

    for socket_group in socket_group_list:
        socket_word_forms = socket_group.socket_word_forms
        socket_word_forms = [x for x in socket_word_forms if not x.invisible]
        socket_names = [x.name for x in socket_word_forms]
        replays_names = sorted(list(set(
            [x for x in socket_names if socket_names.count(x) > 1]
        )))

        if replays_names:
            replays_in_groups.append(str(socket_group.socket_word_forms[0]))
            for sub_group in socket_group.sub_groups:
                flag = True
                for word_form in sub_group.socket_word_forms:
                    if word_form.name in replays_names:
                        if flag:
                            replays_in_groups.append(' '.join([
                                '!',
                                str(sub_group.title_word_form),
                            ]))
                            flag = False
                        replays_in_groups.append(str(word_form))

            replays_in_groups.append('')

    save_list_to_file(replays_in_groups, 'out/Повторы в группах.txt')


def get_bg_note():
    socket_group_list = read_src_socket_bs('src_dict/БГ 23.02.21.txt')

    bg_notes = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms[1:]:
                if word_form.note:
                    print(word_form)
                    bg_notes.append(str(word_form))

    save_list_to_file(
        sorted(bg_notes, key=lambda x: x.replace('*', '').strip().lower()),
        'out/Пояснительные примечания БГ, не-ЗС.txt'
    )


def parsing_replays_in_groups():
    word_forms = []

    with open('out/Повторы в группах.txt', encoding='utf-8') as f_in:
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
