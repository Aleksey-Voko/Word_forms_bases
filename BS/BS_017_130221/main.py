import pandas as pd

from BS.utils import (read_src_socket_bs, get_dicts_from_csv_file,
                      save_list_to_file, read_src_bs, get_socket_word_form)


def get_root_index_data_set():
    """
    13.1. найти в док-те БГ 12.02.21.txt все многокорневые слова,
    т.е. слова (кроме невидимок), у которых есть корневой индекс;

    13.2. создать док-т Excel Многокорневые слова.xlsx и заполнить его строками
    с найденными многокорневыми словами с соблюдением следующих правил:
      а. строки приводятся ПОЛНОСТЬЮ;
      б. строки вставляются в тот или иной столбец в зависимости
        от корневого индекса;
      в. уже вставленная строка не должна вставляться второй (и более!) раз!
        Другими словами, в док-те Многокорневые слова.xlsx не должно быть повторов
        абсолютно одинаковых строк

    13.3. по завершении заполнения док-та Многокорневые слова.xlsx
    вставленные строки в столбцах расположить в соответствии
    с алфавитным порядком слов,
    а сами столбцы - в следующем порядке:
    2 2! 2*
    3 3! 3* 3**
    4 4! 4* 4**
    5 5! 5* 5**
    6 6! 6* 6**
    7 7! 7* 7**
    """
    socket_group_word_form_list = read_src_socket_bs(
        'src_dict/БГ 12.02.21.txt')

    root_index_ds = {
        '2': [],
        '2!': [],
        '2*': [],
        '3': [],
        '3!': [],
        '3*': [],
        '3**': [],
        '4': [],
        '4!': [],
        '4*': [],
        '4**': [],
        '5': [],
        '5!': [],
        '5*': [],
        '5**': [],
        '6': [],
        '6!': [],
        '6*': [],
        '6**': [],
        '7': [],
        '7!': [],
        '7*': [],
        '7**': [],
    }

    for socket_group_word_form in socket_group_word_form_list:
        for socket_word_form in socket_group_word_form.socket_word_forms:
            root_index = socket_word_form.root_index
            if root_index and not socket_word_form.invisible:
                root_index_ds[root_index].append(str(socket_word_form))

    for k in root_index_ds:
        root_index_ds[k] = sorted(list(
            set(root_index_ds[k])),
            key=lambda x: x.replace('*', '').lower().strip()
        )

    ds = []
    for k in root_index_ds:
        for word_form in root_index_ds[k]:
            ds.append({
                'root_index': k,
                'word_form': word_form,
            })

    df = pd.DataFrame(ds)
    res_df = (df
              .assign(idx=df.groupby("root_index").cumcount())
              .pivot_table(index="idx", columns="root_index",
                           values="word_form", aggfunc="first"))
    res_df.to_csv('out/Многокорневые слова.csv')


def check_replays():
    """
    14. Проверить каждое слово из док-та Excel Многокорневые слова.xlsx

    на количество повторов в док-те БГ 12.02.21.txt ,
    используя следующую таблицу:

    корневой индекс 2* / 3** - 1 повтор в БГ;
    корневой индекс 2 / 2! / 3* / 4** - 2 повтора в БГ;
    корневой индекс 3 / 3! / 4* / 5** - 3 повтора в БГ;
    корневой индекс 4 / 4! / 5* / 6** - 4 повтора в БГ;
    корневой индекс 5 / 5! / 6* / 7** - 5 повторов в БГ;
    корневой индекс 6 / 6! / 7* - 6 повторов в БГ;
    корневой индекс 7 / 7! - 7 повторов в БГ;

    и на абсолютную идентичность строки со словом в док-те
    Многокорневые слова.xlsx
    со ВСЕМИ строками с этим словом в док-те БГ 12.02.21.txt .
    Т.е. напр. строка из док-та Многокорневые слова.xlsx
    автобус 3* .СеИ неод мI1 мнII1 * auto(mobile) (omni)bus
    должна ИМЕННО В ТАКОМ виде 2 раза присутствовать в док-те БГ 12.02.21.txt .
    """

    multi_root_words = get_dicts_from_csv_file(
        'out/Многокорневые слова.csv')

    socket_group_word_form_list = list(read_src_socket_bs(
        'src_dict/БГ 12.02.21.txt'))

    root_index_ds = {
        '2': [],
        '2!': [],
        '2*': [],
        '3': [],
        '3!': [],
        '3*': [],
        '3**': [],
        '4': [],
        '4!': [],
        '4*': [],
        '4**': [],
        '5': [],
        '5!': [],
        '5*': [],
        '5**': [],
        '6': [],
        '6!': [],
        '6*': [],
        '6**': [],
        '7': [],
        '7!': [],
        '7*': [],
        '7**': [],
    }

    count_index = {
        '2': 2,
        '2!': 2,
        '2*': 1,
        '3': 3,
        '3!': 3,
        '3*': 2,
        '3**': 1,
        '4': 4,
        '4!': 4,
        '4*': 3,
        '4**': 2,
        '5': 5,
        '5!': 5,
        '5*': 4,
        '5**': 3,
        '6': 6,
        '6!': 6,
        '6*': 5,
        '6**': 4,
        '7': 7,
        '7!': 7,
        '7*': 6,
        '7**': 5,
    }

    incorrect_replays = []

    for multi_root_word in multi_root_words:
        for root_index_key in list(multi_root_word)[1:]:
            if multi_root_word[root_index_key]:
                root_index_ds[root_index_key].append(
                    multi_root_word[root_index_key]
                )

    for root_index in root_index_ds:
        for multi_root_word in root_index_ds[root_index]:
            count_word = 0
            for socket_group_word_form in socket_group_word_form_list:
                for socket_word_form in socket_group_word_form.socket_word_forms:
                    if multi_root_word == str(socket_word_form):
                        count_word += 1
            if count_word != count_index[root_index]:
                print(multi_root_word)
                incorrect_replays.append(f'{multi_root_word} - {count_word}')

    save_list_to_file(incorrect_replays, 'out/Не корректные повторы.txt')


def find_all_multi_rooted_words_from_bs():
    """
    15. Найти в док-те БС 03.02.21.txt все слова (ЗС групп и одиночки)
    из док-та Многокорневые слова.xlsx
    и создать список строк с такими словами - док-т Многокорневые слова БС.txt .
    Учитывая п.п. 1 и 2 Правил соотношения БГ и БС,
    сравнить каждую строку док-та Многокорневые слова БС.txt
    с каждой ячейкой со словом в док-те Многокорневые слова.xlsx .
    """

    multi_root_words = get_dicts_from_csv_file(
        'out/Многокорневые слова.csv')

    word_forms_bases = list(read_src_bs('src_dict/БС 03.02.21.txt'))

    multi_root_bg_forms = []

    for multi_root_word in multi_root_words:
        for root_index_key in list(multi_root_word)[1:]:
            if multi_root_word[root_index_key]:
                socket_form = get_socket_word_form(
                    multi_root_word[root_index_key]
                )
                multi_root_bg_forms.append(
                    ' '.join(filter(
                        None,
                        [
                            socket_form.name,
                            socket_form.idf,
                            ' '.join(socket_form.info),
                            socket_form.note.replace('* ', ''),
                        ])))

    multi_root_bs_forms = []

    for group_word_form in word_forms_bases:
        title_form = group_word_form.title_word_form
        src_title_form = ' '.join(filter(
            None,
            [
                title_form.name,
                title_form.idf,
                ' '.join(title_form.info),
                title_form.note.replace('.* ', ''),
            ]))
        if src_title_form in multi_root_bg_forms:
            print(title_form)
            multi_root_bs_forms.append(str(title_form))

    multi_root_bs_forms = sorted(
        multi_root_bs_forms,
        key=lambda x: x.replace('*', '').lower().strip()
    )

    save_list_to_file(multi_root_bs_forms, 'out/Многокорневые слова БС.txt')


if __name__ == '__main__':
    find_all_multi_rooted_words_from_bs()
