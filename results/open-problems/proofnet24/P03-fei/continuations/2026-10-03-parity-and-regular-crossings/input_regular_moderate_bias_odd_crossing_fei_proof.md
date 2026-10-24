# Ordinary FEI for input-regular odd-crossing score functions

Date: 2026-10-03. **Complete proof; independent internal analytic audit passes.**
This strengthens the separately preserved
[bounded-ratio proof](regular_moderate_bias_odd_crossing_fei_proof.md)
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
Here are the details of the degree-tail calculation, to fix every
constant without an inherited theorem. Independent bit-flip noise gives
\(2\operatorname{NS}_\varepsilon(g)=
\sum_S\widehat g(S)^2[1-(1-2\varepsilon)^{|S|}]\).
At \(\varepsilon=1/(2k)\), degrees at least k contribute at least
\(1-e^{-1}\), including k=1, and therefore their mass is at most
\(Am/\sqrt k\). For real t positive, apply this estimate at
\(\lceil t\rceil\) to get the bound \(Am/\sqrt t\).
Conditioning on degree bounds within-level entropy by
\(\log_2\binom nj\le j\ln(en/j)/\ln2\), while degree entropy
is at most \(\log_2(n+1)\). The function
\(b(t)=t\ln(en/t)\), with b(0)=0, has derivative \(\ln(n/t)\).
Tail integration gives the integral in (6), equal to \(4\sqrt n\).
Finally \(\sqrt n-\ln(n+1)\) is positive at one and has
nonnegative derivative for n at least one, since \(n+1\ge2\sqrt n\).
This proves (6), including degree zero, without a weight-ratio or
minimum-weight hypothesis.

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
A complete elementary derivation, including the empty spectral atom and
cube edge-isoperimetric induction, is reproduced in the appendix below.
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
this precise restricted consequence is not certified. The separate
[independent analytic audit](input_regular_moderate_bias_odd_crossing_heat_audit.md)
passes the entire regular-input argument. Its [independent checker](verify_input_regular_odd_crossing_heat.py)
and [report](input_regular_odd_crossing_heat_checks.json) pass 63 rational
weight vectors, 3,339 mask/moment checks with 459 zero-energy masks,
189 exact averages, and 126 exact resampling comparisons. The separate
[author mask checker](verify_input_regular_odd_crossing_mask.py) and
[report](input_regular_odd_crossing_mask_checks.json) pass 11,868 exact
mask/moment checks and 362 averages, including positive weight ratios
up to 1,048,576 and zero weights. Numerical square-root comparisons are
supplements to the exact algebra. The unchanged
[translation/atom checker](verify_regular_moderate_bias_odd_crossing.py)
and [report](regular_moderate_bias_odd_crossing_checks.json) supply the
shared exact constituent checks. Large N0 is not truth-table enumerated;
the analytic argument is the proof of that regime. These checks are
internal, and do not certify historical novelty or external peer review.

## Prior work and known overlaps

Chakraborty, Kulkarni, Lokam and Saurabh, *Upper Bounds on Fourier Entropy*,
[primary ECCC revision 2](https://eccc.weizmann.ac.il/report/2013/052/revision/2/download/),
Theorem 4.5, already converts a noise sensitivity power bound into a
Fourier entropy bound. Their Corollary 4.8 supplies the established LTF
entropy bound of order square root of the dimension. Together with
KOS Theorem 21 and the edge-flip union bound, this framework gives
entropy of order m times square root of the dimension for functions
of m halfspaces. The explicit degree-tail integral above is a variant
of this established argument, and is not claimed new.

The one-crossing case is a linear threshold function and is not a
claimed novelty. Prior regular-LTF FEI appears in Corollary 10 of the
[primary regular/random-LTF manuscript](https://iuuk.mff.cuni.cz/~koucky/LBCAD/papers/random-ltf.pdf).
Its Definition 9 normalizes and bounds the bias as an additional weight;
our input regularity and normalized crossing bias are stated separately.
When all weights are equal, arbitrary score labelings are symmetric,
so FEI is already covered by the O'Donnell–Wright–Zhou
[primary symmetric-function theorem](https://www.cs.cmu.edu/~odonnell/papers/fei.pdf).
These overlaps must be credited. The specific m at least three weighted
odd-crossing consequence has not been certified historically new.

## Appendix: complete weak logarithmic FEI bound


For every Boolean \(f\) in dimension \(n\ge1\),
\[
 \boxed{H(f)\le(\log_2n+3)I(f).}
\]
Here \(H\) includes the empty Fourier coefficient, and all influences
are physical bit-flip probabilities. We prove the weak bound completely, without
assuming a constant variance or influence bounded away from zero.

First recall the classical cube edge-isoperimetric inequality, in this
normalization:
\[
 I(f)\ge2r\log_2(1/r),
\]
where \(r\le1/2\) is the minority probability. An explicit induction
is short. For an event \(E\) of size \(a\) in the \(n\)-cube, its
undirected boundary is at least \(a\log_2(2^n/a)\), with the zero-size
convention. Split its sections into sizes \(a_0\le a_1\), and write
\(u=a_0/a\). By induction, the total internal boundary is at least
\[
 a\log_2(2^{n-1}/a)+ah_2(u).
\]
The crossing boundary is at least \(a_1-a_0=a(1-2u)\).
Since concavity gives \(h_2(u)\ge2u\) on \([0,1/2]\), their sum
is at least \(a\log_2(2^n/a)\). The zero-dimensional base is immediate.
Physical influence is twice the undirected boundary divided by \(2^n\),
giving the edge bound.

For a nonconstant \(f\), let
\(v=\operatorname{Var}(f)=4r(1-r)\) and
\(R=\log_2(1/r)\). The elementary binary entropy bound is
\[
 h_2(v)\le4rR\le2I(f).
\]
For \(r\le1/4\), indeed
\[
 h_2(v)\le v[\log_2(1/v)+\log_2e]
 =v\left[R+\log_2\frac{e}{4(1-r)}\right]\le vR\le4rR,
\]
because \(4(1-r)\ge3>e\). For \(r\ge1/4\), use
\(h_2(v)\le1\le4r\le4rR\). This includes \(v=1\).
The second inequality in the binary bound follows from the edge bound. Constants have both
sides zero.

Let \(P\) be the squared-Fourier spectral law. Its empty atom has mass
\(1-v\), and the nonempty atoms have mass \(v\). For \(v>0\), denote
the conditional nonempty law by \(P_+\). On nonempty subsets define
the strictly positive reference probability law
\[
 Q(S)=\frac{n^{-|S|}}{Z_n},\qquad
 Z_n=\sum_{S\ne\varnothing}n^{-|S|}
     =(1+1/n)^n-1.
\]
For \(n\ge1\), \(1\le Z_n<e-1<2\); in dimension one, \(Z_1=1\).
Nonnegativity of the finite relative entropy \(D(P_+\|Q)\) gives
\[
 H(P_+)\le\mathbb E_{P_+}|S|\log_2n+\log_2Z_n.
\]
The full spectral energy satisfies
\(v\mathbb E_{P_+}|S|=I(f)\). Splitting the empty atom and using the binary bound,
\[
 \begin{aligned}
 H(f)&=h_2(v)+vH(P_+)\\
 &\le h_2(v)+I(f)\log_2n+v\log_2Z_n\\
 &\le2I(f)+I(f)\log_2n+I(f).
 \end{aligned}
\]
The final step uses \(\log_2Z_n<1\) and Fourier Poincare
\(v\le I(f)\). This proves the weak bound, with no lost empty spectral atom.

Universal weak bounds of order \(\log n\) precede this work. For
example, the primary Wan–Wright–Wu manuscript
[*Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture*](https://arxiv.org/pdf/1312.3003)
discusses such bounds in Section 1.1; its Lemma 1.5 and Appendix B
retain the empty atom at cost \(2I(f)\). The proof above is supplied
for transparent constants and normalization, not as a novelty claim
for the weak bound or classical edge isoperimetry.

