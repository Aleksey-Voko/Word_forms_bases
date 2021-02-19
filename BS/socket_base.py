from collections import OrderedDict


class SocketWordForm:
    def __init__(self, invisible,  name, root_index, idf, info: list,
                 note, etml_note):
        self.__invisible = invisible
        self.__name = name
        self.__root_index = root_index
        self.__idf = idf
        self.__info = info
        self.__note = note
        self.__etml_note = etml_note

    def __repr__(self):
        return ' '.join(filter(
            None,
            [
                # self.__invisible,
                self.__name,
                self.__root_index,
                self.__idf,
                ' '.join(self.__info),
                self.__note,
                self.__etml_note,
            ]
        )).strip()

    def __eq__(self, other):
        self_name = self.clean_string
        other_name = other.clean_string
        return self_name == other_name

    def __ne__(self, other):
        self_name = self.clean_string
        other_name = other.clean_string
        return self_name != other_name

    def __gt__(self, other):
        self_name = self.clean_string
        other_name = other.clean_string
        return self_name > other_name

    def __lt__(self, other):
        self_name = self.clean_string
        other_name = other.clean_string
        return self_name < other_name

    @property
    def invisible(self):
        return self.__invisible

    @invisible.setter
    def invisible(self, invisible):
        self.__invisible = invisible

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def root_index(self):
        return self.__root_index

    @root_index.setter
    def root_index(self, root_index):
        self.__root_index = root_index

    @property
    def idf(self):
        return self.__idf

    @idf.setter
    def idf(self, idf):
        self.__idf = idf

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, info):
        self.__info = info

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note):
        self.__note = note

    @property
    def et_note(self):
        return self.__etml_note

    @et_note.setter
    def et_note(self, et_note):
        self.__etml_note = et_note

    @property
    def clean_string(self):
        return ' '.join(filter(
            None,
            [
                self.__invisible,
                self.__name.replace('*', '').strip().lower(),
                self.__root_index,
                self.__idf,
                ' '.join(self.__info),
                self.__note,
                self.__etml_note,
            ]
        )).strip()

    @property
    def dict_form(self):
        return OrderedDict({
            'invisible': self.__invisible,
            'name': self.__name,
            'root_index': self.__root_index,
            'idf': self.__idf,
            'info': self.__info,
            'note': self.__note,
            'etymological_note': self.__etml_note,
        })

    @property
    def list_form(self):
        return [
            self.__invisible,
            self.__name,
            self.__root_index,
            self.__idf,
            self.__info,
            self.__note,
            self.__etml_note,
        ]


class SocketSubGroupWordForm:
    def __init__(self, socket_word_forms: list):
        self.__title_word_form = socket_word_forms[0]
        self.__socket_word_forms = socket_word_forms

    def __repr__(self):
        return '\n'.join(str(x) for x in self.__socket_word_forms)

    @property
    def title_word_form(self):
        return self.__title_word_form

    @property
    def socket_word_forms(self):
        return self.__socket_word_forms

    @socket_word_forms.setter
    def socket_word_forms(self, socket_word_forms):
        self.__socket_word_forms = socket_word_forms


class SocketGroupWordForm:
    def __init__(self, s_groups: list):
        self.__sub_groups = s_groups

    def __repr__(self):
        return '\n\n'.join(str(x) for x in self.__sub_groups)

    @property
    def sub_groups(self):
        return self.__sub_groups

    @property
    def socket_word_forms(self):
        word_forms = []
        for sub_group in self.__sub_groups:
            word_forms += sub_group.socket_word_forms
        return word_forms

    @property
    def title_word_form(self):
        return self.socket_word_forms[0]
