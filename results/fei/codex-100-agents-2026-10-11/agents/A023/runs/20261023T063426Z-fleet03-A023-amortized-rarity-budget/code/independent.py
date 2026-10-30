"""Independent physical-character reconstruction of complete pair frontiers."""
from pathlib import Path
from fractions import Fraction as F
import itertools,json,time,hashlib
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1];START=time.perf_counter();CHECKS=0
arith=ROOT/'runs/20261023T022946Z-fleet03-A023-amortized-rarity-budget/code/independent.py'
prefix=arith.read_text(encoding='utf-8').split('rows=json.loads')[0];ns={'__file__':__file__};exec(compile(prefix,str(arith),'exec'),ns)
scatter=ns['scatter'];b=ns['b'];spectrum=ns['spectrum'];entropy=ns['entropy'];cross=ns['cross'];combo=ns['combo'];edge=ns['edge']
def ck(ok):
 global CHECKS
 assert ok
 CHECKS+=1
 assert time.perf_counter()-START<60
def seed(x,m,mask):return b(x,m)*(-1 if (x&mask).bit_count()%2 else 1)
def interval(z):
 power=z;total=F(0)
 for j in range(24):total+=power/(2*j+1);power*=z*z
 return 2*total,2*total+2*power/(49*(1-z*z))
L2,H2=interval(F(1,3))
def sign(v):
 lo=hi=F(0)
 for p,c in v.items():
  k=p.bit_length()-1;a=F(p,1<<k);l,u=interval((a-1)/(a+1));l+=k*L2;u+=k*H2
  lo+=c*(l if c>=0 else u);hi+=c*(u if c>=0 else l)
 ck(lo>0 or hi<0 or not v)
 return (1 if lo>0 else -1 if hi<0 else 0),lo,hi
rows=json.loads((RUN/'out/rows.json').read_text(encoding='utf-8'))
lookup={(r['m'],r['w'],r['mask'],tuple(sorted((int(i),a) for i,a in r['fix'].items())),r['z']):r for r in rows}
frontiers=[];cases=0
for m,w,mask in [(4,1,0),(4,3,15),(6,1,0)]:
 opts=[]
 for i in range(0,m,2):
  beta=(mask>>(i+1))&1;opts.append([{i:1-beta},{i:beta,i+1:0},{i:beta,i+1:1}])
 EB={};EZ=EM=DEPTH=MASS=NEG=F(0)
 delta=F(1,1<<m);nu={s:a for s,a in enumerate([1-3*delta/2]+[delta/2]*3)}
 for pieces in itertools.product(*opts):
  fix={i:a for piece in pieces for i,a in piece.items()};data=[i for i in range(m) if i not in fix];indices=data+[m+1,m+2];N=1<<len(indices)
  base=[seed(scatter(x,data,fix),m,mask) for x in range(1<<len(data))];pb=spectrum(base);q={s:(pb.get(s,F(0))+F(1,len(base)))/2 for s in range(len(base))}
  table=[];flips=0
  for x in range(N):
   y=scatter(x,indices,fix);core=y% (1<<m);A=(y>>(m+1))&1;B=(y>>(m+2))&1;original=seed(core,m,mask);f=original
   if A and ((not B and core==0) or (B and core==w)):f=-f
   flips+=int(f!=original);table.append(f)
  M=F(flips,N);p=spectrum(table);H=entropy(p);pd={s:F(0) for s in q};py={s:F(0) for s in nu};ref={}
  for s,a in p.items():ds=s%len(base);cs=s>>len(data);pd[ds]+=a;py[cs]+=a;ref[s]=q[ds]*nu[cs]
  C=cross(p,ref);CX=cross(pd,q);CY=cross(py,nu);K=combo((1,C),(-1,H));IS=sum(edge(base,i) for i in range(len(data)));r=len(pb).bit_length()-1;Z=4*IS-r
  influences=[edge(table,i) for i in range(len(indices))];ID=sum(influences[:len(data)]);IC=sum(influences[len(data):]);cores=[]
  for j in range(3):cores.append([a*(-1 if j and scatter(x,data,fix)==(0 if j==1 else w) else 1) for x,a in enumerate(base)])
  pi=[F(1,2),F(1,4),F(1,4)];R=F(0)
  for j in range(3):
   for k in range(j):
    prod=[a*c for a,c in zip(cores[j],cores[k])];R+=2*pi[j]*pi[k]*sum(edge(prod,i) for i in range(len(data)))
  bank=combo((1,{2:4*ID-F(m,8)-R}),(-1,C));row=lookup[(m,w,mask,tuple(sorted(fix.items())),0)]
  for name,val in [('H',H),('C',C),('CX',CX),('CY',CY),('K',K),('B',bank)]:ck(val=={int(p):F(c) for p,c in row[name].items()})
  for name,val in [('ID',ID),('IC',IC),('IS',IS),('R',R),('M',M),('Z',Z)]:ck(val==F(row[name]))
  reach=F(1,1<<len(fix));MASS+=reach;DEPTH+=reach*len(fix);EM+=reach*M;EZ+=reach*Z;EB=combo((1,EB),(reach,bank))
  if IS==0:ck(sign(bank)[0]<0);NEG+=reach
  cases+=1
 ck(MASS==1);ck(DEPTH==F(3*m,4));ck(EM==delta/2);ck(EZ==m);ck(NEG==F(1,1<<(m//2)))
 bound=F(7*m,8)-1-(9*m+F(15,4))*delta;sg,l,u=sign(combo((1,EB),(-1,{2:bound})));ck(sg>0)
 frontiers.append({'m':m,'w':w,'mask':mask,'expected_B':{str(p):str(c) for p,c in EB.items()},'expected_depth':str(DEPTH),'rare_M':str(EM),'source_Z':str(EZ),'negative_mass':str(NEG),'strict_bound_sign_ln_interval':[str(l),str(u)]})
for m in range(4,65):
 bound=F(7*m,8)-1-(9*m+F(15,4))*F(1,1<<m);ck(bound>=F(1,64));ck(9*m-F(21,4)>0)
 if m>=6:ck(bound-F(m,2)>=F(89,256))
ck(cases==45)
out={'status':'PASS','actual_boolean_leaves':cases,'complete_frontiers':len(frontiers),'scalar_integers':61,'checks':CHECKS+ns['COUNT'],'elapsed_seconds':time.perf_counter()-START,'arithmetic_source_sha256':hashlib.sha256(arith.read_bytes()).hexdigest(),'scope':'Separate character-sum/physical-event implementation by same author; independent-person review pending.'}
(RUN/'out/independent_frontiers.json').write_text(json.dumps(frontiers,indent=2)+'\n',encoding='utf-8');(RUN/'out/independent_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
