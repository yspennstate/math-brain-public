from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
exec(compile((R/'code/reconstruct.py').read_text(encoding='utf-8').split('g=(1,-1')[0],str(R/'code/reconstruct.py'),'exec'))
old=R.parent/'20261023T014805Z-account03-A047-boundary-search/code/check.py'
H={'__file__':str(old)};exec(compile(old.read_text(encoding='utf-8').split('cases=')[0],str(old),'exec'),H)
kl=H['kl'];add=H['add'];scale=H['scale'];bounds=H['bounds']
def outer2(t,q,eps,sp,qsp):
 actual,_=outer(t,q,eps,sp);k=len(t).bit_length()-1
 u=tuple(t[z&(len(t)-1)]*sp[z>>k] for z in range(len(t)*len(sp)));mu=F(sum(u),len(u))
 qt={s|(b<<k):v*w for s,v in q.items() for b,w in qsp.items()}
 law={0:(eps+mu)**2/4,1:(eps-mu)**2/4}
 for s,v in qt.items():
  if s:law[2*s]=v/4;law[2*s+1]=v/4
 return actual,{s:v for s,v in law.items() if v}
rows=[]
for w in range(2,6):
 t=tuple(-1 if z==(1<<w)-1 else 1 for z in range(1<<w));pv=spectrum(t)
 for a in [F(1,8),F(1,6),F(1,3)]:
  qv=qref(pv,(1<<w)-1,a)
  for name,sp in [('constant',(1,)),('character',(1,-1)),('point2',(1,1,1,-1))]:
   psp=spectrum(sp);qsp=qref(psp,len(sp)-1,F(1,3))
   for eps in [-1,1]:
    actual,qq=outer2(t,qv,eps,sp,qsp);_,B=outer2(t,qv,eps,sp,psp)
    ts,ps,oldlaws,outcomes=transport(actual,qq,1)
    _,_,_,boutcomes=transport(actual,B,1);ck(outcomes==boutcomes)
    target_children=[child(t,0,b) for b in [0,1]]
    fresh=[outer2(z,qref(spectrum(z),(1<<(w-1))-1,a),eps,sp,qsp)[1] for z in target_children]
    delta=scale(add(*(add(kl(p,n),scale(kl(p,o),-1)) for p,n,o in zip(ps,fresh,oldlaws))),F(1,2))
    lo,hi=bounds(delta);ck(not delta or hi<=0)
    if w>=3:ck(hi<=-F(308,255)*a*a*F(1,1<<(2*w))/H['LN2'][0])
    p=spectrum(actual);pe=erase(p,1);be=erase(B,1)
    # Independently inspect the atomwise compensated identity on every source atom.
    for b in [0,1]:
     vchild=spectrum(target_children[b]);qchild=qref(vchild,(1<<(w-1))-1,a)
     for s,pval in ps[b].items():
      U=s>>w;V=(s>>1)&((1<<(w-1))-1)
      sr=qsp[U]/psp[U] if psp.get(U,F(0)) else F(1)
      lr=qchild[V]/vchild[V] if vchild.get(V,F(0)) else F(1)
      ck(oldlaws[b][s]==pval*sr*(be[s]/pe[s])/(2*outcomes[b]))
      ck(fresh[b][s]==pval*sr*lr)
    first=scale(add(*(kl(spectrum(z),qref(spectrum(z),(1<<(w-1))-1,a)) for z in target_children)),F(1,4))
    normalizer=kl({0:F(1,2),1:F(1,2)},{0:outcomes[0],1:outcomes[1]})
    rhs=add(first,scale(kl(pe,be),-1),normalizer)
    diag=bounds(add(delta,scale(rhs,-1)));ck(diag[0]<=0<=diag[1] and diag[1]-diag[0]<F(1,1<<90))
    rows.append({'width':w,'alpha':str(a),'spectator':name,'epsilon':eps,'signed_reset_interval':list(map(str,(lo,hi))),'same_reference_outcomes':list(map(str,outcomes)),'atomwise_compensated_identity':True})
result={'status':'PASS','cases':len(rows),'assertions':checks,'primitive_assertions':H['COUNT'],'runtime_seconds':time.perf_counter()-T0,'source_claim':'A036-NONPOSITIVE-COHERENT-SAME-PROFILE@1','scope':'unchanged source theorem independently reconstructed; finite checks plus separate analytic proof, interval overlap diagnostic only','rows':rows}
(R/'out/REVIEW.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'));print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
