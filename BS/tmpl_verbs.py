from BS.word_form import WordForm


# Глаголы настоящее/будущее время
def get_present_future_forms(src_dict) -> list:
    present_future = {
        'НБI-II3': present_future_nbi_ii3,
        'НБI-II4ч': present_future_nbi_ii4ch,
        'НБI1': present_future_nbi1,
        'НБI2в': present_future_nbi2v,
        'НБI2г': present_future_nbi2g,
        'НБI2н': present_future_nbi2n,
        'НБI3': present_future_nbi3,
        'НБI3-': present_future_nbi3_dash,
        'НБI3&6ч': present_future_nbi3_6ch,
        'НБI3&6ш': present_future_nbi3_6sh,
        'НБI4': present_future_nbi4,
        'НБI4-': present_future_nbi4_dash,
        'НБI4б': present_future_nbi4b,
        'НБI4д': present_future_nbi4d,
        'НБI4м': present_future_nbi4m,
        'НБI4н': present_future_nbi4n,
        'НБI5': present_future_nbi5,
        'НБI5л&I-II1': present_future_nbi5l_and_i_ii1,
        'НБI5о': present_future_nbi5o,
        'НБI6ж': present_future_nbi6g,
        'НБI6ч': present_future_nbi6ch,
        'НБI6ч-': present_future_nbi6ch_dash,
        'НБI6ш': present_future_nbi6sh,
        'НБI7': present_future_nbi7,
        'НБI8щ': present_future_nbi8shch,
        'НБI9е': present_future_nbi9e,
        'НБI9у': present_future_nbi9u,
        'НБI9ю': present_future_nbi9yu,
        'НБII1': present_future_nbii1,
        'НБII1-': present_future_nbii1_dash,
        'НБII2': present_future_nbii2,
        'НБII2л': present_future_nbii2l,
        'НБII3-': present_future_nbii3_dash,
        'НБII2+3ж': present_future_nbii2_and_3g,
        'НБII3ж': present_future_nbii3g,
        'НБII3ч': present_future_nbii3ch,
        'НБII3ш': present_future_nbii3sh,
        'НБII3щ': present_future_nbii3shch,
        'НБII5щ': present_future_nbii5shch,
    }
    return present_future[src_dict['Inf_3']](src_dict)


# НБI-II3
def present_future_nbi_ii3(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}у', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ышь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ыт', '.ГНБ3е'),
            WordForm(f'{name[:-3]}ым', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ыте', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}усь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ышься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ытся', '.ГНБ3е'),
            WordForm(f'{name[:-5]}ымся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}ытесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}утся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI-II4ч
def present_future_nbi_ii4ch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}чу', '.ГНБ1е'),
            WordForm(f'{name[:-4]}чешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}чет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}чусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}чешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}чется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI1
def present_future_nbi1(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-1]}у', '.ГНБ1е'),
            WordForm(f'{name[:-1]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-1]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-1]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-1]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-1]}ут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-3]}усь', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-3]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}утся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2в
def present_future_nbi2v(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ву', '.ГНБ1е'),
            WordForm(f'{name[:-2]}вешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}вет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}вем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}вете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}вут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}вусь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}вешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}вется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}вемся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}ветесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}вутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2г
def present_future_nbi2g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}гу', '.ГНБ1е'),
            WordForm(f'{name[:-2]}жешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}жет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}жем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}жете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}гут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}гусь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}жешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}жется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}жемся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}жетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}гутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2н
def present_future_nbi2n(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ну', '.ГНБ1е'),
            WordForm(f'{name[:-2]}нешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}нет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}нем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}нете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}нут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}нусь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}нешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}нется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}немся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}нетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}нутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI3
def present_future_nbi3(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ю', '.ГНБ1е'),
            WordForm(f'{name[:-2]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}ют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}юсь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}ются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI3-
def present_future_nbi3_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}ется', '.ГНБ3е'),
        ]
    return word_forms


# НБI3&6ч
def present_future_nbi3_6ch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ю', '.ГНБ1е1'),
            WordForm(f'{name[:-4]}чу', '.ГНБ1е2'),
            WordForm(f'{name[:-2]}ешь', '.ГНБ2е1'),
            WordForm(f'{name[:-4]}чешь', '.ГНБ2е2'),
            WordForm(f'{name[:-2]}ет', '.ГНБ3е1'),
            WordForm(f'{name[:-4]}чет', '.ГНБ3е2'),
            WordForm(f'{name[:-2]}ем', '.ГНБ1мн1'),
            WordForm(f'{name[:-4]}чем', '.ГНБ1мн2'),
            WordForm(f'{name[:-2]}ете', '.ГНБ2мн1'),
            WordForm(f'{name[:-4]}чете', '.ГНБ2мн2'),
            WordForm(f'{name[:-2]}ют', '.ГНБ3мн1'),
            WordForm(f'{name[:-4]}чут', '.ГНБ3мн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}юсь', '.ГНБ1е1'),
            WordForm(f'{name[:-6]}чусь', '.ГНБ1е2'),
            WordForm(f'{name[:-4]}ешься', '.ГНБ2е1'),
            WordForm(f'{name[:-6]}чешься', '.ГНБ2е2'),
            WordForm(f'{name[:-4]}ется', '.ГНБ3е1'),
            WordForm(f'{name[:-6]}чется', '.ГНБ3е2'),
            WordForm(f'{name[:-4]}емся', '.ГНБ1мн1'),
            WordForm(f'{name[:-6]}чемся', '.ГНБ1мн2'),
            WordForm(f'{name[:-4]}етесь', '.ГНБ2мн1'),
            WordForm(f'{name[:-6]}четесь', '.ГНБ2мн2'),
            WordForm(f'{name[:-4]}ются', '.ГНБ3мн1'),
            WordForm(f'{name[:-6]}чутся', '.ГНБ3мн2'),
        ]
    return word_forms


# НБI3&6ш
def present_future_nbi3_6sh(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ю', '.ГНБ1е1'),
            WordForm(f'{name[:-4]}шу', '.ГНБ1е2'),
            WordForm(f'{name[:-2]}ешь', '.ГНБ2е1'),
            WordForm(f'{name[:-4]}шешь', '.ГНБ2е2'),
            WordForm(f'{name[:-2]}ет', '.ГНБ3е1'),
            WordForm(f'{name[:-4]}шет', '.ГНБ3е2'),
            WordForm(f'{name[:-2]}ем', '.ГНБ1мн1'),
            WordForm(f'{name[:-4]}шем', '.ГНБ1мн2'),
            WordForm(f'{name[:-2]}ете', '.ГНБ2мн1'),
            WordForm(f'{name[:-4]}шете', '.ГНБ2мн2'),
            WordForm(f'{name[:-2]}ют', '.ГНБ3мн1'),
            WordForm(f'{name[:-4]}шут', '.ГНБ3мн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}юсь', '.ГНБ1е1'),
            WordForm(f'{name[:-6]}шусь', '.ГНБ1е2'),
            WordForm(f'{name[:-4]}ешься', '.ГНБ2е1'),
            WordForm(f'{name[:-6]}шешься', '.ГНБ2е2'),
            WordForm(f'{name[:-4]}ется', '.ГНБ3е1'),
            WordForm(f'{name[:-6]}шется', '.ГНБ3е2'),
            WordForm(f'{name[:-4]}емся', '.ГНБ1мн1'),
            WordForm(f'{name[:-6]}шемся', '.ГНБ1мн2'),
            WordForm(f'{name[:-4]}етесь', '.ГНБ2мн1'),
            WordForm(f'{name[:-6]}шетесь', '.ГНБ2мн2'),
            WordForm(f'{name[:-4]}ются', '.ГНБ3мн1'),
            WordForm(f'{name[:-6]}шутся', '.ГНБ3мн2'),
        ]
    return word_forms


# НБI4
def present_future_nbi4(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}у', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}усь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}утся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4-
def present_future_nbi4_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ется', '.ГНБ3е'),
        ]
    return word_forms


# НБI4б
def present_future_nbi4b(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}бу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}бешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}бет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}бем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}бете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}бут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}бусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}бешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}бется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}бемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}бетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}бутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4д
def present_future_nbi4d(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ду', '.ГНБ1е'),
            WordForm(f'{name[:-3]}дешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}дет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}дем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}дете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}дут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}дусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}дешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}дется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}демся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}детесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}дутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4м
def present_future_nbi4m(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}му', '.ГНБ1е'),
            WordForm(f'{name[:-3]}мешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}мет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}мем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}мете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}мут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}мусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}мешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}мется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}мемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}метесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}мутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4н
def present_future_nbi4n(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ну', '.ГНБ1е'),
            WordForm(f'{name[:-3]}нешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}нет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}нем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}нете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}нут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}нусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}нешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}нется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}немся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}нетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}нутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5
def present_future_nbi5(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ю', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}юсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5л&I-II1
def present_future_nbi5l_and_i_ii1(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}лю', '.ГНБ1е'),
            WordForm(f'{name[:-3]}лешь', '.ГНБ2е1'),
            WordForm(f'{name[:-3]}ешь', '.ГНБ2е2'),
            WordForm(f'{name[:-3]}лет', '.ГНБ3е1'),
            WordForm(f'{name[:-3]}ет', '.ГНБ3е2'),
            WordForm(f'{name[:-3]}лем', '.ГНБ1мн1'),
            WordForm(f'{name[:-3]}ем', '.ГНБ1мн2'),
            WordForm(f'{name[:-3]}лете', '.ГНБ2мн1'),
            WordForm(f'{name[:-3]}ете', '.ГНБ2мн2'),
            WordForm(f'{name[:-3]}лют', '.ГНБ3мн1'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}люсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}лешься', '.ГНБ2е1'),
            WordForm(f'{name[:-5]}ешься', '.ГНБ2е2'),
            WordForm(f'{name[:-5]}лется', '.ГНБ3е1'),
            WordForm(f'{name[:-5]}ется', '.ГНБ3е2'),
            WordForm(f'{name[:-5]}лемся', '.ГНБ1мн1'),
            WordForm(f'{name[:-5]}емся', '.ГНБ1мн2'),
            WordForm(f'{name[:-5]}летесь', '.ГНБ2мн1'),
            WordForm(f'{name[:-5]}етесь', '.ГНБ2мн2'),
            WordForm(f'{name[:-5]}лются', '.ГНБ3мн1'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн2'),
        ]
    return word_forms


# НБI5о
def present_future_nbi5o(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ою', '.ГНБ1е'),
            WordForm(f'{name[:-3]}оешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}оет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}оем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}оете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}оют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}оюсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}оешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}оется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}оемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}оетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}оются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6ж
def present_future_nbi6g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}жу', '.ГНБ1е'),
            WordForm(f'{name[:-4]}жешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}жет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}жем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}жете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}жут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}жусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}жешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}жется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}жемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}жетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}жутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6ч
def present_future_nbi6ch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}чу', '.ГНБ1е'),
            WordForm(f'{name[:-4]}чешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}чет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}чем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}чете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}чут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}чусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}чешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}чется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}чемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}четесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}чутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6ч-
def present_future_nbi6ch_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}чет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}чется', '.ГНБ3е'),
        ]
    return word_forms


# НБI6ш
def present_future_nbi6sh(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}шу', '.ГНБ1е'),
            WordForm(f'{name[:-4]}шешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}шет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}шем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}шете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}шут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}шусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}шешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}шется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}шемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}шетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}шутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI7
def present_future_nbi7(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}ю', '.ГНБ1е'),
            WordForm(f'{name[:-4]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}ют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}юсь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}ются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8щ
def present_future_nbi8shch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}щу', '.ГНБ1е'),
            WordForm(f'{name[:-5]}щешь', '.ГНБ2е'),
            WordForm(f'{name[:-5]}щет', '.ГНБ3е'),
            WordForm(f'{name[:-5]}щем', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}щете', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}щут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}щусь', '.ГНБ1е'),
            WordForm(f'{name[:-7]}щешься', '.ГНБ2е'),
            WordForm(f'{name[:-7]}щется', '.ГНБ3е'),
            WordForm(f'{name[:-7]}щемся', '.ГНБ1мн'),
            WordForm(f'{name[:-7]}щетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-7]}щутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI9е
def present_future_nbi9e(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}елю', '.ГНБ1е'),
            WordForm(f'{name[:-5]}елешь', '.ГНБ2е'),
            WordForm(f'{name[:-5]}елет', '.ГНБ3е'),
            WordForm(f'{name[:-5]}елем', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}елете', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}елют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}елюсь', '.ГНБ1е'),
            WordForm(f'{name[:-7]}елешься', '.ГНБ2е'),
            WordForm(f'{name[:-7]}елется', '.ГНБ3е'),
            WordForm(f'{name[:-7]}елемся', '.ГНБ1мн'),
            WordForm(f'{name[:-7]}елетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-7]}елются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI9у
def present_future_nbi9u(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}ую', '.ГНБ1е'),
            WordForm(f'{name[:-5]}уешь', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ует', '.ГНБ3е'),
            WordForm(f'{name[:-5]}уем', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}уете', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}уют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}уюсь', '.ГНБ1е'),
            WordForm(f'{name[:-7]}уешься', '.ГНБ2е'),
            WordForm(f'{name[:-7]}уется', '.ГНБ3е'),
            WordForm(f'{name[:-7]}уемся', '.ГНБ1мн'),
            WordForm(f'{name[:-7]}уетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-7]}уются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI9ю
def present_future_nbi9yu(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}юю', '.ГНБ1е'),
            WordForm(f'{name[:-5]}юешь', '.ГНБ2е'),
            WordForm(f'{name[:-5]}юет', '.ГНБ3е'),
            WordForm(f'{name[:-5]}юем', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}юете', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}юют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}ююсь', '.ГНБ1е'),
            WordForm(f'{name[:-7]}юешься', '.ГНБ2е'),
            WordForm(f'{name[:-7]}юется', '.ГНБ3е'),
            WordForm(f'{name[:-7]}юемся', '.ГНБ1мн'),
            WordForm(f'{name[:-7]}юетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-7]}юются', '.ГНБ3мн'),
        ]
    return word_forms


# НБII1
def present_future_nbii1(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}у', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ат', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}усь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}атся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII1-
def present_future_nbii1_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
        ]
    return word_forms


# НБII2
def present_future_nbii2(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ю', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}юсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII2л
def present_future_nbii2l(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}лю', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}люсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII3-
def present_future_nbii3_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII2+3ж
def present_future_nbii2_and_3g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ю', '.ГНБ1е1'),
            WordForm(f'{name[:-4]}жу', '.ГНБ1е2'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}юсь', '.ГНБ1е1'),
            WordForm(f'{name[:-6]}жусь', '.ГНБ1е2'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII3ж
def present_future_nbii3g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}жу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}жусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII3ч
def present_future_nbii3ch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}чу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}чусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII3ш
def present_future_nbii3sh(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}шу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}шусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII3щ
def present_future_nbii3shch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}щу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}щусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII5щ
def present_future_nbii5shch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}щу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}щусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# ############################################################
# Глаголы прошедшее время
def get_past_tense_forms(src_dict) -> list:
    past_tense = {
        'П1': past_tense_p1,
        'П1-': past_tense_p1_dash,
        'П10о': past_tense_p10o,
        'П2': past_tense_p2,
        'П3г': past_tense_p3g,
        'П5': past_tense_p5,
        'П7б': past_tense_p7b,
        'П9': past_tense_p9,
    }
    return past_tense[src_dict['Inf_4']](src_dict)


# П1
def past_tense_p1(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-2]}л'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}а', '.ГПж'),
            WordForm(f'{gpm}о', '.ГПс'),
            WordForm(f'{gpm}и', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-4]}лся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}ась', '.ГПж'),
            WordForm(f'{gpm[:-2]}ось', '.ГПс'),
            WordForm(f'{gpm[:-2]}ись', '.ГПмн'),
        ]
    return word_forms


# П1-
def past_tense_p1_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ло', '.ГПс'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}лось', '.ГПс'),
        ]
    return word_forms


# П10о
def past_tense_p10o(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-4]}ос'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-6]}осся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# П2
def past_tense_p2(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}л', '.ГПм'),
            WordForm(f'{name[:-4]}ла', '.ГПж'),
            WordForm(f'{name[:-4]}ло', '.ГПс'),
            WordForm(f'{name[:-4]}ли', '.ГПмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}лся', '.ГПм'),
            WordForm(f'{name[:-6]}лась', '.ГПж'),
            WordForm(f'{name[:-6]}лось', '.ГПс'),
            WordForm(f'{name[:-6]}лись', '.ГПмн'),
        ]
    return word_forms


# П3г
def past_tense_p3g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-2]}г'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-4]}гся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# П5
def past_tense_p5(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-3]}л'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}а', '.ГПж'),
            WordForm(f'{gpm}о', '.ГПс'),
            WordForm(f'{gpm}и', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-5]}лся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}ась', '.ГПж'),
            WordForm(f'{gpm[:-2]}ось', '.ГПс'),
            WordForm(f'{gpm[:-2]}ись', '.ГПмн'),
        ]
    return word_forms


# П7б
def past_tense_p7b(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-3]}б'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-5]}бся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# П9
def past_tense_p9(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-4]}'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-6]}ся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# ############################################################
# Глаголы повелительное наклонение
def get_imperative_mood_forms(src_dict) -> list:
    imperative_mood = {
        'Пв1': imperative_mood_pv1,
        'Пв1-': imperative_mood_pv1_dash,
        'Пв1*': imperative_mood_pv1_prim,
        'Пв1|2': imperative_mood_pv1_2,
        'Пв1|3': imperative_mood_pv1_3,
        'Пв2': imperative_mood_pv2,
        'Пв2-': imperative_mood_pv2_dash,
        'Пв2!': imperative_mood_pv2_excl,
        'Пв2!&3': imperative_mood_pv2_excl_and_3,
        'Пв2**': imperative_mood_pv2_2prim,
        'Пв2**-': imperative_mood_pv2_2prim_dash,
        'Пв2|2': imperative_mood_pv2_2,
        'Пв3': imperative_mood_pv3,
        'Пв3-': imperative_mood_pv3_dash,
        'Пв4': imperative_mood_pv4,
    }
    return imperative_mood[src_dict['Inf_5']](src_dict)


# Пв1
def imperative_mood_pv1(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve = f'{gnb3mn[:-2]}й'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{gnb3mn[:-4]}йся'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв1-
def imperative_mood_pv1_dash(src_dict) -> list:
    name = src_dict['name']
    gnb3e = list(filter(
        lambda x: x.idf == '.ГНБ3е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3e[:-2]}й', '.ГПве'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3e[:-4]}йся', '.ГПве'),
        ]
    return word_forms


# Пв1*
def imperative_mood_pv1_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpve = f'{name[:-2]}й'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{name[:-4]}йся'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв1|2
def imperative_mood_pv1_2(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve1 = f'{gnb3mn1[:-2]}й'
        gpve2 = f'{gnb3mn2[:-2]}и'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(f'{gpve2}те', '.ГПвмн2'),
        ]
    else:
        gpve1 = f'{gnb3mn1[:-4]}йся'
        gpve2 = f'{gnb3mn2[:-4]}ись'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(f'{gpve2[:-2]}тесь', '.ГПвмн2'),
        ]
    return word_forms


# Пв1|3
def imperative_mood_pv1_3(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve1 = f'{gnb3mn1[:-2]}й'
        gpve2 = f'{gnb3mn2[:-2]}ь'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(f'{gpve2}те', '.ГПвмн2'),
        ]
    else:
        gpve1 = f'{gnb3mn1[:-4]}йся'
        gpve2 = f'{gnb3mn2[:-4]}ься'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(f'{gpve2[:-2]}тесь', '.ГПвмн2'),
        ]
    return word_forms


# Пв2
def imperative_mood_pv2(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve = f'{gnb3mn[:-2]}и'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{gnb3mn[:-4]}ись'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв2-
def imperative_mood_pv2_dash(src_dict) -> list:
    name = src_dict['name']
    gnb3e = list(filter(
        lambda x: x.idf == '.ГНБ3е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3e[:-2]}и', '.ГПве'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3e[:-4]}ись', '.ГПве'),
        ]
    return word_forms


# Пв2!
def imperative_mood_pv2_excl(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2mn = list(filter(
        lambda x: x.idf == '.ГНБ2мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3mn[:-2]}и', '.ГПве'),
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3mn[:-4]}ись', '.ГПве'),
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    return word_forms


# Пв2!&3
def imperative_mood_pv2_excl_and_3(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2mn = list(filter(
        lambda x: x.idf == '.ГНБ2мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3mn[:-2]}и', '.ГПве1'),
            WordForm(f'{gnb3mn[:-2]}ь', '.ГПве2'),
            WordForm(gnb2mn, '.ГПвмн1'),
            WordForm(f'{gnb3mn[:-2]}ьте', '.ГПвмн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3mn[:-4]}ись', '.ГПве1'),
            WordForm(f'{gnb3mn[:-4]}ься', '.ГПве2'),
            WordForm(gnb2mn, '.ГПвмн1'),
            WordForm(f'{gnb3mn[:-4]}ьтесь', '.ГПвмн2'),
        ]
    return word_forms


# Пв2**
def imperative_mood_pv2_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(name, '.ГПве'),
            WordForm(f'{name}те', '.ГПвмн'),
        ]
    else:
        word_forms = [
            WordForm(name, '.ГПве'),
            WordForm(f'{name[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв2**-
def imperative_mood_pv2_2prim_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}и', '.ГПве'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ись', '.ГПве'),
        ]
    return word_forms


# Пв2|2
def imperative_mood_pv2_2(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve1 = f'{gnb3mn1[:-2]}и'
        gpve2 = f'{gnb3mn2[:-2]}и'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(f'{gpve2}те', '.ГПвмн2'),
        ]
    else:
        gpve1 = f'{gnb3mn1[:-4]}ись'
        gpve2 = f'{gnb3mn2[:-4]}ись'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(f'{gpve2[:-2]}тесь', '.ГПвмн2'),
        ]
    return word_forms


# Пв3
def imperative_mood_pv3(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve = f'{gnb3mn[:-2]}ь'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{gnb3mn[:-4]}ься'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв3-
def imperative_mood_pv3_dash(src_dict) -> list:
    name = src_dict['name']
    gnb3e = list(filter(
        lambda x: x.idf == '.ГНБ3е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3e[:-2]}ь', '.ГПве'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3e[:-4]}ься', '.ГПве'),
        ]
    return word_forms


# Пв4
def imperative_mood_pv4(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2mn = list(filter(
        lambda x: x.idf == '.ГНБ2мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3mn[:-2]}ы', '.ГПве'),
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3mn[:-4]}ысь', '.ГПве'),
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    return word_forms


# ############################################################
# Глаголы форма совместного действия
def get_joint_action_forms(src_dict) -> list:
    joint_action = {
        'С': joint_action_c,
        'С(2)': joint_action_c2,
    }
    return joint_action[src_dict['Inf_6']](src_dict)


# С
def joint_action_c(src_dict) -> list:
    name = src_dict['name']
    gnb1mn = list(filter(
        lambda x: x.idf == '.ГНБ1мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb1mn}те', '.ГСДмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb1mn[:-2]}тесь', '.ГСДмн'),
        ]
    return word_forms


# С(2)
def joint_action_c2(src_dict) -> list:
    name = src_dict['name']
    gnb1mn1 = list(filter(
        lambda x: x.idf == '.ГНБ1мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb1mn2 = list(filter(
        lambda x: x.idf == '.ГНБ1мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb1mn1}те', '.ГСДмн1'),
            WordForm(f'{gnb1mn2}те', '.ГСДмн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb1mn1[:-2]}тесь', '.ГСДмн1'),
            WordForm(f'{gnb1mn2[:-2]}тесь', '.ГСДмн2'),
        ]
    return word_forms


# ############################################################
#  Причастие настоящего времени действительное
def get_present_participle_is_valid(src_dict) -> list:
    present_participle = {
        'ПНД1': present_participle_is_valid_pnd1,
    }
    return present_participle[src_dict['Inf_7']](src_dict)


# ПНД1
def present_participle_is_valid_pnd1(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        pndmi = f'{gnb3mn[:-1]}щий'
        word_forms = [
            WordForm(pndmi, '.ПНДмИ'),
            WordForm(f'{pndmi[:-2]}его', '.ПНДмР'),
            WordForm(f'{pndmi[:-2]}ему', '.ПНДмД'),
            WordForm(pndmi, '.ПНДмВ'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДмТ'),
            WordForm(f'{pndmi[:-2]}ем', '.ПНДмП'),
            WordForm(f'{pndmi[:-2]}ая', '.ПНДжИ'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжР'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжД'),
            WordForm(f'{pndmi[:-2]}ую', '.ПНДжВ'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжТ1'),
            WordForm(f'{pndmi[:-2]}ею', '.ПНДжТ2'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжП'),
            WordForm(f'{pndmi[:-2]}ее', '.ПНДсИ'),
            WordForm(f'{pndmi[:-2]}его', '.ПНДсР'),
            WordForm(f'{pndmi[:-2]}ему', '.ПНДсД'),
            WordForm(f'{pndmi[:-2]}ее', '.ПНДсВ'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДсТ'),
            WordForm(f'{pndmi[:-2]}ем', '.ПНДсП'),
            WordForm(f'{pndmi[:-2]}ие', '.ПНДмнИ'),
            WordForm(f'{pndmi[:-2]}их', '.ПНДмнР'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДмнД'),
            WordForm(f'{pndmi[:-2]}ие', '.ПНДмнВ'),
            WordForm(f'{pndmi[:-2]}ими', '.ПНДмнТ'),
            WordForm(f'{pndmi[:-2]}их', '.ПНДмнП'),
        ]
    else:
        pndmi = f'{gnb3mn[:-3]}щийся'
        word_forms = [
            WordForm(pndmi, '.ПНДмИ'),
            WordForm(f'{pndmi[:-4]}егося', '.ПНДмР'),
            WordForm(f'{pndmi[:-4]}емуся', '.ПНДмД'),
            WordForm(pndmi, '.ПНДмВ'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДмТ'),
            WordForm(f'{pndmi[:-4]}емся', '.ПНДмП'),
            WordForm(f'{pndmi[:-4]}аяся', '.ПНДжИ'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжР'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжД'),
            WordForm(f'{pndmi[:-4]}уюся', '.ПНДжВ'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжТ1'),
            WordForm(f'{pndmi[:-4]}еюся', '.ПНДжТ2'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжП'),
            WordForm(f'{pndmi[:-4]}ееся', '.ПНДсИ'),
            WordForm(f'{pndmi[:-4]}егося', '.ПНДсР'),
            WordForm(f'{pndmi[:-4]}емуся', '.ПНДсД'),
            WordForm(f'{pndmi[:-4]}ееся', '.ПНДсВ'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДсТ'),
            WordForm(f'{pndmi[:-4]}емся', '.ПНДсП'),
            WordForm(f'{pndmi[:-4]}иеся', '.ПНДмнИ'),
            WordForm(f'{pndmi[:-4]}ихся', '.ПНДмнР'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДмнД'),
            WordForm(f'{pndmi[:-4]}иеся', '.ПНДмнВ'),
            WordForm(f'{pndmi[:-4]}имися', '.ПНДмнТ'),
            WordForm(f'{pndmi[:-4]}ихся', '.ПНДмнП'),
        ]
    return word_forms


# ############################################################
#  Причастие настоящего времени страдательное
def get_passive_present_participle(src_dict) -> list:
    passive_present = {
        'ПНС1': passive_present_participle_pns1,
        'ПНС2': passive_present_participle_pns2,
    }
    return passive_present[src_dict['Inf_8']](src_dict)


# ПНС1
def passive_present_participle_pns1(src_dict) -> list:
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb1mn = list(filter(
        lambda x: x.idf == '.ГНБ1мн',
        get_present_future_forms(src_dict)
    ))[0].name

    pnsmi = f'{gnb3mn[:-2]}емый'
    word_forms = [
        WordForm(pnsmi, '.ПНСмИ'),
        WordForm(f'{pnsmi[:-2]}ого', '.ПНСмР'),
        WordForm(f'{pnsmi[:-2]}ому', '.ПНСмД'),
        WordForm(pnsmi, '.ПНСмВ'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСмТ'),
        WordForm(f'{pnsmi[:-2]}ом', '.ПНСмП'),
        WordForm(f'{pnsmi[:-2]}ая', '.ПНСжИ'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжР'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжД'),
        WordForm(f'{pnsmi[:-2]}ую', '.ПНСжВ'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжТ1'),
        WordForm(f'{pnsmi[:-2]}ою', '.ПНСжТ2'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжП'),
        WordForm(f'{pnsmi[:-2]}ое', '.ПНСсИ'),
        WordForm(f'{pnsmi[:-2]}ого', '.ПНСсР'),
        WordForm(f'{pnsmi[:-2]}ому', '.ПНСсД'),
        WordForm(f'{pnsmi[:-2]}ое', '.ПНСсВ'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСсТ'),
        WordForm(f'{pnsmi[:-2]}ом', '.ПНСсП'),
        WordForm(f'{pnsmi[:-2]}ые', '.ПНСмнИ'),
        WordForm(f'{pnsmi[:-2]}ых', '.ПНСмнР'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСмнД'),
        WordForm(f'{pnsmi[:-2]}ые', '.ПНСмнВ'),
        WordForm(f'{pnsmi[:-2]}ыми', '.ПНСмнТ'),
        WordForm(f'{pnsmi[:-2]}ых', '.ПНСмнП'),
        WordForm(gnb1mn, '.ПНСКм'),
        WordForm(f'{pnsmi[:-2]}а', '.ПНСКж'),
        WordForm(f'{pnsmi[:-2]}о', '.ПНСКс'),
        WordForm(f'{pnsmi[:-2]}ы', '.ПНСКмн'),
    ]

    return word_forms


# ПНС2
def passive_present_participle_pns2(src_dict) -> list:
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb1mn = list(filter(
        lambda x: x.idf == '.ГНБ1мн',
        get_present_future_forms(src_dict)
    ))[0].name

    pnsmi = f'{gnb3mn[:-2]}имый'
    word_forms = [
        WordForm(pnsmi, '.ПНСмИ'),
        WordForm(f'{pnsmi[:-2]}ого', '.ПНСмР'),
        WordForm(f'{pnsmi[:-2]}ому', '.ПНСмД'),
        WordForm(pnsmi, '.ПНСмВ'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСмТ'),
        WordForm(f'{pnsmi[:-2]}ом', '.ПНСмП'),
        WordForm(f'{pnsmi[:-2]}ая', '.ПНСжИ'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжР'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжД'),
        WordForm(f'{pnsmi[:-2]}ую', '.ПНСжВ'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжТ1'),
        WordForm(f'{pnsmi[:-2]}ою', '.ПНСжТ2'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжП'),
        WordForm(f'{pnsmi[:-2]}ое', '.ПНСсИ'),
        WordForm(f'{pnsmi[:-2]}ого', '.ПНСсР'),
        WordForm(f'{pnsmi[:-2]}ому', '.ПНСсД'),
        WordForm(f'{pnsmi[:-2]}ое', '.ПНСсВ'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСсТ'),
        WordForm(f'{pnsmi[:-2]}ом', '.ПНСсП'),
        WordForm(f'{pnsmi[:-2]}ые', '.ПНСмнИ'),
        WordForm(f'{pnsmi[:-2]}ых', '.ПНСмнР'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСмнД'),
        WordForm(f'{pnsmi[:-2]}ые', '.ПНСмнВ'),
        WordForm(f'{pnsmi[:-2]}ыми', '.ПНСмнТ'),
        WordForm(f'{pnsmi[:-2]}ых', '.ПНСмнП'),
        WordForm(gnb1mn, '.ПНСКм'),
        WordForm(f'{pnsmi[:-2]}а', '.ПНСКж'),
        WordForm(f'{pnsmi[:-2]}о', '.ПНСКс'),
        WordForm(f'{pnsmi[:-2]}ы', '.ПНСКмн'),
    ]

    return word_forms


# ############################################################
#   Причастие прошедшего времени действительное
def get_past_participle_is_valid(src_dict) -> list:
    past_participle = {
        'ППД1в': past_participle_is_valid_ppd1v,
        'ППД2в': past_participle_is_valid_ppd2v,
        'ППД2в&5': past_participle_is_valid_ppd2v_and_5,
        'ППД5': past_participle_is_valid_ppd5,
    }
    return past_participle[src_dict['Inf_9']](src_dict)


# ППД1в
def past_participle_is_valid_ppd1v(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        ppdmi = f'{gpm[:-1]}вший'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДмР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДмП'),
            WordForm(f'{ppdmi[:-2]}ая', '.ППДжИ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжР'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжД'),
            WordForm(f'{ppdmi[:-2]}ую', '.ППДжВ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-2]}ею', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжП'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДсР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДсД'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДсТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДсП'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнР'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмнД'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-2]}ими', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнП'),
        ]
    else:
        ppdmi = f'{gpm[:-3]}вшийся'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДмР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДмП'),
            WordForm(f'{ppdmi[:-4]}аяся', '.ППДжИ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжР'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжД'),
            WordForm(f'{ppdmi[:-4]}уюся', '.ППДжВ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-4]}еюся', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжП'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДсР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДсД'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДсТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДсП'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнР'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмнД'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-4]}имися', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнП'),
        ]
    return word_forms


# ППД2в
def past_participle_is_valid_ppd2v(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        ppdmi = f'{name[:-2]}вший'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДмР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДмП'),
            WordForm(f'{ppdmi[:-2]}ая', '.ППДжИ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжР'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжД'),
            WordForm(f'{ppdmi[:-2]}ую', '.ППДжВ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-2]}ею', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжП'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДсР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДсД'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДсТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДсП'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнР'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмнД'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-2]}ими', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнП'),
        ]
    else:
        ppdmi = f'{name[:-4]}вшийся'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДмР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДмП'),
            WordForm(f'{ppdmi[:-4]}аяся', '.ППДжИ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжР'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжД'),
            WordForm(f'{ppdmi[:-4]}уюся', '.ППДжВ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-4]}еюся', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжП'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДсР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДсД'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДсТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДсП'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнР'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмнД'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-4]}имися', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнП'),
        ]
    return word_forms


# ППД2в&5
def past_participle_is_valid_ppd2v_and_5(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        ppdm1i = f'{name[:-2]}вший'
        ppdm2i = f'{name[:-4]}ший'
        word_forms = [
            WordForm(ppdm1i, '.ППД1мИ'),
            WordForm(f'{ppdm1i[:-2]}его', '.ППД1мР'),
            WordForm(f'{ppdm1i[:-2]}ему', '.ППД1мД'),
            WordForm(ppdm1i, '.ППД1мВ'),
            WordForm(f'{ppdm1i[:-2]}им', '.ППД1мТ'),
            WordForm(f'{ppdm1i[:-2]}ем', '.ППД1мП'),
            WordForm(f'{ppdm1i[:-2]}ая', '.ППД1жИ'),
            WordForm(f'{ppdm1i[:-2]}ей', '.ППД1жР'),
            WordForm(f'{ppdm1i[:-2]}ей', '.ППД1жД'),
            WordForm(f'{ppdm1i[:-2]}ую', '.ППД1жВ'),
            WordForm(f'{ppdm1i[:-2]}ей', '.ППД1жТ1'),
            WordForm(f'{ppdm1i[:-2]}ею', '.ППД1жТ2'),
            WordForm(f'{ppdm1i[:-2]}ей', '.ППД1жП'),
            WordForm(f'{ppdm1i[:-2]}ее', '.ППД1сИ'),
            WordForm(f'{ppdm1i[:-2]}его', '.ППД1сР'),
            WordForm(f'{ppdm1i[:-2]}ему', '.ППД1сД'),
            WordForm(f'{ppdm1i[:-2]}ее', '.ППД1сВ'),
            WordForm(f'{ppdm1i[:-2]}им', '.ППД1сТ'),
            WordForm(f'{ppdm1i[:-2]}ем', '.ППД1сП'),
            WordForm(f'{ppdm1i[:-2]}ие', '.ППД1мнИ'),
            WordForm(f'{ppdm1i[:-2]}их', '.ППД1мнР'),
            WordForm(f'{ppdm1i[:-2]}им', '.ППД1мнД'),
            WordForm(f'{ppdm1i[:-2]}ие', '.ППД1мнВ'),
            WordForm(f'{ppdm1i[:-2]}ими', '.ППД1мнТ'),
            WordForm(f'{ppdm1i[:-2]}их', '.ППД1мнП'),
            WordForm(ppdm2i, '.ППД2мИ'),
            WordForm(f'{ppdm2i[:-2]}его', '.ППД2мР'),
            WordForm(f'{ppdm2i[:-2]}ему', '.ППД2мД'),
            WordForm(ppdm2i, '.ППД2мВ'),
            WordForm(f'{ppdm2i[:-2]}им', '.ППД2мТ'),
            WordForm(f'{ppdm2i[:-2]}ем', '.ППД2мП'),
            WordForm(f'{ppdm2i[:-2]}ая', '.ППД2жИ'),
            WordForm(f'{ppdm2i[:-2]}ей', '.ППД2жР'),
            WordForm(f'{ppdm2i[:-2]}ей', '.ППД2жД'),
            WordForm(f'{ppdm2i[:-2]}ую', '.ППД2жВ'),
            WordForm(f'{ppdm2i[:-2]}ей', '.ППД2жТ1'),
            WordForm(f'{ppdm2i[:-2]}ею', '.ППД2жТ2'),
            WordForm(f'{ppdm2i[:-2]}ей', '.ППД2жП'),
            WordForm(f'{ppdm2i[:-2]}ее', '.ППД2сИ'),
            WordForm(f'{ppdm2i[:-2]}его', '.ППД2сР'),
            WordForm(f'{ppdm2i[:-2]}ему', '.ППД2сД'),
            WordForm(f'{ppdm2i[:-2]}ее', '.ППД2сВ'),
            WordForm(f'{ppdm2i[:-2]}им', '.ППД2сТ'),
            WordForm(f'{ppdm2i[:-2]}ем', '.ППД2сП'),
            WordForm(f'{ppdm2i[:-2]}ие', '.ППД2мнИ'),
            WordForm(f'{ppdm2i[:-2]}их', '.ППД2мнР'),
            WordForm(f'{ppdm2i[:-2]}им', '.ППД2мнД'),
            WordForm(f'{ppdm2i[:-2]}ие', '.ППД2мнВ'),
            WordForm(f'{ppdm2i[:-2]}ими', '.ППД2мнТ'),
            WordForm(f'{ppdm2i[:-2]}их', '.ППД2мнП'),
        ]
    else:
        ppdm1i = f'{name[:-4]}вшийся'
        ppdm2i = f'{name[:-6]}шийся'
        word_forms = [
            WordForm(ppdm1i, '.ППД1мИ'),
            WordForm(f'{ppdm1i[:-4]}егося', '.ППД1мР'),
            WordForm(f'{ppdm1i[:-4]}емуся', '.ППД1мД'),
            WordForm(ppdm1i, '.ППД1мВ'),
            WordForm(f'{ppdm1i[:-4]}имся', '.ППД1мТ'),
            WordForm(f'{ppdm1i[:-4]}емся', '.ППД1мП'),
            WordForm(f'{ppdm1i[:-4]}аяся', '.ППД1жИ'),
            WordForm(f'{ppdm1i[:-4]}ейся', '.ППД1жР'),
            WordForm(f'{ppdm1i[:-4]}ейся', '.ППД1жД'),
            WordForm(f'{ppdm1i[:-4]}уюся', '.ППД1жВ'),
            WordForm(f'{ppdm1i[:-4]}ейся', '.ППД1жТ1'),
            WordForm(f'{ppdm1i[:-4]}еюся', '.ППД1жТ2'),
            WordForm(f'{ppdm1i[:-4]}ейся', '.ППД1жП'),
            WordForm(f'{ppdm1i[:-4]}ееся', '.ППД1сИ'),
            WordForm(f'{ppdm1i[:-4]}егося', '.ППД1сР'),
            WordForm(f'{ppdm1i[:-4]}емуся', '.ППД1сД'),
            WordForm(f'{ppdm1i[:-4]}ееся', '.ППД1сВ'),
            WordForm(f'{ppdm1i[:-4]}имся', '.ППД1сТ'),
            WordForm(f'{ppdm1i[:-4]}емся', '.ППД1сП'),
            WordForm(f'{ppdm1i[:-4]}иеся', '.ППД1мнИ'),
            WordForm(f'{ppdm1i[:-4]}ихся', '.ППД1мнР'),
            WordForm(f'{ppdm1i[:-4]}имся', '.ППД1мнД'),
            WordForm(f'{ppdm1i[:-4]}иеся', '.ППД1мнВ'),
            WordForm(f'{ppdm1i[:-4]}имися', '.ППД1мнТ'),
            WordForm(f'{ppdm1i[:-4]}ихся', '.ППД1мнП'),
            WordForm(ppdm2i, '.ППД2мИ'),
            WordForm(f'{ppdm2i[:-4]}егося', '.ППД2мР'),
            WordForm(f'{ppdm2i[:-4]}емуся', '.ППД2мД'),
            WordForm(ppdm2i, '.ППД2мВ'),
            WordForm(f'{ppdm2i[:-4]}имся', '.ППД2мТ'),
            WordForm(f'{ppdm2i[:-4]}емся', '.ППД2мП'),
            WordForm(f'{ppdm2i[:-4]}аяся', '.ППД2жИ'),
            WordForm(f'{ppdm2i[:-4]}ейся', '.ППД2жР'),
            WordForm(f'{ppdm2i[:-4]}ейся', '.ППД2жД'),
            WordForm(f'{ppdm2i[:-4]}уюся', '.ППД2жВ'),
            WordForm(f'{ppdm2i[:-4]}ейся', '.ППД2жТ1'),
            WordForm(f'{ppdm2i[:-4]}еюся', '.ППД2жТ2'),
            WordForm(f'{ppdm2i[:-4]}ейся', '.ППД2жП'),
            WordForm(f'{ppdm2i[:-4]}ееся', '.ППД2сИ'),
            WordForm(f'{ppdm2i[:-4]}егося', '.ППД2сР'),
            WordForm(f'{ppdm2i[:-4]}емуся', '.ППД2сД'),
            WordForm(f'{ppdm2i[:-4]}ееся', '.ППД2сВ'),
            WordForm(f'{ppdm2i[:-4]}имся', '.ППД2сТ'),
            WordForm(f'{ppdm2i[:-4]}емся', '.ППД2сП'),
            WordForm(f'{ppdm2i[:-4]}иеся', '.ППД2мнИ'),
            WordForm(f'{ppdm2i[:-4]}ихся', '.ППД2мнР'),
            WordForm(f'{ppdm2i[:-4]}имся', '.ППД2мнД'),
            WordForm(f'{ppdm2i[:-4]}иеся', '.ППД2мнВ'),
            WordForm(f'{ppdm2i[:-4]}имися', '.ППД2мнТ'),
            WordForm(f'{ppdm2i[:-4]}ихся', '.ППД2мнП'),
        ]
    return word_forms


# ППД5
def past_participle_is_valid_ppd5(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        ppdmi = f'{name[:-4]}ший'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДмР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДмП'),
            WordForm(f'{ppdmi[:-2]}ая', '.ППДжИ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжР'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжД'),
            WordForm(f'{ppdmi[:-2]}ую', '.ППДжВ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-2]}ею', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжП'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДсР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДсД'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДсТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДсП'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнР'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмнД'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-2]}ими', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнП'),
        ]
    else:
        ppdmi = f'{name[:-6]}шийся'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДмР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДмП'),
            WordForm(f'{ppdmi[:-4]}аяся', '.ППДжИ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжР'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжД'),
            WordForm(f'{ppdmi[:-4]}уюся', '.ППДжВ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-4]}еюся', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжП'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДсР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДсД'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДсТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДсП'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнР'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмнД'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-4]}имися', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнП'),
        ]
    return word_forms


# ############################################################
#   Причастие прошедшего времени страдательное
def get_passive_past_participle(src_dict) -> list:
    passive_past_participle = {
        'ППС1': passive_past_participle_pps1,
        'ППС2': passive_past_participle_pps2,
        'ППС3': passive_past_participle_pps3,
        'ППС5ж': passive_past_participle_pps5g,
    }
    return passive_past_participle[src_dict['Inf_10']](src_dict)


# ППС1
def passive_past_participle_pps1(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-2]}нный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС2
def passive_past_participle_pps2(src_dict) -> list:
    gnb1e = list(filter(
        lambda x: x.idf == '.ГНБ1е',
        get_present_future_forms(src_dict)
    ))[0].name
    ppsmi = f'{gnb1e[:-1]}енный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС3
def passive_past_participle_pps3(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-2]}тый'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-2]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-2]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-2]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-2]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС5ж
def passive_past_participle_pps5g(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-4]}женный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ############################################################
# Деепричастие настоящего времени
def get_present_participle(src_dict) -> list:
    present_participle = {
        'ДН1': present_participle_dn1,
        'ДН2': present_participle_dn2,
    }
    return present_participle[src_dict['Inf_11']](src_dict)


# ДН1
def present_participle_dn1(src_dict) -> list:
    name = src_dict['name']
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb2e[:-3]}я', '.ДН'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb2e[:-5]}ясь', '.ДН'),
        ]
    return word_forms


# ДН2
def present_participle_dn2(src_dict) -> list:
    name = src_dict['name']
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb2e[:-3]}а', '.ДН'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb2e[:-5]}ась', '.ДН'),
        ]
    return word_forms


# ############################################################
# Деепричастие прошедшего времени
def get_past_participle(src_dict) -> list:
    past_participle = {
        'ДП1': past_participle_dp1,
        'ДП2': past_participle_dp2,
        'ДП3': past_participle_dp3,
        'ДП4': past_participle_dp4,
        'ДП6': past_participle_dp6,
        'ДП8': past_participle_dp8,
        'ДП9&10': past_participle_dp9_and_10,
    }
    return past_participle[src_dict['Inf_12']](src_dict)


# ДП1
def past_participle_dp1(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm[:-1]}в', '.ДП'),
            WordForm(f'{gpm[:-1]}вши', '.ДП*'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-3]}вшись', '.ДП'),
        ]
    return word_forms


# ДП2
def past_participle_dp2(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm[:-1]}в', '.ДП'),
            WordForm(f'{gpm[:-1]}вши', '.ДП*'),
            WordForm(f'{gnb2e[:-3]}я', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-3]}вшись', '.ДП'),
            WordForm(f'{gnb2e[:-5]}ясь', '.ДП!'),
        ]
    return word_forms


# ДП3
def past_participle_dp3(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm[:-1]}в', '.ДП'),
            WordForm(f'{gpm[:-1]}вши', '.ДП*'),
            WordForm(f'{gnb2e[:-3]}а', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-3]}вшись', '.ДП'),
            WordForm(f'{gnb2e[:-5]}ась', '.ДП!'),
        ]
    return word_forms


# ДП4
def past_participle_dp4(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm}ши', '.ДП'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-2]}шись', '.ДП'),
        ]
    return word_forms


# ДП6
def past_participle_dp6(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm}ши', '.ДП'),
            WordForm(f'{gnb2e[:-3]}я', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-2]}шись', '.ДП'),
            WordForm(f'{gnb2e[:-5]}ясь', '.ДП!'),
        ]
    return word_forms


# ДП8
def past_participle_dp8(src_dict) -> list:
    name = src_dict['name']
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb2e[:-3]}я', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb2e[:-5]}ясь', '.ДП!'),
        ]
    return word_forms


# ДП9&10
def past_participle_dp9_and_10(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}в', '.ДП1'),
            WordForm(f'{name[:-2]}вши', '.ДП1*'),
            WordForm(f'{name[:-4]}ши', '.ДП2'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}вшись', '.ДП1'),
            WordForm(f'{name[:-6]}шись', '.ДП2'),
        ]
    return word_forms
