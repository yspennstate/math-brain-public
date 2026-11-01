# fleet02/B03 — sharp cubic Fourier replacement and the exact limit of one-copy symmetrization

**Run:** `20260922T114427Z-b03-qform-a11`  
**Assignment:** `Decoupled time integral`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Classification:** `ESSENTIAL_STEP_APPLIED / METHOD_CORRECTION / TARGET_SUPPORTING_LEMMA / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

The earlier FEI instruction for this slot was superseded by the fresh owner control before any new FEI mathematics was done. This report addresses only the live quadratic-form target.

## 1. Sources actually consumed

The live target is the arbitrary-dimensional, arbitrary-sign rotated quadratic-form conjecture with independent input densities bounded by one and at least three eigenvalues of magnitude at least one.

The main external fleet dependency used here is:

* `yspennstate/math-open-problems@c64fcff680b0a252a3c92002c60eedba02bbb9ec:qform/fleet-2026-09-22/fleet03/B17/fleet03-B17-20260922T112131Z/REPORT.md`.

That fleet03/B17 report proves two facts used below: (i) no law-uniform pointwise Fresnel decay is possible at a prescribed nonzero frequency, and (ii) for one square term the pushforward density has the exact envelope `g(y)<=|a y|^{-1/2}` on the appropriate half-line. I do not reuse its pointwise-decay conjecture; it was refuted there.

I also use the immutable fleet02/B15 obstruction

* `yspennstate/math-open-problems@d5392d73398e2811f58b612fb8f191aa79d8ee5e:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`,

which exhibits flat rank-three projectors for which every fixed principal coordinate triple has curvature only `O(1/n)`. This is used only to delimit the remaining bridge.

The named partner for this card is fleet03/B03. At the pre-proof source check, the canonical partner deliverable path had no completed commit on `math-open-problems/master`; I therefore did not wait or invent a partner result.

## 2. Exact independent-copy identity, with the dependence retained

Let `X` have density `f<=1`, let `X'` be an independent copy, fix `b in R`, and put

`psi_a,b(t)=E exp(i t a (X-b)^2)`.

Set

`U=X-X'`,  `V=X+X'-2b`.

Then

`a[(X-b)^2-(X'-b)^2]=a U V`,

and the exact joint density of `(U,V)` is

`h_b(u,v)=(1/2) f(b+(v+u)/2) f(b+(v-u)/2)`.

Thus

`|psi_a,b(t)|^2 = E exp(i t a U V)`

under this **joint** law. In general `U` and `V` are not independent. For example, when `X` is uniform on a unit interval centered at `b`, `(U,V)` is supported on a diamond. Any decoupling argument that replaces `h_b` by the product of its marginals changes the problem.

The positive estimate below therefore never makes that replacement.

## 3. Sharp `L^p` bound for one squared coordinate

### Theorem 3.1 — `QFORM-SQUARE-PUSHFORWARD-LP-SHARP-v1`

Let `X` have a probability density `0<=f<=1`. Let `a!=0`, `b in R`, and let

`Y=a(X-b)^2`.

For every `1<=p<2`, the density `g` of `Y` satisfies

\[
\boxed{
 \|g\|_p^p
 \le {2^{p-1}\over 2-p}|a|^{1-p},
\qquad
 \|g\|_p
 \le \left({2^{p-1}\over2-p}\right)^{1/p}|a|^{1/p-1}.
}
\tag{3.1}
\]

The constant in (3.1) is sharp for the pushforward problem: equality holds for the centered unit-interval density `f=1_[b-1/2,b+1/2]`.

### Proof

Reflection reduces to `a>0`. The two-branch change of variables gives, for `y>0`,

\[
g(y)= {f(b+\sqrt{y/a})+f(b-\sqrt{y/a})\over 2\sqrt{a y}},
\]

hence

\[
0\le g(y)\le w(y):={1\over\sqrt{a y}},
\qquad \int_0^\infty g(y)dy=1.
\tag{3.2}
\]

Put `R=a/4`. Then `int_0^R w=1`. Fix `1<p<2`, and set `lambda=w(R)^(p-1)`. For any `0<=t<=w(y)`, convexity of `t^p-lambda t` implies

\[
t^p-\lambda t\le \max\{0,w(y)^p-\lambda w(y)\}.
\]

The positive term occurs exactly for `0<y<R`. Integrating with `t=g(y)` and using `int g=int_0^R w=1`,

\[
\int g^p
\le \lambda +\int_0^R(w^p-\lambda w)
=\int_0^R w^p.
\]

Finally

\[
\int_0^{a/4}(a y)^{-p/2}dy
={2^{p-1}\over2-p}a^{1-p}.
\]

This proves (3.1). The endpoint `p=1` is just normalization. For `f=1_[b-1/2,b+1/2]`, the pushforward is exactly `g=w 1_(0,a/4)`, so equality holds. `QED`.

The critical case for this card is

\[
\boxed{\|g\|_{3/2}\le 2|a|^{-1/3}.}
\tag{3.3}
\]

## 4. Uniform integrated Fresnel bound: `L^3`, not pointwise decay

Use the Fourier convention

`hat g(t)=int exp(i t y) g(y)dy`.

By Hausdorff-Young (from the `L^1->L^infinity` and Plancherel endpoints), for `1<=p<=2`, `q=p/(p-1)`,

\[
\|\widehat g\|_q\le (2\pi)^{1/q}\|g\|_p.
\]

Combining with Theorem 3.1 gives, for every `q>2`,

\[
\boxed{
\|\psi_{a,b}\|_q
\le (2\pi)^{1/q}
\left[2^{1/(q-1)}{q-1\over q-2}\right]^{(q-1)/q}
|a|^{-1/q}.
}
\tag{4.1}
\]

In particular,

\[
\boxed{
\int_{\mathbb R}|\psi_{a,b}(t)|^3dt
\le 8(2\pi)|a|^{-1},
\qquad
\|\psi_{a,b}\|_3\le2(2\pi)^{1/3}|a|^{-1/3}.
}
\tag{4.2}
\]

This is the sought replacement for the false law-uniform pointwise estimate. At each fixed nonzero `t`, fleet03/B17 showed that the law can make `|psi(t)|` arbitrarily close to one. Nevertheless the **integrated cubic norm** is uniformly finite, with the correct coefficient scaling.

The exponent `3` is structurally matched to the target threshold: `q=2` would require an `L^2` bound on the square-pushforward density, and the centered interval example has `g(y)=y^{-1/2}` near zero, so `g notin L^2`. The integrated route genuinely turns on only above two factors.

## 5. Three independent square directions give an `L^1` characteristic function

### Theorem 5.1 — `QFORM-INTEGRATED-THREE-SQUARE-v1`

Let `X_1,...,X_m` be independent, each with density bounded by one. For `m>=3`, take arbitrary shifts `b_j` and nonzero coefficients `a_j`, and put

\[
S=\sum_{j=1}^m a_j(X_j-b_j)^2.
\]

Then its characteristic function satisfies

\[
\boxed{
\|\phi_S\|_1
\le
4\pi\left({m-1\over m-2}\right)^{m-1}
\left(\prod_{j=1}^m|a_j|\right)^{-1/m}.
}
\tag{5.1}
\]

Consequently `S` has a bounded uniformly continuous density and

\[
\boxed{
\|p_S\|_\infty
\le
2\left({m-1\over m-2}\right)^{m-1}
\left(\prod_{j=1}^m|a_j|\right)^{-1/m}.
}
\tag{5.2}
\]

For the target threshold `m=3`,

\[
\boxed{
\|\phi_S\|_1\le16\pi(|a_1a_2a_3|)^{-1/3},
\qquad
\|p_S\|_\infty\le8(|a_1a_2a_3|)^{-1/3}.
}
\tag{5.3}
\]

No sign condition is required.

### Proof

Take `q=m` in (4.1) and use independence:

`phi_S(t)=prod_j psi_{a_j,b_j}(t)`.

Hölder with `m` equal exponents gives

`||phi_S||_1 <= prod_j ||psi_j||_m`.

The product of the `(2 pi)^(1/m)` factors is `2 pi`, while

\[
\left(
2^{1/(m-1)}{m-1\over m-2}
\right)^{m-1}
=2\left({m-1\over m-2}\right)^{m-1}.
\]

This is (5.1). Fourier inversion for an `L^1` characteristic function yields a bounded uniformly continuous density, and division by `2 pi` gives (5.2). `QED`.

For `m=3` this is a complete **integrated Fourier** proof of the diagonal threshold-three branch. Its constant `8` is weaker than the beta-integral constant `pi` from fleet03/B17, but it survives every sign pattern without selecting a same-sign pair and, more importantly for this card, it demonstrates that the pointwise counterexample does **not** kill a uniform integrated Fourier mechanism.

## 6. High-dimensional conditional corollary with arbitrary outside couplings

### Corollary 6.1 — `QFORM-DIAGONAL-PRINCIPAL-TRIPLE-L1-v1`

Let `A` be any real symmetric `n x n` matrix. Suppose there are three original coordinates `I={i_1,i_2,i_3}` such that the principal block is diagonal,

`A_{I,I}=diag(a_1,a_2,a_3)`,

with `|a_j|>=1`. No restriction is placed on couplings from these coordinates to `I^c` or on `A_{I^c,I^c}`. Then under the full target input assumptions,

\[
\boxed{\|\phi_{X^TAX}\|_1\le16\pi,
\qquad \|p_{X^TAX}\|_\infty\le8,}
\tag{6.1}
\]

and the output density has a uniformly continuous representative.

### Proof

Condition on all coordinates outside `I`. The remaining polynomial is

\[
\sum_{j=1}^3 a_j x_{i_j}^2+2\sum_{j=1}^3\beta_j x_{i_j}+c
=
\sum_{j=1}^3 a_j(x_{i_j}+\beta_j/a_j)^2+c'.
\]

The selected input coordinates remain independent with their original density bounds. Theorem 5.1 gives the same `L^1_t` bound `16 pi` for every fixed outside configuration, uniformly in the induced shifts and additive constant. If `phi_w` is the conditional characteristic function,

\[
\int|E_w\phi_w(t)|dt
\le E_w\int|\phi_w(t)|dt
\le16\pi.
\]

Fourier inversion gives (6.1). `QED`.

This is not the full conjecture: fleet02/B15's flat rank-three projector shows that the spectral hypothesis need not produce any fixed coordinate triple with order-one principal curvature. The remaining step must therefore aggregate delocalized curvature rather than select one good raw triple.

## 7. A decisive obstruction: scalar small-ball symmetrization cannot recover linear scaling

The independent-copy identity is still useful, but one natural use of it is impossible.

### Proposition 7.1 — `QFORM-ONE-DIFFERENCE-SMALLBALL-OBSTRUCTION-v1`

Let `Z` have a nonzero density `p in L^2`, and let `Z'` be an independent copy. Then `D=Z-Z'` has the continuous density

\[
k(s)=\int p(x)p(x-s)dx,
\]

with

\[
k(0)=\|p\|_2^2>0.
\]

Hence

\[
\boxed{
P(|Z-Z'|\le\varepsilon)
=2\varepsilon\|p\|_2^2+o(\varepsilon).
}
\tag{7.1}
\]

In particular, the elementary symmetrization inequality

\[
P(Z\in I)^2\le P(|Z-Z'|\le |I|)
\tag{7.2}
\]

cannot yield a linear `O(|I|)` bound from a scalar small-ball estimate on the one-copy difference: it would require an `O(epsilon^2)` estimate in (7.1), which is false even for smooth, bounded output densities.

### Proof

The formula for `k` is convolution with the reflected density. Translation is continuous in `L^2`, so `k` is continuous; Cauchy-Schwarz gives the needed domination and `k(0)=||p||_2^2`. Integrating `k` on `[-epsilon,epsilon]` proves (7.1). `QED`.

Thus the card's independent-copy mechanism must be used at the **integrated-frequency level** (or with additional vector/multicopy structure), not by taking a square root of a one-dimensional small-ball estimate for `Q-Q'`.

The diagonal three-square branch above has `p in L^infinity cap L^1`, hence `p in L^2`, so it already supplies a source-valid witness to this obstruction while satisfying the conjectured conclusion.

## 8. Conditional end-to-end chain and first unpaid implication

A valid Fourier chain would be:

1. prove a law- and dimension-uniform `L^1_t` bound for `phi_Q` under the three-large-eigenvalue hypothesis;
2. apply Fourier inversion to obtain a bounded uniformly continuous density;
3. specialize the constant independently of `n`, the laws and the eigenbasis.

This report closes step 1 for every conditional decomposition into three independent shifted square directions and identifies a sharp one-coordinate integrated ingredient. It also rules out the simplest scalar-difference symmetrization shortcut.

The first unpaid implication is the **delocalized aggregation step**:

> convert the product structure of the original coordinates and the aggregate rank-three spectral curvature into the cubic/integrated gain without selecting one principal triple and without pretending `U_i=X_i-X_i'` and `V_i=X_i+X_i'` are independent.

The flat rank-three projector from fleet02/B15 is the mandatory stress family for that step. A successful next lemma should be determinant/minor averaged or otherwise genuinely delocalized.

## 9. Status and correction ledger

* `FULL_TARGET`: OPEN.
* `QFORM-SQUARE-PUSHFORWARD-LP-SHARP-v1`: PROVED.
* `QFORM-INTEGRATED-THREE-SQUARE-v1`: PROVED.
* `QFORM-DIAGONAL-PRINCIPAL-TRIPLE-L1-v1`: PROVED.
* `QFORM-ONE-DIFFERENCE-SMALLBALL-OBSTRUCTION-v1`: PROVED; refutes only the scalar one-difference proof mechanism, not the target.
* Required corrections consumed: pointwise decay false; fiber-sup dimension loss; no independence after rotation.
* Named partner fleet03/B03: no completed deliverable found at the checked source pin; work continued without waiting.
* No numerical experiment or heuristic is used in these proofs.
* No novelty/publication-priority claim is made.
