from collections import OrderedDict


class SocketWordForm:
    def __init__(self, name, root_index, idf, info: list, note, et_note):
        self.__name = name
        self.__root_index = root_index
        self.__idf = idf
        self.__info = info
        self.__note = note
        self.__et_note = et_note

    def __repr__(self):
        return ' '.join(filter(
            None,
            [
                self.__name,
                self.__root_index,
                self.__idf,
                ' '.join(self.__info),
                self.__note,
                self.__et_note,
            ]
        )).strip()

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
        return self.__et_note

    @et_note.setter
    def et_note(self, et_note):
        self.__et_note = et_note

    @property
    def clean_string(self):
        return ' '.join(filter(
            None,
            [
                self.__name.replace('*', '').lower().strip(),
                self.__root_index,
                self.__idf,
                ' '.join(self.__info),
                self.__note,
                self.__et_note,
            ]
        )).strip()

    @property
    def dict_form(self):
        return OrderedDict({
            'name': self.__name,
            'root_index': self.__root_index,
            'idf': self.__idf,
            'info': self.__info,
            'note': self.__note,
            'etymological_note': self.__et_note,
        })

    @property
    def list_form(self):
        return [
            self.__name,
            self.__root_index,
            self.__idf,
            self.__info,
            self.__note,
            self.__et_note,
        ]


class SocketSubGroupWordForm:
    def __init__(self, socket_word_forms: list):
        self.__socket_word_forms = socket_word_forms

    def __repr__(self):
        return '\n'.join(str(x) for x in self.__socket_word_forms)

    @property
    def socket_word_forms(self):
        return self.__socket_word_forms

    @socket_word_forms.setter
    def socket_word_forms(self, socket_word_forms):
        self.__socket_word_forms = socket_word_forms
