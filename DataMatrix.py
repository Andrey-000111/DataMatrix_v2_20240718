import os

# Создаем папку "inPath"
in_path = 'inPath'
if not os.path.exists(in_path):
    os.makedirs(in_path)

# Сканируем папку "inPath" и обрабатываем текстовые файлы
for file in os.listdir(in_path):
    if file.endswith('.txt'):
        with open(os.path.join(in_path, file), 'r') as f:
            lines = f.readlines()

        # Обработка текстового файла
        new_lines = []
        for line in lines:
            if line[0] == '':
                line = line[1:]
            new_lines.append(line)

        # Сохраняем обработанный файл в новой папке "outPath"
        out_path = 'outPath'
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        file_name = os.path.splitext(file)[0] + '.txt'
        with open(os.path.join(out_path, file_name), 'w') as out_file:
            out_file.writelines(new_lines)


# Создание отчета
report_text = 'Количество обработанных строк: {0}\nКоличество удаленных символов: {1}'
with open('report.txt', 'w') as report:
    report.write(report_text.format(len(lines), sum([len(line) - len(new_line) for line, new_line in zip(lines, new_lines)])))

# Сохраняем отчет в папке "outPath"
file_name = 'report.txt'
with open(os.path.join(out_path, file_name), 'w'):
    pass