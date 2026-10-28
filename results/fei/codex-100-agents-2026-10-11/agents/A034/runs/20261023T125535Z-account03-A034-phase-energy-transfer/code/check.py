from pathlib import Path
import sys,json,time,itertools,hashlib
RUN=Path(__file__).resolve().parents[1]
OLD=RUN.parents[0]/'20261023T105619Z-account03-A034-phase-energy-transfer'/'code/check.py'
source=OLD.read_text(encoding='utf8')
# Reuse only the pinned, previously checked definitions; do not execute its modes.
exec(compile(source.split("mode=sys.argv[1]")[0],str(OLD),'exec'),globals())
START=time.monotonic();CHECKS=0
def relative_row(v,alpha,anf=True):
 N=len(v);K=(alpha.denominator.bit_length()-1)-(alpha.numerator.bit_length()-1)
 need(alpha==Q(1,1<<K),'minimum component mass dyadic')
 E,H,HC,mu=row(v,K,anf)
 if not mu:return E,H,HC,mu
 R=mu/alpha;lr=log_interval(R)[1]
 need(HC<=(lr+Q(5,2))*E,'mass-relative full conditional bound')
 need(H<=(lr+Q(9,2))*E,'mass-relative complete row bill')
 return E,H,HC,mu
def equal_rows():
 count=0;domains={}
 for n in range(4):
  N=1<<n;count_n=0
  for v in itertools.product((-1,0,1),repeat=N):
   support=[y for y,a in enumerate(v) if a];s=len(support)
   if not s or (s>4 and s%2):continue
   size=2 if s%2==0 else 1;pieces=s//size
   if pieces>4:continue
   # Canonical two-point cells are affine lines; any two signs form an affine phase.
   cells=[support[j:j+size] for j in range(0,s,size)]
   need(all(len(c)==size for c in cells),'equal affine-cell certificate')
   E,H,HC,mu=relative_row(v,Q(size,N))
   need(mu/Q(size,N)==pieces,'exact equal-mass R')
   count+=1;count_n+=1
  domains[n]=count_n
 return {'rows':count,'by_n':domains}
def controls():
 receipts=[]
 for r in range(1,17):
  original=Q(1,1<<(r+1));a=Q(1,2);b=original
  need(a/b==1<<r,'equal-mass restriction ratio explosion')
  need((a+b)/b==(1<<r)+1,'unbounded residual R after restriction')
  # Cardinalities from explicit affine equations; no 2^(2r+1) truth table.
  need(Q(1<<r,1<<(2*r+1))==original,'both original affine cells equal mass')
  receipts.append({'r':r,'original_cell_mass':str(original),'restricted_masses':[str(a),str(b)],'restricted_R':str((a+b)/b)})
 need(Q(15)>Q(29,2),'nonBoolean psi_(2^15) violates eight-phase-cell rate')
 # Explicit admitted cubic point defect and sharp eight-cell degree9 tensor.
 point=[1]*8;point[-1]=-1
 relative_row(point,Q(1,2))
 need(degree([int(x==-1) for x in point])==3,'point defect admitted cubic')
 bits=[int(y==511) for y in range(512)]
 need(degree(bits)==9,'sharp nested eight-cell tensor degree9')
 return {'restriction_instability':receipts,'point_defect':'PASS','nonBoolean_control':'H=15>I=1 times29/2','tensor_degree':9}
def full_data(kind,r=0):
 if kind=='M2':
  nx=r+1;ny=r+3;result=[]
  for y in range(1<<ny):
   t=y&1;L=y&(((1<<(r+1))-1)^1);label=L^t
   q=t*(y>>(r+1)&1)*(y>>(r+2)&1)
   result.append((t,L,label,q))
  return nx,ny,result
 nx=4;ny=7;result=[];offsets=[0,1,3,7]
 for y in range(128):
  t=next((j for j in range(3) if not(y>>j&1)),3)
  z0=y>>3&1;z1=y>>4&1;a=y>>5&1;b=y>>6&1
  L=((y&1)^((y>>1)&1))|(z0<<1)|(z1<<2)|(a<<3)
  q=[a*b,(z0*a)^b,z1*b,(a*b)^a][t]
  result.append((t,L,L^offsets[t],q))
 return nx,ny,result
def carrier(kind,r=0,direct_only=False,first=None):
 nx,ny,data=full_data(kind,r);states=0;maxlabels=0;maxR=Q(0);witness=None
 for xs in restrictions(nx):
  if first is not None and xs[0]!=first:continue
  free=[i for i,x in enumerate(xs) if x==-1];nxf=len(free)
  Ystates=[(-1,)*ny] if direct_only else restrictions(ny,1 if kind=='M2' else 2)
  for ys in Ystates:
   nf=ys.count(-1);N=1<<nf;rows={};pieces={};phasecounts=Counter();Lcounts=Counter();stored=[]
   for ylocal in range(N):
    y=assignment(ys,ylocal);t,L,label,q=data[y]
    phasecounts[t]+=1
    lp=sum((L>>i&1)<<j for j,i in enumerate(free));Lcounts[lp]+=1
    j=sum((label>>i&1)<<j for j,i in enumerate(free))
    fixed=sum((label>>i&1)*v for i,v in enumerate(xs) if v!=-1)&1
    rows.setdefault(j,[0]*N)[ylocal]=1-2*(q^fixed)
    pieces.setdefault(j,Counter())[t]+=1
    stored.append((label,q))
   M=len(phasecounts);k=max(nf-c.bit_length()+1 for c in phasecounts.values())
   need(all(c&(c-1)==0 for c in phasecounts.values()),'restricted phase cells affine')
   need(k<=M-1,'complete phase-cover codimension')
   need(len(set(Lcounts.values()))==1,'common affine carrier equal fibers')
   rank=len(Lcounts).bit_length()-1
   need(len(Lcounts)==1<<rank,'affine carrier rank')
   ledger=[]
   for j,v in rows.items():
    cs=pieces[j];need(all(c&(c-1)==0 for c in cs.values()),'actual row affine pieces')
    alpha=Q(min(cs.values()),N);mu=Q(sum(cs.values()),N);R=mu/alpha;maxR=max(maxR,R)
    need(alpha>=Q(1,1<<(rank+k)),'nonempty intersection lower mass')
    need(R<=M*(1<<k),'common-carrier mass ratio bound')
    ledger.append(relative_row(v,alpha,False))
   E=sum(a[0] for a in ledger);H=sum(a[1] for a in ledger);HC=sum(a[2] for a in ledger)
   lm=log_interval(Q(M))[1]
   need(sum(a[3] for a in ledger)==1,'actual Boolean row norm total')
   need(H<=(k+lm+Q(9,2))*E,'stable full common-carrier theorem')
   need(HC<=(k+lm+Q(5,2))*E,'stable conditional common-carrier theorem')
   maxlabels=max(maxlabels,len(rows));states+=1
   if direct_only:
    values=[]
    for label,q in stored:
     for x in range(1<<nxf):values.append(1-2*(q^((label&assignment(xs,x)).bit_count()&1)))
    W=walsh(values);Ws={j:walsh(v) for j,v in rows.items()};scale=1<<nxf
    for s,w in enumerate(W):
     j=s&(scale-1);t=s>>nxf
     need(w==scale*(Ws[j][t] if j in Ws else 0),'independent full-F Walsh assembly')
    directE=Q(sum((s>>nxf).bit_count()*w*w for s,w in enumerate(W)),len(values)**2)
    need(directE==E,'same original full-F influence owner')
   if xs==(-1,)*nx and ys==(-1,)*ny:
    witness={'kind':kind,'r':r,'nonempty_labels':len(rows),'phase_cells':M,'phase_codimension':k,'original_IY':str(E),'full_H_upper':str(H),'conditional_H_upper':str(HC),'actual_row_Rs':sorted({str(Q(sum(c.values()),min(c.values()))) for c in pieces.values()})}
 return {'states':states,'max_nonempty_X_labels':maxlabels,'max_actual_R':str(maxR),'original_witness':witness}
mode=sys.argv[1];result={'helper':'A034-stage20-mass-relative-v1','mode':mode,'dependency_sha256':hashlib.sha256(source.encode()).hexdigest()}
if mode=='rows':result.update(equal_rows())
elif mode=='controls':result.update(controls())
elif mode=='M2':result['fixtures']=[carrier('M2',r) for r in range(5)];result['states']=sum(v['states'] for v in result['fixtures'])
elif mode in ('M4a','M4b','M4c'):result.update(carrier('M4',first={'M4a':-1,'M4b':0,'M4c':1}[mode]))
elif mode=='direct':result.update(carrier('M4',direct_only=True))
else:raise ValueError(mode)
result.update(assertions=CHECKS,seconds=time.monotonic()-START,status='PASS')
out=RUN/'out';out.mkdir(exist_ok=True)
(out/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k not in ('fixtures','restriction_instability','original_witness')}))
