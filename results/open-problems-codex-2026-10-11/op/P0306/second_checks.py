"""Numerical diagnostics for an exact deterministic countermodel, never LQG evidence."""
import pathlib,json,math
from scipy.integrate import quad
ROOT=pathlib.Path(__file__).resolve().parent
out=[]
for H in [0.01,1.,10.]:
    integ,err=quad(lambda u:2*math.sqrt(H)*math.cos(u)**2,0,math.pi/2)
    exact=math.pi*math.sqrt(H)/2
    assert abs(integ-exact)<1e-10
    max_error=0.
    for j in range(1,1000):
        t=2*math.pi*j/1000
        y=H/2*(1-math.cos(t)); xp=y; yp=H/2*math.sin(t)
        max_error=max(max_error,abs(xp*xp+yp*yp-H*y))
    assert max_error<1e-10
    delta=math.pi*H
    bound=delta/math.sqrt(H)+math.pi*math.sqrt(H)
    assert abs(bound-2*math.sqrt(math.pi*delta))<1e-10
    out.append({'H':H,'integral':integ,'exact_integral':exact,'speed_identity_max_abs_error':max_error,'boundary_distance':bound})
for k in [2,4,6,8]:
    delta=10.**(-k)
    ratio=(1+math.sqrt(1+delta))/math.sqrt(delta)
    out.append({'record_inverse_delta':delta,'distance_to_label_difference_ratio':ratio})
(ROOT/'second_check_results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
