from arithmetic import Q,add,scale,log,phi,table,spectrum,influence,edge_inf,restrict,ser
from pathlib import Path
from functools import lru_cache
import json,time,sys
R=Path(__file__).resolve().parents[1]
def ce(P,Z):
 out={}
 for p,z in zip(P,Z):
  if p:assert z>0;out=add(out,log(z),-p)
 return out
def kl(P,Z):
 out=ce(P,Z)
 for p in P:out=add(out,phi(p),-1)
 return out
def probs(f):return tuple(a*a for a in spectrum(f))
def cal(P,Z,labels):
 mass={}; ref={}
 for p,z,l in zip(P,Z,labels):mass[l]=mass.get(l,Q(0))+p;ref[l]=ref.get(l,Q(0))+z
 result=tuple(z*mass[l]/ref[l] if mass[l] else Q(0) for z,l in zip(Z,labels))
 assert sum(result)==1
 pp=tuple(mass[l] for l in mass);zz=tuple(ref[l] for l in mass)
 assert kl(P,Z)==add(kl(pp,zz),kl(P,result))
 return result,kl(pp,zz)
def seed(f,t,weighted):
 n=len(f);P=probs(f);Z=tuple(Q(i+1,n*(n+1)//2) if weighted else Q(1,n) for i in range(n))
 labs=tuple(('s',i) if i<(1<<t) else ('p',) for i in range(n))
 return cal(P,Z,labs)[0]
def embed(s,t,nx):return (s&((1<<t)-1))|((s>>t)<<(t+nx))
def family(c,g,h,dims):
 nw,t,nx,ny=dims;nd=t+nx+ny;out=[]
 for x in range(1<<(nd+nw)):
  si=x&((1<<t)-1);xi=(x>>t)&((1<<nx)-1);yi=(x>>(t+nx))&((1<<ny)-1)
  out.append(g[si|(xi<<t)] if c[x>>nd] else h[si|(yi<<t)])
 return tuple(out)
def labels(dims):
 nw,t,nx,ny=dims;nd=t+nx+ny;out=[]
 for s in range(1<<(nd+nw)):
  data=s&((1<<nd)-1);xi=(data>>t)&((1<<nx)-1);yi=data>>(t+nx)
  out.append(('s',s) if not xi and not yi else ('G',) if xi and not yi else ('H',) if yi and not xi else ('zero',))
 return tuple(out)
def reference(c,g,h,rg,rh,dims,old=False):
 nw,t,nx,ny=dims;nd=t+nx+ny;P=probs(family(c,g,h,dims));labs=labels(dims)
 ca=spectrum(c);cb=spectrum(tuple(1-v for v in c));pg=probs(g);ph=probs(h);p=Q(sum(c),len(c));Z=[]
 for s,l in enumerate(labs):
  data=s&((1<<nd)-1);u=s>>nd
  if l[0]=='s':z=P[s]
  elif l[0]=='G':
   j=data&((1<<(t+nx))-1)
   z=(p*rg[j] if u==0 else Q(0)) if old and not pg[j] else ca[u]**2*rg[j]
  elif l[0]=='H':
   j=(data&((1<<t)-1))|((data>>(t+nx))<<t)
   z=((1-p)*rh[j] if u==0 else Q(0)) if old and not ph[j] else cb[u]**2*rh[j]
  else:z=Q(0)
  Z.append(z)
 assert sum(Z)==1
 assert kl(P,Z)==add(scale(kl(pg,rg),p),kl(ph,rh),1-p)
 return tuple(Z)
def lift(g,Z,i,zero=None):
 af=spectrum(g);n=len(g).bit_length()-1;out=[[],[]];E={}
 for s in range(1<<(n-1)):
  k=(s&((1<<i)-1))|((s>>i)<<(i+1));a=af[k];b=af[k|(1<<i)]
  q=a*a+b*b;r=Z[k]+Z[k|(1<<i)]
  ker=((a+b)**2/(2*q),(a-b)**2/(2*q)) if q else (zero(s) if zero else (Q(1,2),Q(1,2)))
  assert sum(ker)==1
  for j in range(2):out[j].append(r*ker[j])
  if q:
   pp=(a*a/q,b*b/q);rr=(Z[k]/r,Z[k|(1<<i)]/r)
   E=add(E,kl(pp,rr),q)
 z=tuple(sum(v,Q(0)) for v in out);assert sum(z)==1 and all(z)
 refs=tuple(tuple(v/zj for v in vals) for zj,vals in zip(z,out))
 child=tuple(restrict(g,i,b) for b in [0,1])
 assert kl(probs(g),Z)==add(add(E,kl((Q(1,2),Q(1,2)),z)),add(kl(probs(child[0]),refs[0]),kl(probs(child[1]),refs[1])),Q(1,2))
 return child,refs,E,kl((Q(1,2),Q(1,2)),z)
def children(c,g,h,rg,rh,dims,i):
 nw,t,nx,ny=dims;nd=t+nx+ny;cdims=list(dims)
 if i>=nd:
  cdims[0]-=1;cs=tuple(restrict(c,i-nd,b) for b in [0,1]);gs=(g,g);hs=(h,h);rs=(rg,rg);ss=(rh,rh)
 elif i<t:
  cdims[1]-=1;cs=(c,c);gs,rs,_,_=lift(g,rg,i);hs,ss,_,_=lift(h,rh,i)
 elif i<t+nx:
  cdims[2]-=1;cs=(c,c);gs,rs,_,_=lift(g,rg,i);hs=(h,h);ss=(rh,rh)
 else:
  cdims[3]-=1;cs=(c,c);gs=(g,g);rs=(rg,rg);hs,ss,_,_=lift(h,rh,i-nx)
 dt=cdims[1]
 for j in range(2):
  labsG=tuple(('s',k) if k<(1<<dt) else ('p',) for k in range(len(gs[j])))
  labsH=tuple(('s',k) if k<(1<<dt) else ('p',) for k in range(len(hs[j])))
  rr=cal(probs(gs[j]),rs[j],labsG)[0];hh=cal(probs(hs[j]),ss[j],labsH)[0]
  yield cs[j],gs[j],hs[j],rr,hh,tuple(cdims)
def zero_kernel(c,g,h,dims,i):
 nw,t,nx,ny=dims;nd=t+nx+ny
 if i<nd:return None
 ci=i-nd;ca=spectrum(c);cb=spectrum(tuple(1-v for v in c))
 def zero(s):
  data=s&((1<<nd)-1);u=s>>nd;xi=(data>>t)&((1<<nx)-1);yi=data>>(t+nx)
  v=ca if xi and not yi else cb if yi and not xi else None
  if v is None:return (Q(1,2),Q(1,2))
  k=(u&((1<<ci)-1))|((u>>ci)<<(ci+1));a=v[k];b=v[k|(1<<ci)];q=a*a+b*b
  return ((a+b)**2/(2*q),(a-b)**2/(2*q)) if q else (Q(1,2),Q(1,2))
 return zero
def check(c,g,h,dims,i,weighted):
 rg=seed(g,dims[1],weighted);rh=seed(h,dims[1],weighted);f=family(c,g,h,dims)
 Z=reference(c,g,h,rg,rh,dims)
 ff,refs,E,O=lift(f,Z,i,zero_kernel(c,g,h,dims,i));C={};D={}
 for j,child in enumerate(children(c,g,h,rg,rh,dims,i)):
  cc,gg,hh,rr,ss,dd=child;assert ff[j]==family(cc,gg,hh,dd)
  Znew=reference(cc,gg,hh,rr,ss,dd)
  projected,saving=cal(probs(ff[j]),refs[j],labels(dd))
  assert projected==Znew
  C=add(C,saving,Q(1,2));D=add(D,kl(probs(ff[j]),Znew),Q(1,2))
 assert kl(probs(f),Z)==add(add(add(E,O),C),D)
 return E,O,C,D
def old_boundary():
 c=(1,0);g=tuple((-1 if (x&1)^((x>>1)&1) else 1) for x in range(4));h=(-1,-1,1,1);dims=(1,1,1,1)
 rg=seed(g,1,False);rh=seed(h,1,False);f=family(c,g,h,dims);Z=reference(c,g,h,rg,rh,dims,old=True)
 ff,refs,E,O=lift(f,Z,0);record=[]
 for j,ch in enumerate(children(c,g,h,rg,rh,dims,0)):
  cc,gg,hh,rr,ss,dd=ch;new=reference(cc,gg,hh,rr,ss,dd);projected,C=cal(probs(ff[j]),refs[j],labels(dd))
  assert projected!=new;assert C=={};record.append({'projected':[str(z) for z in projected],'rebuilt':[str(z) for z in new],'inherited_KL':ser(kl(probs(ff[j]),refs[j]))})
 assert edge_inf(f,0)==Q(1,2)
 return {'controller_indicator':list(c),'G':list(g),'H':list(h),'physical_query':0,'query_influence':'1/2','parent_KL':ser(kl(probs(f),Z)),'erasure_release':ser(E),'outcome_release':ser(O),'children':record,'scope':'old zero-fiber kernel has valid root cost but is not closed under categorical-only sector reset; does not refute FEI or v2 local theorem'}
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;count=0
 controllers=[tuple((1-v)//2 for v in table(1,k)) for k in range(4)]+[(1,0,0,0),(0,1,1,1)]
 for c in controllers:
  dims=(len(c).bit_length()-1,1,1,1)
  for gc in ([6] if pilot else range(16)):
   for hc in ([12] if pilot else range(16)):
    for i in range(sum(dims)):
     for weighted in [False,True]:check(c,table(2,gc),table(2,hc),dims,i,weighted);count+=1
 boundary=old_boundary()
 result={'helper_version':'A056-compatible-history-v1','pilot':pilot,'reference_transports':count,'actual_child_reference_comparisons':2*count,'result':'ALL PASS','seconds':time.perf_counter()-start,'zero_completion_boundary':boundary}
 (R/'out'/('pilot.json' if pilot else 'checks.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
