from pathlib import Path
import sys,json,time,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out';pilot='--pilot' in sys.argv
helper=R.parent/'20261023T065941Z-account03-A078-coding-and-padding/code/exact.py'
spec={'version':'A078-affine-mask-ledger4','helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),'family':'actual Boolean two-profile syndrome wrappers B=[Id|P], every partial physical shared assignment; guarded bent4/spike2 donor on coded majority5','domain':{'syndrome_dimensions':[2] if pilot else [2,3],'carriers_per_dimension':4,'profile_private_dimensions':[0,1],'extra_parity_columns':[3] if pilot else [1,2,3],'d3_extra_columns':[] if pilot else [1,3,7]},'case_count':{'restricted_states':2160 if pilot else 25920,'histories':0 if pilot else 4},'symmetry':'none for local states; each labeled function/profile/matrix/ternary assignment enumerated','arithmetic':'Fraction FWHT and edges, exact prime-log vectors with outward16-term atanh','memory_estimate_MB':160,'max_runtime_seconds':55 if pilot else 240,'automatic_dimension_escalation':False}
(O/('FROZEN_PILOT.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2),encoding='utf-8',newline='\n')
(R/'code/exact.py').write_bytes(helper.read_bytes())
from exact import Q,add,g,entropy,fwht,infl,restrict,xi,mean,scalar,nonneg,interval
from itertools import product
from functools import lru_cache
start=time.monotonic();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks
 assert time.monotonic()-start<spec['max_runtime_seconds']
def save(n,x):(O/n).write_text(json.dumps(x,indent=2),encoding='utf-8',newline='\n')
def je(x):return {str(p):str(v) for p,v in x.items()}
def delta(a,b,c):return add((1,a),(-Q(1,2),b),(-Q(1,2),c))
def image(cols,off=0):
 out=[off]
 for c in cols:out += [s^c for s in out]
 return tuple(out)
def shared_child(cols,off,j,b):return cols[:j]+cols[j+1:],off^(cols[j] if b else 0)
@lru_cache(maxsize=512)
def st(h,cols,off,v,w):
 im=image(cols,off);ss=set(im);r=len(ss).bit_length()-1;p=Q(1,len(ss));live=tuple(t for t in [0,1] if t in ss);pr=[v,w]
 f=tuple(pr[s][z] if s in [0,1] else h[s] for z in range(len(v)) for s in im)
 ff=fwht(f);H=entropy(ff);U=add(*[(p,entropy(fwht(pr[t]))) for t in live]);rr=r*p*sum((1-mean(pr[t])**2 for t in live),Q(0))
 X=xi(v,w,p) if len(live)==2 else {}
 ma=fwht(tuple(Q(sum(f[z*len(im)+s] for z in range(len(v))),len(v)) for s in range(len(im))))
 E=entropy(ma);Z=add((1,E),(1,scalar(rr+1)),*[( -p,g(mean(pr[t]))) for t in live])
 return f,ff,H,U,rr,X,Z,r,p,live
def coded_carriers(d):
 if d==2:return [tuple(1 if s<2 else 1-2*((mask>>(s-2))&1) for s in range(4)) for mask in range(4)]
 return [tuple(1 for s in range(8)),tuple(1 if s.bit_count()<=1 else -1 for s in range(8)),tuple(1 if s!=7 else -1 for s in range(8)),tuple(-1 if s&6==6 else 1 for s in range(8))]
states=shared=private=rankstable=separators=maskchecks=0;geometry={}
for d in spec['domain']['syndrome_dimensions']:
 for P in ([3] if pilot else [1,2,3] if d==2 else [1,3,7]):
  original=tuple([1<<i for i in range(d)]+[P]);N=len(original)
  for h in coded_carriers(d):
   for n in [0,1]:
    tables=[tuple(1-2*((m>>x)&1) for x in range(2**n)) for m in range(2**(2**n))]
    for v in tables:
     for w in tables:
      base=st(h,tuple(1<<i for i in range(d)),0,v,w);lift=st(h,original,0,v,w)
      ck(base[2]==lift[2]);ck(sum((infl(lift[0],i) for i in range(N+n)),Q(0))>=sum((infl(base[0],i) for i in range(d+n)),Q(0)))
      direct=tuple(v[s] if False else 0 for s in [])
      for pat in product([-1,0,1],repeat=N):
       cols=tuple(c for c,b in zip(original,pat) if b==-1);off=0
       for c,b in zip(original,pat):
        if b==1:off^=c
       f,ff,H,U,rr,X,Z,r,p,live=st(h,cols,off,v,w);states+=1
       ck(sum(a*a for a in ff)==1);ck(nonneg(Z));ck(H==add((1,U),(1,X),(1,scalar(rr)),(1,Z),(-1,scalar(1))))
       for t in live:
        indicator=tuple(Q(s==t) for s in image(cols,off));a=fwht(indicator);maskchecks+=1
        ck(sum(abs(z) for z in a)==1);ck(sum(z!=0 for z in a)==2**r)
       for j in range(len(cols)):
        shared+=1;cs=[st(h,*shared_child(cols,off,j,b),v,w) for b in [0,1]]
        DH=delta(H,cs[0][2],cs[1][2]);DU=delta(U,cs[0][3],cs[1][3]);DX=delta(X,cs[0][5],cs[1][5]);DZ=delta(Z,cs[0][6],cs[1][6]);rel=rr-(cs[0][4]+cs[1][4])/2
        ck(not DU);ck(rel>=0)
        separated=len(live)==2 and all(len(c[9])==1 for c in cs)
        if separated:separators+=1;ck(nonneg(add((-1,DX))))
        else:ck(not DX)
        ck(nonneg(add((1,scalar(rel)),(1,DZ),(-1,DH))))
        if cs[0][7]==r:
         rankstable+=1;ck(not DH);ck(cs[0][6]==Z==cs[1][6])
         ck(sorted(z*z for z in ff if z)==sorted(z*z for z in cs[0][1] if z))
        geom='rank_preserved' if cs[0][7]==r else 'separator' if separated else 'rank_dropped'
        geometry[geom]=geometry.get(geom,0)+1
       for j in range(n):
        private+=1;cs=[st(h,cols,off,restrict(v,j,b),restrict(w,j,b)) for b in [0,1]]
        ck(infl(f,len(cols)+j)==p*sum((infl([v,w][t],j) for t in live),Q(0)))
        DH=delta(H,cs[0][2],cs[1][2]);DU=delta(U,cs[0][3],cs[1][3]);DX=delta(X,cs[0][5],cs[1][5]);DZ=delta(Z,cs[0][6],cs[1][6]);rel=rr-(cs[0][4]+cs[1][4])/2
        ck(DH==add((1,DU),(1,DX),(1,scalar(rel)),(1,DZ)))
ck(states==spec['case_count']['restricted_states'])
histories=[];ledger=[];source_audit={}
if not pilot:
 h=tuple(1 if s.bit_count()<=2 else -1 for s in range(32));columns=(1,2,4,8,16,17);e=Q(1,32);I0=Q(15,8);Q0=96*I0;S=11*e;oldfirst=4*e;D0=e;B0=S-oldfirst-D0
 v=[];w=[]
 for x in range(128):
  z=x%16;y=1-2*((x>>6)&1);b=(-1)**((z&1)*((z>>1)&1)+((z>>2)&1)*((z>>3)&1))
  v.append(y*b);w.append(y*(1-2*(x%64==0)))
 v,w=tuple(v),tuple(w);orig=st(h,columns,0,v,w);base=st(h,(1,2,4,8,16),0,v,w)
 infs=[infl(orig[0],j) for j in range(13)];ck(sum(infs)==Q(2783,1024));ck(infs[5]==Q(7,16));ck(orig[2]==base[2])
 source_audit={'physical_coordinate_influences':[str(a) for a in infs],'total_influence':str(sum(infs)),'added_code_influence':str(infs[5]),'uncoded_total_influence':str(sum(infl(base[0],j) for j in range(12))),'entropy_preserved':orig[2]==base[2],'actual_affine_coset_sizes':[2,2],'parity_column':17,'Q':str(Q0),'I0':str(I0)}
 orders=[['a1','y','a2','z0','a3','c','a0','b2'],['a3','z0','a1','y','a2','a4','c','b2']]
 for first in [0,1]:
  a,b=restrict(v,4,first),restrict(w,4,first);Xo=xi(a,b,e);C=add((1,scalar(B0/e)),(-1/e,Xo))
  for policy,order in enumerate(orders):
   prefixP=[Q(0)];allcost=[Q(0)];leaves=[];admissions=[]
   def walk(cols,off,v,w,sl,pl,depth,reach,mode,Kfixed,L,Lambda):
    f,ff,H,U,rr,X,Z,r,p,live=st(h,cols,off,v,w)
    K=add((p,C),(1,X)) if mode=='live' else Kfixed
    ck(nonneg(K));ck(nonneg(Z))
    if depth==5:
     Lambda=add((1,scalar(Q0-L)),(-1,Z));ck(nonneg(add((1,Lambda),(-1,scalar(3*I0)))))
     ck(add((1,Lambda),(1,Z),(1,scalar(L)))==scalar(Q0))
     admissions.append({'reach':str(reach),'old_shared_L':str(L),'Z':je(Z),'Lambda':je(Lambda),'rank':r})
    rec={'initial_padding_answer':first,'policy':policy,'depth':depth,'reach':str(reach),'remaining_shared_labels':sl,'remaining_private_labels':pl,'columns':cols,'offset':off,'rank':r,'live_targets':live,'means':[str(mean(v)),str(mean(w))],'H':je(H),'U':je(U),'R':str(rr),'Xi':je(X),'K':je(K),'Z':je(Z),'Lambda':None if Lambda is None else je(Lambda),'mode':mode,'old_L':str(L),'full_squared_spectrum':[str(a*a) for a in ff],'core_squared_spectra':[[str(a*a) for a in fwht(t)] for t in [v,w]]}
    if depth==len(order):
     rec['terminal']=True;ledger.append(rec);leaves.append((reach,H,U,rr,K,Z,Lambda));return
    label=order[depth];rec['query']=label;rec['terminal']=False;ledger.append(rec)
    if label in sl:
     j=sl.index(label);influence=infl(f,j);allcost[0]+=reach*influence
     nextL=L
     if depth<5:
      number=sum(t in ['a1','a2','a3'] for t in order[:depth]);nextL+= [5,15,38][number]*influence
     cc=[shared_child(cols,off,j,t) for t in [0,1]];ss=[st(h,*c,v,w) for c in cc]
     sep=mode=='live' and all(len(c[9])==1 for c in ss)
     for child,childst in zip(cc,ss):
      nm='frozen' if sep else 'live' if mode=='live' and len(childst[9])==2 else 'dead' if mode=='live' else mode
      nk=K if sep else {} if nm=='dead' else Kfixed
      walk(*child,v,w,sl[:j]+sl[j+1:],pl,depth+1,reach/2,nm,nk,nextL,Lambda)
    else:
     j=pl.index(label);inf=infl(f,len(cols)+j);allcost[0]+=reach*inf
     if depth<5:prefixP[0]+=reach*inf
     for t in [0,1]:walk(cols,off,restrict(v,j,t),restrict(w,j,t),sl,pl[:j]+pl[j+1:],depth+1,reach/2,mode,Kfixed,L,Lambda)
   root=st(h,columns,0,a,b)
   walk(columns,0,a,b,['a0','a1','a2','a3','a4','c'],['z0','z1','z2','z3','b2','y'],0,Q(1),'live',{},Q(0),None)
   EH=add(*[(p,h) for p,h,u,r,k,z,l in leaves]);EU=add(*[(p,u) for p,h,u,r,k,z,l in leaves]);EK=add(*[(p,k) for p,h,u,r,k,z,l in leaves]);EZ=add(*[(p,z) for p,h,u,r,k,z,l in leaves]);EL=add(*[(p,l) for p,h,u,r,k,z,l in leaves]);ER=sum((p*r for p,h,u,r,k,z,l in leaves),Q(0))
   margin=add((1,root[3]),(-1,EU),(1,scalar(root[4]+B0+Q0+12*prefixP[0]-ER)),(-1,root[2]),(1,EH),(-1,EK),(-1,EZ),(-1,EL))
   ck(nonneg(margin));ck(nonneg(add((1,EK),(-1,scalar(B0-4*e)))));ck(nonneg(add((1,EL),(-1,scalar(3*I0)))))
   histories.append({'initial_padding_answer':first,'policy':policy,'order':order,'S':str(S),'first4e':str(oldfirst),'oldD0':str(D0),'B0':str(B0),'Q':str(Q0),'I0':str(I0),'expected_K':je(EK),'K_floor':str(B0-4*e),'expected_Z':je(EZ),'expected_Lambda':je(EL),'Lambda_floor':str(3*I0),'expected_full_terminal_H':je(EH),'expected_core_U':je(EU),'expected_R':str(ER),'prefix_private_physical_cost':str(prefixP[0]),'all_queries_physical_cost':str(allcost[0]),'margin_interval':[str(a) for a in interval(margin)],'leaves':len(leaves),'admissions':admissions})
 save('MIXED_LEDGER.json',ledger);save('HISTORIES.json',histories);save('SOURCE_INFLUENCE_AUDIT.json',source_audit)
bent=[]
for k in range(2,65,2):
 A=Q(1+2**(k//2),2);I=Q(k,2)
 if k<=8:
  b=tuple((-1)**sum(((x>>j)&1)*((x>>(j+1))&1) for j in range(0,k,2)) for x in range(2**k));ind=tuple(Q(1+t,2) for t in b)
  ck(sum(abs(t) for t in fwht(ind))==A);ck(sum((infl(b,j) for j in range(k)),Q(0))==I)
 bent.append({'k':k,'mask_fourier_l1':str(A),'mask_boolean_influence':str(I),'ratio':str(A/I)})
save('BENT_L1_OBSTRUCTION.json',bent)
result={'status':'PASS','pilot':pilot,'exact_assertions':checks,'restricted_states':states,'shared_queries':shared,'private_queries':private,'rank_preserving_queries':rankstable,'separating_queries':separators,'affine_mask_checks':maskchecks,'geometry':geometry,'histories':len(histories),'ledger_nodes':len(ledger),'runtime_seconds':time.monotonic()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
save('PILOT.json' if pilot else 'CHECK.json',result);print(json.dumps(result))
