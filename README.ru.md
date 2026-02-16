# stafit-cli

CLI для обработки CSV-файлов с макроэкономическими данными и формирования отчётов.

## Использование

```bash
python main.py --files data/economic1.csv data/economic2.csv --report average-gdp
```

Можно передать несколько CSV-файлов. Отчёт формируется по всем файлам.

## Добавление новых отчётов

Чтобы добавить новый тип отчёта:

1. Создайте функцию в `handlers/` по примеру (`handlers/average_gdp.py`)
2. Зарегистрируйте её в `handlers/__init__.py` в словаре `REPORTS`

Функция должна возвращать заголовки и строки. Строки автоматически нумеруются и отображаются таблицей.

## Запуск

Установите зависимости через выбранный менеджер пакетов

Astral UV:
```bash
uv sync
```

Poetry:
```bash
poetry install
```

## Запуск

Из корня проекта:

```bash
python main.py --files data/economic1.csv data/economic2.csv --report average-gdp
```

Или через uv:

```bash
uv run main.py --files data/economic1.csv data/economic2.csv --report average-gdp
```

## Тестирование

Запускать тесты можно командой

```bash
pytest .
```
