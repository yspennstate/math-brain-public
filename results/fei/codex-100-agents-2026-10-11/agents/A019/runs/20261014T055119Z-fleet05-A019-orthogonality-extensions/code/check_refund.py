import json,time,sys
from pathlib import Path
from fractions import Fraction as Q
R=Path(__file__).resolve().parents[1]
spec={'helper_version':'A019-refund-net-v1','family':'same Boolean private-query core/reference family as exposure job','domain':'all one/two/three-bit cores; every private query; uniform child references; one fixed positive point mask','case_count':804,'symmetry':'none','arithmetic':'exact prime-log forms and rational log intervals from byte-pinned local exposure helper definitions only','memory_estimate_MB':100,'maximum_runtime_seconds':60}
(R/'out/REFUND_SPEC.json').write_text(json.dumps(spec,indent=2))
source=(R/'code/check_exposure.py').read_text();defs=source[source.index('def ck(x):'):source.index("transport={'positive'")]
ns={'Q':Q,'lru_cache':__import__('functools').lru_cache,'checks':0};exec(defs,ns)
fw=ns['fw'];sp=ns['spectrum'];ce=ns['ce'];add=ns['add'];gate=ns['gate'];iv=ns['interval'];start=time.monotonic();cases=positive=negative=zero=0;witnesses={}
for n in (1,2,3):
 N=1<<n
 for mask in range(1<<N):
  h=tuple(1-2*((mask>>v)&1) for v in range(N));ph=sp(h)
  for query in range(n):
   cases+=1;assert time.monotonic()-start<60
   children=[tuple(h[(u&((1<<query)-1))|(((u>>query)<<1|b)<<query)] for u in range(N//2)) for b in (0,1)]
   qchild=tuple(Q(1,N//2) for _ in range(N//2));qh=[Q(0)]*N
   for u in range(N//2):
    j=(u&((1<<query)-1))|((u>>query)<<(query+1));row=ph[j]+ph[j|(1<<query)]
    for b in (0,1):qh[j|(b<<query)]=qchild[u]*(ph[j|(b<<query)]/row if row else Q(1,2))
   root=gate(h,tuple(qh),1);ch=[gate(t,qchild,1) for t in children]
   kp=add((1,root[2]),(-1,ce(ph,ph)))
   kc=[add((1,ch[b][2]),(-1,ce(sp(children[b]),sp(children[b])))) for b in (0,1)]
   Dcore=add((Q(1,2),kc[0]),(Q(1,2),kc[1]),(-1,kp))
   deltaD=add((Q(1,2),ch[0][1]),(Q(1,2),ch[1][1]),(-1,root[1]))
   net=add((1,deltaD),(-Q(1,2),Dcore))
   if not net:zero+=1;continue
   l,u=iv(net);assert l>0 or u<0
   s='positive' if l>0 else 'negative'
   positive+=s=='positive';negative+=s=='negative'
   if s not in witnesses:
    witnesses[s]={'n':n,'core_mask':mask,'query':query,'net_prime_log':{str(p):str(v) for p,v in net.items()},'two_nonconstant_children':all(abs(sum(t))<len(t) for t in children)}
    (R/'out/REFUND_WITNESSES.json').write_text(json.dumps(witnesses,indent=2))
out={'status':'PASS','cases':cases,'positive_net_debts':positive,'negative_net_debts':negative,'zero_net_debts':zero,'seconds':time.monotonic()-start,'witnesses':witnesses,'scope':'finite exact sign census, no all-dimensional conclusion'}
(R/'out/REFUND_CHECK.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
