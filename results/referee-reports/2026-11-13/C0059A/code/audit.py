#!/usr/bin/env python3
"""Independent checks of sampling, layer bookkeeping, and electrical solves."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import math,json,csv,random
from pathlib import Path
from scipy.integrate import quad
from scipy.special import gammaln
from peeling_layers import logh,layer_update,Sampler
from peeling_skeleton import statistics_for,rotate,split_at

checks={}
# A beta-geometric mixture, computed independently by integration, agrees with the gamma law.
errs=[]
for a in [1.8,2.,2.2,2.4]:
 alpha,beta=a-1.5,2.5-a
 normal=math.exp(gammaln(alpha+beta)-gammaln(alpha)-gammaln(beta))
 c=-math.sqrt(math.pi)/(2*math.gamma(1.5-a))
 for k in [1,2,7,31]:
  pm=quad(lambda b:normal*b**alpha*(1-b)**(beta+k-2),0,1,epsabs=1e-10)[0]
  target=c*math.exp(gammaln(k+1.5-a)-gammaln(k+1.5)+logh(k+1))
  errs.append(abs(pm-target))
assert max(errs)<1e-7
checks['beta_geometric_vs_gamma_max_abs_error']=max(errs)
# Check every small layer state directly by a cyclic list of heights.
nchecks=0
for p in range(1,16):
 for d in range(1,2*p+1):
  # Peel the last low edge before the block of high edges.
  initial=[0]*d+[1]*(2*p-d);j=d-1
  for k in [0,1,5]+[-z for z in range(1,p)]:
   for side in [0,1]:
    rotated=initial[j:]+initial[:j]
    if k>=0:out=[1]*(2*k+1)+rotated[1:]
    elif side==0:
     # Delete backwards into low-height edges, including the peeled edge.
     start=(j-(2*(-k)-1))%(2*p)
     rr=initial[start:]+initial[:start];out=rr[2*(-k):]
    else:out=rotated[2*(-k):]
    expected_height=min(out);expected_d=out.count(expected_height)
    pp,dd,hh=layer_update(p,d,0,k,side)
    assert (pp,dd,hh)==(p+k,expected_d,expected_height),(p,d,k,side,out,(pp,dd,hh))
    nchecks+=1
checks['layer_states_checked_against_explicit_cyclic_boundary']=nchecks
# Analytic networks: initial two half-edges in parallel; chain plus one terminal half-edge.
s=statistics_for([(0,2)],[-1],[],1)
assert abs(s['skeleton_resistance']-.25)<1e-12
s=statistics_for([(2,2)],[-1,0,1],[],1)
assert abs(s['skeleton_resistance']-2.25)<1e-12
checks['analytic_networks']='two half-edges: 1/4; length-two chain plus two half-edges: 9/4'
# Exact acceptance probability is 1/(1+nu(negative)); compare measured frequencies.
r=list(csv.DictReader(open('data/sampler_acceptance.csv')))
checks['acceptance_by_a']={}
for a in [1.8,2.,2.2,2.4]:
 rr=[x for x in r if float(x['a'])==a]
 accepted=sum(int(x['accepted']) for x in rr);proposals=sum(int(x['proposals']) for x in rr)
 observed=accepted/proposals;expected=1/(1+1/(2*(a-1)))
 z=(observed-expected)/math.sqrt(expected*(1-expected)/proposals)
 assert abs(z)<6
 checks['acceptance_by_a'][str(a)]=dict(observed=observed,expected=expected,z=z)
rr=list(csv.DictReader(open('data/skeleton_runs.csv')))
checks['max_electrical_energy_relative_error']=max(float(x['electrical_energy_relative_error']) for x in rr)
assert checks['max_electrical_energy_relative_error']<1e-7
# No PDFs, archives, or paper page images were retained.
for p in Path('sources').iterdir():assert p.is_file() and p.suffix=='.txt'
checks['source_files_plain_text_only']=True
Path('data/audit_results.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
