class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for character in key:
            total += ord(character)
        return total % self.size

    def insert(self, key, value):
        contact = Contact(key, value)
        index = self.hash_function(key)

        if self.data[index] is None:
            self.data[index] = Node(key, contact)
            return

        current = self.data[index]

        while current is not None:
            if current.key == key:
                current.value.number = value
                return

            if current.next is None:
                break

            current = current.next

        current.next = Node(key, contact)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        return None

    def print_table(self):
        for index in range(self.size):
            print(f"Index {index}:", end="")

            current = self.data[index]

            if current is None:
                print(" Empty")
                continue

            while current is not None:
                print(f" - {current.value}", end="")
                current = current.next

            print()

# Test your hash table implementation here.  
table = HashTable(10)

# Test an empty table
print("Initial table:")
table.print_table()

# Insert contacts
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")

print("\nTable after inserting contacts:")
table.print_table()

# Search for a contact
contact = table.search("John")
print("\nSearch result:", contact)

# Test collision handling
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")

print("\nTable after inserting Amy and May:")
table.print_table()

# Test updating an existing contact
table.insert("Rebecca", "999-444-9999")

print("\nTable after updating Rebecca:")
table.print_table()

# Test searching for a missing contact
print("\nSearch for Chris:", table.search("Chris"))