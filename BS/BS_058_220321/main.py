import fileinput
from collections import Counter
from pathlib import Path

from BS.utils import save_list_to_file


def get_file_lines(file_list, mode='r', encoding='utf-8', errors=None):
    hook = fileinput.hook_encoded(encoding=encoding, errors=errors)
    with fileinput.input(files=file_list, mode=mode, openhook=hook) as f:
        for ln in f:
            yield ln.rstrip()


def check_replays(dir_num):
    files_path = [x for x in Path(f'src_dict/{dir_num}').glob('*')]
    lines = [x for x in get_file_lines(files_path)]
    replays = [x for x, y in Counter(lines).items() if y > 1]
    if replays:
        save_list_to_file(sorted(replays), f'out/{dir_num} повторы.txt')


if __name__ == '__main__':
    for group in ('1-13', '14-46', '47-54'):
        check_replays(group)
