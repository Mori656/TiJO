
from src.librarySomeRepository import LibrarySomeRepository

class Library:
    def __init__(self, repository: LibrarySomeRepository):
        self.repository = repository

    def borrow_book(self, title: str) -> bool:
        return self.repository.remove_book(title)

    def return_book(self, title: str, author: str, year: int):
        self.repository.add_book(title, author, year)

    def list_books(self):
        return self.repository.get_all_books()