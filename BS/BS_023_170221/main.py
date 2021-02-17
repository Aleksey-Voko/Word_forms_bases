from collections import Counter

from BS.utils import (read_src_socket_bs, save_list_to_file, read_src_bs)


def get_homonyms_bg():
    socket_group_list = list(read_src_socket_bs(
        'src_dict/БГ 17.02.21.txt'))

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

    loner_names = [x.split()[0] for x in sort_homonyms]
    loner_homonyms = [x for x in sort_homonyms
                      if loner_names.count(x.split()[0]) == 1]
    save_list_to_file(loner_homonyms, 'out/Единичные омонимы.txt')


if __name__ == '__main__':
    get_homonyms_bg()
