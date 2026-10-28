from pathlib import Path
from fractions import Fraction as F
import importlib.util,argparse,json,time
R=Path(__file__).resolve().parents[1];sp=importlib.util.spec_from_file_location('local_calibration',R/'code/check_calibration.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
checks=0
def ck(b):
 global checks
 assert b
 checks+=1
def config(g,t1,t2):
 q=(F(1,2)-g)/2;lam=1/(2*q*((1-t1*t1)/t1+(1-t2*t2)/t2));pa=lam*q*(1-t1*t1)/t1;pb=lam*q*(1-t2*t2)/t2
 p=[pa,pb,F(0),pa,pb,F(0)];Q=[q,q,g,q,q,g];ts=[t1,t2,F(1),-t1,-t2,F(-1)]
 refs=[[Q[s]*(1+sg*ts[s]) for s in range(6)] for sg in [1,-1]]
 ck(sum(p)==sum(Q)==sum(refs[0])==sum(refs[1])==1)
 ck(all((refs[0][s]+refs[1][s])/2==Q[s] for s in range(6)))
 for z in [0,1]:
  L=lam*(-1)**z
  for i in [0,1]:
   s=3*z+i;ck(p[s]*ts[s]/(1-ts[s]**2)==L*Q[s])
  ck(ts[3*z+2]==(-1)**z)
  ck(sum(Q[s]*ts[s] for s in range(3*z,3*z+3))==(-1)**z*(g+q*(t1+t2)))
 cost=m.sub(m.pair_ce(p,refs),m.ce(p,Q));formula=m.logs([(p[s]/2,1/(1-ts[s]**2)) for s in range(6) if p[s]])
 m.zero(m.sub(cost,formula));ck(cost[0]>0)
 return {'g':str(g),'t1':str(t1),'t2':str(t2),'lambda':str(lam),'p':[str(x) for x in p],'Q':[str(x) for x in Q],'tilts':[str(x) for x in ts],'minimum_cost':[str(x) for x in cost],'exact_primal_dual':True}
def zero_case(g,fraction):
 q=(F(1,2)-g)/2;p=[F(1,4),F(1,4),F(0)]*2;Q=[q,q,g]*2;tilt=fraction if g else F(0);ts=[F(0),F(0),tilt,F(0),F(0),-tilt]
 refs=[[Q[s]*(1+sg*ts[s]) for s in range(6)] for sg in [1,-1]]
 ck(sum(refs[0])==sum(refs[1])==1);ck(all(refs[u][s]==Q[s] for u in [0,1] for s in range(6) if p[s]));ck(sum(Q[s]*ts[s] for s in range(3))==g*fraction)
 ck(m.pair_ce(p,refs)==m.ce(p,Q))
 return {'g':str(g),'fraction':str(fraction),'cost_exact':0}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');a=ap.parse_args();start=time.monotonic()
 gs=[F(0),F(1,12)] if a.pilot else [F(0),F(1,12),F(1,6)];tt=[F(1,4),F(1,3)] if a.pilot else [F(1,4),F(1,3),F(1,2),F(2,3),F(3,4)]
 rows=[config(g,t1,t2) for g in gs for t1 in tt for t2 in tt];ck(len(rows)==(8 if a.pilot else 75))
 zeros=[zero_case(g,x) for g in [F(0),F(1,12),F(1,6)] for x in [F(0),F(1,4),F(1,2),F(3,4),F(1)]]
 p=[F(0),F(0),F(1)];Q=[F(1,2),F(1,4),F(1,4)];rr=[[F(5,8),F(1,8),F(1,4)],[F(3,8),F(3,8),F(1,4)]]
 ck(sum(rr[0])==sum(rr[1])==sum(Q)==1);ck(all((rr[0][s]+rr[1][s])/2==Q[s] for s in range(3)));ck(m.ce(p,Q)==m.pair_ce(p,rr)==(F(2),F(2)))
 ck(time.monotonic()-start<55)
 out={'positive_KKT_cases':rows,'zero_cost_boundary_cases':zeros,'actual_free_nonempty_profile':{'labels':[1,2,7],'p':['0','0','1'],'Q':['1/2','1/4','1/4'],'R_plus':['5/8','1/8','1/4'],'R_minus':['3/8','3/8','1/4'],'old_and_both_new_CE_bits':2},'checks':checks+m.N,'seconds':time.monotonic()-start}
 name='GHOST_PILOT.json' if a.pilot else 'GHOST_CHECK.json';(R/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'file':name,'KKT_cases':len(rows),'checks':out['checks'],'seconds':out['seconds']}))
