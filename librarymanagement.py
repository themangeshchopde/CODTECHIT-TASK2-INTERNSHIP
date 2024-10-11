from datetime import datetime, timedelta

class LibraryItem:
    def __init__(self, title, author, category, item_type):
        self.title = title
        self.author = author
        self.category = category
        self.item_type = item_type
        self.is_checked_out = False
        self.due_date = None

    def checkout(self, checkout_period_days=14):
        if not self.is_checked_out:
            self.is_checked_out = True
            self.due_date = datetime.now() + timedelta(days=checkout_period_days)
            print(f"{self.title} checked out. Due on {self.due_date.date()}.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            overdue_days = (datetime.now() - self.due_date).days
            fine = 0 if overdue_days <= 0 else overdue_days * 1  # 1 unit fine per overdue day
            self.due_date = None
            print(f"{self.title} returned. Fine: {fine} units.")
        else:
            print(f"{self.title} was not checked out.")

    def __str__(self):
        return f"{self.item_type}: {self.title} by {self.author} (Category: {self.category})"


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.item_type}: {item.title} by {item.author}.")

    def search_items(self, query, search_type='title'):
        results = []
        query = query.lower()
        for item in self.items:
            if search_type == 'title' and query in item.title.lower():
                results.append(item)
            elif search_type == 'author' and query in item.author.lower():
                results.append(item)
            elif search_type == 'category' and query in item.category.lower():
                results.append(item)
        
        if results:
            print(f"Found {len(results)} matching items:")
            for result in results:
                print(result)
        else:
            print("No matching items found.")

    def checkout_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                item.checkout()
                return
        print(f"No item found with title: {title}")

    def return_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                item.return_item()
                return
        print(f"No item found with title: {title}")

def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add new item")
        print("2. Search for an item")
        print("3. Check out an item")
        print("4. Return an item")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Adding new item
            title = input("Enter the title of the item: ")
            author = input("Enter the author of the item: ")
            category = input("Enter the category of the item: ")
            item_type = input("Enter the type of the item (Book/Magazine/DVD): ")
            library.add_item(LibraryItem(title, author, category, item_type))
        
        elif choice == '2':
            # Search for an item
            search_type = input("Search by (title/author/category): ").lower()
            query = input(f"Enter the {search_type} to search: ")
            library.search_items(query, search_type=search_type)

        elif choice == '3':
            # Check out an item
            title = input("Enter the title of the item to check out: ")
            library.checkout_item(title)

        elif choice == '4':
            # Return an item
            title = input("Enter the title of the item to return: ")
            library.return_item(title)

        elif choice == '5':
            # Exit
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
