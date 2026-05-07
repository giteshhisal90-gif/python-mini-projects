class library:
    librayanme = 0
    def __init__(self):
        self.noOfbooks = 0
        self.books = []
    def addbook(self,book):
        self.books.append(book)
        self.noOfbooks  = len(self.books)
    def showcount(self):
        library.librayanme += 1
        print(f"\n*libtary {self.librayanme}*\n")
        print(f"The no. of Books are : {self.noOfbooks}\n")
        for book in self.books:
            print(book)
while True:
    str = "WELLCOME IN OUR library"
    print(str.center(50))
    print("Please enter your choice : ")
    print("1.library 1")
    print("2.library 2")
    print("3.library 3")
    print("4.library 4")
    print("5.Exit")
    lab = input("Enter a choice : ")
    match lab :
        case "1" :
            l1 = library()
            l1 . addbook("> Power")
            l1 . addbook("> Black swan")
            l1 . addbook("> Read people like a book")
            l1 . addbook("> How to talk")
            l1 . addbook("> Money")
            l1 . addbook("> victry")
            l1.showcount()
        case "2":
            l2 = library()
            l2.addbook("> Harry Potter and the Philosopher's Stone ")
            l2.addbook("> The Diary of a Young Girl")
            l2.addbook("> The Alchemist")
            l2.addbook("> The Great Gatsby")
            l2.addbook("> Pride and Prejudice")
            l2.addbook("> The White Tiger")
            l2.addbook("> The Forest of Enchantments ")
            l2.showcount()
        case "3":
            print("library coming soon !!")
        case "4":
            print("library coming soon !!")
        case "5":
            print("Thank you for visiting")
            break
        case _ :
            print("These library is not avalable right now !!")
            print("Thank you")