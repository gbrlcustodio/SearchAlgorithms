from settings import Settings
import re

class FileParser:
    def __init__(self, file_name):
        self._vertices = set()
        self.dictionary = {}
        self.file_name = file_name
        if Settings.debug: print('created a reference to file %s' % file_name)

    def read_content(self):
        if Settings.debug: print('reading file content...')

        try:
            file = open(self.file_name, 'r')
        except IOError:
            print('Could not open file!')

        for line in file:
            self.parse_line(line.rstrip('\n'))

        file.close()

        self.dictionary['vertices'] = list(self._vertices)

        return self.dictionary

    def parse_line(self, line):
        if Settings.debug: print('parsing line "%s"' % line)
        regex = re.compile(r'^(\S*)\(')
        matched = regex.match(line)

        if matched:
            token = matched.group(1)
            if self.dictionary.get(token) is None:
                self.dictionary[token] = []

            regex = re.compile(r'(\w*)[,\)]')
            self.dictionary[token].append(regex.findall(line))

            if token == 'caminho':
                self._vertices |= set(self.dictionary[token][-1][0:2])
        else:
            print('\tThere is no matched token. Invalid entry!')
