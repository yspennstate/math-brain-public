# B18 FEI proof integration — synchronized mixed-corner / Han block descent

**Date:** 21 September 2026  
**Fleet scope:** fleet04/B18  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / PROVED a new universal synchronized block lemma. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim is made.

## 0. Fresh state and exact unpaid implication

This run follows `FEI-PROOF-NUMERICS-SPRINT-20260921T120803Z`, whose fleet04/B18 assignment is a unified decomposition with a summable influence budget. The fresh scientific head observed before this derivation was master `3cb9106df20e50bbe05aa92d17024b03d9d053b4`.

The compatible inputs used are:

1. fleet04/B18, `20260921T134305Z-mixed-corner-budget/REPORT.md`, blob `ed2b2cce2cd2b4b8f1014d9da9655968f1adb541`: for
   \[
   \Gamma_2(f)=\sum_{i<j}\beta_{ij}(f),
   \]
   where `beta_ij` is the density of mixed `1-versus-3` `(i,j)`-faces,
   \[
   H(f)\le \frac3{\ln2}I(f)+\frac12\Gamma_2(f),
   \]
   and mixed-corner variation is paid exactly once on a coordinate restriction tree. The same report identifies the missing corner-heavy branch: find a proper block that removes a definite fraction of the corner budget without losing the influence bookkeeping.
2. fleet02/B18, `fleet-2026-09-21/fleet02/B18/20260921T133721Z-han-credit-block-descent/REPORT.md`: on a restriction-maximal ratio core `r=H/I`, for every fixed block size `k=n-q`, the local excesses
   \[
   e_A=\Delta_AH-rI_A\ge0
   \]
   obey
   \[
   \Gamma_q^{\rm Han}:=
   \frac{\sum_{|A|=k}e_A}{\sum_{|A|=k}(I-I_A)}
   =
   \frac{\sum_{|A|=k}R_A-\binom nk A_q}
        {\binom{n-1}{k}I},
   \]
   retaining the Han dependence credit `A_q>=0`.
3. fleet03/B18, `20260921T100020Z-block-selector-compiler/REPORT.md`, blob `4d0a67f151c9fd9674bd985460c33113c3363418`: physical block influence costs telescope exactly, and a universal proper-block erasure selector would compile to full FEI.
4. fleet04/B17, `B17-20260921T131430Z-selector-composition/REPORT.md`: rare one-point selector geometry is not itself an obstruction; balanced one-point selector substitution has a uniform selector toll below `4.6`.
5. the fresh fleet01/B16 projective-resolvent report at blob `cd14c137d9a965742ca45a71f4134dd910b337e0` supplies a separate signed-transport payment. No signed disintegration hypothesis from that route is assumed here.

The exact question attacked here is narrower than the full corner-compression lemma:

> Can one choose **the same proper physical block** that (a) contracts the mixed-corner/influence ratio by a definite factor and (b) has restriction-ratio loss controlled by the fixed-cardinality Han toll, rather than obtaining those two blocks from unrelated averaging arguments?

The answer is **yes**, with exact constants. This synchronizes the two freshest B18 mechanisms. It does **not** yet bound the Han toll by a dimension-independent summable quantity, so it is not full FEI.

---

## 1. Exact corner loss of a physical block

Let `f:{-1,1}^n->{-1,1}` be nonconstant and assume all `n>=2` displayed coordinates are relevant. Write
\[
I=I(f),\qquad \Gamma=\Gamma_2(f),\qquad R=\Gamma/I.
\]
For a nonempty proper block `A subsetneq [n]`, write `f_a` for the `2^{|A|}` restrictions obtained by fixing `A` uniformly, and put
\[
I_A=\sum_{i\in A}\operatorname{Inf}_i(f),
\qquad
J_A:=I-I_A=2^{-|A|}\sum_a I(f_a)>0.
\tag{1.1}
\]
Define the mixed-corner loss
\[
D_A:=\Gamma-2^{-|A|}\sum_a\Gamma_2(f_a).
\tag{1.2}
\]

### Lemma 1.1 — exact block corner deletion — **PROVED**

For every block `A`,
\[
\boxed{
D_A=\sum_{\{i,j\}:\,\{i,j\}\cap A\ne\varnothing}\beta_{ij}(f).
}
\tag{1.3}
\]

#### Proof

A residual mixed-corner statistic `beta_ij` survives a restriction of `A` only when both `i,j` lie outside `A`. For such a pair, averaging `beta_ij(f_a)` over the uniform assignments `a` is exactly `beta_ij(f)` by conditioning on the coordinates in `A`. Hence
\[
2^{-|A|}\sum_a\Gamma_2(f_a)
=
\sum_{i<j,\ i,j\notin A}\beta_{ij}(f),
\]
and subtracting from `Gamma` proves (1.3). QED.

Thus the corner budget is literally a nonnegative weighted graph on the relevant physical coordinates, and restricting `A` deletes every edge incident to `A`.

Define the **corner surplus**
\[
s_A:=D_A-RI_A.
\tag{1.4}
\]
Then, using (1.1),
\[
\boxed{
R-\overline R_A=\frac{s_A}{J_A},
\qquad
\overline R_A:=
\frac{2^{-|A|}\sum_a\Gamma_2(f_a)}
     {2^{-|A|}\sum_a I(f_a)}.
}
\tag{1.5}
\]
So `s_A/J_A` is exactly the decrease in the influence-weighted mean corner ratio after restricting `A`.

---

## 2. Fixed-cardinality corner averaging

Fix `1<=k<=n-1`, put `q=n-k`, and average over all `N_k=binom(n,k)` blocks of size `k`.

A fixed mixed edge `{i,j}` is missed exactly when all `k` chosen coordinates lie among the other `n-2` vertices. Therefore
\[
\frac1{N_k}\sum_{|A|=k}D_A
=
\left(1-\frac{q(q-1)}{n(n-1)}\right)\Gamma.
\tag{2.1}
\]
Also
\[
\frac1{N_k}\sum_{|A|=k}I_A=\frac kn I.
\tag{2.2}
\]
Subtracting `R` times (2.2) from (2.1) gives
\[
\boxed{
\frac1{N_k}\sum_{|A|=k}s_A
=
\frac{kq}{n(n-1)}\Gamma.
}
\tag{2.3}
\]
Meanwhile
\[
\sum_{|A|=k}J_A
=
\binom{n-1}{k}I
=
\frac qnN_k I.
\tag{2.4}
\]
Hence if blocks are weighted by
\[
w_A:=\frac{J_A}{\sum_{|B|=k}J_B},
\tag{2.5}
\]
then
\[
\boxed{
\sum_{|A|=k}w_A\frac{s_A}{J_A}
=\frac{k}{n-1}R.
}
\tag{2.6}
\]
This identity holds for every Boolean function; no extremality is used yet.

---

## 3. Synchronization with the exact Han-credit toll

Now assume `f` is a **restriction-maximal ratio core**:
\[
r:=H(f)/I(f)
\]
is at least the ratio of every nonconstant physical restriction descendant. Then for every proper block
\[
e_A:=\Delta_AH-rI_A\ge0.
\tag{3.1}
\]
Put
\[
\ell_A:=e_A/J_A.
\tag{3.2}
\]
By the fleet02/B18 fixed-cardinality identity,
\[
\boxed{
\sum_{|A|=k}w_A\ell_A=\Gamma_q^{\rm Han}.
}
\tag{3.3}
\]
Equations (2.6) and (3.3) are averages under the **same weights**. This is the key point that was absent when the corner and Han mechanisms were considered separately.

### Theorem 3.1 — synchronized corner/Han block selector — **PROVED**

For every `1<=k<=n-1`, there is a `k`-coordinate proper block `A` such that simultaneously
\[
\boxed{
\overline R_A
\le
\left(1-\frac{k}{2(n-1)}\right)R
}
\tag{3.4}
\]
and
\[
\boxed{
\ell_A
\le
\left(\frac{2(n-1)}k-1\right)\Gamma_q^{\rm Han}.
}
\tag{3.5}
\]

#### Proof

Set
\[
c_A:=s_A/J_A=R-\overline R_A,
\qquad
C:=\frac{k}{n-1}R,
\qquad
G:=\Gamma_q^{\rm Han}.
\]
Then `sum w_A c_A=C` and `sum w_A ell_A=G`, with `ell_A>=0` and `c_A<=R` because `overline R_A>=0`.

If `G=0`, every `ell_A=0`, and some block has `c_A>=C`, which is stronger than both claims.

Assume `G>0` and set
\[
\lambda=\frac{C}{2G}.
\]
Averaging gives
\[
\sum_Aw_A(c_A-\lambda\ell_A)=C-\lambda G=C/2.
\]
Hence some block `A` obeys
\[
c_A-\lambda\ell_A\ge C/2.
\tag{3.6}
\]
Since `ell_A>=0`, (3.6) gives `c_A>=C/2`, which is (3.4). Also `c_A<=R`, so
\[
\lambda\ell_A
\le c_A-C/2
\le R-C/2.
\]
Therefore
\[
\ell_A
\le
\frac{R-C/2}{\lambda}
=
\left(\frac{2(n-1)}k-1\right)G,
\]
proving (3.5). QED.

This is a true **same-block** theorem: the corner-compressing block and the low-Han-loss block are not selected in two incompatible existential arguments.

---

## 4. Half-block corollary and an actual child

Take
\[
k=\lfloor n/2\rfloor,
\qquad q=\lceil n/2\rceil.
\]
Then
\[
\frac{k}{2(n-1)}\ge\frac14
\quad(n\ge3),
\]
with the `n=2` case even stronger, and
\[
\frac{2(n-1)}k-1\le3.
\]
Thus Theorem 3.1 gives a proper half-block `A` with
\[
\boxed{
\overline R_A\le\frac34R,
\qquad
\ell_A\le3\Gamma_q^{\rm Han}.
}
\tag{4.1}
\]

Now put a probability distribution on the nonconstant children by
\[
\Pr(a)=\frac{2^{-k}I(f_a)}{J_A}.
\tag{4.2}
\]
Restriction-maximality gives `r(f_a)<=r`. By the exact telescopes,
\[
\mathbb E_a[r-r(f_a)]=\ell_A,
\qquad
\mathbb E_a\frac{\Gamma_2(f_a)}{I(f_a)}=\overline R_A.
\tag{4.3}
\]
Therefore, for every `theta` with `3/4<theta<1`, some nonconstant child satisfies both
\[
\boxed{
\frac{\Gamma_2(f_a)}{I(f_a)}\le\theta R
}
\tag{4.4}
\]
and
\[
\boxed{
r(f_a)
\ge
r-rac{12\theta}{4\theta-3}\Gamma_q^{\rm Han}.
}
\tag{4.5}
\]
Indeed the expectation of
\[
\frac{r-r(f_a)}{L}
+
\frac{\Gamma_2(f_a)/I(f_a)}{\theta R},
\qquad
L:=\frac{12\theta}{4\theta-3}\Gamma_q^{\rm Han},
\]
is at most one by (4.1)-(4.3), so some child has both nonnegative summands at most one. If `Gamma_q^Han=0`, all influence-weighted children have the same ratio `r` and one of them has corner ratio at most `3R/4`.

For the concrete choice `theta=0.9`,
\[
\boxed{
R(f_a)\le0.9R(f),
\qquad
r(f_a)\ge r(f)-18\Gamma_q^{\rm Han}.
}
\tag{4.6}
\]
The fleet02 source-admissible estimate
\[
\Gamma_q^{\rm Han}
\le
\frac{n}{qI}
\left\{
\frac2{\ln2}(n-q)\varepsilon_q-
\left[h_q-\frac qnH\right]
\right\}
\tag{4.7}
\]
has `n/q<=2` at this half scale, so (4.6) also yields the explicit one-step toll
\[
r(f_a)
\ge r(f)-
\frac{36}{I}
\left\{
\frac2{\ln2}(n-q)\varepsilon_q-
\left[h_q-\frac qnH\right]
\right\}.
\tag{4.8}
\]
The Han deficit is retained with its negative sign.

---

## 5. What this solves and what remains

The preceding B18 report left open a hybrid corner-compression statement: in the corner-heavy regime, find a proper block that removes a definite fraction of the mixed-corner budget **and** is compatible with the restriction payment. The present theorem proves the geometric and recursion synchronization part exactly:

- a half-block can be chosen so the influence-weighted residual corner ratio contracts by at least `1/4`;
- **the same block** has ratio-loss toll at most three times the optimal fixed-cardinality Han toll;
- an actual nonconstant child can be chosen with a strict corner-ratio contraction and an explicit multiple of that Han toll.

Thus the previous problem is reduced further. The missing universal implication is no longer “can the corner block and Han block be the same?” They can. The remaining scalar obstruction is:

> **OPEN summable-Han-toll lemma.** Control the exact half-scale toll `Gamma_q^Han`, or the bracket in (4.7), by a quantity that is summable along the synchronized corner-contraction descent, uniformly in dimension.

A particularly sharp sufficient direction suggested by the one-point selector is an inverse-corner estimate of the form
\[
\Gamma_{\lceil n/2\rceil}^{\rm Han}
\lesssim \frac{1}{R}
\quad\text{on corner-heavy restriction-maximal cores},
\tag{5.1}
\]
but **(5.1) is OPEN here**. It is not inserted as an assumption into any proved statement. The one-point family and small-dimensional exhaustive data support testing this scaling, but they do not prove it.

The fresh fleet04/B17 composition theorem explains why this is a plausible scale to examine: the canonical one-point selector has `R=n-1` while its FEI/selector cost stays bounded. The new theorem says precisely where that cheapness must appear in the Han block toll if the mechanism extends universally.

---

## 6. Decisive finite calculation

A fresh checker for this run enumerated Boolean functions up to global sign through `n=4`, retained only functions whose `H/I` is maximal among all their nonconstant physical restriction descendants, and tested Theorem 3.1 at `k=floor(n/2)`.

Counts of restriction-maximal nonconstant cores were:

- `n=2`: 7;
- `n=3`: 27;
- `n=4`: 679;
- total: **713**.

There were **zero violations** of the synchronized same-block inequalities. Among these cores the largest observed product
\[
R\,\Gamma_q^{\rm Han}
\]
was `4.207426653595761`, attained by the four-bit one-point defect (`R=3`, `Gamma_q^Han=1.4024755511985871`). This number is only exploratory evidence for the OPEN inverse-corner target (5.1), not a universal constant.

The analytic theorems above do not depend on this enumeration.

---

## 7. Claim ledger

### PROVED here

- exact block mixed-corner deletion identity (1.3);
- exact fixed-cardinality surplus average (2.3) and common-weight corner contraction identity (2.6);
- synchronized same-block corner/Han selector (3.4)-(3.5);
- half-block contraction/toll bound (4.1);
- actual-child tradeoff (4.4)-(4.6), at the exact scope of a restriction-maximal core.

### COMPUTATIONAL SUPPORT

- exhaustive-up-to-global-sign check through `n=4` on 713 restriction-maximal nonconstant cores: zero theorem violations;
- largest observed `R Gamma_q^Han = 4.207426653595761` in that search.

### OPEN / CONDITIONAL

- the inverse-corner Han-toll estimate (5.1) or any other dimension-independent summable replacement;
- conversion of the synchronized descent into a full universal FEI constant without an additional summability theorem;
- full uniform-cube Fourier entropy-influence.

### REFUTED / PRESERVED

- the preceding refutation of a universal direct `Gamma_2<=K I` bound remains in force; the one-point defect has `Gamma_2=(n-1)I`.
- no every-coordinate selector is claimed.
- no signed-projective disintegration from B16 is assumed.

**Full FEI remains OPEN / NOT PROVED.**
