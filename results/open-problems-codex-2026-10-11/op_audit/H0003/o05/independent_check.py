from pathlib import Path
from fractions import Fraction as F
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

base = Path(__file__).parent
text = BeautifulSoup((base/'source.html').read_text(encoding='utf8'), 'html.parser').get_text(' ', strip=True)
(base/'source_text.txt').write_text(text, encoding='utf8')
terms = ['Definition 2.1', 'Definition 2.3', 'Hypothesis 2.4', 'Conjecture 11.8', 'Example 9.2', 'initial', 'safe', 'saturated forcing', 'first-passage']
excerpts = []
for term in terms:
    start = 0
    for i in range(8):
        pos = text.find(term, start)
        if pos < 0:
            break
        excerpts.append(f'\nTERM {term}; OFFSET {pos}\n{text[max(0,pos-200):pos+4000]}\n')
        start = pos + len(term)
(base/'source_excerpts.txt').write_text(''.join(excerpts), encoding='utf8')
print(''.join(excerpts[:12]))

p = F(3,4)
q = ((1-p)/p)**2
assert q == F(1,9)
assert (1-p+p*q)**2 == q
assert 1-q == F(8,9)
assert (1-p+p*q)**3 == F(1,27)
# Independently compare polynomial coefficients of f(s)-s and the factorization.
assert [(1-p)**2, 2*p*(1-p)-1, p*p] == [F(1,16), F(-10,16), F(9,16)]
a = F(0)
iterations = []
for k in range(8):
    b = (1-p+p*a)**2
    assert a <= b <= q
    iterations.append({'generation': k+1, 'extinction_probability': float(b)})
    a = b
result = {'q': str(q), 'survival': str(1-q), 'root_degree_3_survival': str(1-(1-p+p*q)**3), 'iterations': iterations, 'checks': 'all exact rational assertions passed'}
(base/'independent_results.json').write_text(json.dumps(result, indent=2), encoding='utf8')
print(json.dumps(result, indent=2))
ns = {'a':'http://www.w3.org/2005/Atom'}
root = ET.parse(base/'arxiv_search.xml').getroot()
for entry in root.findall('a:entry', ns):
    title = entry.findtext('a:title', '', ns)
    summary = entry.findtext('a:summary', '', ns)
    if any(word in title.lower() for word in ['cascade', 'decoupling', 'threshold']):
        print('LITERATURE', entry.findtext('a:id', '', ns), title, summary)
later = BeautifulSoup((base/'later_abs.html').read_text(encoding='utf8'), 'html.parser')
abstract = later.find('blockquote', class_='abstract')
print('LATER ABSTRACT', abstract.get_text(' ', strip=True) if abstract else 'not found')
