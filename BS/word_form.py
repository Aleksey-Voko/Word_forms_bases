from collections import OrderedDict

L_JUST_SIZE = 32


class WordForm:
    def __init__(self, name, idf):
        self.__name = name
        self.__idf = idf

    def __repr__(self):
        return ' '.join(filter(
            None,
            [self.name.ljust(L_JUST_SIZE), self.idf]
        )).strip()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def idf(self):
        return self.__idf

    @idf.setter
    def idf(self, idf):
        self.__idf = idf

    @property
    def dict_form(self):
        return OrderedDict({
            'name': self.__name,
            'idf': self.__idf,
        })

    @property
    def list_form(self):
        return [
            self.__name,
            self.__idf,
        ]


class TitleWordForm(WordForm):
    def __init__(self, name, idf, info: list, note):
        super().__init__(name, idf)
        self.__info = info
        self.__note = note

    def __repr__(self):
        return ' '.join(filter(
            None,
            [
                self.name.ljust(L_JUST_SIZE),
                self.idf,
                ' '.join(self.info),
                self.note
            ]
        )).strip()

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
    def clean_string(self):
        return ' '.join(filter(
            None,
            [
                self.name.replace('*', '').lower(),
                self.idf,
                ' '.join(self.info),
                self.note
            ]
        )).strip()

    @property
    def dict_form(self):
        return (
                super().dict_form |
                OrderedDict({
                    'info': self.info,
                    'note': self.note,
                })
        )

    @property
    def list_form(self):
        return super().list_form + [self.info, self.note]


class GroupWordForm:
    def __init__(self, title_word_form: TitleWordForm, word_forms: list):
        self.__title_word_form = title_word_form
        self.__word_forms = word_forms

    def __repr__(self):
        return '\n'.join(filter(None, (
            str(self.title_word_form),
            '\n'.join(str(x) for x in self.word_forms),
        )))

    def __eq__(self, other):
        self_name = self.title_word_form.clean_string
        other_name = other.title_word_form.clean_string
        return self_name == other_name

    def __ne__(self, other):
        self_name = self.title_word_form.clean_string
        other_name = other.title_word_form.clean_string
        return self_name != other_name

    def __gt__(self, other):
        self_name = self.title_word_form.clean_string
        other_name = other.title_word_form.clean_string
        return self_name > other_name

    def __lt__(self, other):
        self_name = self.title_word_form.clean_string
        other_name = other.title_word_form.clean_string
        return self_name < other_name

    @property
    def title_word_form(self):
        return self.__title_word_form

    @title_word_form.setter
    def title_word_form(self, title_word_form):
        self.__title_word_form = title_word_form

    @property
    def word_forms(self):
        return self.__word_forms

    @word_forms.setter
    def word_forms(self, word_forms):
        self.__word_forms = word_forms

    @property
    def dict_form(self):
        return OrderedDict({
            'title_word_form': self.title_word_form.dict_form,
            'word_forms': [x.dict_form for x in self.word_forms],
        })

    @property
    def list_form(self):
        return [
            self.title_word_form.list_form,
            [x.list_form for x in self.word_forms]
        ]
