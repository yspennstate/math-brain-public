from exact import fw,entropy,add,mul,enc,sgn,put,R
from fractions import Fraction as Q
import json,time,sys
checks=0
def ck(x):
 global checks
 assert x;checks+=1
def rank(vec):
 piv={}
 for x in vec:
  while x:
   b=x.bit_length()-1
   if b in piv:x^=piv[b]
   else:piv[b]=x;break
 return len(piv)
def stats(v,direct=False):
 N=len(v);n=N.bit_length()-1;a=[Q(w,N) for w in fw(v)];h=entropy(a);ii=sum(s.bit_count()*x*x for s,x in enumerate(a));ck(sum(x*x for x in a)==1)
 ck(ii==Q(sum(v[x]!=v[x^(1<<j)] for x in range(N) for j in range(n)),N))
 if direct:ck(a==[Q(sum(v[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)),N) for s in range(N)])
 return a,h,ii
def affine(a):
 n=len(a).bit_length()-1;support=[s for s,q in enumerate(a) if q];p=[sum(q*q for s,q in enumerate(a) if s>>i&1) for i in range(n)]
 full=rank([s^support[0] for s in support])==n
 costs=[]
 for v in range(1,1<<n):
  w=sum(q*q for s,q in enumerate(a) if (s&v).bit_count()%2);mm=min(w,1-w);costs.append(mm)
  if mm<max(p[i] for i in range(n) if v>>i&1):return False,full,costs
 return all(x<=Q(1,2) for x in p),full,costs
def path(m):
 M=1<<m;r=M-2;C=[0,1]+[(1<<(j-1))|(1<<j) for j in range(1,r)]+[1<<(r-1)]
 C[3],C[4]=C[4],C[3] # make the diagonal row's address difference weight two
 ck(len(C)==M and len(set(C))==M);ck(C[3]==12);return C,r
def restrict(v,A,z):
 n=len(v).bit_length()-1;B=[j for j in range(n) if j not in A];out=[]
 for y in range(1<<len(B)):
  x=sum(((z>>k)&1)<<j for k,j in enumerate(A))+sum(((y>>k)&1)<<j for k,j in enumerate(B));out.append(v[x])
 return out
def collision(a,i,j):
 groups={}
 for s,x in a.items():
  t=s&~((1<<i)|(1<<j));pos=((s>>i)&1)+2*((s>>j)&1);groups.setdefault(t,[Q(0)]*4)[pos]=x
 ci=cj=qq=Q(0)
 def frac(x,y):return 4*x*x*y*y/(x*x+y*y) if x or y else Q(0)
 for aa,bb,cc,dd in groups.values():
  ci+=frac(aa,bb)+frac(cc,dd);cj+=frac(aa,cc)+frac(bb,dd);q=aa*aa+bb*bb+cc*cc+dd*dd
  if q:qq+=4*((aa*bb+cc*dd)**2+(aa*cc+bb*dd)**2+(aa*dd+bb*cc)**2)/q
 return ci,cj,qq
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;C,r=path(3);M=8;n=r+3
 vals=[(-1 if ((x&((1<<r)-1))&C[x>>r]).bit_count()%2 else 1) for x in range(1<<n)]
 a,h,ii=stats(vals,True);ck(h=={2:Q(6)});ck(ii==3)
 expected={s|(v<<r):Q(-1 if (v&y).bit_count()%2 else 1,M) for y,s in enumerate(C) for v in range(M)}
 ck({s:q for s,q in enumerate(a) if q}==expected)
 ok,full,cost=affine(a);ck(ok and full);ck(collision(expected,2,3)==(0,0,Q(1,4)))
 singleton=[];pair=[]
 for j in [2,3]:
  for z in range(2):
   aa,hh,jj=stats(restrict(vals,[j],z));ck(hh==h);ck(jj==ii-Q(2,M));singleton.append((hh,jj))
 for z in range(4):
  aa,hh,jj=stats(restrict(vals,[2,3],z));ck(hh==add(h,{2:Q(-4,M)}));ck(jj==ii-Q(4,M));pair.append((hh,jj))
 seeds=[]
 for d in range(2,4):
  for mask in range(1<<(1<<d)):
   v=[1 if mask>>x&1 else -1 for x in range(1<<d)];aa,hh,jj=stats(v);ok,full,costs=affine(aa)
   if ok and full and hh:seeds.append((d,mask,v,aa,hh,jj,costs))
 if pilot:seeds=[x for x in seeds if x[0]==2 and x[1]==14]
 fixtures=[];fullroots=0
 for d,mask,v,ga,gh,gi,gcost in seeds:
  for t in ([1] if pilot else [1,2]):
   # Positive-deficit child-bank identity holds at every real K; three exact rates replay it.
   H=add(mul(gh,t),h);I=t*gi+ii
   for K in [2,4,8]:
    D=add(H,{2:-K*I});Sc=add(mul(D,-1),{2:Q(-2*K,M)});Sp=add(mul(D,-1),{2:Q(4*(1-K),M)})
    childD=add(H,{2:-K*(I-Q(2,M))});pairD=add(add(H,{2:Q(-4,M)}),{2:-K*(I-Q(4,M))})
    ck(Sc==mul(childD,-1));ck(Sp==mul(pairD,-1));ck(add(D,Sc)=={2:Q(-2*K,M)});ck(add(D,Sp)=={2:Q(4*(1-K),M)})
   # Tensor parity costs: |bias_product| <= every factor |bias|.
   distinct=set(gcost+cost+[Q(0)])
   for u in distinct:
    for w in distinct:
     z=(1-(1-2*u)*(1-2*w))/2;ck(z>=max(u,w));ck(z<=Q(1,2))
   if t==1 and (d,mask) in [(2,14),(3,254)]:
    root=[vals[x&511]*v[x>>9] for x in range(1<<(9+d))];ra,rh,ri=stats(root);ck(rh==H and ri==I)
    ck(collision({s:q for s,q in enumerate(ra) if q},2,3)==(0,0,Q(1,4)))
    for z in range(4):
     ca,ch,ci=stats(restrict(root,[2,3],z));ck(ch==add(H,{2:Q(-4,M)}));ck(ci==I-Q(4,M))
    fullroots+=1
   fixtures.append({'seed_n':d,'seed_mask':mask,'copies':t,'H':enc(H),'I':str(I),'singleton_drop':'0','pair_entropy_drop':'1/2','pair_influence':'1/2','C_i':'0','C_j':'0','C_ij':'1/4'})
   ck(time.perf_counter()-start<55)
 # Structural large-m cases, without exponentially sized truth tables.
 for m in range(3,7):
  cc,rr=path(m);MM=1<<m;ck(rank(cc)==rr)
  diffs=[(cc[i]^cc[j]) for i in range(MM) for j in range(i)]
  ck(diffs.count(4)==0 and diffs.count(8)==0 and diffs.count(12)==1)
  ck(Q(4,MM)/Q(4,MM)==1)
 out={'status':'PASS','pilot':pilot,'assertions':checks,'seed_count':len(seeds),'tensor_profiles':len(fixtures),'named_full_tensor_roots':fullroots,'path_truth_entries':len(vals),'direct_character_coefficients':len(a),'path_parities':511,'singleton_path_children':4,'pair_path_children':4,'m_structural':[3,4,5,6],'fixtures':fixtures,'elapsed_seconds':time.perf_counter()-start}
 put('PILOT.json' if pilot else 'CHECK.json',out);print(json.dumps({k:v for k,v in out.items() if k!='fixtures'}))
if __name__=='__main__':main()
