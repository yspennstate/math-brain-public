# Read-once formulas: the sharp Fourier entropy-influence constant, a computer-assisted theorem, and what the numerics say about full FEI

21 September 2026. Full FEI remains OPEN / NOT PROVED. What is proved here is the conjecture on a subclass, with an
explicit constant that is sharp to within 3e-3, together with a set of exact and numerical facts about the general
case that any new attempt should know. Everything below was produced on one laptop between 20 and 21 September
2026; the scripts, the certificate data and the run logs are in `code/` and `data/` next to this file. Notation
follows Hod (2017): true = -1, Pr[f] = Pr[f = true], h = binary entropy in bits, V_p = 4p(1-p), H = spectral entropy
(entropy in bits of the spectral sample S, Pr[S] = f-hat(S)^2), I = total influence = E|S|, I+ = I/V,
H+ = (H - h(V))/V.

## 1. The theorem

For every read-once formula f over AND, OR, NOT on independent uniform bits (fan-in two; larger fan-in is a
composition),

    H(f) <= 6.4573 I(f).

Hod's construction gives read-once formulas with H/I -> beta(1/2) = 6.4547837..., so the read-once constant C_RO
lies in [6.45478, 6.4573]. The bound published before this was 10 (Chakraborty, Kulkarni, Lokam, Saurabh; the
O'Donnell-Tan composition argument gives 2^{O(k)} for bounded-arity bases), as cited by Hod. Numerically
C_RO = beta(1/2) exactly: value iteration on fine grids gives 6.454794 at 600 points, and a Pareto search over all
read-once formulas, exhaustive and annealed searches over self-similar recursive systems with one to three symbols
and gates of two and three inputs, and the fan-in-three check of section 5 all reach 6.4547837 and nothing above it.
So the working conjecture is: Hod's construction is extremal for read-once formulas over every gate of fan-in at
most three, and the sharp constant of that class is beta(1/2).

The proof has two parts: a reduction of the whole class to one inequality in two real variables (section 2, a
complete proof), and a certificate for that inequality verified with interval arithmetic (section 4).

## 2. The reduction

Composition through a gate. Let a, b be Boolean functions on disjoint variable sets with Pr[a] = p, Pr[b] = q, and
g = AND(a, b). By the composition lemma (O'Donnell-Tan 2013, Prop. 3.2; Hod 2017, Lemma 3.1) with the biased Fourier
transform of AND at the biases 1-2p, 1-2q,

    I(g) = It_a I+(a) + It_b I+(b),      H(g) = It_a H+(a) + It_b H+(b) + Ht_AND(p, q),

where (a direct computation, checked against the general biased transform and against brute force on formulas with
up to 17 variables, error 2e-15)

    It_a = q V_p,   It_b = p V_q,   w_empty = (1 - 2pq)^2,   w_ab = w_empty + It_a + It_b - 1,
    Ht_AND(p, q) = phi(w_empty) + phi(It_a - w_ab) + phi(It_b - w_ab) + phi(w_ab),   phi(w) = w log2(1/w).

Since It_a I+(a) = q I(a) and It_b I+(b) = p I(b): I(AND(a, b)) = q I(a) + p I(b). OR(a, b) is the negation of
AND(not a, not b); negation of a function or of its inputs changes neither H nor I, so OR(a, b) has the H and I of
AND(a', b') with Pr[a'] = 1-p, Pr[b'] = 1-q.

Proposition. Let C > 0 and let Gamma: (0,1) -> [0, inf) satisfy Gamma(p) = Gamma(1-p) and, for all p, q in (0,1),

    (A)   Gamma(pq) <= q (Gamma(p) + h(V_p)) + p (Gamma(q) + h(V_q)) - Ht_AND(p, q).

If Gamma(1/2) <= C, then every read-once formula f over AND, OR, NOT satisfies H(f) <= C I(f) - Gamma(Pr[f]) <= C I(f).

Proof. Induction on the formula. A variable: H = 0, I = 1, Pr = 1/2, and 0 <= C - Gamma(1/2). NOT preserves H and I
and maps p to 1-p; Gamma is symmetric. For g = AND(a, b) with H(a) <= C I(a) - Gamma(p) and H(b) <= C I(b) - Gamma(q):

    H(g) = q V_p H+(a) + p V_q H+(b) + Ht_AND
         <= q (C I(a) - Gamma(p) - h(V_p)) + p (C I(b) - Gamma(q) - h(V_q)) + Ht_AND
         = C I(g) - [ q (Gamma(p) + h(V_p)) + p (Gamma(q) + h(V_q)) - Ht_AND(p, q) ]
         <= C I(g) - Gamma(pq)                                  by (A), and Pr[g] = pq.

OR follows from AND on the negated inputs and the symmetry of Gamma; Gamma >= 0 gives the last inequality.

Remarks. The constant does not enter (A); it enters only through Gamma(1/2) <= C. Conversely the extremal slack
Sigma*(p) = inf { C I(f) - H(f) : f read-once, Pr[f] = p } is admissible at the realised (dyadic) measures and
dominates every admissible Gamma with Gamma(1/2) <= C, so the smallest cap with Sigma* >= 0 is exactly C_RO; imposing
(A) for all real p, q is a relaxation in the safe direction. The potential is a function of the measure alone
because disjoint composition transforms spectra as products; that is exactly what fails for shared variables
(section 6).

An exact identity that made the verification tractable. Dividing (A) by pq, with G = Gamma/p, L = log2(1/.),
Psi(z) = phi((1-2z)^2)/z = (4/ln 2)(1-2z)^2 ell(2z), ell(u) = -ln(1-u)/u:

    (A)  <=>  Phi(p, q) = G(p) + G(q) - G(pq) - E(p, q) >= 0,
    E(p, q) = 8 p(1-q) L(p) + 8 q(1-p) L(q) + 8 (1-p)(1-q) + Psi(pq) - Psi(p) - Psi(q).

Every log2(1-p), log2(1-q) term of the four AND weights and the two binary entropies cancels (checked to 40 digits).
E -> b* = 8 - 4/ln 2 = 2.2292198 as p, q -> 0, and e(q) = lim_{p->0} E = 8 q L(q) + 8(1-q) - Psi(q), with e(1/2) = 8.

## 3. Lower bound and the shape of the extremal potential

Hod's construction F_{m+1} = (F_m AND F_{m+1})^dual, iterated from a single variable, is read-once with
lim H/I = beta(1/2) = S(1/2) = 6.4547837..., S(z) = sum_{j>=0} h(q_j) q_1...q_j/(1-q_j), q_0 = z, q_{j+1} = 1/(1+q_j).
For any read-once seed with (p, I, H) the same construction gives lim H/I = (H - h(V_p) + V_p S(p))/I, so the extremal
slack obeys Sigma*(p) >= V_p S(p) - h(V_p) =: Gamma_H(p) whenever C_RO = beta(1/2). Gamma_H itself is not admissible
(minimum violation of (A) 0.00075 near p = q = 0.908), nor is the lexicographic slack (fails by 0.10 near
p = q = 0.665): the extremal potential is the fixed point of the value iteration, not a closed form. It equals the
AND-chain slack at every dyadic p = 2^-k, has a downward cusp at 1/2 (G = Gamma/p has slope 30 in x = log2(1/p) just
below p = 1/2), and Gamma(p)/p - 2(C-4) log2(1/p) tends to 8 - 8/ln 4 = 2.229 with a bounded log-periodic wobble at
non-dyadic small p. The tight set of (A) is: the fresh-variable line q = 1/2 and its dyadic relatives q = 2^-k, the
strip p -> 1/2- with q -> 1 (and its mirror), and the arc pq = 1/2 near p = q = 0.71 where the cap at 1/2 is active.
Along AND chains (A) is tight to first order: both the p log(1/p) and the constant term cancel exactly, so no
verification can rely on absolute margins near p = 0.

## 4. The certificate

Candidate. Gamma_hat(p) = p G_num(x) + c p(1-p) on p <= 1/2 (x = log2(1/p)), mirrored to p > 1/2; G_num is piecewise
linear in x through the nodes of a value iteration run in the exact representation of section 2 (`fei_cert_vi.py`:
uniform step 2^-11 in p on [1/32, 1/2], M = 24 nodes per octave down to 2^-40, every dyadic a node, C0 = 6.4548,
converged in 120 iterations, reproducing the AND-chain slack at every dyadic to six digits); linear tail of slope
(G_J - b*)/K so that G(x) + G(y) - G(x+y) = b* in the tail. The margin term c p(1-p) raises the slack of (A) by
c(1-p)(1-q) everywhere (in the units of Phi) at the price of Gamma_hat(1/2) = C0 + c/4; the theorem constant is
6.4548 + 0.01/4 = 6.4573 at c = 0.01. (The earlier form c min(p, 1-p) fails when both p, q > 1/2.)

Verification (`fei_cert.py`, `fei_cert23.py`; numpy float64 with nextafter outward rounding after every operation,
8-ulp padding on log2, log1p, exp2, the primitives checked against 90-digit mpmath on 9,000 random cells with no
failure). Coverage of (0,1)^2:

- region 1, p, q <= 1/2: adaptive cells in (x, y) with directional splitting; the enclosure bounds G(p), G(q), G(pq)
  and E from separate ranges (it does not keep the cancellation in G(x) + G(y) - G(x+y), which is what limits c);
- region 2, p <= 1/2 < q, v = 1-q: Phi/v with mean-value forms [G(x) - G(x+L(1-v))]/v = -(ell(v)/ln 2) G'(xi) and
  [Psi(p(1-v)) - Psi(p)]/v = -p Psi'(zeta), plus the direct forms, taking the best lower bound;
- region 3, p, q > 1/2, u = 1-p <= v = 1-q, w = u+v-uv: Phi/u with Lambda(z) = Gamma_hat(z)/(1-z),
  [Lambda(v) - Lambda(w)]/u = -(1-v) Lambda'(xi), and a split at pq = 1/2 through m = 1-2v = -expm1((1-y') ln 2);
- tails: (T1) both p, q < 2^-K: Phi = b* + c(1-p)(1-q) - E with E - b* <= (16K + 19) 2^-K; (T2), (T3) one variable
  below the grid: one-dimensional conditions using E - e(q) <= p [8(1-q) L(p) + 12/ln 2]; three constant lemmas
  for measures beyond the grid in regions 2 and 3.

Result at c = 0.01 (`run_cert_all.py`, six separate processes, logs in `data/cert_h24_c001_*.out`, summary
`data/cert_h24_c001_SUMMARY.json` with all_ok = true):

    lemmas   T1 margin +0.010; region 2 beyond the grid +120.5; region 3 beyond the grid +7.98; both deep +7.08
    T2       depth 5 (1,800 cells at depth 0, 72 at depth 5, minimum lower bound +2.6e-3)
    T3       depth 2 (1,800 cells, minimum +1.7e-3)
    region 1 depth 13 (1.62M cells at depth 0, 32.7M at the widest level, 2 cells still failing at depth 12; 951 s)
    region 2 depth 22 (3.24M cells at depth 0, 19.7M at the widest level, minimum +9.6e-4; 4,978 s)
    region 3 deepest level 28 (1.66M initial cells, 23.3M evaluated in memory-bounded batches; 280 s)

The same run at c = 0.05 gave 6.4673 first. Cross-check: at 6,750 random points evaluated in 40-digit arithmetic the
interval lower bounds never exceed the true normalised values (the float64 version of that test falsely reports
violations up to 0.05 where Phi is divided by a tiny v or u, its own rounding). Assumptions: IEEE double arithmetic
with correctly rounded +, -, *, /; numpy log2, log1p, exp2 within 8 ulp.

What limits the constant. (i) The candidate's violation of (A) between its nodes: 6.1e-3 (units of (1-p)(1-q)) for
M = 24, 2.2e-3 for M = 96, both sitting in the uniform part next to p = 1/2; so M = 96 alone reaches about 6.4554 and
a finer grid near 1/2 about 6.4551. (ii) The region-1 enclosure has width about 20h for a cell of side h whatever the
margin, so below c = 0.01 the refinement explodes (150M live cells and 15 GB at c = 0.003 before it was stopped). The
cure is an enclosure that keeps the cancellation: G is piecewise linear in x, so on a cell inside one linear piece
the exact minimum of G(x) + G(y) - G(x+y) is at a corner, and E can be enclosed by a mean-value form of width O(h).
With that and the M = 96 candidate the machinery should certify about 6.4554. Closing the last 6e-4 to beta(1/2)
itself would need an exact description of the fixed point, which is open (section 7, approach 9).

Update, 21 September, 14:2x. The cure named in (ii) is implemented (`code/fei_cert_r1x.py`) and cross-checked
(`code/crosscheck_r1x.py`, log `data/crosscheck_r1x_h24_c001.out`). On a cell whose x and y sides each lie in one
segment of the node grid, the piecewise-linear part G_num(x) + G_num(y) - G_num(x+y) is linear on every piece of the
cell's subdivision by the lines x + y = node, so its minimum is at a vertex of that subdivision (a corner, or a point
where such a line meets an edge); the vertices are evaluated with one-ulp interval coordinates, which is exact to
rounding. The margin term c(1-p)(1-q) is monotone in each variable, so its minimum is at a corner. E is bounded by
the smaller of its interval evaluation and the mean-value form E(centre) + rx max|dE/dx| + ry max|dE/dy|, with
dE/dx = p[8(1-q)(1 - x ln 2) + 8qy ln 2 + 8(1-q) ln 2 - Psi'(pq) q ln 2 + Psi'(p) ln 2]. A second bound is the centred
form Phi(centre) - rx max|dPhi/dx| - ry max|dPhi/dy|, the derivative enclosed over the cell with the slope of x's
segment and the slope range of the segments met by x + y (Phi is Lipschitz, so the mean-value inequality holds with
the essential supremum); the cell's bound is the larger of the two. On 251 random cells of widths h to h/32 the bound
is never above the true value at 1,993 points evaluated at 40 digits, its slack (sampled minimum minus bound) has
median 7.7e-6 and maximum 1.8e-2 against 0.10 and 0.41 for the bound above, and with the margin set to c = -0.2, a
control that has to fail, every one of the 247 cells whose sampled Phi is negative is flagged and none is bounded
above its true value. Region 1 then verifies at c = 0.01 on the M = 24 candidate in 557 s at deepest level 6
(`data/r1x_h24_c0.01.log`; the old bound needed 951 s and depth 13) and at c = 0.003 on the M = 96 candidate in
2,066 s at deepest level 9 with 9.5M cells evaluated (`data/r1x_h96_c0.003.log`), where the old bound had 108M
cells still failing at depth 9 after 2,846 s. Region 3 followed at the same margin with the section-9 bound:
verified in 2,900 s, 9.42M initial cells, 118M evaluated, deepest level 27 (`data/cert_h96_c0003_R3x.out`; note that
log's closing line reads "ALL VERIFIED" because that process ran region 3 alone, so it is not a statement about the
other parts). The lemmas, T2 and T3 pass at c = 0.003 on this candidate as well. Region 2 does not: run to depth
30 it stops at the degenerate cell x = 4.000000, v = 1.584632 with bound -9.949e-04
(`data/cert_h96_c0003_R2x.out`, closing line `RESULTS: {'R2': False}`). A cell of zero width is enclosed exactly
up to rounding, so that value is the candidate's own violation of the region-2 inequality at that point rather
than slack in the bound: the M = 96 candidate does not support c = 0.003, and the constant of the theorem stays
6.4573 at c = 0.01. Closing the margin needs a better candidate, not a better bound.

Region 2 carries the same lost cancellation, and the same cure. Its A term is [Ghat(x) - Ghat(x+lam)]/v with
lam = v ell(v)/ln 2, and a term-by-term measurement of the bound's width on the failing cells (`code/probe_r2_terms.py`,
`data/probe_r2_terms.out`) puts 83 per cent of it in that one term, with the direct form (a difference of two
separate ranges of G) chosen on every failing cell because the mean-value form is sixty times wider there. Writing
Ghat(x) - Ghat(x+lam) = D(x, lam) + c p (2^-lam - 1) with D = G_num(x) - G_num(x+lam), and relaxing lam to its range
over the cell, D is piecewise linear on the rectangle cut by the diagonals x + lam = node, so its enclosure is the
extremes over the vertices: the corners and where each diagonal meets an edge (`code/fei_cert_r1x.py`, D_enclose and
phi2_over_v_lower_exact). On 400,000 random node cells at c = 0.003 this takes the failing fraction from 7.8 to 3.5
per cent and the worst bound from -8.16 to -0.28, and it is never below the old bound because the result is the best
of the three forms. That improvement is real and is not enough at this margin: the cells that survive it
are the ones where the candidate itself is short, which is where the run above stops. Cross-check (`code/crosscheck_r2x.py`): on 400 cells and 2,800 points at 40 digits the bound is
never above the true value, the D enclosure contains the truth on a 25x25 grid of every rectangle, and the
negative-margin control at c = -0.2 flags every cell whose sampled Phi/v is negative without ever bounding one
above its truth.

The next floor is the candidate's own residual of 2.2e-3 between its nodes, which sits next to p = 1/2 on the lines
q = 2^-k; `fei_cert_vi.py` now takes a refinement factor for the uniform part of the grid there, and a four times
finer candidate (`fei_cert_vi.py 96 40 6.4548 h96k40_f4 2000 4`, 7,201 nodes) is being built.

## 5. Fan-in three

The induction closes for a k-input gate G exactly when
Gamma(p_out) <= sum_i It_i(G; p) (Gamma(p_i) + h(V_i))/V_i - Ht_G(p) for all input measures. With Gamma the AND/OR
fixed point, all 218 nondegenerate 3-input gates satisfy this on a 33^3 grid of measures in [0.02, 0.98]; the
smallest value is -0.00002, attained only by gates that reduce to a two-input gate on a fresh variable
(`fei_gate3_check.py`). So numerically the sharp constant is the same for read-once formulas over every gate of
fan-in at most three, with Hod's two-input construction extremal in the larger class. This is not yet rigorous.

## 6. What the numerics say about full FEI

These are exact computations (Walsh spectra in double precision, entropies in bits) on the general problem, done
while looking for a potential that could carry an induction over restrictions instead of compositions.

The restriction identity. For a coordinate i, with p_0, p_1 the spectral distributions of the two restrictions
(on sets not containing i) and m = (p_0 + p_1)/2, the parent law satisfies p(S) + p(S u i) = m(S) exactly, hence

    Delta_i H := H(f) - (H(f_0) + H(f_1))/2 = JS(p_0, p_1) + sum_S m(S) h(p(S u i)/m(S)),

where JS is the Jensen-Shannon divergence, i.e. the mutual information between the bit x_i and the spectral sample
of the restricted function. Since sum_S m(S) h(.) <= h(Inf_i) by concavity and JS <= 1 bit,
Delta_i H <= 1 + h(Inf_i) <= 2 bits for every coordinate (checked on 79,200 function-coordinate pairs, maximum
violation 4e-16). This is the mechanism behind the Wan-Wright-Wu average-decision-tree-depth theorem, and it says a
potential-free induction over restrictions can only fail through coordinates of small influence.

The potential-free step. Define rho_0(f) = min over relevant coordinates of Delta_i H / Inf_i. If sup_f rho_0(f) = C
were finite, FEI would follow with that constant by induction. Measured: over all functions of at most 5 variables
(2^32 functions, exhaustive) the supremum is 4.8677, attained by the three-variable one-point flip with dummy
coordinates; one-point flips give 4.00, 4.87, 4.74, 4.51, 4.32, 4.19 at n = 2..7; hill climbing found 5.1949 at
n = 6 (a Hamming ball of radius one plus a perfect matching at distance two; its H/I is only 3.31, so the hard
functions for the step are not the hard functions for the ratio); tribes of width 2 (AND of s ORs of disjoint pairs)
give 3.25, 4.15, 5.39, 5.78, 5.94, 5.997, 6.004, 5.987, 5.960 for s = 2..10, a maximum of 6.0037 at n = 16, every
coordinate equal; width 3 tops at 5.599, width 4 at 5.071, width 5 at 4.63, width 8 at 4.11 (`fei_step_tribes.py`,
closed form checked against brute force). So any potential-free scheme needs C >= 6.0 on this family alone, every
structured family tried is bounded, and nothing found grows without limit. Any scheme of this shape also needs
C >= beta(1/2) because of the read-once class.

Potentials that buy nothing. The package's simplest potentials Psi = K I psi(f) with
psi in {1 - max_S p_S, 1 - W^{<=1}, 1 - E[f]^2, I/n} do not help: on all 4-variable functions and on the n = 6 and
n = 7 record functions the delivered constant C_needed(K) + K is minimal at K = 0 for every psi (C falls by at most
0.35 per unit of K). A useful psi must decrease by more than Inf_i under the cheapest restriction of the hard
functions; none of the inspectable statistics does. The best-potential LP on a finite universe is vacuous
(Psi = C I - H is always admissible there), so the potential has to come from structure, not from an LP.

Other measured facts. The supremum of H/I over AND/OR chains is 4; over all functions of at most 5 variables the
maximum of H/I is 3.6237 (the one-point function); the best read-once ratio found by the Pareto search climbs
2.0, 3.40, 3.89, 4.40, 4.72, 5.07, 5.28, 5.51, 5.64, 5.79, 5.88, 5.98, ..., 6.30 and never passes beta(1/2).

## 7. Files

- `code/`: fei_chain.py (exact O(n) recursion for chains), fei_comp_search.py, fei_recsys.py, fei_recsearch_run.py,
  fei_recanneal.py, verify_record.py (materialised brute-force control), fei_readonce_dp.py / dp2.py (Pareto DP),
  fei_readonce_gamma.py, fei_readonce_gamma_geo.py, fei_readonce_gamma_dyadic.py (value iteration; the logit-linear
  dyadic version loses its deep tail below 2^-34 to cancellation, the cert_vi form does not), fei_hod_slack.py,
  fei_lex_slack.py, fei_gate3_check.py, fei_step_tribes.py, fei_cert_vi.py (the candidate), fei_cert.py and
  fei_cert23.py (the interval verification), run_cert_all.py (the six-part driver), scan_cmin.py (floating-point margin
  estimate), test_fei_cert.py (primitives against mpmath), crosscheck_mp.py (40-digit cross-check), check_tail_bounds.py,
  diag_r3.py, diag_r3b.py, time_cert23.py, the patch scripts that record each change to fei_cert23.py,
  fei_cert_r1x.py (the region-1 enclosure that keeps the cancellation; `python fei_cert_r1x.py <npz> <c> [depth]`),
  crosscheck_r1x.py (its 40-digit cross-check with the negative-margin control) and probe_r2_depth0.py (depth-0
  failure count of the region-2 bound at several margins).
- `data/`: cert_vi_h24k40.npz and cert_vi_h96k40.npz (the two candidates: xs, G, C, M, K), the c = 0.01 run logs and
  summary, the c = 0.05 region logs, gate3_check.json, the search logs and the N = 3000 bisection log,
  r1x_h24_c0.01.log and r1x_h96_c0.003.log (region 1 with the new enclosure), crosscheck_r1x_h24_c001.out and
  probe_r2_h24.log.
- To reproduce the theorem: `python fei_cert_vi.py` (or use the npz), then `python run_cert_all.py cert_vi_h24k40.npz
  0.01 60 h24_c001`; the six parts take about two hours on eight cores.
