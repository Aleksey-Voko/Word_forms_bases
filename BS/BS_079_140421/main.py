from pprint import pprint

from BS.utils import get_string_list_from_file, get_bs_title_word_form, save_list_to_file


def remove_strings():
    relevant_repetitions = get_string_list_from_file(
        'src_dict/Повторы ост. совпадает с БС.txt')
    multi_root_bs = list(get_string_list_from_file(
        'src_dict/Многокорневые слова БС.txt'))
    multi_root_bs = [get_bs_title_word_form(x) for x in multi_root_bs]
    multi_root_bs = [
        ' '.join(filter(None, [
            x.name,
            x.idf,
            ' '.join(x.info),
            x.note,
        ]))
        for x in multi_root_bs
    ]

    save_list_to_file(sorted(list(set(
        relevant_repetitions) - set(multi_root_bs))),
                      'out/Повторы ост. совпадает с БС.txt')


if __name__ == '__main__':
    remove_strings()
