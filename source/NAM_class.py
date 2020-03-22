from source.NAM_lookup_class import NAM_lookup
from source.parsing_tools import separate_to_lines


class NAM_worker:
    def __init__(self, output, input_word="", code=""):
        self.lookups = []
        self.output = output

        # success_status = self.parse_code(code)
        # if success_status:
        #     self.calculate(input_word)
        # else:
        #     return False, self.report

        self.report = ""
        # self.alphabet = input_alphabet + working_alphabet
        # self.empty_word = empty_word
        # self.lookups = lookups

    def add_lookup(self, first_part, second_part, final=False):
        self.lookups.append(NAM_lookup(first_part, second_part, final))

    # def add_lookup(self, lookup):
    #     self.lookups.append(lookup)

    def parse_line(self, line):
        first_part = ""
        second_part = ""
        final = False

        if line.find("->") == -1:
            self.report = "Error:\n No '->' symbol in one of lines"
            return False
        else:
            line = line.replace("->", " ", 1)

            if line.find("->") != -1:
                self.report = "Error:\n More than one -> in one line\n\n Note: If you tried to write two commands in one line - replace them to two lines and don`t do like that anymore please :)"
                return False
            else:
                move = 0
                if line[line.find(' ') + 1] == '.':
                    final = True
                    move = 1

                first_part = line[0:line.find(' ')]
                second_part = line[line.find('') + 1 + move:len(line)]

                self.add_lookup(first_part, second_part, final)
                return True  # Success

    # TODO: add pasring
    def parse_code(self, code):
        lines = separate_to_lines(code)

        for line in lines:
            if not self.parse_line(line):
                return False
        return True

    def calculate(self, input_word):
        counter = 0
        while True:
            counter += 1
            self.output.addItem(str(counter) + ") " + input_word + '\n')
            found = False
            for lookup in self.lookups:
                if input_word.find(lookup.first_part):
                    input_word = input_word.replace(lookup.first_part, lookup.second_part, 1)
                    if lookup.final:
                        break
                    found = True

            if not found:
                break

        return input_word
