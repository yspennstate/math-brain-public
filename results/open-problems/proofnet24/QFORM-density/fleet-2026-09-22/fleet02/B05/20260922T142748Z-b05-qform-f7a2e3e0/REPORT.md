# fleet02/B05 — fractional cross-Riesz coarea and Schur-cancellation boundary

**Programme:** QFORM-DENSITY-3EIG-20260922, owner revision 2026-09-22.5  
**Run:** `20260922T142748Z-b05-qform-f7a2e3e0`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET-LEVEL BRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. First unpaid implication attacked

The preceding B05 state had removed the generic two-variable Schur-fiber obstruction for a *fixed* nonsingular physical triple, but a single local triple can lose dimension in diffuse rank-three examples. The live global residual is to aggregate original-coordinate banks before paying reciprocal minors. This run attacks that residual at the exact coarea interface:

> after completing one original-coordinate square, can the remaining half-Riesz potential
> `sup_t E |t-R|^(-1/2)` be bounded from an aggregate physical cross block without assuming that `R` has exact rank two?

The answer is yes for two cross directions whenever their physical range leverage is strictly below one, and unconditionally for three cross directions. This is stable under arbitrary self blocks, outside couplings, signs, and arbitrary additional spectrum because the proof applies the reviewed regularized-determinant characteristic-function inequality to the *full residual*.

The remaining obstruction is correspondingly narrower: two useful cross directions can be destroyed by the rank-one Schur correction, and when they survive but have physical range leverage exactly one the fractional determinant exponent reaches the nonintegrable endpoint. The assigned partner fleet03/B05 already closes the exact-rank-two version of that endpoint, so the unpaid case is specifically **extra spectrum + coordinate-full two-direction cross range, or failure to extract a post-Schur cross certificate**.

## 2. Sources actually used

1. **Regularized determinant theorem.**  
   `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`  
   `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.  
   For any symmetric residual matrix `S`, disjoint original-coordinate sets `I,J`, and `B=S[I,J]`, for `1<=q<2` with
   `rho := max diag(P_range(B)) <= q/2`,
   \[
   |\phi_R(s)| \le
   \det\!\left(I+\frac{2q s^2}{\pi^2e^2}BB^T\right)^{-1/(4q)}.
   \]
   At `q=2` the leverage condition disappears and the exponent is `-1/8`. The source allows arbitrary self blocks, outside couplings and arbitrary additional small singular values. The determinant proof has a scoped independent PASS in fleet03/B04, canonical mathematics commit `55e0a30b6ac56934614a5416056cae2e4a6dc77e`.

2. **Assigned partner fleet03/B05.**  
   `yspennstate/math-open-problems@bf7bff5c9b11cf495ccbcb09ef48549fd9c0d409`  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/fleet03-B05-20260922T133738Z-qform-r12/REPORT.md`.  
   For every exact rank-two product quadratic form with nonzero eigenvalues `mu_1,mu_2`,
   \[
   \sup_t E|t-R|^{-1/2}
   \le 16\,2^{3/4} |\mu_1\mu_2|^{-1/4}.
   \]
   This is applied below to remove the localized exact-rank-two endpoint from the new residual debt.

3. **Canonical hard family.**  
   fleet02/B03 event `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`,
   canonical report commit `24fc7b37c60f77b399936faa7f280296a7ce8c8c`, gives
   `A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)` with spectrum `{1,1,-1}` and no uniformly conditioned fixed principal triple. The new theorem is checked on this family as an aggregation control.

No pointwise law-uniform scalar oscillatory decay, no post-rotation independence, no unrestricted curved-fiber supremum, and no conditional density-cap substitution is used.

## 3. A rigorous Fourier-to-half-Riesz lemma

Use the convention `phi_R(s)=E exp(isR)`. If
\[
\int_{\mathbb R} |s|^{-1/2}|\phi_R(s)|\,ds <\infty ,
\]
then
\[
\sup_t E|t-R|^{-1/2}
\le \frac1{\sqrt{2\pi}}
     \int_{\mathbb R} |s|^{-1/2}|\phi_R(s)|\,ds.       \tag{3.1}
\]

A direct regularization avoids assuming in advance that `R` has a density. For `delta>0` put
\[
k_\delta(x)=\frac1{\sqrt{2\pi}}
 \int_{\mathbb R}e^{-\delta|s|}|s|^{-1/2}e^{-isx}\,ds
 =\sqrt2\,\Re(\delta-ix)^{-1/2}\ge0 .
\]
For `x!=0`, `k_delta(x) -> |x|^(-1/2)`. Hence Fatou and Fubini give
\[
E|t-R|^{-1/2}
\le \liminf_{\delta\downarrow0}E k_\delta(t-R)
\le \frac1{\sqrt{2\pi}}
     \int |s|^{-1/2}|\phi_R(s)|ds .
\]
A finite right side also rules out an atom at `t`.

## 4. New theorem: two-cross fractional Riesz smoothing

### Theorem 4.1 — `QFORM-CROSS2-FRACTIONAL-RIESZ-v1`

Let `R=Y^T S Y` for arbitrary independent original coordinates with densities at most one. Let `I,J` be disjoint original-coordinate sets and `B=S[I,J]`. Suppose `B` has two positive singular values `sigma_1,sigma_2`, and let
\[
\rho=\max_i (P_{\rm range(B)})_{ii}<1.
\]
For every
\[
\max(1,2\rho)\le q<2
\]
one has
\[
\boxed{
\sup_t E|t-R|^{-1/2}
\le C_q (\sigma_1\sigma_2)^{-1/4}
}
\tag{4.1}
\]
with
\[
C_q=
\frac{\sqrt e}{2^{3/4}q^{1/4}}
B\!\left(\frac14,\frac1{2q}-\frac14\right).           \tag{4.2}
\]
In particular, if `rho<=1/2`, take `q=1`:
\[
C_1=
\frac{\sqrt e}{2^{3/4}}
B(1/4,1/4)
=7.270461147134126\ldots .                                  \tag{4.3}
\]

#### Proof

Let `c_q=2q/(pi^2 e^2)`. The reviewed determinant theorem and discarding all but the two selected singular factors give
\[
|\phi_R(s)|
\le[(1+c_qs^2\sigma_1^2)(1+c_qs^2\sigma_2^2)]^{-1/(4q)}.
\]
Since `(1+a)(1+b)>=(1+sqrt(ab))^2`,
\[
|\phi_R(s)|
\le(1+c_qs^2\sigma_1\sigma_2)^{-1/(2q)}.                \tag{4.4}
\]
Because `q<2`, the right side times `|s|^(-1/2)` is integrable. Applying (3.1), scaling
`u=s sqrt(c_q sigma_1 sigma_2)`, and then `v=u^2`,
\[
\int_{\mathbb R} |u|^{-1/2}(1+u^2)^{-1/(2q)}du
=B\!\left(\frac14,\frac1{2q}-\frac14\right).
\]
Substituting `c_q` gives exactly (4.1)--(4.2). No property of the other singular values or self blocks is used. QED.

**Exact missing factor.** The constant blows up as `q↑2`, i.e. as the available range leverage approaches the full-coordinate endpoint `rho=1`. This is an analytic endpoint of this determinant-to-Riesz conversion, not a claim that the half-Riesz potential itself must diverge there. The partner theorem proves it stays finite for every **exact rank-two** residual even at localized leverage one.

## 5. New theorem: unconditional three-cross half-Riesz smoothing

### Theorem 5.1 — `QFORM-CROSS3-HALF-RIESZ-v1`

Under the same product-law hypotheses, if some physical cross block `B=S[I,J]` has three positive singular values `sigma_1,sigma_2,sigma_3`, then, with no leverage assumption,
\[
\boxed{
\sup_t E|t-R|^{-1/2}
\le C_3 (\sigma_1\sigma_2\sigma_3)^{-1/6}
}
\tag{5.1}
\]
where
\[
C_3=\frac{\sqrt e}2 B(1/4,1/8)
=9.499315272418065\ldots .                                  \tag{5.2}
\]

#### Proof

Use the unconditional determinant estimate
\[
|\phi_R(s)|\le\prod_{j=1}^3
(1+c s^2\sigma_j^2)^{-1/8},\qquad c=4/(\pi^2e^2).
\]
Let `g=(sigma_1 sigma_2 sigma_3)^(1/3)`. The AM--GM inequalities for the first two elementary symmetric polynomials imply
\[
\prod_{j=1}^3(1+c s^2\sigma_j^2)
\ge(1+c s^2g^2)^3.
\]
Thus `|phi_R(s)| <= (1+c s^2 g^2)^(-3/8)`. Equation (3.1) and the same beta substitution yield (5.1)--(5.2). QED.

## 6. Coarea closure after one physical scalar pivot

Let `i` be an original coordinate with `a=A_ii !=0`, write `Y=X_{-i}`, and let `b=A_{-i,i}`. Completing the square only in the original coordinate gives
\[
Q=a(X_i+a^{-1}b^TY)^2+R(Y),\qquad
R(Y)=Y^T\left(A_{-i,-i}-a^{-1}bb^T\right)Y.             \tag{6.1}
\]
The conditional square density obeys, uniformly in its random shift,
\[
p_Q(t)\le |a|^{-1/2}E|t-R|^{-1/2}.                      \tag{6.2}
\]
Therefore:

* if a post-Schur physical cross block of `R` has two singular values `sigma_1,sigma_2` and leverage `rho<1`, then
  \[
  \|p_Q\|_\infty\le
  |a|^{-1/2} C_q(\sigma_1\sigma_2)^{-1/4};
  \]
* if it has three positive singular values, then without leverage assumptions
  \[
  \|p_Q\|_\infty\le
  9.499316\,|a|^{-1/2}
  (\sigma_1\sigma_2\sigma_3)^{-1/6}.                    \tag{6.3}
  \]

These are genuine density/small-interval conclusions: for every interval of length `h`,
`P(Q in interval) <= h ||p_Q||_infinity`. The curved square kernel is kept inside the residual expectation; there is no unrestricted fiber supremum.

## 7. Rank-one Schur robustness and a sharp structural falsifier

If `C=A[I,J]` is a cross block disjoint from the pivot coordinate, the post-Schur block is
\[
C'=C-a^{-1}A[I,i]A[i,J],
\]
a rank-one perturbation. Singular-value rank-one interlacing gives
\[
\sigma_j(C')\ge\sigma_{j+1}(C).                          \tag{7.1}
\]
Hence a pre-pivot four-direction certificate implies the target-level branch
\[
\boxed{
\|p_Q\|_\infty
\le 9.499316\,|a|^{-1/2}
(\sigma_2(C)\sigma_3(C)\sigma_4(C))^{-1/6}
}.                                                          \tag{7.2}
\]
This is one cross direction cheaper than the direct unconditional `L^1` determinant route, which needs five cross directions.

The tempting stronger implication “two pre-pivot cross directions remain two after Schur completion” is **false even inside the target spectral class**. Take
\[
A=
\begin{pmatrix}
1&1&0&1&0\\
1&0&0&1&0\\
0&0&0&0&1\\
1&1&0&0&0\\
0&0&1&0&0
\end{pmatrix}.
\]
Its eigenvalues are
\[
-1,-1,1-\sqrt2,1,1+\sqrt2,
\]
so at least three have modulus at least one. Pivot at coordinate `0`, and take
`I={1,2}`, `J={3,4}`. Then
\[
C=I_2,
\qquad
A[I,0]=(1,0)^T,
\qquad
A[0,J]=(1,0),
\]
but
\[
C'=I_2-(1,0)^T(1,0)=\operatorname{diag}(0,1).
\]
Thus an arbitrary proof cannot pay for the first pivot and then silently retain both original cross directions. One rank can genuinely disappear.

## 8. Application to the canonical low-local-minor bank family

For
\[
A_m=[1]\oplus J_m/m\oplus(-J_m/m),
\]
the B03 source gives the exact target spectrum `{1,1,-1}` while every fixed nonsingular physical triple becomes badly conditioned as `m` grows. Pivot the first coordinate (`a=1`); the residual is the two-bank form.

For `m>=3`, split each bank with `p=ceil(m/2)` coordinates on the `I` side and `q=floor(m/2)` on the `J` side. The cross block has exactly two nonzero singular values
\[
\sigma_1=\sigma_2=\frac{\sqrt{pq}}m,
\]
and its range projection has diagonal leverage
\[
\rho=1/p\le1/2.
\]
Theorem 4.1 with `q=1` gives
\[
\|p_Q\|_\infty
\le C_1\left(\frac{\sqrt{pq}}m\right)^{-1/2}
\le 10.589248 .                                             \tag{8.1}
\]
For `m=1,2`, the assigned partner's universal exact-rank-two half-Riesz theorem and the same scalar-square coarea give the uniform (weaker) bound `<26.909`.

Thus the canonical family that refutes “one well-conditioned physical triple or rank-three cross cut” is handled by **bank aggregation before reciprocal-minor payment**. More importantly, Theorem 4.1 is robust to arbitrary additional self blocks and outside couplings: the same two-cross certificate controls the half-Riesz potential without requiring the residual to remain exact rank two.

## 9. Status and first unpaid implication

**Proved this run**

* `QFORM-CROSS2-FRACTIONAL-RIESZ-v1`, arbitrary additional spectrum and arbitrary self/outside couplings;
* `QFORM-CROSS3-HALF-RIESZ-v1`, no leverage assumption;
* the scalar-pivot coarea closures (6.2)--(6.3);
* the rank-one-resistant four-cross pre-pivot branch (7.2);
* a uniform coarea closure of the canonical `A_m` low-local-minor family by balanced bank aggregation;
* a target-valid 5-by-5 falsifier showing that two pre-pivot cross directions can collapse to one after the Schur rank-one correction.

**Partner result actually applied**

fleet03/B05 removes the exact-rank-two localized endpoint: its universal half-Riesz theorem remains valid when the new determinant conversion reaches `rho=1`, provided no extra spectral directions are present.

**First unpaid implication: `QFORM-POSTSCHUR-CROSS2-EXTRA-SPECTRUM-BRIDGE-v1`.**

Starting from the live low-stable-rank/heavy-coordinate residual, prove an exhaustive dimension-free reduction which, *before paying a reciprocal first pivot*, yields at least one of:

1. a nonzero original scalar pivot whose Schur residual has a two-cross block with `rho<1` and controlled `sigma_1 sigma_2`;
2. a post-Schur three-cross block with controlled geometric mean;
3. an exact-rank-two residual, invoking the partner theorem; or
4. a direct aggregate bank/hyperbolic-square certificate.

The 5-by-5 example above forbids replacing this with the false statement that a pre-pivot rank-two cross block automatically survives. The remaining missing factor is therefore a genuine **post-Schur aggregate extraction**, not the curved-fiber integral itself.

Full QFORM remains OPEN. No continuity claim is made beyond branches where the cited Fourier source itself supplies it.
