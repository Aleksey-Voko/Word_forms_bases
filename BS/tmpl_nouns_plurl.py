# Существительные множественное число
from BS.word_form import WordForm


def get_plurl_word_forms(src_dict, singl_word_forms) -> list:
    plurls = {
        'I1': get_plurl_i1,
        'I1*': get_plurl_i1_prim,
        'I1&IV11': get_plurl_i1_and_iv11,
        'I10': get_plurl_i10,
        'I11': get_plurl_i11,
        'I13е**': get_plurl_i13e2_prim,
        'I13о': get_plurl_i13o,
        'I16': get_plurl_i16,
        'I16*': get_plurl_i16_prim,
        'I16#е': get_plurl_i16sharp_e,
        'I16#е*': get_plurl_i16sharp_e_prim,
        'I16е': get_plurl_i16e,
        'I16е*': get_plurl_i16e_prim,
        'I16е*-': get_plurl_i16e_prim__,
        'I16о': get_plurl_i16o,
        'I16о*': get_plurl_i16o_prim,
        'I17#е': get_plurl_i17sharp_e,
        'I19': get_plurl_i19,
        'I2': get_plurl_i2,
        'I2*': get_plurl_i2_prim,
        'I3': get_plurl_i3,
        'I3*': get_plurl_i3_prim,
        'I4': get_plurl_i4,
        'I4*': get_plurl_i4_prim,
        'I4+III7': get_plurl_i4_and_iii7,
        'I6': get_plurl_i6,
        'II1': get_plurl_ii1,
        'II1*': get_plurl_ii1_prim,
        'II1*+6*': get_plurl_ii1_prim_and_6_prim,
        'II1+IV1': get_plurl_ii1_and_iv1,
        'II3': get_plurl_ii3,
        'II6': get_plurl_ii6,
        'II6*': get_plurl_ii6_prim,
        'III12': get_plurl_iii12,
        'III2*': get_plurl_iii2_prim,
        'III7': get_plurl_iii7,
        'III7*': get_plurl_iii7_prim,
        'IV1': get_plurl_iv1,
        'IV1+I1': get_plurl_iv1_and_i1,
        'IV12': get_plurl_iv12,
        'IV13': get_plurl_iv13,
        'IV6': get_plurl_iv6,
        'IV6*': get_plurl_iv6_prim,
        'IV6*+I13*': get_plurl_iv6_prim_and_i13,
        'IV6*+II5*': get_plurl_iv6_prim_and_ii5_prim,
        'IV6+I13': get_plurl_iv6_and_i13,
        'V2': get_plurl_v2,
    }
    return plurls[src_dict['Inf_6']](src_dict['name'], src_dict['Inf_0'], singl_word_forms)


# I1
def get_plurl_i1(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser[:-1]}и'
    else:
        smnv = f'{ser[:-1]}ов'
    word_forms = [
        WordForm(f'{ser[:-1]}и', '.СмнИ'),
        WordForm(f'{ser[:-1]}ов', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I1*
def get_plurl_i1_prim(name: str, inf_0: str, _) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-1]}ов'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}ов', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I1&IV11
def get_plurl_i1_and_iv11(name: str, _, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    word_forms = [
        WordForm(f'{ser[:-1]}и', '.СмнИ1'),
        WordForm(f'{name[:-2]}ята', '.СмнИ2'),
        WordForm(f'{ser[:-1]}ов', '.СмнР1'),
        WordForm(f'{name[:-2]}ят', '.СмнР2'),
        WordForm(f'{ser[:-1]}ам', '.СмнД1'),
        WordForm(f'{name[:-2]}ятам', '.СмнД2'),
        WordForm(f'{ser[:-1]}ов', '.СмнВ1'),
        WordForm(f'{name[:-2]}ят', '.СмнВ2'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ1'),
        WordForm(f'{name[:-2]}ятами', '.СмнТ2'),
        WordForm(f'{ser[:-1]}ах', '.СмнП1'),
        WordForm(f'{name[:-2]}ятах', '.СмнП2'),
    ]
    return word_forms


# I10
def get_plurl_i10(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-2]}ий'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-2]}ий', '.СмнР'),
        WordForm(f'{ser[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ями', '.СмнТ'),
        WordForm(f'{ser[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I11
def get_plurl_i11(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-1]}й'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-1]}й', '.СмнР'),
        WordForm(f'{ser[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ями', '.СмнТ'),
        WordForm(f'{ser[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I13е**
def get_plurl_i13e2_prim(_, __, singl_word_forms: list) -> list:
    ser2 = list(filter(lambda x: x.idf == '.СеР2', singl_word_forms))[0].name
    word_forms = [
        WordForm(f'{ser2[:-1]}и', '.СмнИ'),
        WordForm(f'{ser2[:-2]}е{ser2[-2]}', '.СмнР'),
        WordForm(f'{ser2[:-1]}ам', '.СмнД'),
        WordForm(f'{ser2[:-1]}и', '.СмнВ'),
        WordForm(f'{ser2[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser2[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I13о
def get_plurl_i13o(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser[:-1]}и'
    else:
        smnv = f'{ser[:-2]}о{ser[-2]}'
    word_forms = [
        WordForm(f'{ser[:-1]}и', '.СмнИ'),
        WordForm(f'{ser[:-2]}о{ser[-2]}', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16
def get_plurl_i16(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-1]}'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-1]}', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16*
def get_plurl_i16_prim(name: str, inf_0: str, _) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-1]}'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16#е
def get_plurl_i16sharp_e(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-3]}е{ser[-2:-1]}'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-3]}е{ser[-2:-1]}', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16#е*
def get_plurl_i16sharp_e_prim(name: str, inf_0: str, _) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-3]}е{name[-2:-1]}'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-3]}е{name[-2:-1]}', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16е
def get_plurl_i16e(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-2]}е{ser[-2]}'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-2]}е{ser[-2]}', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16е*
def get_plurl_i16e_prim(name: str, inf_0: str, _) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-2]}е{name[-2]}'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-2]}е{name[-2]}', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16е*-
def get_plurl_i16e_prim__(name: str, _, __) -> list:
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-2]}е{name[-2]}', '.СмнР'),
        WordForm(f'{name}', '.СмнВ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16о
def get_plurl_i16o(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-2]}о{ser[-2]}'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-2]}о{ser[-2]}', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16о*
def get_plurl_i16o_prim(name: str, inf_0: str, _) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-2]}о{name[-2]}'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-2]}о{name[-2]}', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I17#е
def get_plurl_i17sharp_e(_, __, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-3]}е{ser[-2:-1]}', '.СмнР'),
        WordForm(f'{ser[:-1]}ям', '.СмнД'),
        WordForm(f'{ser}', '.СмнВ'),
        WordForm(f'{ser[:-1]}ями', '.СмнТ'),
        WordForm(f'{ser[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I19
def get_plurl_i19(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-1]}ь'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-1]}ь', '.СмнР'),
        WordForm(f'{ser[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ями', '.СмнТ'),
        WordForm(f'{ser[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I2
def get_plurl_i2(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser[:-1]}и'
    else:
        smnv = f'{ser[:-1]}ев'
    word_forms = [
        WordForm(f'{ser[:-1]}и', '.СмнИ'),
        WordForm(f'{ser[:-1]}ев', '.СмнР'),
        WordForm(f'{ser[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ями', '.СмнТ'),
        WordForm(f'{ser[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I2*
def get_plurl_i2_prim(name: str, inf_0: str, __) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-1]}ев'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}ев', '.СмнР'),
        WordForm(f'{name[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ями', '.СмнТ'),
        WordForm(f'{name[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I3
def get_plurl_i3(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser[:-1]}и'
    else:
        smnv = f'{ser[:-1]}ей'
    word_forms = [
        WordForm(f'{ser[:-1]}и', '.СмнИ'),
        WordForm(f'{ser[:-1]}ей', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I3*
def get_plurl_i3_prim(name: str, inf_0: str, _) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-1]}ей'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}ей', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I4
def get_plurl_i4(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser[:-1]}и'
    else:
        smnv = f'{ser[:-1]}ей'
    word_forms = [
        WordForm(f'{ser[:-1]}и', '.СмнИ'),
        WordForm(f'{ser[:-1]}ей', '.СмнР'),
        WordForm(f'{ser[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ями', '.СмнТ'),
        WordForm(f'{ser[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I4*
def get_plurl_i4_prim(name: str, inf_0: str, _) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-1]}ей'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}ей', '.СмнР'),
        WordForm(f'{name[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ями', '.СмнТ'),
        WordForm(f'{name[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I4+III7
def get_plurl_i4_and_iii7(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv1 = WordForm(f'{ser[:-1]}и', '.СмнВ1')
        smnv2 = WordForm(f'{ser}', '.СмнВ2')
        smnv = ''
    else:
        smnv1 = ''
        smnv2 = ''
        smnv = WordForm(f'{ser[:-1]}и', '.СмнВ'),
    word_forms = [
        WordForm(f'{ser[:-1]}и', '.СмнИ1'),
        WordForm(f'{ser}', '.СмнИ2'),
        WordForm(f'{ser[:-1]}ей', '.СмнР'),
        WordForm(f'{ser[:-1]}ям', '.СмнД'),
        smnv1,
        smnv2,
        smnv,
        WordForm(f'{ser[:-1]}ями', '.СмнТ'),
        WordForm(f'{ser[:-1]}ях', '.СмнП'),
    ]
    return list(filter(None, word_forms))


# I6
def get_plurl_i6(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-1]}ей'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-1]}ей', '.СмнР'),
        WordForm(f'{ser[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ями', '.СмнТ'),
        WordForm(f'{ser[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# II1
def get_plurl_ii1(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser[:-1]}ы'
    else:
        smnv = f'{ser[:-1]}ов'
    word_forms = [
        WordForm(f'{ser[:-1]}ы', '.СмнИ'),
        WordForm(f'{ser[:-1]}ов', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II1*
def get_plurl_ii1_prim(name: str, inf_0: str, _) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-1]}ов'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}ов', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II1*+6*
def get_plurl_ii1_prim_and_6_prim(name: str, _, __) -> list:
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}ов', '.СмнР1'),
        WordForm(f'{name[:-1]}', '.СмнР2'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(f'{name}', '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II1+IV1
def get_plurl_ii1_and_iv1(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv1 = WordForm(f'{ser[:-1]}ы', '.СмнВ1')
        smnv2 = WordForm(f'{ser}', '.СмнВ2')
        smnv = ''
    else:
        smnv1 = ''
        smnv2 = ''
        smnv = WordForm(f'{ser[:-1]}ов', '.СмнВ3'),
    word_forms = [
        WordForm(f'{ser[:-1]}ы', '.СмнИ1'),
        WordForm(f'{ser}', '.СмнИ2'),
        WordForm(f'{ser[:-1]}ов', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        smnv1,
        smnv2,
        smnv,
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return list(filter(None, word_forms))


# II3
def get_plurl_ii3(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser[:-1]}ы'
    else:
        smnv = f'{ser[:-1]}ев'
    word_forms = [
        WordForm(f'{ser[:-1]}ы', '.СмнИ'),
        WordForm(f'{ser[:-1]}ев', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6
def get_plurl_ii6(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-1]}'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-1]}', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6*
def get_plurl_ii6_prim(name: str, inf_0: str, __) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-1]}'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# III12
def get_plurl_iii12(_, __, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-2]}ий', '.СмнР'),
        WordForm(f'{ser[:-1]}ям', '.СмнД'),
        WordForm(f'{ser}', '.СмнВ'),
        WordForm(f'{ser[:-1]}ями', '.СмнТ'),
        WordForm(f'{ser[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III2*
def get_plurl_iii2_prim(name: str, inf_0: str, _) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-1]}ев'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}ев', '.СмнР'),
        WordForm(f'{name[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ями', '.СмнТ'),
        WordForm(f'{name[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III7
def get_plurl_iii7(name, __, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{name[:-1]}ей', '.СмнР'),
        WordForm(f'{name[:-1]}ям', '.СмнД'),
        WordForm(f'{name[:-1]}ей', '.СмнВ1'),
        WordForm(f'{name[:-1]}ями', '.СмнТ'),
        WordForm(f'{name[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III7*
def get_plurl_iii7_prim(name: str, _, __) -> list:
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}ей', '.СмнР'),
        WordForm(f'{name[:-1]}ям', '.СмнД'),
        WordForm(f'{name}', '.СмнВ'),
        WordForm(f'{name[:-1]}ями', '.СмнТ'),
        WordForm(f'{name[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# IV1
def get_plurl_iv1(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-1]}ов'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-1]}ов', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV1+I1
def get_plurl_iv1_and_i1(_, __, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    word_forms = [
        WordForm(f'{ser}', '.СмнИ1'),
        WordForm(f'{ser[:-1]}и', '.СмнИ2'),
        WordForm(f'{ser[:-1]}ов', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(f'{ser}', '.СмнВ1'),
        WordForm(f'{ser[:-1]}и', '.СмнВ2'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV12
def get_plurl_iv12(name: str, inf_0: str, _) -> list:
    if inf_0 == 'неод':
        smnv = f'{name[:-4]}ята'
    else:
        smnv = f'{name[:-4]}ят'
    word_forms = [
        WordForm(f'{name[:-4]}ята', '.СмнИ'),
        WordForm(f'{name[:-4]}ят', '.СмнР'),
        WordForm(f'{name[:-4]}ятам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-4]}ятами', '.СмнТ'),
        WordForm(f'{name[:-4]}ятах', '.СмнП'),
    ]
    return word_forms


# IV13
def get_plurl_iv13(name: str, _, __) -> list:
    word_forms = [
        WordForm(f'{name[:-4]}ата', '.СмнИ'),
        WordForm(f'{name[:-4]}ат', '.СмнР'),
        WordForm(f'{name[:-4]}атам', '.СмнД'),
        WordForm(f'{name[:-4]}ат', '.СмнВ'),
        WordForm(f'{name[:-4]}атами', '.СмнТ'),
        WordForm(f'{name[:-4]}атах', '.СмнП'),
    ]
    return word_forms


# IV6
def get_plurl_iv6(_, inf_0: str, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv = f'{ser}'
    else:
        smnv = f'{ser[:-1]}'
    word_forms = [
        WordForm(f'{ser}', '.СмнИ'),
        WordForm(f'{ser[:-1]}', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6*
def get_plurl_iv6_prim(name: str, inf_0: str, __) -> list:
    if inf_0 == 'неод':
        smnv = f'{name}'
    else:
        smnv = f'{name[:-1]}'
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6*+I13*
def get_plurl_iv6_prim_and_i13(name: str, _, __) -> list:
    word_forms = [
        WordForm(f'{name}', '.СмнИ1'),
        WordForm(f'{name[:-1]}и', '.СмнИ2'),
        WordForm(f'{name[:-1]}', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(f'{name}', '.СмнВ1'),
        WordForm(f'{name[:-1]}и', '.СмнВ2'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6*+II5*
def get_plurl_iv6_prim_and_ii5_prim(name: str, _, __) -> list:
    word_forms = [
        WordForm(f'{name}', '.СмнИ1'),
        WordForm(f'{name[:-1]}ы', '.СмнИ2'),
        WordForm(f'{name[:-1]}', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(f'{name}', '.СмнВ1'),
        WordForm(f'{name[:-1]}ы', '.СмнВ2'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6+I13
def get_plurl_iv6_and_i13(_, __, singl_word_forms: list) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    word_forms = [
        WordForm(f'{ser}', '.СмнИ1'),
        WordForm(f'{ser[:-1]}и', '.СмнИ2'),
        WordForm(f'{ser[:-1]}', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(f'{ser}', '.СмнВ1'),
        WordForm(f'{ser[:-1]}и', '.СмнВ2'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# V2
def get_plurl_v2(name: str, _, __) -> list:
    word_forms = [
        WordForm(f'{name[:-2]}е', '.СмнИ'),
        WordForm(f'{name[:-2]}', '.СмнР'),
        WordForm(f'{name[:-2]}ам', '.СмнД'),
        WordForm(f'{name[:-2]}', '.СмнВ'),
        WordForm(f'{name[:-2]}ами', '.СмнТ'),
        WordForm(f'{name[:-2]}ах', '.СмнП'),
    ]
    return word_forms
