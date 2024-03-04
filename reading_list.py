class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.review = ""
        self.rating = 0

class ReadingList:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def write_review(self, title, review):
        for book in self.books:
            if book.title == title:
                book.review = review
                break

    def rate_book(self, title, rating):
        for book in self.books:
            if book.title == title:
                book.rating = rating
                break

    def display_books(self):
        if not self.books:
            print("Your reading list is empty.")
        else:
            print("Your reading list:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Rating: {book.rating}, Review: {book.review}")

def main():
    reading_list = ReadingList()

    while True:
        print("\n✿✿✿✿ Welcome to Itzel's Reading List Menu ✿✿✿✿")
        print("1 ~~ Add a Book")
        print("2 ~~ Write a Review")
        print("3 ~~ Rate a Book")
        print("4 ~~ Display your Reading list")
        print("5 ~~ Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            new_book = Book(title, author)
            reading_list.add_book(new_book)
            print(f"{title} by {author} added to your reading list.")

        elif choice == "2":
            if not reading_list.books:
                print("Your reading list is empty. Please add a book first.")
                continue
            title = input("Enter the title of the book: ")
            review = input("Write your review: ")
            reading_list.write_review(title, review)
            print("Review added successfully.")

        elif choice == "3":
            if not reading_list.books:
                print("Your reading list is empty. Please add a book first.")
                continue
            title = input("Enter the title of the book: ")
            rating = int(input("Enter your rating (1-5): "))
            reading_list.rate_book(title, rating)
            print("Rating added successfully.")

        elif choice == "4":
            reading_list.display_books()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()