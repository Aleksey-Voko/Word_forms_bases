from BS.utils import read_src_socket_bs, save_list_to_file, get_dicts_from_csv_file, read_src_bs, get_socket_word_form


def check_root_index():
    socket_group_word_form_list = read_src_socket_bs(
        'src_dict/БГ 11.02.21.txt')

    title_word_root_index_list = []

    for socket_group_form in socket_group_word_form_list:
        for socket_sub_group_form in socket_group_form.sub_groups:
            if len(socket_sub_group_form.socket_word_forms) >= 2:
                form_0, form_1 = socket_sub_group_form.socket_word_forms[:2]
                if form_0.root_index and not form_1.root_index:
                    print(form_0)
                    title_word_root_index_list.append(str(form_0))

    save_list_to_file(
        sorted(title_word_root_index_list, key=lambda x: x.lower()),
        'out/ЗС корневой индекс.txt'
    )


def find_all_multi_rooted_words_from_bs():
    multi_root_words = get_dicts_from_csv_file(
        'src_dict/Многокорневые слова.csv')

    word_forms_bases = list(read_src_bs('src_dict/БС 03.02.21.txt'))

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
                            socket_form.note.replace('* ', '')
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
                title_form.note.replace('.* ', '')
            ]))
        if src_title_form in multi_root_bg_forms:
            print(title_form)
            multi_root_bs_forms.append(str(title_form))

    multi_root_bs_forms = sorted(
        multi_root_bs_forms,
        key=lambda x: x.replace('*', '').lower().strip()
    )

    save_list_to_file(multi_root_bs_forms, 'out/Многокорневые слова БС.txt')


def get_mismatched_notes():
    socket_group_word_form_list = list(read_src_socket_bs(
        'src_dict/БГ 11.02.21.txt'))
    word_forms_bases = read_src_bs('src_dict/БС 03.02.21.txt')

    mismatched_notes = []

    for group_word_form in word_forms_bases:
        title_form = group_word_form.title_word_form

        for socket_group_form in socket_group_word_form_list:
            for socket_sub_group_form in socket_group_form.sub_groups:
                for socket_form in socket_sub_group_form.socket_word_forms:
                    if (
                            title_form.name == socket_form.name
                            and title_form.idf == socket_form.idf
                            and ' '.join(title_form.info) == ' '.join(socket_form.info)
                            and title_form.note.replace('.* ', '') != socket_form.note.replace('* ', '')
                    ):
                        mismatched_notes.append(str(title_form))

    save_list_to_file(mismatched_notes, 'out/Несовпадающие примечания.txt')


if __name__ == '__main__':
    get_mismatched_notes()
