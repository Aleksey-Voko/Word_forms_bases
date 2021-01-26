from BS.tmpl_adjectives import get_full_forms, get_short_forms, get_comparative_forms, get_superlative_forms
from BS.utils import get_dicts_from_csv_file, save_bs_dicts_to_txt
from BS.word_form import GroupWordForm, TitleWordForm


def get_socket_group_word_form(src_dict: dict) -> GroupWordForm:
    name = src_dict['name']
    info = [src_dict['Inf_0'], ' '.join(list(filter(None, [
        src_dict['Inf_1'],
        src_dict['Inf_2'],
        src_dict['Inf_3'],
        src_dict['Inf_4'],
        src_dict['Inf_5'],
    ])))]

    word_forms = []
    adjectives_full_forms = get_full_forms(src_dict)
    word_forms += adjectives_full_forms

    if src_dict['Inf_1']:
        adjectives_short_forms = get_short_forms(src_dict)
        word_forms += adjectives_short_forms

    if src_dict['Inf_2']:
        adjectives_comparative_forms = get_comparative_forms(src_dict)
        word_forms += adjectives_comparative_forms

    if src_dict['Inf_3']:
        adjectives_superlative_forms = get_superlative_forms(src_dict)
        word_forms += adjectives_superlative_forms

    title_word_form = TitleWordForm(name, word_forms[0].idf, info, '')
    return GroupWordForm(title_word_form, word_forms[1:])


def save_groups_to_bs():
    """
    6. Используя списки на вкладке "Прил-ные в столбик" док-та Прилагательные.xlsx ,
    а также шаблоны, приведённые на вкладках
    "ШАБЛОНЫ полн. ф., прев. ст."
    и "ШАБЛОНЫ кр. ф., срав. ст."
    того же док-та,
    создать док-т Добавить группы в БС. Прил-ные.txt .
    """
    src_groups = get_dicts_from_csv_file('Прилагательные.csv')
    add_groups_to_bs_list = []

    for src_dict in src_groups:
        add_groups_to_bs_list.append(get_socket_group_word_form(src_dict))

    save_bs_dicts_to_txt(sorted(add_groups_to_bs_list),
                         'out/Добавить группы в БС. Прил-ные.txt',
                         encoding='utf-8')


if __name__ == '__main__':
    save_groups_to_bs()
