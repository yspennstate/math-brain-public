"""Actual data interposition, retained references and complete reset bookings."""
import reference as r
from fractions import Fraction as F
from pathlib import Path
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]

def pos(e):
 if not e:return {}
 lo,hi=r.interval(e)
 r.ck(lo>0 or hi<0,'strict resolved booking sign')
 return e if lo>0 else {}

def value(e):return {'exact':r.enc(e),'interval':r.enciv(e)}

def liftcheck(Q):
 # Physical ordering u,v,remaining masked data. Lifted core R need not match source.
 N=len(Q)//4;mask=N-1
 core=tuple(4*Q[s<<2] for s in range(N))
 r.ck(sum(core)==1,'normalized retained core reference')
 for s,q in enumerate(Q):r.ck(q==core[(s>>2)^(mask if s&1 else 0)]/4,'exact full lifted reference')
 return core

def run(l,pilot):
 h=r.core(l);m=3*l
 G=r.carrier((1,)*len(h));H=r.carrier(h)
 parent=tuple((G if not s&1 else H)[s>>1] for s in range(2*len(G)))
 cs,qs,_,Os,Ks,Es,_=r.transport(parent,0,[F(1,len(parent))]*len(parent))
 records=[]
 for branch,(t,Q,K) in enumerate(zip(cs,qs,Ks)):
  liftcheck(Q)
  basecs,_,basepr,baseO,_,_,_=r.transport(t,1,Q)
  baseTC=r.stats(basecs[0])[4]
  basebooking=pos(r.plus((1,baseTC),(-1,K)))
  for j in ([0] if pilot else range(m)):
   ds,dqs,pr,O,Kc,E,refonly=r.transport(t,j+2,Q)
   bs=[];terms=[]
   for bit,(tt,QQ,KK) in enumerate(zip(ds,dqs,Kc)):
    RR=liftcheck(QQ)
    # Compare full transported reference with a separate core-only transport.
    expected_core=r.transport(h if branch else (1,)*len(h),j,liftcheck(Q))[1][bit]
    r.ck(tuple(expected_core)==RR,'commutation with core-only normalized transport')
    vchildren,_,reach,Ov,_,Ev,refs=r.transport(tt,1,QQ)
    r.ck(reach==[F(1,2),F(1,2)],'carrier remains fair after ACTUAL data query')
    r.eq(Ov,{},'zero carrier cost after data query')
    # Exact erasure-pair imbalance eta, including all reference-only atoms.
    U=[QQ[r.insert(s,1,0)]+QQ[r.insert(s,1,1)] for s in range(len(QQ)//2)]
    eta=sum((abs(x-U[s^(len(U)-1)]) for s,x in enumerate(U)),F())/2
    r.ck(eta==0,'actual erased reference pairing preserved')
    TC=r.stats(vchildren[0])[4];HH=r.stats(vchildren[0])[2]
    r.eq(TC,r.stats(vchildren[1])[4],'both full terminal TC retained')
    r.eq(HH,r.stats(vchildren[1])[2],'both full terminal H retained')
    bk=pos(r.plus((1,TC),(-1,KK)));bs.append(bk)
    terms.append({'data_bit':bit,'eta':str(eta),'carrier_reach':[str(x) for x in reach],'incoming_K':value(KK),'full_terminal_TC':value(TC),'full_terminal_H':value(HH),'positive_booking':value(bk),'reference_only_mass':str(refs)})
   meanb=r.plus(*[(F(1,2),b) for b in bs])
   needed=pos(r.plus((1,meanb),(-1,E)))
   gap=r.plus((1,needed),(-1,basebooking))
   rec={'l':l,'selector_branch':branch,'data_coordinate':j,'data_reach':[str(x) for x in pr],'reference_only_mass':str(refonly),'data_outcome_cost':value(O),'data_erasure_release':value(E),'old_booking':value(basebooking),'mean_child_booking':value(meanb),'new_parent_booking':value(needed),'increase':value(gap),'children':terms}
   records.append(rec)
 return records

def main():
 start=time.perf_counter();pilot='pilot' in sys.argv
 ls=[2] if pilot else [2,3]
 out=[]
 for l in ls:out.extend(run(l,pilot))
 r.ck(time.perf_counter()-start<55,'frozen runtime cap')
 result={'status':'PASS','records':out,'cases':len(out),'exact_assertions':r.COUNT,'seconds':time.perf_counter()-start,'positive_booking_increases':sum(r.interval({int(p):F(c) for p,c in row['increase']['exact'].items()})[0]>0 for row in out)}
 (ROOT/'out'/('PILOT.json' if pilot else 'INTERPOSITION.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print({key:v for key,v in result.items() if key!='records'})
 print('INCREASES',[(x['l'],x['selector_branch'],x['data_coordinate'],x['increase']['interval']) for x in out if x['increase']['exact']])
if __name__=='__main__':main()
