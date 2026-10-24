"""Independently verify the remembered FA-1f / neighbor-refresh duality."""
from fractions import Fraction
import pathlib,json,time
root=pathlib.Path(__file__).resolve().parent
start=time.monotonic(); records=[]
for n in [3,4,5]:
 for q in [Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(3,4)]:
  p=1-q; S=range(1<<n)
  # eta and A are bit masks of infected primal sites and occupied dual sites.
  D=[[(-p/q)**((eta&A).bit_count()) for eta in S] for A in S]
  for A in S:
   for eta in S:
    primal=Fraction(0); dual=Fraction(0)
    for x in range(n):
     l=(x-1)%n;r=(x+1)%n
     if eta>>l&1 or eta>>r&1:
      rate=p if eta>>x&1 else q
      primal+=rate*(D[A][eta^(1<<x)]-D[A][eta])
     if A>>x&1:
      base=A&~((1<<l)|(1<<r))
      refreshed=Fraction(0)
      for b in [0,1]:
       for c in [0,1]:
        B=base|(b<<l)|(c<<r)
        refreshed+=(q if b else p)*(q if c else p)*D[B][eta]
      dual+=refreshed-D[A][eta]
    assert primal==dual,(n,q,A,eta,primal,dual)
  records.append({'n_cycle':n,'q':str(q),'all_pairs':4**n,'identity':'L_eta D(A,eta) = Q_A D(A,eta) exact rational PASS'})
result={'checks':records,'seconds':time.monotonic()-start,'scope':'Finite cyclic generator algebra only; no infinite-time convergence certificate.'}
(root/'dual_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
