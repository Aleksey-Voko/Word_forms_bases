from pathlib import Path

from BS.utils import (get_string_list_from_file, add_string_to_file,
                      get_file_lines, save_list_to_file, read_src_bs)


def check_repeats_in_lists(in_dir):
    file_stems = {
        x.stem: list(get_string_list_from_file(f'{x}'))
        for x in Path(f'src_dict/{in_dir}').glob('*')
    }

    dict_line = {}

    for f_stem in file_stems:
        for line in file_stems[f_stem]:
            dict_line.setdefault(line, []).append(f_stem)

    for line in dict_line:
        if len(dict_line[line]) > 1:
            print(line)
            add_string_to_file(
                f'{line} > {dict_line[line]}',
                f'out/Повторы {in_dir}.txt'
            )


def find_extra_lines(in_file, in_dir):
    files_path = [x for x in Path(in_dir).glob('*')]
    in_dir_lines = [x for x in get_file_lines(files_path)]
    in_lines = list(get_string_list_from_file(in_file))
    extra_lines = [x for x in in_dir_lines if x not in in_lines]
    if extra_lines:
        save_list_to_file(extra_lines, f'out/Лишние {Path(in_file).stem}.txt')


def get_no_full_form():
    word_forms_bases = read_src_bs('src_dict/БС 24.03.21.txt')

    no_full_form_list = []

    for group in word_forms_bases:
        title_form = group.title_word_form
        info_list = title_form.info
        if info_list and title_form.idf.startswith('.П'):
            if info_list[0].startswith(('К', 'С', 'П')):
                print(title_form)
                no_full_form_list.append(str(title_form))

    save_list_to_file(no_full_form_list, 'out/НЕТ полной формы.txt')


if __name__ == '__main__':
    for in_d in ('1-11', '13-21', '23-26'):
        check_repeats_in_lists(in_d)

    find_extra_lines('src_dict/П12. ЕСТЬ краткая форма.txt', 'src_dict/13-21')
    find_extra_lines('src_dict/П22. ЕСТЬ сравнительная степень.txt', 'src_dict/23-26')

    get_no_full_form()
