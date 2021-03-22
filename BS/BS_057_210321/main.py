from pathlib import Path

from BS.utils import read_src_bs, get_string_list_from_file, add_string_to_file

IDFS = {
    'мI1#': ('С1', 'С5'), 'м!I1#': ('С1', 'С5'),
    'мI1#ь': ('С2', 'С6'), 'м!I1#ь': ('С2', 'С6'),
    'мI1#й': ('С3',), 'м!I1#й': ('С3',),
    'мI1': ('С4',), 'м!I1': ('С4',),
    'мI2#й': ('С7',), 'м!I2#й': ('С7',),
    'мI3#': ('С8',), 'м!I3#': ('С8',),
    'мI3#ь': ('С9',), 'м!I3#ь': ('С9',),
    'мI6': ('С10',), 'м!I6': ('С10',), 'сI6': ('С10',), 'с!I6': ('С10',),
    'мI4': ('С10а',), 'м!I4': ('С10а',), 'сI4': ('С10а',), 'с!I4': ('С10а',),
    'мII1': ('С11',), 'м!II1': ('С11',), 'жII1': ('С11',), 'ж!II1': ('С11',),
    'мII2': ('С12',), 'м!II2': ('С12',), 'жII2': ('С12',), 'ж!II2': ('С12',),
    'жIII1#': ('С13',), 'ж!III1#': ('С13',),

    'мнI12': ('С14',),
    'мнI15о': ('С15',),
    'мнIV1': ('С16', 'С24'),
    'мнIV1+I1': ('С17',),
    'мнIII7': ('С18',),
    'мнI4+III7': ('С19',),
    'мнI6+7': ('С20',),
    'мнII3': ('С21',),
    'мнII4': ('С22',),
    'мнIII3': ('С23',),
    'мнII1+4': ('С25',),
    'мнII1+IV1': ('С26',),
    'мнII1&III3': ('С27',),
    'мнIII2': ('С28',),
    'мнIV6е': ('С29', 'С35'),
    'мнIV6#е': ('С30',),
    'мнIV3+6е': ('С31',),
    'мнIV3+6#е': ('С32',),
    'мнI1': ('С33',),
    'мнI13': ('С34',),
    'мнIV6о': ('С36',),
    'мнI5': ('С37',),
    'мнI16': ('С38',),
    'мнII6е': ('С39',),
    'мнII6#е': ('С40',),
    'мнI6': ('С41',),
    'мнI9': ('С42',),
    'мнI17е': ('С43',),
    'мнI19': ('С44',),
    'мнI19е': ('С45',),
    'мнI19+6': ('С46',),

    'мн!I2*': ('С47',),
    'мн!I16*': ('С48', 'С49'),
    'мн!I16е*': ('С50',),
    'мн!I16о*': ('С51',),
    'мн!I1*+16о*': ('С52',),
    'мн!II6*': ('С53',),
    'мн!III2*': ('С54',),
}


def get_not_included_in_the_lists():
    word_forms_bases = read_src_bs('src_dict/БС 20.03.21.txt')
    file_stems = {
        x.stem: list(get_string_list_from_file(f'{x}'))
        for x in Path('src_dict/lst').glob('*')
    }

    for group in word_forms_bases:
        title_form = group.title_word_form
        info_list = title_form.info
        if info_list:
            for idf in info_list:
                if idf in IDFS:
                    out_stem = ', '.join(IDFS[idf])
                    flag = True
                    added_title_form = []
                    for f_stem in IDFS[idf]:
                        if str(title_form) in file_stems[f_stem]:
                            flag = False
                    if (
                            flag
                            and str(title_form) not in added_title_form
                    ):
                        print(title_form)
                        add_string_to_file(str(title_form),
                                           f'out/lst/{out_stem} ещё.txt')

                        added_title_form.append(str(title_form))


if __name__ == '__main__':
    get_not_included_in_the_lists()
