"""Deterministic finite-Fourier checks; these numbers do not prove a gas phase."""
from pathlib import Path
from datetime import datetime, timezone
import json
import math
import time

ROOT=Path(__file__).resolve().parent
start=time.monotonic()
gate={'created_utc':datetime.now(timezone.utc).isoformat(), 'purpose':'Check the spectral compatibility constants and identify a false angular-GFF substitution.', 'max_wall_seconds':30, 'max_L':512, 'max_mode_pairs':30000, 'hardware':'CPU only; no GPU, training, services, agents, or network', 'inputs':'stipulated Gaussian model only; no test-bank input'}
(ROOT/'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2)+'\n', encoding='utf-8')
beta,a,b,cutoff,rho=1.0,1.3,1.0,1.0,1.0
rows=[]
worst_theta_error=0.0
worst_density_error=0.0
checked_modes=0
for L in [64,128,256,512]:
    radius=math.floor(cutoff*L/(2*math.pi))
    mode_count=0
    theta0=0.0
    theta_r=0.0
    incompatible_var=0.0
    r=L/4
    for nx in range(-radius,radius+1):
        for ny in range(-radius,radius+1):
            if time.monotonic()-start>gate['max_wall_seconds']:
                raise RuntimeError('Fresh compute gate elapsed; preserve partial artifacts and stop.')
            kx=2*math.pi*nx/L
            ky=2*math.pi*ny/L
            k2=kx*kx+ky*ky
            if not (0<k2<=cutoff*cutoff):
                continue
            mode_count+=1
            checked_modes+=1
            x,y=kx/math.sqrt(k2),ky/math.sqrt(k2)
            w0,w1=-ky/2,kx/2
            cos=math.cos(kx*r)
            for s in [0.25,1.0,1.75]:
                ql=1/(beta*a*k2**(s/2))
                qt=1/(beta*b*k2)
                c00=ql*x*x+qt*y*y
                c01=(ql-qt)*x*y
                c11=ql*y*y+qt*x*x
                induced=w0*w0*c00+2*w0*w1*c01+w1*w1*c11
                density=rho*rho*(kx*kx*c00+2*kx*ky*c01+ky*ky*c11)
                expected_theta=1/(4*beta*b)
                expected_density=rho*rho*k2**(1-s/2)/(beta*a)
                worst_theta_error=max(worst_theta_error,abs(induced-expected_theta))
                worst_density_error=max(worst_density_error,abs(density-expected_density))
            # Exact modal contraction reduces to constant theta spectrum.
            theta0+=expected_theta/L**2
            theta_r+=expected_theta*cos/L**2
            # Baseline shortcut: independent angular GFF, with stiffness K_A=1.
            incompatible_var+=2*(1-cos)/(beta*k2*L**2)
    if mode_count>gate['max_mode_pairs']:
        raise RuntimeError('Mode count exceeds fresh compute gate.')
    c6=math.exp(-36*(theta0-theta_r))
    baseline_c6=math.exp(-18*incompatible_var)
    exact_limit=math.exp(-9*cutoff**2/(4*math.pi*beta*b))
    rows.append({'L':L,'distance':r,'mode_count':mode_count,'theta_variance':theta0,'theta_covariance':theta_r,'compatible_C6':c6,'continuum_C6_limit':exact_limit,'relative_error_to_limit':abs(c6-exact_limit)/exact_limit,'independent_angle_GFF_C6':baseline_c6})
assert worst_theta_error<1e-10
assert worst_density_error<1e-10
assert rows[-1]['relative_error_to_limit']<0.015
assert rows[-1]['compatible_C6']>0.45
assert rows[-1]['independent_angle_GFF_C6']<0.01
result={'command':'python -X utf8 ~/brain_workers/w544/verify_elasticity.py','model':'UV-cutoff compatible Gaussian displacement; not a Riesz Gibbs gas','parameters':{'beta':beta,'a':a,'b':b,'Lambda':cutoff,'rho':rho,'s_values':[0.25,1.0,1.75]},'checks':{'modal_pairs':checked_modes,'covariance_contractions':3*checked_modes,'max_absolute_theta_contraction_error':worst_theta_error,'max_absolute_density_contraction_error':worst_density_error,'all_assertions_passed':True},'rows':rows,'elapsed_seconds':time.monotonic()-start,'interpretation':'The incompatible independent-angle substitution gives decay, while the angle derived from a stable shear displacement tends to a positive constant. This tests formulas only; no Monte Carlo, microscopic transfer, or independent review is claimed.'}
(ROOT/'MEASUREMENTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
