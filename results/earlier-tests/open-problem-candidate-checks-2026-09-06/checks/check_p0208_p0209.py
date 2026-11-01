"""Exact checks for the two Aldous-Fill questions (P0208 and P0209).

P0208: for m = 5, 7, 9, 11, 13 the 4-regular graph on Z_m x {0,1} (each vertex joined to both fibre points over the
two neighbouring positions) is checked to be arc-transitive by carrying a fixed arc to every arc with an explicit
automorphism. Hitting times of (0,0) are solved exactly and matched with the closed form, giving tau_0 = (m^2-1)/6 + m
and the maximal commute time 2 floor(m^2/4) + 2m. A formula that omits the fibre-arrival cost is rejected.

P0209: for s = 3, 4, 10, 100, 1000 a four-state reversible chain with a rare coordinate (epsilon = 1/s^2) and a fast
sign flip (rate s^4) is checked in exact quadratic-field arithmetic: stationarity, reversibility, the four
eigenvalues 0, 1, R, R+1, the centred unit-variance observable bounded by 2, its Poisson solution, and the asymptotic
variance. A rate matrix with one asymmetric entry is rejected.
Finite cases check the formulas; the arguments for the infinite families are in
analyses/P0208_P0209_aldous_fill_questions.md.
"""
from fractions import Fraction as F
import json


def solve(matrix,rhs):
 a=[list(row)+[b] for row,b in zip(matrix,rhs)];n=len(a)
 for j in range(n):
  pivot=next(i for i in range(j,n) if a[i][j]);a[j],a[pivot]=a[pivot],a[j]
  scale=a[j][j];a[j]=[x/scale for x in a[j]]
  for i in range(n):
   if i!=j:
    c=a[i][j];a[i]=[x-c*y for x,y in zip(a[i],a[j])]
 return [row[-1] for row in a]

def wreath(m):
 vertices=[(j,b) for j in range(m) for b in [0,1]]
 adj={v:{((v[0]+delta)%m,b) for delta in [-1,1] for b in [0,1]} for v in vertices}
 assert all(len(adj[v])==4 and v not in adj[v] for v in vertices)
 arc_count=0
 # Carry a fixed directed edge to every directed edge and check the full permutation.
 for u in vertices:
  for v in adj[u]:
   direction=1 if v[0]==(u[0]+1)%m else -1
   perm={x:((u[0]+direction*x[0])%m,x[1]^(u[1] if x[0]==0 else v[1] if x[0]==1 else 0)) for x in vertices}
   assert perm[(0,0)]==u and perm[(1,0)]==v and len(set(perm.values()))==2*m
   assert all({perm[w] for w in adj[x]}==adj[perm[x]] for x in vertices)
   arc_count+=1
 target=(0,0);states=[v for v in vertices if v!=target]
 matrix=[[F(int(v==w))-F(int(w in adj[v]),4) for w in states] for v in states]
 hitting=solve(matrix,[F(1)]*len(states)); h={target:F(0),**dict(zip(states,hitting))}
 formula={v:F(0) if v==target else F(2*m) if v[0]==0 else F(v[0]*(m-v[0])+m) for v in vertices}
 assert h==formula
 assert all(h[v]==1+sum(h[w] for w in adj[v])/4 for v in states)
 tau0=sum(h.values())/(2*m);taumax=2*max(h.values())
 assert tau0==F(m*m-1,6)+m and taumax==2*(m*m//4)+2*m
 # A deliberately omitted fiber-arrival cost must fail the direct equations.
 bad={v:F(v[0]*(m-v[0])) for v in vertices}
 assert any(bad[v]!=1+sum(bad[w] for w in adj[v])/4 for v in states)
 return {'m':m,'vertices':2*m,'arcs_checked':arc_count,'tau0':str(tau0),'max_commute':str(taumax),'ratio':str(taumax/(2*tau0)),'all_hitting_equations_exact':True,'missing_fiber_cost_control_rejected':True}

def rare(s):
 e=F(1,s*s); rate=F(s**4);D=(1-e)*(1-4*e)
 def scalar(x):return (F(x),F(0))
 def add(x,y):return (x[0]+y[0],x[1]+y[1])
 def scale(c,x):return (c*x[0],c*x[1])
 def mul(x,y):return (x[0]*y[0]+D*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
 def sign(x):
  a,b=x
  if a==0:return (b>0)-(b<0)
  if b==0:return (a>0)-(a<0)
  if a*b>0:return (a>0)-(a<0)
  delta=a*a-b*b*D
  return ((a>0)-(a<0))*((delta>0)-(delta<0))
 def total(xs):
  out=scalar(0)
  for x in xs:out=add(out,x)
  return out
 A=(2*e,F(1));B=scale(1/(1-e),add(scalar(2),scale(-1,A)))
 assert sign(A)>0 and sign(add(scalar(1),scale(-1,A)))>0 and sign(add(B,scalar(-1)))>0
 states=[(y,z) for y in [0,1] for z in [-1,1]]
 pi=[(e if y else 1-e)/2 for y,z in states]
 Q=[]
 for i,(y,z) in enumerate(states):
  row=[F(0)]*4
  row[states.index((1-y,z))]=e if y==0 else 1-e
  row[states.index((y,-z))]=rate/2
  row[i]=-sum(row);Q.append(row)
 assert all(sum(pi[i]*Q[i][j] for i in range(4))==0 for j in range(4))
 assert all(pi[i]*Q[i][j]==pi[j]*Q[j][i] for i in range(4) for j in range(4))
 g=[add(scale(z,A),scale(y-e,B)) for y,z in states]
 h=[add(scale(F(z)/rate,A),scale(y-e,B)) for y,z in states]
 assert total(scale(pi[i],g[i]) for i in range(4))==scalar(0)
 assert total(scale(pi[i],mul(g[i],g[i])) for i in range(4))==scalar(1)
 assert g[states.index((1,1))]==scalar(2)
 assert all(sign(add(scalar(2),scale(-1,x)))>=0 and sign(add(scalar(2),x))>=0 for x in g)
 assert all(total(scale(-Q[i][j],h[j]) for j in range(4))==g[i] for i in range(4))
 sigma2=scale(2,total(scale(pi[i],mul(g[i],h[i])) for i in range(4)))
 expected=add(scale(2/rate,mul(A,A)),scale(2*e*(1-e),mul(B,B)))
 assert sigma2==expected and sign(sigma2)>0
 # Spectrum checked through a basis of four exact coordinate eigenvectors.
 vectors=[[F(1)]*4,[F(y)-e for y,z in states],[F(z) for y,z in states],[(F(y)-e)*z for y,z in states]]
 for vector,lam in zip(vectors,[F(0),F(1),rate,rate+1]):
  assert all(sum(Q[i][j]*vector[j] for j in range(4))==-lam*vector[i] for i in range(4))
 broken=[row[:] for row in Q];broken[0][2]+=e;broken[0][0]-=e
 assert any(sum(pi[i]*broken[i][j] for i in range(4))!=0 for j in range(4))
 assert all(sum(Q[i][j]/rate for j in range(4) if j!=i)<=1 for i in range(4))
 return {'s':s,'epsilon':str(e),'R':str(rate),'D':str(D),'mean_variance_supnorm_exact':True,'stationarity_reversibility_poisson_spectrum_exact':True,
         'sigma2_quadratic_coefficients':[str(x) for x in sigma2],'asymmetric_rate_control_rejected':True,
         'cdf_zero_distance_lower_bound':str(F(1,2)-F(3,s)-e)}

def main():
 graphs=[wreath(m) for m in [5,7,9,11,13]]
 chains=[rare(s) for s in [3,4,10,100,1000]]
 print(json.dumps({'wreath_checks':graphs,'rare_chain_checks':chains},indent=2))


if __name__=='__main__':main()
