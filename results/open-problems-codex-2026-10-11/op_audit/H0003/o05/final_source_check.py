from pathlib import Path
from html.parser import HTMLParser

base = Path(__file__).parent
text = (base/'fresh_source_text.txt').read_text(encoding='utf8')
for term in ['Definition 2.1 (Cascade system)', 'Conjecture 11.8 (Front-Markov property', 'initial state', 'initial condition']:
    pos = text.find(term)
    print(term, 'offset', pos)
    if pos >= 0:
        print(text[pos:pos+3100])

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
    def handle_data(self, data):
        self.data.append(data)
p = P()
p.feed((base/'later_abs.html').read_text(encoding='utf8'))
t = ' '.join(' '.join(p.data).split())
pos = t.find('Abstract:')
print('LATER ABSTRACT', t[pos:pos+4500])
for i, line in enumerate(Path('~/brain_workers/TRIO_1011/op/H0003/ATTEMPT.md').read_text(encoding='utf8').splitlines(),1):
    if line.startswith('## ') or any(term in line for term in ['intended nonvacuous', 'For each δ', 'If θ', 'These choices', 'choose three independent', 'No collision']):
        print('ATTEMPT LINE', i, line)
