from BS.utils import (get_string_list_from_file, get_bs_title_word_form,
                      save_list_to_file)


def check_g6():
    endings = ('нуть', 'нуться', 'зиждить', 'зиждиться', 'врать', 'враться',
               'жрать', 'жраться', 'рвать', 'рваться', 'реветь', 'реветься',
               'ржать', 'ржаться', 'сосать', 'сосаться', 'срать', 'сраться',
               'стонать', 'стонаться', 'ткать', 'ткаться', 'шибить',
               'шибиться')

    g6_list = get_string_list_from_file('src_dict/Г6 ещё.txt')
    word_forms = [get_bs_title_word_form(x) for x in g6_list]

    out_list = []

    for word_form in word_forms[:]:
        if not word_form.name.endswith(endings):
            print(word_form)
            out_list.append(str(word_form))

    save_list_to_file(sorted(out_list), 'out/Г6 ещё изм.txt')


def check_g15():
    endings = ('бормотать', 'бормотаться', 'лепетать', 'лепетаться',
               'плакать', 'плакаться', 'прятать', 'прятаться', 'скакать',
               'скакаться', 'топтать', 'топтаться', 'шептать', 'шептаться',
               'щебетать', 'щебетаться', 'готать', 'готаться', 'котать',
               'котаться', 'потать', 'потаться', 'хотать', 'хотаться',
               'хтать', 'хтаться')

    g15_list = get_string_list_from_file('src_dict/Г15 ещё.txt')
    word_forms = [get_bs_title_word_form(x) for x in g15_list]

    out_list = []

    for word_form in word_forms[:]:
        if not word_form.name.endswith(endings):
            print(word_form)
            out_list.append(str(word_form))

    save_list_to_file(sorted(out_list), 'out/Г15 ещё изм.txt')


def check_g21():
    endings = ('верещать', 'верещаться', 'дышать', 'дышаться', 'кишеть',
               'кишеться', 'пищать', 'пищаться', 'слышать', 'слышаться',
               'трещать', 'трещаться', 'ршать', 'ршаться', 'жить', 'житься',
               'чить', 'читься', 'шить', 'шиться', 'щить', 'щиться')

    g21_list = get_string_list_from_file('src_dict/Г21 ещё.txt')
    word_forms = [get_bs_title_word_form(x) for x in g21_list]

    out_list = []

    for word_form in word_forms[:]:
        if not word_form.name.endswith(endings):
            print(word_form)
            out_list.append(str(word_form))

    save_list_to_file(sorted(out_list), 'out/Г21 ещё изм.txt')


def check_g50_51():
    endings = ('выкнуть', 'выкнуться', 'гибнуть', 'гибнуться', 'глохнуть',
               'глохнуться', 'грязнуть', 'грязнуться', 'дрыхнуть',
               'дрыхнуться', 'дрябнуть', 'дрябнуться', 'зябнуть', 'зябнуться',
               'киснуть', 'киснуться', 'крепнуть', 'крепнуться', 'липнуть',
               'липнуться', 'мерзнуть', 'мерзнуться', 'мокнуть', 'мокнуться',
               'мякнуть', 'мякнуться', 'пухнуть', 'пухнуться', 'сохнуть',
               'сохнуться', 'чахнуть', 'чахнуться')

    g50_51_list = get_string_list_from_file('src_dict/Г50, Г51 ещё.txt')
    word_forms = [get_bs_title_word_form(x) for x in g50_51_list]

    out_list = []

    for word_form in word_forms[:]:
        if not word_form.name.endswith(endings):
            print(word_form)
            out_list.append(str(word_form))

    save_list_to_file(sorted(out_list), 'out/Г50, Г51 ещё изм.txt')


def check_g53_56():
    endings = ('шел', 'авать', 'ивать', 'увать', 'ывать', 'вевать', 'мевать',
               'певать', 'ревать', 'севать', 'тевать', 'щевать', 'длевать',
               'тлевать', 'одолевать', 'одолевать', 'разевать')

    nes_endings = ('водить', 'возить', 'носить', 'ходить')

    g53_56_list = get_string_list_from_file('src_dict/Г53, Г54, Г55, Г56 ещё.txt')
    word_forms = [get_bs_title_word_form(x) for x in g53_56_list]

    out_list = []

    for word_form in word_forms[:]:
        if not (
                'неп' in word_form.info
                or 'б' in word_form.info
                or word_form.name.endswith(endings)
                or (
                        'нес' in word_form.info
                        and word_form.name.endswith(nes_endings)
                )
        ):
            print(word_form)
            out_list.append(str(word_form))

    save_list_to_file(sorted(out_list), 'out/Г53, Г54, Г55, Г56 ещё изм.txt')


def check_g58():
    endings = ('греть', 'мять', 'оть', 'ыть', 'пеленать')

    g58_list = get_string_list_from_file('src_dict/Г58 ещё.txt')
    word_forms = [get_bs_title_word_form(x) for x in g58_list]

    out_list = []

    for word_form in word_forms[:]:
        if not word_form.name.endswith(endings):
            print(word_form)
            out_list.append(str(word_form))

    save_list_to_file(sorted(out_list), 'out/Г58 ещё изм.txt')


def add_g37():
    g37_list = get_string_list_from_file('src_dict/Г37. -И(СЬ).txt')
    g37_add_list = get_string_list_from_file('src_dict/Г37 ещё ДОБАВИТЬ.txt')

    out_list = list(g37_list) + list(g37_add_list)
    out_list = sorted(out_list, key=lambda x: x.replace('*', '').lower())
    save_list_to_file(out_list, 'out/-И(СЬ).txt')


def add_g38():
    g38_list = get_string_list_from_file('src_dict/Г38. -Ь(СЯ).txt')
    g38_add_list = get_string_list_from_file('src_dict/Г38 ещё ДОБАВИТЬ.txt')

    out_list = list(g38_list) + list(g38_add_list)
    out_list = sorted(out_list, key=lambda x: x.replace('*', '').lower())
    save_list_to_file(out_list, 'out/-Ь(СЯ).txt')


if __name__ == '__main__':
    add_g38()
