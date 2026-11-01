from pathlib import Path
import sys,json,time
sys.dont_write_bytecode=True
import helper as h
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];start=time.perf_counter();N=0
def ck(x,msg):
 global N
 assert x,msg
 N+=1
 assert time.perf_counter()-start<60,'frozen runtime'
records=json.loads((R/'out/BLOCK_CHECK.json').read_text(encoding='utf-8'))['rows']
unique={}
for row in records:unique[json.dumps([row['essential'],row['values']])]=row
states=list(unique.values())
pilot='--pilot' in sys.argv
if pilot:states=states[:5]
def rows(k,seed,phase,padding=False):
 rho=F(1,1<<k);mu=F(5,8)**5;nu=phase*F(seed['mean']);pg=list(map(F,seed['P']));rg=list(map(F,seed['Q']))
 kp=0 if padding else k;rhoc=F(1) if padding else rho;a=rhoc*(1-nu)/2;p=rho*(1-mu)/2;ans=[]
 for t in range(len(pg)):
  for z,count in [(True,1),(False,(1<<kp)-1)]:
   if not count:continue
   for u in [0,1]:
    at0=z and t==0 and u==0;atu=z and t==0 and u==1
    pp=rhoc*rhoc*(pg[t]+(1-2*nu)*int(t==0))/4+(1-2*a)*int(atu)
    qq=rho*rhoc*(rg[t]+(1-2*mu)*int(t==0))/8+(1-2*p)*int(atu)/2+F(int(at0),2)
    ck(pp>=0 and qq>=0,'complete coincident signed coefficients')
    ans.append((count,pp,qq,at0))
 return ans,nu,a,p
out=[]
for state in states:
 for k in ([5] if pilot else [5,8,32,64]):
  for phase in [-1,1]:
   rr,nu,a,p=rows(k,state,phase);I=F(state['I']);rho=F(1,1<<k);C=h.fullcost(rr);U=h.add(h.Lq(p),h.conversion(p))
   ck(U[0]>=0 and U[1]<F(5,8),'actual SAME old U finite interval')
   seedC=tuple(map(F,state['CE_interval']))
   if nu<=F(1,2):
    dv=3*F(state['Q'][0])+3-8*F(5,8)**5+2*nu
    ck(dv>=F(971,4096),'new vacuum criterion needs NO R0>=nu squared')
    bound=h.add(h.val(3),h.eta(2*a),h.eta(1-2*a),h.val(2*a*(k+2)),h.scale(seedC,rho/2))
   else:bound=h.add(h.val(2+2*a*(2*k+3)),h.scale(seedC,rho/2))
   core=h.cehist([(n,pp,qq) for n,pp,qq,z in rr]);ck(core[1]<=bound[0],'full core coding bound')
   ar,_,aa,_=rows(k,state,phase,True);AC=h.fullcost(ar)
   OC=h.add(h.val(5),h.scale(h.log((9+p)*(1-p)),F(-1,2)))
   endC=h.add(h.scale(OC,1-rho),h.scale(AC,rho))
   release=h.sub(C,endC)
   ck(release[0]>=0,'entire physical padding endpoint has nonnegative full CE release')
   for sign in [-1,1]:
    preI=6+2*(k-1)*a+rho*I-sign*a
    activeI=6+I-2*aa-sign*aa
    avgI=(1-rho)*6+rho*activeI
    ck(preI-avgI==2*k*a,'retire original padding influence EXACTLY ONCE')
    W=h.sub(h.sub(h.val(preI),C),U)
    EW=h.sub(h.sub(h.val(avgI),endC),U)
    ck(W[0]>F(5,8),'every cleaned interacting profile paid at original rate4')
    ck(EW[0]>F(5,16),'full padding tree paid from SAME inherited reserve')
    if nu>F(1,2):ck(W[0]>F(85,64),'high-mean branch direct rare-law bound')
   out.append({'state':state['assignment'],'k':k,'phase':phase,'nu':str(nu),'old_U':h.pack(U),'source_CE':h.pack(C),'all_padding_CE':h.pack(endC),'CE_release':h.pack(release),'padding_4I_retired':str(2*k*a)})
ck(F(5,8)**5<F(1,8),'original five-block vacuum threshold')
ck(15**15>2**56 and 31**31>2**152,'entropy endpoints exact integer inequalities')
result={'status':'PASS','profiles':len(out),'assertions':N,'helper_assertions':h.N,'seconds':time.perf_counter()-start,'rows':out}
(R/'out'/('CONTINUATION_PILOT.json' if pilot else 'CONTINUATION_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','profiles','assertions','helper_assertions','seconds']}))
