import json,time
from pathlib import Path
from fractions import Fraction as F
import interval_primitives as m
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=0
def check(x,label):
 global count
 count+=1
 assert x,label
 if time.monotonic()-start>55:raise RuntimeError('55 second watchdog')
C=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
def v(row):return m.V(*map(F,row))
H3=v(C['scalar_rows'][2]['H']);H4=v(C['scalar_rows'][3]['H'])
A=v(next(h['A'] for h in C['histories'] if h['m']==4))
s3=3-H3;s4=2-H4
T3=3*m.h(F(1,4))-H3;T4=4*m.h(F(1,8))-H4
S0=3+s4/4;S1=3+s3/8;U=m.positive(S1-S0);B0=T4/4;B1=T3/8
res=S1-A-B0-B1-F(11,32)-U
check(F(37,32)<F(155,128) and F(17,16)<F(155,128),'uniform sharper old whole bound')
check(2-F(155,128)-F(7,32)-F(11,32)-F(7,32)==F(1,128),'exact second-reset margin')
check(B0.a>0 and B1.a>0,'actual prescribed first and second full new reference bills positive')
check(U.a>0,'actual added post-data transaction debit positive')
check(B0.b<=F(7,32) and B1.b<=F(7,32),'old and second reset budgets')
check(res.a>F(1,128),'all old booked components plus second new full KL paid')
out={'status':'PASS','assertions':count,'runtime_seconds':time.monotonic()-start,'m':4,'A_and_booked_L0':A.out(),'S0':S0.out(),'S1':S1.out(),'B0':B0.out(),'B1':B1.out(),'U':U.out(),'omega':'11/32','remaining_after_second_reset':res.out(),'scope':'explicit actual Boolean spectrum formulas; full new KL bills positive, signed conversion positivity not asserted'}
(R/'out/SECOND.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:out[k] for k in ['status','assertions','runtime_seconds']}))
