from BS.utils import get_string_list_from_file, save_list_to_file


def fix_adjusted_participles():
    socket_group_28_01 = list(get_string_list_from_file(
        'src_dict/БГ 28.01.21 изм.txt', encoding='cp1251'))
    socket_group_23_01 = list(get_string_list_from_file(
        'src_dict/БГ 23.01.21.txt', encoding='cp1251'))

    adjusted_participles_list = []

    for count, socket_string in enumerate(socket_group_28_01[:]):
        if socket_string.startswith('*'):
            for replace_string in socket_group_23_01[:]:
                if replace_string.startswith('*'):
                    if replace_string.split()[0].endswith(
                            socket_string.split()[1]
                    ):
                        print(replace_string)
                        socket_group_28_01[count] = replace_string
                        adjusted_participles_list.append(replace_string)

    save_list_to_file(sorted(adjusted_participles_list,
                             key=lambda x: x.replace('*', '').lower()),
                      'out/Адъектированные причастия.txt'
                      )
    save_list_to_file(socket_group_28_01, 'out/БГ 28.01.21.txt',
                      encoding='cp1251')


if __name__ == '__main__':
    fix_adjusted_participles()
