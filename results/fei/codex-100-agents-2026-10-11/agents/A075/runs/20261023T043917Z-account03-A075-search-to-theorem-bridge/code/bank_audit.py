"""Independent bottom-up hull replay and physical inherited-credit replay."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
import json,time
import review_log as ar
ROOT=Path(__file__).resolve().parents[1]
def save(n,o):(ROOT/'out'/n).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
save('SOURCE_PHASE_AMENDMENT.json',{'frozen_before_execution':True,'domain':'same two triple orbits and6*144 source cuts; additionally allow a real original one-core-envelope prefix before pair admission, then actual pair allocation','states_added':0,'credit_rule':'unchanged rho_child+a-mean rho_child; one-core and pair phases kept separate','arithmetic':'exact prime logs and directed192-bit intervals','memory_estimate_mb':150,'maximum_runtime_seconds':180})
start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x;checks+=1
def add(a,b,c=F(1)):return ar.add(a,b,c)
def scale(a,c):return ar.scale(a,c)
def avg(a,b):return scale(add(a,b),F(1,2))
def cmp(a,b):
 d=add(a,b,F(-1))
 if not d:return 0
 lo,hi=ar.enclose(d);ck(lo>0 or hi<0);return 1 if lo>0 else -1
def pos(a):return a if cmp(a,{})>0 else {}
def unpack(d):return {int(k):F(v) for k,v in d.items() if F(v)}
def pack(d):return {str(k):str(v) for k,v in d.items() if v}
def truth(n):
 if n=='P':return (1,)
 m=int(n[1:]);return tuple(-1 if x in ({0} if n[0]=='A' else {0,1,2}) else 1 for x in range(1<<m))
def name(t):return 'P' if t==(1,) else ('A' if t.count(-1)==1 else 'L')+str((len(t)-1).bit_length())
N=['P']+['A'+str(m) for m in range(6)]+['L'+str(m) for m in range(2,7)]
def acts(n):
 if n in ['P','A0']:return []
 m=int(n[1:])
 if n[0]=='A':return [(0,'A'+str(m-1),'P')]
 return [(0,'A'+str(m-2),'A'+str(m-1))]+([(2,'L'+str(m-1),'P')] if m>=3 else [])
def rank(key):return sum(len(truth(n)) for n in key)
def args(key,side,a,b):
 out=[]
 for c in [a,b]:
  z=list(key);z[side]=c;out.append(tuple(z))
 return out
def actual_path(path,pair,Rpair,singles,A,expected):
 current=['L6','L6'];axes={j:list(range(6)) for j in pair};a=A;original=[]
 for step in path:
  j,i,b=step[:3];phase=step[3] if len(step)>3 else 'pair';side=pair.index(j);t=truth(current[side]);kids=[];newaxes=[]
  for bit in [0,1]:
   c=tuple(t[x] for x in range(len(t)) if x>>i&1==bit);ca=[x for k,x in enumerate(axes[j]) if k!=i]
   while len(c)>1:
    dummy=next((k for k in range((len(c)-1).bit_length()) if all(c[x]==c[x^(1<<k)] for x in range(len(c)))),None)
    if dummy is None:break
    c=tuple(c[x] for x in range(len(c)) if not(x>>dummy&1));ca.pop(dummy)
   kids.append(name(c));newaxes.append(ca);ck(truth(name(c))==c)
  aa=args(tuple(current),side,*kids)
  rv=[singles[side][c] for c in kids] if phase=='single' else [Rpair[z] for z in aa]
  reserve=add(a,avg(*rv),F(-1));ck(cmp(reserve,{})>=0)
  original.append([j,axes[j][i],b,phase]);a=add(rv[b],reserve);current=list(aa[b]);axes[j]=newaxes[b]
 ck(a==expected)
 return original,tuple(current)

summaries=[];source_paths=0;phase_paths=0;state_count=0;rep_rows=0
for triple in [(2,3,4),(2,3,5)]:
 tag=''.join(map(str,triple));rows=[]
 for p in sorted((ROOT/'out').glob('CERT_'+tag+'_*.json')):rows+=json.loads(p.read_text(encoding='utf-8'))
 ck(len(rows)==1728);Ss={tuple(r['types']):unpack(r['S']) for r in rows};given={tuple(r['types']):unpack(r['R']) for r in rows};R={}
 for key in sorted(Ss,key=rank):
  r=pos(scale(Ss[key],F(-1)))
  for side,n in enumerate(key):
   for i,a,b in acts(n):
    aa=args(key,side,a,b);v=avg(R[aa[0]],R[aa[1]]);rep_rows+=1
    if cmp(v,r)>0:r=v
  R[key]=r;ck(r==given[key])
 state_count+=len(R);A=scale(Ss[('L6',)*3],F(-1));ck(R[('L6',)*3]==A)
 # Positive control: a live reported root altered by one bit must fail.
 ck(add(given[('L6',)*3],{2:F(1)})!=R[('L6',)*3])
 for admitted in combinations(range(3),2):
  pair=[triple[i] for i in admitted]
  def joint(key):
   z=['L6']*3
   for side,n in zip(admitted,key):z[side]=n
   return tuple(z)
  RP={}
  for key in sorted(product(N,repeat=2),key=rank):
   r=pos(scale(Ss[joint(key)],F(-1)))
   for side,n in enumerate(key):
    for i,a,b in acts(n):
     aa=args(key,side,a,b);v=avg(RP[aa[0]],RP[aa[1]])
     if cmp(v,r)>0:r=v
   RP[key]=r
  singles=[];seeds={('L6','L6'):A};seedpaths={('L6','L6'):[]}
  for side in [0,1]:
   def key(n):return (n,'L6') if side==0 else ('L6',n)
   rs={}
   for n in sorted(N,key=lambda n:len(truth(n))):
    r=pos(scale(Ss[joint(key(n))],F(-1)))
    for i,a,b in acts(n):
     v=avg(rs[a],rs[b])
     if cmp(v,r)>0:r=v
    rs[n]=r
   singles.append(rs);incoming={'L6':A};paths={'L6':[]}
   for n in sorted(N,key=lambda n:len(truth(n)),reverse=True):
    for i,a,b in acts(n):
     reserve=add(incoming[n],avg(rs[a],rs[b]),F(-1))
     for bit,c in enumerate([a,b]):
      credit=add(rs[c],reserve)
      if c not in incoming or cmp(credit,incoming[c])<0:incoming[c]=credit;paths[c]=paths[n]+[[pair[side],i,bit,'single']]
   for n,a in incoming.items():
    k=key(n);ck(cmp(a,RP[k])>=0)
    if k not in seeds or cmp(a,seeds[k])<0:seeds[k]=a;seedpaths[k]=paths[n]
  # Reconstruct every primary actual-pair witness physically, with no credit reset.
  source=json.loads((ROOT/'out'/('CUTS_'+tag+'_'+''.join(map(str,pair))+'.json')).read_text(encoding='utf-8'))
  for cut in source:
   credit=unpack(cut['credit']);original,k=actual_path(cut['path_reduced_coordinates'],pair,RP,singles,A,credit)
   ck(k==tuple(cut['types']));ck(cmp(credit,R[joint(k)])>=0)
   ck(cut['reach']==str(F(1,1<<len(original))));source_paths+=1
  # Forward minima seeded by actual one-core phase, NOT by a fresh root optimum.
  incoming=seeds.copy();paths=seedpaths.copy()
  for key in sorted(product(N,repeat=2),key=rank,reverse=True):
   for side,n in enumerate(key):
    for i,a,b in acts(n):
     aa=args(key,side,a,b);reserve=add(incoming[key],avg(RP[aa[0]],RP[aa[1]]),F(-1));ck(cmp(reserve,{})>=0)
     for bit,arg in enumerate(aa):
      credit=add(RP[arg],reserve)
      if arg not in incoming or cmp(credit,incoming[arg])<0:incoming[arg]=credit;paths[arg]=paths[key]+[[pair[side],i,bit,'pair']]
  B={};witness=None;cuts=[]
  for key in product(N,repeat=2):
   a=incoming[key];gap=add(R[joint(key)],a,F(-1));original,k=actual_path(paths[key],pair,RP,singles,A,a);ck(k==key);phase_paths+=1
   cut={'types':key,'actual_credit':pack(a),'new_requirement':pack(R[joint(key)]),'gap':pack(gap),'original_physical_path':original,'true_reach':str(F(1,1<<len(original)))};cuts.append(cut)
   if cmp(gap,B)>0:B=gap;witness=cut
  summary={'triple':triple,'pair':pair,'cuts':144,'extra_old_debit_threshold':pack(B),'threshold_bounds':list(map(str,ar.enclose(B))),'witness':witness}
  summaries.append(summary);save('PHASE_CUTS_'+tag+'_'+''.join(map(str,pair))+'.json',cuts)
  save('BANK_AUDIT_PARTIAL.json',summaries);ck(time.perf_counter()-start<180)
out={'triple_states':state_count,'representative_query_rows':rep_rows,'primary_actual_physical_paths_replayed':source_paths,'one_then_two_phase_paths_replayed':phase_paths,'phase_results':summaries,'all_phase_thresholds_zero':all(not r['extra_old_debit_threshold'] for r in summaries),'checks':checks,'seconds':time.perf_counter()-start,'positive_control':'altered live root rejected','new_external_review':'PENDING','full_fei':'OPEN'}
save('BANK_AUDIT.json',out);print(json.dumps(out))
