class WordsFinder:
    file_names=[]
    all_words={}
    def __init__(self, *txt_file):
        for i in range(len(txt_file)):
            self.file_names.append(txt_file[i])
        for i in range(0, len(self.file_names)):
            n = ''
            with open(self.file_names[i], encoding='utf-8') as file:
                for line in file:
                    a = ''
                    for char in line:
                        if char not in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            a = a + char
                        else:
                            a += ' '
                    n += a

                s = list(n.split())
                self.all_words[self.file_names[i]] = s



    def get_all_words(self):
        return self.all_words
    def find(self, word):
        f={}
        a=0
        b=word.upper()
        for name in self.file_names:
            g=[]
            for i in range(len(self.all_words[name])):
                g.append(self.all_words[name][i].upper())
            if b in g and a==0:
                f[name]=g.index(word)+1
                a=1
        return f
    def count(self, word):
        f = {}
        a = 0
        b = word.upper()
        for name in self.file_names:
            g = []
            for i in range(len(self.all_words[name])):
                g.append(self.all_words[name][i].upper())
            if b in g and a == 0:
                f[name] = g.count(b)
                a = 1
        return f

finder2 = WordsFinder('test_file1.txt', 'test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
