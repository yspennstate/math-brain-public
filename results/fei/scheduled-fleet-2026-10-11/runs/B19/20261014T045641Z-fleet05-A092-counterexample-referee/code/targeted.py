import check as C
from fractions import Fraction as F
import json,time
START=time.perf_counter();hits=[];counts={}
for mask in range(256):
 t=tuple(1-2*(mask>>x&1) for x in range(8))
 r=C.audit(t,0,6,'two_spectators_mask'+str(mask));key=str((r['entropy_drift_sign'],r['conditional_reset_sign']))
 counts[key]=counts.get(key,0)+1
 if F(r['influence']) and r['entropy_drift_sign']<=0 and r['conditional_reset_sign']>0:hits.append(r)
C.save('TWO_SPECTATOR_WITNESSES.json',hits)
# Independent original character sums, no FWHT used for the critical certificate.
def direct(t,labels):
 N=len(t);ans={}
 for mask in range(N):
  amplitude=sum(v*(-1)**((x&mask).bit_count()) for x,v in enumerate(t))
  if amplitude:ans[sum(1<<i for j,i in enumerate(labels) if mask>>j&1)]=F(amplitude*amplitude,N*N)
 C.ck(sum(ans.values())==1)
 return ans
C.spectrum=direct
t=tuple((-1)**(x>>1&1) if (x&1)==0 else (-1 if x>>3==0 else 1) if x>>2&1 else 1 for x in range(16))
r=C.audit(t,1,8,'FOUR_BIT_CERTIFICATE')
C.ck(r['entropy_drift']=={'2':'-1/2','3':'9/8','5':'-5/8'})
C.ck(r['conditional_reset']=={'2':'-2','3':'9/8','5':'1/8'})
C.ck(3**9<2**4*5**5 and 3**9*5>2**16)
C.ck(r['entropy_drift_sign']==-1 and r['conditional_reset_sign']==1 and not r['sufficient_retained_likelihood'])
C.ck(F(r['influence'])==F(1,2))
C.ck(r['spectator_marginal_JS']=={} and r['joint_conditional_debit']==r['entropy_drift'])
C.ck(2**24*5**4>3**21 and 27>25)
C.ck(r['conditional_root_KL']=={'2':'3/2','3':'-3/4'})
C.ck(r['conditional_branch_release']=={'2':'-2','3':'-3/4','5':'11/8'})
r['strict_sign_integer_certificates']={'negative_entropy_drift':'3^9 < 2^4*5^5','positive_conditional_KL_reset':'3^9*5 > 2^16'}
r['false_extension']='[extra conditional KL reset]_+ <= [conditional spectator entropy drift]_+'
C.save('FOUR_BIT_CERTIFICATE.json',r)
C.ck(time.perf_counter()-START<120)
result={'status':'PASS','cases':257,'primary_assertions':C.COUNT,'entropy_helper_assertions':C.E.ASSERTIONS,'runtime_seconds':time.perf_counter()-START,'two_spectator_counterexamples':len(hits),'two_spectator_sign_counts':counts,'direct_character_four_bit_certificate':True}
C.save('TARGETED_RESULT.json',result);print(json.dumps(result))
