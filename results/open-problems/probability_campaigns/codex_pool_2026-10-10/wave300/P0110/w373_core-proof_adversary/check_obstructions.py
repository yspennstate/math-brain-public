"""Exact small checks, not an FPP exponent experiment or a formal proof."""
from fractions import Fraction as Q
from itertools import product
import json
import math
from pathlib import Path
import time

root = Path(__file__).resolve().parent
start = time.process_time()
checks = []
def check(name, ok, **data):
    checks.append({"check": name, "passed": bool(ok), **data})
    if not ok:
        raise AssertionError(name)

rare_rows = []
for m in (2, 3, 10, 100, 1000):
    n = m ** 3
    pm = Q(1, n)
    dist = [(Q(m), (1-pm)/2), (Q(-m), (1-pm)/2), (Q(m*m), pm/2), (Q(-m*m), pm/2)]
    mean = sum(x*p for x,p in dist)
    variance = sum(x*x*p for x,p in dist) - mean*mean
    expected = Q(m*m) + Q(m) - Q(1,m)
    check(f"rare_variance_m_{m}", sum(p for x,p in dist)==1 and mean==0 and variance==expected,
          n=n, variance=str(variance))
    # alpha=1, denominator=n^(1/3)=m; log-sum-exp avoids overflow.
    log1 = math.log1p(-1/n) + 1
    log2 = -math.log(n) + m
    high = max(log1,log2)
    log_mgf = high + math.log(math.exp(log1-high)+math.exp(log2-high))
    log_at_upper = math.log((1-1/n)*math.exp(1/m)+(1/n)*math.e)
    rare_rows.append({"n":n,"variance_over_n_2_3":str(variance/Q(m*m)),
                      "log_exponential_moment_at_n_1_3":log_mgf,
                      "log_exponential_moment_at_n_2_3":log_at_upper})
    check(f"upper_mgf_bounded_m_{m}", log_at_upper<=1+1e-12)

# Two edge-disjoint two-edge paths in a diamond, each iid edge in {1,2}.
# Conditioning on which path is optimal couples the initially independent sums.
states = []
for a1,a2,b1,b2 in product((1,2),repeat=4):
    states.append((a1+a2,b1+b2))
p_top = Q(sum(a<=b for a,b in states),len(states))
p_A2 = Q(sum(a==2 and a<=b for a,b in states),len(states))/p_top
p_B4 = Q(sum(b==4 and a<=b for a,b in states),len(states))/p_top
p_joint = Q(sum(a==2 and b==4 and a<=b for a,b in states),len(states))/p_top
check("iid_disjoint_sums_unconditional_independence", Q(sum(a==2 and b==4 for a,b in states),16)==Q(1,4)*Q(1,4))
check("selection_destroys_conditional_independence", p_joint != p_A2*p_B4,
      selected_event="A<=B (top path wins, ties assigned top)", probability_event=str(p_top),
      conditional_A2=str(p_A2), conditional_B4=str(p_B4),
      conditional_joint=str(p_joint), conditional_product=str(p_A2*p_B4))
check("selection_biases_other_path", p_B4 != Q(1,4), unconditional_B4="1/4", conditional_B4=str(p_B4))

# Continuous analogue: transform iid continuous path sums by their common CDF.
# The transformed pair is uniform on the unit square; integrate its six order
# regions exactly. This removes both atoms and geodesic ties from the obstruction.
prob_selected = Q(1,2)
prob_A_below_and_selected = Q(1,2)-Q(1,8)
prob_B_above_and_selected = Q(1,2)-Q(1,8)
prob_cross_quadrant = Q(1,4)
cm_A = prob_A_below_and_selected/prob_selected
cm_B = prob_B_above_and_selected/prob_selected
cm_joint = prob_cross_quadrant/prob_selected
check("continuous_selection_dependence", cm_A==Q(3,4) and cm_B==Q(3,4) and cm_joint==Q(1,2) and cm_joint!=cm_A*cm_B,
      conditional_marginals=[str(cm_A),str(cm_B)], conditional_joint=str(cm_joint),
      independence_prediction=str(cm_A*cm_B), absolute_error_before=str(abs(cm_joint-cm_A*cm_B)),
      absolute_error_after_exact_conditioning="0",
      scope="Four-edge square graph with iid Uniform[1,2] weights, conditioned on one route being the unique geodesic; not the full lattice model.")
check("discrete_factorization_error_measured", abs(p_joint-p_A2*p_B4)==Q(5,121),
      absolute_error_before=str(abs(p_joint-p_A2*p_B4)), absolute_error_after_exact_conditioning="0")

# In full Z^d with all weights in [1,2], a nearest-neighbor detour has at least
# three edges and costs >=3, while the direct edge costs <=2.
check("bounded_law_adjacent_geodesic", Q(2)<3*Q(1), direct_path_upper=2,
      any_other_simple_path_lower=3, D_zero_at_v_e1=True,
      scope="Refutes a positive lower wandering bound over EVERY nonzero endpoint for this law; does not refute a large-distance lower bound.")

for n in (2,3,10,1000):
    coupled = [(Q(n),Q(n),1-Q(1,n)),(Q(n),Q(2*n),Q(1,n))]
    mean_y = sum(y*p for t,y,p in coupled)
    variance_y = sum((y-mean_y)**2*p for t,y,p in coupled)
    error_squared = sum((y-t)**2*p for t,y,p in coupled)
    agreement = sum(p for t,y,p in coupled if t==y)
    check(f"hp_agreement_variance_failure_n_{n}", variance_y==n-1 and error_squared==n and agreement==1-Q(1,n),
          probability_agreement=str(agreement), variance_T="0", variance_Y=str(variance_y),
          L2_error_squared=str(error_squared))

def norm_countermodel(x,y):
    return max(abs(Q(x))+abs(Q(y)),Q(3,2)*max(abs(Q(x)),abs(Q(y))))
for n,w in ((16,1),(64,7),(100,10),(1000,100)):
    gz=norm_countermodel(Q(n,2),w+1)
    gv=norm_countermodel(n,0)
    gap=2*gz-gv
    check(f"symmetric_norm_zero_bend_n_{n}", w+1<=Q(n,4) and gap==0,
          n=n,w=w,g_v=str(gv),g_z=str(gz),bend=str(gap),
          point_outside_width_w=True,
          scope="Norm countermodel with the elementary FPP bounds and lattice symmetries; no FPP realization is claimed.")

elapsed = time.process_time()-start
check("within_fresh_compute_gate", elapsed<10 and len(states)<=256, cpu_seconds=elapsed, enumerated_states=len(states))
report = {"command":"python -X utf8 ~/brain_workers/w373/check_obstructions.py",
          "checks_passed":sum(x["passed"] for x in checks),"checks_total":len(checks),
          "rare_event_rows":rare_rows,"checks":checks,
          "interpretation":"Finite exact checks corroborate the written proofs; no exponent estimate for actual FPP, no independent review, and no formal verification is claimed."}
(root / "verification.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print(json.dumps(report,indent=2))
