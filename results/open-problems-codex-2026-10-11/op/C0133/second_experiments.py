from fractions import Fraction as F
from pathlib import Path
import itertools,json,time
start=time.monotonic();q=F(1,4);a=F(1,8)
anti=sum(((q+s*a)*(q-s*a) for s in [-1,1]),F(0))/2*q
persistent=sum(((q+s*a)**2 for s in [-1,1]),F(0))/2*q
assert anti==F(3,256) and persistent==F(5,256) and q**3==F(4,256)
# Independent cookie noise with visit-dependent variance, conditionally centered on Q.
bias=F(1,16);count=0
for arrows in itertools.product(range(4),repeat=3):
 actual=F(0);prediction=F(0)
 for s in [-1,1]:
  Q=[q+s*bias,q-s*bias,q,q]
  prediction+=F(1,2)*Q[arrows[0]]*Q[arrows[1]]*Q[arrows[2]]
  for noise in itertools.product([-1,1],repeat=3):
   w=F(1,16)
   for i,e in enumerate(arrows,1):
    p=Q.copy();eps=F(1,16) if i%2 else F(1,32);p[2]+=noise[i-1]*eps;p[3]-=noise[i-1]*eps
    assert min(p)>0 and sum(p)==1;w*=p[e]
   actual+=w
 assert actual==prediction;count+=1
# Nonexchangeable, strictly elliptic arrows with summable probabilities in one direction.
tails={}
for N in [3,10,100]:
 t=F(1)
 for m in range(3,N+1):t*=1-F(1,m*m)
 assert t==F(2*(N+1),3*N);tails[str(N)]=str(t)
results={'anti_cookie_path':str(anti),'marginal_walk_path':str(q**3),'persistent_sign_rwre_path':str(persistent),'anti_pair_covariance':str(-a*a),'latent_noise_joint_strings_checked':count,'cookie_parameter_variance_first_up':str(F(1,16)**2),'cookie_parameter_variance_second_up':str(F(1,32)**2),'summable_direction_tail_products':tails,'summable_direction_limit_tail':'2/3','summable_direction_exactly_one_at_first_probability':'1/6','summable_direction_no_occurrence_probability':'1/2','elapsed_seconds':time.monotonic()-start,'scope':'Exact finite algebra and joint laws; no inference about general C0133.'}
Path('second_experiments.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
