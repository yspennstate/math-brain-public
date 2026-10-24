Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. GPT-6 / maximum reasoning was requested as a preference, but no authenticated runtime model-effort selector or guaranteed full-hour execution is exposed here, so I do not claim it.

# P03-A analytic proof report — fine-secant monotonicity above sqrt(2) for small mean-preserving three-point perturbations

**Status:** PROVED PARTIAL / NEW RESTRICTED MONOTONICITY THEOREM CANDIDATE. Not independently audited. This is not the full Lyons–Pemantle–Peres conjecture.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursion / derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Canonical ownership was checked on assignment and is unchanged. P03-B retains coupling/regeneration/posterior-score work; I used its `0904Z` score/continuation-energy report only for continuity and did not duplicate that argument. Old D0047 history is untouched.

**Captured master immediately before this write:** `84e9590e61a598d9d276dc51a4e70b4630808f80`.

**Inherited analytic checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1559Z__mean-preserving-three-point-profile-and-mesoscopic-interior-order.md`.

That checkpoint proved global relative `L^2` concentration of the escape probability for the symmetric mean-preserving `{1,2,3}` family, an exact one-coordinate effective-degree defect, and monotonic ordering only for secants wider than `O(epsilon)`. The missing obligation was to control arbitrarily fine secants. This report closes that obligation on every interval `[a,2)` with `a>sqrt(2)`, for sufficiently small offspring perturbation.

The fixed full-source metric remains

`R_full: 1 -> 1`.

---

## 1. Source convention and currently checked frontier

At a non-root vertex with `k` children I use the reciprocal/parent-bias convention

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\tag{1.1}
\]

Thus larger `lambda` means weaker outward bias. For offspring mean `m`, transience is `0<=lambda<m`, and the LPP conjecture asks that the speed `ell_lambda` be nonincreasing over the whole transient interval. In the original outward-bias variable `beta=1/lambda`, this is increasing speed in `beta`.

Primary historical partial source: G. Ben Arous, A. Fribergh and V. Sidoravicius, arXiv:1111.5865 / CPAM 67 (2014), the high-outward-bias monotonicity theorem. The old cutoff is not used as the present frontier. A bounded current source check on 20 September 2026 again found the later Song–Wang–Xiang theorem, J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: it records Aidekon's no-leaf monotonicity improvement through parent bias `lambda<=1/2`, and for minimum offspring `m_1>=2` proves the stronger range

\[
0\le\lambda\le \frac{m_1}{1+\sqrt{1-1/m_1}}.
\tag{1.2}
\]

Bowditch–Tokushige, arXiv:1906.07913 and arXiv:2006.03433, provide differentiability/analyticity in ballistic regimes but no source-wide derivative sign. I found no later source-wide resolution in the bounded check; that is negative search evidence, not a novelty certificate.

For the family treated below, `m_1=1`, so the broad source-uniform certified range is only the `lambda<=1/2` range. The theorem here creates a disjoint high-`lambda` interval with **all fine secants controlled**, not merely mesoscopic pairs.

---

## 2. Family and inherited global escape concentration

Fix

\[
P_\varepsilon(\nu=1)=\frac\varepsilon2,\qquad
P_\varepsilon(\nu=2)=1-\varepsilon,\qquad
P_\varepsilon(\nu=3)=\frac\varepsilon2,
\qquad 0<\varepsilon<1.
\tag{2.1}
\]

Then

\[
E\nu=2,\qquad \operatorname{Var}(\nu)=\varepsilon.
\tag{2.2}
\]

Let `B=B_{lambda,epsilon}` denote the quenched descendant escape probability and

\[
B\stackrel d=\frac{S}{\lambda+S},\qquad
S=\sum_{i=1}^{\nu} B_i.
\tag{2.3}
\]

Put

\[
b_\lambda:=1-\frac\lambda2=\frac{2-\lambda}{2},\qquad
e_\lambda:=EB.
\tag{2.4}
\]

The inherited `1559Z` theorem gives, simultaneously for all `0<=lambda<2`,

\[
\frac{b_\lambda}{1+\varepsilon/2}\le e_\lambda\le b_\lambda,
\qquad
\operatorname{Var}(B)\le\frac\varepsilon2e_\lambda^2.
\tag{2.5}
\]

The decisive normalization in this run is therefore

\[
Z_\lambda:=\frac{B}{e_\lambda}.
\tag{2.6}
\]

It has

\[
EZ_\lambda=1,
\qquad
\boxed{\operatorname{Var}(Z_\lambda)\le\frac\varepsilon2}
\tag{2.7}
\]

**uniformly all the way to `lambda=2`.** This exact mean-one normalization is what makes the random-sum coupling contract with factor `sqrt(2)/lambda`, rather than paying a mean-difference term.

Write

\[
d_\lambda:=e_\lambda-b_\lambda\le0.
\tag{2.8}
\]

From (2.5),

\[
|d_\lambda|=b_\lambda-e_\lambda
\le \frac\varepsilon2 e_\lambda
\le\frac\varepsilon2.
\tag{2.9}
\]

If

\[
Y_\lambda:=\sum_{i=1}^{\nu} Z_{\lambda,i},
\tag{2.10}
\]

then

\[
Z_\lambda\stackrel d=
F_{\lambda,d_\lambda}(Y_\lambda),
\qquad
F_{\lambda,d}(y):=
\frac{y}{\lambda+(b_\lambda+d)y}.
\tag{2.11}
\]

Because `lambda+2b_lambda=2`, it is often useful to rewrite the denominator as

\[
D_{\lambda,d}(y)
=2+b_\lambda(y-2)+dy.
\tag{2.12}
\]

---

## 3. A uniform fourth-moment lemma for the normalized escape profile

The previous report only needed second moments. Fine parameter secants require enough integrability to control the `lambda` derivative of the normalized transform without introducing a critical-edge singularity. Bounded offspring gives exactly what is needed.

Fix any

\[
a>\sqrt2
\tag{3.1}
\]

and consider `a<=lambda<2`.

### Lemma 3.1 — uniform fourth centered moment

There are `epsilon_0(a)>0` and `C_a<infinity` such that, for every `0<epsilon<=epsilon_0(a)` and every `a<=lambda<2`,

\[
\boxed{
E|Z_\lambda-1|^4\le C_a\varepsilon.
}
\tag{3.2}
\]

Consequently, with `R_lambda:=Y_lambda-2`,

\[
ER_\lambda^2\le2\varepsilon,
\qquad
\boxed{ER_\lambda^4\le C_a\varepsilon.}
\tag{3.3}
\]

#### Proof

Let

\[
V:=Z_\lambda-1,\qquad
s^2:=EV^2\le\frac\varepsilon2,\qquad
\mu_3:=EV^3,\qquad
\mu_4:=EV^4.
\tag{3.4}
\]

Write `xi:=nu-2`, so `xi` is `-1,0,+1` with probabilities `epsilon/2,1-epsilon,epsilon/2`, and

\[
R=Y-2=\xi+\sum_{i=1}^{\nu}V_i.
\tag{3.5}
\]

The variance identity is immediate:

\[
ER^2=2s^2+\varepsilon\le2\varepsilon.
\tag{3.6}
\]

For the fourth moment, conditioning on `nu=1,2,3` and using the exact centered iid sum formula gives

\[
\boxed{
ER^4
=2\mu_4+4\varepsilon\mu_3
+\varepsilon+12\varepsilon s^2
+(6+3\varepsilon)s^4.
}
\tag{3.7}
\]

This identity is useful: the coefficient of `mu_4` is exactly `2`, independent of `epsilon`. Also

\[
|\mu_3|\le(s^2\mu_4)^{1/2}.
\tag{3.8}
\]

Young's inequality and `s^2<=epsilon/2` therefore imply, for `epsilon<=1`,

\[
ER^4\le \frac52\mu_4+C\varepsilon
\tag{3.9}
\]

for an absolute finite `C`.

Now subtract one from the recursion (2.11). Since

\[
Y-D_{\lambda,d}(Y)
=\frac\lambda2(Y-2)-dY,
\]

we have the exact identity

\[
V
=\frac{(\lambda/2)R-dY}{D_{\lambda,d}(Y)}.
\tag{3.10}
\]

Because `D=lambda+eY>=lambda>=a`,

\[
\left|\frac{(\lambda/2)R}{D}\right|\le\frac{|R|}{2},
\qquad
\left|\frac{dY}{D}\right|\le\frac{\varepsilon}{2a}Y.
\tag{3.11}
\]

Use the standard Young inequality `(x+y)^4 <= 2x^4+C_4 y^4` for some absolute finite `C_4`. Then

\[
\mu_4\le\frac18ER^4+C_a\varepsilon^4 EY^4.
\tag{3.12}
\]

Since `Y=2+R`, `EY^4<=C(1+ER^4)`. Insert (3.9) into (3.12). For sufficiently small `epsilon_0(a)`, the `epsilon^4 mu_4` term is absorbable, while the leading coefficient is

\[
\frac18\cdot\frac52=\frac5{16}<1.
\]

Hence `mu_4<=C_a epsilon`. Returning to (3.9) gives the same bound for `ER^4`. QED.

### Remark 3.2

No upper cutoff `lambda<=2-eta` is needed. This is important: normalization by `e_lambda`, rather than by the deterministic scale `b_lambda`, removes the vanishing escape scale from all moments used below.

---

## 4. Exact companion identity for the mean defect

The mean-one condition `EZ=1` gives a scalar identity that couples `d_lambda` to the normalized law.

Since

\[
1=E\frac{Y}{D},
\tag{4.1}
\]

and

\[
Y-D=\frac\lambda2(Y-2)-dY,
\tag{4.2}
\]

we obtain

\[
d=\frac\lambda2E\frac{Y-2}{D}.
\tag{4.3}
\]

Because `E(Y-2)=0`, subtracting `1/2` inside the reciprocal produces a second exact form. Put

\[
A_\lambda:=E\frac{(Y-2)^2}{D},
\qquad
C_\lambda:=E\frac{(Y-2)Y}{D}.
\tag{4.4}
\]

Then

\[
\boxed{
d_\lambda
=-\frac{\lambda b_\lambda}{4}
\frac{A_\lambda}{1+\lambda C_\lambda/4}.
}
\tag{4.5}
\]

Indeed,

\[
\frac1D-\frac12
=-\frac{b(Y-2)+dY}{2D},
\]

which substituted into (4.3) yields

\[
d=-\frac{\lambda b}{4}A-\frac{\lambda d}{4}C.
\]

By Lemma 3.1,

\[
A_\lambda=O_a(\varepsilon),
\qquad
C_\lambda=O_a(\sqrt\varepsilon)
\tag{4.6}
\]

uniformly for `a<=lambda<2`. After shrinking `epsilon_0(a)`,

\[
1+\lambda C_\lambda/4\ge\frac12.
\tag{4.7}
\]

This formula is the scalar part of the fine-secant argument.

---

## 5. Fine secant control of the normalized fixed point

Let `lambda,lambda' in [a,2)`, and abbreviate

\[
W:=W_2(\mathcal L(Z_\lambda),\mathcal L(Z_{\lambda'})),
\qquad
\Delta:=|\lambda-\lambda'|.
\tag{5.1}
\]

Couple the offspring count `nu` identically and couple each child pair `(Z_i,Z_i')` optimally, independently across children. Since both normalized laws have mean one,

\[
E(Z_i-Z_i')=0.
\]

Therefore the random-sum difference has the exact second-moment identity

\[
\boxed{
\|Y-Y'\|_2=\sqrt2\,W.
}
\tag{5.2}
\]

This is where the threshold `sqrt(2)` enters.

The transform derivatives are

\[
\partial_yF_{\lambda,d}(y)
=\frac{\lambda}{D^2},
\tag{5.3}
\]

\[
\partial_\lambda F_{\lambda,d}(y)
=\frac{y(y-2)}{2D^2}
\quad\text{when `d` is held fixed},
\tag{5.4}
\]

and

\[
\partial_dF_{\lambda,d}(y)
=-\frac{y^2}{D^2}.
\tag{5.5}
\]

Since `D>=lambda>=a`, (5.2) and (5.3) give the strict law-change contraction

\[
\left\|F_{\lambda,d}(Y)-F_{\lambda,d}(Y')\right\|_2
\le
\frac{\sqrt2}{a}W.
\tag{5.6}
\]

Set

\[
q_a:=\frac{\sqrt2}{a}<1.
\tag{5.7}
\]

The parameter derivative (5.4) is small because `Y-2` is small. By Lemma 3.1,

\[
E[Y^2(Y-2)^2]
=E[(2+R)^2R^2]
=O_a(\varepsilon),
\tag{5.8}
\]

where `E|R|^3<=sqrt(ER^2 ER^4)=O_a(epsilon)` was used. Hence

\[
\|\partial_\lambda F(Y)\|_2=O_a(\sqrt\varepsilon).
\tag{5.9}
\]

Similarly, (5.5) and the uniform fourth moment give

\[
\|\partial_dF(Y)\|_2=O_a(1).
\tag{5.10}
\]

Splitting the two fixed-point transforms first by law, then by `lambda`, then by `d`, yields

\[
\boxed{
W
\le q_a W
+C_a\sqrt\varepsilon\,\Delta
+C_a|d_\lambda-d_{\lambda'}|.
}
\tag{5.11}
\]

We now control the scalar defect by (4.5). Mean-value estimates using Lemma 3.1 give

\[
|A_\lambda-A_{\lambda'}|
\le
C_a\Big(
\sqrt\varepsilon\,W
+\varepsilon\Delta
+\varepsilon|d_\lambda-d_{\lambda'}|
\Big),
\tag{5.12}
\]

and

\[
|C_\lambda-C_{\lambda'}|
\le
C_a\Big(
W+\varepsilon\Delta
+\sqrt\varepsilon|d_\lambda-d_{\lambda'}|
\Big).
\tag{5.13}
\]

For completeness, the powers of `epsilon` in these two bounds come from the vanishing of the relevant numerators at `Y=2`:

* for `A=E[R^2/D]`, the law derivative is `O(|R|+R^2)`, whose `L^2` norm is `O(sqrt(epsilon))`; the direct `lambda` derivative is `O(|R|^3)` and the direct `d` derivative is `O(R^2Y)`, both with expectation `O(epsilon)`;
* for `C=E[RY/D]`, the law derivative is only `O(1+|R|)`, while the direct `lambda` derivative is `O(R^2Y)` and the direct `d` derivative is `O(RY^2)`.

Substituting (5.12)–(5.13) into the exact quotient (4.5), using `A=O(epsilon)`, `C=O(sqrt(epsilon))` and (4.7), gives

\[
|d_\lambda-d_{\lambda'}|
\le
C_a\big(
\varepsilon\Delta+\sqrt\varepsilon W
\big)
+C_a\varepsilon|d_\lambda-d_{\lambda'}|.
\tag{5.14}
\]

After another harmless reduction of `epsilon_0(a)`, the last term is absorbed:

\[
\boxed{
|d_\lambda-d_{\lambda'}|
\le
C_a\big(
\varepsilon\Delta+\sqrt\varepsilon W
\big).
}
\tag{5.15}
\]

Insert (5.15) into (5.11). Since `q_a<1`, choose `epsilon_a>0` so small that the additional `C_a sqrt(epsilon)` coefficient of `W` is at most `(1-q_a)/2`. Then

\[
\boxed{
W_2(\mathcal L(Z_\lambda),\mathcal L(Z_{\lambda'}))
\le C_a\sqrt\varepsilon\,|\lambda-\lambda'|,
}
\tag{5.16}
\]

and back-substitution gives

\[
\boxed{
|d_\lambda-d_{\lambda'}|
\le C_a\varepsilon|\lambda-\lambda'|.
}
\tag{5.17}
\]

These are the missing **fine-secant estimates**. They hold uniformly for all pairs in `[a,2)`, including pairs arbitrarily close to the critical edge and pairs with arbitrarily small separation.

Since `e=b+d`, (5.17) also gives

\[
|e_\lambda-e_{\lambda'}|
\le\left(\frac12+C_a\varepsilon\right)|\lambda-\lambda'|.
\tag{5.18}
\]

---

## 6. Fine secants of Aidekon's effective offspring tilt

For `lambda>1`, define as in the inherited report

\[
H_n(\lambda)
:=E\frac{B_0}{\lambda-1+\sum_{i=0}^{n}B_i},
\qquad n=1,2,3.
\tag{6.1}
\]

The symmetric offspring law gives the exact effective-degree defect

\[
q_\lambda:=2-M_\lambda
=\frac\varepsilon2
\frac{H_1-H_3}
{\frac\varepsilon2H_1+(1-\varepsilon)H_2+\frac\varepsilon2H_3}.
\tag{6.2}
\]

To avoid the fact that every `H_n` vanishes at criticality, divide out `e_lambda`:

\[
\bar H_n(\lambda)
:=\frac{H_n(\lambda)}{e_\lambda}
=E\frac{Z_0}
{\lambda-1+e_\lambda\sum_{i=0}^{n}Z_i}.
\tag{6.3}
\]

Then the factor `e_lambda` cancels from (6.2):

\[
\boxed{
q_\lambda
=\frac\varepsilon2
\frac{\bar H_1-\bar H_3}
{\frac\varepsilon2\bar H_1+(1-\varepsilon)\bar H_2+\frac\varepsilon2\bar H_3}.
}
\tag{6.4}
\]

Let

\[
\kappa:=a-1>0.
\tag{6.5}
\]

The denominator inside every `bar H_n` is at least `kappa`. It is also at most `lambda-1+n+1< n+2<=5`, because `eZ=B<=1`. Thus

\[
\boxed{
\frac15\le \bar H_n(\lambda)\le\frac1\kappa,
\qquad n=1,2,3.
}
\tag{6.6}
\]

The integrand in (6.3) is uniformly Lipschitz in `lambda`, in `e`, and in each `Z_i` in the required `L^1/L^2` sense. Using (5.16) and (5.18) with independent coordinatewise optimal couplings therefore gives

\[
\boxed{
|\bar H_n(\lambda)-\bar H_n(\lambda')|
\le C_a|\lambda-\lambda'|,
\qquad n=1,2,3.
}
\tag{6.7}
\]

The lower bound (6.6) means that the denominator in (6.4) is uniformly at least `1/5`. Consequently there are finite constants `K_a,L_a`, independent of sufficiently small `epsilon`, such that

\[
\boxed{0\le q_\lambda\le K_a\varepsilon}
\tag{6.8}
\]

and, crucially,

\[
\boxed{
|q_\lambda-q_{\lambda'}|
\le L_a\varepsilon|\lambda-\lambda'|.
}
\tag{6.9}
\]

Equation (6.9) is exactly what the preceding mesoscopic report lacked.

---

## 7. New monotonicity theorem on the entire interval `[a,2)`

Aidekon's speed formula reduces to

\[
\ell_{\lambda,\varepsilon}
=\frac{M_\lambda-\lambda}{M_\lambda+\lambda}
=\frac{2-q_\lambda-\lambda}{2-q_\lambda+\lambda}.
\tag{7.1}
\]

Take

\[
a\le\lambda_1<\lambda_2<2,
\qquad
\Delta=\lambda_2-\lambda_1.
\]

Exact cross-multiplication gives

\[
\ell_{\lambda_1,\varepsilon}
-\ell_{\lambda_2,\varepsilon}
=
\frac{2\big[\lambda_2(2-q_1)-\lambda_1(2-q_2)\big]}
{(2-q_1+\lambda_1)(2-q_2+\lambda_2)}.
\tag{7.2}
\]

The square bracket is

\[
2\Delta-(\lambda_2q_1-\lambda_1q_2)
=2\Delta-\Delta q_1-\lambda_1(q_1-q_2).
\tag{7.3}
\]

By (6.8)–(6.9),

\[
\lambda_2q_1-\lambda_1q_2
\le (K_a+2L_a)\varepsilon\Delta.
\tag{7.4}
\]

Hence, after shrinking `epsilon_a` so that

\[
(K_a+2L_a)\varepsilon_a\le1,
\tag{7.5}
\]

the bracket in (7.2) is at least `Delta`. Also each denominator factor is less than `4`. Therefore

\[
\boxed{
\ell_{\lambda_1,\varepsilon}
-\ell_{\lambda_2,\varepsilon}
\ge \frac18(\lambda_2-\lambda_1)>0.
}
\tag{7.6}
\]

We have proved:

### Theorem 7.1 — fine-secant interior-to-critical monotonicity for a genuinely random family

For every fixed

\[
\boxed{a>\sqrt2}
\]

there exists `epsilon_a>0` such that, for every

\[
0<\varepsilon\le\varepsilon_a,
\]

the biased walk on the no-leaf Galton–Watson tree with offspring law

\[
P(\nu=1)=P(\nu=3)=\varepsilon/2,
\qquad
P(\nu=2)=1-\varepsilon
\]

has strictly decreasing parent-bias speed on the **whole interval**

\[
\boxed{a\le\lambda<2.}
\tag{7.7}
\]

After decreasing `epsilon_a` if necessary, the uniform secant margin (7.6) holds for every pair in that interval.

In particular, taking `a=3/2`, there exists a nonzero `epsilon_*` such that every sufficiently small but genuinely random symmetric `{1,2,3}` perturbation of the deterministic binary tree satisfies

\[
\boxed{\ell_{\lambda,\varepsilon}\ \text{strictly decreases for all }\ 3/2\le\lambda<2.}
\tag{7.8}
\]

This is stronger than the previous `1559Z` result in two ways:

1. there is **no minimum secant width**; arbitrarily fine pairs are ordered;
2. there is **no terminal gap**; the same argument reaches all the way to `lambda\uparrow2`.

No differentiability theorem is needed for the proof; it is entirely a secant argument.

---

## 8. What actually caused the `sqrt(2)` threshold

The threshold is not coming from the speed formula. It comes only from the deliberately crude but robust normalized-law contraction

\[
\|Y-Y'\|_2=\sqrt2 W_2(Z,Z')
\]

combined with

\[
\sup_y|\partial_yF_{\lambda,d}(y)|\le\frac1\lambda.
\]

Thus the contraction constant is

\[
q=\frac{\sqrt2}{\lambda}.
\tag{8.1}
\]

At the deterministic binary fixed point the true local coefficient is much better:

\[
\partial_yF_{\lambda,0}(2)=\frac\lambda4,
\]

so the infinitesimal mean-zero `W_2` factor is

\[
\frac{\lambda}{2\sqrt2}<1
\qquad\text{for every }\lambda<2.
\tag{8.2}
\]

Therefore `sqrt(2)` is an artifact of using the worst-case denominator `D>=lambda`, not a candidate phase transition.

The next analytic attack is now very concrete: replace the supremum derivative in (5.6) by an averaged derivative bound under the already-proved concentration

\[
ER^2=O(\varepsilon),\qquad ER^4=O(\varepsilon).
\]

A successful estimate of the form

\[
E\left[
\left(
\frac{\lambda}{D(Y)D(Y')}
\right)^2
(Y-Y')^2
\right]
\le
\left(\frac{\lambda^2}{8}+O(\sqrt\varepsilon)\right)W^2
\tag{8.3}
\]

would replace `sqrt(2)/lambda` by `lambda/(2sqrt(2))+o(1)` and should push Theorem 7.1 from `a>sqrt(2)` to **every compact interval `[a,2)` with `a>1`**. The remaining source gap would then be reduced to `(1/2,1]` for this family. The obstacle is correlation between the denominator and the optimal-coupling difference; it should be attacked by a good/bad decomposition using the fourth-moment estimate rather than by another worst-case bound.

---

## 9. Failed route that taught something

The first attempted derivative route differentiated the unnormalized recursion directly and introduced

\[
J=\partial_\lambda B,
\qquad K=J+1/2.
\]

The linearized child coefficient can be bounded by `1/lambda`, but the noncentered random sum then pays an `E nu(nu-1)(EK)^2` term. That makes a direct `L^2` closure needlessly awkward near the interior. The normalized variable `Z=B/e` removes this mean term exactly because `EZ=1` for every `lambda`, giving (5.2). This is the main methodological gain of the run.

P03-B's posterior-score/continuation-energy identity remains complementary: it may be useful if the averaged contraction in (8.3) encounters a correlation term with no direct sign, but no P03-B coupling lemma was re-proved here.

---

## 10. Exact remaining gap and next attack

**New proved restricted theorem:** for every `a>sqrt(2)`, sufficiently small symmetric mean-preserving `{1,2,3}` perturbations have strictly decreasing speed on the whole interval `[a,2)`, with a uniform positive fine-secant margin after shrinking the perturbation size.

**Still not proved:**

1. the same family for `1/2<lambda<=sqrt(2)`;
2. non-small three-point perturbations;
3. arbitrary no-leaf offspring laws;
4. the full LPP conjecture.

**Next attack:** prove the averaged contraction (8.3) by splitting according to `|Y-2|+|Y'-2|<=rho`, choosing `rho=epsilon^alpha`, using the exact derivative near `Y=2` on the good event and the fourth-moment bound to charge the bad event. If the correlation with `(Y-Y')^2` prevents an `L^2` closure, switch the difference norm to an `L^p` / ideal-metric interpolation with `p>2` supplied by bounded offspring. The objective is to lower the left endpoint from `sqrt(2)` to `1`, not to repeat terminal analysis.

The fixed full-source metric is unchanged:

`R_full: 1 -> 1`.
