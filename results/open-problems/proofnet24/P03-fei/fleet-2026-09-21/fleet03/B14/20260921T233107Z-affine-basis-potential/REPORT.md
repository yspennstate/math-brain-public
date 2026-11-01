# B14 — affine-basis corrected potential and a geometry-free restriction telescope

**Date:** 21 September 2026 UTC  
**Scope:** `fleet03 / B14`, FEI campaign A (realizable restriction argument)  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status:** **PARTIAL / PROVED auxiliary reduction + finite falsification evidence. Full unrestricted FEI remains OPEN / NOT PROVED.**  
**Publication priority:** UNVERIFIED; no novelty claim.

## 0. Version change and exact target

This run changes mechanism rather than extending the previous fixed-physical-coordinate selector. The newest execution order asks fleet03/B14 for a distinct realizable restriction policy on the same hard cases, with any affine-coordinate cost charged explicitly.

The attempted universal statement is:

> **Affine-selector target (OPEN).** There is a finite dimension-independent constant `K` such that every noncharacter Boolean function `f` admits a realizable affine parity query `ell` for which
> 
> `Delta_ell Pi(f) > 0` and `Delta_ell H(f) <= K Delta_ell Pi(f)`,
> 
> where `Pi` is the affine-invariant minimum-basis potential defined below.

If this statement is proved, it gives full FEI immediately. This report proves the reduction, proves the potential's invariance/root/terminal properties, connects the drop to the existing corrected-erasure/crossing payment, and attacks the selector on exact finite hard families. It does **not** prove the universal selector.

## 1. Named cross-account result actually consumed

The primary completed peer artifact used substantively is

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B14/20260921T194301Z-crossing-amplified-erasure/REPORT.md`.

It proves, in any fixed physical coordinate system after character centering, for

`j(p)=1-h_2(1/2+sqrt(p(1-p)))`, `Phi=sum_i j(p_i)`,

the exact block identities

`Delta_A H = B_A + JS_A`,

`Delta_A Phi = Phi_A + G_A`,

with `Phi_A=sum_{i in A}j(p_i)`, `G_A=sum_{j notin A}[j(p_j)-E j(p_j(z))]`, and the tensorization `JS_A<=Phi_A`. It also proves the reflected-tangent crossing refund `G_A >= sum_{j notin A} j'(p_j)c_j(A)` at its stated centered scope.

I also use the completed fleet02/B14 information-payment result

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/20260921T210915Z-crossing-information-selector/REPORT.md`,

which proves for a survivor `j` and physical reveal block `A`

`I_A >= (1/2) log_2((1-p_j)/p_j) c_j(A)`,

and, for `p_j<=1/4` with `c_j(A)>=gamma p_j`, the Shannon payment `h_2(p_j) <= 9 I_A/(2 gamma)`.

The present construction uses fleet04's exact `Phi_A+G_A` drop as a lower bound for a **basis-minimized affine-invariant** potential drop. This is the cross-account result's application to the exact realizable-selector gap, rather than a citation-only reuse.

## 2. New potential: minimize the corrected influence potential over every affine basis

For each nonzero translation direction `v in F_2^n`, define

`alpha_f(v) = Pr_x[f(x) != f(x+v)]`.

For a linear basis `B={v_1,...,v_n}` of `F_2^n`, define

`Phi_B(f)=sum_{v in B} j(alpha_f(v))`,

and

\[
\boxed{\Pi(f)=\min_{B\text{ basis}}\Phi_B(f).}\tag{2.1}
\]

The minimization is a minimum-weight basis problem in the binary vector matroid; therefore a minimum is attained, and for finite computations it is found exactly by the ordinary greedy matroid algorithm after sorting the nonzero directions by weight `j(alpha_f(v))`.

### Theorem 2.1 — exact affine and character invariance — PROVED

For every invertible linear map `L` and every character `chi_a`,

\[
\boxed{\Pi(f\circ L)=\Pi(f),\qquad \Pi(\chi_a f)=\Pi(f).}\tag{2.2}
\]

**Proof.** Linear input change maps direction `v` bijectively to direction `Lv`, hence merely permutes the set of bases and their directional influences. For character multiplication,

`(chi_a f)(x)(chi_a f)(x+v)=(-1)^{a dot v} f(x)f(x+v)`.

Thus `alpha(v)` is either unchanged or replaced by `1-alpha(v)`. Since `j(p)=j(1-p)`, every basis weight is unchanged. QED.

This is the key geometry change: arbitrary affine reparameterizations no longer incur a fresh ordinary-influence comparison at each generation.

### Theorem 2.2 — root cost and terminal value — PROVED

The scalar bound already used by the corrected-erasure work is

\[
0\le j(p)\le {2\over\ln2}\min(p,1-p).
\]

Choose the ordinary coordinate basis and multiply by a character to fold every coordinate influence. Then

\[
\boxed{0\le\Pi(f)\le {2\over\ln2}\,\mathfrak I(f)\le {2\over\ln2} I(f),}\tag{2.3}
\]

where `mathfrak I` is the previously established minimum affine influence. A character has directional influence in `{0,1}` in every direction, hence `Pi=0`. Conversely, if a basis has zero weight in every direction, every basis derivative is a constant sign; integrating these signs shows `f` is a character up to global sign. Thus `Pi=0` exactly at the terminal character class.

## 3. Geometry-free affine restriction telescope — PROVED

At a node supported on an affine subspace, choose **any** nonzero affine linear functional and reveal its value. Each child is an affine hyperplane and may be reparameterized by any affine isomorphism before continuing. Define

`Delta Pi = Pi(parent)-E Pi(child)` and `Delta H=H(parent)-E H(child)`.

Because `Pi` and `H` are intrinsic under those reparameterizations, every complete finite affine restriction tree ending in characters satisfies the exact algebraic telescopes

\[
\sum_v \Pr[v]\Delta_v H=H(f),\qquad
\sum_v \Pr[v]\Delta_v\Pi=\Pi(f).\tag{3.1}
\]

No intermediate ordinary-influence comparison appears. Therefore:

### Corollary 3.1 — compact conditional end-to-end FEI argument — PROVED as an implication

If a finite `K` exists such that at every noncharacter node one can choose an affine parity query with

\[
0<\Delta\Pi,\qquad \Delta H\le K\Delta\Pi,\tag{3.2}
\]

then recursive selection terminates after at most the current affine dimension and

\[
H(f)\le K\Pi(f)\le {2K\over\ln2}I(f).\tag{3.3}
\]

Thus (3.2) is a genuine sufficient universal implication, not another equivalent residual with no deduction to FEI. **The existence assertion (3.2) remains OPEN.**

As a calibration, the current externally sourced unrestricted lower bound `C_FEI>6.521845710923046575` means this route cannot prove the optimum through (2.3) with `K<2.26029948...`; the small-dimensional ratios below are therefore only falsification evidence.

## 4. Applying the peer corrected-erasure theorem to `Pi`

Let `B={v_1,...,v_n}` be a `Pi`-minimizing basis at the current node. Reparameterize so these are the coordinate translations and character-center them, so `p_i=alpha_f(v_i)<=1/2` and

`Pi(f)=sum_i j(p_i)=Phi_B(f)`.

Restrict any coordinate block `A` in this minimizing basis. In each child, the surviving vectors `v_j`, `j notin A`, form a legal basis of the child translation space, but need not minimize its `Pi`. Therefore

`Pi(child) <= sum_{j notin A} j(p_j(child))`.

Using the exact fleet04 fixed-basis potential identity gives the universal one-sided bridge

\[
\boxed{\Delta_A\Pi\ge \Phi_A+G_A.}\tag{4.1}
\]

This is the point at which the named peer result enters the new mechanism. The affine minimization can only create **more** potential drop than the old fixed-basis corrected potential; it cannot lose the peer's `G_A` crossing/refinement refund.

Consequently a sufficient block-selector statement is

\[
\exists A:\quad B_A+JS_A\le K(\Phi_A+G_A).\tag{4.2}
\]

Every object in (4.2) comes from an actual realizable affine restriction after one legal change of coordinates, and the affine coordinate geometry is paid once by the root potential bound (2.3), not once per generation.

### Critical-core necessary condition

Choose an `H/Pi`-maximal affine restriction descendant with ratio `rho=H/Pi` (minimum dimension among maximizers). Each nonterminal child has ratio at most `rho`; hence for every block in a minimizing basis,

`Delta_A H >= rho Delta_A Pi >= rho(Phi_A+G_A)`.

Using `Delta_A H=B_A+JS_A` and `R_A=Phi_A-JS_A>=0`,

\[
\boxed{B_A\ge (\rho-1)\Phi_A+R_A+\rho G_A.}\tag{4.3}
\]

For a uniformly random `m`-block, let `A_q` be the fixed-cardinality Han excess from the peer work and `G_m=E G_A`, `JS_m=E JS_A`. Averaging (4.3) and using `E B_A=(m/n)H-A_q`, `H=rho Pi`, and `E Phi_A=(m/n)Pi` gives

\[
\boxed{A_q+\rho G_m\le JS_m.}\tag{4.4}
\]

So a high affine-critical ratio is possible only if its block recombination information persistently dominates both Han excess and the genuine potential-instability bank. The remaining universal gap is now precise: force a scale/query where that dominance fails, or equivalently prove (4.2) for some finite `K`.

The fleet02 crossing-information theorem suggests a concrete dichotomy for the next attack: large posterior crossings make `G_A` nontrivial and simultaneously require logarithmic physical information expenditure; if crossings are all small, one must exploit the resulting low-crossing structure to force small `B_A` or positive Han excess. That dichotomy is not proved here.

## 5. Decisive finite falsification tests

A self-contained checker for these computations is adjacent to this report. It computes Fourier entropy directly, computes all directional influences, obtains `Pi` by exact greedy minimum-weight matroid basis, realizes parity restrictions as affine hyperplanes, and recomputes child `Pi` after restriction.

### Exhaustive `n=4`

Fixing global sign leaves `2^15` truth tables. After removing the 16 zero-potential characters, **32,752 nonterminal Boolean functions** remain. For every one, at least one of the 15 nonzero parity queries had positive `Delta Pi`. The maximum, over all those functions, of the *best* selector ratio was

\[
\boxed{\max_f\min_{\ell:\Delta_\ell\Pi>0}{\Delta_\ell H\over\Delta_\ell\Pi}
=1.4541800170075352.}\tag{5.1}
\]

The observed maximizer is a one-point-defect representative (`truth-mask 2` under the checker's normalization), with `H=1.7012377755992936` and `Pi=1.3757697481091413`.

This is exhaustive finite evidence, **not** a theorem in arbitrary dimension.

### Structured families, querying only a `Pi`-minimizing basis

Even restricting the selector to the coordinates of one minimizing basis (a subset of all affine parity queries), the best observed ratios were:

| family | size | best `Delta H/Delta Pi` |
|---|---:|---:|
| one-point defect | n=3 | 1.2997595837424472 |
| one-point defect | n=4 | 1.4541800170075352 |
| one-point defect | n=6 | 1.4318794563366490 |
| one-point defect | n=10 | 1.3914129480133640 |
| width-2 tribes | 4 vars | 0.7793792444618476 |
| width-2 tribes | 10 vars | 1.8303402466057823 |
| addressing | k=2 address bits | 1.0000000000000000 |
| addressing | k=3 address bits | 1.0832797036981350 |
| majority | n=5 | 0.7793792444618476 |
| majority | n=9 | 0.7627819637924613 |

Again these are attacks on the candidate, not a proof.

### The known every-coordinate erasure obstruction is avoided rather than denied

The newest gate-reformulation report gives an explicit family: take a bent inner-product function on even `m` variables, adjoin a variable `z`, and flip one point in the `z=1` half. Its physical `z` coordinate has `B_z/Inf_z` growing linearly (`~m+1.44` in the recorded erasure statistic), so a universal every-coordinate payment is false.

The new affine potential was tested on the same family. The table below gives `H/Pi`, the best query among a `Pi`-minimizing basis, and the ratio for the bad appended physical `z` query:

| m | `H/Pi` | best minimizing-basis query | appended-`z` query |
|---:|---:|---:|---:|
| 2 | 1.1449461423162186 | 1.2997595837424472 | 1.2997595837424472 |
| 4 | 1.0338033332409780 | 0.9656815311128423 | 1.9037240829520220 |
| 6 | 1.0076929218577295 | 0.9800994958086726 | 2.7299256974104260 |
| 8 | 1.0020608683503338 | 0.9931900125833454 | 3.7283860032119630 |
| 10 | 1.0005744037121770 | 0.9978604907573151 | 4.6889052182235655 |

So the specifically known bad coordinate becomes rapidly worse while an alternative affine/minimizing-basis query stays near one. This does **not** establish boundedness for the family asymptotically, but it is the intended early adversarial test: the new policy is not immediately killed by the latest every-coordinate obstruction.

## 6. Claim ledger

### PROVED in this report

1. `Pi` is invariant under invertible linear input changes and output-character multiplication.
2. `0<=Pi<=(2/ln2) I` and `Pi=0` exactly on characters.
3. `Pi` and `H` telescope exactly on arbitrary realizable affine-parity restriction trees without accumulating affine geometry loss.
4. The universal selector (3.2), if proved with finite `K`, implies full FEI with constant `2K/ln2`.
5. In a `Pi`-minimizing basis, the completed fleet04 corrected-erasure theorem gives `Delta_A Pi >= Phi_A+G_A`.
6. On an `H/Pi`-critical descendant, the exact necessary conditions (4.3)-(4.4) hold.

### REFUTED / PRESERVED DEAD ROUTES

- A universal **every prescribed coordinate** erasure payment remains false. The bent-plus-flip family is explicitly retained; no affine change is used to pretend the bad physical coordinate became cheap.
- Repeatedly comparing arbitrary affine bases to ordinary influence at every generation is unnecessary for this potential, but this does **not** prove arbitrary affine restrictions are free in the original influence metric.

### FINITE EVIDENCE ONLY

- Exhaustive `n=4` selector ratio bound (5.1).
- The structured-family and bent-plus-flip tables.
- These computations do not promote the universal selector to PROVED.

### OPEN / CONDITIONAL

- The decisive implication remains: prove a dimension-free `K` in (3.2), or construct a Boolean family whose best affine query has unbounded `Delta H/Delta Pi` or nonpositive `Delta Pi` everywhere.
- A promising sharpened bridge is a crossing dichotomy combining fleet04's `G_A` lower bound with fleet02's logarithmic information cost for posterior crossings, while using Han excess when crossing is small.
- Full uniform-cube FEI remains **OPEN / NOT PROVED**.

## 7. Joint handoff fields

- `consumed_peer_artifact`: `fleet04/B14/20260921T194301Z-crossing-amplified-erasure/REPORT.md` (primary), plus `fleet02/B14/20260921T210915Z-crossing-information-selector/REPORT.md` for the next crossing-information bridge.
- `applied_to_claim`: convert fixed-basis corrected-erasure/crossing refunds into a lower bound on an affine-invariant minimum-basis potential drop, so affine restriction choices can telescope without repeated geometry loss.
- `remaining_implication`: establish `exists affine parity ell: 0<Delta_ell Pi and Delta_ell H<=K Delta_ell Pi` for one universal finite `K`; equivalently force a realizable block satisfying (4.2).
- `next_recipient`: `fleet01/B14` and `fleet04/B14` for realizable block/crossing construction; `fleet03/B17` for an adversarial search against the exact `Pi` selector.
- `full_problem_change`: auxiliary reduction strengthened; full FEI remains OPEN.
- `mechanism_change`: YES — from fixed physical-coordinate/block payment to an affine-invariant binary-matroid basis potential and affine-hyperplane decision tree.

## 8. Next attack

Prove or refute the following **single** quantitative dichotomy on an `H/Pi`-critical node in a `Pi`-minimizing basis. For some universal constants `gamma,c>0`, either

1. a block `A` creates a survivor crossing `c_j(A)>=gamma p_j`, in which case fleet02's information theorem and fleet04's `G_A` refund should jointly pay the logarithmic erasure contribution; or
2. all relevant crossings are below that threshold, in which case show from the posterior laws that some affine parity/block has `B_A+JS_A <= c(Phi_A+G_A)` using Han excess or a low-crossing coupling.

A counterexample must be a genuine Boolean family and must be tested against **all** relevant affine queries, not just the known bad physical coordinate.
