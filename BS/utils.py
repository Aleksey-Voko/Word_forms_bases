import csv
from pathlib import Path

from ruamel.yaml import YAML

from word_form import TitleWordForm, WordForm, GroupWordForm


def read_src_bs(f_name: str, encoding='cp1251'):
    """
    Читает БС.
    :param f_name: имя файла БС
    :param encoding: encoding f_in
    :return: word_forms_bases (список объектов GroupWordForm)
    """
    with open(f_name, encoding=encoding) as f_in:
        src_group_word_form_list = (x.strip() for x in f_in.read().split('\n\n'))

        for src_group_word_form in src_group_word_form_list:
            src_title_word_form, *src_word_forms = src_group_word_form.split('\n')

            # title_word_form
            if '.*' in src_title_word_form:
                src_title_word_form_w_note, src_note = [x.strip() for x in src_title_word_form.split(' .* ')]
                note = ' '.join(['.*', src_note])
            else:
                src_title_word_form_w_note = src_title_word_form
                note = ''
            name, *idf_info, = src_title_word_form_w_note.split()
            if idf_info:
                idf, *info = idf_info
            else:
                idf, *info = '', ''
            title_word_form = TitleWordForm(name, idf, info, note)

            # word_forms
            word_forms = []
            for src_word_form in src_word_forms:
                name, *idf_list, = src_word_form.split()  # idf бывает с пробелом: '.ДП* -ДП*'
                word_forms.append(WordForm(name, ' '.join(idf_list)))

            # group_word_form
            group_word_form = GroupWordForm(title_word_form, word_forms)

            yield group_word_form


def save_dicts_to_yaml(in_dicts, f_name, encoding='utf-8', flow_style=True):
    yaml = YAML(pure=True)
    yaml.default_flow_style = flow_style
    Path(f_name).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(f_name), 'w', encoding=encoding) as f_out:
        yaml.dump_all(in_dicts, f_out)


def save_bs_dicts_to_txt(in_dicts: list, f_name, encoding='cp1251'):
    Path(f_name).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(f_name), 'w', encoding=encoding) as f_out:
        f_out.write('\n\n'.join(str(x) for x in in_dicts) + '\n')


def get_string_list_from_file(f_name, encoding='utf-8'):
    with open(Path(f_name), encoding=encoding) as f_in:
        for line in f_in:
            yield line.rstrip()


def save_list_to_file(input_list: list, out_file: str, encoding='utf-8'):
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(out_file), 'w', encoding=encoding) as f_out:
        for line in input_list:
            f_out.write(str(line) + '\n')


def get_dicts_from_csv_file(f_name, encoding='utf-8',
                            newline='', delimiter=','):
    with open(Path(f_name), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.DictReader(f_in, delimiter=delimiter)
        for row in csv_reader:
            yield row


def get_fieldnames_from_csv_file(f_name, encoding='utf-8',
                                 newline='', delimiter=','):
    with open(Path(f_name), encoding=encoding, newline=newline) as f_in:
        return csv.DictReader(f_in, delimiter=delimiter).fieldnames
