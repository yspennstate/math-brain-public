"""Exact finite checks of the source-normalized count and path sprinkling obstruction."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json
import math
import time

ROOT = Path(__file__).resolve().parent
start = time.monotonic()
rows = []
# Independent geometric-length sum, rather than the claimed closed form.
for m in (1,2,4,8,16,64):
    p = F(1,4)
    law = [(1-p)*p**k for k in range(m)] + [p**m]
    assert sum(law) == 1
    sprinkled = sum(law[i]*law[j] for i,j in product(range(m+1),repeat=2) if i+j>=m)
    original = p**m
    ratio = sprinkled/original
    assert ratio == 1+m*(1-p)
    rows.append({"case":"path-sprinkling","bridge_edges":m,"p":"1/4",
                 "original_probability_exact":str(original),
                 "sprinkled_probability_exact":str(sprinkled),
                 "amplification_exact":str(ratio),"amplification":float(ratio)})

# Direct spin enumeration on short paths independently checks the switching ratio.
for m in (1,2):
    n = 3*m+1
    r = 3
    sites = (0,m,2*m,3*m)
    samples = []
    for state in range(1<<n):
        spins = [1 if state & (1<<i) else -1 for i in range(n)]
        weight = r**sum(spins[i]==spins[i+1] for i in range(n-1))
        samples.append((spins,weight))
    z = sum(weight for _,weight in samples)
    def moment(indices):
        value = 0
        for spins,weight in samples:
            sign = math.prod(spins[x] for x in indices)
            value += sign*weight
        return F(value,z)
    a,b,c,d = sites
    u = moment(sites)-moment((a,b))*moment((c,d))-moment((a,c))*moment((b,d))-moment((a,d))*moment((b,c))
    switching = -u/(2*moment((a,b))*moment((c,d)))
    assert switching == F(1,4)**m
    rows.append({"case":"path-spin-enumeration","bridge_edges":m,
                 "configurations":1<<n,"switching_ratio_exact":str(switching)})

# Translation-invariant one-dimensional Ising covariance on an eight-site window.
# Its exact moments have E[sigma_a sigma_b sigma_c sigma_d]=t^(b-a+d-c) in sorted order.
for t in (F(1,3),F(1,2),F(4,5)):
    sites = tuple(range(8))
    def g(a,b): return t**abs(a-b)
    def u(a,b,c,d):
        s = sorted((a,b,c,d))
        return t**(s[1]-s[0]+s[3]-s[2])-g(a,b)*g(c,d)-g(a,c)*g(b,d)-g(a,d)*g(b,c)
    h = [sum(g(x,y) for y in sites) for x in sites]
    v = sum(h)
    bsum = sum(g(x,y)**2 for x,y in product(sites,repeat=2))
    direct = -sum(u(*quad) for quad in product(sites,repeat=4) if len(set(quad))<4)
    formula = 12*sum(x*x for x in h)-6*bsum-16*v+12*len(sites)
    assert direct == formula
    assert direct/v**2 <= 12/math.sqrt(len(sites))
    chi = (1+t)/(1-t)
    bubble = (1+t*t)/(1-t*t)
    anchored = 12*chi*chi-6*bubble-16*chi+12
    # Multiplicity-pattern calculation independently checks anchored count.
    pattern = 2+8*(chi-1)+6*(bubble-1)+12*((chi-1)**2-(bubble-1))
    assert anchored == pattern and 0 <= anchored <= 12*chi*chi
    rows.append({"case":"infinite-line-window","t":str(t),
                 "formula_error_exact":"0","anchored_contact_exact":str(anchored),
                 "contact_ratio":float(direct/v**2),"chi_exact":str(chi)})

# Explicit sharpness examples: fully locked spins, plus the cost of dropping transitivity.
for n in (64,512,4096):
    transitive = F(12,n)-F(22,n*n)+F(12,n*n*n)
    rows.append({"case":"transitive-locked-sharpness","N":n,
                 "N_times_contact_ratio":float(n*transitive)})
for n in (100,10000,1000000):
    m = math.isqrt(3*n)
    v = m*m+n-m
    contact = F(12*m**3-22*m*m+12*m+2*(n-m),v*v)
    assert contact <= 12/math.sqrt(n)
    rows.append({"case":"one-locked-component-plus-independent-spins","N":n,"locked_component":m,
                 "contact_ratio":float(contact),"sqrt_N_times_ratio":float(math.isqrt(n)*contact),
                 "violates_transitive_12_over_N":contact>F(12,n)})

result = {"gate":"BRIDGE_COMPUTE_GATE.json","checks_passed":len(rows),
          "seconds":time.monotonic()-start,"method":"exact rational geometric sums and finite spin moments",
          "cases":rows,"proof_status":"computation corroborates written derivations; independent referee pending"}
(ROOT/"bridge_measurements.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"checks_passed":len(rows),"seconds":result["seconds"],
                  "amplification_at_m64":rows[5]["amplification"],
                  "transitive_sharpness":rows[-6:-3],"nontransitive":rows[-3:]},indent=2))
