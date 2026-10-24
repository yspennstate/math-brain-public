import hashlib,itertools,json,sys,time
from fractions import Fraction as F
from pathlib import Path
run=Path(__file__).resolve().parents[1];mode=sys.argv[1];assert mode in ('pilot','full')
start=time.perf_counter();checks=0;cases=0;counts={};digest=hashlib.sha256()
def ck(p):
 global checks
 assert p
 checks+=1
def done(k,record):
 global cases
 cases+=1;counts[k]=counts.get(k,0)+1;digest.update((k+str(record)+'\n').encode())
 if cases%128==0 and time.perf_counter()-start>(55 if mode=='pilot' else 175):raise RuntimeError('Frozen runtime guard')
def fw(a):
 a=a[:];h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):x,y=a[k],a[k+h];a[k],a[k+h]=x+y,x-y
  h*=2
 return a
def vals(mask,k):return [1-2*((mask>>j)&1) for j in range(1<<k)]
def tree(ids,cells):
 if len(ids)==1:return 1<<ids[0]
 k=len(ids)//2;a=tree(ids[:k],cells);b=tree(ids[k:],cells);cells.append((a|b,2));return a|b
def layout(sizes):
 cells=[];blocks=[];ids=[];off=0
 for size in sizes:
  x=list(range(off,off+size));ids.append(x);blocks.append(tree(x,cells));off+=size
 c,u,v,y=blocks;cells.extend([(u|v,2),(c|u|v,2),(c|u|v|y,2)])
 return off,blocks,ids,cells
def weights(n,cells):return [1+sum(b for c,b in cells if c&s) for s in range(1<<n)]
def gamma(a,L):return sum(x*x*l for x,l in zip(fw(a),L))
def influences(a,n):return [sum(a[x]!=a[x^(1<<i)] for x in range(1<<n)) for i in range(n)]
def index(x,ids):return sum(((x>>b)&1)<<i for i,b in enumerate(ids))
def assignment_list(block):return [j for j in range(block+1) if j&~block==0]
def maskq(n,blocks,ass):
 c,u,v,y=blocks;a,b,d=ass
 return [(-1 if (x&c)==a and (x&u)==b else 1)*(-1 if (x&c)==a and (x&v)==d else 1) for x in range(1<<n)]
def source_edge_theta(q,n,visible):
 private=[i for i in range(n) if i not in visible];zmask=sum(1<<i for i in private)
 base=[x for x in range(1<<n) if x&zmask==0];pmax=F(0)
 for x in base:
  for i in visible:
   count=sum(q[x|z]!=q[(x|z)^(1<<i)] for z in assignment_list(zmask))
   pmax=max(pmax,F(count,1<<len(private)))
 return pmax
def basic(g,q,n,L):
 M=1<<n;f=[a*b for a,b in zip(g,q)]
 G,Q,Fg=gamma(g,L),gamma(q,L),gamma(f,L)
 ig,iq,iff=influences(g,n),influences(q,n),influences(f,n)
 ck(Fg<=G+Q-M*M);ck(Q-M*M<=12*sum(iq)*M)
 return f,G,Q,Fg,ig,iq,iff

domains=[(1,1,1,1),(2,1,1,1),(1,2,1,1),(1,1,2,1)] if mode=='full' else [(1,1,1,1)]
for sizes in domains:
 n,blocks,ids,cells=layout(sizes);M=1<<n;L=weights(n,cells);ass=list(itertools.product(*(assignment_list(b) for b in blocks[:3])))
 if mode=='pilot':ass=ass[:1]
 for assignment in ass:
  q=maskq(n,blocks,assignment)
  theta=source_edge_theta(q,n,ids[0]+ids[3]);ck(theta<=F(1,2))
  for hp in range(4):
   for hm in range(4):
    H1,H0=vals(hp,1),vals(hm,1)
    g=[(H0 if x&1 else H1)[index(x,ids[3])] for x in range(M)]
    f,G,Q,Fg,ig,iq,iff=basic(g,q,n,L)
    B=F(1);J=F(H1[0]!=H1[1],2)+F(H0[0]!=H0[1],2);D=F(sum(a!=b for a,b in zip(H1,H0)),2)
    mean=F(sum(g),M);d=0 if sizes[0]==1 else 1
    ck(F(G,M*M)==B+2*(1-mean*mean)+2*(d+1)*D)
    IY=F(sum(iff[i] for i in ids[3]),M);IZ=F(sum(iff[i] for i in ids[0]+ids[1]+ids[2]),M)
    ck(IY==J);ck(F(Fg,M*M)<=B+2*IY+(4*d+20)*IZ)
    terminals=[]
    for z in range(1<<sum(sizes[:3])):
     terminal=[f[z|(y<<sum(sizes[:3]))] for y in range(2)]
     terminals.append(F(gamma(terminal,[1,1]),4))
    ck(sum(terminals,F(0))/len(terminals)==B)
    for K in (1,7,12):
     A=max(F(12),(K+12*theta)/(1-theta))
     ck(K*sum(ig)+12*sum(iq)<=A*sum(iff))
    done('review_core1',(sizes,assignment,hp,hm,G,Fg))

if mode=='full':
 for sizes in [(1,1,1,2),(2,1,1,2),(1,2,1,2),(1,1,2,2)]:
  n,blocks,ids,cells=layout(sizes);M=1<<n;L=weights(n,cells);q=maskq(n,blocks,(0,0,0));d=0 if sizes[0]==1 else 1
  for hp in range(16):
   for hm in range(16):
    H1,H0=vals(hp,2),vals(hm,2)
    g=[(H0 if x&1 else H1)[index(x,ids[3])] for x in range(M)]
    f,G,Q,Fg,ig,iq,iff=basic(g,q,n,L)
    B=F(gamma(H1,[1,3,3,3])+gamma(H0,[1,3,3,3]),32)
    D=F(sum(a!=b for a,b in zip(H1,H0)),4);mean=F(sum(g),M)
    ck(F(G,M*M)==B+2*(1-mean*mean)+2*(d+1)*D)
    IY=F(sum(iff[i] for i in ids[3]),M);IZ=F(sum(iff[i] for i in ids[0]+ids[1]+ids[2]),M)
    ck(F(Fg,M*M)<=B+2*IY+(4*d+20)*IZ)
    actual=sum(F(gamma([f[z|(y<<sum(sizes[:3]))] for y in range(4)],[1,3,3,3]),16) for z in range(1<<sum(sizes[:3])))/(1<<sum(sizes[:3]))
    ck(actual==B);done('review_core2',(sizes,hp,hm,G,Fg))
 n,blocks,ids,cells=layout((2,1,1,1));M=1<<n;L=weights(n,cells);q=maskq(n,blocks,(0,0,0));visible=ids[0]+ids[3]
 for seed in range(256):
  h=vals(seed,3);g=[h[index(x,visible)] for x in range(M)]
  f,G,Q,Fg,ig,iq,iff=basic(g,q,n,L)
  for K in (1,7,12):ck(K*sum(ig)+12*sum(iq)<=(2*K+12)*sum(iff))
  done('review_common',(seed,G,Fg))

# Independent one-private-coordinate sources, with an unrevealed bit in each block.
for sizes in [(1,2,1,1),(1,1,2,1)]:
 n,blocks,ids,cells=layout(sizes);M=1<<n;L=weights(n,cells)
 visible=ids[0]+([ids[1][0]] if sizes[1]==2 else [ids[2][0]])+ids[3]
 ass=list(itertools.product(*(assignment_list(b) for b in blocks[:3])))
 if mode=='pilot':ass=ass[:1]
 for assignment in ass:
  q=maskq(n,blocks,assignment);theta=source_edge_theta(q,n,visible);ck(theta<=F(1,2))
  for seed in range(256 if mode=='full' else 4):
   h=vals(seed,3);g=[h[index(x,visible)] for x in range(M)]
   f,G,Q,Fg,ig,iq,iff=basic(g,q,n,L)
   for K in (1,7,12):
    A=max(F(12),(K+12*theta)/(1-theta))
    ck(K*sum(ig)+12*sum(iq)<=A*sum(iff))
    if G<=K*sum(ig)*M:ck(Fg<=A*sum(iff)*M)
   done('partial_privacy',(sizes,assignment,seed,G,Fg))

boundary=[]
for t in ([4] if mode=='pilot' else list(range(4,17))+[32,64]):
 delta=F(1,1<<t);hmean=1-2*delta
 yc=[];tree(list(range(t)),yc);S=sum(1-F(1,1<<c.bit_count()) for c,b in yc)
 WY=8*delta*S;G=F(11,2)-hmean*hmean/2+WY
 Ig=1+2*t*delta;Iq=1+t*delta;If=(3*t+1)*delta
 ck(G<=7*Ig);ck(G<=5+8*t*delta);ck(Ig+Iq-If==2-delta)
 ratio=(7*Ig+12*Iq)/If;ck(ratio>26)
 # Factorized formula for the exact complete output cost, including all joins.
 Gf=1+2*(1-(1-delta)**2*hmean**2)+2*(2*delta-delta**2)+2*(2*delta-2*delta**2)+12*delta*S
 if t in (4,5):
  n,blocks,ids,cells=layout((1,1,t,t));M=1<<n;L=weights(n,cells)
  q=maskq(n,blocks,(0,0,0));g=[];f=[]
  for x in range(M):
   h=-1 if x&blocks[3]==0 else 1
   q1=-1 if x&blocks[0]==0 and x&blocks[1]==0 else 1
   g.append(q1*h);f.append(q1*h*q[x])
  ck(F(gamma(g,L),M*M)==G);ck(F(gamma(f,L),M*M)==Gf)
  ck(F(sum(influences(g,n)),M)==Ig);ck(F(sum(influences(q,n)),M)==Iq);ck(F(sum(influences(f,n)),M)==If)
 record={'t':t,'I_source':str(Ig),'I_mask':str(Iq),'I_final':str(If),'Gamma_source':str(G),'Gamma_final':str(Gf),'ancestral_bill_over_final_I':str(ratio),'R_influence':str(2-delta),'nonconstant_terminal_core':'point mask on t independent Y bits','entropy_certificate':'H(final)<=4I(final), analytic disjoint point-mask bound'}
 boundary.append(record);done('boundary',record)

# Exact real source sqrt(2)1{x=+}, represented as integer values divided by sqrt(2).
n=3;M=8;raw=[2 if x&1==0 else 0 for x in range(M)];q=[-1 if x==1 else 1 for x in range(M)]
f=[a*b for a,b in zip(raw,q)]
ck(raw==f);ck(F(sum(a*a for a in raw),2*M)==1)
Ireal=F(sum((raw[x]-raw[x^(1<<i)])**2 for x in range(M) for i in range(n)),8*M)
Iq=F(sum(influences(q,n)),M);theta=source_edge_theta(q,n,[0]);A=max(F(1),(1+theta)/(1-theta))
ck((Ireal,Iq,theta,A)==(F(1,2),F(3,4),F(1,4),F(5,3)))
ck(Ireal+Iq>A*Ireal)
real={'source':'sqrt(2)1{x=+}','mask':'single flip at x=-,z1=z2=+','I_source':str(Ireal),'I_final':str(Ireal),'I_mask':str(Iq),'theta':str(theta),'Boolean_factor':str(A),'left_bill':str(Ireal+Iq),'right_bill':str(A*Ireal),'normalized_final':True}
done('real',real)
ck(cases==(26 if mode=='pilot' else 10384))
out={'status':'PASS','helper':'A070-partial-privacy-v1','mode':mode,'cases':cases,'counts':counts,'exact_assertions':checks,'seconds':time.perf_counter()-start,'ordered_certificate_sha256':digest.hexdigest(),'boundary_family':boundary,'real_source':real,'author_code_imported':False}
(run/'out'/('PILOT.json' if mode=='pilot' else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ('status','mode','cases','exact_assertions','seconds')}))
