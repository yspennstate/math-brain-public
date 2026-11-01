from pathlib import Path
import concurrent.futures as cf
import urllib.request, urllib.parse, json, math, xml.etree.ElementTree as ET
from fractions import Fraction as F
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
queries = {
    'source': 'https://arxiv.org/pdf/2202.02366',
    'arxiv': 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': 'all:"symmetric queues" OR (all:"symmetric queue" AND all:"diffusion")', 'start': 0, 'max_results': 40}),
    'openalex': 'https://api.openalex.org/works?' + urllib.parse.urlencode({'search': 'symmetric queues heavy traffic diffusion', 'per-page': 30}),
    'crossref': 'https://api.crossref.org/works?' + urllib.parse.urlencode({'query': 'symmetric queues heavy traffic diffusion', 'rows': 30}),
}

def fetch(item):
    name, url = item
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'IndependentMathematicalAudit/1.0'})
        with urllib.request.urlopen(req, timeout=45) as res:
            data = res.read()
            status = res.status
        path = ROOT / (name + ('.pdf' if name == 'source' else '.response'))
        path.write_bytes(data)
        record = {'url': url, 'status': status, 'bytes': len(data)}
        if name == 'source':
            text = '\n'.join(p.extract_text() or '' for p in PdfReader(path).pages)
            (ROOT / 'source.txt').write_text(text, encoding='utf-8')
            record['text'] = text
        elif name == 'arxiv':
            ns = {'a': 'http://www.w3.org/2005/Atom'}
            record['entries'] = [{'title': e.findtext('a:title', namespaces=ns), 'id': e.findtext('a:id', namespaces=ns), 'summary': e.findtext('a:summary', namespaces=ns)} for e in ET.fromstring(data).findall('a:entry', ns)]
        elif name == 'openalex':
            record['entries'] = [{'title': e.get('title'), 'year': e.get('publication_year'), 'doi': e.get('doi')} for e in json.loads(data).get('results', [])]
        else:
            record['entries'] = [{'title': e.get('title'), 'doi': e.get('DOI')} for e in json.loads(data)['message']['items']]
        return name, record
    except Exception as exc:
        return name, {'url': url, 'error': str(exc)}

with cf.ThreadPoolExecutor(max_workers=4) as pool:
    network = dict(pool.map(fetch, queries.items()))
(ROOT / 'literature_checks.json').write_text(json.dumps(network, indent=2, ensure_ascii=False), encoding='utf-8')
for name, record in network.items():
    print(name, json.dumps(record, ensure_ascii=False))

# Exact Irwin-Hall tails, including mixed original marks under H.
def uniform_tail(k, y):
    if k == 0:
        return F(int(y < 0))
    if y <= 0:
        return F(1)
    if y >= k:
        return F(0)
    cdf = sum((-1)**i * math.comb(k, i) * (y-i)**k for i in range(int(y)+1)) / math.factorial(k)
    return 1-cdf

rho = F(4, 5)
pi_mark = sum((1-rho)*rho**n * sum(F(math.comb(n,k),2**n)*uniform_tail(k,F(5,9)) for k in range(n+1)) for n in range(1,7))
pi_det = sum((1-rho)*rho**n * uniform_tail(n,F(2)) for n in range(7))
assert pi_mark == F(117178177528,373669453125)
assert pi_det == F(552032,3515625)

tests = 0
worst_ratio = 0.0
for n in range(1,21):
    mu, raw2, b = F(9,4), F(27,2), F(9,2)
    for x in range(1,91):
        z = F(x,2)
        threshold = (n*mu+z)/9
        prob = sum(F(math.comb(n,k),2**n)*uniform_tail(k,threshold) for k in range(n+1))
        bound = math.exp(-float(F(x*x)/(8*(n*raw2+b*F(x,3)))))
        assert float(prob) <= bound + 1e-12
        tests += 1
        worst_ratio = max(worst_ratio, float(prob)/bound)

# Exact augmented-generator cancellation for f=product_i(1+c(B_i)R_i).
# B=1 (p=.9), B=9 (p=.1); f=1 at residual zero, so deletion-compatible.
m = F(9,5)
generator_tests = []
for c1, c9 in [(F(-1,2),F(-1,18)), (F(0),F(-1,9)), (F(-1),F(0))]:
    A = 1 + (F(9,10)*c1 + F(1,10)*81*c9)/(2*m)
    d = (F(9,10)*c1 + F(9,10)*c9)/m
    J = 1 + F(9,10)*c1 + F(9,10)*c9
    lam = rho/m
    residual = (1-rho)*(-rho*d+lam*(J-1))/(1-rho*A)
    assert residual == 0
    generator_tests.append(str(residual))

q = 2**(-.25)
dyadic_tests = 0
for C in [0.1,1,10,100]:
    for eps in [.01,.1,1,10]:
        constant = eps**2 * (1-q)**2 / (4*(C*10+eps/3))
        for j in range(160):
            aj = (1-q)*q**j
            r, b, w = 123456., 123456.*2**(-(j+1)), 10.
            x = eps*r*aj
            V = C*r*b*w
            exponent = x*x/(8*(V+b*x/3))
            assert exponent >= constant*2**(j/2)*(1-1e-12)
            dyadic_tests += 1

result = {'exact_pi_deterministic': str(pi_det), 'exact_reward_deterministic': str(5*pi_det), 'exact_pi_marked': str(pi_mark), 'exact_reward_marked': str(pi_mark/2), 'bernstein_exact_distribution_tests': tests, 'largest_probability_to_bound_ratio': worst_ratio, 'generator_cancellations': generator_tests, 'dyadic_constant_tests': dyadic_tests, 'all_passed': True}
(ROOT / 'math_checks.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print('MATHEMATICAL CHECKS', json.dumps(result))
