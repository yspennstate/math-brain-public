"""Exact algebra supporting a conditional lemma, not a SAW experiment."""
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
import time

ROOT=Path(__file__).resolve().parent
START=time.monotonic()
J=[[F(-1,2),F(-3,4),F(1,4)],[F(1,2),F(-3,4),F(1,4)],[F(-3,4),F(-9,16),F(9,16)]]
INV=[[F(-1),F(1),F(0)],[F(-5,3),F(-1,3),F(8,9)],[F(-3),F(1),F(8,3)]]
checks=0

def check(condition):
    global checks
    assert condition
    checks+=1
    if time.monotonic()-START>45:
        raise TimeoutError("w399 second fresh gate expired")

def matvec(matrix, vector):
    return [sum((a*b for a,b in zip(row,vector)),F(0)) for row in matrix]

for r in range(3):
    for c in range(3):
        check(sum((INV[r][k]*J[k][c] for k in range(3)),F(0))==F(r==c))
        check(sum((J[r][k]*INV[k][c] for k in range(3)),F(0))==F(r==c))

det=sum((F(sign)*J[0][p[0]]*J[1][p[1]]*J[2][p[2]] for p,sign in [((0,1,2),1),((1,2,0),1),((2,0,1),1),((2,1,0),-1),((1,0,2),-1),((0,2,1),-1)]),F(0))
check(det==F(9,32))
row_norms=[sum(map(abs,row),F(0)) for row in INV]
check(row_norms==[F(2),F(26,9),F(20,3)])

reconstruction_cases=0
for mu,variance,alpha in itertools.product([F(-1),F(0),F(1)],[F(1),F(8,3),F(14,3),F(4)],[F(1,2),F(5,8),F(1),F(29,14)]):
    theta=[mu,variance/2-F(4,3),(1+variance*(alpha-1))/2]
    check(matvec(INV,matvec(J,theta))==theta)
    reconstruction_cases+=1

corner_max=[F(0)]*3
for e in itertools.product([F(-1),F(1)],repeat=3):
    theta=matvec(INV,e)
    for k in range(3):
        check(abs(theta[k])<=row_norms[k])
        corner_max[k]=max(corner_max[k],abs(theta[k]))
check(corner_max==row_norms)
check(F(3,8)*F(52,9)+F(40,3)==F(31,2))

ito_cases=0
for a,b,c,alpha,variance,mu in itertools.product([F(1),F(2),F(3,2)],[F(-1),F(0),F(3,2)],[F(-2),F(1)],[F(1,2),F(5,8),F(29,14)],[F(1),F(8,3),F(14,3)],[F(0),F(2)]):
    # Laurent inverse of a*y + b*y^2/2 + c*y^3/6, through the y term.
    r=b/(2*a)
    s=c/(6*a)
    fixed_space_derivative=2*a*(r*r-s)-c
    check(fixed_space_derivative==b*b/(2*a)-F(4,3)*c)
    derivative_drift=fixed_space_derivative+mu*b+variance*c/2
    power_ito=alpha*derivative_drift/a+alpha*(alpha-1)*variance*b*b/(2*a*a)
    jet_drift=alpha*(mu*(b/a)+(variance/2-F(4,3))*(c/a)+(1+variance*(alpha-1))*(b/a)**2/2)
    check(power_ito==jet_drift)
    ito_cases+=1

wrong=[F(0),F(14,3)/2-F(4,3),(1+F(14,3)*(F(29,14)-1))/2]
wrong_residual=matvec(J,wrong)
check(wrong_residual==[F(0),F(0),F(9,8)])
correct=[F(0),F(8,3)/2-F(4,3),(1+F(8,3)*(F(5,8)-1))/2]
check(matvec(J,correct)==[F(0)]*3)

result={
    "command":"python -B -X utf8 check_three_probe.py",
    "elapsed_seconds":round(time.monotonic()-START,6),
    "passed":True,
    "exact_arithmetic":"fractions.Fraction",
    "checks":checks,
    "parameter_reconstruction_cases":reconstruction_cases,
    "ito_and_laurent_cases":ito_cases,
    "residual_corner_cases":8,
    "matrix":[[str(v) for v in row] for row in J],
    "determinant":str(det),
    "inverse":[[str(v) for v in row] for row in INV],
    "inverse_row_norms":[str(v) for v in row_norms],
    "maximum_reconstruction_error":"0 (exact)",
    "before_two_symmetric_probes":{"rank":2,"mu":"0","variance":"14/3","alpha":"29/14","normalized_initial_drift_residuals":["0","0"],"identifies_target_coefficients":False},
    "after_three_probes":{"rank":3,"wrong_parameter_third_residual":"9/8","target_mu":"0","target_variance":"8/3","target_alpha":"5/8","all_target_residuals":"0"},
    "stability_constants":{"mu":"2 epsilon","variance":"(52/9) epsilon","exponent":"(31/(2 v_min)) epsilon, requiring v>=v_min>0","jet_inverse_norm":"20/3"},
    "scope":"Algebra and conditional-lemma checks only. No measured SAW scaling limit, Brownian driver approximation, global probe cover, retrieval lift, or novelty claim.",
    "formal_checker":None
}
(ROOT/"MEASUREMENTS_THREE_PROBE.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
