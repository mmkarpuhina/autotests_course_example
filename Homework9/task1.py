# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код

from pathlib import Path
with open(Path.cwd().joinpath('test_file', 'task1_data.txt'), mode='r', encoding='utf-8') as f:
    file = f.read()

text = ''.join([x for x in file if not x.isdigit()])

    
with open(Path.cwd().joinpath('test_file', 'task1_answer.txt'), mode='w', encoding='utf-8') as f:
    f.write(text)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
