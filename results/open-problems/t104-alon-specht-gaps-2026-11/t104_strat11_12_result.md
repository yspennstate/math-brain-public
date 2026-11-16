# T104, 5+1 region (11), N = 6: corner ball, Bernstein cover and collars (STRAT11, STRAT12, STRAT13)

Status on 13 Nov 2026, 09:41 local. Region (11) at N = 6 is proved.

## Proved

STRAT11 (strat11/, replay strat11/replay_all.py): for 0 < ||S - S0|| <= 1/20800 the numerator satisfies T6 >= ||S - S0||/120.
Checked independently in strat11_check/t104_check_strat11_ball.py. After the ball, 13,368 boxes of the STRAT10 cover stayed
OPEN, chart volume 3333609/32768.

STRAT12 (strat12/, replay strat12/replay_all.py, all checks PASS): each OPEN box gets an exact certificate of one of two kinds on
the box B, with rational lambda_k >= 0 and the feasibility constraints g_k of STRAT10 cover_face.necessary():

- exclusion: -sum lambda_k g_k has every Bernstein coefficient on B positive, so B has no feasible point;
- positivity: T - sum lambda_k g_k (products g_k g_l allowed) has every Bernstein coefficient on B positive, so T > 0 on the
  feasible part of B.

Boxes that fail both are halved along their widest side, to depth 16. Result: 13,359 of 13,368 boxes closed (7,384 by exclusion,
5,314 by positivity, 661 after splitting; 15,748 certified leaves). Open chart volume 3333609/32768 -> 189/134217728.

The connected constraint used by STRAT12, 25t^2 - 5t tau + delta, is STRAT10's (5t - M00)(5t - M11) - M01^2 with tau the trace
and delta the determinant of M (strat12/verify_formulation.py).

## Independent replay

strat12_check/my_replay.py rebuilds each residual, maps the box to [0,1]^6 and computes the full tensor of Bernstein
coefficients with its own code, in Fractions only. On 120 random certified leaves (60 of each kind, seed 7): 120 PASS, 0 FAIL
(strat12_check/my_replay_120.out). The target polynomial agrees with STRAT10 cover_face.polynomials()[0] exactly, ratio 1 at six
random rational points. The tarball sha256 matched on both machines (strat12_check/remote_sha.txt).

## Nine leaves left by STRAT12

Nine leaves remain, one per box: nodes 12091 12407 14175 15603 15773 19750 20736 21058 21550 (strat12_check/open9_boxes.txt).
All lie at v1 near -1 and v2 near -1. Each contains a point of the closure where the connected constraint vanishes: five contain
two-edge limits with coordinates in Q(sqrt 5), four (19750, 21058, 12407, 15603) contain limits with coordinates in Q(sqrt 15),
a triangle with weights 1/3 and two isolated vertices. These points are not feasible, so they are not counterexamples, but no
strict certificate of either kind exists on a box containing them (strat12/verify_obstruction.py). STRAT13
(strat12_check/STRAT13_PROMPT.md) seeks a local lower bound near each limit, in the manner of the STRAT11 corner ball.
STRAT13 below closes them.

## STRAT13: collars at the nine equality limits

STRAT13 (strat13/, replay strat13/replay_all.py) closes the nine leaves. Near each limit it proves a local lower bound in a chart
that removes the eigenframe rotation at the repeated eigenvalue: with h = (x,y,k,p,q,v,z), B = (U+pX+qY, W+vX+zY),
K = [(1+x)/nu, k/nu; k/nu, (1+y)/nw] and S = B K B^T, the active edge weights are omega_ij = lambda/5 + S_ij with
lambda = (2 + tr S)/4. Farkas multipliers on the active edges give T >= ||h||_1/6 - M ||h||_1^2/2, hence T >= ||h||_1/12 for
||h||_1 <= 1/384 (two edges of weight 1/2, M = 32) and ||h||_1 <= 1/648 (triangle of weights 1/3, M = 54). In matrix terms,
T6(S) >= ||S - S_P||_max/24 on the feasible punctured balls of radius 1/15360 and 1/27864. Outside the collars the nine boxes are
split again and certified as in STRAT12: 366 positivity leaves, 216 exclusion leaves, 17 collar leaves, 590 splits, depth at most
72 below the STRAT12 box, no open leaf (strat13/collar_verification.json).

replay_all.py replays STRAT12 in full, every premise of the original STRAT10 cover (the complete partition, 40,177 splits), and
verify_collars.py, all in exact arithmetic (strat13/replay_all.out).

## Independent checks of STRAT13

strat13_check/my_collar_check.py rebuilds, at random rational points of every collar leaf and with its own code, the gap matrix
G = 2R/D, the invariant F(G) from the projector onto range(G), and the inverse map to the chart. It checks target(p) =
20 D^2 Delta F(G) exactly, the chart reconstruction B K B^T, the edge identity t + R_ij = (D/2) omega_ij, and at feasible points
T6/(20 D^2 Delta) >= ||h||_1/12. On the final cover, 25 points in each of the 17 collar leaves: 425 of 425 pass every identity,
no failure (strat13_check/my_collar_check.out). strat13_check/my_chart_stress.py samples the feasible cone of the active weights
in the chart up to the collar radius, 600 points per type, and checks the same bound: 600 of 600 for each type, smallest ratio
F/||h||_1 equal to 0.201 (two edges) and 0.245 (triangle) against the required 1/12 (strat13_check/my_chart_stress.out).

## Status

Region (11) at N = 6 is proved: the STRAT10 cover, the STRAT11 corner ball, the STRAT12 certificates and the STRAT13 collars
give T6 > 0 at every feasible connected point of the region (the nine centers have a disconnected carrier and are not
feasible), and every step is replayed exactly. The combined partition of the canonical root has 32,925 positive leaves,
20,277 exclusions, 17 collar leaves and 53,218 splits, with chart volume 1152 and no open leaf (strat13/RESULT.md). The endpoint
at scale E is covered, and the radial identity T6(a,ar) = (1-t^2) 9/80 + a(1-t) L6 + t^2 T6(E,rE), with L6 >= 3(1+r)/32, carries
positivity to every inward scale t = a/E < 1.

The statement is for N = 6: a five-vertex connected carrier with the gap representation of region (11) and one isolated vertex,
under the original (11) hypotheses as written in strat13/RESULT.md. The corresponding regions for N >= 7 and larger carriers are
open.
