"""A078 all-mean Maj3 source history v2: exact Boolean certificates."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json,time,sys,hashlib
from exact import add,g,entropy,fwht,walsh,infl,restrict,xi,mean,scalar,interval,nonneg
R=Path(__file__).resolve().parents[1];O=R/'out';pilot='--pilot' in sys.argv
spec={'version':'A078-all-mean-carrier-2','family':'Maj3 carrier edited at vertices0,1 by every ordered Boolean profile pair on n0..2, every partial shared assignment; original guarded bent4/spike2 donor after first x1 with early guard policies','domain':{'private_n':[0,1] if pilot else [0,1,2],'shared_partial_assignments':27,'donor_k':4,'padding_m':2,'policies':4,'initial_x1_answers':2},'case_count':{'profile_pairs':20 if pilot else 276,'wrapper_states':540 if pilot else 7452,'shared_queries':540 if pilot else 7452,'private_queries':432 if pilot else 14256},'symmetry':'none; all ordered labeled profiles and all ternary shared restrictions','arithmetic':'Fraction Fourier spectra, exact prime-log vectors, outward rational 16-term atanh logarithms','memory_estimate_MB':120,'max_runtime_seconds':55 if pilot else 180,'dimension_escalation':False}
(O/('FROZEN_PILOT.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2),encoding='utf-8')
start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks
 if time.monotonic()-start>spec['max_runtime_seconds']:raise TimeoutError('frozen runtime cap')
def je(x):return {str(p):str(v) for p,v in x.items()}
def out(name,data):(O/name).write_text(json.dumps(data,indent=2),encoding='utf-8',newline='\n')
def shared_child(h,ed,i,b):
 hh=restrict(h,i,b);ee=[]
 for x,t in ed:
  if ((x>>i)&1)==b:ee.append(((x&((1<<i)-1))|((x>>(i+1))<<i),t))
 return hh,tuple(ee)
def point_table(h,ed,v,w):
 ee=dict(ed);p=[v,w];d=len(h).bit_length()-1
 return tuple(p[ee[x%len(h)]][x>>d] if x%len(h) in ee else h[x%len(h)] for x in range(len(h)*len(v)))
@lru_cache(maxsize=2048)
def stats(h,ed,v,w):
 d=len(h).bit_length()-1;e=Q(1,len(h));p=[v,w];a=[fwht(v),fwht(w)]
 f=point_table(h,ed,v,w);ff=fwht(f);hv=[entropy(a[0]),entropy(a[1])]
 U=add(*[(e,hv[t]) for _,t in ed]);rr=d*e*sum((1-mean(p[t])**2 for _,t in ed),Q(0))
 xx=xi(v,w,e) if len(ed)==2 else {}
 return f,ff,entropy(ff),U,rr,xx,hv
def diff(a,b,c):return add((Q(1),a),(Q(-1,2),b),(Q(-1,2),c))
def char(v):return sum(x!=0 for x in fwht(v))==1
def shared_kind(h,ed,i):
 cs=[shared_child(h,ed,i,b) for b in [0,1]]
 if any(not ee and char(hh) for hh,ee in cs):return 'character',Q(0)
 if len(h)==2 and len(ed)==2:return 'last_separator',Q(0)
 ee=dict(ed)
 floor=Q(sum(x not in ee and (x^(1<<i)) not in ee and h[x]!=h[x^(1<<i)] for x in range(len(h))),len(h))
 ck(floor>=Q(1,4));return 'fixed_carrier_edge',floor

h0=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
carrier_states=[]
for pat in product([-1,0,1],repeat=3):
 h=h0;ed=((0,0),(1,1))
 for i in reversed(range(3)):
  if pat[i]!=-1:h,ed=shared_child(h,ed,i,pat[i])
 carrier_states.append((pat,h,ed))
certificate=[]
for pat,h,ed in carrier_states:
 for i in range(len(h).bit_length()-1):
  kind,floor=shared_kind(h,ed,i);certificate.append({'assignment':pat,'carrier':h,'edits':ed,'query':i,'kind':kind,'floor':str(floor)})
ck(len(certificate)==27);out('CARRIER_CLASSIFICATION.json',certificate)
roots=states=shq=prq=nonzero_means=0;kind_counts={}
for n in spec['domain']['private_n']:
 tables=[tuple(1-2*((mask>>x)&1) for x in range(2**n)) for mask in range(2**(2**n))]
 for v in tables:
  for w in tables:
   roots+=1
   for pat,h,ed in carrier_states:
    states+=1;f,ff,H,U,rr,X,hv=stats(h,ed,v,w);d=len(h).bit_length()-1;e=Q(1,len(h))
    ck(sum(a*a for a in ff)==1)
    if states<=40:ck(ff==walsh(f))
    if len(ed)==2:
     ck(nonneg(add((Q(1),X),(Q(1),scalar(4*e)))));ck(nonneg(add((Q(-1),X))))
    for i in range(d):
     shq+=1;kind,floor=shared_kind(h,ed,i);kind_counts[kind]=kind_counts.get(kind,0)+1
     children=[]
     for b in [0,1]:
      hh,ee=shared_child(h,ed,i,b);children.append((hh,ee,stats(hh,ee,v,w)))
     D=diff(H,children[0][2][2],children[1][2][2]);j=infl(f,i)
     release=rr-(children[0][2][4]+children[1][2][4])/2
     ck(release==e*sum((1-mean([v,w][t])**2 for _,t in ed),Q(0)))
     ck(not diff(U,children[0][2][3],children[1][2][3]))
     bound=10*j if kind=='character' else 8*j if kind=='fixed_carrier_edge' else release+6*j
     ck(nonneg(add((Q(1),scalar(bound)),(Q(-1),D))))
     ck(nonneg(add((Q(1),scalar(release+10*j)),(Q(-1),D))))
     if kind=='fixed_carrier_edge':ck(j>=floor)
     if len(ed)==2:
      K=add((Q(1),scalar(8*e)),(Q(1),X))
      if all(len(ee)==1 for hh,ee,c in children):ks=[K,K]
      else:ks=[add((Q(1),scalar(Q(8,len(hh)))),(Q(1),c[5])) if len(ee)==2 else {} for hh,ee,c in children]
      ck(not diff(K,ks[0],ks[1]))
      for kk in ks:ck(nonneg(kk))
     if len(ed)==2 and mean(v)!=0 and mean(w)!=0:nonzero_means+=1
    for i in range(n):
     prq+=1
     cc=[stats(h,ed,restrict(v,i,b),restrict(w,i,b)) for b in [0,1]]
     DH=diff(H,cc[0][2],cc[1][2]);DU=diff(U,cc[0][3],cc[1][3]);DX=diff(X,cc[0][5],cc[1][5]);j=infl(f,d+i)
     ck(j==e*sum((infl([v,w][t],i) for _,t in ed),Q(0)))
     rel=rr-(cc[0][4]+cc[1][4])/2
     ck(rel==d*e*sum((fwht([v,w][t])[1<<i]**2 for _,t in ed),Q(0)))
     ck(nonneg(add((Q(1),DU),(Q(1),DX),(Q(1),scalar(rel+12*j)),(Q(-1),DH))))
ck(roots==spec['case_count']['profile_pairs']);ck(states==spec['case_count']['wrapper_states']);ck(shq==spec['case_count']['shared_queries']);ck(prq==spec['case_count']['private_queries'])

ledger=[];histories=[]
if not pilot:
 k=4;m=2;e0=Q(1,8);S=11*e0;D0=e0;old=4*e0;B=S-D0-old
 v=[];w=[]
 for x in range(128):
  z=x%16;y=1-2*((x>>6)&1);b=(-1)**sum(((z>>i)&1)*((z>>(i+1))&1) for i in [0,2])
  v.append(y*b);w.append(y*(1-2*(x%64==0)))
 v,w=tuple(v),tuple(w)
 ck(entropy(fwht(v))==scalar(4));ck(sum((infl(v,i) for i in range(7)),Q(0))==3)
 orders=[['s1','y','s2','s0','x2','z0'],['s1','y','s0','s2','z0','x2'],['y','s1','z0','s0','s2','x2'],['z0','s2','y','s1','s0','x2']]
 for first in [0,1]:
  vv,ww=restrict(v,4,first),restrict(w,4,first)
  X0=xi(vv,ww,e0);C=add((Q(1),scalar(B/e0)),(-1/e0,X0))
  for policy,order in enumerate(orders):
   Pp=Ps=Q(0);leaves=[];tree_nodes=0
   def walk(h,ed,a,b,sl,pl,mode,Kfixed,depth,reach):
    global checks
    nonlocal_dummy=None
    f,ff,H,U,rr,X,hv=stats(h,ed,a,b);e=Q(1,len(h));d=len(sl)
    K=add((e,C),(Q(1),X)) if mode=='live' else Kfixed
    ck(nonneg(K))
    rec={'first_x1':first,'policy':policy,'depth':depth,'reach':str(reach),'shared_labels':sl,'private_labels':pl,'edits':ed,'meanV':str(mean(a)),'meanW':str(mean(b)),'H':je(H),'U':je(U),'R':str(rr),'K':je(K),'mode':mode,'full_squared_spectrum':[str(t*t) for t in ff],'core_squared_spectra':[[str(t*t) for t in fwht(a)],[str(t*t) for t in fwht(b)]]}
    if depth==len(order):
     rec['terminal']=True;ledger.append(rec);leaves.append((reach,H,U,rr,K));return
    label=order[depth];rec['query']=label;rec['terminal']=False;ledger.append(rec)
    if label in sl:
     i=sl.index(label);j=infl(f,i);cost[1]+=reach*j
     cs=[shared_child(h,ed,i,t) for t in [0,1]]
     separated=mode=='live' and all(len(ee)==1 for hh,ee in cs)
     for hh,ee in cs:
      nm='frozen' if separated else 'live' if mode=='live' and len(ee)==2 else 'dead' if mode=='live' else mode
      nk=K if separated else {} if nm=='dead' else Kfixed
      walk(hh,ee,a,b,sl[:i]+sl[i+1:],pl,nm,nk,depth+1,reach/2)
    else:
     i=pl.index(label);j=infl(f,d+i);cost[0]+=reach*j
     for t in [0,1]:walk(h,ed,restrict(a,i,t),restrict(b,i,t),sl,pl[:i]+pl[i+1:],mode,Kfixed,depth+1,reach/2)
   cost=[Q(0),Q(0)]
   root=stats(h0,((0,0),(1,1)),vv,ww)
   walk(h0,((0,0),(1,1)),vv,ww,['s0','s1','s2'],['z0','z1','z2','z3','x2','y'],'live',{},0,Q(1))
   EH=add(*[(p,h) for p,h,u,r,k in leaves]);EU=add(*[(p,u) for p,h,u,r,k in leaves]);EK=add(*[(p,k) for p,h,u,r,k in leaves]);ER=sum((p*r for p,h,u,r,k in leaves),Q(0))
   margin=add((Q(1),root[3]),(Q(-1),EU),(Q(1),scalar(root[4]+B+12*cost[0]+10*cost[1]-ER)),(Q(-1),root[2]),(Q(1),EH),(Q(-1),EK))
   ck(nonneg(margin));ck(nonneg(add((Q(1),EK),(Q(-1),scalar(B-4*e0)))))
   histories.append({'first_x1':first,'policy':policy,'order':order,'old_first_debit':str(old),'old_D0':str(D0),'original_S':str(S),'B':str(B),'minimum_guaranteed_expected_K':str(B-4*e0),'expected_K':je(EK),'full_expected_terminal_H':je(EH),'inherited_expected_terminal_U':je(EU),'expected_terminal_R':str(ER),'P_private':str(cost[0]),'P_shared':str(cost[1]),'stopped_margin_interval':[str(z) for z in interval(margin)],'leaves':len(leaves)})
 out('MIXED_LEDGER.json',ledger);out('HISTORIES.json',histories)
result={'status':'PASS','pilot':pilot,'exact_assertions':checks,'profile_pairs':roots,'wrapper_states':states,'shared_queries':shq,'private_queries':prq,'shared_classes':kind_counts,'shared_queries_with_both_nonzero_means':nonzero_means,'histories':len(histories),'ledger_nodes':len(ledger),'runtime_seconds':time.monotonic()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out('PILOT.json' if pilot else 'CHECK.json',result);print(json.dumps(result),flush=True)
