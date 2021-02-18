from pprint import pprint

from BS.utils import get_socket_word_form, get_string_list_from_file, get_bs_title_word_form, save_list_to_file


def compare_replays_in_groups():
    replays_in_groups = []

    with open('src_dict/Повторы в группах.txt', encoding='utf-8') as f_in:
        groups = (x.strip() for x in f_in.read().split('\n\n'))
        for group in groups:
            for line in group.split('\n')[1:]:
                if not line.startswith('!'):
                    replays_in_groups.append(get_socket_word_form(line))

    replays_in_groups = [
        ' '.join(filter(
            None,
            [
                x.name,
                x.idf,
                ' '.join(x.info),
                x.note.replace('*', '').strip(),
            ]))
        for x in replays_in_groups
    ]

    homonyms_bs = get_string_list_from_file('src_dict/Омонимы БС.txt')
    inequable_bs = []
    inequable_string_form_bs = []
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

        if string_form not in replays_in_groups:
            inequable_bs.append(homonym)
            inequable_string_form_bs.append(string_form)

    save_list_to_file(
        sorted(inequable_bs, key=lambda x: x.replace('*', '').strip().lower()),
        'out/19.1.txt'
    )

    homonyms_bg = get_string_list_from_file('src_dict/Омонимы БГ.txt')
    inequable_bg = []
    for homonym in homonyms_bg:
        if homonym not in inequable_string_form_bs:
            inequable_bg.append(homonym)

    save_list_to_file(
        sorted(inequable_bg, key=lambda x: x.replace('*', '').strip().lower()),
        'out/19.2.txt'
    )


if __name__ == '__main__':
    compare_replays_in_groups()
