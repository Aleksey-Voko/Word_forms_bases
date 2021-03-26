from BS.utils import read_src_bs, get_string_list_from_file, add_string_to_file


def get_not_included_in_the_lists():
    word_forms_bases = read_src_bs('src_dict/БС 24.03.21.txt')

    short_form = list(get_string_list_from_file(
        'src_dict/П12. ЕСТЬ краткая форма.txt'))
    comparative = list(get_string_list_from_file(
        'src_dict/П22. ЕСТЬ сравнительная степень.txt'))
    superlative_degree = list(get_string_list_from_file(
        'src_dict/П27. ЕСТЬ превосходная степень.txt'))

    for group in word_forms_bases:
        title_form = group.title_word_form
        info_list = title_form.info
        if info_list and title_form.idf.startswith('.П'):
            flag_p12 = False
            flag_p22 = False
            flag_p27 = False
            for info_id in info_list:
                if info_id.startswith('К'):
                    flag_p12 = True
                elif info_id.startswith('С'):
                    flag_p22 = True
                elif info_id.startswith('П'):
                    flag_p27 = True

            if flag_p12 and str(title_form) not in short_form:
                print(title_form)
                add_string_to_file(str(title_form), f'out/П12 ЕЩЁ.txt')

            if flag_p22 and str(title_form) not in comparative:
                print(title_form)
                add_string_to_file(str(title_form), f'out/П22 ЕЩЁ.txt')

            if flag_p27 and str(title_form) not in superlative_degree:
                print(title_form)
                add_string_to_file(str(title_form), f'out/П27 ЕЩЁ.txt')


if __name__ == '__main__':
    get_not_included_in_the_lists()
