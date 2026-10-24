from fractions import Fraction as F
import json
# Prescribed residual endpoint recurrence; not a network simulation.
for L in [120,240,480,960]:
 h=F(1,L);q=F(0);v=F(1);maxerr=F(0);occ=F(0);maxocc=F(0)
 for n in range(L):
  t=n*h;z=1+t/L;r1=-1+F(3,4)*t;s=int(q>0)
  if t<F(1,3):
   theta=-F(1,2)/r1;occ+=h*(s-theta);maxocc=max(maxocc,abs(occ))
  q+=h*z*(r1*s+F(1,2));v+=h*z*(F(1,2)*r1*s+1)
  tt=(n+1)*h;qt=F(3,8)*max(F(0),tt-F(2,3))**2
  vt=1+F(1,2)*qt+F(3,4)*tt
  maxerr=max(maxerr,abs(q-qt),abs(v-vt))
 assert maxerr<F(3,L)
 print(json.dumps({'L':L,'max_path_error':float(maxerr),'strict_prefix_occupation_primitive_error':float(maxocc),'final_q1':float(q),'limit_final_q1':float(F(1,24)),'bound_3_over_L_pass':True}))
