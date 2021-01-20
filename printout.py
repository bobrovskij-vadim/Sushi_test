import tempfile
import os


class Printout:
    def __init__(self, text_print):
        filename = tempfile.mktemp(".txt")
        open(filename, "w").write(text_print)
        os.startfile(filename, "print")
