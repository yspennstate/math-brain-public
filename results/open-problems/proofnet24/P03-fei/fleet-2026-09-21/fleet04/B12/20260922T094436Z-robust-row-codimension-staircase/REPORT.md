# fleet04/B12 — robust-row codimension staircase and a direct influence-relative address payment

**Run:** `B12-20260922T094436Z-r46`  
**Classification:** `ESSENTIAL_STEP_APPLIED / ROBUST_ROW_CODIMENSION_STAIRCASE / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Current source state and the completed peer result consumed


The newest completed compatible `fleet02` result consumed substantively is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`,
blob `68e838a493671ed5c27a29468dfcce7bb621d860`.

Its exact implication used below is candidate-independent. If the terminal-class inequality fails, a minimum-dimensional ratio core may be chosen centered, essential and tensor-primitive and satisfies, for every nonempty physical block `A`,

\[
U_A\ge K D_A,
\]
where
\[
U_A=\sum_{i\in A}h_2(q_i)-W_A,
\qquad
D_A=\sum_{i\in A}q_i+C_A,
\qquad W_A,C_A\ge0.
\]
In particular, taking `A={i}` gives the exact singleton consequence

\[
\boxed{h_2(q_i)\ge Kq_i\qquad\text{for every physical coordinate }i.}
\tag{0.1}
\]

The current-hour `fleet02/B12` invocation had started but had no completed source-bound result at the time this proof was frozen, so I do not consume an unfinished artifact. Its newest completed prior report is tied to the now-refuted fixed `Gamma^dagger` candidate and is therefore not spent as universal credit.

I also preserve and use the pairwise integrability behind fleet04/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`,
blob `0e8c2cc28da81af8843b565cb47285684b164480`.

Crucially, I do **not** use or assume `sum_k d_k=O(J)`. The theorem below avoids the raw depth bank entirely.

## 1. Setup

Work in the centered character gauge, so

\[
0<q_i=\operatorname{Inf}_i(g)\le\frac12,
\qquad
J=\sum_iq_i.
\]

For a derivative row `i`, let

\[
E_i=\{y:D_i g(y)\ne0\},\qquad \mu(E_i)=q_i.
\]

Assume `E_i` is relative-`eta` near a coordinate subcube

\[
Q_i=\{y_{F_i}=a_i\},
\qquad s_i:=\mu(Q_i)=2^{-r_i},
\qquad r_i:=|F_i|,
\]
with

\[
\varepsilon_i:=\mu(E_i\triangle Q_i)\le\eta q_i,
\qquad 0\le\eta<\frac12.
\tag{1.1}
\]

For `k\ne i`, write

\[
p_{ik}=\Pr[1_{E_i}(Y)\ne1_{E_i}(Y+e_k)].
\]

The previous B12 trigger-boundary lemma gives, for every `k in F_i`,

\[
\boxed{p_{ik}\ge2(1-2\eta)q_i.}
\tag{1.2}
\]

## 2. Pairwise transfer lemma: every trigger carries comparable physical influence

### Lemma 2.1

For every pair `i\ne k`,

\[
\boxed{p_{ik}=p_{ki}\le2q_k.}
\tag{2.1}
\]

Consequently, for every trigger `k in F_i`,

\[
\boxed{q_k\ge(1-2\eta)q_i.}
\tag{2.2}
\]

### Proof

Freeze all coordinates except `i,k` and write the four Boolean values as `a,b,c,d in {+-1}` in the natural square order. The support status of the two `i`-edges differs between the two `k`-layers iff exactly one of `a!=b` and `c!=d` holds. In signs, this is equivalent to

\[
(ab)(cd)=-1,
\]
that is `abcd=-1`.

The support status of the two `k`-edges differs between the two `i`-layers iff exactly one of `a!=c` and `b!=d` holds, which is likewise equivalent to

\[
(ac)(bd)=-1,
\]
again `abcd=-1`. Thus the two boundary events agree pointwise on every Boolean square, proving `p_{ik}=p_{ki}`. This is the support-level part of the same mixed-derivative integrability used by B18.

For any set of measure `q_k`, the directional boundary probability is at most the probability that either endpoint lies in the set:

\[
p_{ki}\le \Pr(Y\in E_k)+\Pr(Y+e_i\in E_k)=2q_k.
\]

Combine this with (1.2) to obtain (2.2). QED.

This step is important because it replaces an incidence count by **actual influence on each trigger coordinate**. No ambient dimension and no derivative depth appear.

## 3. New theorem: a direct influence-relative address payment

Because `i notin F_i`, (2.2) implies

\[
J
\ge q_i+\sum_{k\in F_i}q_k
\ge \bigl[1+(1-2\eta)r_i\bigr]q_i.
\]
Hence:

### Theorem 3.1 — single-row address payment

Every relative-`eta` robust row obeys

\[
\boxed{
\bigl[1+(1-2\eta)r_i\bigr]q_i\le J.
}
\tag{3.1}
\]

Equivalently,

\[
\boxed{
r_iq_i\le\frac{J-q_i}{1-2\eta}.}
\tag{3.2}
\]

At the live threshold `eta=1/16`,

\[
\boxed{
\left(1+\frac78r_i\right)q_i\le J,
\qquad
r_iq_i\le\frac87(J-q_i)<\frac87J.
}
\tag{3.3}
\]

Thus the physical trigger address of **one robust row** is already influence-relative in the natural weighted units `r_i q_i`: it costs at most `8J/7`, with no `n`, `log n`, alphabet-size term, or `sum d_k` payment.

This does **not** yet sum over all robust rows: different rows may reuse the same trigger influence. That nonreuse issue remains real. The point here is that the obstruction has moved from ambient dimension to an explicit overlap problem among physically influential trigger coordinates.

## 4. New terminal codimension staircase

Define

\[
R(q):=\frac{h_2(q)}q,
\qquad 0<q\le\frac12.
\]

A direct derivative computation gives

\[
R'(q)
=\frac{q h_2'(q)-h_2(q)}{q^2}
=\frac{\log_2(1-q)}{q^2}<0.
\tag{4.1}
\]

Hence for each `K>2` there is a unique `q_K in (0,1/2)` satisfying

\[
R(q_K)=K.
\tag{4.2}
\]

The singleton terminal inequality (0.1) and strict monotonicity imply

\[
\boxed{q_i\le q_K.}
\tag{4.3}
\]

On the other hand, (1.1) gives

\[
|s_i-q_i|\le\varepsilon_i\le\eta q_i,
\]
so

\[
2^{-r_i}=s_i\le(1+\eta)q_i\le(1+\eta)q_K.
\]
Therefore:

### Theorem 4.1 — terminal robust-row codimension staircase

Every relative-`eta` robust row in an all-block terminal core at level `K>2` satisfies

\[
\boxed{
r_i\ge
\left\lceil
\log_2\frac1{(1+\eta)q_K}
\right\rceil.}
\tag{4.4}
\]

Combining with (3.1),

\[
\boxed{
\frac{q_i}{J}
\le
\frac1{1+(1-2\eta)r_i}.}
\tag{4.5}
\]

At `eta=1/16`, for an integer `m>=2`, define

\[
q_m^*=\frac{16}{17}\,2^{-(m-1)},
\qquad
K_m:=\frac{h_2(q_m^*)}{q_m^*}.
\tag{4.6}
\]

If `K>K_m`, then `(17/16)q_K<2^{-(m-1)}`, so every robust row has `r_i>=m` and

\[
\boxed{
\frac{q_i}{J}\le\frac8{8+7m}.}
\tag{4.7}
\]

The first useful thresholds are

\[
\begin{array}{c|c|c}
 m & K_m & q_i/J\text{ cap}\cr
\hline
2 & 2.1196929110343698\ldots & 4/11\\
3 & 3.3452879913553929\ldots & 8/29\\
4 & 4.4417546835639960\ldots & 2/9\\
5 & 5.4868683012557699\ldots & 8/43\\
6 & 6.5087306636825764\ldots & 4/25
\end{array}
\tag{4.8}
\]

For example, at the concrete terminal target `K=4`,

\[
q_K=0.1564173549642720155\ldots,
\]
so every relative-`1/16` robust row has at least three physical triggers and

\[
\boxed{q_i\le\frac8{29}J.}
\tag{4.9}
\]

As a calibration to the current record lower-bound scale, taking

\[
K_{\rm rec}:=
6.521845710923046575-\frac2{\ln2}
=3.6364556291451197602\ldots
\]
again lies strictly between `K_3` and `K_4`. Thus the same forced three-trigger / `8J/29` cap already applies at that phase-corrected scale.

## 5. Why this is a new obstruction rather than another depth estimate

The previous B12 aggregate theorem converted robust rows into the weighted bank

\[
\sum_k (h_2(q_k)-Kq_k)d_k,
\]
which was honest but left an unpaid depth factor. The present argument deliberately changes mechanism:

1. use Boolean-square integrability only **pairwise**, to transfer trigger boundary to actual trigger influence;
2. spend the global first-moment budget `J` immediately, before any row aggregation;
3. combine terminal singleton entropy with dyadic subcube geometry to force a discrete codimension staircase.

The result is a direct dimension-free exclusion of heavy, low-codimension robust rows. No statement of the form `sum_k d_k=O(J)` is used or needed.

The new remaining obstruction is sharper. If a terminal counterexample has substantial robust-row mass, it must either

* be distributed among many individually small rows satisfying the staircase, or
* exhibit strong overlap among the physically influential trigger sets when one tries to aggregate the single-row payments.

That overlap problem is now the only place where B18's full column conservation may need to re-enter. It should not be replaced by an unjustified global depth bound.

## 6. Verification

`CHECKER.py` evaluates the staircase thresholds at 70-decimal precision and checks the exact rational caps

\[
8/29,\qquad 2/9,\qquad 4/25,
\]
for `m=3,4,6`, together with the `K=4` and record-scale placements. It returns `PASS`.

The analytic claims do not depend on floating point: monotonicity is the exact identity (4.1), trigger comparability is the Boolean-square identity plus a union bound, and all `eta=1/16` payment constants are rational.

## 7. Status

This is an `ESSENTIAL_STEP_APPLIED` on the candidate-independent terminal-core branch. It gives a new influence-relative row-address payment and a quantitative codimension staircase for robust near-subcube rows. It does **not** close the simultaneous trigger-overlap problem, the nonrobust rows, or the all-prime-gate envelope. Therefore full uniform-cube FEI remains **OPEN / NOT PROVED**.
