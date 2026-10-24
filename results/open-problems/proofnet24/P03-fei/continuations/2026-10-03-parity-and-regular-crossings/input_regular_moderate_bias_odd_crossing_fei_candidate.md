# Ordinary FEI for input-regular odd-crossing score functions

Date: 2026-10-03. **Complete candidate derivation; independent audit pending.**
This strengthens the separately preserved
[bounded-ratio candidate](regular_moderate_bias_odd_crossing_fei_candidate.md)
by removing every lower bound on individual weights. It is a restricted
ordinary FEI theorem, without output parity. Novelty is unverified.

## The statement

Let \(m\ge1\) be odd, \(B\ge1\), and \(\lambda\ge0\). On the uniform
Boolean cube in dimension \(n\ge1\), put
\[
 S(X)=\sum_{i=1}^n w_iX_i,
 \qquad \sigma^2=\sum_iw_i^2>0.
\]
Assume input-weight regularity in the precise sense
\[
 \max_i|w_i|\le\frac{B\sigma}{\sqrt n}.
\tag{1}
\]
There is no minimum-weight premise. Let \(F:\mathbb R\to\{-1,1\}\)
have exactly \(m\) distinct genuine crossings \(\theta_1<\cdots<\theta_m\).
It is constant on the complementary open intervals, adjacent interval
labels are opposite, each crossing is assigned either adjacent label,
and there are no other isolated point anomalies. Suppose
\[
 |\theta_r|\le\lambda\sigma\quad(1\le r\le m).
\tag{2}
\]
For \(g=F(S)\), we prove
\[
 \boxed{H(g)\le C(m,B,\lambda)I(g).}
\tag{3}
\]
Entropy is in bits, includes the empty Fourier atom, and influence is
the physical flip probability. All crossing spacings are allowed.

Use the explicit constants
\[
 d=\frac{e^{-(\lambda+1)^2}}{\sqrt{2\pi}},\quad
 c_D=\sqrt{2/3},\quad E=2.24\sqrt2,\quad
 A=\frac{41}{\sqrt2(1-e^{-1})},
\]
\[
 K=\max\left\{1,\left\lceil
     \left(\frac{2EmB^2}{dc_D}\right)^2\right\rceil\right\},
 \quad N_0=\left\lceil\max\{2KB^2,K^2B^2\}\right\rceil.
\tag{4}
\]
Then a valid constant is
\[
 \boxed{C(m,B,\lambda)=
  \max\left\{\log_2N_0+3,
       \frac{(1+4Am)B\sqrt K}{(\ln2)dc_D}\right\}.}
\tag{5}
\]
Coordinate sign flips preserve entropy and influence, so we may take
all weights nonnegative in the proof. Zero weights cause no difficulty;
alternatively delete them before imposing (1), which improves regularity.
If \(\sigma=0\), \(g\) is constant and entropy is zero. Dimension zero
is likewise immediate. Scaling score and crossings together changes
neither (1), (2), nor the Boolean function.

## Inputs, entropy, and the odd-tail translation lemma

The established Klivans–O'Donnell–Servedio halfspace noise estimate,
Theorem 18 of the [primary author manuscript](https://www.cs.columbia.edu/~rocco/Public/focs02.pdf),
gives \(\operatorname{NS}_\varepsilon(h)\le20.5\sqrt\varepsilon\)
for every halfspace. Each crossing factor has its own allowed tie choice,
realized on the finite cube by a small threshold perturbation when needed.
The product of these factors is \(g\) up to a constant sign. Union bound
therefore gives
\[
 \operatorname{NS}_\varepsilon(g)\le20.5m\sqrt\varepsilon.
\]
The exact degree-noise identity, with \(\varepsilon=1/(2k)\), implies
\(\Pr[D\ge k]\le Am/\sqrt k\) for the squared-Fourier degree law.
Entropy conditional on degree is at most \(\log_2\binom nD\), so
\[
 \begin{aligned}
 H(g)&\le\log_2(n+1)
   +\frac1{\ln2}\mathbb E[D\ln(en/D)]\\
 &\le\frac{\sqrt n}{\ln2}
   +\frac{Am}{\ln2}\int_0^nt^{-1/2}\ln(n/t)\,dt\\
 &=\frac{1+4Am}{\ln2}\sqrt n.
 \end{aligned}
\tag{6}
\]
The full derivation, including \(k=1\), the real-degree tail and
\(\ln(n+1)\le\sqrt n\), is supplied in the preserved
[bounded-ratio candidate](regular_moderate_bias_odd_crossing_fei_candidate.md).
This entropy argument has no weight-ratio or minimum-weight hypothesis.

For any \(u,v\in\mathbb R\), remove the translated crossing endpoints
from \(\{r:F(r+u)\ne F(r+v)\}\), obtaining a union
\(A^\circ_{u,v}\) of at most \(2m\) bounded disjoint open intervals.
These intervals lie in
\[
 [\theta_1-\max(u,v),\theta_m-\min(u,v)].
\tag{7}
\]
Since \(m\) is odd, the tail labels \(a_-,a_+\) are opposite.
Direct integration after cancellation of the tails gives
\[
 \int_{\mathbb R}[F(r+v)-F(r+u)]\,dr
          =(v-u)(a_+-a_-).
\]
The integrand has magnitude two precisely on the pivotal set, up to
endpoints of measure zero. Consequently
\[
 |A^\circ_{u,v}|\ge|u-v|.
\tag{8}
\]
The open-component bound accounts for coincident translated crossings
and arbitrary adjacent endpoint labels; discarding endpoint atoms gives
a lower bound on discrete pivotal probability.

We also use Berry–Esseen with absolute constant \(0.56\), for independent
nonidentical summands. It is stated explicitly in Section 11.5, printed
page 350 of O'Donnell's author-hosted
[*Analysis of Boolean Functions*](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf).
For a weighted-sign remainder \(R\) with variance \(s^2>0\), its CDF
distance from \(N(0,s^2)\) is at most
\[
 0.56\frac{\sum w_i^3}{s^3}\le0.56\frac{w_{\max}}s.
\tag{9}
\]
For any open interval, the probability differs from its Gaussian
probability by at most twice this bound. The CDF comparison extends to
left limits because the Gaussian CDF is continuous, so (9) applies
without excluding attained-score atoms.

## The new regular-input block estimate

Suppose \(n\ge N_0\). Choose a uniform random \(K\)-subset \(J\),
independent of old and fresh input signs, and write
\[
 U=\sum_{i\in J}w_iX_i,\quad V=\sum_{i\in J}w_iY_i,
 \quad R=\sum_{i\notin J}w_iX_i.
\]
Conditional on \(J\), all three scores are independent. Let
\(a_J=\sum_{i\in J}w_i^2\) and \(s_J^2=\sigma^2-a_J\). From (1)
and (4), for every mask,
\[
 a_J\le\frac{KB^2\sigma^2}{n}\le\frac{\sigma^2}{2},
 \quad s_J^2\ge\frac{\sigma^2}{2},
 \quad |U|,|V|\le Kw_{\max}\le\frac{KB\sigma}{\sqrt n}\le\sigma.
\tag{10}
\]
Thus the pivotal intervals (7) lie within
\([-(\lambda+1)\sigma,(\lambda+1)\sigma]\). On that interval the
density of \(N(0,s_J^2)\) is at least \(d/\sigma\). The CDF error
from (9) is at most
\[
 \delta_J\le\frac{0.56\sqrt2B}{\sqrt n}.
\tag{11}
\]
Using at most \(2m\) open intervals and (8), for fixed \(J,U=u,V=v\),
\[
 \Pr[F(R+u)\ne F(R+v)]
    \ge\frac{d|u-v|}{\sigma}-\frac{EmB}{\sqrt n}.
\tag{12}
\]
This lower bound may be negative before averaging, which is harmless.

The selected-difference moments are exact:
\[
 \mathbb E[(U-V)^2\mid J]=2a_J,
\quad
 \mathbb E[(U-V)^4\mid J]
     =3(2a_J)^2-4\sum_{i\in J}w_i^4\le3(2a_J)^2.
\]
Hölder interpolation gives
\[
 \mathbb E[|U-V|\mid J]\ge c_D\sqrt{a_J}.
\tag{13}
\]
If \(a_J=0\), both sides are zero and no division is used.

The absence of a positive minimum weight is addressed by averaging over
the mask. We have exactly
\(\mathbb E_Ja_J=K\sigma^2/n\), while
\(0\le a_J\le KB^2\sigma^2/n\). Pointwise,
\(\sqrt{a_J}\ge a_J/\sqrt{KB^2\sigma^2/n}\). Therefore
\[
 \boxed{\mathbb E_J\sqrt{a_J}
             \ge\frac{\sqrt K\,\sigma}{B\sqrt n}.}
\tag{14}
\]
This is a lower bound obtained from a uniform upper bound and the exact
first moment; it does not use the opposite direction of Jensen's inequality.

Average (12), then (13) and (14), and use the choice of \(K\):
\[
 \begin{aligned}
 \Pr[g(X)\ne g(X^{\mathrm{resample}\,J})]
 &\ge\frac{dc_D\sqrt K/B-EmB}{\sqrt n}\\
 &\ge\frac{dc_D\sqrt K}{2B\sqrt n}.
 \end{aligned}
\tag{15}
\]
Resampling the selected coordinates successively, every intermediate
input is uniform; resampling coordinate \(i\) changes its output with
probability exactly \(I_i(g)/2\). The union bound, averaged over the
uniform mask, gives
\[
 \Pr[g(X)\ne g(X^{\mathrm{resample}\,J})]
          \le\frac{K}{2n}I(g).
\tag{16}
\]
Hence
\[
 \boxed{I(g)\ge\frac{dc_D}{B\sqrt K}\sqrt n
          \quad(n\ge N_0).}
\tag{17}
\]

## Finish, relations, and scope

Combine (6) and (17) in dimensions at least \(N_0\). For dimensions
below \(N_0\), use the established weak bound
\(H(g)\le(\log_2n+3)I(g)\le(\log_2N_0+3)I(g)\).
Its full elementary derivation, including the empty spectral atom and
cube edge-isoperimetric induction, is in the separate
[logarithmic proof](output_parity_unate_gate_combinations_logarithmic_proof.md).
These two cases prove (3) with the constant (5).

The weight-ratio premise \(1\le w_i\le B\) implies (1), because
\(\sigma\ge\sqrt n\). Thus this theorem contains that restricted
class, although the separately preserved bounded-ratio proof has a
smaller choice of \(K\). Regularity (1) permits arbitrarily small
individual weights and does not bound their largest/smallest ratio.

The parameter \(B\) measures regularity of input weights alone; the
bias restriction is explicitly (2). Bias is not included as an extra
weight in (1). The threshold locations can be arbitrarily close and need
not be uniformly separated. Odd crossing count is essential to this
particular proof; it does not cover a general even-crossing function.
Neither arbitrary irregular weights nor unbounded normalized threshold
biases are covered with a universal constant. Full Boolean FEI and the
unrestricted arbitrary-weight three-crossing case remain open.

Halfspace noise bounds, Berry–Esseen, weak logarithmic FEI, and the
noise-to-entropy estimate are established tools. Historical priority of
this precise restricted consequence is not certified. Independent audit
of the new mask averaging and meaningful finite checks are pending.
