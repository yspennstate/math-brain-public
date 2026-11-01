"""Exact sign-function spectra. No entropy or floating arithmetic.

Tables: x=0..2**n-1, little-endian coordinates. Uniform characters
are (-1)**popcount(x&s). Biased basis is (x_i-p_i)/sqrt(p_i(1-p_i)).
fwht is reused verbatim from A016/check_addressing.py (see source receipts).
"""
from fractions import Fraction as F
from math import prod

VERSION = 'A072-exact-walsh/1'

def fwht(v):
    v = list(v)
    h = 1
    while h < len(v):
        for i in range(0,len(v),2*h):
            for j in range(i,i+h):
                u,w=v[j],v[j+h]
                v[j],v[j+h]=u+w,u-w
        h*=2
    return v

def validate(table):
    if not table or len(table) & (len(table)-1):
        raise ValueError('Nonempty power-of-two table required')
    if any(type(x) is not int or x not in (-1,1) for x in table):
        raise ValueError('Integer Boolean signs required')
    return len(table).bit_length()-1

def uniform_certificate(table):
    n=validate(table); N=len(table); W=fwht(table)
    assert sum(w*w for w in W)==N*N
    assert fwht(W)==[N*x for x in table]
    assert W==[sum(table[x]*(-1 if (x&s).bit_count()%2 else 1)
                          for x in range(N)) for s in range(N)]
    spectral=[F(w*w,N*N) for w in W]
    edges=[sum(table[x]!=table[x^(1<<i)] for x in range(N) if not x>>i&1)
           for i in range(n)]
    influences=[F(2*e,N) for e in edges]
    for i in range(n):
        assert influences[i]==sum(spectral[s] for s in range(N) if s>>i&1)
    return {'n':n,'walsh':W,'denominator':N,'undirected_edges':edges,
            'influences':influences,'spectrum':spectral}

def biased_certificate(table, biases):
    n=validate(table); N=len(table); p=tuple(map(F,biases))
    if len(p)!=n or any(not 0<q<1 for q in p):
        raise ValueError('One interior rational bias per coordinate required')
    W=fwht(table)
    # Expand each uniform character t_i=1-2*x_i into
    # (1-2*p_i)-2*(x_i-p_i). Coefficients b have no radicals.
    b=[]
    for s in range(N):
        b.append((-2)**s.bit_count()*sum((F(W[u],N)*prod(
            1-2*p[i] for i in range(n) if (u^s)>>i&1)
            for u in range(N) if u&s==s),F(0)))
    var=[q*(1-q) for q in p]
    spectral=[b[s]**2*prod(var[i] for i in range(n) if s>>i&1)
              for s in range(N)]
    assert sum(spectral)==1
    for x in range(N):
        inverse=sum((b[s]*prod(F((x>>i)&1)-p[i] for i in range(n) if s>>i&1)
                     for s in range(N)),F(0))
        assert inverse==table[x] and inverse in (-1,1)
    pivotal=[]
    for i in range(n):
        pivotal.append(sum((prod(p[j] if x>>j&1 else 1-p[j]
                              for j in range(n) if j!=i)
                             for x in range(N) if not x>>i&1
                             and table[x]!=table[x^(1<<i)]),F(0)))
    spectral_influences=[4*var[i]*pivotal[i] for i in range(n)]
    for i in range(n):
        assert spectral_influences[i]==sum(spectral[s] for s in range(N) if s>>i&1)
    if all(q==F(1,2) for q in p):
        assert spectral==[F(w*w,N*N) for w in W]
    return {'n':n,'biases':p,'walsh':W,'centered_coefficients':b,
            'spectrum':spectral,'pivotal_probabilities':pivotal,
            'spectral_influences':spectral_influences}

def restrict(table,biases,mask,z):
    n=validate(table)
    if not 0<=mask<1<<n: raise ValueError('Invalid block')
    A=[i for i in range(n) if mask>>i&1]
    B=[i for i in range(n) if not mask>>i&1]
    if not 0<=z<1<<len(A): raise ValueError('Invalid assignment')
    child=[]
    for y in range(1<<len(B)):
        x=sum(((z>>j)&1)<<i for j,i in enumerate(A))+sum(((y>>j)&1)<<i for j,i in enumerate(B))
        child.append(table[x])
    return tuple(child),tuple(biases[i] for i in B)
