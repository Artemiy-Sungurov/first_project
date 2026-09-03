import os

from dotenv import load_dotenv


def print_author():
    # Загружаем переменные из файла .env
    load_dotenv()

    # Получаем значение переменной AUTHOR
    author = os.getenv("AUTHOR")

    # Выводим автора
    print(f"Автор проекта: {author}")


print_author()