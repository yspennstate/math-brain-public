# B17 FEI — true-stall exception ladder and exact Boolean fan-in obstruction

**Status:** **ESSENTIAL_STEP_APPLIED / one stronger critical-core reduction proved; one natural replacement refuted.** Full uniform-cube Fourier entropy--influence remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver context was used.

## 0. Live assignment and version change

The invocation text still named the older interface-D remainder-adversary role. The live joint order now contains `FEI-PROOF-EXECUTION-20260921T230620Z`, which supersedes conflicting mathematical duties. Its exact fleet04/B17 assignment is campaign A:

> construct or disprove the necessary critical-core exception reduction, distinguishing existence from every-core claims.

Accordingly this run attacks the current campaign-A stalled-core reduction rather than the superseded D/B15 task.

The exact completed other-account inputs used substantively are:

1. **fleet02/B14**,
   `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/20260921T220126Z-stationary-trigger-selector/REPORT.md`.
   It proves the C12-certified near-subcube selector on a nonempty **closed** control subsystem and the adaptive coefficient-12 compiler. Its stalled state is characterized by an empty maximal closed certified kernel `S_infty`.
2. **fleet01/B18**,
   `proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, report blob `9f2bb40584be20e5e440e7f3913873c34858bc91`.
   It proves the character-invariant folded activation potential and a globally nonreused physical-restriction telescope with descendant re-centering.
3. **fleet04/B18**,
   `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260921T221132Z-support-depth-stalled-core/REPORT.md`.
   It integrates those inputs and localizes the remaining obstruction to the stalled/kernel-free exceptional-row sector.

The present result changes that endpoint: `S_infty=empty` is too coarse to be the actual exception condition. There is a strictly stronger realizable policy whose genuine stall has an exact monotone exception ladder.

## 1. Normalization and the old selector

Work in a median-character gauge, so every active folded influence is

\[
0<p_i=\operatorname{Inf}_i(f)\le \tfrac12,
\qquad J(f)=\sum_i p_i.
\]

For a pivot `j`, write `eta_j` for its pivotality event. A witness `(j,Z,Q)` is **C12-certified** when `Z` is a nonempty physical control block, `r=|Z|`, `Q` is one atom of the `Z` cube of density `q=2^{-r}`, and

\[
\Pr(\eta_j\triangle 1_Q)\le \frac{q}{16r}.
\tag{1.1}
\]

The already proved physical near-support theorem gives the coefficient-12 entropy payment whenever, in addition,

\[
I_Z:=\sum_{i\in Z}p_i\le r p_j.
\tag{1.2}
\]

Fleet02/B14 obtains (1.2) from stationarity when a nonempty certified family is **closed** under the chosen control blocks. Iterative pruning produces a maximal closed kernel `S_infty`; if it is empty, that policy stalls.

The first question here is whether `S_infty=empty` is already the right exceptional-core condition. It is not.

## 2. Exact Boolean false-positive stall for the closed-kernel policy

For integers `r,m>=1`, let `x in {0,1}^r`, `y in {0,1}^m`, let

\[
A=\{0^r\},
\]

and define the Boolean star-parity function

\[
F_{r,m}(x,y)=(-1)^{1_A(x)(y_1\oplus\cdots\oplus y_m)}.
\tag{2.1}
\]

Put `q=2^{-r}`.

### Lemma 2.1 — exact influences
Every coordinate of `F_{r,m}` has influence exactly `q`.

For a pivot `y_i`, changing `y_i` flips the value exactly when `x=0^r`, so `p_{y_i}=q`. For a control `x_j`, changing `x_j` crosses the atom `0^r` only when the other `r-1` controls vanish and the `y`-parity is one, also giving probability `q`.

Hence

\[
J(F_{r,m})=I(F_{r,m})=(r+m)q.
\tag{2.2}
\]

Each `y_i` is exactly C12-certified by the block `Z_i={x_1,...,x_r}` with zero support error, and

\[
I_{Z_i}=rq=rp_{y_i}.
\tag{2.3}
\]

Thus every pivot row is **directly payable** at equality.

Now specialize to `r=1`, `m>=2`. The control `x` has pivotality event

\[
\{y:y_1\oplus\cdots\oplus y_m=1\},
\]

which is not C12-certified. For any codimension-one atom `y_k=b`, its symmetric difference from parity is exactly `1/2`; for any atom of codimension at least two, density mismatch alone is at least `1/4`. Both are far above the C12 tolerance.

Therefore the certified rows are the `y_i`, and every chosen control block is `{x}`, outside that certified set. The old pruning kernel is

\[
S_\infty=\varnothing,
\]

although every certified row satisfies the actual payment condition (1.2).

### Consequence
`S_infty=empty` is a **policy stall**, not a necessary mathematical exception. It can declare a state stalled even when a coefficient-12 physical step is immediately available.

This is an exact Boolean counterexample to treating closed-kernel emptiness as the final critical-core exception reduction. It is not a counterexample to fleet02/B14's stationary theorem and not a counterexample to FEI.

## 3. Replacement: direct-admissible policy and TRUE_STALL

Call a C12-certified witness `(j,Z,Q)` **direct-admissible** when it also satisfies

\[
\frac1{|Z|}\sum_{i\in Z}p_i\le p_j.
\tag{3.1}
\]

Equivalently, the already proved coefficient-12 block theorem applies directly.

Define a centered state to be **TRUE_STALL** when it has at least one C12-certified row but **no** direct-admissible C12 witness. (If it has no certified row at all, it is already an exceptional endpoint of the same reduction.)

This policy strictly dominates the closed-kernel policy. If a nonempty closed certified subsystem exists, the stationary theorem of fleet02/B14 supplies a direct-admissible member. Therefore

\[
\mathrm{TRUE\_STALL}\Longrightarrow S_\infty=\varnothing,
\tag{3.2}
\]

and Section 2 proves the converse is false.

### Theorem 3.1 — strict-influence exception ladder
At a TRUE_STALL state, every certified row `j` has a finite path

\[
j=i_0\to i_1\to\cdots\to i_t
\tag{3.3}
\]

such that

\[
p_{i_0}<p_{i_1}<\cdots<p_{i_t},
\tag{3.4}
\]

and `i_t` is not C12-certified.

### Proof
Choose any C12 witness `(j,Z,Q)`. Since the state is TRUE_STALL, (3.1) fails:

\[
\frac1{|Z|}\sum_{i\in Z}p_i>p_j.
\]

Hence some `i in Z` satisfies `p_i>p_j`. If that `i` is not C12-certified, stop. Otherwise choose any C12 witness for it and repeat. Influence strictly increases at every step, so no coordinate can repeat. There are finitely many coordinates, hence the process terminates at a non-certified coordinate. QED.

### Corollary 3.2 — stronger exact critical-core reduction
Run the physical restriction policy that uses **any** direct-admissible C12 witness whenever one exists. Each successful step obeys

\[
\Delta H\le12 I_Z\le12D_Z,
\]

and entropy and folded drift telescope on the finite physical restriction tree. Therefore, if a Boolean function has `H/J>12`, some physical descendant with positive `H-12J` must be TRUE_STALL or have no C12-certified row. Among such descendants one may choose minimum relevant dimension.

Thus the live campaign-A exception sector can be narrowed from

\[
S_\infty=\varnothing
\]

to the stronger, policy-independent statement

\[
\boxed{\text{no directly payable certified witness exists}.}
\tag{3.5}
\]

Moreover every remaining certified row is connected by a strict-influence ladder to a genuinely non-certified endpoint.

This is an actual realizable restriction reduction, not an every-core shell claim, and tensor replication does not invalidate its existential descendant quantifier.

## 4. The tempting next replacement is false: endpoint influence cannot pay all certified influence

One might now try to charge the certified rows along the strict-influence ladders to the exceptional endpoints. That also fails, even for an exact Boolean family.

For `r>=3`, `m>=2`, let

\[
h_r(x)=1-2\,1_{\{1^r\}}(x)
\]

be the one-point defect at the opposite control corner, and define

\[
G_{r,m}(x,y)=h_r(x)F_{r,m}(x,y).
\tag{4.1}
\]

Again let `q=2^{-r}`.

### Lemma 4.1 — exact TRUE_STALL geometry
For every pivot `y_i`,

\[
p_{y_i}=q,
\]

and its pivotality support is still exactly `x=0^r`, so it is C12-certified with zero error and control block all `r` control coordinates.

For every control coordinate `x_j`, the derivative support is the disjoint union of

- the one-point-defect edge family `x_{-j}=1^{r-1}`, of density `2q`, and
- the star edge family `x_{-j}=0^{r-1}` with odd `y` parity, of density `q`.

Thus

\[
p_{x_j}=3q.
\tag{4.2}
\]

Consequently every certified pivot fails direct payment:

\[
I_Z=3rq>rq=rp_{y_i}.
\tag{4.3}
\]

The control coordinates are not C12-certified. Indeed their pivotality-event density is `3q`. For any atom of density `d=2^{-s}`,

\[
\frac{|d-3q|}{d}=|1-3\,2^{s-r}|\ge\frac14,
\]

whereas the allowed relative error is only `1/(16s)<=1/16`. Density mismatch alone therefore rules out every C12 atom.

So the `y_i` are certified rows, the `x_j` are exceptional endpoints, and this is an exact TRUE_STALL family.

But

\[
J_{\rm certified}=mq,
\qquad
J_{\rm exceptional}=3rq,
\]

hence

\[
\frac{J_{\rm certified}}{J_{\rm exceptional}}=\frac{m}{3r},
\tag{4.4}
\]

which is arbitrarily large at fixed `r` as `m->infinity`.

### Consequence
No dimension-free argument can simply charge every true-stalled certified influence mass to the total exceptional endpoint influence mass. Large fan-in to a few exceptional controls is a genuine obstruction to that replacement.

## 5. The obstruction family itself satisfies FEI with constant four

The same family shows what information the replacement must retain. Since the two control atoms `0^r` and `1^r` are disjoint,

\[
G_{r,m}(x,y)
=(1-2\delta_{1^r}(x))
 (1-\delta_{0^r}(x)+\delta_{0^r}(x)\chi_Y(y)),
\tag{5.1}
\]

where `chi_Y(y)=(-1)^{y_1+...+y_m}`.

Its nonzero Walsh magnitudes are exactly:

- one coefficient of magnitude `1-3q`;
- `3*2^{r-1}` coefficients of magnitude `q`;
- `2^{r-1}-1` coefficients of magnitude `3q`.

Therefore

\[
I(G_{r,m})=J(G_{r,m})=q(3r+m),
\tag{5.2}
\]

and

\[
\begin{aligned}
H(G_{r,m})
={}&(1-3q)^2\log_2\frac1{(1-3q)^2}
+3rq\\
&+\left(\frac{9q}{2}-9q^2\right)
  (2r-\log_2 9).
\end{aligned}
\tag{5.3}
\]

For `r>=3`, `q<=1/8`. With `u=3q`,

\[
(1-u)^2\log_2\frac1{(1-u)^2}
\le \frac{2u}{\ln2}=\frac{6q}{\ln2}.
\tag{5.4}
\]

Also

\[
\left(\frac{9q}{2}-9q^2\right)\log_2 9
\ge \frac{27q}{8}\log_2 9
>\frac{6q}{\ln2}.
\tag{5.5}
\]

Thus the negative `-log_2 9` spectral credit already pays the entire main-coefficient entropy term, and the remaining positive terms are strictly below `12rq`. Hence

\[
\boxed{
H(G_{r,m})<12rq<4q(3r+m)=4J(G_{r,m}).
}
\tag{5.6}
\]

So the arbitrarily large certified-to-exception fan-in in (4.4) is completely harmless for FEI. The missing campaign-A payment is not raw endpoint influence. It must preserve a Shannon/interference credit that notices many certified pivots sharing the same exceptional geometry.

This is exactly the sort of negative-credit phenomenon that a coarse support-mass transfer would erase.

## 6. Exact computation

`CHECK_TRUE_STALL.py` uses exact rational Walsh transforms and exact rational influences. It checks:

- `F_{r,m}` for `1<=r<=4`, `1<=m<=4`: every coordinate influence equals `2^{-r}`, spectral and physical influence agree, and the finite instances satisfy `H<4J`;
- the closed-kernel false-positive family `F_{1,m}` for `2<=m<=8`, including the exact half-cube symmetric difference of parity with every codimension-one atom;
- `G_{r,m}` for `r=3,4` and `m=2,3,4`: control influence `3q`, pivot influence `q`, exact Walsh magnitude counts, exact spectral influence `q(3r+m)`, and finite-instance `H<4J`.

Checker SHA-256:

`140fab99adedd64700105d435e8a64f0e6c5cc44e104cd3bf2270178226c6675`.

The universal inequality (5.6) is proved analytically above; the entropy calculation in the checker is only a finite sanity check.

## 7. Full-problem change and next exact missing implication

**Old missing implication:** after the stationary selector stalls, infer that an empty closed C12 kernel is the true exceptional critical core and pay that sector.

**New proved inference:** empty closed kernel is not the true exception. The adaptive compiler can be strengthened to use every directly admissible C12 witness. Any `H/J>12` obstruction localizes to a minimum-dimensional **TRUE_STALL** state, and every certified row in such a state has a strict-influence path to a genuinely non-certified endpoint.

**Exact failed replacement:** total exceptional endpoint influence cannot pay total certified influence; `G_{r,m}` has ratio `m/(3r)` with `m` unbounded.

**Next missing implication:** prove a fan-in/overlap-sensitive Shannon payment along the strict-influence forest. It must retain the negative information/spectral credits generated when many certified rows share the same exceptional controls, rather than charging each incoming row independently. A sufficient version would bound the total unpaid restriction entropy of a TRUE_STALL core by `O(J)` using those shared-endpoint credits.

This would plug directly into campaign A's physical restriction telescope. No such universal bound is proved here.

**Outcome:** `ESSENTIAL_STEP_APPLIED` for the stronger critical-core reduction; the naive exceptional-mass replacement is `CANDIDATE_REFUTED`. Full FEI remains open.
