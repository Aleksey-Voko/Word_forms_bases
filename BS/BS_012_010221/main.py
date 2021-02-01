from BS.tmpl_verbs import (get_present_future_forms, get_past_tense_forms,
                           get_imperative_mood_forms, get_joint_action_forms,
                           get_present_participle_is_valid,
                           get_passive_present_participle,
                           get_past_participle_is_valid,
                           get_passive_past_participle, get_present_participle,
                           get_past_participle)
from BS.utils import get_dicts_from_csv_file, save_bs_dicts_to_txt
from BS.word_form import GroupWordForm, TitleWordForm


def get_group_word_form(src_dict: dict) -> GroupWordForm:
    name = src_dict['name']
    info = [src_dict['Inf_0'], src_dict['Inf_1']]
    info += list(filter(None, [
        src_dict['Inf_2'],
        src_dict['Inf_3'],
        src_dict['Inf_4'],
        src_dict['Inf_5'],
        src_dict['Inf_6'],
        src_dict['Inf_7'],
        src_dict['Inf_8'],
        src_dict['Inf_9'],
        src_dict['Inf_10'],
        src_dict['Inf_11'],
        src_dict['Inf_12'],
    ]))

    title_word_form = TitleWordForm(name, '.ГИ', info, '')

    word_forms = []
    if src_dict['Inf_3']:
        present_future_forms = get_present_future_forms(src_dict)
        word_forms += present_future_forms

    if src_dict['Inf_4']:
        past_tense_forms = get_past_tense_forms(src_dict)
        word_forms += past_tense_forms

    if src_dict['Inf_5']:
        imperative_mood_forms = get_imperative_mood_forms(src_dict)
        word_forms += imperative_mood_forms

    if src_dict['Inf_6']:
        joint_action_forms = get_joint_action_forms(src_dict)
        word_forms += joint_action_forms

    if src_dict['Inf_7']:
        present_participle_is_valid_forms = get_present_participle_is_valid(src_dict)
        word_forms += present_participle_is_valid_forms

    if src_dict['Inf_8']:
        passive_present_participle_forms = get_passive_present_participle(src_dict)
        word_forms += passive_present_participle_forms

    if src_dict['Inf_9']:
        past_participle_is_valid_forms = get_past_participle_is_valid(src_dict)
        word_forms += past_participle_is_valid_forms

    if src_dict['Inf_10']:
        passive_past_participle_forms = get_passive_past_participle(src_dict)
        word_forms += passive_past_participle_forms

    if src_dict['Inf_11']:
        present_participle_forms = get_present_participle(src_dict)
        word_forms += present_participle_forms

    if src_dict['Inf_12']:
        past_participle_forms = get_past_participle(src_dict)
        word_forms += past_participle_forms

    return GroupWordForm(title_word_form, word_forms)


def save_groups_to_bs():
    """
    10. Используя списки на вкладке "Глаголы" док-та Глаголы.xlsx ,
    а также шаблоны, приведённые на вкладках "Шаблоны НБ вр.", "Шаблоны Причастия"
    и "Шаблоны Остальное" того же док-та,
    создать док-т Добавить группы в БС. Глаголы.txt .
    """
    src_groups = get_dicts_from_csv_file('Добавить глаголы.csv')
    add_groups_to_bs_list = []

    for src_dict in src_groups:
        add_groups_to_bs_list.append(get_group_word_form(src_dict))

    save_bs_dicts_to_txt(sorted(add_groups_to_bs_list),
                         'out/Добавить группы в БС. Глаголы.txt',
                         encoding='utf-8')


if __name__ == '__main__':
    save_groups_to_bs()
