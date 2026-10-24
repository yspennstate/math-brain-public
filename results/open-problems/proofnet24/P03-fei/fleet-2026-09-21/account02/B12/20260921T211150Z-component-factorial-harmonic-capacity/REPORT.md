TASK: B12 ACCOUNT: account02 RUN: 2026-09-21T21:11:50Z — FEI interface B: factorial reciprocal-component contraction and harmonic trigger capacity

STATUS: PARTIAL / FULL UNIFORM-CUBE FEI REMAINS OPEN / NOT PROVED.
EXECUTION: WITHOUT_VERIFIED_BRAIN. No authenticated brain retrieval or receiver-context use occurred.
MODEL SELF-REPORT: GPT-5.6 Sol.
REQUESTED EFFORT: deepest / maximum actually supported.
CONFIGURED REASONING LEVEL: UNKNOWN / selector not exposed.
KNOWN REASONING LEVEL: NOT_EXPOSED.
PROVIDER REASONING USAGE: null / NOT_EXPOSED.

This run follows FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z and makes a material mechanism change after three B12 runs left the same positive-defect / terminal-to-prefix gap unpaid.

## 0. Fresh dependencies and the last three B12 reports

The mathematical master was refreshed during the run. The direct seven-FEI owner order remains the operative assignment for B12.

The last three substantive own reports compared were:

1. `proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260921T155715Z-random-prefix-loss-hypercontractive/REPORT.md`: exact terminal-to-prefix loss `L_f`, Palm hypercontractive/shallow-prefix bounds, and the conclusion that depth alone does not recover row identity.
2. `proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260921T165622Z-depth-rigidity-obstruction/REPORT.md`, blob `8e497dcff529c2128a74e6d199032906fa313440`: an abstract fixed-depth surrogate makes terminal-to-prefix loss unbounded, while genuine Boolean equality in the sharp mean-depth bound forces a constant-sign coordinate-subcube derivative.
3. `proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260921T175134Z-physical-erasure-budget/REPORT.md`: exact physical erasure / dual-total-correlation identity and dimension-free near-subcube Palm stability, but also a rigorous entropy-continuity obstruction showing that small TV plus small mean excess cannot by itself pay rare off-subcube address entropy.

The same universal implication was therefore still unpaid for three runs: turn quantitative near-rigidity of many genuine Boolean derivative Palm rows into a nonreused `O(I)`/information payment for their address entropy.

This run does not iterate the TV/mean route. It changes mechanism to two coding currencies already present in the exact selector identity: (i) the factorial order refund, used at reciprocal-component level, and (ii) the actual prefix KL refund, used through a symmetric harmonic trigger capacity.

### Completed other-account result consumed

The required named cross-account input is account04/B12:

`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260921T201418Z-palm-trigger-cluster/REPORT.md`, read at scientific master `28eb593ef50251e09475a7a7aa8c20647599f376`, blob `4643e5dd27cc48a508820a30413e24b9c4717fac`.

It proves, at Palm-row TV error `epsilon<=1/16`, that a robust trigger `i -> k` satisfies `q_ik/j_i >= 1/2-epsilon`, reciprocal triggers lock the exact signature `T_i={i} union F_i`, reciprocal connected components share that signature, and nonreciprocal robust edges increase influence by at least factor 7 (and, under the physical scale approximation, drop codimension by at least 3).

A second compatible completed input used for interpretation is account04/B13:

`proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260921T2025Z-zero-defect-exception-peeling/REPORT.md`.

It proves that exact zero-defect components are clique-like one-point phases gated only by exceptional rows, and that their zero-defect Fourier-entropy sector can be peeled despite arbitrary exceptional rows. The present result is a sequential/factorial quantitative analogue: it pays the *internal selector entropy* of an approximate reciprocal component and exposes a concrete positive-defect residual.

FLEET_RULES moves executed here: #12 (find the conserved nonreuse capacity), #14 (quotient by reciprocal trigger components), and #19 (make the selector payment an explicit two-part code rather than another scalar stability inequality).

## 1. Normalization and the exact selector ledger

Let `f:{-1,1}^n->{-1,1}`, let

`p_B = \hat f(B)^2`,  `I = sum_B |B| p_B > 0`,

and write

`j_i = Inf_i(f) = sum_{B contains i} p_B`,
`pi_i = j_i/I`.

Use the B12 size-biased Palm experiment: sample `B*` with `P(B*=B)=|B|p_B/I`, choose `X` uniformly from `B*`, and expose the unordered set `A` preceding `X` in a uniform random order of `B*`. Then

`P(X=i)=pi_i`,
`P(B*=B | X=i)=p_B/j_i` for `i in B`.

For a terminal size `K=|B*|`, put

`phi(K)=log_2(K!)/K`.

The previously proved exact selector identity is

`Sel(f)/I = H(X) - I(X;A) - R_ord`,                       (1.1)

where

`R_ord = E[phi(K)]`
under the Palm law. Indeed

`E[phi(K)] = (1/I) sum_B p_B log_2(|B|!)`.

This run exploits both negative terms in (1.1), rather than trying to bound `H(X)` by a row-local depth statistic.

For distinct `i,k`, set

`q_ik = P_p(i,k in B) = sum_{B contains i,k} p_B`,
`d_i = sum_{k!=i} q_ik`,
`M_i = d_i/j_i` when `j_i>0`.

The exact prefix marginals are

`alpha_ik := P(k in A | X=i) = q_ik/(2j_i)`,             (1.2)
`beta_k  := P(k in A)       = d_k/(2I)`.                 (1.3)

The factor `1/2` in (1.2) is exact: conditional on a terminal set containing `i,k`, the probability that `k` precedes `i` is `1/2`.

Let

`D_i = D_2(Law(A|X=i) || Law(A))`.

Then the scaled sequential information refund is

`D_seq := I I(X;A) = sum_i j_i D_i`.                     (1.4)

## 2. New theorem A: a symmetric harmonic trigger capacity is paid nonreusably by actual prefix KL

Fix `epsilon=1/16`, and call a directed pair `(i,k)` a `7/16-trigger` if

`q_ik/j_i >= 7/16`.                                     (2.1)

Every account04/B12 robust trigger is a `7/16-trigger`.

Define its symmetric harmonic capacity

`c_ik = q_ik / max(M_i,M_k)`                             (2.2)

when the denominator is positive, and zero otherwise.

For any set `E` of directed `7/16-trigger` edges, put `C_E=sum_(i,k in E)c_ik`.

### Theorem A

For every Boolean `f` (in fact the proof uses only the actual Palm subset law identities above),

`C_E <= K_* D_seq`,                                      (2.3)

with

`K_* = 1/d_2(7/32 || 1/8) + 1/[-log_2(7/8)]`
`    = 25.651039887607705...`.                           (2.4)

Equivalently,

`D_seq >= 0.03898477427744015... C_E`.                  (2.5)

The key point is nonreuse:

`sum_k c_ik <= j_i`,                                     (2.6)
`sum_i c_ik <= j_k`.                                     (2.7)

So the same target coordinate cannot absorb arbitrarily many units of harmonic trigger capacity even when the raw depth bank `sum_i d_i` is huge.

### Proof

Let `tau=1/8`, `a=7/32`, and
`d0=d_2(a||tau)=0.04887550460410142...`,
`b0=-log_2(1-tau)=0.19264507794239588...`.

Split directed trigger edges according to whether their target has `beta_k<=tau` or `beta_k>tau`.

**Low-target part.** For each source row `i`, data processing under the binary observable `1_{k in A}` gives

`D_i >= d_2(alpha_ik || beta_k)`                         (2.8)

for every `k`. Since the weights `q_ik/d_i` sum to one over `k!=i` when `d_i>0`,

`D_i >= sum_k (q_ik/d_i) d_2(alpha_ik||beta_k)`.        (2.9)

For a trigger edge with `beta_k<=1/8`, (2.1)-(1.2) give `alpha_ik>=7/32`; monotonicity of binary KL on `alpha>=beta` therefore gives

`d_2(alpha_ik||beta_k) >= d0`.                           (2.10)

Multiplying (2.9) by `j_i` and retaining only low-target trigger terms,

`j_iD_i >= d0 sum_(low trigger k) q_ik/M_i`
`       >= d0 sum_(low trigger k) c_ik`,                 (2.11)

because `M_i=d_i/j_i` and `max(M_i,M_k)>=M_i`.

Summing `i`,

`C_low <= D_seq/d0`.                                     (2.12)

**High-target part.** Because `X=k` implies `k notin A`, the same binary data-processing argument with the *self* coordinate gives

`D_k >= d_2(0||beta_k) = -log_2(1-beta_k)`.             (2.13)

Hence every high target `beta_k>1/8` has `D_k>=b0`.

For each fixed target `k`,

`sum_i c_ik <= sum_i q_ik/M_k = d_k/M_k = j_k`.         (2.14)

Therefore

`C_high <= sum_(k:beta_k>1/8) j_k`
`       <= (1/b0) sum_k j_kD_k`
`       <= D_seq/b0`.                                    (2.15)

Adding (2.12) and (2.15) proves (2.3). QED.

### Why this is different from the killed raw-depth route

The account03/B12/odd-majority obstruction rules out paying `sum_i d_i` by `D_seq`. Theorem A never asks for that. The symmetric denominator automatically discounts a pair when either endpoint has a large Palm mean degree. In the exhaustive small-cube self-check below, the theorem has large slack; the written proof, not the enumeration, is the universal claim.

## 3. New theorem B: the factorial refund pays reciprocal-component internal address entropy

The previous three B12 runs tried to pay row identity directly from depth/TV. Here the order/factorial refund is used as a *code length*.

Suppose a Palm row `i` has a trigger set `F_i` of size `r>=1`, and its terminal remainder law

`nu_i = Law(B*\{i} | X=i)`

satisfies

`TV(nu_i, U_{F_i}) <= eps_i`,                            (3.1)

where `U_F` is the uniform law on all subsets of `F` (each trigger independently present with probability `1/2`).

Let `K=|B*|`.

### Lemma B1 — robust factorial refund

For every such row,

`E[phi(K)|X=i] >= log_2(r+1) - 2 log_2(e) - eps_i log_2(r+1)`.       (3.2)

In particular, if `eps_i<=1/(16r)`,

`E[phi(K)|X=i] >= log_2(r+1) - C_fact`,               (3.3)

where

`C_fact = 2log_2(e)+1/16 = 2.9478900817779268...`.     (3.4)

### Proof

First take the ideal row `nu_i=U_F`. Then `K=1+Z`, `Z~Bin(r,1/2)`.

For every integer `K>=1`, the integral lower bound on the factorial gives

`log_2(K!)/K >= log_2 K - log_2 e`.                     (3.5)

Also, using `ln x <= x-1`,

`log_2(r+1)-E log_2 K <= [(r+1) E(1/K)-1]/ln2`.        (3.6)

The binomial identity

`E[1/(Z+1)] = int_0^1 ((1+t)/2)^r dt = 2(1-2^{-(r+1)})/(r+1)`       (3.7)

makes the right side of (3.6) strictly smaller than `log_2 e`. Combining (3.5)-(3.7),

`log_2(r+1)-E phi(K) < 2log_2 e`.                       (3.8)

For a row within TV `eps_i`, couple it to the ideal row with mismatch probability at most `eps_i`. On the ideal support `1<=K<=r+1`, `0<=phi(K)<=log_2(r+1)`, while `phi` is nonnegative everywhere. Thus the expected refund can decrease by at most `eps_i log_2(r+1)`. This proves (3.2). Finally `log_2(r+1)<=r` for `r>=1`, giving (3.3). QED.

### Reciprocal-component contraction

Now consume account04/B12's exact reciprocal signature locking. Let `G` be a family of robust labels partitioned into reciprocal components `C`. For a component there is one common closed trigger signature `T_C` such that

`T_C = {i} union F_i` for every `i in C`.                (3.9)

Hence all its rows have the same `r_C=|T_C|-1`, and

`|C| <= |T_C| = r_C+1`.                                 (3.10)

Let `Zeta` denote the reciprocal component of `X` when `X in G`.

Assume first that every active row is in `G`. Applying (3.2) componentwise and using `H(X|Zeta=C)<=log_2|C|<=log_2(r_C+1)` gives

`R_ord >= H(X|Zeta) - 2log_2 e - E[eps_X log_2(r_X+1)]`.            (3.11)

Insert this into the exact selector ledger (1.1) and use data processing `I(X;A)>=I(Zeta;A)`:

`Sel(f)/I <= H(Zeta|A) + 2log_2 e + E[eps_X log_2(r_X+1)]`.         (3.12)

If every robust component is at the stronger accuracy `eps_i<=1/(16r_i)`, then

`Sel(f)/I <= H(Zeta|A) + C_fact`.                        (3.13)

This is the first B12 reduction in this chain that makes the reciprocal component, rather than the individual derivative row, the coding symbol. The factorial term pays the *entire within-component coordinate entropy* up to a universal constant.

### Partial-good form with arbitrary exceptional rows

Let `G=1` denote the event that the selected row belongs to a reciprocal component satisfying the hypotheses above; let `w=P(G=1)`. Keep the actual bad-row prefix information rather than discarding it.

The same decomposition yields

`Sel(f)/I <= H(G|A) + w H(Zeta|A,G=1) + (1-w) H(X|A,G=0) + 2w log_2 e + w E[eps_X log_2(r_X+1)|G=1]`.       (3.14)

At `eps_X<=1/(16r_X)` on the good sector, the last two terms are at most `w C_fact`.

Equation (3.14) is a quantified interface-B remainder. It isolates exactly two unpaid address channels:

1. reciprocal-*component* identity after seeing the actual prefix;
2. the genuinely exceptional-row conditional address entropy.

The individual-coordinate entropy inside every sufficiently accurate reciprocal cluster is already paid by the pre-existing factorial refund, without spending influence a second time.

## 4. How Theorems A and B use the account04 trigger-cluster theorem

The account04/B12 theorem supplies more than notation.

For every robust trigger at `epsilon<=1/16`, `q_ik/j_i>=7/16`; hence every such edge is admissible in Theorem A.

For a reciprocal component it supplies the exact common signature (3.9), which is the only reason the factorial lower bound can be compared to the *conditional coordinate entropy* `H(X|Zeta)` without inventing a cluster.

For nonreciprocal robust edges it supplies the factor-7 influence jump and codimension drop. Those are now naturally interpreted as *component escape edges*. Theorem A shows that a symmetric harmonic amount of these escape edges is already paid by the genuine prefix KL with no incoming or outgoing reuse.

This is also compatible with account04/B13's exact zero-defect peeling. In the exact endpoint the reciprocal components become true one-point phases gated by exceptional rows. Equation (3.12) is a noisy sequential analogue of the internal phase payment: exact/near-exact component-internal address entropy is removed, and only component gates/escapes plus exceptional rows remain.

## 5. A concrete low-defect corollary for the harmonic capacity

Let the account04 physical scale approximation hold with `|2^{-r_i}-j_i| <= (1/16) j_i`. Put

`delta_i = M_i - (1/2)log_2(1/j_i) >= 0`.               (5.1)

If a robust row obeys the normalized low-defect condition

`delta_i <= r_i/16`,                                    (5.2)

then, since `|log_2(1/j_i)-r_i| <= log_2(16/15)`, for `r_i>=1`,

`M_i <= c_* r_i`,                                       (5.3)

where

`c_* = 1/2 + 1/16 + (1/2)log_2(16/15) = 0.6090547021957408...`.     (5.4)

If `i->k` is a robust trigger and both endpoint rows satisfy (5.2), account04/B12 gives `r_k<=r_i` (equality on a reciprocal edge; at least a 3-step drop on a nonreciprocal edge). Therefore

`c_ik >= (7/16) j_i/(c_* r_i)`.                         (5.5)

If a fraction `gamma_i` of the `r_i` trigger positions of source `i` land in robust low-defect targets, then

`sum_(good trigger k)c_ik >= gamma_i * (7/16)/c_* * j_i = 0.7183262823893186... gamma_i j_i`.     (5.6)

Together with Theorem A,

`D_seq >= 0.028003787976500313... * sum_i gamma_i j_i`.             (5.7)

This is an actual influence-relative, nonreused payment for the low-normalized-defect trigger sector. It is intentionally not advertised as the missing full selector bound: (5.7) pays influence mass, not all remaining component address entropy. Its value is that it removes the old congestion ambiguity from the good sector and pins the unpaid mechanism to component-label/exception entropy in (3.14).

## 6. FULL-PROBLEM CHANGE

**Before this run.** After the last three B12 reports, full FEI was open and the surviving interface-B implication was only qualitative:

> use quantitative Boolean near-subcube stability to control terminal-to-prefix *address* information without reusing raw derivative depth.

TV closeness and first moments were known insufficient; exact equality was rigid; no nonreused component-level code was available.

**After this run.** Full FEI is still **OPEN / NOT PROVED**, so the universal FEI constant has not moved.

What changed is the precise universal remainder. For a reciprocal robust sector, the old individual-row address entropy is no longer an unpaid object: the existing factorial term pays its entire within-component entropy, yielding (3.12)/(3.14). Separately, every robust trigger edge enters the genuinely nonreused harmonic capacity (2.2), which is paid by actual terminal-to-prefix KL with the explicit universal constant `K_*`.

The quantified remaining implication is now:

> bound the reciprocal-component conditional address `w H(Zeta|A,G=1)` and the exceptional-row conditional address `(1-w)H(X|A,G=0)`, together with the positive-defect distortion `w E[eps_X log_2(r_X+1)|G=1]`, by a dimension-independent constant after the selector normalization, using the factor-7/codimension DAG, exact common-potential integrability, or a new exceptional-row elimination.

At the stronger accuracy `eps_i<=1/(16r_i)`, the distortion is already universal (`<=1/16`); then only component identity plus genuinely exceptional rows remain.

## 7. MECHANISM CHANGE

**Old mechanism:** derive stronger scalar depth/TV consequences for one derivative row and hope entropy continuity turns them into a row-address bound. This route was decisively blocked by the preceding B12 abstract rare-address construction and by the joint fixed-relative-error obstruction.

**New mechanism actually executed here:** quotient robust rows by account04 reciprocal trigger signatures and use an explicit *two-currency compression*:
- factorial/order refund pays within-component coordinate identity;
- actual prefix KL pays a symmetric harmonic trigger/escape capacity with provable incoming and outgoing nonreuse.

This is not a renamed depth residual. Neither theorem asks for `sum_i d_i=O(I)`, and the proof keeps the actual conditional prefix channel.

## 8. Executed checks

A standard-library checker was executed after the derivation.

It exhaustively enumerates Boolean functions through dimension four modulo global sign (32,906 truth tables), computes the exact Walsh-square spectrum and the actual Palm-prefix mutual information, takes every directed pair satisfying `q_ik/j_i>=7/16` as a trigger, and checks Theorem A numerically.

Results:
- Boolean functions checked: 32,906.
- Directed qualifying trigger edges: 278,878.
- Violations of `C_E <= K_* D_seq`: 0.
- Minimum observed positive `D_seq/C_E`: 0.25.
- The ideal factorial gap was checked for `1<=r<=2048`; maximum observed `log_2(r+1)-E phi(1+Bin(r,1/2))` was `2.4361681465194724`, below the analytic bound `2log_2 e = 2.8853900817779268`.

These are self-checks only. The universal claims are the written information-theoretic proofs above.

## 9. Failed stronger bridge and next attack

A stronger hope would be to replace `H(Zeta|A)` in (3.12) by a universal constant using only the local trigger incidence graph. That is not justified. Even exact component-internal product structure does not by itself rule out many component labels; the missing fact is a *global Boolean common-potential constraint* on how approximate components are gated or escape into exceptional rows.

The next B12 target is therefore not another depth inequality. It is one of these two exact alternatives:

1. **Component escape code.** Use the factor-7/codimension DAG plus Theorem A to code `Zeta` adaptively, proving that the remaining component-label entropy is canceled by prefix KL without reusing an exceptional target.
2. **Quantitative B13 peeling.** Perturb account04/B13's exact statement that zero-defect component gates lie entirely in the exceptional set and are disjoint, replacing exact disjointness by a paid overlap inequality whose error is precisely the distortion term in (3.14).

Either route must retain the real Boolean mixed-derivative symmetry and the actual prefix channel. A fixed-relative one-row support approximation, raw depth sum, or generic entropy continuity is already known insufficient.
