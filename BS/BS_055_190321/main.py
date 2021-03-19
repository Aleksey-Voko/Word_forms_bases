from collections import Counter

from BS.utils import save_list_to_file, read_src_bs


def get_homonyms_bs():
    word_forms_bases = list(read_src_bs('src_dict/БС 16.03.21 изм.txt'))

    word_names = [
        x.title_word_form.name.replace('*', '').strip()
        for x in word_forms_bases
    ]
    word_names = [x for x, y in Counter(word_names).items() if y > 1]
    word_names = sorted(list(set(word_names)))

    homonyms = []

    for group_word_form in word_forms_bases:
        title_form = group_word_form.title_word_form
        if title_form.name.replace('*', '').strip() in word_names:
            print(title_form)
            homonyms.append(str(title_form))

    save_list_to_file(
        sorted(homonyms, key=lambda x: x.replace('*', '').strip().lower()),
        'out/Омонимы БС.txt'
    )


if __name__ == '__main__':
    get_homonyms_bs()
