# FEI: state of the attack (kept current; newest entry first)

## 2026-09-21 03:5x: a candidate theorem, the read-once FEI constant is Hod's beta(1/2)

For read-once formulas over AND/OR/NOT the composition lemma turns FEI into a one-variable functional inequality.
If Gamma: (0,1) -> [0, inf) is symmetric and for all p, q

    Gamma(pq) <= q (Gamma(p) + h(V_p)) + p (Gamma(q) + h(V_q)) - Ht_AND(p, q),      V_p = 4p(1-p),

then every read-once formula satisfies H(f) <= Gamma(1/2) I(f) - Gamma(Pr f) (induction over gates; OR is the dual
of AND, NOT preserves H and I). Value iteration on a 600-point grid (`fei_readonce_gamma.py`) finds the smallest
feasible Gamma(1/2) = 6.454794, against Hod's lower bound 6.4547837 from a read-once construction. So, up to the
discretization, the FEI constant restricted to read-once formulas is exactly beta(1/2) = 6.45478..., Hod's
limit-of-limits construction is extremal, and Gamma is the potential that proves it. Finer grids (1500, 3000) are
running; a rigorous version needs the inequality verified with interval bounds or a closed form for Gamma.
Independent evidence: every exhaustive and annealed search over self-similar recursive systems tonight tops out at
exactly 6.4547837 from many different systems, and the Pareto DP over all read-once formulas climbs toward it.

## 2026-09-21 02:4x-03:2x, goal "keep working on closing FEI, you can use the cpu"

**Frontier read from the papers themselves.** Lower bounds on the FEI constant: 60/13 (O'Donnell-Wright-Zhou 2011),
6.278944 (O'Donnell-Tan 2013, recursive composition of a balanced 6-variable function: the limit ratio of
f_m = F(f_{m-1}, ..., f_{m-1}) is H[F]/(I[F]-1)), 6.377444 = 4 + 3 log_4 3, 6.413846 and 6.454784 (Hod 2017, the
last two by biased composition of NAND at the golden-ratio fixed point and a "limit of limits"
F_{m+1} = (F_m AND F_{m+1})^dual). Upper direction: FEI holds for symmetric functions, read-once formulas over
bounded-arity gates (O'Donnell-Tan), read-k DNFs for the min-entropy version (Arunachalam et al. 2021); no general
bound better than the trivial H <= I log(en) + log(e(I+1)) is known to us.

**Tools built and validated here** (this folder):
- `fei_chain.py`: exact O(n) recursion for AND/OR chains (= lexicographic threshold functions): the state
  (E f, H, I) of x op g follows from that of g. Validated on 528 patterns against brute force (5.7e-14). Consequences:
  sup of H/I over all AND/OR chains is 4 (AND_n approaches it); the 4.87 min-step and 5.14 total-step constants
  of chains never approach Hod's numbers; l<2/3> = (2/3, 4/3, 2 log2 3) and l<Phi> = (1.2976895, 2.4239396) exactly
  as in Hod.
- `fei_comp_search.py`: the biased composition objective R(F, g) = H_g/I_g + (V Ht[F] - It[F] h(V)) / (I_g (It[F] - V))
  at a self-consistent bias p (Pr_p[F] = p), base g = l<p>. Reproduces 6.413846 for NAND2 to six digits. Exhaustive over
  all 3- and 4-input composers: nothing above NAND2; annealing at 5-8 inputs: nothing above it either.
- `fei_recsys.py` + `fei_recsearch_run.py`: general recursive read-once systems (symbols wired to fresh variables,
  previous-level copies, or same-level copies = Hod's inner limit), evaluated by the vector-bias composition lemma
  level by level. Reproduces Hod's beta(1/2) = 6.4547837 to seven digits from a single variable. Exhaustive over
  one-symbol systems with 2-input gates: the record is exactly 6.4547837 (NAND / NOR with one prev and one cur input).
  3-input one-symbol systems and two-symbol 2-input systems: running (background workers, logs recsearch_*.jsonl).
- `verify_record.py`: positive control that materializes the finite functions of a system and brute-forces H, I.

**What the step statistics say (09-20/21).** The potential-free induction step needs 4.8677 on every function of
<= 5 variables, 6.0037 on width-2 tribes at 16 variables, and any inductive scheme needs at least sup H/I >= 6.4548.
The "best potential" LP on a finite universe is vacuous: Psi = C I - H is always admissible, so finite LPs return
max H/I on the universe; a potential route is exactly as hard as FEI unless the potential is restricted to a fixed
feature family (the 09-20 four simple potentials all failed to lower the constant).

**Open threads being pursued.** (1) beat 6.4547837 with two-symbol or 3-input recursive systems (a new record lower
bound would be a publishable computational note); (2) restricted-feature potential LP across n = 4..8 hard functions
to see whether any feature family holds the step constant flat in n; (3) the total-step identity
sum_i Delta_i H = sum_i JS_i + sum over spectral-cube edges w_e h(q_e) as a route to an amortized argument.

## 2026-09-21 04:5x - the constant survives every 3-input gate; the edge is tight to first order

- fei_gate3_check.py: with Gamma the AND/OR fixed point (N = 600, C = 6.4548), the k-input induction condition
  Gamma(p_out) <= sum_i It_i (Gamma(p_i) + h(V_i))/V_i - Ht_G holds for all 218 nondegenerate 3-input gates on a
  33^3 grid of input measures; smallest value -0.00002 (grid noise), and only on gates that reduce to a 2-input gate
  on a fresh variable. So the read-once constant over gates of fan-in <= 3 is (numerically) still beta(1/2).
- fei_readonce_gamma_geo.py, hybrid grid (24/octave down to 2^-14 both sides + uniform 1/2000 middle, 2,321 points):
  feasible at C = 6.4548; Gamma/p - 2(C-4) log2(1/p) at p = 2^-k reads 8.0, 8.0, 6.26, 4.78, 3.88, 3.28, 2.90, 2.68,
  2.55, 2.48, 2.44, 2.42, 2.41, 2.20 (k = 1..14), against the AND-chain constant 8 - 8/ln 4 = 2.229. The p log(1/p)
  and constant terms cancel exactly along AND chains, so a rigorous check needs a margin device (THEOREM_NOTE §6).
- N = 1500 uniform bisection finished: threshold in (6.454782, 6.454788]; N = 3000 still bisecting (6.5625 feasible,
  6.375 not).

## 2026-09-21 05:0x-06:3x - the rigorous certificate is built and its pieces pass at c = 0.05

- Exact rewriting of (A): Phi = G(p) + G(q) - G(pq) - E with E = 8p(1-q)L(p) + 8q(1-p)L(q) + 8(1-p)(1-q) + Psi(pq)
  - Psi(p) - Psi(q), Psi(z) = phi((1-2z)^2)/z (checked at 40 digits). E -> b* = 8 - 4/ln2 in the corner.
- fei_cert_vi.py: value iteration in the certificate's own representation; the M = 24, K = 40 candidate converges in
  120 iterations at 6.4548 and matches the AND-chain slack at every dyadic to six digits down to 2^-40 (the old
  logit-linear code lost the tail below 2^-34 to cancellation, so its deep values were wrong).
- fei_cert.py / fei_cert23.py: interval verifier (outward rounding, 8-ulp padding, mpmath-checked primitives), three
  regions with adaptive cells and mean-value enclosures, two one-dimensional tail checks, four constant lemmas.
  At c = 0.05 (constant 6.4673): lemmas OK, T2 OK, T3 OK, region 1 OK on the first candidate; regions 1-3 on the new
  candidate running. Interpolation error bounds this candidate at about c = 0.007 (6.4566); M = 96 candidate running.
- Known read-once constant before this: 10 (Chakraborty-Kulkarni-Lokam-Saurabh; O'Donnell-Tan, as cited by Hod).

## 2026-09-21 06:5x - THEOREM: H <= 6.4673 I for every read-once formula (computer-assisted)

All six parts of the certificate pass at c = 0.05 on the M = 24, K = 40 candidate (THEOREM_NOTE section 8).
Region 2 needed 17 directional levels (26 min), region 3 needed 22 (84 s) once the split axis was chosen from the
widths of the enclosures actually used; splitting both axes had doubled the failing count every level.  Sharper runs:
c = 0.01 (6.4573) in progress on the same candidate; the M = 96 candidate is still iterating (starved on a saturated
box).  Independent consistency test: at 1,500 random sub-cells per region and three points each, the interval lower bounds of regions 2 and 3 never exceed the true normalised value evaluated in 40-digit arithmetic (crosscheck_mp.py; the float64 version of the same test, crosscheck_bounds.py, reports false violations of up to 0.05 wherever Phi is divided by a tiny v or u - its own rounding, not the certificate's).

- 07:0x: the M = 96 candidate converged (feasible at 6.4548, dyadic values identical to M = 24); scan_cmin.py puts its needed margin at 2.2e-3 (not 16x smaller than M = 24's 6.1e-3): the residual violations sit at p = 0.44 on the q = 2^-k lines and at p -> 1/2- with q small, i.e. in the uniform 2^-11 part of the grid, which M does not refine. Certificate at c = 0.003 (constant 6.4556) launched; c = 0.01 on the M = 24 candidate has lemmas, T2, T3, R1 done and R2 at depth 4.

- 07:4x: the M = 96 run at c = 0.003 was stopped - region 1 had 150M live cells at depth 8 (15 GB, box commit at 81 of 95 GB) and 95M still failing: the decoupled region-1 bound has width ~20h (h the cell size) everywhere, so a margin of 3e-3 asks for h ~ 4e-5 across the whole tight band and the cell count is infeasible. The driver is now memory-bounded (depth-first batches, at most ~2 x 4M live cells; region 3 at c = 0.05 re-verified in 56 s). Margins below ~0.01 need a sharper region-1 enclosure (exact piecewise-linear minimum of G(x)+G(y)-G(x+y) over the cell plus a mean-value form for E), not more cells; c = 0.01 (6.4573) continues on the M = 24 candidate.

## 2026-09-21 08:1x - THEOREM sharpened: H <= 6.4573 I for read-once formulas
- run_cert_all.py cert_vi_h24k40.npz 0.01 60 h24_c001: all six parts OK (lemmas; T2 depth 5; T3 depth 2; region 1 depth 13
  in 951 s; region 2 depth 22 in 83 min; region 3 deepest level 28 in 280 s).  THEOREM_NOTE.md section 9 has the figures.
- Memory readonce_fei_theorem_6_4673_computer_assisted_2026_09_21 updated to 6.4573 (index line too).
- The disk copies of THEOREM_NOTE.md and README.md were missing at 08:1x: the dream's git sync (07:45) removed untracked
  files identical to the incoming tracked ones, was then refused the checkout move, and left them deleted.  Restored from
  main (byte-identical); the sync script is being fixed to put such files back when the move is refused.
- Next for a sharper constant: the cancellation-keeping region-1 enclosure (exact corner minimum of the piecewise-linear
  part plus a mean-value form for E) and the M = 96 candidate at c about 0.003; expected about 6.4554.

## 2026-09-21 14:2x - region-1 enclosure rebuilt to keep the cancellation
- fei_cert_r1x.py (exact piecewise-linear minimum over the cell's subdivision vertices, corner minimum of the margin term,
  mean-value E, centred form of Phi) and crosscheck_r1x.py (40-digit soundness, dense-grid tightness of the PL part, and a
  negative-margin control that must and does fail): CROSSCHECK PASS; the control found the c > 0 assumption in the margin
  term, fixed to a corner minimum.  Median slack 7.7e-6 against 0.10 for the decoupled bound.
- M = 24, c = 0.01: region 1 verified in 557 s at deepest level 6 (the old bound: 951 s, deepest level 13).
- M = 96, c = 0.003: VERIFIED in 2,066 s: 9.33M node cells, 9.50M cells evaluated, deepest level 9 (the decoupled bound had 108M cells still failing at depth 9 after 2,846 s when it was stopped); region 3: running at the time of writing with the section-9 bound (deepest level 27, 68M cells evaluated after 1,722 s); region 2: running at the time of writing with the section-9 bound (started 14:16).
- With region 1 no longer the bottleneck, the constant at c = 0.003 is 6.45555 once regions 2 and 3 confirm at that margin (their lemmas, T2 and T3 already passed at c = 0.003 on the M = 96 candidate, cert_h96_c0003_SUMMARY.json); the next step is a candidate with a finer grid next to p = 1/2, where the M = 96 residual of 2.2e-3 sits, to bring c below 0.001.
