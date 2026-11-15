"""PROVED: coefficient and exact PSD replay for the independently saved SOS."""
import json
import sympy as s
from cubic_moment import construct
from exact_psd import psd
z,target=construct();cert=json.load(open('cubic_sos.json'));total=0
for block in cert['blocks']:
    w=block['weight'];basis=[]
    for b in block['basis']:basis.append(sum(s.Rational(c)*s.prod(x**k for x,k in zip(z,m))for m,c in b))
    M=s.Matrix([[s.Rational(v)for v in row]for row in block['matrix']]);assert M==M.T and psd(M)
    total+=s.prod(x**k for x,k in zip(z,w))*(s.Matrix(basis).T*M*s.Matrix(basis))[0]
assert s.Poly(s.Rational(cert['scale'])*total,z)==target
print('PROVED: all rational orthant Gram matrices PSD and every sextic coefficient matched.')
