# Антиплагиат
Скрипт для проверки схожести python файлов
### Запуск
Для запуска требуется в качестве аргументов передать файл с парами программ для сравнения и файл, куда следует записать полученные оценки схожести
> Например, python3 compare.py input.txt output.txt

### Используемые библиотеки и алгоритмы:
- *[Abstract Syntax Trees(ast)](https://docs.python.org/3/library/ast.html)*-для парсинга кода
- *[argparse](https://docs.python.org/3/library/argparse.html)* - парсер для командной строки
- *[расстояние Левенштейна](https://en.wikipedia.org/wiki/Levenshtein_distance)* - выбранная метрика сравнения двух программ
