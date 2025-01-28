from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

        # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Игра престолов': 'Фантастика',
                                 'Еретик' : 'Ужасы',
                                 'Каштановые человечки' : 'Детектив',
                                 'Моана' : 'Мультфильм',
                                 'Американский пирог' : 'Комедии'
                                 }
        collector.set_book_genre('Моана' , 'Мультфильм')
        assert collector.books_genre ['Моана'] == 'Мультфильм'

    def test_get_book_genre_good(self, name):
        collector = BooksCollector()
        collector.books_genre = {'Игра престолов': 'Фантастика',
                                 'Еретик' : 'Ужасы',
                                 'Каштановые человечки' : 'Детектив',
                                 'Моана' : 'Мультфильм',
                                 'Американский пирог' : 'Комедии'
                                 }
        assert collector.get_book_genre(name) == collector.books_genre[name]

    def test_get_books_with_specific_genre_valid_genre_good(self):
        collector = BooksCollector()
        collector.books_genre = {'Игра престолов': 'Фантастика',
                                 'Еретик' : 'Ужасы',
                                 'Каштановые человечки' : 'Детектив',
                                 'Моана' : 'Мультфильм',
                                 'Американский пирог' : 'Комедии'
                                 }
        assert collector.get_books_with_specific_genre('Ужасы') == ['Еретик']

    def get_books_for_children_no_added(self):
        collector = BooksCollector()
        collector.books_genre = {'Игра престолов': 'Фантастика',
                                 'Еретик': 'Ужасы',
                                 'Каштановые человечки': 'Детектив',
                                 'Моана': 'Мультфильм',
                                 'Американский пирог': 'Комедии'
                                 }
        assert collector.get_books_for_children() == ['Моана']

    def add_book_in_favorites_my_again(self, name):
        collector = BooksCollector()
        collector.books_genre = {'Каштановые человечки': 'Детектив'}
        collector.favorites = ['Каштановые человечки']
        collector.add_book_in_favorites('Каштановые человечки')
        assert collector.favorites == ['Каштановые человечки'] and len(collector.favorites) == 1

    def test_delete_book_from_favorites_valid_name_true(self):
        collector = BooksCollector()
        collector.favorites = ['Моана', 'Игра престолов', 'Каштановые человечки']
        collector.delete_book_from_favorites('Моана')
        assert collector.favorites == ['Игра престолов', 'Каштановые человечки']

    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.favorites = ['Моана', 'Игра престолов', 'Каштановые человечки']
        assert collector.get_list_of_favorites_books() == collector.favorites
