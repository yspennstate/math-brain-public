from pathlib import Path
from fractions import Fraction as F
from html.parser import HTMLParser
import json
import xml.etree.ElementTree as ET

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)

base = Path(__file__).parent
p = F(3, 4)
q = F(1, 9)
assert (1-p+p*q)**2 == q
assert [(1-p)**2, 2*p*(1-p)-1, p*p] == [F(1,16), F(-10,16), F(9,16)]
assert 1-q == F(8,9)
assert 1-(1-p+p*q)**3 == F(26,27)
a = F(0)
values = []
for k in range(7):
    b = (1-p+p*a)**2
    assert a <= b <= q
    a = b
    values.append(float(a))
result = dict(extinction=str(q), survival=str(1-q), corrected_root_survival=str(1-(1-p+p*q)**3), extinction_iterations=values, exact_assertions='passed')
(base/'fast_results.json').write_text(json.dumps(result, indent=2), encoding='utf8')
print(json.dumps(result), flush=True)
parser = Text()
parser.feed((base/'source.html').read_text(encoding='utf8'))
text = ' '.join(' '.join(parser.parts).split())
(base/'fresh_source_text.txt').write_text(text, encoding='utf8')
out = []
for term in ['Definition 2.1', 'Definition 2.3', 'Hypothesis 2.4', 'Conjecture 11.8', 'Example 9.2', 'finite connected', 'initial']:
    pos = text.find(term)
    out.append(f'\n{term}:\n{text[max(pos-80,0):pos+3200]}\n')
(base/'fresh_excerpts.txt').write_text(''.join(out), encoding='utf8')
print(''.join(out), flush=True)
root = ET.parse(base/'arxiv_search.xml').getroot()
ns = {'a':'http://www.w3.org/2005/Atom'}
for entry in root.findall('a:entry',ns):
    title = entry.findtext('a:title','',ns)
    if any(w in title.lower() for w in ['cascade','decoupling']):
        print(entry.findtext('a:id','',ns),title,entry.findtext('a:summary','',ns), flush=True)
