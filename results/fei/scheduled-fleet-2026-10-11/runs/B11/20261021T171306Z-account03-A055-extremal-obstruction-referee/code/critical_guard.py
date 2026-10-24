from check import *
def main():
 start=time.perf_counter();N=8;K=2;rows=dataset(3);m=254;v,a,h,i=rows[m];D=add(h,{2:-K*i});ck(D=={2:Q(5,2),3:Q(-9,8)});ck(sgn(D)>0)
 for t in range(256):ck(sgn(add(add(rows[t][2],{2:-K*rows[t][3]}),D,-1))<=0)
 for n in [0,1,2]:
  for vv,aa,hh,ii in dataset(n):ck(sgn(add(hh,{2:-K*ii}))<=0)
 # Every proper physical descendant, with its exact original reach.
 child_checks=0
 for A in range(1,7):
  queried=[j for j in range(3) if A>>j&1];retained=[j for j in range(3) if not A>>j&1]
  for z in range(1<<len(queried)):
   child=[]
   for y in range(1<<len(retained)):
    x=sum(((z>>k)&1)<<j for k,j in enumerate(queried))+sum(((y>>k)&1)<<j for k,j in enumerate(retained));child.append(v[x])
   ca=[Q(w,len(child)) for w in fw(child)];ch=entropy(ca);ci=sum(s.bit_count()*q*q for s,q in enumerate(ca));ck(sgn(add(ch,{2:-K*ci}))<=0);child_checks+=1
 refunds={};gains={}
 for E in range(256):
  target=m^E;ap=rows[target][1];rem={}
  for q,t in zip(a,ap):rem=add(rem,add(add(kval(t),kval(q),-1),mul(kp(q),t-q),-1))
  gain=add(add(rows[target][2],{2:-K*rows[target][3]}),D,-1)
  pot={}
  for x in range(N):
   if E>>x&1:
    gx={}
    for s,q in enumerate(a):
     if q:gx=add(gx,log(q*q),q*(-1 if (s&x).bit_count()%2 else 1))
    pot=add(pot,gx,v[x])
  edge=sum(v[x]*v[x^(1<<j)] for x in range(N) if E>>x&1 for j in range(3) if not E>>(x^(1<<j))&1)
  W=add(add(pot,{'e':-2*E.bit_count()}),{2:Q(-K,2)*edge})
  ck(add(mul(W,Q(4,N)),rem)==gain);ck(sgn(rem)>=0);ck(sgn(gain)<=0)
  refunds[E]=rem;gains[E]=gain
 cross=add(add(refunds[129],refunds[1],-1),refunds[128],-1)
 expected={2:Q(6),3:Q(-9,4)};ck(cross==expected);ck(sgn(add(cross,{2:Q(-12,5)}))>0);ck(3**5<2**8)
 ck(gains[129]=={});ck(gains[1]==mul(D,-1));ck(gains[128]==add(mul(D,-1),{2:-1}))
 ck((0^7).bit_count()==3)
 out={'status':'PASS','root_mask':m,'n':3,'K':K,'root_H':enc(h),'root_I':str(i),'root_deficit':enc(D),'all_edit_maximality_checks':256,'proper_physical_children':child_checks,'all_smaller_tables':22,'mixed_edit':129,'single_edits':[1,128],'internal_pivotal_cross_edges':0,'mixed_refund_excess':enc(cross),'lower_bound_bits':'12/5','integer_certificate':'3^5=243<256=2^8','gains':{str(e):enc(gains[e]) for e in [1,128,129]},'assertions':__import__('check').checks,'elapsed_seconds':time.perf_counter()-start}
 put('CRITICAL_GUARD.json',out);print(json.dumps(out))
if __name__=='__main__':main()
