from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];t=time.perf_counter();d=json.loads((R/'out/SECOND_QUERY.json').read_text(encoding='utf-8'));checks=0
def ck(b):
 global checks
 checks+=1
 assert b
ck(d['status']=='PASS');ck(7**100>2**269)
for row in d['roots']:
 Slo,Shi=map(F,row['S_original']['interval']);w=row['W_depth0_1_2'];w1lo,w1hi=map(F,w[1]['interval']);w2lo,w2hi=map(F,w[2]['interval']);toplo,tophi=map(F,row['second_topup']['interval'])
 ck(w2hi<Slo/25);ck(tophi<Slo/50);ck(w2lo>=w1hi if row['l']==2 else w2lo==w1hi==0)
 ck(F(3,4)*Slo-w2hi>F(71,100)*Shi);ck(toplo>=0)
 if row['l']==2:ck(w[2]['exact']=={'2':'47/32','7':'-3/8'})
 else:ck(w[2]['exact']=={})
out={'status':'PASS','assertions':checks,'seconds':time.perf_counter()-t,'width2_total':'47/32-(3/8)log2(7)','width3_total':'0','total_bound':'<S_original/25','additional_second_topup':'<S_original/50','unused_after_oldquarter':'>71S_original/100','arithmetic':'saved outward Fraction enclosures and exact integer powers'}
(R/'out/READBACK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
