from fractions import Fraction as F
from pathlib import Path
import random,json,math
random.seed(27)
# Exact rational checks of every denominator inequality used below.
min_slack=None
for j in range(4000):
 a=F(random.randint(1,100),10); c=F(random.randint(0,60),10)
 b=F(random.randint(0,1000),1000)*c*a
 u=F(random.randint(-1000,1000),10)
 v=F(random.randint(-1000,1000),1000)*c*a
 D1=a*a+u*u; Ds=(a+b)**2+(u+v)**2
 K=(1+c)**2+2*c*c+2; L=2*c*c+2
 assert Ds<=K*D1
 assert D1<=L*Ds
 assert a/D1<=K*(a+b)/Ds
 for lam in [F(1),F(2),F(100)]:
  assert lam/(lam*lam+Ds)<=L*lam/(lam*lam+D1)
sl=[];M=1;I1=F(0);I2=F(0);Isum=F(0);Imax=F(0)
for j in range(1,25):
 old=M;M=old*(2**j)
 f1,f2=(M,old) if j%2 else (old,M)
 I1+=F(old,f1);I2+=F(old,f2);Isum+=F(old,f1+f2);Imax+=F(old,max(f1,f2))
 sl.append({'block':j,'length':str(old),'f1':str(f1),'f2':str(f2),'I1':str(I1),'I2':str(I2),'I_sum':str(Isum),'I_max':str(Imax)})
assert I1>=12 and I2>=12 and Isum<1 and Imax<1
out={'seed':27,'exact_rational_scalar_cases':4000,'lambda_values':[1,2,100],'all_scalar_assertions_passed':True,'envelope_blocks':sl,'envelope_final':{'I1':float(I1),'I2':float(I2),'I_sum':float(Isum),'I_max':float(Imax)},'warning':'Finite checks supplement the written proofs; no simulation tests (H).'}
Path('checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='envelope_blocks'},indent=2))
