---
name: p0073_ants_unique_fixed_point_all_graphs_to_7_vertices_2026_11_10
description: "[PROVISIONAL] P0073 trace-reinforced ants (Kious-Mailler-Schapira): any graph with two stable limits? None found: all 22,824 (graph, nest, food) cases on connected graphs with 4-7 vertices, 8 starts each, one attracting fixed point of p(w)=w. Part (b) of the conjecture is refuted (dead branches, 11 Nov) and the paper is posted: see p0073_ants_dead_branches_paper_posted_2026_11_11. Convergence, part (a), is still open."
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T22:50:59+02:00
  status: provisional
  evidence: "mini2 ~/p0073/out7_p*.txt, out456_v2.txt (DONE instances, multi 0)"
---

# P0073 trace-reinforced ants: numerical evidence for a unique attracting fixed point

Conjecture (Kious-Mailler-Schapira, JEP 9 (2022) 505-536): on a finite graph with nest N and food F, the normalized
weights W_n/n converge to a deterministic limit. Reduces to: dw/dt = p(w) - w has a unique attracting zero, where
p_e(w) = P_w(walk from N crosses e before hitting F).

Search (ants_fp2.py on Mac mini 2, 10-11 Nov 2026): every connected graph in the networkx atlas with 4 to 7 vertices,
every ordered (N, F) pair up to automorphism. For each case, 8 starts (4 uniform on (0,1)^m, 4 log-uniform in
(e^-7, 1)^m), damped iteration w <- max(w + 0.4 (p(w) - w), 1e-12) up to 6000 steps, converged when max |p(w)-w| < 1e-6;
two limits counted distinct if they differ by more than 2e-3 in some coordinate.

Result: 22,824 cases (n=4..6: 1,734; n=7: 21,090). Every start converged and every case had a single limit.
No case printed MULTI or NOCONV. (An earlier v1 run with tolerance 1e-8 / 1e-5 covered n=3..6 with the same answer.)

What this does not show: it samples 8 starts per case, it only sees attracting points of the damped map (saddles and
repellers are invisible), and n <= 7 is small. The conjecture stays open; no proof argument yet.
Files: ants_fp.py, mk_v2.py -> ants_fp2.py; outputs on yitz@mini2 ~/p0073/out7_p0..p5.txt, out456_v2.txt.


CORRECTION 2026-11-11 00:2x (audit by an agent, accepted): the v1 outputs out_n4/5/6 hold 10,274 NOCONV lines (90/936/9,248; residual ~1.7e-7), so "v1 gives the same answer" is wrong. Cause: an edge into a dead end has limit 0 and p_e - w_e ~ -w_e^2 there (the linear term cancels), so convergence is only 1/t; v2 passes its 1e-6 test with such coordinates still ~1e-3 off, half the 2e-3 distinctness threshold. The unique-fixed-point conclusion survives on v2. Before any paper uses the census: prune edges on no N-F path, then check the Jacobian at each limit.

UPDATE 2026-11-11 01:1x (an agent; counterexample confirmed by an agent, referee note dc2f89e110d5): do NOT prune dead ends.
The 00:2x line above ("prune edges on no N-F path") is withdrawn. Path N-x-F plus a pendant edge N-y: at pendant weight c the
walk never enters y with probability q/(2-q), q = 1/(1+c), so p_c = 2c/(1+2c) and the fixed point is c = 1/2, not 0. In general a
zero-weight edge {u,v} has linear rate G(u)/W_u + G(v)/W_v (G = expected visits before F, W = total weight at the vertex, F
contributes 0); rate > 1 means 0 repels, rate < 1 attracts, and rate exactly 1 (common) gives the 1/t decay seen as NOCONV.
New census agent_run/p0073/ants_audit.py on FULL graphs: damped flow then Newton to 1e-13 on the detected support, pure Newton
from random starts (finds unstable points too), coordinates under 1e-8 snapped to 0 and re-solved, eigenvalues of Dp - I on the
support, the transverse rate for every zero edge, and a perturb-and-flow test when the rate is exactly 1.
n <= 5 (189 cases): exactly one attractor each, 184 unstable fixed points beside them; every marginal point that fails the
flow-back test flows to that one attractor. agent's independent rerun (32 starts, orbit counts 23/162/1549/21090) agrees for n <= 5.
n = 6 running 11 Nov 01:0x (full6.jsonl); n = 7 (21,090 cases) not yet rerun with the new census.

UPDATE 2026-11-11 02:1x (an agent; status of this paragraph: PROVISIONAL - Theorem 1 proof written as a sketch, not yet refereed; census n<=6 complete, n=7 running).
Source read on the rendered page: Kious-Mailler-Schapira arXiv 2106.10559v2, Conjecture 1.1 has two sentences: (a) W(n)/n -> deterministic chi a.s.; (b) "if in addition the distance between N and F is at least 2, then chi_e > 0 for all e".
SENTENCE (b) IS FALSE. Rigorous: Theorem 1 (dead branch). Let u be a neighbour of F and e={u,y} an edge of G-F such that the component H of y in G-F-e contains neither u nor N. Then W_f(n)/n -> 0 a.s. for e, every edge inside H and every edge H-F. Proof: with X=W_e, A=W_uF, h=P_N(hit u before F): P(e crossed)=hX/(X+S), P(uF crossed)=hA/(S+X(1-rho_H)), rho_H >= 1/deg(y) because every other edge at y has weight <= X; so log(X/A) has drift <= -c p_X/(n+1) + summable, and limsup X/n>0 would force sum p_X(j)/(j+1)=inf, hence X/A -> 0. Smallest examples with dist 2: the paw (N pendant on a triangle through F; also follows from their Thm 1.3), and the 2-connected C4 = N,a,F,b plus a vertex joined to a and F (limit 2^-1/2,1/2 on the square, 0 on the detour).
A triangle (non-bridge) pocket hanging at a neighbour of F stays ALIVE (joint rate up to 4/3): the bridge is essential.
FIXED-POINT STRUCTURE (v = voltage of unit current N->F in the limit network): expected crossings of e = w_e(v(u)+v(z)); at a fixed point v=1 at every neighbour x of F with w_xF>0, v>=1 on visited vertices; an F-neighbour with positive F-edge needs a neighbour with v>1. Hence no all-positive fixed point when some F-neighbour is not adjacent to I0 = component of N in G-F-N(F) (second family of counterexamples, includes 3-connected graphs).
REFINED CONJECTURE (front/shadow rule), exact on the mean-field census: dead edges = never-crossable edges + xF for F-neighbours x not adjacent to I0 + every branch of G-F hanging by a bridge at a shadow vertex (a reachable vertex outside I0), on the side away from N. Census (ants_exact.py + classify.py in agent_run/p0073, Mac 2 ~/p0073): all connected graphs with <= 6 vertices, all (N,F) up to automorphism, 1,738 cases: one flow limit from 6 starts in every case, zero set == rule in 1,738/1,738 (961 d=1, 777 d>=2), max Re eig(Dp-I) on the support -0.054. Theta graph (k branches of L edges): j-th edge from N has limit k^(-j/L) (numerics k=2..8).
TOOL SCARS: (1) the Woodbury one-inverse kernel has ~1e-10 cancellation noise - fine for the flow, wrong for classifying marginal zeros (35 false flags); polish with the per-edge solve. (2) marginal zeros decay like 1/t and a Newton polish parks them at ~1e-7 "stable": detect dying coordinates by the decay ratio between T and 2T, set them to 0, then polish. (3) reduce the graph to the component of N in G-F first or the per-edge solve is singular. (4) p(w)-w is not a gradient field under a diagonal metric (gradtest.py).
What would change it: a referee finding a gap in the drift argument of Theorem 1; an n=7 case with two limits or a zero set off the rule.

UPDATE 11 Nov 03:0x local: written up and posted as "Dead branches in the trace-reinforced ant process", github.com/yspennstate/trace-reinforced-ants-dead-branches main 227e6bc; what is proved and what is only computed, and the posting checklist, are in [[p0073_ants_dead_branches_paper_posted_2026_11_11]]. Theorem numbers there: Theorem 2 = the drift argument called Theorem 1 above; Theorem 5 = the shadowed-neighbour statement. Referee verdict (an agent) still pending.
