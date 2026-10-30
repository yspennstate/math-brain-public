from pathlib import Path
helper=Path(__file__).with_name('check.py')
exec(compile(helper.read_text(encoding='utf-8').split("pilot='--pilot'")[0],str(helper),'exec'))
b=tuple((-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16))
controllers=[]
for point in [0,3]:
 c=list(b);c[point]*=-1
 w=tuple(b[x//2] if x%2==0 else c[x//2] for x in range(32))
 controllers.extend([w,tuple(-x for x in w)])
@lru_cache(None)
def account(v,K):
 if len(v)==1:return Q(0),Q(0)
 v0,v1,d,q,B=split(v,0);own=int(sign(add(B,const(-K*d)))>0)
 q0,p0=account(v0,K);q1,p1=account(v1,K)
 return own*q+(q0+q1)/2,own*d+(p0+p1)/2
def subtrees(v):
 out={v}
 if len(v)>1:
  out.update(subtrees(restrict(v,0,0)));out.update(subtrees(restrict(v,0,1)))
 return out
def phi(w,h,K):
 a,Iw,_=stats(w);b,J,_=stats(h);t=(1-a)/2;r=(1-b)/2
 Qw,Pw=account(w,K);Qh,Ph=account(h,K)
 return r*Qw+t*Qh+(J*Pw+Iw*Ph-Pw*Ph)/2
@lru_cache(None)
def badq(w,h,block,K):
 v,other=(w,h) if block==0 else (h,w)
 if len(v)==1:return Q(0)
 v0,v1,d,q,B=split(v,0);a=stats(v)[0];beta=(stats(v0)[0]-stats(v1)[0])/2
 r=(1-stats(other)[0])/2;J=stats(other)[1]
 BF=add(sc(B,r),rem(r,a,beta));bad=sign(add(BF,const(-(K+9)*r*d)))>0
 own=sign(add(B,const(-K*d)))>0
 le(int(bad),int(own))
 return (r*q+J*d/2) if bad else Q(0)
@lru_cache(None)
def worst(w,h,K):
 opts=[]
 if len(w)>1:opts.append(badq(w,h,0,K)+sum(worst(restrict(w,0,j),h,K) for j in [0,1])/2)
 if len(h)>1:opts.append(badq(w,h,1,K)+sum(worst(w,restrict(h,0,j),K) for j in [0,1])/2)
 v=max(opts) if opts else Q(0);le(v,phi(w,h,K));return v
states=local_steps=active_bad=0;rows=[]
for wi,wroot in enumerate(controllers):
 for hi,hroot in enumerate(controllers):
  for K in [-5,4]:
   for w in subtrees(wroot):
    for h in subtrees(hroot):
     a,Iw,_=stats(w);b,J,_=stats(h);t=(1-a)/2;r=(1-b)/2
     Qw,Pw=account(w,K);Qh,Ph=account(h,K);value=phi(w,h,K)
     le(Q(0),Pw);le(Pw,Iw);le(Q(0),Ph);le(Ph,J);le(Q(0),value)
     for block in [0,1]:
      v,other=(w,h) if block==0 else (h,w)
      if len(v)==1:continue
      v0,v1,d,q,B=split(v,0);own=int(sign(add(B,const(-K*d)))>0)
      lifted_r=(1-stats(other)[0])/2;otherI=stats(other)[1]
      otherP=account(other,K)[1]
      avg=(phi(v0,h,K)+phi(v1,h,K))/2 if block==0 else (phi(w,v0,K)+phi(w,v1,K))/2
      debit=own*(lifted_r*q+otherI*d/2)+(1-own)*otherP*d/2
      eq(value-avg,debit);cost=badq(w,h,block,K);le(cost,debit)
      active_bad+=int(cost>0);local_steps+=1
     states+=1
     if time.monotonic()-start>60:raise TimeoutError('mixed frozen runtime cap')
   bill=worst(wroot,hroot,K)
   rows.append({'w':wi,'h':hi,'K0':K,'envelope':str(phi(wroot,hroot,K)),'worst_actual_bill':str(bill)})
out={'status':'PASS','state_pairs_counted_with_root_multiplicity':states,'local_steps':local_steps,'active_bad_steps':active_bad,'exact_assertions':checks,'distinct_sign_certificates':sign_cache.cache_info().currsize,'memoized_bellman_states':worst.cache_info().currsize,'runtime_seconds':time.monotonic()-start,'roots':rows}
(run/'out/MIXED_VALIDATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='roots'}))
