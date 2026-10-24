# account03/B06 — global rank-one Schur curvature aggregation

**Run:** `20260922T172229Z-account03-B06-qform-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Fresh control, scope, and dependencies

Fresh `main` control was read from `yspennstate/math-research-brain@7616d5e069b312c428e179da7d6549210f01cc42` at startup and refreshed before publication at `c639bcc078717be24746e44827785eceeaaf90f0`. The active OWNER CONTROL is revision `2026-09-22.8`; QFORM remains the sole research target and account03/B06 remains `Curved fiber integration`. The full target is unchanged: independent real physical coordinates with densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one; prove a universal essential-density bound or give a valid counterexample. Continuity is a separate desired conclusion.

The live correction inbox was reread before publication. This report does **not** use law-uniform pointwise quadratic oscillatory decay, independence after spectral rotation, an unrestricted fiber supremum, a generic X-ray bound, a conditional-density surrogate for independence, or the existence of one uniformly good physical triple. In particular it responds directly to the corrections showing that reciprocal local minors can lose powers of dimension and that product aggregation must occur before or jointly with the curved trace.

The exact assigned partner is `account04/B06`. The canonical shared handoff root and canonical math-open-problems root for that slot were both absent at startup and again at the partner refresh, so no exact-partner theorem or PASS is fabricated. Work proceeded asynchronously as instructed.

Two completed compatible results are actually used:

1. **account03/B09**, `QFORM-INDEFINITE-PAIR-SCHUR-SMOOTHING-v1`, latest canonical report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/account03-B09-20260922T171558Z-qform13/REPORT.md`. Its needed ingredient is the translation-uniform density envelope for an indefinite original-coordinate pair. For
   \[
   H=\begin{pmatrix}r&s\\s&t\end{pmatrix},\qquad D_H=|\det H|,
   \]
   and independent cap-one pair variables, arbitrary deterministic translations allowed,
   \[
   p_{Z^THZ}(u)\le 8D_H^{-1/2}\Psi(ru/D_H)\quad(r\ne0),                 \tag{0.1}
   \]
   with the symmetric version using `t`; if `r=t=0`, so `H=[[0,s],[s,0]]`,
   \[
   p_{Z^THZ}(u)\le |s|^{-1}\Psi(u/(2s)).                              \tag{0.2}
   \]
   Here
   \[
   \Psi(x)=\begin{cases}1+\log(1/|x|),&0<|x|\le1,\\ |x|^{-1/4},&|x|\ge1.\end{cases}
   \]
   The same source, using account03/B16, records for every cap-one scalar density `g`
   \[
   \int g(z)\Psi(a\pm\delta z^2)\,dz\le2\sqrt{15}\,\delta^{-1/4}.     \tag{0.3}
   \]

2. **account04/B18**, `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical report `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, is applied below to the explicit distributed-third-direction witness to quantify exactly how a one-triple square-smoothing payment loses `m^{1/4}`. This is a compatible account04 result actually used at an inequality. It is not mislabelled as the unavailable assigned `account04/B06` result.

The standard Rogozin--Ball one-dimensional projection theorem, already source-pinned in the completed rank-two fusion report, is also used: if `w` is a Euclidean unit vector and the coordinates of `X` are independent with densities at most one, then `w.X` has density at most `sqrt(2)`.

## 1. The unpaid implication attacked

A local physical `3 x 3` theorem can be useless when the third spectral direction is spread over many original coordinates: each individual determinant can be of order `1/m`, so paying a reciprocal fourth-root costs `m^{1/4}` even though the total third-direction curvature is order one.

This run proves that for **exact rank three**, once an invertible indefinite physical pair is selected, the *entire remaining coordinate bank* can be integrated before any third-coordinate determinant is inverted. The Schur complement is rank one, so all third-direction curvature is represented by one genuine product-linear projection of the remaining independent coordinates. The exact Cauchy--Binet sum then converts its coefficient into a two-row Pluecker mass without choosing a third coordinate.

This is a weighted replacement for the dimension-losing local fiber/minor step.

## 2. Scaling the curved ridge bank to a bounded projection density

We first record the precise scaling of (0.3) that will be needed.

### Lemma 2.1 — `QFORM-PSI-RIDGE-CAP-SCALING-v1`

Let `L` be a real random variable with density bounded by `K<infinity`. Then for every `a in R` and `delta>0`,

\[
\mathbb E\,\Psi(a\pm\delta L^2)
 \le 2\sqrt{15}\,K^{1/2}\delta^{-1/4}.                                \tag{2.1}
\]

#### Proof

Put `Z=K L`. Its density is at most one. Then

\[
\mathbb E\Psi(a\pm\delta L^2)
 =\mathbb E\Psi\left(a\pm(\delta/K^2)Z^2\right),
\]

and (0.3) gives

\[
2\sqrt{15}(\delta/K^2)^{-1/4}
=2\sqrt{15}K^{1/2}\delta^{-1/4}.
\]

`QED`

For a unit product-linear projection we may take `K=sqrt(2)`, hence the additional factor is only `2^(1/4)`.

## 3. Exact all-third-coordinates Schur identity

Let

\[
A=R\Lambda R^T,\qquad R^TR=I_3,                                     \tag{3.1}
\]

have exact rank three, with `Lambda` real symmetric and invertible. The target normalization later gives `|det Lambda|>=1`, but the algebra below does not need it.

Choose two **original physical coordinates** `i,j`, write `I={i,j}`, and assume the physical pair

\[
H=A_{I,I}                                                           \tag{3.2}
\]

is invertible. Let `K=I^c`, partition

\[
A=\begin{pmatrix}H&B\\B^T&D\end{pmatrix},
\]

and define its Schur complement

\[
S=D-B^TH^{-1}B.                                                      \tag{3.3}
\]

Because block Gaussian elimination is a congruence,

\[
\operatorname{rank}A=\operatorname{rank}H+\operatorname{rank}S.
\]

Hence exact rank three and `rank H=2` imply

\[
\operatorname{rank}S=1.                                             \tag{3.4}
\]

Write

\[
S=\sigma ww^T,\qquad \|w\|_2=1,\quad \sigma\ne0.                    \tag{3.5}
\]

For the two rows `r_i,r_j` of `R`, put

\[
\Delta_{ij}
 :=\det\begin{pmatrix}\langle r_i,r_i\rangle&\langle r_i,r_j\rangle\\
                       \langle r_j,r_i\rangle&\langle r_j,r_j\rangle
       \end{pmatrix}
 =\|r_i\wedge r_j\|^2.                                               \tag{3.6}
\]

### Lemma 3.1 — `QFORM-ALL-THIRD-SCHUR-MASS-IDENTITY-v1`

Under (3.1)--(3.6),

\[
\boxed{\det(H)\,\sigma=\det(\Lambda)\,\Delta_{ij}.}                 \tag{3.7}
\]

In particular,

\[
|\det H|\,|\sigma|=|\det\Lambda|\,\Delta_{ij}.                       \tag{3.8}
\]

#### Proof

For every `k in K`, the scalar Schur determinant identity gives

\[
\det A_{I\cup\{k\},I\cup\{k\}}=\det(H)\,S_{kk}.                    \tag{3.9}
\]

Since `A=R Lambda R^T` has exact rank three,

\[
\det A_{I\cup\{k\},I\cup\{k\}}
 =\det(\Lambda)\det(R_{I\cup\{k\}})^2.                              \tag{3.10}
\]

Sum (3.9)--(3.10) over all `k notin I`. The left Schur sum is

\[
\det(H)\operatorname{tr}S=\det(H)\sigma,                             \tag{3.11}
\]

because `S` has the sole nonzero eigenvalue `sigma`.

For the spectral side, in three dimensions

\[
\det(R_{I\cup\{k\}})=(r_i\times r_j)\cdot r_k.
\]

Since `sum_k r_k r_k^T=R^TR=I_3`, and the `k=i,j` terms vanish,

\[
\sum_{k\notin I}\det(R_{I\cup\{k\}})^2
 =(r_i\times r_j)^T\left(\sum_k r_k r_k^T\right)(r_i\times r_j)
 =\|r_i\times r_j\|^2
 =\Delta_{ij}.                                                       \tag{3.12}
\]

Equations (3.11)--(3.12) prove (3.7). `QED`

This is the exact aggregate identity that one-third-coordinate arguments discard.

## 4. Main theorem: integrate the entire rank-one Schur bank

Completing the pair square in original coordinates gives the exact identity

\[
Q=X^TAX
 =\bigl(X_I+H^{-1}BX_K\bigr)^T H\bigl(X_I+H^{-1}BX_K\bigr)
   +\sigma (w\cdot X_K)^2.                                          \tag{4.1}
\]

No spectral coordinate is declared independent. Conditional on `X_K=y`, the two components of `X_I+H^{-1}By` are merely deterministic translations of the two original independent cap-one coordinates. Thus the account03/B09 pair envelopes (0.1)--(0.2) apply uniformly in `y`.

Meanwhile

\[
L=w\cdot X_K                                                          \tag{4.2}
\]

is a genuine linear combination of a disjoint bank of original independent cap-one coordinates, with `||w||_2=1`. Hence

\[
\|p_L\|_\infty\le\sqrt2.                                            \tag{4.3}
\]

### Theorem 4.1 — `QFORM-RANK3-GLOBAL-RANK1-SCHUR-AGGREGATION-v1`

Assume (3.1), and suppose an original physical pair `I={i,j}` has an invertible **indefinite** principal block

\[
H=\begin{pmatrix}r&s\\s&t\end{pmatrix}.                              \tag{4.4}
\]

Let `Delta_ij` be (3.6).

**(a) Nonzero-diagonal pair.** If `r!=0`, then `Q` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
 \le 16\sqrt{15}\,2^{1/4}
      \bigl(|r|\,|\det\Lambda|\,\Delta_{ij}\bigr)^{-1/4}.
}                                                                    \tag{4.5}
\]

The symmetric estimate with `t` in place of `r` also holds whenever `t!=0`. Numerically the front constant is less than `73.693`.

**(b) Pure-bilinear pair.** If `r=t=0`, so `H=[[0,s],[s,0]]` with `s!=0`, then

\[
\boxed{
\|p_Q\|_\infty
 \le 2\sqrt{30}
      \bigl(|s|\,|\det\Lambda|\,\Delta_{ij}\bigr)^{-1/4}.
}                                                                    \tag{4.6}
\]

The front constant is less than `10.955`.

These bounds integrate **all remaining physical coordinates at once**. No individual third-coordinate determinant occurs.

#### Proof of (a)

Put `D_H=|det H|`. From (4.1), condition on `X_K`; account03/B09 gives, uniformly in the resulting translation,

\[
p_{Q\mid X_K}(u+\sigma L^2)
 \le 8D_H^{-1/2}\Psi(ru/D_H).
\]

Therefore for every output point `x`, after averaging in `X_K`,

\[
p_Q(x)
 \le 8D_H^{-1/2}
      \mathbb E\Psi\left(\frac r{D_H}(x-\sigma L^2)\right).           \tag{4.7}
\]

Apply Lemma 2.1 with `K=sqrt2` and

\[
\delta=\frac{|r\sigma|}{D_H}.
\]

Then

\[
\begin{aligned}
p_Q(x)
&\le 8D_H^{-1/2}\cdot2\sqrt{15}\,2^{1/4}
       \left(\frac{|r\sigma|}{D_H}\right)^{-1/4}\\
&=16\sqrt{15}\,2^{1/4}
   \bigl(|r|D_H|\sigma|\bigr)^{-1/4}.                                \tag{4.8}
\end{aligned}
\]

Now use the aggregate identity (3.8):

\[
D_H|\sigma|=|\det\Lambda|\Delta_{ij}.
\]

This yields (4.5). `QED`

#### Proof of (b)

Account03/B09's pure-bilinear envelope gives

\[
p_Q(x)
 \le |s|^{-1}\mathbb E\Psi\left(\frac{x-\sigma L^2}{2s}\right).
                                                                            \tag{4.9}
\]

Lemma 2.1 with `K=sqrt2` and `delta=|sigma|/(2|s|)` gives

\[
\begin{aligned}
p_Q(x)
&\le |s|^{-1}\,2\sqrt{15}\,2^{1/4}
       \left(\frac{|\sigma|}{2|s|}\right)^{-1/4}\\
&=2\sqrt{30}\,(|s|^3|\sigma|)^{-1/4}.                                \tag{4.10}
\end{aligned}
\]

Since `D_H=s^2`, (3.8) says

\[
|s|^2|\sigma|=|\det\Lambda|\Delta_{ij},
\]

so (4.10) becomes (4.6). `QED`

### Why this is a curved-fiber statement rather than a disguised fiber supremum

The hyperbolic singularity of the indefinite pair is retained as the actual profile `Psi`. The remaining coordinates are not replaced by

`int sup_(fiber) product-density`.

Instead their whole contribution enters through the **probability law** of the one-dimensional Schur coordinate `L=w.X_K`; product structure gives a universal density cap for that law, and the `Psi` ridge is integrated against it. Thus curvature and product measure are coupled before any supremum or reciprocal local minor is taken.

## 5. A distributed-third-direction witness: local triple payment diverges, global payment stays constant

For `m>=1`, take `n=m+2` and the exact rank-three frame

\[
r_1=e_1,\qquad r_2=e_2,\qquad
r_{2+k}=m^{-1/2}e_3\quad(1\le k\le m),                               \tag{5.1}
\]

with

\[
\Lambda=\operatorname{diag}(1,-1,1).                                \tag{5.2}
\]

Then `R^TR=I_3`, the three nonzero eigenvalues of `A=R Lambda R^T` are exactly `1,-1,1`, and for the physical pair `I={1,2}`,

\[
H=\operatorname{diag}(1,-1),\qquad \Delta_{12}=1.                    \tag{5.3}
\]

The Schur complement on the remaining bank is

\[
S=m^{-1}J_m,
\]

which has its sole nonzero eigenvalue `sigma=1`, exactly as Lemma 3.1 predicts.

But every individual physical triple `I union {k}` has

\[
|\det A_{I\cup\{k\}}|=1/m.                                         \tag{5.4}
\]

Hence any theorem that first chooses one third coordinate and then pays a reciprocal fourth-root loses `m^{1/4}`.

Here is an explicit use of the completed **account04/B18** square-smoothing result. For any one of these triples, pivoting the minority-sign diagonal `-1` leaves a definite Schur complement, so its theorem gives the valid local estimate

\[
\|p_Q\|_\infty\le 2\sqrt\pi\,m^{1/4}.                               \tag{5.5}
\]

The estimate is mathematically correct but diverges solely because one third coordinate was selected.

By contrast, Theorem 4.1(a) integrates the whole bank before paying curvature and gives

\[
\|p_Q\|_\infty
 \le16\sqrt{15}\,2^{1/4}<73.693                                    \tag{5.6}
\]

for every `m`. This is precisely the requested weighted replacement in a family where local fiber/minor selection loses dimension.

The determinant bookkeeping also makes the resource conservation transparent:

\[
\max_k|\det A_{I\cup\{k\}}|=1/m,
\qquad
\sum_k|\det A_{I\cup\{k\}}|=1.                                    \tag{5.7}
\]

No census of triples is used in the proof of (5.6); the sum is compressed exactly into the rank-one Schur eigenvalue.

## 6. Computation used only as a sanity check

The proof above is exact. A deterministic checker was nevertheless run on `50` random `8 x 3` orthonormal frames with

`Lambda=diag(1.25,-1.75,2.5)`.

Across `993` indefinite physical pairs it verified

\[
|\det H|\,|\sigma|=|\det\Lambda|\Delta_{ij}
\]

with maximum relative floating-point discrepancy `3.527e-14`; the maximum absolute size of either nominally zero Schur eigenvalue was `3.913e-13`.

For the witness (5.1) at `m=4,16,64,256`, the checker returned `det H=-1`, `sigma=1` to floating precision, largest local triple determinant `1/m`, and sum of absolute local triple determinants `1`.

These calculations are checks of the formulas, not evidence for any unproved universal extraction statement.

## 7. Exact status and next unpaid implication

### What this run proves

`QFORM-RANK3-GLOBAL-RANK1-SCHUR-AGGREGATION-v1` is a source-complete supporting theorem for exact-rank-three forms. Once one original physical pair is invertible and indefinite, the third spectral curvature may be aggregated across **all** remaining independent coordinates before any local third-index determinant is inverted. The theorem handles both nonzero-diagonal hyperbolic pairs and the pure-bilinear pair.

This removes one genuine source of dimension loss from the rank-three curved-fiber route.

### What remains open

It does **not** prove that every exact-rank-three target frame has one indefinite physical pair for which the resource in (4.5) or (4.6) is uniformly bounded below. The current Pluecker-support correction explicitly warns that naive weighting of local pair certificates can fail. A surviving frame may require grouping or a diffuse-bank theorem before an indefinite pair is paid.

It also does not handle a general higher-rank `A`: after eliminating a physical pair, the Schur complement need not have rank one, and its additional correlated quadratic components cannot simply be discarded or treated as an independent convolution.

The next precise implication is therefore:

**`QFORM-INDEFINITE-PAIR-RESOURCE-OR-GROUPED-DIFFUSE-v1` — OPEN.** For an exact-rank-three target matrix, use the original-coordinate frame identities to prove either

1. an indefinite physical pair `I={i,j}` for which one of
   `|A_ii| |det Lambda| Delta_ij`, `|A_jj| |det Lambda| Delta_ij`, or in the pure-bilinear case `|A_ij| |det Lambda| Delta_ij`
   has a universal positive lower bound; or
2. a product-preserving grouped/diffuse alternative that yields the target density bound **before** reciprocal pair resource is paid.

The distributed-third-direction obstruction has now been removed from that question. After exact rank three, an additional separate bridge must retain arbitrary extra spectral components in higher rank.

**Full QFORM status:** `OPEN / NOT PROVED / NOT DISPROVED`.  
**Continuity:** not proved by Theorem 4.1; only an essentially bounded density is established in its scope.
