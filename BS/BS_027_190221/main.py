from BS.utils import save_list_to_file, get_string_list_from_file, get_bs_title_word_form


def get_replays_in_groups():
    replays_in_groups = []

    with open('src_dict/Повторы в группах.txt', encoding='utf-8') as f_in:
        groups = (x.strip() for x in f_in.read().split('\n\n'))
        for group in groups:
            for line in group.split('\n')[1:]:
                if not line.startswith('!'):
                    replays_in_groups.append(line)

    replays_in_groups = sorted(
        list(set(replays_in_groups)),
        key=lambda x: x.replace('*', '').strip().lower()
    )

    save_list_to_file(replays_in_groups,
                      'out/Повторы в группах (без повторов).txt')


def get_remaining_repetitions():
    homonyms = []

    for line in get_string_list_from_file(
            'src_dict/О-мы БС спец. прим. совпадают с Повторами.txt'):
        bs_form = get_bs_title_word_form(line)
        homonyms.append(' '.join(filter(None, [
            bs_form.name,
            bs_form.idf,
            ' '.join(bs_form.info),
        ])))

    for line in get_string_list_from_file(
            'src_dict/О-мы БС совпадают с Повторами.txt'):
        bs_form = get_bs_title_word_form(line)
        homonyms.append(' '.join(filter(None, [
            bs_form.name,
            bs_form.idf,
            ' '.join(bs_form.info),
            bs_form.note
        ])))

    remaining_repetitions = []

    replays_in_groups = get_string_list_from_file(
        'out/Повторы в группах (без повторов).txt')
    for replay in replays_in_groups:
        if replay not in homonyms:
            remaining_repetitions.append(replay)

    save_list_to_file(remaining_repetitions, 'out/Повторы ост.txt')


def get_remaining_homonyms():
    remaining_homonyms = list(get_string_list_from_file(
        'src_dict/О-мы БС спец. прим. не совпадают с Повторами.txt'))
    remaining_homonyms += list(get_string_list_from_file(
        'src_dict/О-мы БС не совпадают с Повторами.txt'))
    save_list_to_file(
        sorted(remaining_homonyms,
               key=lambda x: x.replace('*', '').strip().lower()),
        'out/О-мы БС ост.txt'
    )


if __name__ == '__main__':
    get_remaining_homonyms()
