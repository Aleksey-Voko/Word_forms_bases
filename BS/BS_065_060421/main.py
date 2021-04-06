from pathlib import Path

from BS.utils import read_src_bs, get_string_list_from_file, add_string_to_file

IDFS = {
    'НБI2в': ('Г2',), 'НБI2ж-': ('Г3',), 'НБI2н': ('Г4',), 'НБI3-': ('Г5',),
    'НБI4': ('Г6',), 'НБI4-': ('Г7',), 'НБI4и': ('Г8',), 'НБI4м': ('Г9',),
    'НБI4н': ('Г10',), 'НБI4т': ('Г11',), 'НБI5е': ('Г12',), 'НБI5о': ('Г13',),
    'НБI5ь': ('Г14', 'Г25'), 'НБI6ч': ('Г15',), 'НБI6ч-': ('Г16',),
    'НБI6ш': ('Г17',), 'НБI9у-': ('Г18',), 'НБI3&6ж': ('Г19',),
    'НБI3&6ч': ('Г20',), 'НБII1': ('Г21',), 'НБII1-': ('Г22',),
    'НБII2': ('Г23', 'Г24'), 'НБII3-': ('Г26',), 'НБII4о': ('Г27',),
    'НБI-II*д': ('Г28',),

    'НБI5ь*': ('Г25',), 'НБI5ь**': ('Г25',), 'НБI5ь***': ('Г25',),
    'НБI5ь****': ('Г25',), 'НБI5ь*****': ('Г25',), 'НБI5ь******': ('Г25',),
    'НБI5ь!': ('Г25',), 'НБI5ь*!': ('Г25',),
    'НБI5ь**!': ('Г25',), 'НБI5ь***!': ('Г25',),

    'П3г-': ('Г3',), 'П1-': ('Г29',), 'П2': ('Г30',),
    'П2+9': ('Г31',), 'П9': ('Г32', 'Г33'),

    'Пв2г-': ('Г3',), 'Пв2**-': ('Г16',), 'Пв1е': ('Г25',), 'Пв1*': ('Г28',),
    'Пв1-': ('Г34',), 'Пв2': ('Г35',), 'Пв2-': ('Г36',), 'Пв2!': ('Г37',),
    'Пв3': ('Г38',), 'Пв3-': ('Г39',), 'Пв1|2': ('Г40',), 'Пв1|3': ('Г41',),
    'Пв2&3': ('Г42',), 'Пв2!&3': ('Г43',),

    'С': ('Г44',),

    'ПНД2': ('Г45',),

    'ПНС1*': ('Г47',), 'ПНС3': ('Г48',), 'ПНС1|1': ('Г49',),

    'ППД5': ('Г50', 'Г51',), 'ППД2в&5': ('Г52',),

    'ППС2ж': ('Г57',), 'ППС3': ('Г58',), 'ППС7': ('Г59',), 'ППС2&2о': ('Г60',),

    'ДН1|1': ('Г62',),

    'ДП2': ('Г64&Г65А',), 'ДП3': ('Г64&Г65Б',), 'ДП9': ('Г66',),
}

set_g1 = ('НБ', 'Пв', 'С', 'ПНД', 'ПНС', 'ДН')


def get_not_included_in_the_lists():
    word_forms_bases = read_src_bs('src_dict/БС 03.04.21.txt')
    file_stems = {
        x.stem.split('.')[0]: list(get_string_list_from_file(f'{x}'))
        for x in Path('src_dict/lst').glob('*')
    }

    pps_list = (file_stems['Г53'] + file_stems['Г54']
                + file_stems['Г55'] + file_stems['Г56'])

    for group in word_forms_bases:
        title_form = group.title_word_form
        title_id = group.title_word_form.idf
        info_list = title_form.info
        if info_list and title_id.startswith('.Г'):
            for identifier in info_list:
                if identifier in IDFS:
                    for f_stem in IDFS[identifier]:
                        flag = True
                        added_title_form = []
                        if str(title_form) in file_stems[f_stem]:
                            flag = False
                        if (
                                flag
                                and str(title_form) not in added_title_form
                        ):
                            print(title_form)
                            add_string_to_file(str(title_form),
                                               f'out/lst/{f_stem} ещё.txt')

                            added_title_form.append(str(title_form))

            # 30.21.
            flag_g1 = False
            for identifier in info_list:
                if identifier.startswith(set_g1):
                    flag_g1 = True
                    break
            if not flag_g1 and str(title_form) not in file_stems['Г1']:
                print(title_form)
                add_string_to_file(str(title_form),
                                   f'out/lst/Г1 ещё.txt')

            # 30.22.
            flag_g46 = False
            for identifier in info_list:
                if identifier.startswith('ПНС'):
                    flag_g46 = True
                    break
            if not flag_g46 and str(title_form) not in file_stems['Г46']:
                print(title_form)
                add_string_to_file(str(title_form),
                                   f'out/lst/Г46 ещё.txt')

            # 30.23.
            flag_g53_56 = False
            for identifier in info_list:
                if identifier.startswith('ППС'):
                    flag_g53_56 = True
                    break
            if not flag_g53_56 and str(title_form) not in pps_list:
                print(title_form)
                add_string_to_file(str(title_form),
                                   f'out/lst/Г53, Г54, Г55, Г56 ещё.txt')

            # 30.24.
            flag_g61 = False
            for identifier in info_list:
                if identifier.startswith('ДН'):
                    flag_g61 = True
                    break
            if not flag_g61 and str(title_form) not in file_stems['Г61']:
                print(title_form)
                add_string_to_file(str(title_form),
                                   f'out/lst/Г61 ещё.txt')

            # 30.25.
            flag_g63 = False
            for identifier in info_list:
                if identifier.startswith('ДП'):
                    flag_g63 = True
                    break
            if not flag_g63 and str(title_form) not in file_stems['Г63']:
                print(title_form)
                add_string_to_file(str(title_form),
                                   f'out/lst/Г63 ещё.txt')


if __name__ == '__main__':
    get_not_included_in_the_lists()
