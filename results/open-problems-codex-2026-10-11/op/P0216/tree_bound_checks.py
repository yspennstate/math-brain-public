import math,json,pathlib
R=pathlib.Path(__file__).resolve().parent;N=100
S=[[0]*N for _ in range(N)];S[0][0]=1
for k in range(1,N):
 for s in range(k,N):
  S[k][s]=sum(4*math.factorial(j+1)*S[k-1][s-j] for j in range(1,s-k+2))
Z=[0,1]
for n in range(2,N+1):
 numerator=sum(math.comb(n+k-1,k)*S[k][n-1] for k in range(1,n))
 assert numerator%n==0
 z=numerator//n;Z.append(z)
 assert math.log(z)-math.lgamma(n+1)<=math.log(4)+2*math.sqrt(32*n)+1e-10
# Verify the two finite factorial estimates over a large boundary grid.
for r in range(1,80):
 for s in range(1,80):assert math.factorial(r+1)*math.factorial(s+1)<=2*math.factorial(r+s)
for n in range(2,150):
 for k in range(1,n):assert math.factorial(n+k-1)*math.factorial(n-k+1)<=4**(k-1)*math.factorial(n)**2
balanced=json.loads((R/'balanced_counts.json').read_text())
for rec in balanced:assert rec['H']<=Z[rec['n']]
lo=.9;hi=.99
for _ in range(80):
 mid=(lo+hi)/2
 if math.log1p(-mid)+3*mid>0:lo=mid
 else:hi=mid
r=(lo+hi)/2;c=math.exp(r)/r**(2/3)
result={'max_n_tree_bound_checked':N,'Z_first_8':Z[1:9],'factorial_merge_r_s_checked_to':79,'factorial_ratio_n_checked_to':149,'r_star':r,'upper_constant':c,'root_residual':math.log1p(-r)+3*r}
(R/'tree_bound_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2))
