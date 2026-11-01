import concurrent.futures
import itertools
import json
import math
from pathlib import Path
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln

BASE = Path(__file__).resolve().parent
report = {}

def fetch(item):
    name, url = item
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'IndependentProbabilityAudit/1.0'})
        with urllib.request.urlopen(req, timeout=45) as response:
            data = response.read()
        (BASE / name).write_bytes(data)
        return {'file': name, 'url': url, 'bytes': len(data), 'status': 'OK'}
    except Exception as exc:
        return {'file': name, 'url': url, 'status': str(exc)}

queries = [
    ('source_v5.pdf', 'https://arxiv.org/pdf/2002.03993v5'),
    ('arxiv_search.xml', 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': 'all:"Erlang Weighted Tree" OR all:"bilateral preference" OR all:"La-Kabkab"', 'max_results': 30})),
    ('openalex_search.json', 'https://api.openalex.org/works?' + urllib.parse.urlencode({'search': 'Erlang Weighted Tree', 'per-page': 10})),
    ('citations.json', 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2002.03993/citations?fields=title,year,externalIds&limit=100'),
    ('connectivity.pdf', 'https://arxiv.org/pdf/2209.05677v3'),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    report['fetches'] = list(pool.map(fetch, queries))
print(json.dumps(report['fetches'], indent=2), flush=True)

import pymupdf
for name in ['source_v5', 'connectivity']:
    p = BASE / (name + '.pdf')
    if p.exists():
        doc = pymupdf.open(p)
        text = '\n'.join(f'\nPDF PAGE {i+1}\n{page.get_text()}' for i, page in enumerate(doc))
        (BASE / (name + '.txt')).write_text(text, encoding='utf-8')
        report[name + '_pages'] = len(doc)

if (BASE / 'arxiv_search.xml').exists():
    root = ET.fromstring((BASE / 'arxiv_search.xml').read_bytes())
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    report['arxiv_titles'] = [e.findtext('a:title', namespaces=ns) for e in root.findall('a:entry', ns)]

# Independently integrate the fresh-child motif; includes very large budgets.
report['motif'] = []
for k in [2, 3, 7, 40]:
    for t in [0.5, 3, 9]:
        integral = quad(lambda z: math.exp(-z + (k-1)*math.log(z-t) - gammaln(k)), t, math.inf, epsabs=1e-12)[0]
        report['motif'].append({'budget': k, 't': t, 'integral': integral, 'target': math.exp(-t)})
assert max(abs(q['integral']-q['target']) for q in report['motif']) < 1e-10

# Exhaustive independent arrival test on K4, every budget and ordering.
edges = list(itertools.combinations(range(4), 2))
states = 0
for budgets in itertools.product([1, 2, 3], repeat=4):
    for ordering in itertools.permutations(edges):
        seen = set()
        counters = [0]*4
        parent = list(range(4))
        def find(i):
            while parent[i] != i:
                i = parent[i]
            return i
        for prefix in range(7):
            active = [i for i in range(4) if counters[i] < budgets[i]]
            for i, j in itertools.combinations(active, 2):
                if find(i) != find(j):
                    assert (i,j) not in seen
            states += 1
            if prefix < 6:
                i,j = ordering[prefix]
                if counters[i] < budgets[i] and counters[j] < budgets[j]:
                    parent[find(i)] = find(j)
                counters[i] += 1
                counters[j] += 1
                seen.add((i,j))
report['arrival_states'] = states

# Finite discrete slot model: derive the return kernel by a Schur complement
# rather than reuse claimant code. Deliberately use a nonsymmetric mean matrix.
m = np.array([1., 2., 5., 3.])
x = np.array([0.4, 1.2, 4., 9.])
mu = np.array([0.18, 0.31, 0.10, 0.41])
h = np.minimum(x[:,None], x[None,:]) / x[:,None]
M = m[:,None]*h*mu[None,:]
K = [1,3]; O = [0,2]
epsilon = float(mu[O] @ m[O])
assert epsilon < 1
R = M[np.ix_(K,K)] + M[np.ix_(K,O)] @ np.linalg.solve(np.eye(len(O))-M[np.ix_(O,O)], M[np.ix_(O,K)])
pi = mu[K]*x[K]/m[K]
balance = pi[:,None]*R
assert np.max(np.abs(balance-balance.T)) < 1e-12
partial = M[np.ix_(K,K)].copy()
power = np.eye(len(O))
errors = []
for n in range(30):
    partial += M[np.ix_(K,O)] @ power @ M[np.ix_(O,K)]
    assert np.all(partial <= R + 1e-12)
    errors.append(float(np.max(np.abs(partial-R))))
    power = power @ M[np.ix_(O,O)]
report['return_proxy'] = {'outside_potential': epsilon, 'balance_error': float(np.max(np.abs(balance-balance.T))), 'return_spectral_radius': float(max(np.linalg.eigvals(R).real)), 'truncation_errors': errors}

(BASE / 'independent_checks.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['fetches', 'motif']}, indent=2), flush=True)
