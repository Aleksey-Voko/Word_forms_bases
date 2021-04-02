from BS.utils import (get_string_list_from_file, read_src_bs,
                      save_list_to_file)


ENDINGS = ('ешь', 'ешься', 'ишь', 'ишься', 'ышь', 'ышься')
LETTERS = ('ж', 'ч', 'ш', 'щ')


def check_verbs():
    verbs = sorted(
        list(get_string_list_from_file(
            'src_dict/Г64. -АТЬ(СЯ), -ЕТЬ(СЯ) II спр. сов. в.txt'))
        + list(get_string_list_from_file(
            'src_dict/Г65. -ИТЬ(СЯ) II спр. сов. в.txt'))
    )

    word_forms_bases = list(read_src_bs('src_dict/БС 27.03.21.txt'))

    nouns = []
    g64_g65_a = []
    g64_g65_b = []

    for verb in verbs:
        for group in word_forms_bases:
            if verb == str(group.title_word_form):
                print(verb)
                gnb2e = None
                for word_form in group.word_forms:
                    if word_form.idf == '.ГНБ2е':
                        gnb2e = word_form
                        break

                if gnb2e:
                    if gnb2e.name.endswith(ENDINGS):
                        if gnb2e.name.endswith('ся'):
                            prefix = gnb2e.name[:-5]
                        else:
                            prefix = gnb2e.name[:-3]

                        if prefix[-1] in LETTERS:
                            g64_g65_b.append(verb)
                        else:
                            g64_g65_a.append(verb)

                    else:  # окончание какое-то другое
                        nouns.append(verb)

                else:  # если словоформа .ГНБ2е отсутствует
                    nouns.append(verb)

                break

    save_list_to_file(verbs, 'out/Г64&Г65.txt')
    save_list_to_file(nouns, 'out/ГНБ2е отс. или оконч. другое.txt')
    save_list_to_file(g64_g65_a, 'out/Г64&Г65А.txt')
    save_list_to_file(g64_g65_b, 'out/Г64&Г65Б.txt')


if __name__ == '__main__':
    check_verbs()
