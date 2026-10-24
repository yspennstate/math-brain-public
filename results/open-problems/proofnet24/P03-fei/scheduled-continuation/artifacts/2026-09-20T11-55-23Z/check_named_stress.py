#!/usr/bin/env python3
import json
from check_prob10_fei_block_recombination import truth_from_func, stress_summary

def maj3(bits):
    return 1 if sum(bits)<=1 else -1

def maj3_of_maj3(x):
    g=[maj3(x[0:3]),maj3(x[3:6]),maj3(x[6:9])]
    return 1 if sum(v==1 for v in g)>=2 else -1

def addressing(x):
    return -1 if x[2+x[0]+2*x[1]] else 1

def gamma3_maj3(x):
    seed=maj3(x[3:])
    return seed if sum(x[:3])==0 else 1

families={
  "w6": truth_from_func(6,lambda x:-1 if sum(x)==0 else 1),
  "Maj5": truth_from_func(5,lambda x:1 if sum(x)<=2 else -1),
  "Maj3_of_Maj3": truth_from_func(9,maj3_of_maj3),
  "addressing_m2_n6": truth_from_func(6,addressing),
  "bent_quadratic_n4": truth_from_func(4,lambda x:-1 if (x[0]*x[1]+x[2]*x[3])%2 else 1),
  "w3_tensor_w3": truth_from_func(6,lambda x:(-1 if sum(x[:3])==0 else 1)*(-1 if sum(x[3:])==0 else 1)),
  "Gamma3_Maj3": truth_from_func(6,gamma3_maj3),
}
print(json.dumps({
  "status":"PASS",
  "named_stress":[stress_summary(k,v) for k,v in families.items()],
  "coded_family_limitation":"The archived exact coded F_8 has 2040 inputs, so no truth-table enumeration is attempted; the all-dimensional analytic block theorem applies to it without simulation.",
  "interpretation":"These are theorem sanity/stress checks, not an independent audit and not evidence of a universal block selector."
},indent=2,sort_keys=True))
