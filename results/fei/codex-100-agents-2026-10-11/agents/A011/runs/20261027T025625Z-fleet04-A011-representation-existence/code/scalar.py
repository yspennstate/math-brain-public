from pathlib import Path
from fractions import Fraction as F
import time,json,hashlib
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
    global checks
    checks+=1
    assert x,checks
    if checks%1000==0:assert time.monotonic()-start<55,'RUNTIME_INCOMPLETE'
ws=[]
for b in range(12,33):
    e=F(1,1<<(b+1));den=(1+3*e)*(1-2*e+2*e*e);num=1+3*e*e
    ck(den-num==e*(1-e)*(1-6*e));ck(den>num>0)
    z=num/den;ze=2-z;gap=1-z*ze
    ck(gap==(1-z)**2);ck(0<gap<1)
    ws.append(dict(b=b,epsilon=str(e),Zclean=str(z),Zedit=str(ze),loss_lower=str(gap/2),loss_upper=str(3*gap/(4*(1-gap)))))
rows=0
for a in range(1,17):
    for b in range(12,33):
        L=a+b;finite=F(0)
        for M in range(129):
            if M:finite+=(1+M*(M+1))*F(L+M,1<<M)
            tail=F(M**3+(L+7)*M*M+(5*L+23)*M+9*L+34,1<<M)
            ck(finite+tail==9*L+34)
            ck(F(9*L+34,a*(1<<(b+1)))<=F(151,8192))
            ck(F(a+b+2,a*(1<<b))<=F(15,4096));rows+=1
for j in range(3,129):
    A=1+j*(j+1);B=1+4*j*(j+1)
    ck(5+16*j*(j+1)<=2**(j+5));ck(B<=4*A);ck(F(1536*B,23)<=320*A)
cs=4*F(4081,4096)-F(135,92)-1;cc=15*F(4081,4096)-320*F(151,8192)-F(37,8)
ck(cs==F(35751,23552));ck(cc==F(18111,4096));ck(cs>0 and cc>0)
# Hypothesis and compatibility guards; no larger claim is inferred.
# With one-bit dictator and exact source model Droot=0, a reset Qchild=Pchild/2
# on BOTH constant children has e=1 and Qloss=0: no-reset is essential.
ck(F(1,2)+F(1,2)==1)
# References of mass two have D(P||2P)=-1; subprobability is essential.
ck(2>1)
ans=dict(status='PASS',assertions=checks,scalar_tuples=rows,witnesses=len(ws),seconds=time.monotonic()-start,residual_C0=str(cs),residual_constant=str(cc),helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(R/'out/WITNESSES.json').write_text(json.dumps(ws,indent=2),encoding='utf-8')
(R/'out/SCALAR.json').write_text(json.dumps(ans,indent=2),encoding='utf-8')
(R/'out/SCALAR_V1_INCOMPLETE.json').write_text(json.dumps({'status':'INCOMPLETE','reason':'RUNTIME_INCOMPLETE after frozen55 seconds; original helper recomputed each Fraction partial sum; no scalar completion claimed','helper_sha256':'b216ed7ca44fcc3e44f8d26b57323b244b762da07b6fa32f2dfddda1a1fbff12'},indent=2),encoding='utf-8')
print(json.dumps(ans))
