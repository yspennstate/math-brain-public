"""Exact coefficient test for the homogeneous Phi bound on the ordered cone."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[k]='1'
import sympy as sp
import time, json

def log(s):
    print(s,flush=True)
    with open('LOG.md','a') as f:f.write('\n'+s+'\n')

def rays(n):
    r={j:sp.Matrix([n-j]*j+[-j]*(n-j)) for j in range(1,n)}
    out=[]; labels=[]
    for i in range(1,n):
        if n-2*i>=0: out.append(r[i]);labels.append((i,))
    for i in range(1,n):
      for j in range(1,n):
        if n-2*i>0 and n-2*j<0:
            out.append((2*j-n)*r[i]+(n-2*i)*r[j]);labels.append((i,j))
    return out,labels

def main():
    start=time.monotonic(); n=5
    log('## 3. Exact ordered-cone coefficient attempt (cone_certificate.py)')
    rr,labels=rays(n); z=sp.symbols('z:'+str(len(rr)))
    xx=[sp.Poly(sum(v[i]*t for v,t in zip(rr,z)),*z,domain=sp.ZZ) for i in range(n)]
    a=xx[0]; T=sum(v*v for v in xx); P=sum(v**3 for v in xx); Q=sum(v**4 for v in xx)
    K=(n*n-6*n+6)*T*T+2*n*Q
    H=K*(n*(n-1)*(T*T-Q+2*a*P-2*a*a*T)+T*T) +2*(n-3)*(n*(n-1)*a*a-T)*(n*Q*T-T**3-n*P*P)
    terms=H.terms(); neg=[(m,int(c)) for m,c in terms if c<0]
    print('rays',[(l,list(r)) for l,r in zip(labels,rr)],flush=True)
    print('terms',len(terms),'negative',len(neg),'seconds',time.monotonic()-start,flush=True)
    print('negative examples',neg[:20],flush=True)
    with open('cone_coefficients.json','w') as f:json.dump({'rays':[[int(v) for v in r] for r in rr],'labels':labels,'terms':[(m,int(c)) for m,c in terms]},f)
    if neg:log(f'Exact coefficient attempt FAILED: homogeneous Phi on all {len(rr)} cone rays has {len(neg)} negative coefficients among {len(terms)} terms. This disproves this coefficient certificate, not the inequality.')
    else:log('PROVED computational identity: all coefficients of homogeneous Phi on the generating rays are nonnegative. Cone-generation proof still to be written and checked.')

if __name__=='__main__':main()
