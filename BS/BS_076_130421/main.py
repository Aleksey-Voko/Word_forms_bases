from collections import Counter
from pprint import pprint

from BS.utils import (read_src_socket_bs, save_list_to_file,
                      get_socket_word_form, get_dicts_from_csv_file)


def get_homonyms_bg():
    socket_group_list = list(read_src_socket_bs(
        'src_dict/БГ 10.04.21.txt'))

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

    all_homonyms = []

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
                            all_homonyms.append(str(word_form))
                        else:
                            all_homonyms.append(' < '.join([
                                str(word_form),
                                str(title_word_form),
                            ]))

    replays_homonyms = [get_socket_word_form(x).name for x in all_homonyms]
    replays_homonyms = [x for x in replays_homonyms
                        if replays_homonyms.count(x) > 1]

    homonyms = []
    homonymous_repetitions = []

    for homonym in all_homonyms:
        if get_socket_word_form(homonym).name in replays_homonyms:
            homonyms.append(homonym)
        else:
            homonymous_repetitions.append(homonym)

    homonyms = sorted(homonyms,
                      key=lambda x: x.replace('*', '').strip().lower())
    homonymous_repetitions = sorted(homonymous_repetitions,
                                    key=lambda x:
                                    x.replace('*', '').strip().lower())

    save_list_to_file(homonyms, 'out/Омонимы БГ.txt')
    save_list_to_file(homonymous_repetitions,
                      'out/Слова, омонимичные повторам в группе.txt')


def get_homonymous_multi_rooted():
    multi_root_words = get_dicts_from_csv_file(
        'src_dict/Многокорневые слова.csv')

    multi_root_names = []
    for multi_root_word in multi_root_words:
        for root_index_key in list(multi_root_word):
            if multi_root_word[root_index_key]:
                multi_root_names.append(
                    get_socket_word_form(multi_root_word[root_index_key]).name
                )

    socket_group_list = list(read_src_socket_bs(
        'src_dict/БГ 10.04.21.txt'))

    homonymous_multi_rooted = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            title_word_form = sub_group.title_word_form
            for word_form in sub_group.socket_word_forms:
                if (
                        not word_form.invisible
                        and not word_form.root_index
                ):
                    if word_form.name in multi_root_names:
                        print(word_form)
                        if str(word_form) == str(title_word_form):
                            homonymous_multi_rooted.append(str(word_form))
                        else:
                            homonymous_multi_rooted.append(' < '.join([
                                str(word_form),
                                str(title_word_form),
                            ]))

    homonymous_multi_rooted = sorted(homonymous_multi_rooted,
                                     key=lambda x:
                                     x.replace('*', '').strip().lower())
    save_list_to_file(homonymous_multi_rooted,
                      'out/Слова, омонимичные многокорневым словам.txt')


if __name__ == '__main__':
    get_homonymous_multi_rooted()
