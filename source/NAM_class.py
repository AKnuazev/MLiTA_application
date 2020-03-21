from source.NAM_lookup_class import NAM_lookup


class NAM_worker:
    def __init__(self, input_word="", code=""):
        self.lookups=[]

        self.parse(code)
        self.calculate(input_word)

        # self.alphabet = input_alphabet + working_alphabet
        # self.empty_word = empty_word
        # self.lookups = lookups

    def generate_lookup(self, first_part, second_part, final=False):
        return NAM_lookup(first_part, second_part, final)

    def add_lookup(self, lookup):
        self.lookups.append(lookup)

    # TODO: add pasring
    # def parse_code(self, code):

    def calculate(self):
        while True:
            found = False
            for lookup in self.lookups:
                if self.input.find(lookup.first_part):
                    self.input.replace(lookup.first_part, lookup.second_part, 1)
                    if lookup.final:
                        break
                    found = True

            if not found:
                break

        return self.input
