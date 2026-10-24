Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. GPT-6 / maximum reasoning was requested as a preference, but no authenticated runtime model-effort selector or guaranteed full-hour execution is exposed here, so I do not claim it.

# P03-A analytic proof report — mean-preserving three-point escape concentration and mesoscopic interior ordering

**Status:** PROVED PARTIAL / NEW GLOBAL ESCAPE-PROFILE LEMMA + NEW INTERIOR SECANT ORDERING FOR A GENUINELY THREE-POINT OFFSPRING FAMILY. Not independently audited. This is not the full Lyons–Pemantle–Peres conjecture.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursion / derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Canonical ownership was checked on assignment and is unchanged. P03-B retains regeneration/coupling/spine work; I used its latest escape-spine report only for continuity and do not duplicate its quenched descendant-skeleton argument. Old D0047 history is untouched.

**Inherited analytic checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1539Z__finite-variance-terminal-monotonicity-via-zolotarev-secants.md`.

That report gives a candidate whole terminal interval under only finite offspring variance. The present run deliberately leaves the critical-edge method and attacks the interior for a nontrivial three-point family by perturbing the deterministic binary tree in a mean-preserving direction.

The fixed full-source metric remains

`R_full: 1 -> 1`.

The genuine intermediate obligation moves from “only terminal control for minimum-offspring-one laws” to “fine-secants only”: for the family below, all escape probabilities are now globally `L^2`-close to the regular-tree value at every transient bias, and all sufficiently separated interior pairs above `1+kappa` are rigorously ordered. What remains is a derivative/fine-secant estimate at separation `O(epsilon)` or smaller.

---

## 1. Bias convention and corrected source frontier

At a non-root vertex with `k` children I use the original parent-bias convention

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\tag{1.1}
\]

Thus larger `lambda` means weaker outward bias. If `m=E nu`, the transient interval is `0<=lambda<m`, and the LPP conjecture asks that the speed `ell_lambda` be nonincreasing on the whole interval.

Primary historical partial source: G. Ben Arous, A. Fribergh and V. Sidoravicius, *Lyons–Pemantle–Peres monotonicity problem for high biases*, Comm. Pure Appl. Math. 67 (2014), 519–530, arXiv:1111.5865. In outward-bias notation their theorem is a large-bias theorem; it is not the current frontier.

A source correction worth recording explicitly: the later Song–Wang–Xiang paper (arXiv:1610.08151; published J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`) records Aidekon's improvement to **all no-leaf offspring laws for `lambda<=1/2`**, not only the `m_1>=2` regime. For minimum offspring `m_1>=2`, Song–Wang–Xiang prove the stronger interval

\[
0\le\lambda\le
\frac{m_1}{1+\sqrt{1-1/m_1}}.
\tag{1.2}
\]

Their paper also writes Aidekon's exact speed formula used below. Bowditch–Tokushige, arXiv:1906.07913 (ALEA 17 (2020), 609–642), prove differentiability in the CLT regime, and arXiv:2006.03433 proves analyticity in the ballistic regime; neither supplies the missing derivative sign. The Ben Arous–Hu–Olla–Zeitouni Einstein relation (Ann. IHP 49 (2013), 698–721) gives critical linear response under stronger hypotheses including an exponential offspring moment. A bounded current search on 20 September 2026 did not surface a source-wide resolution. This is negative evidence only, not a novelty certificate.

Useful source links:

- https://arxiv.org/abs/1111.5865
- https://arxiv.org/abs/1610.08151
- https://doi.org/10.1017/jpr.2024.113
- https://arxiv.org/abs/1906.07913
- https://arxiv.org/abs/2006.03433
- https://arxiv.org/abs/1111.4313

---

## 2. The mean-preserving three-point family

Fix

\[
\boxed{
P_\varepsilon(\nu=1)=\frac\varepsilon2,
\qquad
P_\varepsilon(\nu=2)=1-\varepsilon,
\qquad
P_\varepsilon(\nu=3)=\frac\varepsilon2,
}
\tag{2.1}
\]

with `0<=epsilon<1`. This is genuinely three-point for `epsilon>0`, has no leaves, and preserves the mean exactly:

\[
E\nu=2,
\qquad
\operatorname{Var}(\nu)=\varepsilon.
\tag{2.2}
\]

At `epsilon=0` the tree is deterministic binary and

\[
\ell_0(\lambda)=\frac{2-\lambda}{2+\lambda},
\qquad
0\le\lambda<2.
\tag{2.3}
\]

The point of (2.1) is that it isolates offspring heterogeneity while keeping the critical parameter exactly fixed at `m=2`. The first theorem below is uniform over the **entire** transient interval and does not use a terminal expansion.

---

## 3. Global `L^2` concentration of the escape profile

Let `B=B_{lambda,epsilon}` be the quenched escape probability from the root of a fresh Galton–Watson descendant tree to never hit its artificial parent. With iid copies `B_i`,

\[
B\stackrel d=
\frac{S}{\lambda+S},
\qquad
S:=\sum_{i=1}^{\nu}B_i.
\tag{3.1}
\]

Write

\[
b:=1-\frac\lambda2=\frac{2-\lambda}{2},
\qquad
e:=EB,
\qquad U:=B-b,
\qquad \mu:=EU=e-b,
\qquad v:=\operatorname{Var}(B).
\tag{3.2}
\]

For the deterministic binary tree, `B=b`. Put

\[
Z:=S-2b.
\tag{3.3}
\]

### Theorem 3.1 — uniform escape-profile concentration

For every `0<=epsilon<1` and every `0<=lambda<2`,

\[
\boxed{
\frac{b}{1+\varepsilon/2}\le e\le b,
}
\tag{3.4}
\]

\[
\boxed{
0\le b-e\le \frac{\varepsilon}{2+\varepsilon}\,b,
}
\tag{3.5}
\]

and

\[
\boxed{
\operatorname{Var}(B)\le \frac\varepsilon2\,e^2
\le \frac\varepsilon2\,b^2.
}
\tag{3.6}
\]

Consequently

\[
\boxed{
E\left(\frac{B}{b}-1\right)^2
\le
\tau_\varepsilon^2
:=
\frac\varepsilon2+\left(\frac\varepsilon{2+\varepsilon}\right)^2,
\qquad 0<\lambda<2,
}
\tag{3.7}
\]

so

\[
W_2\!\left(\mathcal L(B/b),\delta_1\right)
\le \tau_\varepsilon=O(\sqrt\varepsilon)
\tag{3.8}
\]

**uniformly all the way from zero bias to the critical edge.**

### Proof

The upper bound for the mean is immediate from concavity. Since `ES=2e`,

\[
e=E\frac{S}{\lambda+S}
\le \frac{2e}{\lambda+2e}.
\tag{3.9}
\]

For `lambda<2`, transience gives `e>0`; hence `lambda+2e<=2`, i.e.

\[
e\le b.
\tag{3.10}
\]

The key algebra is exact. Since `2b=2-lambda`,

\[
\boxed{
U
=\frac{\lambda Z}{2(\lambda+S)}
=\frac{\lambda Z}{2(2+Z)}.
}
\tag{3.11}
\]

Because `lambda/(lambda+S)<=1`,

\[
|U|\le \frac{|Z|}{2}.
\tag{3.12}
\]

Now `E nu=2` and `Var(nu)=epsilon`, so the random-sum variance formula gives

\[
EZ=2\mu,
\qquad
\operatorname{Var}(Z)=2v+\varepsilon e^2.
\tag{3.13}
\]

Therefore

\[
EZ^2=2v+\varepsilon e^2+4\mu^2.
\tag{3.14}
\]

Using (3.12),

\[
v+\mu^2=EU^2
\le \frac14 EZ^2
=\frac12v+\frac\varepsilon4 e^2+\mu^2,
\]

and the mean-square term cancels exactly. Thus

\[
\boxed{v\le\frac\varepsilon2e^2.}
\tag{3.15}
\]

This cancellation is the first useful feature of the mean-preserving perturbation.

For the sharper mean deficit, let `t:=b-e=-mu>=0`. From (3.11),

\[
\mu
=\frac\lambda2 E\frac{Z}{2+Z}.
\tag{3.16}
\]

Use the exact decomposition

\[
\frac{Z}{2+Z}
=\frac Z2-\frac{Z^2}{2(2+Z)}.
\tag{3.17}
\]

Since `EZ=2mu`,

\[
\mu b
=-\frac\lambda4 E\frac{Z^2}{2+Z}.
\tag{3.18}
\]

Thus, for `lambda>0`, because `2+Z=lambda+S>=lambda`,

\[
tb
\le \frac14 EZ^2.
\tag{3.19}
\]

By (3.14) and (3.15),

\[
EZ^2
\le 2\varepsilon e^2+4t^2.
\tag{3.20}
\]

Substitution into (3.19) gives

\[
tb\le\frac\varepsilon2e^2+t^2.
\tag{3.21}
\]

But `b=e+t`, hence `tb-t^2=te`; since `e>0`,

\[
\boxed{t\le\frac\varepsilon2e.}
\tag{3.22}
\]

Equivalently `b<=e(1+epsilon/2)`, proving (3.4) and (3.5). Finally

\[
E(B-b)^2=v+t^2
\le \frac\varepsilon2b^2
+\left(\frac\varepsilon{2+\varepsilon}\right)^2b^2,
\]

which is (3.7). At `lambda=0`, `B=b=1` identically, so the endpoint is trivial. `square`

### Why this is useful

This is much stronger than the inherited terminal normalization for this special family: the relative escape profile is uniformly close to the regular value at **every** transient bias. No third moment, critical scaling, or support-tail truncation is used. The estimate is also correctly scale-free near `lambda=2`, because both `B` and `b` vanish at the same rate.

---

## 4. Exact effective-degree defect for the symmetric family

Aidekon's exact speed formula, written as in Song–Wang–Xiang, is

\[
\ell_\lambda
=
\frac{E\left[\frac{(\nu-\lambda)B_0}
{\lambda-1+\sum_{i=0}^{\nu}B_i}\right]}
{E\left[\frac{(\nu+\lambda)B_0}
{\lambda-1+\sum_{i=0}^{\nu}B_i}\right]}.
\tag{4.1}
\]

For `lambda>1`, all denominators below are positive. Define

\[
H_n(\lambda,\varepsilon)
:=E\frac{B_0}
{\lambda-1+\sum_{i=0}^{n}B_i},
\qquad n=1,2,3.
\tag{4.2}
\]

Set

\[
D:=\frac\varepsilon2H_1+(1-\varepsilon)H_2+rac\varepsilon2H_3
\tag{4.3}
\]

and the escape-tilted effective offspring mean

\[
M:=
\frac{\frac\varepsilon2H_1+2(1-\varepsilon)H_2+\frac{3\varepsilon}{2}H_3}{D}.
\tag{4.4}
\]

Then

\[
\ell_\lambda=\frac{M-\lambda}{M+\lambda}.
\tag{4.5}
\]

Because `H_1>=H_2>=H_3>0`, the symmetric mean-preserving perturbation has the exact one-line defect identity

\[
\boxed{
q:=2-M
=\frac\varepsilon2\,
\frac{H_1-H_3}{D}
\ge0.
}
\tag{4.6}
\]

This is an interior analogue of the terminal branch-vector identity, but here the symmetry of (2.1) collapses the entire tilt to the difference between only the `n=1` and `n=3` weights. In particular randomness slows the walk relative to the binary regular tree at fixed `lambda>1`:

\[
\boxed{\ell_{\lambda,\varepsilon}\le\ell_{\lambda,0}.}
\tag{4.7}
\]

---

## 5. Mesoscopic interior monotonicity

Fix `kappa in (0,1)` and restrict to

\[
1+\kappa\le\lambda<2.
\tag{5.1}
\]

Let

\[
D_1=\lambda-1+B_0+B_1,
\qquad D_2=D_1+B_2.
\]

Since `D_1>=kappa` and `0<=B_2<=1`, pointwise

\[
\frac{B_0}{D_1}
=\frac{B_0}{D_2}\frac{D_2}{D_1}
\le\left(1+\frac1\kappa\right)\frac{B_0}{D_2}.
\]

Hence

\[
\boxed{H_1\le\left(1+\frac1\kappa\right)H_2.}
\tag{5.2}
\]

Since `H_1-H_3<=H_1` and `D>=(1-epsilon)H_2`, (4.6) gives

\[
\boxed{
0\le q
\le
\frac\varepsilon{2(1-\varepsilon)}
\left(1+\frac1\kappa\right).
}
\tag{5.3}
\]

The map

\[
f_\lambda(M):=\frac{M-\lambda}{M+\lambda}
\]

is increasing in `M`, and for `M>=1`,

\[
0<\partial_M f_\lambda(M)
=\frac{2\lambda}{(M+\lambda)^2}
\le\frac1{2M}\le\frac12.
\tag{5.4}
\]

Therefore

\[
\boxed{
0\le
\ell_{\lambda,0}-\ell_{\lambda,\varepsilon}
\le
\frac\varepsilon{4(1-\varepsilon)}
\left(1+\frac1\kappa\right).
}
\tag{5.5}
\]

For the regular binary tree,

\[
\ell_{\lambda,0}=\frac{2-\lambda}{2+\lambda},
\qquad
-\ell'_{\lambda,0}
=\frac4{(2+\lambda)^2}\ge\frac14.
\tag{5.6}
\]

Thus for `1+kappa<=lambda_1<lambda_2<2`, combining (4.7), (5.5), and (5.6),

\[
\boxed{
\ell_{\lambda_1,\varepsilon}
-
\ell_{\lambda_2,\varepsilon}
\ge
\frac{\lambda_2-\lambda_1}{4}
-
\frac\varepsilon{4(1-\varepsilon)}
\left(1+\frac1\kappa\right).
}
\tag{5.7}
\]

Hence:

### Theorem 5.1 — mesoscopic interior ordering

For the three-point law (2.1), every pair satisfying

\[
1+\kappa\le\lambda_1<\lambda_2<2
\]

and

\[
\boxed{
\lambda_2-\lambda_1
>
\frac\varepsilon{1-\varepsilon}
\left(1+\frac1\kappa\right)
}
\tag{5.8}
\]

obeys

\[
\boxed{
\ell_{\lambda_1,\varepsilon}
>
\ell_{\lambda_2,\varepsilon}.
}
\tag{5.9}
\]

This is not yet a monotonicity interval because arbitrarily fine secants are not covered. It is nevertheless a new interior ordering result: at fixed `kappa`, the only potentially dangerous reversals have width `O(epsilon)` as `epsilon downarrow0`.

For example, with `kappa=1/10` and `epsilon=10^{-4}`, every pair in `[1.1,2)` separated by more than about `1.10011 x 10^{-3}` is rigorously ordered in the conjectured direction. Fine local behavior remains the only issue.

---

## 6. First-order offspring-heterogeneity expansion on the interior

The global escape concentration sharpens (5.3) into an actual first-order perturbation formula.

For `n=1,2,3`, put

\[
d_n:=\lambda-1+(n+1)b.
\tag{6.1}
\]

Thus

\[
d_1=1,
\qquad d_2=1+b,
\qquad d_3=1+2b.
\tag{6.2}
\]

Using `D_n>=kappa`, `d_n>=1`, and (3.7),

\[
\begin{aligned}
\left|H_n-\frac b{d_n}\right|
&\le
E\frac{|B_0-b|}{D_n}
+bE\frac{|D_n-d_n|}{D_nd_n}\\
&\le
\frac{b\tau_\varepsilon}{\kappa}
+
\frac{(n+1)b^2\tau_\varepsilon}{\kappa d_n}.
\end{aligned}
\tag{6.3}
\]

Since `(n+1)b<=2` for `n<=3`,

\[
\boxed{
\left|\frac{H_n}{b}-\frac1{d_n}\right|
\le \frac{3\tau_\varepsilon}{\kappa}.
}
\tag{6.4}
\]

Let

\[
r:=\frac{3\tau_\varepsilon}{\kappa}.
\tag{6.5}
\]

If `epsilon<=1/2` and `r<=1/6`, the denominator in (4.6), after division by `b`, is at least `1/4`. Elementary Lipschitz control of the rational map

\[
(A_1,A_2,A_3,\varepsilon)
\mapsto
\frac12
\frac{A_1-A_3}
{\frac\varepsilon2A_1+(1-\varepsilon)A_2+\frac\varepsilon2A_3}
\]

on this box yields the safe explicit estimate

\[
\boxed{
\left|
\frac q\varepsilon
-
\frac{b(1+b)}{1+2b}
\right|
\le
100\left(r+\varepsilon\right).
}
\tag{6.6}
\]

(The constant 100 is deliberately crude: on the stated box the sum of the three coordinate Lipschitz constants is `<33` and the epsilon derivative is `<44`.)

Thus, for every fixed `kappa>0`, uniformly on `1+kappa<=lambda<2`,

\[
\boxed{
q
=
\varepsilon\frac{b(1+b)}{1+2b}
+O_\kappa(\varepsilon^{3/2}).
}
\tag{6.7}
\]

Substituting in (4.5),

\[
\boxed{
\ell_{\lambda,\varepsilon}
=
\frac{2-\lambda}{2+\lambda}
-
\varepsilon\,
\frac{\lambda(2-\lambda)(4-\lambda)}
{2(2+\lambda)^2(3-\lambda)}
+O_\kappa(\varepsilon^{3/2}).
}
\tag{6.8}
\]

So the Gateaux derivative of the speed in this mean-preserving offspring direction is explicit for every fixed `lambda>1`:

\[
\boxed{
\left.\partial_\varepsilon
\ell_{\lambda,\varepsilon}\right|_{\varepsilon=0}
=
-
\frac{\lambda(2-\lambda)(4-\lambda)}
{2(2+\lambda)^2(3-\lambda)}.
}
\tag{6.9}
\]

The coefficient is positive before the minus sign: infinitesimal symmetric offspring heterogeneity lowers the speed, as expected from Aidekon's effective-degree picture.

A direct calculus check gives, on `1<=lambda<2`, if

\[
c(\lambda):=
\frac{\lambda(2-\lambda)(4-\lambda)}
{2(2+\lambda)^2(3-\lambda)},
\]

then

\[
c'(\lambda)
=-\frac{7\lambda^3-46\lambda^2+96\lambda-48}
{2(\lambda-3)^2(\lambda+2)^3}<0,
\tag{6.10}
\]

with endpoint values `c'(1)=-1/24` and `c'(2-)=-1/8`. Thus the first-order heterogeneity correction weakens the regular-tree negative derivative by only `O(epsilon)`; it does not suggest an interior sign reversal.

---

## 7. What this proves, and what it does not

### New proved mathematical content

For the nondegenerate three-point family (2.1):

1. `B/b` is uniformly `L^2`-close to `1` over the **whole transient interval** with explicit error `O(sqrt(epsilon))`; see (3.7).
2. For every `kappa>0`, all interior speed comparisons in `[1+kappa,2)` at separation larger than the explicit `O(epsilon)` scale (5.8) have the conjectured strict sign.
3. The effective-degree defect has the explicit first-order expansion (6.7), and the speed has the uniform value expansion (6.8).
4. The first offspring-heterogeneity derivative of speed at the binary regular law is explicit, (6.9), and its lambda-profile is benign.

These statements are exact restricted progress. They do **not** imply that `lambda -> ell_{lambda,epsilon}` is monotone on the whole interval for any fixed `epsilon>0`, because a value error `O(epsilon^{3/2})` cannot be differentiated or divided by an arbitrarily small `lambda` increment.

### Relation to existing certified regions

For any `epsilon>0`, minimum offspring is one. The checked source-wide low-bias certificate is therefore the universal Aidekon range through `lambda=1/2`; the stronger Song–Wang–Xiang `m_1>=2` endpoint does not apply. The inherited P03-A finite-variance terminal theorem candidate covers a law-dependent neighborhood of `lambda=2`. The present report attacks the genuinely unresolved interior between those regimes, especially `lambda>1`, and reduces possible reversals for small `epsilon` to a fine-secant phenomenon.

---

## 8. Exact remaining gap and next analytic attack

The next useful statement is now sharply isolated. It is enough, for each fixed `kappa>0`, to upgrade (6.8) from a value remainder to a **secant remainder**

\[
R_\varepsilon(\lambda_2)-R_\varepsilon(\lambda_1)
=
O_\kappa(\varepsilon^{3/2})
(\lambda_2-\lambda_1),
\tag{8.1}
\]

or equivalently a `C^1` bound

\[
\sup_{1+\kappa\le\lambda\le 2-\eta}
|\partial_\lambda R_\varepsilon(\lambda)|
=O_{\kappa,\eta}(\varepsilon^{3/2}).
\tag{8.2}
\]

The first-order derivative margin is generous: the regular-tree slope has magnitude at least `1/4`, while the first-order correction changes it by at most `epsilon/8` on `[1,2)`. Therefore any genuine `C^1` perturbation estimate of order `o(1)` closes monotonicity on compact interior subintervals for sufficiently small `epsilon`.

The natural analytic variable is

\[
K:=\partial_\lambda B+\frac12.
\]

Differentiating the exact mean-preserving recursion (3.11), with

\[
Z=b(\nu-2)+\sum_i(B_i-b),
\]

gives

\[
K
=
\frac{Z}{2(2+Z)}
+
\frac{\lambda}{(2+Z)^2}
\left[-\frac12(\nu-2)+\sum_iK_i\right].
\tag{8.3}
\]

The already-proved estimate `Z=O_{L^2}(b sqrt(epsilon))` makes every inhomogeneous term small. On any compact interval bounded away from `lambda=2`, the mean mode of the linearized operator has factor `lambda/2<1`. The next run should separate the mean and centered parts of `K`, prove an `L^2` bound `EK^2=O_{kappa,eta}(epsilon)`, and feed that into the derivatives of `H_1,H_2,H_3`. That is the direct route to (8.2) and an actual new interior monotonicity interval for a genuinely random three-point offspring law.

A second, complementary possibility is to combine the derivative recursion (8.3) with P03-B's escape-spine elasticity representation to control the rare long unary-pipe histories rather than bounding them degreewise. P03-B owns that coupling implementation; this slot should use only any resulting valid aggregate lemma.

No handoff is triggered: this run changed the mathematical state substantially and exposed a narrower fine-secant obstruction.
