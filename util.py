def replacer(value):
    s = str(value)
    if s.find('\n') != -1:
        s = '!' + s
        s = s.replace('\n', '@')
    return s


def getcell_(group, date=0, endis=0):
    cels = '4'
    cele = '15'
    cols = ''
    cole = ''
    if group == 1:
        cols = 'F'
        cole = 'I'
    elif group == 2:
        cols = 'K'
        cole = 'N'
    elif group == 3:
        cols = 'P'
        cole = 'S'
    elif group == 4:
        cols = 'Z'
        cole = 'AC'
    elif group == 5:
        cols = 'AE'
        cole = 'AH'
    elif group == 6:
        cols = 'AJ'
        cole = 'AM'
    cels = str(int(cels) + date * 12)
    cele = str(int(cele) + date * 12)
    start = cols + cels
    end = cole + cele
    if endis:
        return end
    else:
        return start


def zapoln(f, sheet, group=1):
    op = True
    k = 1
    # мб допилить разделение на группы
    start = getcell_(group, 0, 0)
    end = getcell_(group, 0, 1)
    cell_range = sheet[start:end]
    f.write('Понедельник:\n')
    for row in cell_range:
        f.write(str(k) + '+' + ('I' if op else 'II') + '+')
        if op == False:
            k += 1
            op = True
        else:
            op = False
        for cell in row:
            if cell.value == None:
                f.write('Ничего' + '+')
            else:
                cell.value = replacer(cell.value)
                f.write(cell.value + '+')
        f.write('\n')
    op = True
    k = 1
    start = getcell_(group, 1, 0)
    end = getcell_(group, 1, 1)
    cell_range = sheet[start:end]
    f.write('Вторник:\n')
    for row in cell_range:
        f.write(str(k) + '+' + ('I' if op else 'II') + '+')
        if not op:
            k += 1
            op = True
        else:
            op = False
        for cell in row:
            if cell.value == None:
                f.write('Ничего' + '+')
            else:
                cell.value = replacer(cell.value)
                f.write(cell.value + '+')
        f.write('\n')
    op = True
    k = 1
    start = getcell_(group, 2, 0)
    end = getcell_(group, 2, 1)
    cell_range = sheet[start:end]
    f.write('Среда:\n')
    for row in cell_range:
        f.write(str(k) + '+' + ('I' if op else 'II') + '+')
        if op == False:
            k += 1
            op = True
        else:
            op = False
        for cell in row:
            if cell.value == None:
                f.write('Ничего' + '+')
            else:
                cell.value = replacer(cell.value)
                f.write(cell.value + '+')
        f.write('\n')
    op = True
    k = 1
    start = getcell_(group, 3, 0)
    end = getcell_(group, 3, 1)
    cell_range = sheet[start:end]
    f.write('Четверг:\n')
    for row in cell_range:
        f.write(str(k) + '+' + ('I' if op else 'II') + '+')
        if op == False:
            k += 1
            op = True
        else:
            op = False
        for cell in row:
            if cell.value == None:
                f.write('Ничего' + '+')
            else:
                cell.value = replacer(cell.value)
                f.write(cell.value + '+')
        f.write('\n')
    op = True
    k = 1
    start = getcell_(group, 4, 0)
    end = getcell_(group, 4, 1)
    cell_range = sheet[start:end]
    f.write('Пятница:\n')
    for row in cell_range:
        f.write(str(k) + '+' + ('I' if op else 'II') + '+')
        if op == False:
            k += 1
            op = True
        else:
            op = False
        for cell in row:
            if cell.value == None:
                f.write('Ничего' + '+')
            else:
                cell.value = replacer(cell.value)
                f.write(cell.value + '+')
        f.write('\n')
    op = True
    k = 1
    start = getcell_(group, 5, 0)
    end = getcell_(group, 5, 1)
    cell_range = sheet[start:end]
    f.write('Суббота:\n')
    for row in cell_range:
        f.write(str(k) + '+' + ('I' if op else 'II') + '+')
        if op == False:
            k += 1
            op = True
        else:
            op = False
        for cell in row:
            if cell.value == None:
                f.write('Ничего' + '+')
            else:
                cell.value = replacer(cell.value)
                f.write(cell.value + '+')
        f.write('\n')
