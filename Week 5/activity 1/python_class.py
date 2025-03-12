# Activity 1: Design your own class
class Book:
    def __init__(self, title, author, pages, year_published):
        self.title = title
        self.author = author
        self.pages = pages
        self.year_published = year_published
        self.rating = None # Encapsulated attribute
        self.is_available = True

    def get_info(self):
        return f"{self.title} by {self.author}, {self.pages} pages, published in ({self.year_published})"

    def check_out(self):
        if self.is_available:
            self.is_available = False
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is not available for checkout"

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is already available for checkout"

    # Getter and setter for encapsulated rating attribute
    def get_rating(self):
        return self.rating if self.rating else "No rating available"

    def set_rating(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            return "Invalid rating. Rating must be between 1 and 5"


# Inheritance: FictionBook subclass
class FictionBook(Book):
    def __init__(self, title, author, pages, year_published, genre):
        # Call the parent class constructor
        super().__init__(title, author, pages, year_published)
        self.genre = genre

    def get_info(self):
        # Override parent method to include genre
        basic_info = super().get_info()
        return f"{basic_info}, Genre: {self.genre}"


# Inheritance: Non-Fiction Book subclass
class NonFictionBook(Book):
    def __init__(self, title, author, pages, year_published, subject):
        super().__init__(title, author, pages, year_published)
        self.subject = subject

    def get_info(self):
        basic_info = super().get_info()
        return f"{basic_info}, Subject: {self.subject}"

# Demonstration
def main():
    print("BOOK CLASS DEMONSTRATION")
    print("-----------------------")

    # Create book instances
    novel = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", 180, 1925, "Classic")
    textbook = NonFictionBook("Python Programming", "John Smith", 450, 2020, "Computer Science")

    # Test book methods
    print(novel.get_info())
    print(novel.check_out())
    novel.set_rating(4)
    print(f"Rating: {novel.get_rating()}")

    print("\n" + textbook.get_info())
    print(textbook.check_out())
    print(textbook.return_book())

# Run the main function
if __name__ == "__main__":
    main()