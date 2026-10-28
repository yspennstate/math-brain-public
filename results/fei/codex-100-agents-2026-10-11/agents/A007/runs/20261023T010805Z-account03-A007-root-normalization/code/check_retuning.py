"""Frozen, independent exact audit of the actual overlapping-prime obstruction."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json, time, hashlib

ROOT = Path(__file__).resolve().parents[1]
start = time.monotonic()
checks = 0
def ck(value):
    global checks
    assert value
    checks += 1
    assert time.monotonic() - start < 55

def log_interval(value):
    exponent = 0
    while value >= 2:
        value /= 2
        exponent += 1
    while value < 1:
        value *= 2
        exponent -= 1
    def series(z):
        total = sum((2*z**(2*k+1)/F(2*k+1) for k in range(96)), F(0))
        error = 2*z**193/(193*(1-z*z))
        return total, total+error
    lo, hi = series((value-1)/(value+1))
    a, b = series(F(1,3))
    return (lo+exponent*a, hi+exponent*b) if exponent >= 0 else (lo+exponent*b, hi+exponent*a)

def scale(interval, number):
    return tuple(number*x for x in interval) if number >= 0 else tuple(number*x for x in reversed(interval))

def display_enclosure(interval):
    # Compress by verified outward rounding, without decimal conversion of giant integers.
    denominator = 2**256
    lower = F((interval[0]*denominator).__floor__(),denominator)
    upper = F((interval[1]*denominator).__ceil__(),denominator)
    ck(lower <= interval[0] <= interval[1] <= upper)
    return [str(lower),str(upper)]

truth = [1 if ((z>>1)&1) and ((z&1) or ((z>>2)&1)) else -1 for z in range(8)]
mean = F(sum(truth),8)
influences = [F(sum(truth[z] != truth[z^(1<<i)] for z in range(8)),8) for i in range(3)]
ck(influences == [F(1,4), F(3,4), F(1,4)])
variance, influence = 1-mean**2, sum(influences)
ck(variance == F(15,16) and influence == F(5,4))
fourier = [F(sum(truth[z]*(-1)**((z&s).bit_count()) for z in range(8)),8) for s in range(8)]
ck(sum(c*c for c in fourier) == 1)
ck(sum(s.bit_count()*c*c for s,c in enumerate(fourier)) == influence)
# Enumerate every signed conjunction; prime means no proper face obtained by deletion is an implicant.
implicants = set()
for signs in product([-1,0,1], repeat=3):
    if not any(signs):
        continue
    points = [z for z in range(8) if all(not s or bool(z>>i&1)==(s==1) for i,s in enumerate(signs))]
    if all(truth[z] == 1 for z in points):
        implicants.add(signs)
primes = set()
for signs in implicants:
    if all(tuple(0 if j==i else s for j,s in enumerate(signs)) not in implicants for i,s in enumerate(signs) if s):
        primes.add(signs)
ck(primes == {(1,1,0), (0,1,1)})
ln2 = log_interval(F(2))
ck(ln2[0] >= F(2,3) and ln2[1] > F(2,3))
records = []
for j in [1,2,8,32,128]:
    delta = F(1,2**j)
    old = [delta/2, delta**2/2]
    new = [delta**3/2, delta**2/2]
    ck(all(0<b<=a for a,b in zip(old,new)))
    ck(sum(old) <= F(3,8))
    x,y = [a/4 for a in old], [a/4 for a in new]
    dx,dy = x[0]+x[1]+x[0]*x[1], y[0]+y[1]+y[0]*y[1]
    px = [x[0]/dx,x[1]/dx,x[0]*x[1]/dx]
    py = [y[0]/dy,y[1]/dy,y[0]*y[1]/dy]
    ck(sum(px) == sum(py) == 1)
    ck(sum(y)/sum(x) == delta)
    # Directly sum the three likelihood ratios, without the marginal identity.
    kl = [F(0),F(0)]
    for p,q in zip(py,px):
        term = scale(log_interval(p/q),p)
        kl = [kl[k]+term[k] for k in range(2)]
    bit_kl = [kl[0]/ln2[1],kl[1]/ln2[0]]
    name = j*(1-delta)/(1+delta)
    loss = (delta-delta**3)/8
    error = loss/ln2[1]
    assert bit_kl[0] > name-error and bit_kl[1] < name+error, ('precision audit',j,str(bit_kl[0]-name),str(bit_kl[1]-name),str(error))
    checks += 1
    norm = log_interval(dy/(dx*delta))
    ck(-loss <= norm[0] <= norm[1] < 0)
    ck(F(3,4)*bit_kl[0] > F(3,4)*j-1)
    ck(j*delta <= F(1,2))
    records.append({'j':j,'name_KL_bits':str(name),'root_KL_bits_interval':display_enclosure(bit_kl),
                    'signed_normalizer_remainder_nats':display_enclosure(norm), 'lost_activity':str(loss)})
result = {'status':'PASS','assertions':checks,'parameter_cases':len(records),
          'truth':truth,'fourier_coefficients':list(map(str,fourier)),
          'physical_influences':list(map(str,influences)), 'primes':[list(p) for p in sorted(primes)],
          'arithmetic':'Fraction; 96-term atanh series with rational geometric tail',
          'records':records,'seconds':time.monotonic()-start,
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out'/'retuning.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k != 'records'}))
