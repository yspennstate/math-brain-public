from fractions import Fraction as F
import core as c
rows=[]
for width in range(1,6):
 for sign in [1,-1]:
  h=tuple(sign*(1 if x==0 else -1) for x in range(1<<width))
  f=(-1,-1,-1,1) if sign==1 else (-1,-1,1,-1)
  s=c.shadow(f);ph=c.physical(h);q=(1+ph['mu'])/2;v=4*q*(1-q)
  X=q*sum(s['ap'])+(1-q)*sum(s['am']);actual=c.physical(c.compose(f,h))
  assert s['B']==c.const(1) and s['Ip']==1 and actual['d'][width]==X
  assert v*s['Ip']==4*max(q,1-q)*X
  rows.append({'width':width,'encoder_sign':sign,'q':str(q),'X':str(X),'W':str(v),'physical_data_I':str(actual['d'][width]),'price':str(v/X)})
c.dump('physical_bias_controls.json',{'status':'PASS','cases':len(rows),'rows':rows});print('PASS:10 actual oriented sharp-bias compositions')
