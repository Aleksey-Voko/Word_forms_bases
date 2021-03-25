from pathlib import Path

from BS.utils import read_src_bs, get_string_list_from_file, add_string_to_file

IDFS = {
    'I2м': 'П1',
    'I2-с': 'П2',
    'I3м': 'П3',
    'I3-с': 'П4',
    'II1м': 'П5',
    'II1ж': 'П6',
    'II1с': 'П7',
    'II1-с': 'П8',
    'II2-с': 'П8а',
    'II3-с': 'П9',
    'III3': 'П10',
    'IIIф': 'П11',
    'К1': 'П12. ЕСТЬ краткая форма',
    'К1е': 'П13',
    'К2': 'П14',
    'К2о': 'П15',
    'К5е': 'П16',
    'К5мн': 'П17',
    'К6': 'П18',
    'К8': 'П19',
    'К6+1е': 'П20',
    'К6&8': 'П21',
    'СI1': 'П22. ЕСТЬ сравнительная степень',
    'СI1-': 'П23',
    'СII3ж': 'П24',
    'СII4ж': 'П25',
    'СII13щ': 'П26',
    'ПI1': 'П27. ЕСТЬ превосходная степень',
}


def get_not_included_in_the_lists():
    word_forms_bases = read_src_bs('src_dict/БС 24.03.21.txt')
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
                    out_stem = IDFS[idf]
                    if str(title_form) not in file_stems[out_stem]:
                        print(title_form)
                        add_string_to_file(str(title_form),
                                           f'out/lst/{out_stem} ещё.txt')


if __name__ == '__main__':
    get_not_included_in_the_lists()
