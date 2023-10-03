import random

class BookBuilder:
    def __init__(self):
        self.book = Book()

    def set_title(self, title):
        self.book.title = title
        return self

    def set_author(self, author):
        self.book.author = author
        return self

    def set_type(self, book_type):
        self.book.book_type = book_type
        return self

    def add_page(self, page):
        self.book.pages.append(page)
        return self

    def build(self):
        return self.book


class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.book_type = ""
        self.pages = []

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nType: {self.book_type}\nPages: {len(self.pages)}"


class ScientificBook(Book):
    def __init__(self):
        super().__init__()
        self.references = []
        self.glossary = []

    def __str__(self):
        return super().__str__() + f"\nReferences: {len(self.references)}\nGlossary: {len(self.glossary)}"


class Novel(Book):
    def __init__(self):
        super().__init__()
        self.characters = []

    def __str__(self):
        return super().__str__() + f"\nCharacters: {len(self.characters)}"


class Manual(Book):
    def __init__(self):
        super().__init__()
        self.image = ""

    def __str__(self):
        return super().__str__() + f"\nImage: {self.image}"


class PageRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.pages = []
        return cls._instance

    def add_page(self, page):
        self.pages.append(page)

    def get_pages(self):
        return self.pages


class Page:
    def __init__(self, content):
        self.content = content


class BookGenerator:
    def generate_book(self):
        book_builder = BookBuilder()

        # Виберіть випадковий тип книги
        book_type = random.choice(["Scientific", "Novel", "Manual"])

        # Встановіть заголовок, автора та тип книги
        book_builder.set_title("Random Book") \
                   .set_author("Anonymous") \
                   .set_type(book_type)

        # Згенеруйте випадкову кількість сторінок
        num_pages = random.randint(50, 200)

        # Згенеруйте випадковий вміст сторінок
        page_registry = PageRegistry()
        for _ in range(num_pages):
            page_content = self.generate_page_content()
            page = Page(page_content)
            page_registry.add_page(page)
            book_builder.add_page(page)

        return book_builder.build()

    def generate_page_content(self):
        # Згенеруйте випадковий реєстр слів та об'єднайте їх у речення та абзаци
        word_registry = ["word1", "word2", "word3", "word4", "word5"]
        num_sentences = random.randint(3, 10)
        num_paragraphs = random.randint(1, 5)

        content = ""
        for _ in range(num_paragraphs):
            paragraph = ""
            for _ in range(num_sentences):
                sentence = " ".join(random.choices(word_registry, k=random.randint(5, 10)))
                paragraph += sentence + ". "
            content += paragraph + "\n\n"

        return content


book_generator = BookGenerator()
book = book_generator.generate_book()
print(book)

choice = input("Would you like to view the content of the pages? (yes/no): ")
if choice.lower() == "yes":
    page_registry = PageRegistry()
    pages = page_registry.get_pages()

    for i, page in enumerate(pages):
        print(f"Page {i+1}:")
        print(page.content)
        print()