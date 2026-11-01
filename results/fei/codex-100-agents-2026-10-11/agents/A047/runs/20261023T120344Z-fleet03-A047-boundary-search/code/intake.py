from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
exec(compile((R/'code/check.py').read_text(encoding='utf-8').split("if __name__=='__main__':")[0],str(R/'code/check.py'),'exec'))
def a046(k):
 return tuple((-1 if z&1 else 1)*(-1 if (z>>1)&63==63 else 1)*(-1 if z>>7==(1<<(k+1))-1 else 1) for z in range(1<<(8+k)))
def local(k,eps):
 t=a046(k);a=F(1,7);q=fresh(t,a);children=[restrict(t,7,b) for b in [0,1]]
 tt=activate(t,eps);new=[lift(z,fresh(z,a),eps) for z in children]
 _,_,_,out,sigma=transaction(tt,lift(t,q,eps),8,new)
 ck(out==[F(13,28),F(15,28)])
 pstar=F(1,1024);tk=4*F(1,1<<(2*k))*pstar;c=a/(1-a)
 def psi(x):return scale(lv(1+c/x),x)
 expected=add(scale(psi(tk/2),F(1,2)),scale(psi(tk),-F(1,4)),scale(psi(pstar),-F(1,4)),scale(lv(1-a*a/4),-F(1,2)))
 bb=bounds(add(sigma,scale(expected,-1)));ck(bb[0]<=0<=bb[1] and bb[1]-bb[0]<F(1,1<<80))
 ck(bounds(sigma)[0]>F(1,2048));p,_=spec(tt);ck(sum(v for s,v in p.items() if s>>8&1)==F(1,1<<(k+1)))
 return {'k':k,'epsilon':eps,'sigma_interval':list(map(str,bounds(sigma))),'outcomes':list(map(str,out)),'incoming_exact_scalar_formula':'independently reproduced','physical_query_influence':str(F(1,1<<(k+1)))}
def bank():
 k=1;tc=a046(k);pc,Ic=spec(tc);qcore=fresh(tc,F(1,8));n=len(tc).bit_length()-1
 t=tuple(1-2*((z>>1)&1) if not z&1 else tc[z>>3] if z&4 else 1 for z in range(1<<(n+3)))
 q={2:F(1,4),3:F(1,4),0:F(1,16),1:F(1,16),4:F(1,16),5:F(1,16)}
 for s,v in qcore.items():
  if s:
   for c in [0,1,4,5]:q[s<<3|c]=v/16
 p,I0=spec(t);H0=ent(p);A0=kl(p,q);M0=add({2:4*I0},scale(H0,-1),scale(A0,-1));debits={}
 def cut(n,coord):
  nonlocal debits
  ts,cc,qs,E,O=step(n['t'],n['cc'],n['q'],coord);debits=add(debits,scale(add(E,O),n['w']))
  return [node(t,cc,q,n['w']/2) for t,q in zip(ts,qs)]
 def reset(n):
  core=restrict(n['t'],0,1);eps=restrict(n['t'],0,0)[0];n['q']=lift(core,fresh(core,F(1,7)),eps)
 b=cut(node(t,tuple(range(n+3)),q,F(1)),2);leaves=[b[0]]+cut(b[1],1)
 oldK=totals(leaves)[2]
 for x in leaves[1:]:reset(x)
 sigma1=add(totals(leaves)[2],scale(oldK,-1));ck(bounds(sigma1)[1]<=bounds(scale(lv(F(7,6)),F(1,4)))[1])
 old=[]
 for x in leaves[1:]:old+=cut(x,10)
 leaves=[leaves[0]]+old;oldK=totals(leaves)[2]
 for x in old:reset(x)
 sigma2=add(totals(leaves)[2],scale(oldK,-1));ck(bounds(sigma2)[0]>F(1,4096))
 Hf,If,Kf=totals(leaves);S=add({2:4*If},scale(Hf,-1));edge=add(H0,scale(Hf,-1),{2:-4*(I0-If)})
 net=add(A0,edge,sigma1,sigma2);remaining=bounds(S)[0]-max(F(0),bounds(net)[1])-F(1,4)
 ck(remaining>=F(3,4));ck(bounds(S)[0]>=1);ck(sum(x['w'] for x in leaves)==1)
 identity=bounds(add(A0,sigma1,sigma2,scale(debits,-1),scale(Kf,-1)));ck(identity[0]<=0<=identity[1] and identity[1]-identity[0]<F(1,1<<80))
 ck(bounds(add(M0,scale(sigma1,-1),scale(sigma2,-1)))[0]>F(45,16))
 return {'k':1,'root_dimension':n+3,'first_actual_reset_interval':list(map(str,bounds(sigma1))),'second_actual_reset_interval':list(map(str,bounds(sigma2))),'full_terminal_count':len(leaves),'S_interval':list(map(str,bounds(S))),'remaining_after_same_original_debits_and_oldquarter':str(remaining),'complete_original_source_query_reset_chain':'exact query atom identities plus complete reset telescoping, interval equality diagnostic only','retained_b0_both_signs_all_four_data_children':True}
if '--bank' in sys.argv:rows=[bank()];name='INTAKE_BANK.json'
else:rows=[local(k,e) for k in [1,2] for e in [-1,1]];name='INTAKE_LOCAL.json'
ck(F(515,3)<256 and F(1,392)-F(1,512)>F(1,2048) and 8**4<2*7**4 and 7**4<2*6**4)
result={'status':'PASS','cases':len(rows),'assertions':COUNT,'physical_query_nodes':NODES,'runtime_seconds':time.perf_counter()-START,'rows':rows,'source_scope':'A046 whole-core rare-query AND actually paid SAME original rate4 embedding; separate rule from product point references'}
save(name,result);print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
