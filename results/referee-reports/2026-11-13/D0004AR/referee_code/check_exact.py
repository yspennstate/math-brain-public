#!/usr/bin/env python3
"""Independent rational certificates. Reads no submitted files. Run from audit root."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import json
import resource
from pathlib import Path
from itertools import product
import sympy as s

R = s.Rational
x, t, u = s.symbols('x t u', real=True)
OUT = {}

def integral(terms, weight=1, lo=0, hi=1):
    return s.simplify(sum(s.integrate(weight*f, (x, max(a, lo), min(b, hi)))
                          for a,b,f in terms if max(a,lo) < min(b,hi)))

def call_piece(terms, z, probe):
    """Polynomial expression valid on the open piece containing probe."""
    total = 0
    for a,b,f in terms:
        zp = z.subs(t,probe) if hasattr(z,'subs') else z
        if zp >= b:
            continue
        lower = a if zp <= a else z
        total += s.integrate((x-z)*f, (x,lower,b))
    return s.expand(total)

def reflected_call_direct(terms,n,mu,probe):
    """Integrate (n*mu-(n-1)*x-t)_+ directly, without put-call parity."""
    c=n-1
    cut=(n*mu-t)/c
    zp=cut.subs(t,probe)
    total=0
    for a,b,f in terms:
        if zp<=a:
            continue
        upper=b if zp>=b else cut
        total+=s.integrate((n*mu-c*x-t)*f,(x,a,upper))
    return s.expand(total)

def bernstein(poly, a, b):
    p = s.Poly(s.expand(poly.subs(t,a+(b-a)*u)),u)
    d = p.degree()
    if d == -s.oo:
        return [s.S.Zero]
    return [s.simplify(sum(p.nth(j)*s.binomial(k,j)/s.binomial(d,j)
                           for j in range(k+1))) for k in range(d+1)]

def certify(poly,a,b,depth=0):
    bs = bernstein(poly,a,b)
    if min(bs) >= 0:
        return [{'interval':[str(a),str(b)],'polynomial':str(poly),
                 'bernstein':list(map(str,bs))}]
    assert depth < 20, (poly,a,b,bs)
    m = (a+b)/2
    return certify(poly,a,m,depth+1)+certify(poly,m,b,depth+1)

def audit_density(name, terms, n):
    mass, mu = integral(terms), integral(terms,x)
    assert mass == 1
    c = n-1
    z = (n*mu-t)/c
    ends = {s.S.Zero,s.S.One}
    for a,b,f in terms:
        assert min(f.subs(x,a),f.subs(x,b)) >= 0 or s.Poly(f,x).degree()>1
        ends.update([a,b,n*mu-c*a,n*mu-c*b])
    ends = sorted(q for q in ends if 0<=q<=1)
    pieces = []
    for a,b in zip(ends,ends[1:]):
        probe = (a+b)/2
        # C_Y(t) = c E(s-X)_+ = c (C_X(s)+s-mu).
        d = s.expand(c*(call_piece(terms,z,probe)+z-mu)
                     -call_piece(terms,t,probe))
        direct=s.expand(reflected_call_direct(terms,n,mu,probe)-call_piece(terms,t,probe))
        assert s.expand(d-direct)==0
        pieces.extend(certify(d,a,b))
    OUT[name] = {'n':n,'mass':str(mass),'mean':str(mu),
                 'call_gap_certificates':pieces,
                 'minimum_bernstein_bound':str(min(R(v) for p in pieces for v in p['bernstein']))}
    print(name, 'mass',mass,'mean',mu,'pieces',len(pieces),
          'Bernstein lower bound',OUT[name]['minimum_bernstein_bound'])
    return mu

g3 = [(R(0),R(1,10),s.Integer(5)),(R(9,10),R(1),s.Integer(5))]
g4 = [(R(0),R(1,20),s.Integer(12)),(R(19,20),R(1),s.Integer(8))]
h4 = [(R(0),R(1),R(157,100)-R(57,50)*x)]
f3 = [(a,b,R(9,10)*f) for a,b,f in g3]+[(R(0),R(1),R(1,10))]
f4 = [(a,b,R(9,10)*f) for a,b,f in g4]+[(a,b,f/10) for a,b,f in h4]
analytic = [(R(0),R(1),R(1,10)+R(27,10)*(2*x-1)**2)]
for name,terms,n in [('polynomial',analytic,3),('G3',g3,3),('G4',g4,4),
                     ('H4',h4,4),('F3',f3,3),('F4',f4,4)]:
    audit_density(name,terms,n)

# Independent reconstruction of the submitted cubic and its four coefficients.
mu = R(81,200)
d = s.expand(3*(call_piece(h4,(4*mu-t)/3,R(1,2))+(4*mu-t)/3-mu)
             -call_piece(h4,t,R(1,2)))
submitted = (11875000*t**3-35208750*t**2+17910675*t+10797948)/56250000
assert s.expand(d-submitted)==0
assert bernstein(d,0,1)==[R(299943,1562500),R(5589391,18750000),
                         R(2750537,14062500),R(5374873,56250000)]
qmid = integral(analytic,lo=R(1,4),hi=R(3,4))
assert qmid == R(13,80)
assert qmid==R(1,10)*R(1,2)+R(9,10)*R(1,2)**3
OUT['polynomial']['central_mass'] = str(qmid)

def sum_gap(n,eps,target):
    intervals = [(k*(1-eps),k*(1-eps)+n*eps) for k in range(n+1)]
    gap = min(max(a-target,target-b,0) for a,b in intervals)
    return gap, intervals

for name,terms,n,eps,mu in [('G3',g3,3,R(1,10),R(1,2)),
                           ('F3',f3,3,R(1,10),R(1,2)),
                           ('G4',g4,4,R(1,20),R(81,200)),
                           ('F4',f4,4,R(1,20),R(81,200)),
                           ('polynomial',analytic,3,R(1,5),R(1,2))]:
    gap, intervals = sum_gap(n,eps,n*mu)
    q = integral(terms,lo=eps,hi=1-eps)
    lb = gap**2*(1-n*q)
    assert gap>0 and q<R(1,n) and lb>0
    OUT[name].update({'sum_intervals':[[str(a),str(b)] for a,b in intervals],
                      'core_gap':str(gap),'outside_mass':str(q),'mse_lower_bound':str(lb)})
    print(name,'gap',gap,'outside',q,'MSE >=',lb)
assert OUT['polynomial']['mse_lower_bound']=='37/15625'
for n,gap in [(3,R(3,10)),(4,R(7,25))]:
    eta = R(1,100)
    lb = ((gap-n*eta)/(1+2*eta))**2*(1-R(n,10))
    assert lb>0
    OUT['smooth'+str(n)] = {'normalized_gap':str((gap-n*eta)/(1+2*eta)),
                             'outside_mass_bound':'1/10','mse_lower_bound':str(lb)}
    print('smooth',n,OUT['smooth'+str(n)])

def stoploss(law,z):
    return sum(p*max(v-z,0) for v,p in law)

def exact_cx(left,right):
    assert sum(p for v,p in left)==sum(p for v,p in right)==1
    if sum(v*p for v,p in left)!=sum(v*p for v,p in right):
        return False
    return all(stoploss(left,z)<=stoploss(right,z) for z in {v for v,p in left+right})

# For two finite laws, all support knots suffice, since call gaps are linear between them.
checks=0
for n in range(2,11):
    for den in range(2,26):
        for num in range(1,den):
            p=R(num,den)
            left=[(s.S.Zero,1-p),(s.S.One,p)]
            right=[(n*p,1-p),(n*p-(n-1),p)]
            passed=exact_cx(left,right)
            assert passed==(R(1,n)<=p<=1-R(1,n))
            # Enumerate all possible constant Bernoulli counts independently.
            counts=[k for k in range(n+1) if k==n*p]
            assert bool(counts)==bool((n*p).is_integer)
            checks+=1
OUT['bernoulli']={'exact_cases':checks,'n_range':[2,10],'denominators':[2,25]}

def count_vectors(m,n):
    if m==1:
        yield (n,)
    else:
        for k in range(n+1):
            for tail in count_vectors(m-1,n-k):
                yield (k,)+tail

atoms=[0,1,2]
p=[R(49,100),R(1,50),R(49,100)]
target=3*sum(a*w for a,w in zip(atoms,p))
counts=[k for k in count_vectors(3,3) if sum(a*c for a,c in zip(atoms,k))==target]
assert counts==[(0,3,0),(1,1,1)]
assert min(k[1] for k in counts)>3*p[1]
assert exact_cx(list(zip(atoms,p)),[(3-2*a,w) for a,w in zip(atoms,p)])
OUT['reachable_discrete']={'admissible_counts':counts,'target':str(target),
                           'dual_certificate':'all admissible k have k[1]>=1, but 3*p[1]=3/50'}
print('Bernoulli exact cases:',checks,'; reachable discrete obstruction:',counts)

# Symbolic audit of the heavy-tail mean and asymptotic ratio, without huge exponentials.
L,m=s.symbols('L m',positive=True)
tailmass=s.integrate(1/u**2,(u,L,2*L))
assert tailmass==1/(2*L)
logterm=L+s.log(2*m)-s.log(1-s.exp(-L))
ratio=logterm**2/(4*m*L)
assert s.limit(ratio/L,L,s.oo)==1/(4*m)
OUT['nonfatou']={'interval_integral':str(tailmass),'ratio_over_L_limit':'1/(4*m)',
                 'mean':'1/3','index_convention':'k=1,2,...'}

OUT['runtime']={'threads':1,'sympy':s.__version__,
                'maxrss_native':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                'maxrss_note':'bytes on macOS; KiB on Linux'}
path=Path('referee_code/exact_results.json')
path.write_text(json.dumps(OUT,indent=2)+'\n')
print('All exact assertions passed. Certificate:',path)
print('Resource usage:',OUT['runtime'])
