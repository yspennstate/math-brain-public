"""Independent integer spectrum versus direct ordered-resampling-pair audit."""
import itertools,json,sys,time,hashlib
from fractions import Fraction as F
from pathlib import Path
run=Path(__file__).resolve().parents[1]
mode=sys.argv[1]; assert mode in ('pilot','full')
start=time.perf_counter(); assertions=0;cases=0; digest=hashlib.sha256()
def ck(p):
 global assertions
 assert p
 assertions+=1
def done(kind,values):
 global cases
 cases+=1;digest.update((kind+':'+str(values)+'\n').encode())
 if cases%128==0 and time.perf_counter()-start>(55 if mode=='pilot' else 175): raise RuntimeError('Frozen runtime guard')
def truth(mask,n): return [1-2*((mask>>x)&1) for x in range(1<<n)]
def bits(a): return sum((v<0)<<x for x,v in enumerate(a))
def walsh(a):
 a=a[:]; step=1
 while step<len(a):
  for j in range(0,len(a),2*step):
   for i in range(j,j+step):
    x,y=a[i],a[i+step];a[i]=x+y;a[i+step]=x-y
  step*=2
 return a
def weights(n,cells):return [sum(b for c,b in cells if c&s) for s in range(1<<n)]
def wp(a,w):return sum(v*v*l for v,l in zip(walsh(a),w))
def piv(a,n):return sum(a[x]!=a[x^(1<<i)] for x in range(1<<n) for i in range(n))
def tables(n,cells,q1,q2=None):
 M=1<<n; ans=[]
 for c,b in cells:
  L=1<<c.bit_count();adj=[];always=0
  for x in range(M):
   row=0
   for y in range(M):
    if (x^y)&~c:continue
    d1=((q1>>x)^(q1>>y))&1
    if q2 is None:
     include=d1
    else:
     d2=((q2>>x)^(q2>>y))&1
     always+=d1*d2
     include=d1^d2
    if include:row|=1<<y
   adj.append(row)
  ans.append((4*b*(M//L),always,adj))
 return ans
def refund(mask,tab):
 result=0
 for scale,always,adj in tab:
  count=always
  for x,row in enumerate(adj):
   c=(row&mask).bit_count()
   count+=row.bit_count()-c if (mask>>x)&1 else c
  result+=scale*count
 return result
def edge_refund(g,q,n):
 M=1<<n
 return 2*M*sum((((g>>x)^(g>>(x^(1<<i))))&1) and (((q>>x)^(q>>(x^(1<<i))))&1) for x in range(M) for i in range(n))
def getcells(sizes):
 blocks=[];offset=0;cells=[]
 def subtree(coords):
  if len(coords)==1:return 1<<coords[0]
  k=len(coords)//2;l=subtree(coords[:k]);r=subtree(coords[k:]);cells.append((l|r,2));return l|r
 for size in sizes:
  blocks.append(subtree(list(range(offset,offset+size))));offset+=size
 c,u,v,y=blocks
 cells.extend([(u|v,2),(c|u|v,2),(c|u|v|y,2)])
 return offset,blocks,cells
def masks(n,blocks,assignment):
 c,u,v,y=blocks;a,b,d=assignment
 M=1<<n
 return sum(((x&c)==a and (x&u)==b)<<x for x in range(M)),sum(((x&c)==a and (x&v)==d)<<x for x in range(M))
def assignments(block):return [x for x in range(block+1) if x&~block==0]

# Exhaustive two-bit real-independent spectra and direct resampling comparisons.
n=2;M=4;cells=[(3,2)];w=weights(n,cells)
limit=16 if mode=='full' else 2
aa=[truth(i,n) for i in range(16)];ww=[wp(a,w) for a in aa]
for g in range(limit):
 for q in range(limit):
  R=refund(g,tables(n,cells,q))
  ck(ww[g^q]==ww[g]+ww[q]-R);ck(R>=0)
  done('pair',(g,q,R))
glimit=16 if mode=='full' else 4
qlimit=16 if mode=='full' else 2
for q1 in range(qlimit):
 for q2 in range(qlimit):
  t3=tables(n,cells,q1,q2);tp=tables(n,cells,q1);tn=tables(n,cells,q1^q2)
  R12=refund(q2,tp)
  for g in range(glimit):
   R=refund(g,t3)
   ck(ww[g^q1^q2]==ww[g]+ww[q1]+ww[q2]-R)
   ck(R==R12+refund(g,tn));ck(R>=0)
   done('triple',(g,q1,q2,R))

# All 65,536 four-bit sources, retaining an actual core coordinate.
n,blocks,cells=getcells((1,1,1,1));M=1<<n;den=M*M;w=weights(n,cells)
q1,q2=masks(n,blocks,(0,0,0));q=q1^q2
t3=tables(n,cells,q1,q2);tq=tables(n,cells,q)
W1,W2,Wq=[wp(truth(b,n),w) for b in (q1,q2,q)]
Iq=piv(truth(q,n),n)*M
Nsource=65536 if mode=='full' else 32
for g in range(Nsource):
 a=truth(g,n);f=truth(g^q,n)
 Wg,Wf=wp(a,w),wp(f,w)
 R3=refund(g,t3);R=refund(g,tq)
 Ig,If=piv(a,n)*M,piv(f,n)*M;RI=edge_refund(g,q,n)
 ck(Wf==Wg+W1+W2-R3);ck(Wf==Wg+Wq-R)
 ck(If==Ig+Iq-RI);ck(Wf<=Wg+12*Iq)
 ck(12*If-den-Wf==(12*Ig-den-Wg)+(12*Iq-Wq)+R-12*RI)
 done('source',(g,Wf,R3,R,RI))

domains=[(1,1,1,1),(2,1,1,1),(1,2,1,1),(1,1,2,1),(1,1,1,2)] if mode=='full' else [(1,1,1,1)]
fixtures=[]
for sizes in domains:
 n,blocks,cells=getcells(sizes);M=1<<n;den=M*M;w=weights(n,cells)
 ass=list(itertools.product(*(assignments(b) for b in blocks[:3])))
 if mode=='pilot':ass=ass[:1]
 for assignment in ass:
  q1,q2=masks(n,blocks,assignment);q=q1^q2
  costs=[wp(truth(b,n),w) for b in (q1,q2,q)]
  Is=[piv(truth(b,n),n)*M for b in (q1,q2,q)]
  c,a,b=[F(1,1<<k) for k in sizes[:3]];r,s,t,_=sizes
  ck(F(Is[2],den)==2*c*(s*a+t*b+r*(a+b-2*a*b)))
  ck(costs[0]<=6*Is[0]);ck(costs[1]<=6*Is[1]);ck(Is[0]+Is[1]<=2*Is[2])
  y=min(i for i in range(n) if blocks[3]&(1<<i))
  ymask=sum(bool(x&(1<<y))<<x for x in range(M))
  parity=sum((x.bit_count()%2)<<x for x in range(M))
  for g in (0,parity,q,q^ymask):
   Wg=wp(truth(g,n),w);Wf=wp(truth(g^q,n),w)
   R3=refund(g,tables(n,cells,q1,q2))
   ck(Wf==Wg+costs[0]+costs[1]-R3);ck(Wf<=Wg+12*Is[2])
   e1=[-2*z*(((q1>>x)&1)) for x,z in enumerate(truth(g,n))]
   e2=[-2*z*(((q2>>x)&1)) for x,z in enumerate(truth(g,n))]
   ei=[-2*z*(((q1&q2)>>x)&1) for x,z in enumerate(truth(g,n))]
   ck(all(f-z==a+b-2*d for f,z,a,b,d in zip(truth(g^q,n),truth(g,n),e1,e2,ei)))
   done('overlap',(sizes,assignment,g,Wf,R3))
  if assignment==ass[0]:fixtures.append({'sizes':sizes,'net_W_over_I':str(F(costs[2],Is[2]))})

# Fixed normalized-real and retained-core exact certificates.
a,b=F(12,13),F(5,13)
ck(a*a+b*b==1)
W_u=2*b*b;W_v=F(28800,42961)
ck(W_v>2*W_u);ck(28800*169-100*42961==571100)
real={'u':'(12+5x1)/13','normalized_product':'(169+120x1)/sqrt(42961)','W_u':str(W_u),'W_product':str(W_v),'comparison_gap':str(W_v-2*W_u),'integer_positive_gap':571100}
done('real',real)
witnesses=[]
if mode=='full':
 n,blocks,cells=getcells((1,1,1,1));M=16;den=256;w=weights(n,cells)
 q1,q2=masks(n,blocks,(0,0,0));q=q1^q2
 ymask=sum(bool(x&8)<<x for x in range(M))
 for g in (q,q^ymask):
  f=g^q;Wg=F(wp(truth(g,n),w),den);Wf=F(wp(truth(f,n),w),den)
  Wq=F(wp(truth(q,n),w),den);R=F(refund(g,tables(n,cells,q)),den);RI=F(edge_refund(g,q,n),den)
  Ig=F(piv(truth(g,n),n),M);Iq=F(piv(truth(q,n),n),M);If=F(piv(truth(f,n),n),M)
  ck(R<12*RI);ck(Wf==Wg+Wq-R);ck(If==Ig+Iq-RI)
  if g==q^ymask:
   ck((1+Wg,1+Wf,Wq,Ig,Iq,If,R,RI)==(F(11,2),F(3),F(4),F(5,2),F(3,2),F(1),F(13,2),F(3)))
  record={'source_truth':truth(g,n),'final_truth':truth(f,n),'Gamma_source':str(1+Wg),'Gamma_final':str(1+Wf),'W_mask':str(Wq),'I_source':str(Ig),'I_mask':str(Iq),'I_final':str(If),'R_tree':str(R),'R_influence':str(RI),'conversion_at_K12':str(R-12*RI),'source_slack_at_K12':str(12*Ig-1-Wg),'mask_bank_at_K12':str(12*Iq-Wq)}
  witnesses.append(record);done('conversion',record)
expected=57 if mode=='pilot' else 70147
ck(cases==expected)
result={'status':'PASS','helper':'A070-mask-referee-v1.1','mode':mode,'cases':cases,'exact_assertions':assertions,'seconds':time.perf_counter()-start,'certificate_sha256':digest.hexdigest(),'normalized_real':real,'conversion_witnesses':witnesses,'mask_fixtures':fixtures,'author_code_imported':False}
(run/'out'/('PILOT.json' if mode=='pilot' else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('status','mode','cases','exact_assertions','seconds')}))
