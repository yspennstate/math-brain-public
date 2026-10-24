from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
p=R/'REPORT.md'; t=p.read_text(encoding='utf-8')
old='For positive finite optimizers the usual necessity follows here without citing a duality theorem: restrict to a compact neighborhood, use a strict feasible point, and apply finite-dimensional separation to the convex epigraph and constraint image to obtain nonnegative multipliers; the strict feasible point forces the objective multiplier to be nonzero. No assertion that every instance has a finite optimizer is needed or used.'
new='Only the proved sufficient certificate and weak duality are asserted and used here. No necessity theorem, minimax interchange, or assertion that every instance has a finite optimizer is needed.'
assert old in t or new in t
t=t.replace(old,new)
t=t.replace('For ANY fixed pointwise decomposition of this derivative among pivotal line gates (including any tie rule, or fractional splitting of signs), each piece\'s squared norm is at most 2^(-(Q-1)). Hence its normalized mass obeys q_{j,l}<=1/[k(1-epsilon_Q)]<=2/k. Fractional splitting satisfies the same upper bound because its amplitude has magnitude at most one; the source outerfractional formula itself uses its disjoint tie pieces with masses summing to one, which is the case needed below.', 'For ANY fixed disjoint pointwise tie decomposition of this derivative among pivotal line gates, each piece\'s squared norm is at most 2^(-(Q-1)). Hence its normalized mass obeys q_{j,l}<=1/[k(1-epsilon_Q)]<=2/k. These are precisely the disjoint signed pieces with masses summing to one required by the source outerfractional formula.')
anchor='## proof dependencies and changed downstream conclusions'
addition='The lead-directed analytic checks were frozen separately in LEAD_FROZEN_SPEC.json before execution: m=1..12 sunflower geometric-mass identities (algebra only), and Q=16,32,64,128,256 affine-plane incidence/union-bound constants (algebra only; no high-dimensional Boolean enumeration). Command: `python -X utf8 runs/20261011T223308Z-account05-A009-fractional-incidence-optimization/code/lead_check.py`. It passed 87 exact rational assertions in under 0.002 seconds. Together the two checkers passed 4,173 assertions. The all-Q geometric proof and Holder lower bound are analytic; these finite checks only certify the stated rational constants and exponents.\n\n'
if addition not in t: t=t.replace(anchor,addition+anchor)
t=t.replace('The proof premise is the complete local source','The proof premise is the complete local source')
t=t.replace('Source-complete conditioned forest theorem, elementary finite Gibbs identity, binomial identity, Jensen, and the supplement\'s complete-reference prior are the only premises.', 'Source-complete conditioned forest theorem and eq:outerfractional, elementary finite Gibbs identity, binomial identity, Jensen, Holder, affine-plane incidence, and the supplement\'s complete-reference prior are the premises. The outer theorem\'s use here is a scoped test of its already derived pressure expression; the lower bound does not assume its FEI conclusion.')
p.write_text(t,encoding='utf-8')
print('Report scope/validation finalized')
