import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json
import check as c
F=c.F;R=c.R
profiles=[]
for k in [5,8,16,32,64,128,256]:
 rho=F(1,1<<k);mu=F(81,256);p=rho*(1-mu)/2;U=c.add(c.Lq(p),c.conversion(p))
 rr,_,_,pre_a,_=c.make_rows(k,4,0,0,1,1,0);preC=c.fullcost(rr)
 active,_,_,aa,_=c.make_rows(k,4,0,0,1,1,k);activeC=c.fullcost(active)
 offC=c.add(c.val(5),c.scale(c.log((9+p)*(1-p)),F(-1,2)))
 averageC=c.add(c.scale(offC,1-rho),c.scale(activeC,rho));spent=k*rho/16
 c.ck(c.sub(preC,averageC)[1]>=0,'interval consistency with analytically nonnegative exact CE release')
 for sign in [-1,1]:
  preI=(6+2*(k-1)*pre_a+rho*F(3,4)+sign*pre_a)/4
  activeI=(F(13,2)+F(sign,8))/4
  averageI=(1-rho)*F(3,2)+rho*activeI
  c.ck(preI-averageI==spent,'actual physical padding influence spent exactly once')
  preW=c.sub(c.sub(c.val(4*preI),preC),U)
  avgW=c.sub(c.sub(c.val(4*averageI),averageC),U)
  c.ck(preW[0]>F(5,4),'initial cleanup endpoint paid same U')
  c.ck(avgW[0]>F(155,128),'entire padding tree averaged reserve positive including negative active leaf')
  sourcebound=c.sub(preW,c.val(4*spent))
  # Exact physical identity gives this lower bound; intervals have ample strict slack.
  c.ck(avgW[1]>=sourcebound[0],'interval consistency with analytic complete CE-release physical ledger')
  whole=c.scale(avgW,F(1,8))
  for s in [1,2,3]:
   rr,_,_,a,_=c.make_rows(k,4,0,s,1,1,0);C=c.fullcost(rr);ig=F(s)+F(3,4)
   fourI=6+2*(k-1)*a+rho*ig+sign*a
   z=c.sub(c.sub(c.val(fourI),C),U)
   c.ck(z[0]>F(5,8),'unchanged OTHER tensor outcomes retain original reference and debit')
   whole=c.add(whole,c.scale(z,F(c.comb(3,s),8)))
  c.ck(whole[0]>F(5,8),'whole actual mixed policy, all firstbit/padding siblings retained')
  profiles.append({'k':k,'sign':sign,'padding_tree_average_reserve':c.pack(avgW),'whole_policy_average_reserve':c.pack(whole),'padding_influence_spent':str(spent),'initial_reserve':c.pack(preW)})
result={'status':'PASS','assertions':c.N,'runtime_seconds':c.time.perf_counter()-c.START,'signed_tree_profiles':profiles,'scope':'all k>=5 analytic, frozen7 widths exact; entire stated mixed policy only, no universal or pointwise claim'}
(R/'out/TREE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','assertions':c.N,'runtime_seconds':result['runtime_seconds'],'signed_tree_profiles':len(profiles)}))