from BS.utils import read_src_socket_bs, save_list_to_file, read_src_bs


def get_adjusted_participles_bg():
    socket_group_word_form_list = read_src_socket_bs('src_dict/БГ 28.01.21.txt')

    adjusted_participles_list = []

    for group in socket_group_word_form_list:
        for sub_group in group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if (
                        word_form.name.startswith('*')
                        and not word_form.name.startswith('* ')
                ):
                    adjusted_participles_list.append(str(word_form))
                    print(word_form)

    save_list_to_file(sorted(adjusted_participles_list,
                             key=lambda x: x.replace('*', '').strip().lower()),
                      'out/Адъектированные причастия БГ.txt'
                      )


def get_adjusted_participles_bs():
    word_forms_bases = read_src_bs('src_dict/БС 28.01.21.txt')

    adjusted_participles_list = []

    for group_word_form in word_forms_bases:
        title_word_form = group_word_form.title_word_form
        if title_word_form.name.startswith('*'):
            print(title_word_form)
            adjusted_participles_list.append(str(title_word_form))

    save_list_to_file(adjusted_participles_list,
                      'out/Адъектированные причастия БС.txt')


if __name__ == '__main__':
    get_adjusted_participles_bs()
