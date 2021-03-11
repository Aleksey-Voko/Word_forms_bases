from BS.utils import read_src_bs, save_list_to_file


def get_bs_names():
    word_forms_bases = list(read_src_bs('src_dict/БС 09.03.21.txt'))

    bs_names = []

    for group in word_forms_bases:
        if group.word_forms:
            word_forms = group.word_forms
            word_form_names = [x.name.replace('*', '') for x in word_forms]
            bs_names += word_form_names

    bs_names = sorted(list(set(bs_names)), key=str.lower)

    save_list_to_file(bs_names, 'out/bs_names.txt')


def get_headwords():
    word_forms_bases = list(read_src_bs('src_dict/БС 09.03.21.txt'))

    headwords = [x.title_word_form for x in word_forms_bases]

    headwords_reruns = []

    for headword in headwords:
        print(headword)
        for group in word_forms_bases:
            if str(headword) != str(group.title_word_form):
                if group.word_forms:
                    word_forms = group.word_forms
                    word_form_names = [x.name for x in word_forms]
                    headword_name = headword.name.replace('*', '')
                    if headword_name in word_form_names:
                        title_form = group.title_word_form
                        headwords_reruns.append(str(headword))
                        headwords_reruns.append(str(title_form))
                        for word_form in word_forms:
                            if word_form.name == headword_name:
                                headwords_reruns.append(str(word_form))
                        headwords_reruns.append('')

    save_list_to_file(headwords_reruns, 'out/ЗС-повторы.txt')


if __name__ == '__main__':
    get_headwords()
