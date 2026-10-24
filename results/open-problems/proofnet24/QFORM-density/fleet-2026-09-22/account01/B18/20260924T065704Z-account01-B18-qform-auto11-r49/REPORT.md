# account01/B18 r49 — source-valid cross/HS-private fusion and curved diffuse tails

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T065704Z-account01-B18-qform-auto11-r49`  
**Role:** literature-to-proof transfer  
**Status:** **PROVED SUPPORTING TARGET-LEVEL IMPLICATION / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
**Continuity:** proved in the private-square/HS branch and the concrete families below; unrestricted QFORM continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-24T06:57:04Z.  
attacking: fuse the exact rank-two original-cross receiver with the new Hilbert--Schmidt private-square receiver, then spend it on target-valid curved diffuse-tail families whose individual cross singular values vanish.

## 1. Correction discipline and exact scope

The full owner target remains OPEN: independent original coordinates with probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. This run does not use arbitrary-joint coarea, conditional projected-density moments, post-rotation independence, law-uniform pointwise oscillatory decay, deletion of a small nonzero remainder, or a claim that `s_3(A)>=1` forces the structural packet below.

Fresh prepublication controls were read at `yspennstate/math-research-brain@fb71ccb02937b879a9a55b5cbeb641a63c731836`, OWNER CONTROL revision `2026-09-22.15`; the live correction inbox blob remained `a884b835aba929c5376e6417ae5cfcd44c0f7a76`.

## 2. Primary literature and hypothesis transfer

### 2.1 Rudelson--Vershynin

Rudelson--Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, arXiv:1402.4492 / IMRN 2015, Theorem 1.2, states that if independent real random variables have densities bounded by `K` and the coefficient vector has Euclidean norm one, then the density of the corresponding linear combination is bounded by `sqrt(2) K`. No moment, iid, support, centering, symmetry, smoothness, or log-concavity hypothesis is imposed.

Thus, for any original-coordinate product bank `X` with scalar caps one and any nonzero vector `b`,

\[
\|p_{b^T X}\|_\infty\le {\sqrt2\over\|b\|_2}. \tag{2.1}
\]

This is the source-valid one-dimensional ingredient in the HS moving-square theorem used below.

### 2.2 Livshyts--Paouris--Pivovarov

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1, proves that if the original density is a product `prod_i f_i` with `||f_i||_infty<=1`, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. This is a marginal-density theorem only; it does **not** make different projections independent.

The exact prior account03/B18 theorem `QFORM-ONE-SIDED-CROSS-NEGATIVE-MOMENT-v1`, scientific commit `a2cf029c5c935d6eadf4216c073911fc8dc404ac`, uses this theorem plus a radial bathtub negative-moment estimate. I re-use its proved ambient corollary and make no novelty claim for it.

### 2.3 Banks--Garza Vargas--Kulkarni--Srivastava

Banks--Garza Vargas--Kulkarni--Srivastava, arXiv:2005.08930, Theorem 2.1 (`Density of Quadratic Forms`), assumes two independent matrices `X,Y` with independent density-capped entries and treats

\[
q(X,Y)=X^T ZY+X^TU+V^TY+W. \tag{2.2}
\]

Its scalar `k=1` Corollary 2.4 gives an improved rank-at-least-two bilinear-affine estimate. This is a genuinely relevant primary source, but (2.2) contains no arbitrary same-`Y` quadratic curvature `Y^TCY`. Therefore it does not by itself close the curved-tail packet below. The extra same-bank curvature is exactly where the source-preserving HS/private-square receiver is useful.

### 2.4 Herry--Malicet--Poly scope comparison

Herry--Malicet--Poly, arXiv:2303.09488, studies quadratic-form regularity for iid inputs whose common law can be represented as a sufficiently smooth function of a Gaussian field. That is materially narrower than the owner's arbitrary non-iid cap-one class and is not used as a full-target theorem.

## 3. Exact prior cross receiver (no novelty claim)

Let original coordinates be partitioned into disjoint banks `I,J,K`. If

\[
A_{II}=0,
\]

and the physical cross block `B=A_{IJ}` has top singular values `beta_1>=beta_2>0`, account03/B18 proved

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le {2\sqrt\pi\over\sqrt{\beta_1\beta_2}}.
} \tag{3.1}
\]

Arbitrary `J--J` curvature, arbitrary coefficients on `K`, and arbitrary couplings to `K` are allowed: one conditions only on ORIGINAL coordinates in `K`. The theorem establishes essential boundedness; it does not by itself assert continuity.

## 4. New matrix-level fusion corollary

### `QFORM-ZEROSELF-PRIVATE-SQUARE-HS-CROSS-FUSION-v1`

Suppose an ORIGINAL-coordinate principal packet is indexed by disjoint sets

\[
R=I\sqcup J\sqcup\{w\},
\]

and has the block form

\[
A_{RR}=
\begin{pmatrix}
0 & B & 0\\
B^T & C & h\\
0 & h^T & a
\end{pmatrix},
\qquad a\ne0,\quad B\ne0. \tag{4.1}
\]

All coefficients and couplings involving coordinates outside `R` are arbitrary. Put

\[
H_B:=\|B\|_{HS}.
\]

Then the full ambient quadratic form has a continuous `C_0(R)` density and

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le {4\sqrt2\over\sqrt{|a|H_B}}.
} \tag{4.2}
\]

If `rank(B)>=2`, with top singular values `beta_1>=beta_2>0`, the same continuous representative satisfies the fused estimate

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le
\min\left\{
{2\sqrt\pi\over\sqrt{\beta_1\beta_2}},
{4\sqrt2\over\sqrt{|a|H_B}}
\right\}.} \tag{4.3}
\]

### Proof

Condition only on every ORIGINAL coordinate outside `R`. The retained original banks remain independent and cap one. For a fixed outside value the quadratic form has the shape

\[
\begin{aligned}
Q=&\ 2X_I^T B X_J+X_J^T C X_J+2W h^T X_J+aW^2\\
 &+\alpha^T X_I+\eta^T X_J+2dW+c.
\end{aligned} \tag{4.4}
\]

Complete the literal original-coordinate square:

\[
aW^2+2W(h^T X_J+d)
=a\left(W+{h^TX_J+d\over a}\right)^2
-{(h^TX_J+d)^2\over a}. \tag{4.5}
\]

Everything in the last term of (4.5), together with `X_J^T C X_J+eta^T X_J+c`, is an arbitrary measurable function `G(X_J)`. Thus (4.4) is exactly the packet in account01/B18 r48,

\[
X_I^T M X_J+\alpha^T X_I+G(X_J)
+a(W+H(X_J))^2,
\qquad M=2B, \tag{4.6}
\]

with `W` a literal independent original coordinate. The r48 theorem gives

\[
\|p_{Q\mid X_{R^c}}\|_\infty
\le {8\over\sqrt{|a|\,\|2B\|_{HS}}}
={4\sqrt2\over\sqrt{|a|H_B}}, \tag{4.7}
\]

uniformly in the conditioning, and supplies a `C_0` conditional density with an integrable uniform majorant. Averaging proves (4.2) and preserves `C_0` by dominated convergence.

Equation (3.1), applied to the `I` versus `J union {w}` split (whose cross block is `[B\ 0]`), gives the first branch in (4.3). Since (4.2) already supplies a continuous representative, an a.e. sharper bound from (3.1) holds pointwise for that representative as well. QED.

No rotation of the random source is used. The only completion of a square is in one literal original coordinate `W`.

## 5. A target-level structural exit

A simple deterministic sufficient condition turns (4.2) into an owner-target exit. Take `h=0`. If

\[
|a|\ge1,
\qquad H_B\ge1,
\tag{5.1}
\]

and `C` has at least two eigenvalues whose absolute values are at least

\[
1+\|B\|_{op}, \tag{5.2}
\]

then the principal packet (4.1) itself has at least three eigenvalues of modulus at least one.

Indeed, on `I union J`, write

\[
\begin{pmatrix}0&B\\B^T&C\end{pmatrix}
=
\begin{pmatrix}0&0\\0&C\end{pmatrix}
+
\begin{pmatrix}0&B\\B^T&0\end{pmatrix}. \tag{5.3}
\]

The second summand has operator norm `||B||_op`. Weyl's inequality therefore preserves two eigenvalues of modulus at least one from the two eigenvalues in (5.2). The independent scalar block contributes the eigenvalue `a`. Hence the full ambient matrix is target-valid as well by principal-submatrix interlacing. From (4.2),

\[
\boxed{\|p_Q\|_\infty\le4\sqrt2<5.657.} \tag{5.4}
\]

This is only a sufficient structural chamber; the bare hypothesis `s_3(A)>=1` is not claimed to force (4.1), (5.1), or (5.2).

## 6. Exact diffuse family: every individual crossing tends to zero

For `N>=2`, let

\[
B_N=N^{-1/2}I_N,
\qquad
C_N=R_N\,\operatorname{diag}(2,-2,0,\ldots,0)\,R_N^T,
\qquad a=1,\ h=0, \tag{6.1}
\]

where `R_N` is an arbitrary deterministic orthogonal matrix. Let

\[
A_N=
\begin{pmatrix}
0&B_N&0\\
B_N&C_N&0\\
0&0&1
\end{pmatrix}. \tag{6.2}
\]

Deterministically one may conjugate (6.2) by `diag(R_N,R_N,1)` to compute its spectrum; this is **not** a probabilistic rotation. The spectrum consists of

\[
1\pm\sqrt{1+1/N},
\qquad
-1\pm\sqrt{1+1/N},
\qquad
\pm N^{-1/2}\ \text{(each repeated `N-2` times)},
\qquad 1. \tag{6.3}
\]

Thus exactly three eigenvalues have modulus at least one for every `N>=2`.

Meanwhile

\[
\|B_N\|_{HS}=1,
\qquad
\|B_N\|_{op}=N^{-1/2}. \tag{6.4}
\]

The new fusion gives

\[
\boxed{
\|p_{X^TA_NX}\|_\infty
\le
\min\{2\sqrt\pi\sqrt N,\ 4\sqrt2\}
\le4\sqrt2,
} \tag{6.5}
\]

with a continuous `C_0` density for every admissible cap-one product law. Every individual cross singular value tends to zero, so the uniform certificate is genuinely paid by aggregate Hilbert--Schmidt energy before reciprocal inversion.

## 7. Required application of the latest account02/B18 theorem

The latest completed designated partner result is account02/B18 run `account02-B18-20260924T060756Z-db964583`, theorem `QFORM-HS-MOVING-DIFFUSE-SQUARE-v1`, scientific report commit `fd7c768025320fbb5e54e13a1acd00d329e8f8dd`.

Use a **literal original coordinate** `W`, so its density cap is `K_beta<=1` rather than the generic projected-bank cap `sqrt(2)`. On the partner's target-valid family

\[
Q^{(0)}_{N,\varepsilon}
=4\sqrt3X_0Y_0
 +2\varepsilon\sum_{j=1}^N X_jY_j
 +3\left(W+\sqrt{2/3}\,Y_0\right)^2,
\qquad 0<\varepsilon<1, \tag{7.1}
\]

the core spectrum is exactly `{-3,2,6}` and the tail contributes `+epsilon,-epsilon`. Put

\[
D=12+N\varepsilon^2,
\qquad
M=\operatorname{diag}(4\sqrt3,2\varepsilon,\ldots,2\varepsilon). \tag{7.2}
\]

Then

\[
\|M\|_{HS}=2\sqrt D,
\qquad
\|M\|_{op}=4\sqrt3. \tag{7.3}
\]

The partner theorem therefore gives the actual whole-line inequality

\[
\boxed{
\|p_{Q^{(0)}_{N,\varepsilon}}\|_\infty
\le
\min\left\{
{K_{HP}\over\sqrt6\,D^{1/4}},
{8\over\sqrt{12\sqrt3}}
\right\},} \tag{7.4}
\]

where `K_HP` is the source constant in the partner's Hu--Paouris/Juskevicius--Lee branch. The explicit operator branch is

\[
\boxed{{8\over\sqrt{12\sqrt3}}=1.754765350603323\ldots .} \tag{7.5}
\]

This is a direct equation-level use of the completed account02/B18 theorem. The improvement from the partner report's `2.4816129576...` generic projection figure is simply that here the private source is one literal cap-one original coordinate, not a projected bank.

## 8. New curved-tail extension of the partner family

Now allow **arbitrary high-dimensional same-bank quadratic curvature** on the tail:

\[
Q^{(C)}_{N,\varepsilon}
=Q^{(0)}_{N,\varepsilon}
+Y_{1:N}^T C_N Y_{1:N}, \tag{8.1}
\]

where `C_N` is any real symmetric `N x N` matrix, with no operator-norm, rank, sign, or orientation restriction.

This remains owner-target-valid for every `C_N`: the three-dimensional `(X_0,Y_0,W)` core is a direct principal block with spectrum `{-3,2,6}`. The completed partner theorem (7.4) itself does not permit the arbitrary additive same-`Y` remainder in its Hilbert--Schmidt branch. The r48 arbitrary-`G(Y)` theorem, equivalently the matrix corollary (4.2), does. Since `W` is literal,

\[
\boxed{
\|p_{Q^{(C)}_{N,\varepsilon}}\|_\infty
\le
{8\over\sqrt6\,(12+N\varepsilon^2)^{1/4}},
} \tag{8.2}
\]

and the density is `C_0(R)`.

For the diffuse choice `epsilon=N^{-1/2}`,

\[
\boxed{
\|p_{Q^{(C)}_{N,N^{-1/2}}}\|_\infty
\le {8\over\sqrt6\,13^{1/4}}
=1.7200003042251348\ldots,
} \tag{8.3}
\]

uniformly in `N`, in the arbitrary symmetric tail curvature `C_N`, and in every admissible rough product law, even though every added tail-cross singular value is `2/sqrt(N)` and tends to zero.

This is a concrete target-level implication of the literature-to-proof transfer: the aggregate cross energy survives completely arbitrary same-bank tail curvature, with original-coordinate product provenance intact.

## 9. What remains unpaid

The unrestricted conjecture is still OPEN. The new fusion requires a literal source-preserving packet with a zero-self bank and a private scalar direction uncoupled from that zero-self bank. The bare condition `s_3(A)>=1` does not force such a packet; live corrections already refute several stronger naive extraction statements. The remaining structural compiler must either

- produce a packet with `|a| ||B||_HS >= c` or `sigma_1(B)sigma_2(B)>=c`, or
- route every failure into an already-paid physical-pair, ridge, grouped-hub, exterior-volume, or other product-preserving branch,

without deleting small nonzero curvature/cross tails and without using post-rotation independence.

Continuity is proved only in the packet/families where the private-square theorem applies; the full-target continuous-representative claim remains open.

## 10. Source pins

- account01/B18 r48 `QFORM-CROSS-MOVING-DIFFUSE-SQUARE-HS-REMAINDER-v1`: `yspennstate/math-open-problems@950cbfd149a2acf0de3c232cf52434c5d7e5e4df`.
- exact prior account03/B18 cross theorem: `yspennstate/math-open-problems@a2cf029c5c935d6eadf4216c073911fc8dc404ac`.
- latest designated partner account02/B18 report: `yspennstate/math-open-problems@fd7c768025320fbb5e54e13a1acd00d329e8f8dd`.
- M. Rudelson and R. Vershynin, arXiv:1402.4492, Theorem 1.2.
- G. Livshyts, G. Paouris and P. Pivovarov, arXiv:1507.07949, Theorem 1.1.
- J. Banks, J. Garza Vargas, A. Kulkarni and N. Srivastava, arXiv:2005.08930, Theorem 2.1 and Corollary 2.4.
- R. Herry, D. Malicet and G. Poly, arXiv:2303.09488, scope comparison only.

A targeted fleet/source search found no exact prior artifact with the full fusion statement (4.3) plus the arbitrary-curved diffuse-tail application (8.2). This search miss is **not** treated as publication-novelty evidence.
