from pathlib import Path

from BS.utils import get_string_list_from_file, add_string_to_file


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


if __name__ == '__main__':
    dirs = ('1-28', '29-33', '34-43', '44', '45', '46-49', '50-52', '53-60',
            '61-62', '63-66')
    for in_d in dirs:
        check_repeats_in_lists(in_d)
