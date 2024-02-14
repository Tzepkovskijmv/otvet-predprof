def main(in_file_name: str, out_file_name: str, serach_preport:str):
    '''
    Основная функция.
    Ищут ученых по имени и фамилии, создает новую таблицу с именами ученых, без ученых плагиатов.
    :param in_file_name: названия файла для обработки.
    :param out_file_name: название файла для сохранения.
    :param serach_preporat: создатели препората.
    '''
    f = open(in_file_name)
    f.readline()
    all_klass = {}
    for line in f.readlines():
        data = line.split('#')
        time = ''
        if data[2] != 'Nope\n':
            time = data[2]
        user_klass = data[1]
        if user_klass in all_klass:
            klass = all_klass[user_klass]
            all_klass[user_klass] = (klass[0] + time, klass[1]+1)
        else:
            all_klass[klass] = (time, 1)
        if serach_preport in data[1]:
            print(f'Создателями {serach_preport} были {data[0]}')
        f.close()
        data_mew_file = 'klass.avg\n'
        for klass ,data_klass in all_klass.items():
            sm_klass, count_klass = data_klass
            avg_klass = sm_klass / count_klass
            data_mew_file +=f'{klass},{avg_klass:.4}\n'


            new_f= open((out_file_name), 'w')
            new_f.write(data_mew_file)
            new_f.close()


if __name__ == '__main__':
    main('scientist.txt', 'scientist_origin.txt','Аллопуринол')


