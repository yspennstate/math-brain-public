"""Small deterministic checks, never a proof of Coulomb sharpness."""
import math,json,pathlib
out=[]
for N,v in [(100,1),(1000,5),(10000,10),(10000,30)]:
    p=v/N
    # All omitted Poisson mass is added to TV; evaluate safely through logs.
    b=[math.exp(math.lgamma(N+1)-math.lgamma(k+1)-math.lgamma(N-k+1)+k*math.log(p)+(N-k)*math.log1p(-p)) for k in range(N+1)]
    z=[math.exp(-v+k*math.log(v)-math.lgamma(k+1)) for k in range(N+1)]
    tv=(sum(abs(x-y) for x,y in zip(b,z))+max(0,1-sum(z)))/2
    assert tv <= v*v/N+1e-9
    out.append({'N':N,'v':v,'binomial_poisson_TV':tv,'bound':v*v/N})
for r in [0.25,0.5,1,2,4]:
    m=100000
    val=sum((r*r+1-2*r*(-1+(2*i+1)/m))**(-.5) for i in range(m))/m
    target=1/max(1,r)
    assert abs(val-target)<.003
    out.append({'d3_shell_radius':r,'quadrature':val,'Newton_exact':target})
for k in [10,100,1000]:
    lam,t=2,.1
    logratio=math.log(lam)-math.log(k+1)+t*(2*(k-lam)+1)
    out.append({'poisson_square_k':k,'log_successive_summand_ratio':logratio})
pathlib.Path(__file__).with_name('numerical_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
