# FEI, Opus routes: synthesis

12 Oct 2026, 16:36 (claude-6bb7036b-s07, recovery stream for this workflow). Sources: each route's NOTES.md,
CLAIMS.json and REFEREE.md in this folder. Statuses are the routes' own; the referee column is the verdict of the
independent pass in that route's REFEREE.md.

The Fourier entropy-influence conjecture is open. No route proves it. What the routes did is prove FEI with explicit
constants on several proper classes, reduce FEI to a few sharp equivalent forms, and kill a number of proof methods
with explicit witnesses. Read together, the obstructions point at one missing object, described in section 3.

Notation shared by the routes: p(S) = fhat(S)^2 is the spectral sample, H its entropy, I = sum_i Inf_i(f).
B = sum_i H(S_i | S - i). U(f) = sum_S p(S) log2(pi(S)/p(S)) with pi(S) = sum_{T contains S} p(T).


## 1. Route by route

A2, two spectral addresses (class K2: all conditional row laws product). PROVED and CONFIRMED: H <= 4I on K2
(A2-T-A); the optimal constant on K2 is c* = 16/3 - (3/2) log2 3 = 2.95589, attained by the 3-variable AND
(A2-T-S, computer step certified twice by different rigorous algorithms); signed-character selectors with any number
of address coordinates satisfy H <= 4(I - Inf_y), sharp (A2-C-sel); the address ladder C_k is nondecreasing with
supremum C_FEI (A2-H-ladder). Evidence: three addresses at n = 5 give max H/I = 3.4025 = AND_4. Referee erratum: the
refuted even-weights shortcut fails by +0.0320 at rho = 3 with e odd, and for e even it works at rho = 3, 4, 5 (the
route had +0.0295 for every rho >= 3). The Codex fleet agent A032 reached the same sharp constant independently
(its n = 6 run); novelty against the literature is not checked.

BT, biased weighted thresholds under product laws. PROVED and CONFIRMED: an exact termwise identity for E_mu and
Delta_mu (BT-3); alpha ln(1/alpha) <= sum_i q_i ln(1/q_i) rho_i for increasing T (BT-4, p-biased case is Kahn-Kalai
2007); E_mu <= Var ln(1/Var) + A_0 I_mu with A_0 < 9.21 nats for every weighted threshold and product law (BT-6);
FEI+ under a bias floor delta (BT-7). REFUTED and CONFIRMED, but already in the campaign source biased.tex: BT-1, BT-2.
The referee refuted the level-wise reference conjecture (LCR, BT-10) with a new family, anti-diagonal tribes
thresholds, on which every product reference loses (1/2) ln m per unit influence. Open: BT-8 (uniform over all product
laws, no floor) and BT-9 (the supremum of H+/Delta is the AND/OR value 2 + 4/ln 2 = 7.7708).

SEL, selector interference. PROVED and CONFIRMED: the multiplexer cost identity cost(F) = H(S|T) + I(X;Y) with the
closure constant K(c), K(1/2) = 4 (SEL-1, SEL-2); the bent point-flip multiplexer closed forms (SEL-3, unboundedness
already in X009); orthogonal-neighbour closure fails under reuse, H(G) = 57/4 > 4 I(G) (SEL-6); random re-signing
(SEL-14); balanced two-cell selectors (SEL-15); the affine-partition joint strategies (SEL-9 to SEL-12). REFUTED and
CONFIRMED with 60-digit intervals: the sharp orthogonal-leaf bound SEL-8. Open: SEL-8' and the Schmidt-entropy defect
SEL-13 with kappa_0 = 0.756151564; the referee found that float64 and 30-digit searches manufacture values above
kappa_0 which disappear at 60 digits, so any search for a counterexample must run at 60 digits or more.

U, universal reductions. PROVED and CONFIRMED: the constant sandwich K_loc <= K_E <= C_FEI <= K_Delta <= K_loc + 2/ln 2
(U-A); the profile of an extremizer (U-C, n >= 2); FEI iff H <= A(I + DTC) (U-C1); FEI iff every ratio-critical f
with all influences <= 1/2 has a relevant coordinate with H(S_i | S_-i) <= K Inf_i (U-C2); |fhat(S)| <= 2^{|S|-1} I_S
(U-Gkey); Theorem G, H <= 2(I - Var) + 2U, so FEI iff sup U/I < infinity (U-G); the restriction identity for Delta_i U
(U-loc); the GU reduction (U-GU-implies-FEI). The quantum meta-obstruction U-Q (Slote): an argument all of whose steps
hold for quantum Boolean functions cannot prove FEI. Open: GU, sum_i Delta_i U <= K I (K about 3.1). Evidence against
the local form Delta_i U <= K Inf_i (max ratio 4.78, 5.11, 5.48, 6.15 at n = 6..9). Novelty not checked.

W, witness cost. PROVED and CONFIRMED: exclusive unions (W-L1), the witness-sum lemma (W-L2), the exact spectrum of
selector trees (W-P41), the direct spectral bound H <= 10.38 I on that class (W-C71), the owner mass lemma (W-L120),
the minimum-witness bound is not linear in I (W-N61). W-T51 and W-T111 as written double-count v Lambda_1 (GAP); the
corrected forms are CONFIRMED: H <= 16.99 I on selector trees with regular leaves on fresh blocks, and 26.71 I on term
decision lists with a common output mean. The reduction W-P121: H <= 23.55 I + 2.4 R(f) for any subcube partition
of a level set and any orders, so a rank term R <= K I (W-CJ122) would prove FEI with C = 23.55 + 2.4 K. Evidence:
on Wan-Wright-Wu's bad tree an adapted order keeps R/I constant (0.428) while the path order grows; on read-once
AND/OR formulas every single-gate order tried grows about 0.2 per level while H/I levels off near 5.3 (W-E5, a
candidate obstruction to the single-gate form). Novelty: the read-once half is O'Donnell-Tan composition plus A2's
Theorem A.

L2, B20 at level two and above (this stream; CLAIMS.json, NOTES.md). Complete proofs written there but checked only
inside the stream, so CANDIDATE until another agent's adversarial pass: Lemma 1, B^(i)_j <= phi(a, d) <=
psi(d_{j,i}), so B_i <= H(S_i | |S - i|); Lemma 2 on the level weights of D_i f; Theorem 3, B_{k-1} <= b_k I with
b_1 = 2/(sqrt(e) ln 2) exactly, b_k <= 2k log2 e, and interval-certified b_2 <= 3.5777 up to b_10 <= 27.4379;
Theorem 5, localization below c ln(1/eps_i) for every c < 1/2 with certified C(0.3) <= 4.0782, C(0.4) <= 13.8404,
C(0.45) <= 46.9287, threshold 1/2 exact for the Bonami bound; the reduction: FEI iff B_gap(tau, c) = O(I), where
B_gap holds the direction-i edges above level c ln(1/eps_i) for coordinates with eps_i < tau. Obstructions O1-O5:
f-independent level constants diverge (x0 times bent), level-local budgets fail (Hamming balls), product references
fail (AND powers), upper-endpoint charging loses k+1, and conditioning S_i on |S - i| loses log(1/eps) on tribes.
On tribes the block of i is a witness that costs (2 + O(w 2^-w)) I against B/I -> 2. PROVED (Proposition 6, Corollary 7):
no level inequality for {0, +-1} functions passes c = 1/2, because the level law of a Hamming slice tends to an arcsine law
whose left edge reaches every c > 1/2 as the slice density tends to 1/2. The adversarial pass is the stream's
own (NOTES section 9, second code path, 107 functions, 0 violations); no independent referee yet. Lemma 2 uses
Booleanity through ||D_i f||_r^r = eps_i for r < 2, a step that fails for quantum Boolean functions, so U-Q does not
reach Theorems 3 and 5 as proved. Novelty checked only against KKLMS (fixed levels, unspecified constants) and
O'Donnell-Wright-Zhou.

K, read-k trees (C017, C021). Set up only: the targets Cov[T] <= A log2(k+1) I, the per-variable potential
sum_i Inf_i log2 a_i(T), and Wan-Wright-Wu's Cov[T] <= log2(k) Var are stated, and both sources (arXiv:1312.3003,
arXiv:1806.03646) are in K-read-k/data/lit. No result. S (signed convolution) is empty; R and L left no folder.
All four stopped at the 00:29 network drop.


## 2. The equivalent forms now on the table

Each line is a statement equivalent to FEI (or sufficient, where marked), with the route that proves the link.

- B <= K I (campaign C018, through J_i <= B_i of B13; used by L2).
- U <= K' I (U-G).
- H <= A(I + DTC) (U-C1).
- Every ratio-critical f with all influences <= 1/2 has a relevant coordinate with H(S_i | S_-i) <= K Inf_i (U-C2).
- B_gap(tau, c) = O(I) for one (equivalently every) tau in (0, 1) and c < 1/2 (L2-gap).
- Sufficient: sum_i Delta_i U <= a I + b U with b < 1 (U-GU-implies-FEI).
- Sufficient: some subcube partition of a level set and some orders with rank term R <= K I (W-P121, W-CJ122).

The two sufficient forms are the only ones with a mechanism that is not already FEI in disguise: GU is a
restriction inequality, W-CJ122 a coding inequality.


## 3. What the obstructions have in common

The methods that are now dead, each with its witness:

| method | witness | route |
| --- | --- | --- |
| per-level constants independent of f | x0 times bent, B_k/I ~ 1.128/sqrt(k) | L2-O1 |
| level-local budgets | Hamming balls | L2-O2 |
| product references | AND tensor powers | L2-O3 |
| product and level-wise Gibbs references for thresholds | anti-diagonal tribes thresholds, (1/2) ln m per unit influence | BT referee |
| conditioning S_i on the size of S - i | balanced tribes, log(1/eps) + 1.34 against 2 | L2-O5 |
| Bonami-type level inequalities past level (1/2) ln(1/eps) | Hamming-slice derivatives (arcsine level law) | L2-slice |
| local form Delta_i U <= K Inf_i | annealed selector pairs (evidence) | U-locfail |
| minimum-witness variational bound | read-once part of the selector-tree class | W-N61 |
| single-gate rank codes | read-once AND/OR formulas (candidate) | W-E5 |
| witness cells of bounded size | AND/OR trees: excess kappa_h eps_i log(1/eps_i) at every fixed height | L2-R-E |
| one integer statistic of S - i (its size, or the rank of its nearest element) | tribes for the size; majority for the rank (B = 0, the rank pays 0.64 of sum h2(eps_i)) | L2-GW-E |
| witness bounds charged coordinate by coordinate | X009's selector bit, B_t = eps_t (log2(1/eps_t) + 1/ln 2 - o(1)) | X009 (SEL referee; re-checked, L2-GW-E) |
| pricing an unpredictable coordinate through a subcube (Harper-tight) pivotal set | random-set selector: u_t -> 1 while the boundary of A_t is twice the Harper minimum | L2-PF-E |
| orthogonal-neighbour closure under reuse | G = g o (g o g), H = 57/4 > 4I | SEL-6 |
| arguments valid for quantum Boolean functions | Slote's Pauli functions, H/I = Theta(d) | U-Q |

Most of these die on the same kind of function: tribes and its relatives (tribes thresholds, AND/OR trees, AND
powers). What each dead method shares is that it summarizes the rest of the spectral sample by a symmetric or product
statistic: its size, a product law, a level-wise Gibbs law, one fixed order inside a cell. What works on those
functions is a statistic that names structure. On tribes the block of i is enough (L2-O5 witness, 2 + o(1) against
B/I -> 2). W's owner codes name the subcube cell and then a position in it, and they fail on AND/OR trees exactly
where one flat order inside a cell has to encode a nested structure; W-E5's own suggestion is a hierarchical subset
code. SEL's cells are the same structure seen from the selector side.

So the open problem in every route is one object: for a general Boolean f, a statistic W_i of S - i, built from a
decision tree or formula of f (nested cells, not one flat cell), whose costs sum to O(I) and which pins S_i to within
O(eps_i) bits, on average over i, on the high-level edges that Theorem 5 leaves over. The average is forced: X009's
selector bit has B_t = eps_t (log2(1/eps_t) + 1/ln 2 - o(1)), so no witness costs O(eps_i) at every coordinate (L2-GW-E). Such a coordinate is paid by its trivial cost h2(eps_t) when those costs sum to O(I), as they do for X009; Proposition P3 (L2-PF) bounds the trivial cost of a set C by log2(e) sum_C eps_t + 2 E[|S cap C| (|S| - 1)] and gives nothing below it. When the unpredictable coordinates form a block Y whose fibers over the remaining coordinates X are signed characters, they are paid together by X: sum_Y B_t <= H(S_Y) <= 2 I_X however many there are (Lemma B, L2-SB, sharp on AND powers). In L2's terms that is B_gap = O(I); in W's terms a
hierarchical rank term R = O(I); in U's terms a restriction inequality that holds on these families. Taking
W_i = S - i itself makes the statement trivially equivalent to FEI, so the content is entirely in how structured W_i is
allowed to be; a proof has to use Booleanity at the high levels (U-Q), where level inequalities stop working (L2).


## 4. Next targets, in order

1. Hierarchical witness on AND/OR trees. W-E5 is the cleanest test bed: H/I levels off near 5.3 while every
   single-gate order grows. Build a nested-cell code (one rank per formula level) and measure R/I and the L2 residual
   H(S_i | W_i) - B_i on depths 1 to 12. If it stays bounded, try it on anti-diagonal tribes thresholds, Hamming
   balls, x0 times bent and the X-family (X002, X003, X009).
   Status 17:1x, 12 Oct (L2 section 5b, L2-R and L2-R-E): the L2 half is done for read-once formulas. The residual is
   exactly zero for the branch witness (the deepest path subtree that S - i meets, and S on its children: Lemma R),
   while every fixed-height cell leaves kappa_h eps_i log(1/eps_i) (kappa = 0.50, 0.16, 0.045, 0.009 at h = 1, 3, 5, 7);
   the residual falls below I once the cell holds a few times log2(1/eps_i) leaves. Exact limits on fan-in 2: B/I 3.6557,
   H/I about 5.345. So the general witness has to be multi-scale, cells of about log(1/eps_i) coordinates; the next
   test is such a rule for a general f (cells by co-occurrence with i, P(S contains i, j) = ||D_i D_j f||^2) on the
   families above. W's rank-code half (R/I with nested ranks) is untouched.
   Status 17:4x, 12 Oct (L2 section 5c, L2-R2 and L2-GW-E): on read-once AND/OR/parity formulas one integer, the height
   at which S - i first reaches the branch of i, is an exact witness. The general rule was run by brute force on 43
   functions, Hamming balls, x0 times bent and X002, X003, X009 among them: a scale-and-count profile over classes of
   equal co-occurrence is exact on 27 of the 28 structured functions outside the X-family and within 0.03 I on that
   family. Co-occurrence order alone is already wrong on AND/OR trees, and X009 forces the cost to be paid on average
   over coordinates. Anti-diagonal tribes thresholds live on a biased measure and were not run. At these sizes H/I <= 4,
   so the bench shows sufficiency, not growth; the missing inequality is a lower bound on P(i in S | W) on the
   high-level mass of D_i f, on average over i.
   Status 18:2x, 12 Oct (L2 section 5d, L2-PF and L2-PF-E): pivotal faces. P(A_i and A_j) = P(i, j in S), and
   Harper's inequality on pivotal sets gives E[|S| - 1 | t in S] >= (1/2) log2(1/eps_t), so the trivial witness cost of a
   set C of coordinates is at most log2(e) sum_C eps_t + 2 E[|S cap C| (|S| - 1)] (Proposition P3; none of this is new).
   P3 prices nothing below the trivial cost, so it exempts no coordinate that the trivial witness does not; X009's selector
   is affordable trivially because the bent coordinates carry I. Leaving out the coordinates whose trivial costs sum to
   O(I) and witnessing the rest restates B = O(I); it is a way to organize a proof, not a reduction. An unpredictable
   coordinate need not have a subcube pivotal set (random-set selector, L2-PF-E).
   Status 18:5x, 12 Oct (L2 section 5e, L2-SB and L2-SB-E): blocks with signed-character fibers. If F(x, y) =
   s(x) chi_{tau(x)}(y) over an address block X, then sum_{t in Y} B_t <= H(S_Y) = H(tau(X)) <= 2 I_X (erasure entropy is
   at most entropy, then Harper on each cell tau^{-1}(T); the constant 2 is attained by AND powers), and for any split
   B_X = sum_T R_T B(nu_T). On this class the data block, with any number of unpredictable coordinates, is never the
   obstruction. The class holds every Boolean function (|Y| = 1), so its address part, B averaged over signed subset
   functions s 1_A, is as hard as FEI. Checked on 25 functions with every quantity computed twice, and by a second code
   path on 278,440 cases with no violation. None of it is claimed new.
   Status 19:0x, 12 Oct (L2 section 5e, Corollary K, L2-SB-K and L2-SB-K-E): if every monomial of the GF(2) polynomial
   of f uses at most one variable from each of K blocks, every block has signed-character fibers over the rest, and
   Lemma B with subadditivity gives B <= H <= 2(K - 1) I. K = 2 is the quadratic case (known, sharp on inner product);
   for K = 3 and 4 the largest ratios found are those of AND_3 and AND_4 (2.9559, 3.4025) against 4 and 6. The
   K-partite constants form a ladder with supremum the FEI constant, like A2's address ladder, so this bounds only its
   first rungs. Checked on 244,934 members and by a second code path; no literature search, not claimed new.
2. GU numerics on the same families (sum_i Delta_i U / I), since GU is the other non-circular sufficient form.
3. BT-8 without the bias floor.
4. SEL-13 at 60 digits or more, only if a counterexample search is wanted; the referee's float artefacts are the trap.
5. An independent referee for L2 (Theorem 3, Theorem 5, the reduction, the certificate in code/certify_constants.py,
   Lemma R and Corollaries R1, R2, sections 5d and 5e); every L2 item is CANDIDATE until then.
6. Relaunch K (read-k trees) from its NOTES; it has the targets and both sources and no work yet.

Nothing here is a full proof. Calling any of the classes above new needs the literature check first (A2 is
duplicated by the fleet's A032 and unchecked against the literature; BT-1, BT-2 are in biased.tex; W's read-once half is O'Donnell-Tan; U and L2 are unchecked beyond the sources named).
