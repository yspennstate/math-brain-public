from itertools import permutations, product
from pathlib import Path
import sympy as s
import requests
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
def cycles(p):
    seen = set()
    count = 0
    for i in range(len(p)):
        if i not in seen:
            count += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return count

def weighted(A, a, determinant=True):
    n = A.rows
    return s.expand(sum(a**(n-cycles(p) if determinant else cycles(p)) * s.prod(A[i,p[i]] for i in range(n)) for p in permutations(range(n))))

a = s.symbols('a')
A = s.Matrix([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
assert A.eigenvals() == {3:2,0:1}
assert s.expand(weighted(A,a)-2*(4-a)*(a+1)) == 0
print('Original 3x3 matrix: eigenvalues 0,3,3; det_alpha =', s.factor(weighted(A,a)))
U = s.Matrix([[1,0,1],[0,1,-1]])
G = U.T*U
x = s.symbols('x0:3')
t = s.symbols('t')
X = s.diag(*x)
assert (s.eye(2)-U*X*U.T).det() == (s.eye(3)-X*G).det()
beta = s.Rational(2,3)
series = s.Poly(s.series((s.eye(3)-t*X*G).det()**(-beta),t,0,5).removeO().subs(t,1).expand(), *x)
count = 0
for r in product(range(5), repeat=3):
    n = sum(r)
    if n > 4:
        continue
    indices = [i for i in range(3) for _ in range(r[i])]
    R = G.extract(indices,indices)
    permanent = weighted(R,beta,False)
    assert series.coeff_monomial(s.prod(x[i]**r[i] for i in range(3))) == permanent / s.prod(s.factorial(k) for k in r)
    assert weighted(R,1/beta) == (1/beta)**n * permanent
    count += 1
print('Exact Sylvester identity and',count,'MacMahon coefficients/parameter conversions checked (total degree <=4).')
print('These algebra checks do not construct the alpha=3/2 negative witness; its existence is a cited theorem.')

url = 'https://export.arxiv.org/api/query?search_query=ti:%22Solutions%20to%20two%20problems%20on%20permanents%22&max_results=5'
r = requests.get(url,timeout=50)
(ROOT/'arxiv_targeted.xml').write_bytes(r.content)
print('Targeted arXiv search:',r.status_code)
if r.ok:
    ns = {'a':'http://www.w3.org/2005/Atom'}
    for e in ET.fromstring(r.content).findall('a:entry',ns):
        print(e.find('a:id',ns).text,e.find('a:title',ns).text,e.find('a:summary',ns).text)
