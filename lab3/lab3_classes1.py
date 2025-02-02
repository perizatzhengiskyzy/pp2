class StringManipulator:
    def __init__(self):
        self.text = ""

    def get_text(self):
        self.text = input("Enter a string: ")

    def print_text(self):
        print(self.text.upper())

if __name__ == "__main__":
    manipulator = StringManipulator()
    manipulator.get_text()
    manipulator.print_text()
