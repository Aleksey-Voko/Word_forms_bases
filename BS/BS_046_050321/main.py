from pprint import pprint

from BS.utils import read_src_bs, save_list_to_file, get_string_list_from_file


def get_loners_reruns():
    word_forms_bases = list(read_src_bs('src_dict/БС 04.03.21.txt'))

    loners = [x.title_word_form for x in word_forms_bases if not x.word_forms]

    loners_reruns = []

    for loner in loners:
        print(loner)
        for group in word_forms_bases:
            if group.word_forms:
                title_form = group.title_word_form
                word_forms = group.word_forms
                word_form_names = [x.name for x in word_forms]
                if loner.name in word_form_names:
                    loners_reruns.append(str(loner))
                    loners_reruns.append(str(title_form))
                    for word_form in word_forms:
                        if word_form.name == loner.name:
                            loners_reruns.append(str(word_form))
                    loners_reruns.append('\n')

    save_list_to_file(loners_reruns, 'out/Одиночки-повторы.txt')


if __name__ == '__main__':
    get_loners_reruns()
