import math,json,random,time
import mpmath as m
from symmetric import integer_data,evaluate
m.mp.dps=70
start=time.monotonic();rng=random.Random(1918);count=0
for n in [3,4,8,16,24,32,64,128,256]:
 for rep in range(12):
  f=[rng.choice([-1,1]) for _ in range(n+1)];rows=integer_data(f);v=evaluate(f,70)
  if not v['I']:continue
  assert all(rows[k][1]>=rows[k+1][1] for k in range(n))
  var=1-m.mpf(rows[0][0])**2/m.mpf(2)**(2*n)
  assert v['Gamma']<=v['H']/2+var*m.log(v['I']/n,2)+m.mpf('1e-60')
  D=sum(m.mpf(math.comb(n,k))*F*F/m.mpf(2)**(2*n)*m.log(math.comb(n,k),2) for k,(F,L,Q,N) in enumerate(rows) if F)
  assert v['Gamma']/v['I']<=D/(2*v['I'])+3/(2*m.exp(m.mpf(1)/3)*m.log(2))*n**(-m.mpf(2)/3)+m.mpf('1e-60')
  # Exact integer derivative-mean check.
  I=sum(k*math.comb(n,k)*F*F for k,(F,L,Q,N) in enumerate(rows))
  moment=sum(k*(k-1)*math.comb(n,k)*F*F for k,(F,L,Q,N) in enumerate(rows))
  assert 2*moment>=(n-1)*I
  count+=1
print('symmetric_random_checks_L1_Gamma_entropy_derivative_mean',count)
checks=[]
for N in [1,2,3,24,100,1999]:
 def phi(x):return m.exp(-x)*m.besseli(0,x)
 def integrand(t):return (phi(N*t*(2-t)/4)-(1-t)**N)/t if t else m.mpf(N)/2
 C=m.quad(integrand,[0,m.mpf(1)/(N+1),1/m.sqrt(N+1),1])
 upper=m.log(4)-(2-m.sqrt(2))/m.sqrt(m.pi*N)+1/(2*m.mpf(N)) if N>=3 else (m.mpf(1) if N==1 else m.mpf(59)/64)
 assert C<upper
 checks.append({'N':N,'C_N':m.nstr(C,50),'analytic_upper':m.nstr(upper,50)})
open('integral_checks.json','w').write(json.dumps(checks,indent=2)+'\n')
print('Bessel_integral_quadrature_checks',len(checks))
print('wall_seconds',time.monotonic()-start)
