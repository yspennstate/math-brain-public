from pathlib import Path
import json,sys,hashlib
HERE=Path(__file__).resolve();R=HERE.parents[1]
OLD=R.parent/'20261023T120344Z-fleet03-A047-boundary-search/code/check.py'
exec(compile(OLD.read_text(encoding='utf-8').split("if __name__=='__main__':")[0],str(OLD),'exec'))
ROOT=R
(R/'out').mkdir(parents=True,exist_ok=True)
def entropy(p):return add(*(scale(lv(1/v),v) for v in p.values()))
def seed(r):return tuple(-1 if (x>>1) in ({0,3,5} if x&1 else {0,1,3}) else 1 for x in range(1<<(r+1)))
def tensor(r,k):
 b=seed(r);mask=len(b)-1
 return tuple(__import__('functools').reduce(lambda a,j:a*b[(x>>(j*(r+1)))&mask],range(k),1) for x in range(1<<(k*(r+1))))
def one(r,k,adaptive=False):
 a=F(1,6);d=F(1,1<<r);t=tensor(r,k);p,I0=spec(t);H0=entropy(p);q=fresh(t,a);A0=kl(p,q);V=1-(1-6*d)**(2*k);eta=F(4,5)*a*V
 ck(I0==k*(6*r-2)*d);ck(F(sum(t),len(t))==(1-6*d)**k);ck(set(p)==set(q));ck(bounds(add({2:8*I0},scale(H0,-1),scale(A0,-1)))[0]>0)
 nodes=[(t,tuple(range(k*(r+1))),F(1),a)];Sigma={};erased={};outcomes={};per=[]
 for level in range(k):
  nextnodes=[];bill={}
  for truth,coords,w,tilt in nodes:
   current=fresh(truth,tilt);ts,cc,olds,E,O=step(truth,coords,current,level*(r+1));ps=[spec(z)[0] for z in ts]
   cap=[tilt*F(mult,5)/(1-tilt+tilt*F(mult,5)) for mult in [1,9]]
   chosen=cap if adaptive else [a,a];news=[fresh(z,chosen[b]) for b,z in enumerate(ts)]
   pe=marginal(spec(truth)[0],coords.index(level*(r+1)));qe=marginal(current,coords.index(level*(r+1)))
   outs=[sum(qv*ps[b].get(s,F(0))/(2*pe[s]) for s,qv in qe.items()) for b in [0,1]]
   current_eta=F(4,5)*tilt*V;ck(outs==[(1-current_eta)/2,(1+current_eta)/2])
   sigma=scale(add(*(add(kl(ps[b],news[b]),scale(kl(ps[b],olds[b]),-1)) for b in [0,1])),F(1,2))
   ck(bounds(sigma)[1]<0 if adaptive else bounds(sigma)[0]>eta*eta/2)
   erased=add(erased,scale(E,w));outcomes=add(outcomes,scale(O,w));bill=add(bill,scale(sigma,w))
   for b in [0,1]:
    ck(set(news[b])==set(olds[b])==set(ps[b]));ck(F(sum(ts[b]),len(ts[b]))==(1-6*d)**k)
    nextnodes.append((ts[b],cc,w/2,chosen[b]))
  ck(sum(w for _,_,w,_ in nextnodes)==1);Sigma=add(Sigma,bill);nodes=nextnodes;per.append(list(map(str,bounds(bill))))
 Hf={};Af={};If=F(0)
 for truth,coords,w,tilt in nodes:
  p,ii=spec(truth);Hf=add(Hf,scale(entropy(p),w));Af=add(Af,scale(kl(p,fresh(truth,tilt)),w));If+=w*ii
 ck(If==k*(6*r-4)*d)
 ident=bounds(add(A0,Sigma,scale(erased,-1),scale(outcomes,-1),scale(Af,-1)))
 ck(ident[0]<=0<=ident[1] and ident[1]-ident[0]<F(1,1<<75))
 ck(bounds(Sigma)[1]<0 if adaptive else bounds(Sigma)[0]>k*eta*eta/2)
 if adaptive:
  S=add({2:8*If},scale(Hf,-1));M=add({2:8*I0},scale(H0,-1),scale(A0,-1));ck(min(bounds(S)[0],bounds(add(M,scale(Sigma,-1)))[0])>=8*k*d)
 row={'r':r,'k':k,'adaptive':adaptive,'dimension':k*(r+1),'I0':str(I0),'If':str(If),'variance':str(V),'complete_terminal_count':len(nodes),'per_generation_signed_reset_intervals':per,'Sigma_interval':list(map(str,bounds(Sigma))),'initial_KL_interval':list(map(str,bounds(A0))),'source_margin_interval':list(map(str,bounds(add({2:8*I0},scale(H0,-1),scale(A0,-1))))),'complete_chain_error_interval':list(map(str,ident)),'source_support_matching':True,'every_physical_outcome_retained':True}
 save(('PILOT_' if '--pilot' in sys.argv else '')+f'CASE_r{r}_k{k}_adaptive{int(adaptive)}.json',row);return row
pilot='--pilot' in sys.argv
specification={'helper_version':'A047 stage10 exactFraction coherent transport plus stage8 source helper; SHA pinned below','helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest(),'actual_Boolean_family':'tensor of k explicit equal-size three-point negative child pairs {0,1,3}/{0,3,5}','domain':[[4,1]] if pilot else [[4,1],[5,1],[4,2],[5,2]],'case_count':1 if pilot else 4,'symmetry':'none; both outcomes at every queried selector, full finite frontier','arithmetic':'Fraction Walsh/physical edges/coherent law; proved outward rational log bounds, no floating sign','memory_estimate_MB':120,'max_runtime_seconds':55,'automatic_dimension_growth':False}
specification['case_count']*=2;specification['policies']=['fixed alpha1/6','inherited-cap; branch odds multiply1/5 or9/5']
(R/('PILOT_SPEC.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(specification,indent=2),encoding='utf-8')
rows=[one(r,k,adaptive) for r,k in specification['domain'] for adaptive in [False,True]]
ck(F(512,25)-F(71,4)==F(273,100));ck(25*(1<<18)==6553600)
result={'status':'PASS','cases':len(rows),'assertions':COUNT,'physical_query_nodes':NODES,'runtime_seconds':time.perf_counter()-START,'rows':rows,'m6_certificate':{'r':24,'k':262144,'dimension':6553600,'Sigma_strict_lower':'512/25','rate8_I0':'71/4','strict_account_deficit':'273/100','method':'analytic rational bound; giant truth table NOT generated'}}
save('PILOT.json' if pilot else 'CHECK.json',result);print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
