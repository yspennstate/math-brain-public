from pathlib import Path
import json,math,random
random.seed(24)
rows=[]
for c in [0.01,0.1,0.5,1.,2.,10.]:
 k=1+c*c/2+c*math.sqrt(c*c+4)/2
 t=c/(k-1)
 ratio=(1+(t+c)**2)/(1+t*t)
 rows.append({'c':c,'K_sharp':k,'equality_ratio':ratio,'relative_error':abs(ratio/k-1)})
mx=0
for j in range(20000):
 c=10**random.uniform(-2,2);k=1+c*c/2+c*math.sqrt(c*c+4)/2
 a=10**random.uniform(-3,3);b=a*random.uniform(-100,100);d=a*c*random.uniform(-1,1)
 ratio=(a*a+(b+d)**2)/(a*a+b*b)
 assert 1/k*(1-1e-12)<=ratio<=k*(1+1e-12)
 mx=max(mx,ratio/k)
cancel=[]
kappa=2/math.pi
for logT in [1,2,5,10,20,50,100]:
 T=math.exp(logT);A=1+T;b=kappa*T*logT
 joint=1/(1+2*T);single=A/(A*A+b*b)
 cancel.append({'log_T':logT,'joint_over_single':joint/single,'asymptotic':kappa*kappa*logT*logT/2})
d={'sharp_constant_checks':rows,'random_checks':20000,'max_ratio_over_bound':mx,'oppositely_skewed_Cauchy_cancellation':cancel}
Path('numerical_checks.json').write_text(json.dumps(d,indent=2));print(json.dumps(d,indent=2))
