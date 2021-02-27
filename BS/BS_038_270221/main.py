from BS.utils import (save_list_to_file, get_string_list_from_file,
                      read_src_bs)


def get_two_in_one():
    remaining_repetitions = get_string_list_from_file('src_dict/Повторы ост.txt')
    word_forms_bases = read_src_bs('src_dict/БС 27.02.21.txt')
    bs_word_forms = [x.title_word_form for x in word_forms_bases]

    bs_word_names = [
        ' '.join(filter(None, [
            x.name,
            x.idf,
            ' '.join(x.info),
            x.note
        ]))
        for x in bs_word_forms
    ]

    relevant = []
    not_relevant = []

    for repeat in remaining_repetitions:
        if repeat in bs_word_names:
            relevant.append(repeat)
        else:
            not_relevant.append(repeat)

    save_list_to_file(relevant, 'out/Повторы ост. совпадает с БС.txt')
    save_list_to_file(not_relevant, 'out/Повторы ост. не совпадает с БС.txt')


if __name__ == '__main__':
    get_two_in_one()
