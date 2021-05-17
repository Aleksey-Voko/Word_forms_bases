from BS.utils import read_src_bs, save_bs_dicts_to_txt, read_src_socket_bs, save_socket_bs_dicts_to_txt


def change_template_bs():
    word_forms_bases = list(read_src_bs('src_dict/БС 15.05.21.txt'))
    for group in word_forms_bases:
        title_form = group.title_word_form
        if all([
                title_form.idf == '.СеИ',
                title_form.name.endswith('ий'),
                title_form.name not in ('вий', 'змий', 'кий'),
        ]):
            for count, identifier in enumerate(title_form.info):
                if identifier == 'мнI2':
                    title_form.info[count] = 'мнI2**'

    save_bs_dicts_to_txt(sorted(word_forms_bases), 'out/БС 17.05.21.txt')


def change_template_bg():
    socket_group_list = list(read_src_socket_bs('src_dict/БГ 15.05.21.txt'))

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if all([
                    word_form.idf == '.СеИ',
                    word_form.name.endswith('ий'),
                    word_form.name not in ('вий', 'змий', 'кий'),
                ]):
                    for count, identifier in enumerate(word_form.info):
                        if identifier == 'мнI2':
                            word_form.info[count] = 'мнI2**'

    save_socket_bs_dicts_to_txt(socket_group_list, 'out/БГ 17.05.21.txt')


if __name__ == '__main__':
    change_template_bg()
