from pathlib import Path
from pprint import pprint

from BS.utils import read_src_bs, save_list_to_file


def get_headwords():
    word_forms_bases = list(read_src_bs('src_dict/БС 06.03.21.txt'))

    headwords = [x.title_word_form for x in word_forms_bases]

    headwords_reruns = []

    for headword in headwords:
        print(headword)
        for group in word_forms_bases:
            if group.word_forms:
                word_forms = group.word_forms
                word_form_names = [x.name for x in word_forms]
                if headword.name in word_form_names:
                    title_form = group.title_word_form
                    headwords_reruns.append(str(headword))
                    headwords_reruns.append(str(title_form))
                    for word_form in word_forms:
                        if word_form.name == headword.name:
                            headwords_reruns.append(str(word_form))
                    headwords_reruns.append('')

    save_list_to_file(headwords_reruns, 'out/ЗС-повторы.txt')


def headwords_test():
    with open(Path('out/ЗС-повторы_001.txt'), encoding='utf-8') as f_in:
        headwords_string = f_in.read()

    headwords_reruns = []

    headwords_groups = [x for x in headwords_string.split('\n\n\n')]
    for group in headwords_groups:
        lines = group.split('\n')
        if lines[0] != lines[1]:
            headwords_reruns.append(group + '\n')

    save_list_to_file(headwords_reruns, 'out/ЗС-повторы.txt')


if __name__ == '__main__':
    headwords_test()
