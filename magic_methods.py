# class Dog:
#     def __init__(self, name, age, breed, color):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.color = color

#     def __str__(self):
#         return (
#             f"{self.name} is a {self.age}-year-old "
#             f"{self.color} {self.breed}."
#         )


# # Creating an instance of the Dog class
# myDog = Dog("Lucky", 5, "German Shepherd", "white")
# print(myDog)


class Book:
    def __init__(self, title, author, pages):
        """
        Initializing a new Book object.
        This is the constructor.
        """
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """
        Returns a human-readable string representation of the Book object.
        """
        return f"Book: '{self.title}' by {self.author}, {self.pages} pages"

    def get_info(self):
        """
        A regular method to demonstrate accessing attributes.
        """
        return f"Title: {self.title}, Author: {self.author}"


# --- Demonstrating __init__() ---

print("\n---- Creating Book instances ----")
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 193)
# When the line above is executed, __init__() is called to set up book1.

book2 = Book("Pride and Prejudice", "Jane Austen", 279)
# Similarly, __init__() is called for book2.

print("\n--- Accessing attributes via a regular method ---")
print(book1.get_info())
print(book2.get_info())


# --- Demonstrating __str__() ---

print("\n--- Using print() on Book instances (calls -> __str__()) ---")
print(book1)
# print() automatically calls __str__() to get a string to display.

print(book2)
# print() automatically calls __str__() to get a string to display.

# print("\n--- Using str() function on Book instances (calls __str__()) ---")
# book1_str = str(book1)
# print(f"String representation of book1: {book1_str}")

# print("\n--- Using an f-string with Book instances (calls __str__()) ---")
# print(f"Here's my favorite book: {book1}")
