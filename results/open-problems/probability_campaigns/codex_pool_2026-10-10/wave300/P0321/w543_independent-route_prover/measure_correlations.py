"""Tiny auxiliary-model quadrature, always gated; never a phase-existence proof."""
import json
import math
import time
from pathlib import Path
from fresh_compute_gate import check

started=time.process_time()
gate=check()
out=Path('NUMERICAL_CHECKS.json')
if not gate['allowed']:
    result={'command':'python -X utf8 measure_correlations.py','status':'WITHHELD',
            'reason':gate['reason'],'gate_receipt':'compute_gate_latest.json',
            'mathematical_proof_claim':False,'passed':None,'cases_run':0}
    out.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
    raise SystemExit(0)

def budget():
    if time.process_time()-started>5:
        raise RuntimeError('single-core CPU budget exceeded; no successful numerical receipt')

N=1024; A=128; T=0.1; K=1.0; L=1.0; EPS=1e-8
angles=[2*math.pi*(j+0.5)/A for j in range(A)]
costheta=[math.cos(v) for v in angles]
def circle_loss(z):
    return sum(2*math.sin(z*c/2)**2 for c in costheta)/A
def simpson(values,h):
    return h/3*(values[0]+values[-1]+4*sum(values[1:-1:2])+2*sum(values[2:-1:2]))
ts=[math.log(EPS)+(math.log(L)-math.log(EPS))*i/N for i in range(N+1)]
ks=[math.exp(t) for t in ts]; h=ts[1]-ts[0]
loss={r:[circle_loss(r*k) for k in ks] for r in (8,16,32,64)}
budget()
def log_c6(mu,r):
    values=[k*k*f/(mu+K*k*k) for k,f in zip(ks,loss[r])]
    return -9*T/(2*math.pi)*simpson(values,h)
base={r:log_c6(0,r) for r in loss}
rows=[]
for mu in (1e-6,1e-8,1e-10):
    vals={r:log_c6(mu,r) for r in loss}
    bound=9*T*mu*64**2/(8*math.pi*K*K)*math.log1p(K*L*L/mu)
    differences={r:vals[r]-base[r] for r in loss}
    assert min(differences.values())>=-1e-12
    assert max(differences.values())<=bound+1e-10
    eta_fit=-(vals[64]-vals[16])/math.log(4)
    eta=9*T/(2*math.pi*K)
    assert abs(eta_fit-eta)<0.01
    plateau=math.exp(-9*T/(4*math.pi*K)*math.log1p(K*L*L/mu))
    row={'mu':mu,'window':[8,64],'max_log_ratio':max(differences.values()),
         'analytic_log_ratio_upper_bound':bound,'fitted_eta6':eta_fit,'massless_eta6':eta,
         'exact_positive_plateau':plateau,'finite_window_relative_tolerance':0.01,
         'fit_only_diagnosis':'accept algebraic-looking orientation',
         'asymptotic_diagnosis':'reject a vanishing orientational correlation at fixed positive shear'}
    rows.append(row)
    with Path('NUMERICAL_ROWS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(row)+'\n')
    budget()

ir=[]
for phi in (0,0.7,math.pi/2):
    ta=math.log(1e-6); tb=math.log(1e-4); ni=64; dh=(tb-ta)/ni
    values=[]
    for i in range(ni+1):
        k=math.exp(ta+dh*i)
        avg=sum(2*math.sin(k*math.cos(theta)/2)**2*math.sin(theta-phi)**2 for theta in angles)/A
        values.append(T/(2*math.pi*K)*avg/(k*k))
    measured=simpson(values,dh)/(tb-ta)
    expected=T*(1+2*math.sin(phi)**2)/(32*math.pi*K)
    assert abs(measured-expected)<1e-10
    ir.append({'angle':phi,'measured_log_coefficient':measured,'exact_H4_coefficient':expected})
    budget()
result={'command':'python -X utf8 measure_correlations.py','status':'PASS','passed':True,
    'gate_receipt':'compute_gate_latest.json','cpu_seconds':time.process_time()-started,
    'single_core':True,'gpu_used':False,'quadrature_radial_intervals':N,'angular_points':A,
    'false_positive_examples_before':3,'false_positive_examples_after_plateau_check':0,
    'scope':'three synthetic auxiliary-field counterexamples only; no brain benchmark or rigorous numerical enclosure',
    'mathematical_proof_claim':False,'finite_window_cases':rows,'infrared_coefficient_cases':ir}
out.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
