class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    # возвращает словарь с ключом названия файла и значением списка всех слов в файле
    def get_all_words(self):
        all_words = {}
        ln = ''
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punc:
                        line = line.replace(i, '')
                ln = ln + line
            all_words.update({self.file_names: ln.split()})
        return all_words

    # возвращает словарь с ключом названия файла и значением первой позиции слова
    def find(self, wl):
        dl = {}
        world = self.get_all_words()[self.file_names]
        for i in range(len(world)):
            if wl.lower() == world[i]:
                dl.update({self.file_names: i + 1})
                return dl

    # возвращает словарь с ключом названия файла и значением количества слов
    def count(self, wd):
        dd = {}
        world = self.get_all_words()[self.file_names]
        dd.update({self.file_names: world.count(wd.lower())})
        return dd


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего