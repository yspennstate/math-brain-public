"""Independent actual-source class audit; complete reference inheritance and ledger."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from time import perf_counter
import importlib.util,json,hashlib,sys
R=Path(__file__).resolve().parents[1];A=R.parents[1]
helper=A/'runs/20261021T203248Z-account03-A086-joint-code-referee/code/check.py'
assert hashlib.sha256(helper.read_bytes()).hexdigest()=='48cd9de1ec443e89be969dd3eac40569c413ddbfafaa9df70e9db1ef238907bc'
sp=importlib.util.spec_from_file_location('own_rational_logs',helper);old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
START=perf_counter();checks=0
def ck(b,label):
 global checks
 checks+=1
 if not b:raise AssertionError(label)
 if perf_counter()-START>58:raise TimeoutError('frozen58sec guard')
def grid(a,m):return [(s,d,b) for s in range(2**a) for d in (0,1) for b in (0,1)]
def count(k,m):return 1 if k[1]==0 else 2**m-1
def total(Q,m):return sum((count(k,m)*v for k,v in Q.items()),F(0))
def spectrum(g):return old.spectrum(g)
def true(g,m,edited=True):
 a=(len(g)-1).bit_length();co=spectrum(g);eps=F(1,2**(a+m));P={}
 for k in grid(a,m):
  s,d,b=k
  P[k]=(co[s]-g[0]*eps)**2 if edited and d==b==0 else (eps**2 if edited else (co[s]**2 if d==b==0 else F(0)))
 ck(total(P,m)==1,'entire true spectrum normalized')
 return P
def canonical(g,m):
 a=(len(g)-1).bit_length();co=spectrum(g);eps=F(1,2**(a+m));N=sum(v!=0 for v in co);W=2*eps-N*eps*eps
 Q={k:(1-W)*co[k[0]]**2 if k[1]==k[2]==0 and co[k[0]] else eps*eps for k in grid(a,m)}
 ck(total(Q,m)==1,'entire current canonical normalized')
 return Q
def mix(Q,m,eta):
 eps=F(1,2**((len(Q)//4-1).bit_length()+m));out={k:(1-eta)*v+eta*eps/2 for k,v in Q.items()}
 ck(total(out,m)==1,'actual quarter-uniform current model')
 return out
def floor(g,m):
 a=(len(g)-1).bit_length();co=spectrum(g);eps=F(1,2**(a+m));P=true(g,m);Q={};data={};qd={}
 for s in range(2**a):
  for d in (0,1):
   q=P[s,d,0]+P[s,d,1];r=((co[s]**2 if d==0 else 0)+3*eps*eps)/(1+3*eps)
   qd[s,d]=q;data[s,d]=r
   for b in (0,1):
    Q[s,d,b]=r*P[s,d,b]/q
    ck(P[s,d,b]/Q[s,d,b]==q/r,'complete conditional selector likelihood cancellation')
 ck(total(Q,m)==1,'ACTUAL new complete floor normalized')
 return Q
def CE(P,Q,m):
 # Exact log-linear code bill, dictionary log argument -> rational coefficient.
 out=defaultdict(F)
 for k,p in P.items():
  if p and count(k,m):
   ck(Q[k]>0,'every actual true atom covered')
   out[Q[k]]-=count(k,m)*p
 return {q:v for q,v in out.items() if v}
def plus(*terms):
 out=defaultdict(F)
 for scale,term in terms:
  for q,v in term.items():out[q]+=scale*v
 return {q:v for q,v in out.items() if v}
def interval(expr):
 lo=hi=F(0)
 for q,v in expr.items():
  l,u=old.log2(q)
  lo+=v*(l if v>=0 else u);hi+=v*(u if v>=0 else l)
 return lo,hi
def div(P,Q,m):return interval(plus((1,CE(P,Q,m)),(-1,CE(P,P,m))))
def restrict(g,j,b):return old.child(g,j,b)
def inherit(g,Q,m,j):
 a=(len(g)-1).bit_length();kids=[restrict(g,j,b) for b in (0,1)];P=[true(kids[0],m),true(kids[1],m,False)];parent=true(g,m)
 raw=[{},{}]
 for k in grid(a-1,m):
  s,d,b=k;s0=old.bitmask_insert(s,j,0);s1=old.bitmask_insert(s,j,1)
  pm=parent[s0,d,b]+parent[s1,d,b];qm=Q[s0,d,b]+Q[s1,d,b]
  ck(pm==(P[0][k]+P[1][k])/2,'actual physical Fourier marginal identity')
  for child in (0,1):raw[child][k]=qm*P[child][k]/pm if pm else qm
 Z=[total(q,m) for q in raw];ck(sum(Z)==2 and min(Z)>0,'both actual inherited normalizers')
 out=[{k:v/Z[b] for k,v in raw[b].items()} for b in (0,1)]
 for q in out:ck(total(q,m)==1,'full inherited mass retained')
 return kids,P,out,Z
def literal():
 # Small fixed physical reconstruction independently checks the class representation.
 g=tuple((-1 if x%16==0 else 1)*(-1 if x//16==0 else 1) for x in range(64))
 table=tuple(g[x%64]-2*int(x==64) for x in range(128))
 for source,tt in [(g,table),(restrict(g,4,0),restrict(table,4,0)),(restrict(restrict(g,4,0),4,0),restrict(restrict(table,4,0),4,0))]:
  a=(len(source)-1).bit_length();direct=spectrum(tt);cl=true(source,0);can=canonical(source,0);fl=floor(source,0)
  for s in range(2**a):
   for b in (0,1):ck(cl[s,0,b]==direct[s+b*2**a]**2,'literal cube point restriction/class match')
  ck(total(can,0)==total(fl,0)==1,'literal full model normalization')
 return 'literal original7-bit/6-bit/5-bit child Fourier reconstructions PASS'
def rational_certificate():
 E=F(1,4096)
 ck(11+56*E+192*E*E<12,'all epsilon endpoint old chi bound')
 ck(F(1,2)+216*E<1,'all epsilon floor upper divergence')
 ck(F(3,2)*121/(1-2*E)<200,'all epsilon canonical divergence upper')
 ck((1-16*E)*(1-6*E)/(1+3*E)>F(15,16),'all epsilon binary complement gap')
 ck(F(75,512)>F(1,8),'binary KL curvature lower coefficient')
 ck(F(1,8)-200*E==F(39,512) and F(39,2048)>F(1,64),'strict positive actual conversion')
 ck(F(451,256)-F(5,4)-F(1,2)-F(1,16384)==F(191,16384),'SAME old positive bookings retained')
 # A094 arbitrary-core sharper allowance, constant then C0 coefficients.
 root=(F(45,4),F(3,2));pad=(F(7,8)*15-F(61,8),F(7,8)*4-F(3,2));src=(F(7,8)*15-F(15,2),F(7,8)*4-F(5,2))
 target=(F(11,2),F(1));booking=(F(37,8),F(1))
 ck(pad==(F(11,2),F(2)) and src==(F(45,8),F(1)),'A094 exact source/padding coefficients')
 ck(all(all(x>=y for x,y in zip(z,target)) for z in (root,pad,src)),'A094 all nonnegative C0 margin')
 ck(tuple(x-y for x,y in zip(target,booking))==(F(7,8),0),'A094 retained residual')
 # q>=3 monotonicity checked via nonnegative shifted polynomial coefficients.
 ck([39,19,1]==[3*3+13*3-9,2*3+13,1],'padding monotonic polynomial after q3')
 return {'epsilon_max':'1/4096','positive_charge':'epsilon/64<e3<epsilon/4','original_reserve_after_positive_bookings':'>191/16384','A094_all_frontier_booking':'(C0+37/8)Ig, residual>=7Ig/8','all_C0_nonnegative':'exact affine coefficients; no sampling'}
def run(m):
 g=tuple((-1 if x%16==0 else 1)*(-1 if x//16==0 else 1) for x in range(64));P0=true(g,m);Q0=canonical(g,m);C0=CE(P0,Q0,m)
 kids1,P1,Q1,Z1=inherit(g,Q0,m,4);gm=kids1[0];Qmix=mix(canonical(gm,m),m,F(1,4));Cmix=CE(P1[0],Qmix,m)
 e1=plus((F(1,2),Cmix),(-F(1,2),CE(P1[0],Q1[0],m)))
 # First floor comparison is NOT installed and its negative charge is NOT credited.
 Qfirstfloor=floor(gm,m);first=interval(plus((F(1,2),CE(P1[0],Qfirstfloor,m)),(-F(1,2),Cmix)))
 kids2,P2,Q2,Z2=inherit(gm,Qmix,m,4);gn=kids2[0];Qcan=canonical(gn,m);Ccan=CE(P2[0],Qcan,m)
 e2=plus((F(1,4),Ccan),(-F(1,4),CE(P2[0],Q2[0],m)))
 Qnew=floor(gn,m);Cnew=CE(P2[0],Qnew,m);e3=plus((F(1,4),Cnew),(-F(1,4),Ccan));ep=F(1,2**(m+4));Dfloor=div(P2[0],Qnew,m);Dcan=div(P2[0],Qcan,m)
 E1=interval(e1);E2=interval(e2);E3=interval(e3)
 ck(Dfloor[0]>ep/8 and Dfloor[1]<ep,'actual complete floor D bounds')
 chi=sum((count(k,m)*(P2[0][k]-Qcan[k])**2/Qcan[k] for k in Qcan),F(0))
 ck(F(3,2)*chi<200*ep*ep,'exact chi-square certificate for actual canonical D')
 ck(Qnew[0,0,1]/Qcan[0,0,1]!=Qnew[1,0,1]/Qcan[1,0,1],'genuine conditional NONEMPTY profile change')
 ck(E3[0]>ep/64 and E3[1]<ep/4,'actual POSITIVE same-child third conversion')
 ck(first[1]<-F(4039,32768),'separate first-child negative comparison, no refund')
 ck(max(E1[1],0)<F(5,4) and max(E2[1],0)<F(1,2),'old positive bookings kept')
 I=F(0)
 for (s,d,b),p in P0.items():
  dm=(m*2**(m-1) if m else 0) if d else 0
  I+=p*(count((s,d,b),m)*(s.bit_count()+b)+dm)
 ck(I==F(3,2)+F(m-5,2**(m+6)),'literal whole-root Fourier influence')
 original=4*I-interval(C0)[1]
 ck(original>F(451,256),'ORIGINAL root reserve, never renewed')
 remain=original-max(E1[1],0)-max(E2[1],0)-E3[1]
 ck(remain>F(191,16384),'same original bank after ALL positive bookings')
 # Independently assemble all query releases and ALL terminal bills.
 G1=plus((1,C0),(-F(1,2),CE(P1[0],Q1[0],m)),(-F(1,2),CE(P1[1],Q1[1],m)))
 G2=plus((F(1,2),Cmix),(-F(1,4),CE(P2[0],Q2[0],m)),(-F(1,4),CE(P2[1],Q2[1],m)))
 T=plus((F(1,2),CE(P1[1],Q1[1],m)),(F(1,4),CE(P2[1],Q2[1],m)),(F(1,4),Cnew))
 lhs=plus((1,G1),(1,G2),(1,T));rhs=plus((1,C0),(1,e1),(1,e2),(1,e3))
 ck(lhs==rhs,'EXACT log-linear entire release+full-terminal ledger')
 ck(interval(G1)[0]>=0 and interval(G2)[0]>=0,'actual complete query releases')
 ck(sum(count(k,m) for k in P2[0])==2**(m+5),'all current Fourier masks counted once')
 return {'m':m,'epsilon':str(ep),'first_normalizers':list(map(str,Z1)),'second_normalizers':list(map(str,Z2)),'e3_interval':list(map(str,E3)),'first_comparison_interval':list(map(str,first)),'remaining_lower':str(remain)}
def main():
 pilot='--pilot' in sys.argv;cert=rational_certificate();lit=literal();rows=[run(m) for m in ([8] if pilot else [8,9,12,32])]
 result={'status':'PASS','assertions':checks,'histories':len(rows),'comparison_cases':2*len(rows),'seconds':perf_counter()-START,'literal':lit,'certificate':cert,'rows':rows,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (R/'out').mkdir(exist_ok=True);(R/'out'/('PILOT.json' if pilot else 'EXACT_RESULTS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
if __name__=='__main__':
 try:main()
 except Exception as e:
  (R/'out').mkdir(exist_ok=True);(R/'out'/'FAILURE.json').write_text(json.dumps({'status':'FAIL_OR_INCOMPLETE','error':repr(e),'assertions':checks,'seconds':perf_counter()-START}),encoding='utf-8');raise
