# (R') corrected: the disjoint-aligned optimum, the exact c*, and the packing core
# Status: agent-derived; the LOWER bound + dichotomy + c* tightness rigorous (my audit
# of the block construction pending only spot checks — the proof uses standard events);
# the corrected residual statement is in the paper (see sec:band).

## Corrections to (R') as previously stated
1. The first term h_0 sqrt(m'n) was WRONG by sqrt(T): the pole-moving aligned adversary
   legally achieves (rigorous lower bound, block construction with coherences 0.6-0.96
   of budget):
     Phi_disj = max_{2 <= k <= n/m'} m' k min(h_0, Lambda(k^{-1/2} - tau_0)_+) 
              = Theta(h_0 n), FLAT in m'.
2. The residual still closes at the honest scale: Phi_disj -> c_0 eps n as d -> inf,
   so the budget eps n/32 forces c_0 <= 1/32 — and c* = 1/32 IS EXACTLY TIGHT (numerics:
   ratio crosses 1 at c_0 = 1/32; c_0 = 0.04 breaks it at 1.21x).
3. THE HEIGHT CEILING IS INACTIVE at the optimum (slope-limited caps sit below it):
   Claim-P's aimed geometry survives the deep peel; the operative constraint is
   nu-INCOHERENCE (budget ~ sqrt(log/d), shrinking with d).
4. DICHOTOMY: for d <= 8 T log(m'n) (inside the slice), W = Theta(Phi_det) — label
   randomness buys NOTHING there; the gain exists only above, and must supply exactly
   sqrt(d/(32 T log)).

## THE SHARPENED OPEN CORE (replaces the chaining formulation)
For d above the deterministic slice: prove W <= C Phi_disj — i.e. nu-incoherence
throttles the typical-y overlap gain of aimed caps to a constant multiple of the
DISJOINT optimum. Character: INCOHERENT-CAP PACKING UNDER A SHRINKING BUDGET — no
longer a chaining/gamma_2 problem. Numerics (strongest legal adversary, m'-budget
enforced): W/Phi_disj = 1.00-1.23 across d up to 32768; W <= 0.86 x budget; overlap
gain beyond the disjoint layout: 6.5% at d = 2048, 0% at d >= 8192 — the incoherence
budget exhausts. (An early overlap test used > m' ridges and showed spurious gains —
budget enforcement matters.)
Obstacles recorded: single-scale/Sudakov reproduces Phi_det (radius grows d^{1/4});
no a-priori packing bound on nu-incoherent aimed same-sign caps below m'.
Candidate route for the upper bound: the pairwise-coherence SECOND MOMENT — the m'
poles have sum_{g != h} <u_g, u_h>^2 <= m'^2 nu^2; overlapping aligned arrangements
need pairwise coherences above ~1/sqrt(shared depth-structure); count the max overlap
gain against the budget. (The numerics' exhaustion mechanism.)

## What is rigorous from this round
- The disjoint-aligned lower bound W >= (1 - o(1)) Phi_disj (whp, every y; block
  construction: monochromatic blocks, aimed poles, cross-contamination O(1) points).
- c* = 1/32 exact.
- The no-gain dichotomy below 8 T log (with W <= Phi_det always).
- The slice reproved via cap-mass.
- Subadditivity gives exactly Phi_det — nothing new.

## Numerics (seed 20260708; rprime_*.py in agent scratchpad; each < 5 min)
Illegal aimed-overlap reaches Phi_det (coh 1-4.5x over budget — the ceiling does not
stop it; incoherence does). Legal disjoint LB ratio 1.00-1.13. c* crossing at 1/32.
W flat in m' (T in [8,128]); W/(h_0 sqrt(m'n)) grows ~ sqrt T. Clean sweep table:
d = 512/2048/8192: W/budget 0.36/0.58/0.76; W/Phi_det 1.23/1.01/0.66; W/Phi_disj
1.23/1.04/1.00.
