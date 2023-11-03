import re
import reprlib

RE_WORD = re.compile(r'\w+')

class sentence:
    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __iter__(self):
        for word in self.words:
            yield word
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
s = sentence('"The time has come,"the walrus said,')
print(s)
for word in s:
    print(word)