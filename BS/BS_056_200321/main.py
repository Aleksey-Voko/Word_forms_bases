from pathlib import Path

from BS.utils import (get_string_list_from_file, save_list_to_file,
                      get_bs_title_word_form, read_src_bs)


def change_case():
    for file_path in Path('src_dict/lst').glob('*'):
        file_stem = file_path.stem
        lower_words = []
        words = get_string_list_from_file(file_path, encoding='cp1251')
        for word in words:
            if word:
                lower_words.append(word.lower())
        out_path = f'out/lst/{file_stem}.txt'
        save_list_to_file(lower_words, out_path, encoding='cp1251')


def check_presence():
    homonyms = [get_bs_title_word_form(x).name
                for x in get_string_list_from_file('src_dict/Омонимы БС.txt')]

    word_forms_bases = list(read_src_bs('src_dict/БС 16.03.21 изм.txt'))
    bs_names = [
        x.title_word_form.name.replace('*', '').strip()
        for x in word_forms_bases
    ]

    for file_path in Path('out/lst').glob('*'):
        file_stem = file_path.stem

        presence = []  # 28а. Если слово имеется в док-те Омонимы БС.txt
        nouns = []  # 29а. если слово находится
        absent = []  # 29б. если слово НЕ находится

        words = get_string_list_from_file(file_path, encoding='cp1251')
        for word in words:
            print(word)
            if word in homonyms:
                presence.append(word)

            else:
                if word in bs_names:
                    for group in word_forms_bases:
                        if word == group.title_word_form.name:
                            print(group.title_word_form)
                            nouns.append(str(group.title_word_form))
                else:
                    absent.append(word)

        if presence:
            save_list_to_file(
                sorted(presence), f'out/homonyms/{file_stem} омонимы.txt')

        if nouns:
            save_list_to_file(sorted(nouns), f'out/C/С{file_stem}.txt')

        if absent:
            save_list_to_file(
                sorted(absent), f'out/absent/{file_stem} отсутствует.txt')


if __name__ == '__main__':
    check_presence()
