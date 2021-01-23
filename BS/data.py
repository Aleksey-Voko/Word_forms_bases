tmpl_word_forms_bases = [
    # group_word_form
    {
        'title_word_form': {
            'name': 'PS',
            'idf': '',
            'info': [],
            'note': '',
        },
        'word_forms': []
    },
    # ----------------------------------------
    # group_word_form
    {
        'title_word_form': {
            'name': 'SMS',
            'idf': '',
            'info': [],
            'note': '.* short message service',
        },
        'word_forms': []
    },
    # ----------------------------------------
    # group_word_form
    {
        'title_word_form': {
            'name': 'SMS-ка',
            'idf': '.СеИ',
            'info': [
                'неод',
                'жII2',
                'мнI16о'
            ],
            'note': '.* short message service',
        },
        'word_forms': [
            {'name': 'SMS-ки', 'idf': '.СеР'},
            {'name': 'SMS-ке', 'idf': '.СеД'},
            # ... #
            {'name': 'SMS-ках', 'idf': '.СмнП'},
        ],
    },
]

tmpl_socket_word_forms_bases = [
    # ---
    # socket
    [
        # sub_group
        [
            {
                'name': '* 5',
                'root_index': '',
                'idf': '',
                'info': [],
                'note': '',
                'etymological_note': '* <= five',
            },
            {
                'name': 'файф-о-клок',
                'root_index': '2',
                'idf': '.СеИ',
                'info': [
                    'неод',
                    'мI1',
                    'мнI1',
                ],
                'note': '',
                'etymological_note': '',
            },
        ],
        # sub_group
        [
            {
                'name': '* short',
                'root_index': '',
                'idf': '',
                'info': [],
                'note': '',
                'etymological_note': '',
            },
            {
                'name': 'шорт-лист',
                'root_index': '2*',
                'idf': '.СеИ',
                'info': [
                    'неод',
                    'мI1',
                    'мнII1',
                ],
                'note': '',
                'etymological_note': '',
            },
            {
                'name': 'SMS',
                'root_index': '3',
                'idf': '',
                'info': [],
                'note': '* short message service',
                'etymological_note': '',
            },
        ],
    ],
    # ---
]
