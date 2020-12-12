from collections import OrderedDict

L_JUST_SIZE = 32


class WordForm:
    def __init__(self, name, idf):
        self._name = name
        self._idf = idf

    def __repr__(self):
        return ' '.join(filter(
            None,
            [self._name.ljust(L_JUST_SIZE), self._idf]
        )).strip()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def idf(self):
        return self._idf

    @idf.setter
    def idf(self, idf):
        self._idf = idf

    @property
    def dict_form(self):
        return OrderedDict({
            'name': self._name,
            'idf': self._idf,
        })

    @property
    def list_form(self):
        return [
            self._name,
            self._idf,
        ]


class TitleWordForm(WordForm):
    def __init__(self, name, idf, info: list, note):
        super().__init__(name, idf)
        self._info = info
        self._note = note

    def __repr__(self):
        return ' '.join(filter(
            None,
            [
                self._name.ljust(L_JUST_SIZE),
                self._idf,
                ' '.join(self._info),
                self._note
            ]
        )).strip()

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info):
        self._info = info

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, note):
        self._note = note

    @property
    def dict_form(self):
        return OrderedDict({
            'name': self._name,
            'idf': self._idf,
            'info': self._info,
            'note': self._note,
        })

    @property
    def list_form(self):
        return [
            self._name,
            self._idf,
            self._info,
            self._note,
        ]


class GroupWordForm:
    def __init__(self, title_word_form: TitleWordForm, word_forms: list):
        self._title_word_form = title_word_form
        self._word_forms = word_forms

    def __repr__(self):
        return '\n'.join(filter(None, (
            str(self._title_word_form),
            '\n'.join(str(x) for x in self._word_forms),
        )))

    @property
    def title_word_form(self):
        return self._title_word_form

    @title_word_form.setter
    def title_word_form(self, title_word_form):
        self._title_word_form = title_word_form

    @property
    def word_forms(self):
        return self._word_forms

    @word_forms.setter
    def word_forms(self, word_forms):
        self._word_forms = word_forms

    @property
    def dict_form(self):
        return OrderedDict({
            'title_word_form': self._title_word_form.dict_form,
            'word_forms': [x.dict_form for x in self._word_forms],
        })

    @property
    def list_form(self):
        return [
            self._title_word_form.list_form,
            [x.list_form for x in self._word_forms]
        ]
