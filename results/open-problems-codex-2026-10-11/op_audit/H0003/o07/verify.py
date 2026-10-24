import concurrent.futures
import json
import pathlib
import urllib.request
import xml.etree.ElementTree as ET
from fractions import Fraction as F
from bs4 import BeautifulSoup
from scipy.integrate import quad
from scipy.optimize import brentq

BASE = pathlib.Path(__file__).resolve().parent
URLS = {
    'fresh_source.html': 'https://arxiv.org/html/2608.15987v1',
    'fresh_arxiv.xml': 'https://export.arxiv.org/api/query?search_query=all%3A%22front-Markov%22%20OR%20all%3A%22multiscale%20front-decoupling%22&max_results=15',
    'fresh_openalex.json': 'https://api.openalex.org/works?search=Threshold%20cascades%20interacting%20diffusions%20unimodular&per-page=10',
    'fresh_later_abs.html': 'https://arxiv.org/abs/2609.27972',
}

def fetch(item):
    name, url = item
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'ProbabilityAudit/1.0'})
        with urllib.request.urlopen(req, timeout=35) as r:
            data = r.read()
            (BASE / name).write_bytes(data)
            return dict(file=name, url=url, status=r.status, bytes=len(data))
    except Exception as e:
        return dict(file=name, url=url, error=str(e))

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, URLS.items()))
(BASE / 'fetch_log.json').write_text(json.dumps(results, indent=2), encoding='utf8')
print(json.dumps(results, indent=2), flush=True)
for name in ['fresh_source.html', 'fresh_later_abs.html']:
    p = BASE / name
    if p.exists():
        soup = BeautifulSoup(p.read_text(encoding='utf8'), 'html.parser')
        (BASE / name.replace('.html', '.txt')).write_text(soup.get_text(' ', strip=True), encoding='utf8')
        if name == 'fresh_source.html':
            excerpts = []
            for sid in ['S2.SS2', 'S2.SS3', 'S2.SS4', 'S9', 'S11.SS5']:
                section = soup.find(id=sid)
                if section:
                    excerpts.append(sid + '\n' + section.get_text(' ', strip=True))
            (BASE / 'fresh_source_excerpts.txt').write_text('\n\n'.join(excerpts), encoding='utf8')
            print('FRESH CONJECTURE:', soup.find(id='S11.SS5').get_text(' ', strip=True) if soup.find(id='S11.SS5') else 'section missing', flush=True)
        if name == 'fresh_later_abs.html':
            abstract = soup.find('blockquote', class_='abstract')
            print('LATER ABSTRACT:', abstract.get_text(' ', strip=True) if abstract else 'not found', flush=True)
if (BASE / 'fresh_arxiv.xml').exists():
    root = ET.fromstring((BASE / 'fresh_arxiv.xml').read_bytes())
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    print('ARXIV RESULTS:', [(e.findtext('a:id', namespaces=ns), e.findtext('a:title', namespaces=ns)) for e in root.findall('a:entry', ns)], flush=True)
if (BASE / 'fresh_openalex.json').exists():
    obj = json.loads((BASE / 'fresh_openalex.json').read_text(encoding='utf8'))
    print('OPENALEX RESULTS:', [(x['id'], x['display_name']) for x in obj.get('results', [])], flush=True)

f = lambda s: (F(1, 4) + F(3, 4) * s)**2
assert f(F(1, 9)) == F(1, 9)
assert 1 - F(1, 9) == F(8, 9)
assert (F(1, 4) + F(3, 4)*F(1, 9))**3 == F(1, 27)
for s in [F(i, 100) for i in range(101)]:
    assert f(s) - s == (s-1)*(9*s-1)/16
a = F(0)
early = []
for k in range(6):
    a = f(a)
    assert 0 <= a <= F(1, 9)
    early.append(float(a))
import math
ou = []
for h in [2., 3., 5., 10.]:
    # Common scaling prevents overflow without changing the ratio.
    shift = max(1., (h-1)**2)
    integrand = lambda y: math.exp((y-1)**2-shift)
    den = quad(integrand, 0, h, epsabs=1e-13)[0]
    prob = lambda x: quad(integrand, 0, x, epsabs=1e-13)[0]/den
    x = brentq(lambda x: prob(x)-.75, 0, h, xtol=1e-12)
    ou.append(dict(h=h, x=x, p=prob(x)))
checks = dict(survival='8/9', corrected_root_survival='26/27', extinction_iterations=early, ou_checks=ou)
(BASE / 'independent_checks.json').write_text(json.dumps(checks, indent=2), encoding='utf8')
print('INDEPENDENT CHECKS:', json.dumps(checks), flush=True)
