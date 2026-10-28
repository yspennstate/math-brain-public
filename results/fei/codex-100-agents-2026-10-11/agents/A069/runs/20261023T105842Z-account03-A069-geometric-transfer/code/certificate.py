from pathlib import Path
from fractions import Fraction as R
from itertools import product
from functools import lru_cache
from rational import fw,add,log,interval,h
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(v):
 global checks
 checks+=1;assert v,checks
 assert time.monotonic()-start<300,'frozen300s'
def marginal(v,i):
 bit=1<<i
 return [v[(s&(bit-1))|((s>>i)<<(i+1))]+v[(s&(bit-1))|((s>>i)<<(i+1))|bit] for s in range(len(v)//2)]
def child(v,i,b):
 bit=1<<i
 return [v[(s&(bit-1))|((s>>i)<<(i+1))|(b<<i)] for s in range(len(v)//2)]
def spec(v):return [R(x*x,len(v)**2) for x in fw(v)]
def influence(v,i):return R(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def cost(v,q):
 P=spec(v);ck(sum(P)==1);ck(sum(q)==1);ck(all(x>0 for x in q))
 return P,add(*[(-p,log(q[s])) for s,p in enumerate(P) if p])
@lru_cache(None)
def bounds(ex):return interval(dict(ex))
def ib(ex):return bounds(tuple(sorted(ex.items())))
def ctrl(m,theta,k):
 n=1<<m;h=1<<k;M=n//h;t=R(1,n*n)
 a=(1+3*t*theta)/4;b=5*(1-t*theta)/16;r=7*(1-t*theta)/R(32*(n-1))
 a+=(h-1)*r;b+=(h-1)*r;r*=h
 return M,a,b,r,[a,b]+[r]*(2*(M-1))
def tab(aa,bb,M,eps):
 return [((eps*((aa[y]+bb[y])//2))+(-1 if c else 1)*((aa[y]-bb[y])//2))*(-1 if c==0 and z==0 else 1) for y,z,c in product(range(len(aa)),range(M),range(2))]
def joint(ry,q):return [w*s for w in ry for s in q]
def formula(M,d,a,b,r):
 eta=R(1,M);p0=(1-d)*(1-eta)**2+d*eta*eta;p1=d*(1-eta)**2+(1-d)*eta*eta
 return add((p0,log(1+r/a)),(p1,log(1+r/b)),(eta*eta,log((1+a/r)*(1+b/r))),(2*(M-2)*eta*eta,log(2)))
core_invoice_checks=0
@lru_cache(None)
def coreB(aa,bb,rr):
 return add((R(1,2),cost(aa,rr)[1]),(R(1,2),cost(bb,rr)[1]))
def core_invoices(v,Q,C,aa,bb,rr,startbit):
 global core_invoice_checks
 B=coreB(tuple(aa),tuple(bb),tuple(rr))
 for j in range((len(aa)-1).bit_length()):
  qj=marginal(Q,startbit+j);rj=marginal(rr,j)
  cs=[cost(child(v,startbit+j,x),qj)[1] for x in (0,1)]
  bs=[coreB(tuple(child(aa,j,x)),tuple(child(bb,j,x)),tuple(rj)) for x in (0,1)]
  dc=add((1,C),*[(-R(1,2),e) for e in cs]);db=add((1,B),*[(-R(1,2),e) for e in bs])
  ck(dc==db);ck(influence(v,startbit+j)==(influence(aa,j)+influence(bb,j))/2)
  core_invoice_checks+=1

nonfactor_witness=None;profiles=0
def check_profile(aa,bb,ry,m,theta,eps,k,label):
 global profiles,nonfactor_witness
 M,a,b,r,qs=ctrl(m,theta,k);eta=R(1,M);d=R(sum(x!=y for x,y in zip(aa,bb)),len(aa));v=tab(aa,bb,M,eps);Q=joint(ry,qs)
 P,C=cost(v,Q);cp=[sum(P[y*2*M+s] for y in range(len(aa))) for s in range(2*M)]
 expected=[(1-d)*(1-eta)**2+d*eta*eta,d*(1-eta)**2+(1-d)*eta*eta]+[eta*eta]*(2*(M-1))
 ck(cp==expected);ck(influence(v,1)==eta);ck(sum(p for s,p in enumerate(P) if s&2)==eta)
 qq=marginal(Q,1);kids=[child(v,1,z) for z in (0,1)]
 cs=[cost(w,qq)[1] for w in kids]
 dc=add((1,C),*[(-R(1,2),c) for c in cs]);f=formula(M,d,a,b,r)
 ck(dc==f);ck(ib(add((1,f),(-4*eta,log(2))))[1]<0)
 py=[sum(P[y*2*M:(y+1)*2*M]) for y in range(len(aa))]
 if nonfactor_witness is None and any(P[y*2*M+s]!=py[y]*cp[s] for y in range(len(aa)) for s in range(2*M)):
  nonfactor_witness={'label':label,'m':m,'theta':str(theta),'epsilon':eps,'zero_private_prefix':k,'core_a':aa,'core_b':bb,'control_marginal':list(map(str,cp))}
 core_invoices(v,Q,C,aa,bb,ry,M.bit_length())
 core_invoices(kids[1],qq,cs[1],aa,bb,ry,M.bit_length()-1)
 profiles+=1
ry=[R(x,16) for x in (1,2,4,9)];root_profiles=interleaved_profiles=0
for ca,cb in product(range(16),repeat=2):
 aa=[1 if ca>>y&1 else -1 for y in range(4)];bb=[1 if cb>>y&1 else -1 for y in range(4)]
 pp=[(x+y)//2 for x,y in zip(aa,bb)];pq=[(x-y)//2 for x,y in zip(aa,bb)]
 ck(all(p*q==0 and p*p+q*q==1 for p,q in zip(pp,pq)))
 ck(sum(x*y for x,y in zip(fw(pp),fw(pq)))==0)
 for m,theta,eps in product((1,2),(R(0),R(1)),(-1,1)):
  for k in range(m):
   check_profile(aa,bb,ry,m,theta,eps,k,[ca,cb]);root_profiles+=1
 for j,out,theta,eps in product((0,1),(0,1),(R(0),R(1)),(-1,1)):
  ar=child(aa,j,out);br=child(bb,j,out);rr=marginal(ry,j)
  _,_,_,_,q0=ctrl(2,theta,0);Q0=joint(ry,q0);v0=tab(aa,bb,4,eps)
  qpc=marginal(marginal(Q0,1),2+j);qcp=marginal(marginal(Q0,3+j),1)
  ck(qpc==qcp);_,_,_,_,q1=ctrl(2,theta,1);ck(qpc==joint(rr,q1))
  vpc=child(child(v0,1,0),2+j,out);vcp=child(child(v0,3+j,out),1,0)
  ck(vpc==vcp==tab(ar,br,2,eps))
  check_profile(ar,br,rr,2,theta,eps,1,[ca,cb,j,out]);interleaved_profiles+=1
ck(root_profiles==3072);ck(interleaved_profiles==4096);ck(nonfactor_witness is not None)
scalar=0
for m in range(1,13):
 for theta in (R(0),R(1,4),R(1,2),R(1)):
  for k in range(m):
   M,a,b,r,_=ctrl(m,theta,k);L=R(8*(M-1),7);U=1+R(10*M,7)
   ck(L<=a/r<=U);ck(L<=b/r<=U);scalar+=1
boundary=[]
for l in (1,2,3):
 M=1<<l;eta=R(1,M);L=R(8*(M-1),7);U=1+R(10*M,7)
 V=add((1-2*eta+2*eta*eta,log(1+1/L)),(2*eta*eta,log(1+U)),(2*(M-2)*eta*eta,log(2)))
 lo,hi=ib(V);ck(hi<4*eta);boundary.append({'l':l,'upper':str(hi),'4Inf':str(4*eta)})
ck(R(4887,1280)<4);ck(scalar==312)
# Independent review of literal-only completion, with all full ghost mass.
completion=literal_queries=0;terminal_cost_nonzero=False
for m,d,sign in product(range(1,6),(0,1),(-1,1)):
 for k,exhausted in [(k,False) for k in range(1,m+1)]+[(m,True)]:
  M,a,b,r,Q=ctrl(m,R(d),k);literal=(d==0) if exhausted else (d==1)
  v=[sign*(-1 if c and literal else 1) for z,c in product(range(M),range(2))]
  _,C=cost(v,Q);ck(ib(C)[1]<=2)
  if C:terminal_cost_nonzero=True
  if literal:
   ck(influence(v,0)==1);qq=marginal(Q,0);kids=[child(v,0,x) for x in (0,1)];cs=[cost(w,qq)[1] for w in kids]
   dc=add((1,C),*[(-R(1,2),c) for c in cs]);ck(dc==log(1+a/b));ck(a/b<=R(28,15));ck(ib(dc)[1]<2)
   ck(all(all(x==w[0] for x in w) for w in kids));ck(all(ib(c)[1]<=2 for c in cs));literal_queries+=1
  else:ck(all(x==v[0] for x in v))
  completion+=1
ck(completion==80);ck(literal_queries==40);ck(terminal_cost_nonzero)
# Early c query: BOTH children have a nonconstant core, Inf_c=0.
M,a,b,r,qs=ctrl(2,R(0),1);v=[-1 if y==0 else 1 for y,z,c in product(range(2),range(M),range(2))]
Q=joint([R(1,4),R(3,4)],qs);_,C=cost(v,Q);qq=marginal(Q,0);kids=[child(v,0,x) for x in (0,1)];cs=[cost(w,qq)[1] for w in kids]
dc=add((1,C),*[(-R(1,2),c) for c in cs]);ck(influence(v,0)==0);ck(dc==log(R(68,31)));ck(68>2*31);ck(ib(dc)[0]>1)
ck(all(influence(w,1)==1 for w in kids));ck(a==R(31,96));ck(b==R(37,96));ck(r==R(14,96))
witness={'family':'a=b=chi_y; m2,theta0,after first private1; query c','table':v,'Q':list(map(str,Q)),'Inf_c':'0','child_core_influences':['1','1'],'Delta_C':'log2(68/31)>1','parent_CE':{str(p):str(c) for p,c in C.items()},'both_child_CE':[{str(p):str(c) for p,c in e.items()} for e in cs]}
(RUN/'out/EARLY_C_WITNESS.json').write_text(json.dumps(witness,indent=2)+'\n',encoding='utf-8')
# Extended theorem: actual early-u identity and conserved core invoices.
def preq(m,theta):
 N=1<<m;t=R(1,N*N);alpha=1-t*theta;out=[]
 for z,u,c in product(range(N),range(2),range(2)):
  if z:q=alpha*R(7,40*(N-1)) if u==0 else alpha*R(7,160*(N-1))
  elif c==u==0:q=t*theta
  else:q=alpha*(R(1,16) if c==u==1 else R(1,4))
  out.append(q)
 return out
def uformula(m,theta,d):
 rho=R(1,1<<m);t=rho*rho
 U0=add(((1-rho)**2,log((1+3*t*theta)/(1-t*theta))),(2*rho-t,log(5)))
 U1=add((t,log((1+3*t*theta)/(4*t*theta))),(1-t,log(R(5,4))))
 return add((1-d,U0),(d,U1))
u_identities=0
for ca,cb,m in product(range(16),range(16),(1,2)):
 aa=[1 if ca>>y&1 else -1 for y in range(4)];bb=[1 if cb>>y&1 else -1 for y in range(4)];N=1<<m;theta=R(1,512)
 v=[[aa[y],bb[y],-bb[y],-aa[y]][c+2*u]*(-1 if c==0 and z==0 else 1) for y,z,u,c in product(range(4),range(N),range(2),range(2))]
 Q=joint(ry,preq(m,theta));_,C=cost(v,Q);qu=marginal(Q,1);kids=[child(v,1,x) for x in (0,1)];cs=[cost(w,qu)[1] for w in kids]
 dc=add((1,C),*[(-R(1,2),c) for c in cs]);d=R(sum(x!=y for x,y in zip(aa,bb)),4)
 ck(dc==uformula(m,theta,d));ck(influence(v,1)==1-d)
 ck(kids==[tab(aa,bb,N,1),tab(aa,bb,N,-1)]);ck(qu==joint(ry,ctrl(m,theta,0)[4]))
 core_invoices(v,Q,C,aa,bb,ry,m+2);u_identities+=1
u_scalar=owner_flags=0
for m in range(1,13):
 t=R(1,1<<(2*m));theta=R(1,512)
 for d in (R(0),R(1,256)):
  U=uformula(m,theta,d);ck(ib(U)[1]<R(13,4));ck(R(13,4)<4*(1-d));u_scalar+=1
 p0=t/256;q0=t/512
 KL=add((p0,log(p0/q0)),(1-p0,log((1-p0)/(1-q0))))
 ck(ib(KL)[1]<p0);ck(p0<=R(1,1024));owner_flags+=1
 if m<=6:
  P0=spec([(-1 if u else 1)*(-1 if c==0 and z==0 else 1) for z,u,c in product(range(1<<m),range(2),range(2))])
  P1=spec([(-1 if c else 1)*(-1 if c==0 and z==0 else 1) for z,u,c in product(range(1<<m),range(2),range(2))])
  ds=R(1,256);Pmix=[(1-ds)*x+ds*y for x,y in zip(P0,P1)];qf=preq(m,theta);qm=preq(m,ds)
  diff=add(*[(pv,log(qm[i]/qf[i])) for i,pv in enumerate(Pmix) if pv]);ck(diff==KL)
ck(ib(h(R(1,256)))[1]<R(19,512));ck(R(19,512)<R(1,16))
owner=R(1,2)*(R(1,2)+R(63,64)-R(1,1024));ck(owner==R(1519,2048));ck(owner>R(5,8));ck(R(5,8)-R(7,12)==R(1,24))
old=RUN.parent/'20261022T224704Z-account03-A069-geometric-transfer/out/CERTIFICATE.json'
paid=json.loads(old.read_text(encoding='utf-8'));ck(R(paid['positive_core_excess_interval'][1])<R(7,12));ck(R(paid['children'][0]['source_surplus_interval'][0])>R(1,2))
ck(core_invoice_checks==21504);ck(u_identities==512)

out={'status':'PASS','assertions':checks,'root_profiles':root_profiles,'interleaved_profiles':interleaved_profiles,'all_ordered_two_bit_pairs':256,'scalar_profiles':scalar,'A070_completion_fixtures':completion,'A070_literal_queries':literal_queries,'full_stopped_terminal_CE_retained':True,'nonfactor_joint_witness':nonfactor_witness,'boundary_majorants':boundary,'large_width_majorant':'4887/1280<4','early_c_obstruction':'log2(68/31)>1 with Inf_c=0 and two nonconstant children','all_m_claim':'Analytic Boolean marginal and frozen-theta corridor, not finite extrapolation','actual_core_invoice_checks':core_invoice_checks,'early_u_identities':u_identities,'early_u_scalar_bounds':u_scalar,'frozen_owner_flag_KL_checks':owner_flags,'original_owner_capacity_lower':'1519/2048','new_same_earmark_spend':'<7/12','new_same_earmark_remainder':'>1/24','elapsed_seconds':time.monotonic()-start,'spec_sha256':hashlib.sha256((RUN/'FROZEN_CERTIFICATE_SPEC_V2.json').read_bytes()).hexdigest()}
(RUN/'out/CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('nonfactor_joint_witness','boundary_majorants')}))
