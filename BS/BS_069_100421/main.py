import pandas as pd

from BS.utils import (read_src_socket_bs, get_dicts_from_csv_file,
                      save_list_to_file, read_src_bs, get_socket_word_form,
                      get_string_list_from_file, get_bs_title_word_form)


def get_root_index_data_set():
    socket_group_word_form_list = read_src_socket_bs(
        'src_dict/БГ 10.04.21.txt')

    root_index_ds = {
        '2': [],
        '2!': [],
        '2*': [],
        '3': [],
        '3!': [],
        '3*': [],
        '3**': [],
        '4': [],
        '4!': [],
        '4*': [],
        '4**': [],
        '5': [],
        '5!': [],
        '5*': [],
        '5**': [],
        '6': [],
        '6!': [],
        '6*': [],
        '6**': [],
        '7': [],
        '7!': [],
        '7*': [],
        '7**': [],
    }

    for socket_group_word_form in socket_group_word_form_list:
        for socket_word_form in socket_group_word_form.socket_word_forms:
            root_index = socket_word_form.root_index
            if root_index and not socket_word_form.invisible:
                root_index_ds[root_index].append(str(socket_word_form))

    for k in root_index_ds:
        root_index_ds[k] = sorted(list(
            set(root_index_ds[k])),
            key=lambda x: x.replace('*', '').lower().strip()
        )

    ds = []
    for k in root_index_ds:
        for word_form in root_index_ds[k]:
            ds.append({
                'root_index': k,
                'word_form': word_form,
            })

    df = pd.DataFrame(ds)
    res_df = (df
              .assign(idx=df.groupby("root_index").cumcount())
              .pivot_table(index="idx", columns="root_index",
                           values="word_form", aggfunc="first"))
    res_df.to_csv('out/Многокорневые слова.csv')


def check_replays():
    multi_root_words = get_dicts_from_csv_file(
        'out/Многокорневые слова.csv')

    socket_group_word_form_list = list(read_src_socket_bs(
        'src_dict/БГ 10.04.21.txt'))

    root_index_ds = {
        '2': [],
        '2!': [],
        '2*': [],
        '3': [],
        '3!': [],
        '3*': [],
        '3**': [],
        '4': [],
        '4!': [],
        '4*': [],
        '4**': [],
        '5': [],
        '5!': [],
        '5*': [],
        '5**': [],
        '6': [],
        '6!': [],
        '6*': [],
        '6**': [],
        '7': [],
        '7!': [],
        '7*': [],
        '7**': [],
    }

    count_index = {
        '2': 2,
        '2!': 2,
        '2*': 1,
        '3': 3,
        '3!': 3,
        '3*': 2,
        '3**': 1,
        '4': 4,
        '4!': 4,
        '4*': 3,
        '4**': 2,
        '5': 5,
        '5!': 5,
        '5*': 4,
        '5**': 3,
        '6': 6,
        '6!': 6,
        '6*': 5,
        '6**': 4,
        '7': 7,
        '7!': 7,
        '7*': 6,
        '7**': 5,
    }

    incorrect_replays = []

    for multi_root_word in multi_root_words:
        for root_index_key in list(multi_root_word)[1:]:
            if multi_root_word[root_index_key]:
                root_index_ds[root_index_key].append(
                    multi_root_word[root_index_key]
                )

    for root_index in root_index_ds:
        for multi_root_word in root_index_ds[root_index]:
            count_word = 0
            for socket_group_word_form in socket_group_word_form_list:
                for socket_word_form in socket_group_word_form.socket_word_forms:
                    if multi_root_word == str(socket_word_form):
                        count_word += 1
            if count_word != count_index[root_index]:
                print(multi_root_word)
                incorrect_replays.append(f'{multi_root_word} - {count_word}')

    save_list_to_file(incorrect_replays, 'out/Не корректные повторы.txt')


def find_all_multi_rooted_words_from_bs():
    multi_root_words = get_dicts_from_csv_file(
        'out/Многокорневые слова.csv')

    word_forms_bases = list(read_src_bs('src_dict/БС 06.04.21.txt'))

    multi_root_bg_forms = []

    for multi_root_word in multi_root_words:
        for root_index_key in list(multi_root_word)[1:]:
            if multi_root_word[root_index_key]:
                socket_form = get_socket_word_form(
                    multi_root_word[root_index_key]
                )
                multi_root_bg_forms.append(
                    ' '.join(filter(
                        None,
                        [
                            socket_form.name,
                            socket_form.idf,
                            ' '.join(socket_form.info),
                            socket_form.note.replace('* ', ''),
                        ])))

    multi_root_bs_forms = []

    for group_word_form in word_forms_bases:
        title_form = group_word_form.title_word_form
        src_title_form = ' '.join(filter(
            None,
            [
                title_form.name,
                title_form.idf,
                ' '.join(title_form.info),
                (title_form.note.replace('.* ', '')
                 if '<' not in title_form.note else None),
            ]))
        if src_title_form in multi_root_bg_forms:
            print(title_form)
            multi_root_bs_forms.append(str(title_form))

    multi_root_bs_forms = sorted(
        multi_root_bs_forms,
        key=lambda x: x.replace('*', '').lower().strip()
    )

    save_list_to_file(multi_root_bs_forms, 'out/Многокорневые слова БС.txt')


def check_socket_bs():
    multi_root_words = get_dicts_from_csv_file(
        'out/Многокорневые слова.csv')
    multi_root_bs_forms = get_string_list_from_file(
        'out/Многокорневые слова БС.txt')
    multi_root_bs_forms = [get_bs_title_word_form(x).name for x in multi_root_bs_forms]

    not_found_in_bs = []

    for multi_root_word in multi_root_words:
        for root_index_key in list(multi_root_word)[1:]:
            if multi_root_word[root_index_key]:
                socket_form = get_socket_word_form(
                    multi_root_word[root_index_key]
                )
                if socket_form.name not in multi_root_bs_forms:
                    print(socket_form)
                    not_found_in_bs.append(str(socket_form))

    save_list_to_file(not_found_in_bs, 'out/Не найденные в БС.txt')


if __name__ == '__main__':
    check_socket_bs()
