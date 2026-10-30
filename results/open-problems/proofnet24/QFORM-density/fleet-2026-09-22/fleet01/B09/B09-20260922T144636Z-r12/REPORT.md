# fleet01/B09 — overlap-one Schur-cut aggregation

Run: `B09-20260922T144636Z-r12`  
Assignment: `Bilinear block mechanism`  
Outcome: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and status

The full target remains OPEN. For every dimension, every independent real coordinates `X_i` with densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, one seeks a universal finite `C` such that

\[
\|p_{X^TAX}\|_\infty\le C,
\]

or equivalently a universal linear small-ball estimate

\[
\Pr\{X^TAX\in I\}\le C|I|.
\]

The owner additionally asks for a continuous density; continuity is tracked separately below. This report proves a new exact-rank-three overlap-one branch and an arbitrary-rank determinant identity. It does **not** handle arbitrary extra spectrum, and therefore is not a full solution.

The live corrections used here include the failures of: law-uniform pointwise quadratic-phase decay; post-rotation independence; a rank-two cross block alone at `L^infinity`; a universal single physical Schur-pivot extraction; and a fixed local principal-block/rank-three-cross-cut dichotomy. In particular the family

\[
A_m=[1]\oplus J_m/m\oplus(-J_m/m)
\]

from `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` must be handled by aggregation rather than a single physical `3 x 2` packet.

## 2. Named partner theorem actually applied

The assigned partner is fleet02/B09. Its canonical theorem is:

- repository: `yspennstate/math-open-problems`;
- commit: `a47c679eb9f7788b5c3c2a900ce516ec11de8d9b`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260922T124417Z-fleet02-B09-QFORM-r2/REPORT.md`;
- theorem: `QFORM-RANK2-SCHUR-PIVOT-v1`.

If an original physical pivot has coefficient `d != 0` and, after completing its square, the Schur cross block across two disjoint original-coordinate banks has rank exactly two with nonzero singular-value product `Delta`, then

\[
\boxed{
\|p_Q\|_\infty\le 4\sqrt6\,|d|^{-1/2}\Delta^{-1/4}.
}\tag{2.1}
\]

The partner proof retains arbitrary quadratic terms on both banks and arbitrary permitted input laws. Equation (2.1) is applied quantitatively in Theorem 4.1 below, after a new aggregate construction of the rank-two Schur cut.

The partner's later correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, canonical commit `17dec75dc10459933f8bfde30daa86d1c6d90a6a`, is also respected: the present argument does **not** assert that every target matrix has such a pivot/cut.

## 3. Exact arbitrary-rank overlap-one / Schur identity

Fix a real symmetric `n x n` matrix `A` and a coordinate `i` with

\[
a:=A_{ii}\ne0.
\]

Write `\bar i=[n]\setminus\{i\}` and let

\[
S_i=A_{\bar i,\bar i}-\frac{A_{\bar i,i}A_{i,\bar i}}{a}
\tag{3.1}
\]

be the physical scalar-pivot Schur complement.

For disjoint two-sets `K,L subset \bar i`, define the overlap-one minor

\[
m_{i;K,L}:=\det A[\{i\}\cup K,\{i\}\cup L].
\tag{3.2}
\]

Define its total pivot-based overlap-one energy

\[
\mathcal M_{1,i}(A)
:=
\sum_{\substack{K,L\subset\bar i\\|K|=|L|=2\\K\cap L=\varnothing}}
 m_{i;K,L}^2.
\tag{3.3}
\]

### Lemma 3.1 — exact Schur conversion

For every such `K,L`,

\[
\boxed{
m_{i;K,L}=a\,\det S_i[K,L].
}\tag{3.4}
\]

Consequently

\[
\boxed{
\mathcal M_{1,i}(A)
=a^2
\sum_{\substack{|K|=|L|=2\\K\cap L=\varnothing}}
\det S_i[K,L]^2.
}\tag{3.5}
\]

**Proof.** Order the selected row and column sets with `i` first. The selected `3 x 3` matrix is

\[
\begin{pmatrix}
a&A_{iL}\\
A_{Ki}&A_{KL}
\end{pmatrix}.
\]

Because `a != 0`, the scalar block-determinant identity gives

\[
\det
\begin{pmatrix}
a&A_{iL}\\A_{Ki}&A_{KL}
\end{pmatrix}
=a\det\left(A_{KL}-A_{Ki}A_{iL}/a\right)
=a\det S_i[K,L].
\]

Squaring and summing proves (3.5). No rank assumption has been used. QED.

### Lemma 3.2 — random physical cut identity

Choose a Bernoulli half-cut `P | P^c` of `\bar i`, independently placing every residual physical coordinate in `P` with probability `1/2`. Put

\[
N_P=S_i[P,P^c].
\]

For a rectangular matrix `N`, write

\[
E_2(N):=
\sum_{\substack{|K|=2\\|L|=2}}
\det N[K,L]^2
=
\sum_{r<s}s_r(N)^2s_s(N)^2.
\tag{3.6}
\]

Then

\[
\boxed{
\mathbb E_P E_2(N_P)
=
\frac{\mathcal M_{1,i}(A)}{16a^2}.
}\tag{3.7}
\]

**Proof.** A fixed ordered disjoint pair `(K,L)` with `|K|=|L|=2` contributes to `E_2(N_P)` exactly on the event `K subset P`, `L subset P^c`, which has probability `2^{-4}=1/16`. Sum (3.5) termwise. QED.

This identity is the key new structural step: it aggregates **all** overlap-one minors sharing the same physical pivot before any reciprocal minor is paid.

## 4. Exact-rank-three endpoint

### Theorem 4.1 — `QFORM-RANK3-OVERLAP1-SCHUR-CUT-v1`

Assume now that `A` has exact rank three. Fix a coordinate `i` with `a=A_ii != 0` and `\mathcal M_{1,i}(A)>0`. Then for every independent input vector whose coordinate densities are bounded by one, `Q=X^TAX` has an essentially bounded density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le
8\sqrt3\,|a|^{-1/4}\,\mathcal M_{1,i}(A)^{-1/8}.
}\tag{4.1}
\]

Hence every interval `I` obeys the direct linear estimate

\[
\boxed{
\Pr\{Q\in I\}
\le
8\sqrt3\,|a|^{-1/4}\mathcal M_{1,i}(A)^{-1/8}|I|.
}\tag{4.2}
\]

**Proof.** Since `a != 0`, scalar Schur congruence gives

\[
\operatorname{rank}A=1+\operatorname{rank}S_i.
\]

Thus `rank(S_i)=2`. Every cross block `N_P=S_i[P,P^c]` has rank at most two. By (3.7), some cut satisfies

\[
E_2(N_P)
\ge
\frac{\mathcal M_{1,i}(A)}{16a^2}>0.
\tag{4.3}
\]

For this cut, `rank(N_P)=2`. If its two nonzero singular values have product `Delta_P`, then because the rank is exactly two,

\[
E_2(N_P)=\Delta_P^2.
\]

Therefore

\[
\Delta_P
\ge
\frac{\mathcal M_{1,i}(A)^{1/2}}{4|a|}.
\tag{4.4}
\]

Apply the assigned partner theorem (2.1) with physical pivot `i` and residual banks `P,P^c`:

\[
\begin{aligned}
\|p_Q\|_\infty
&\le 4\sqrt6\,|a|^{-1/2}\Delta_P^{-1/4}\\
&\le4\sqrt6\,|a|^{-1/2}
\left(\frac{\mathcal M_{1,i}^{1/2}}{4|a|}\right)^{-1/4}\\
&=8\sqrt3\,|a|^{-1/4}\mathcal M_{1,i}^{-1/8}.
\end{aligned}
\]

This is (4.1). The partner theorem supplies a density; integrating its `L^infinity` bound over an interval gives (4.2). QED.

The scaling is exact: under `A -> tA`, `a -> ta` and `\mathcal M_{1,i}->t^6\mathcal M_{1,i}`, so the right side scales as `|t|^{-1}`.

**Continuity.** The argument above proves existence of an essentially bounded density and the `O(|I|)` estimate. The partner `L^3 -> L^infinity` square-smoothing theorem used in (2.1) does not, in the cited result, supply an `L^1` characteristic-function conclusion. Therefore continuity is **not claimed** for Theorem 4.1.

## 5. Pluecker interpretation and a quantitative non-light-cone branch

Let the exact-rank-three matrix be written

\[
A=U\Lambda U^T,
\qquad U^TU=I_3,
\qquad
\Lambda=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3),
\tag{5.1}
\]

with all `lambda_j != 0`. For each three-set `I`, put

\[
w_I:=\det(U_I)^2.
\]

Cauchy--Binet gives `sum_I w_I=1`. For a physical coordinate `i`, define

\[
\delta_i:=
\sum_{\substack{K,L\subset[n]\setminus\{i\}\\|K|=|L|=2\\K\cap L=\varnothing}}
 w_{\{i\}\cup K}\,w_{\{i\}\cup L}.
\tag{5.2}
\]

Since

\[
\det A[I,J]=\det\Lambda\,\det(U_I)\det(U_J),
\]

we have the exact factorization

\[
\boxed{
\mathcal M_{1,i}(A)=|\det\Lambda|^2\delta_i.
}\tag{5.3}
\]

Let `ell_i=||U_{i,*}||_2^2`. The volume-sampling leverage identity gives

\[
\sum_{K}w_{\{i\}\cup K}=\ell_i,
\qquad
\sum_i\ell_i=3.
\tag{5.4}
\]

Hence `delta_i <= ell_i^2`, so

\[
\boxed{
\sum_i\sqrt{\delta_i}\le3.
}\tag{5.5}
\]

Also the total normalized overlap-one mass is

\[
p_1:=\sum_i\delta_i.
\tag{5.6}
\]

For `alpha>0`, define the portion based at genuinely non-light-cone coordinates

\[
p_{1,\alpha}:=
\sum_{i:\ |A_{ii}|\ge\alpha}\delta_i.
\tag{5.7}
\]

If `p_{1,alpha}>0`, let `d=max_{|A_ii|>=alpha} delta_i`. Then

\[
p_{1,\alpha}
\le \sqrt d\sum_i\sqrt{\delta_i}
\le3\sqrt d,
\]

so some qualifying coordinate satisfies

\[
\delta_i\ge p_{1,\alpha}^2/9.
\tag{5.8}
\]

Substituting (5.3) and (5.8) into Theorem 4.1 gives the dimension-free conditional branch

\[
\boxed{
\|p_Q\|_\infty
\le
8\,3^{3/4}
\bigl(\alpha |\det\Lambda| p_{1,\alpha}\bigr)^{-1/4}.
}\tag{5.9}
\]

In the target exact-rank-three regime `|lambda_j|>=1`, `|det Lambda|>=1`; therefore any fixed positive lower bounds on `alpha` and `p_{1,alpha}` close this branch universally. The only overlap-one configurations not paid by (5.9) are those whose normalized overlap-one mass is concentrated on physical coordinates with very small diagonal Rayleigh coefficient `|A_ii|`: a precise light-cone residual, rather than an arbitrary localized case.

## 6. Stress test: the family that defeats fixed local selection is now paid

Consider the source-valid exact-rank-three family

\[
A_m=[1]\oplus J_m/m\oplus(-J_m/m),\qquad m\ge2.
\tag{6.1}
\]

Its nonzero spectrum is exactly `{1,1,-1}`. Let coordinate `0` denote the singleton block. Every nonzero Pluecker triple is

\[
I=\{0,p,n\},
\]

with one positive-bank coordinate `p` and one negative-bank coordinate `n`, and

\[
w_I=1/m^2.
\]

Therefore

\[
\delta_0=\frac{(m-1)^2}{m^2},
\qquad
\delta_i=0\quad(i\ne0),
\tag{6.2}
\]

while `A_00=1`. Theorem 4.1 gives

\[
\boxed{
\|p_{X^TA_mX}\|_\infty
\le
8\sqrt3\left(\frac m{m-1}\right)^{1/4}.
}\tag{6.3}
\]

This is uniform in `m` and in every allowed input law.

More explicitly, after pivoting coordinate `0`, the residual is

\[
S_0=J_m/m\oplus(-J_m/m).
\]

Split each bank as evenly as possible between two physical sides. The resulting Schur cross block has two singular values

\[
\frac{\sqrt{r(m-r)}}m,
\qquad
\frac{\sqrt{s(m-s)}}m,
\]

and with `r=s=floor(m/2)` their product is

\[
\Delta=rac{\lfloor m^2/4\rfloor}{m^2}.
\tag{6.4}
\]

The partner theorem directly yields the slightly sharper explicit bound

\[
\|p_{X^TA_mX}\|_\infty
\le
4\sqrt6\left(\frac{m^2}{\lfloor m^2/4\rfloor}\right)^{1/4},
\tag{6.5}
\]

which equals `8 sqrt(3)` for even `m` and tends to that value for odd `m`.

This is the exact mechanism the previous local-packet route missed. A physical `3 x 2` packet in (6.1) has rank-two singular product only `1/m^2`, so any single-packet reciprocal bound deteriorates with `m`; the high-cardinality Schur cut instead aggregates `Theta(m^4)` tiny overlap-one contributions **before** the partner `L^3 -> L^infinity` cost is paid.

## 7. What this changes in the proof tree

The previous unpaid implication `QFORM-OVERLAP-ENERGY-AGGREGATION-v1` is now partially discharged in a dimension-free, product-preserving way:

- overlap-one minors sharing a nonzero physical pivot convert exactly into disjoint two-minor mass of its Schur complement;
- in exact rank three the Schur complement has rank exactly two, so a Bernoulli physical cut aggregates that mass into one genuine rank-two Schur cross block;
- the assigned partner theorem then gives a direct `O(|I|)` interval bound;
- the delocalized family `A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`, which refutes fixed local principal/cross selection, is uniformly closed by this mechanism.

The first unpaid implication is now sharper:

> **`QFORM-OVERLAP1-LIGHTCONE-OR-EXTRA-SPECTRUM-v1` (OPEN).** Extend the overlap-one payment when either (a) the relevant common physical coordinate has `A_ii=0` or arbitrarily small (the light-cone branch), or (b) extra spectral components make the scalar Schur complement rank greater than two, so `E_2` no longer equals one rank-two singular product. Any extension must retain original product provenance and aggregate before reciprocal local-minor costs.

This is compatible with the partner correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`: that correction's star-family residual has zero disjoint two-basis mass, so it lies outside Theorem 4.1 rather than contradicting it.

## 8. Verification notes

The identities (3.4)--(3.7) and the rank-three specialization were checked algebraically in the proof above. A separate finite numerical checker accompanies this report and verifies, on random exact-rank-three symmetric matrices, both the overlap-one/Schur identity and the Bernoulli-cut expectation. Those checks are sanity tests only; the proof is the exact determinant/Cauchy--Binet argument given above.

No Gaussianity, log-concavity, moment condition, compact/connected support, post-rotation independence, pointwise van-der-Corput estimate, or Monte Carlo density extremality is used.

## 9. Outcome

`ESSENTIAL_STEP_APPLIED`.

New proved items:

1. `QFORM-OVERLAP1-SCHUR-IDENTITY-v1`, valid for arbitrary symmetric rank;
2. `QFORM-RANK3-OVERLAP1-SCHUR-CUT-v1`, the exact-rank-three aggregate overlap-one endpoint (4.1)--(4.2);
3. the non-light-cone Pluecker branch (5.9);
4. a uniform proof for the exact family (6.1) that previously falsified fixed local selection.

Full QFORM remains OPEN. Continuity is not established by the new endpoint; essential boundedness and the linear interval estimate are established on the stated branch.