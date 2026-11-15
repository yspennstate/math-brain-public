#!/usr/bin/env python3
"""Independent derivative, trigonometric, and finite-interval checks."""
import os
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"
import json
from pathlib import Path
import resource
import signal
import sys
import time
import mpmath as mp
from recheck import functional

signal.alarm(120)
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
mp.mp.dps = 100
started = time.monotonic()

def data(g, u):
    d=mp.pi-g; T=d-u; h=mp.pi/d
    a=lambda t: mp.sin(g)/(2*mp.pi*(mp.cos(t-u)+mp.cos(g)))
    b=lambda t: a(-t)
    e=lambda t: (mp.sin(T)/(2*mp.pi*(mp.cos(t)-mp.cos(T))) -
        h*mp.sin(h*T)/(2*mp.pi*(mp.cos(h*t)-mp.cos(h*T))))
    av=[mp.diff(a,0,j) for j in range(4)]
    bv=[mp.diff(b,0,j) for j in range(4)]
    ev=[mp.diff(e,0,j) for j in range(4)]
    W=av[0]*bv[1]-av[1]*bv[0]
    base=ev[0]/(2*av[0])
    C=base*(av[2]+bv[2])-ev[2]
    D=base*(av[3]+bv[3])-ev[3]
    R=av[2]/av[0]; q=1/(1-mp.cos(T)); qh=1/(1-mp.cos(h*T))
    E=mp.cot(T/2)-h*mp.cot(h*T/2)
    Cformula=(E*(R-q)+h*mp.cot(h*T/2)*(h*h*qh-q))/(2*mp.pi)
    lower=h*mp.cot(h*T/2)*(h*h*qh-q)/(2*mp.pi)
    v=(g+u)/2; w=(g-u)/2
    Rminusq=mp.tan(w)*(mp.tan(w)-mp.tan(v))/2
    assert abs(C-Cformula)<mp.mpf("1e-55")*max(1,abs(C)), (g,u,C,Cformula)
    assert abs(R-q-Rminusq)<mp.mpf("1e-55")*max(1,abs(R))
    assert E>0 and h*h*qh-q>0 and C>0 and lower>0
    assert C>=lower-mp.mpf("1e-55")*max(1,abs(C))
    assert abs(D)<mp.mpf("1e-55")

    def point(t):
        at=a(t); bt=b(t); et=e(t)
        ap=mp.diff(a,t); bp=mp.diff(b,t); ep=mp.diff(e,t)
        wt=at*bp-ap*bt
        return ((et*bp-ep*bt)/wt,(at*ep-ap*et)/wt)
    # Differentiate the closed envelope independently of its linear equations.
    xp=mp.diff(lambda t: point(t)[0],0)
    yp=mp.diff(lambda t: point(t)[1],0)
    xpp=mp.diff(lambda t: point(t)[0],0,2)
    ypp=mp.diff(lambda t: point(t)[1],0,2)
    alpha=av[0]; p=bv[1]
    assert abs(xp-C/(2*p))<mp.mpf("1e-50")*max(1,abs(xp))
    assert abs(yp+C/(2*p))<mp.mpf("1e-50")*max(1,abs(yp))
    assert abs(alpha*(xpp+ypp)-C)<mp.mpf("1e-50")*max(1,abs(C))
    graph_curvature=(xpp+ypp)/mp.sqrt(2)/((xp-yp)/mp.sqrt(2))**2
    target=mp.sqrt(2)*p*p/(alpha*C)
    assert abs(graph_curvature-target)<mp.mpf("1e-50")*max(1,abs(target))
    return {"gamma":float(g),"u":float(u),"C":float(C),
            "lower_bound":float(lower),"R_minus_q":float(R-q),
            "graph_second_derivative":float(target),
            "base":float(base),"B2_coefficient":float(C/(4*alpha)),
            "decomposition_relative_error":float(abs(C-Cformula)/abs(C))}

results={"sign_checks":[],"branch_checks":[]}
for g in (mp.mpf(".001"),mp.mpf(".02"),mp.mpf(".4"),mp.pi/3,
          mp.mpf("1.4"),mp.pi/2-mp.mpf(".001")):
    d=mp.pi-g
    for f in map(mp.mpf,("0",".01",".25",".5",".9",".99")):
        results["sign_checks"].append(data(g,g+f*(d-g)))

# The claimed symmetric case, including near Delta=1.
for g in map(mp.mpf,(".0001",".1",".4","1.0")):
    results["sign_checks"].append(data(g,(mp.pi-g)/2))

# Positive finite-B displacements from the independently discretized integral.
for gs, us in ((".4",".4"),(".4","1.3707963267948966"),("1.2","1.5")):
    g=mp.mpf(gs); u=mp.mpf(us); row=data(g,u)
    observations=[]
    for B in (.01,.005):
        eps=B*1e-4
        def deriv(x):
            return (functional(B+eps,float(g),float(u),0,x,x)-
                    functional(B-eps,float(g),float(u),0,x,x))/(2*eps)
        c0=deriv(0); c1=deriv(1)
        x=-c0/(c1-c0)
        observed=(x-row["base"])/(B*B)
        assert x>row["base"]
        observations.append(observed)
    error=abs(observations[-1]-row["B2_coefficient"])
    assert error<.003*row["B2_coefficient"]
    extrapolated=2*observations[-1]-observations[0]
    extrapolation_error=abs(extrapolated-row["B2_coefficient"])
    assert extrapolation_error<1e-5*row["B2_coefficient"]
    results["branch_checks"].append({
        "gamma":float(g),"u":float(u),"predicted_B2":row["B2_coefficient"],
        "observed_B2":observations,"absolute_error":error,
        "extrapolation_error":extrapolation_error})

# An attempted wider sufficient condition really fails outside u>=gamma:
# positivity of C may persist, but R-q is then negative.
g=mp.mpf(".4"); u=mp.mpf(".1")
v=(g+u)/2; w=(g-u)/2
outside=mp.tan(w)*(mp.tan(w)-mp.tan(v))/2
assert outside<0
results["outside_sufficient_range"]={"gamma":float(g),"u":float(u),
                                    "R_minus_q":float(outside)}
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes=rss if sys.platform=="darwin" else rss*1024
assert rss_bytes<1024**3
results["resources"]={"elapsed_seconds":time.monotonic()-started,
    "peak_rss_MiB":rss_bytes/1024**2,"nice":os.getpriority(os.PRIO_PROCESS,0)}
Path(__file__).with_name("geometry_checks.json").write_text(json.dumps(results,indent=2)+"\n")
print("PASS sign/decomposition/graph checks:",len(results["sign_checks"]))
print("max relative decomposition error:",
      max(r["decomposition_relative_error"] for r in results["sign_checks"]))
for row in results["branch_checks"]:
    print("branch",json.dumps(row,sort_keys=True))
print("outside sufficient range:",float(outside))
print("resources:",json.dumps(results["resources"],sort_keys=True))
