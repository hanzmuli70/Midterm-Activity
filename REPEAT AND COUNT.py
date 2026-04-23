class Repeater:
    def repeat(self):
        word = input("Enter a word: ")
        count = int(input("How many times? "))
        for i in range(count):
            print(word)

rep = Repeater()
rep.repeat()