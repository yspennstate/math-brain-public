import mpmath as mp
mp.mp.dps=40

def q2(s,a,b,c,B):
 x,y=a+s,b+s; d=x*y-c*c; Z=(1+x)*(1+y)-c*c
 weights=[mp.mpf(1),x,y,d]
 scores=[mp.mpf(0),B[0]/x,B[1]/y,(y*B[0]+x*B[1]-2*c*B[2])/d]
 v=sum(weights[i]*weights[j]*(scores[i]-scores[j])**2 for i in range(4) for j in range(i))
 return (v-2*mp.log(x*y/d)*(B[0]*B[1]-B[2]**2-B[3]**2))/Z**2
for a,b,c in [(1,2,mp.mpf('0.8')),(mp.mpf('0.1'),mp.mpf('0.2'),mp.mpf('0.13')),(1,1,mp.mpf('0.99')),(mp.mpf('0.01'),3,mp.mpf('0.1'))]:
 for B in [(1,0,0,0),(1,1,0,0),(1,-1,0,0),(0,0,1,0),(0,0,0,1),(1,2,3,0)]:
  vals=[(-1)**k*mp.diff(lambda s:q2(s,a,b,c,B),mp.mpf('0'),k) for k in range(7)]
  if min(vals)<-mp.mpf('1e-20'):print('FAIL',a,b,c,B,[float(v) for v in vals])
print('done')
