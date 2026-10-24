import math,json,itertools
from pathlib import Path
from fractions import Fraction

def rate(c,lam):
 terms=[1.]
 for e in range(1,160):terms.append(terms[-1]*lam/(3+e))
 z=sum(terms)
 ell=sum(t*math.log((3+e)*(2+e)) for e,t in enumerate(terms))/z
 mu=2*c
 return ell-(mu*math.log(mu)-(mu-2)*math.log(mu-2))/2

def exact_check():
 owners=[i for i in range(4) for _ in range(3)]
 cycles=[(0,)+p for p in itertools.permutations(range(1,4)) if p[0]<p[-1]]
 pairings=total_cycles=0
 def rec(stubs,edges):
  nonlocal pairings,total_cycles
  if not stubs:
   pairings+=1
   multiplicities={}
   for a,b in edges:
    key=tuple(sorted((owners[a],owners[b])));multiplicities[key]=multiplicities.get(key,0)+1
   total_cycles+=sum(math.prod(multiplicities.get(tuple(sorted((cyc[i],cyc[(i+1)%4]))),0) for i in range(4)) for cyc in cycles)
   return
  a=stubs[0]
  for i in range(1,len(stubs)):rec(stubs[1:i]+stubs[i+1:],edges+[(a,stubs[i])])
 rec(list(range(12)),[])
 measured=Fraction(total_cycles,pairings)
 formula=Fraction(math.factorial(3)*6**4,2*math.prod(12-(2*j+1) for j in range(4)))
 assert measured==formula
 return {'degree_sequence':[3]*4,'pairings':pairings,'sum_stub_cycles':total_cycles,'measured_expectation':str(measured),'formula':str(formula)}

rows=json.loads(Path('experiments.json').read_text())['constants']
out={'finite_exact_check':exact_check(),'rates':[{'c':r['c'],'log_mean_rate':rate(r['c'],r['lambda'])} for r in rows]}
Path('first_moment.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
