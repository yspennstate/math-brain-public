"""PROVED: exact sextic certificate d^2>=3A-3/2 for zero-sum unit R^5.
Sort the entries and write U_i=sum_j(5-j if i<j else -j)z_j,
z_j>=0. Normalization divides the homogeneous identity by ||U||^6.
"""
import json
from pathlib import Path
import sympy as s
from cubic_moment import construct

def certificate():
    z,p=construct();x,b,c,y=z
    K=3*x*y*(x-y)+b*(x*x+2*x*y-2*y*y)+c*(2*x*x-2*x*y-y*y)
    remainder=s.Poly(p.as_expr()-625*K*K,z)
    assert all(v>=0 for m,v in remainder.terms())
    assert p==s.Poly(625*K*K+remainder.as_expr(),z)
    return dict(label='PROVED',square_coefficient='625',square_terms=[[list(m),str(v)]for m,v in s.Poly(K,z).terms()],nonnegative_terms=[[list(m),str(v)]for m,v in remainder.terms()])
if __name__=='__main__':
    cert=certificate();assert json.load(open('cubic_moment_certificate.json'))==cert
    print('PROVED: homogeneous sextic = 625 K(z)^2 +',len(cert['nonnegative_terms']),'nonnegative monomials on the ordered cone; d^2>=3A-3/2, including all scalar combinations alpha u+beta w.')
