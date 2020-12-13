from utils import read_src_bs, get_string_list_from_file, save_bs_dicts_to_txt, save_list_to_file
from word_form import TitleWordForm, GroupWordForm


def get_singles_bases():
    src_group_word_form_list = get_string_list_from_file('src_dict/Добавить одиночки в БС.txt')
    for src_title_word_form in src_group_word_form_list:
        title_word_form = TitleWordForm(src_title_word_form, '', [], '')
        group_word_form = GroupWordForm(title_word_form, [])
        yield group_word_form


def save_kunstkamera_2():
    to_the_kunstkamera_list = list(get_string_list_from_file('src_dict/В Кунсткамеру2.txt'))
    kunstkamera_2 = []
    kunstkamera_2_title_string = []

    for group in read_src_bs('src_dict/БС 29.11.20.txt'):
        title_form = group.title_word_form
        title_string = ' '.join(filter(
            None,
            [title_form.name,
             title_form.idf,
             ' '.join(title_form.info),
             title_form.note])).strip()
        if title_string in to_the_kunstkamera_list:
            kunstkamera_2.append(group)
            kunstkamera_2_title_string.append(title_string)
    save_bs_dicts_to_txt(sorted(kunstkamera_2), 'out/Кунсткамера2.txt', encoding='utf-8')

    remaining_to_the_kunstkamera = [x for x in to_the_kunstkamera_list if x not in kunstkamera_2_title_string]
    save_list_to_file(remaining_to_the_kunstkamera, 'out/Не выполняется п.1.txt')

    remaining_word_forms_bases = list(filter(
        lambda x: ' '.join(filter(
            None, [x.title_word_form.name, x.title_word_form.idf,
                   ' '.join(x.title_word_form.info),
                   x.title_word_form.note])).strip() not in to_the_kunstkamera_list,
        read_src_bs('src_dict/БС 29.11.20.txt')
    ))
    add_singles_bases = list(get_singles_bases())
    remaining_word_forms_bases += add_singles_bases
    save_bs_dicts_to_txt(sorted(remaining_word_forms_bases), 'out/БС 12.12.20.txt')


if __name__ == '__main__':
    save_kunstkamera_2()
