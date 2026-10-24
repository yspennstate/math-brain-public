Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. GPT-6 / maximum reasoning was requested as a preference, but no authenticated runtime model-effort selector or guaranteed full-hour execution is exposed here, so I do not claim it.

# P03-A analytic proof report — full transient-interval monotonicity for a small symmetric three-point perturbation

**Status:** PROVED PARTIAL / CANDIDATE COMPLETE MONOTONICITY THEOREM FOR A GENUINELY RANDOM RESTRICTED OFFSPRING FAMILY. Not independently audited. No claim of external novelty. This is **not** a proof of the full Lyons–Pemantle–Peres conjecture.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursion / derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Canonical ownership was checked on assignment and remains unchanged. P03-B retains coupling/regeneration/escape-spine ownership. I use none of its current coupling proofs below. Old D0047 history is untouched.

**Captured `master` immediately before this write:** `0c7bd3cf21a1d8b37ec11f6fa07e00a247dfca02`.

**Inherited analytic checkpoints:**

- `2026-09-20T1559Z__mean-preserving-three-point-profile-and-mesoscopic-interior-order.md` proves uniform relative `L^2` concentration of the escape probability for the symmetric `{1,2,3}` perturbation and the exact one-coordinate Aïdékon degree defect.
- `2026-09-20T1700Z__fine-secant-monotonicity-above-sqrt2-for-small-three-point-perturbations.md` proves full fine-secant monotonicity on `[a,2)` for every fixed `a>sqrt(2)`, when the perturbation is sufficiently small.

The unresolved obligation was the interior band between the published source-wide low-bias theorem and the inherited `a>sqrt(2)` theorem. This run closes that band for sufficiently small symmetric perturbations by a different contraction: a monotone same-tree coupling plus an **independent sibling denominator**. It avoids the `sqrt(2)` barrier entirely on compact subintervals of `(0,2)`.

The fixed full-source metric remains

`R_full: 1 -> 1`.

The restricted-family obligation changes from “fine monotonicity only above `sqrt(2)`” to **“the whole transient interval is covered for this nontrivial family when epsilon is small.”**

---

## 1. Source convention, exact family, and current frontier

At a non-root vertex with `k` children I use the parent/inward-bias convention

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\tag{1.1}
\]

Thus increasing `lambda` weakens the outward drift. The source LPP problem asks whether the speed `ell_lambda` is nonincreasing on the transient interval `0<=lambda<m` for every supercritical Galton–Watson offspring law with no leaves.

Primary historical partial source: Ben Arous–Fribergh–Sidoravicius, arXiv:1111.5865 / CPAM 67 (2014). Aïdékon’s speed formula is arXiv:1111.4313 / PTRF 159 (2014). Song–Wang–Xiang, arXiv:1610.08151 and J. Appl. Probab. 62 (2025), 1044–1052, record Aïdékon’s no-leaf monotonicity result through `lambda<=1/2`, and prove the stronger interval

\[
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}
\tag{1.2}
\]

when the minimum offspring is `d>=2`. Their paper also records Aïdékon’s exact speed representation for no-leaf trees for `lambda<m`. Bowditch–Tokushige, arXiv:1906.07913 and arXiv:2006.03433, provide differentiability/analyticity in ballistic regimes but do not supply the missing sign.

The family in this report is

\[
\boxed{
P_\varepsilon(\nu=1)=\frac\varepsilon2,\qquad
P_\varepsilon(\nu=2)=1-\varepsilon,\qquad
P_\varepsilon(\nu=3)=\frac\varepsilon2,
}
\tag{1.3}
\]

with `0<epsilon<1`. It is genuinely random, has no leaves, and preserves

\[
E\nu=2,\qquad \operatorname{Var}(\nu)=\varepsilon.
\tag{1.4}
\]

Its minimum offspring is one, so the `d>=2` extension (1.2) does not apply. The source-wide published interval relevant to this family is therefore the interval through `1/2`; the remainder `(1/2,2)` is the genuine target attacked here together with the inherited P03-A terminal theorem.

---

## 2. Escape recursion and inherited global concentration

Let `B_lambda` be the quenched probability, from the root of a fresh descendant tree with an artificial parent, of never hitting that parent. With iid copies `B_{lambda,i}`,

\[
B_\lambda\stackrel d=\frac{S_\lambda}{\lambda+S_\lambda},
\qquad
S_\lambda:=\sum_{i=1}^{\nu}B_{\lambda,i}.
\tag{2.1}
\]

Couple all biases on the same Galton–Watson tree. Then

\[
\lambda<\lambda'\quad\Longrightarrow\quad
B_\lambda\ge B_{\lambda'}\quad\text{a.s.}
\tag{2.2}
\]

Write

\[
b_\lambda:=\frac{2-\lambda}{2},
\qquad e_\lambda:=EB_\lambda.
\tag{2.3}
\]

The inherited `1559Z` theorem gives simultaneously for all `0<=lambda<2`

\[
\frac{b_\lambda}{1+\varepsilon/2}\le e_\lambda\le b_\lambda,
\qquad
\operatorname{Var}(B_\lambda)\le\frac\varepsilon2e_\lambda^2,
\tag{2.4}
\]

and

\[
E\left(\frac{B_\lambda}{b_\lambda}-1\right)^2
\le
\tau_\varepsilon^2,
\qquad
\tau_\varepsilon^2:=
\frac\varepsilon2+\left(\frac{\varepsilon}{2+\varepsilon}\right)^2.
\tag{2.5}
\]

In particular,

\[
E|B_\lambda-b_\lambda|\le b_\lambda\tau_\varepsilon\le\tau_\varepsilon.
\tag{2.6}
\]

This global scale-free concentration is the perturbative input below.

---

## 3. Two denominator lemmas that remove the apparent singularity at lambda=1

### Lemma 3.1 — no-leaf escape floor

For every deterministic no-leaf rooted tree and every `0<=lambda<=1`,

\[
\boxed{B_\lambda\ge1-\lambda.}
\tag{3.1}
\]

#### Proof

Let `B^{(N)}` be the probability of reaching descendant level `N` before the artificial parent, with boundary value one at level `N`. If all child values at a vertex are at least `1-lambda`, then, because there is at least one child,

\[
S\ge1-\lambda
\quad\Longrightarrow\quad
\frac{S}{\lambda+S}\ge
\frac{1-\lambda}{\lambda+1-\lambda}=1-\lambda.
\]

Backward induction gives the same lower bound at every finite depth. Letting `N` increase gives (3.1). `square`

This is the minimum-offspring-one specialization of the escape lower bounds used in the published low-bias argument; it is rederived here because it gives exactly the denominator control needed below.

### Lemma 3.2 — every Aïdékon denominator dominates every displayed escape coordinate

For `n>=1`, put

\[
D_n(\lambda):=
\lambda-1+\sum_{i=0}^{n}B_{\lambda,i}.
\tag{3.2}
\]

Then for every `0<lambda<2`, every `n>=1`, and every `j in {0,...,n}`,

\[
\boxed{D_n(\lambda)\ge B_{\lambda,j}>0.}
\tag{3.3}
\]

#### Proof

If `lambda>=1`, this is immediate. If `lambda<1`, choose `k!=j`, which is possible because `n>=1`. Lemma 3.1 gives `B_{lambda,k}>=1-lambda`, hence

\[
\lambda-1+B_{\lambda,k}\ge0,
\]

and the remaining nonnegative summands include `B_{lambda,j}`. `square`

The importance of (3.3) is that all inverse-denominator estimates below pass smoothly through `lambda=1`; no artificial split into `<1` and `>1` regions is needed.

---

## 4. A uniform inverse-escape first moment on compact lambda intervals

The fine-secant estimates for Aïdékon’s weights require an integrable inverse escape probability. For the present family this follows from the recursion without any high moment assumption.

### Lemma 4.1 — compact inverse moment

Fix `c<2`. If `epsilon` is small enough that

\[
\theta:=\frac{c(1+\varepsilon/2)}2<1,
\tag{4.1}
\]

then uniformly for `0<lambda<=c`,

\[
\boxed{
E\frac1{B_\lambda}
\le r_*:=\frac1{1-\theta}.
}
\tag{4.2}
\]

#### Proof

Write `R=1/B`. From (2.1),

\[
R=1+\frac\lambda S.
\tag{4.3}
\]

If `nu=1`, then `1/S=R_1`. If `nu>=2`,

\[
\frac1S\le\frac1{B_1+B_2}
=\frac{R_1R_2}{R_1+R_2}
\le\frac{R_1+R_2}{4}.
\tag{4.4}
\]

For `r=ER`, using `P(nu=1)=epsilon/2`,

\[
r
\le1+\lambda\left[
\frac\varepsilon2 r+\left(1-\frac\varepsilon2\right)\frac r2
\right]
=1+\frac{\lambda(1+\varepsilon/2)}2r
\le1+\theta r.
\tag{4.5}
\]

To avoid presupposing integrability, apply (4.5) first to finite-depth escape variables with terminal value one. Their inverse moments are bounded uniformly by `(1-theta)^{-1}`; monotone convergence in depth then yields (4.2). `square`

This inverse-moment bound is one of the two new analytic inputs of the run.

---

## 5. New sibling-decoupling contraction for the mean escape probability

The preceding `1700Z` report compared normalized laws in `W_2` and paid the worst-case factor `sqrt(2)/lambda`, creating the artificial threshold `lambda>sqrt(2)`. The present argument does not compare full normalized laws. It couples the two escape fields on the **same tree**, then charges each child difference against an independent sibling in the denominator.

Fix once and for all

\[
0<a<c<2.
\tag{5.1}
\]

Choose `h>0` so small that `h<2-c` and

\[
\boxed{
r_0:=\frac{8c}{(c+2-h)^2}<1.}
\tag{5.2}
\]

Such an `h` exists because

\[
\frac{8c}{(c+2)^2}<1
\iff(c-2)^2>0.
\]

Take

\[
a\le\lambda<\lambda'\le c,
\qquad
\Delta:=\lambda'-\lambda\le h.
\tag{5.3}
\]

Under the same-tree coupling define

\[
\delta_i:=B_{\lambda,i}-B_{\lambda',i}\ge0,
\qquad
d:=e_\lambda-e_{\lambda'}=E\delta_i\ge0.
\tag{5.4}
\]

For `f_lambda(s)=s/(lambda+s)`, the exact difference is

\[
f_\lambda(S)-f_{\lambda'}(S')
=
\frac{\lambda(S-S')}{(\lambda+S)(\lambda+S')}
+
\frac{\Delta S'}{(\lambda+S')(\lambda'+S')}.
\tag{5.5}
\]

The second term is at most `Delta/(4lambda)<=Delta/(4a)`.

For the first term, if `nu=1`, its coefficient is at most `1/lambda<=1/a`. If `nu>=2`, then for the term containing a particular `delta_i`, choose any sibling `j!=i`. Since `S'>=B_{lambda',j}`,

\[
\frac{\lambda}{(\lambda+S)(\lambda+S')}
\le
\frac{\lambda}{(\lambda+B_{\lambda',j})^2}.
\tag{5.6}
\]

The selected sibling is independent of `delta_i`. Therefore, with

\[
\alpha:=E\frac{\lambda}{(\lambda+B_{\lambda'})^2},
\tag{5.7}
\]

averaging (5.5) gives

\[
\boxed{
d\le\frac\Delta{4a}+\rho d,}
\qquad
\rho:=\frac{\varepsilon}{2a}
+\left(2-\frac\varepsilon2\right)\alpha.
\tag{5.8}
\]

Now `x -> lambda/(lambda+x)^2` has derivative bounded by `2/a^2`. By (2.6),

\[
\alpha
\le
\frac{\lambda}{(\lambda+b_{\lambda'})^2}
+\frac{2}{a^2}\tau_\varepsilon.
\tag{5.9}
\]

Because `lambda'=lambda+Delta`,

\[
\frac{\lambda}{(\lambda+b_{\lambda'})^2}
=
\frac{4\lambda}{(\lambda+2-\Delta)^2}
\le
\frac{4c}{(c+2-h)^2}.
\tag{5.10}
\]

Hence

\[
\boxed{
\rho
\le
\frac\varepsilon{2a}
+rac{8c}{(c+2-h)^2}
+rac{4}{a^2}\tau_\varepsilon.
}
\tag{5.11}
\]

Since `tau_epsilon ->0` and the middle term is strictly below one by (5.2), there is `epsilon_0(a,c,h)>0` such that `rho<1` for all `epsilon<=epsilon_0`. Equation (5.8) then yields the genuine local fine-secant estimate

\[
\boxed{
0\le e_\lambda-e_{\lambda'}
\le L_e(\lambda'-\lambda),
\qquad
L_e:=\frac1{4a(1-\rho)}.
}
\tag{5.12}
\]

This is the main new contraction of the run. It has no `sqrt(2)` threshold. The strict margin comes from the deterministic sibling denominator, while perturbative concentration only controls the deviation of that sibling from the regular-tree escape value.

For orientation, on `[a,c]=[1/2,3/2]` one may take `h=10^{-3}`; then the epsilon-free core of (5.11) is

\[
\frac{12}{3.499^2}\approx0.9801518435<1.
\tag{5.13}
\]

No numerical epsilon threshold is optimized below.

---

## 6. Fine secants for all three Aïdékon weights

For `n=1,2,3`, define

\[
H_n(\lambda)
:=E\frac{B_{\lambda,0}}{D_n(\lambda)},
\qquad
D_n(\lambda)=\lambda-1+\sum_{i=0}^nB_{\lambda,i}.
\tag{6.1}
\]

### Lemma 6.1 — compact Lipschitz control of `H_1,H_2,H_3`

Under the assumptions of Section 5 and (4.1),

\[
\boxed{
|H_n(\lambda)-H_n(\lambda')|
\le L_H(\lambda'-\lambda),
\qquad n=1,2,3,
}
\tag{6.2}
\]

where one may take

\[
L_H:=r_*(1+5L_e).
\tag{6.3}
\]

#### Proof

Let `D=D_n(lambda)` and `D'=D_n(lambda')`. Then

\[
|D'-D|\le\Delta+\sum_{i=0}^n\delta_i.
\tag{6.4}
\]

Also, by Lemma 3.2, every `D` and `D'` dominates every displayed escape coordinate at the same parameter. Therefore

\[
\left|\frac{B_0}{D}-\frac{B_0'}{D'}\right|
\le
\frac{\delta_0}{D}
+rac{B_0'|D'-D|}{DD'}.
\tag{6.5}
\]

The first term is bounded by `delta_0/B_1`; independence and Lemma 4.1 give expectation at most `d r_*`.

For the explicit `Delta` in (6.4), use `B_0'<=B_0<=D` and `D'>=B_1'` to obtain expectation at most `Delta r_*`.

For the `i=0` term in the sum, use `B_0'<=D'`, giving `delta_0/D<=delta_0/B_1` and cost at most `d r_*`. For every `i>=1`, use `B_0'<=D`, then `D'>=B_0'`, giving

\[
\frac{B_0'\delta_i}{DD'}\le\frac{\delta_i}{D'}\le\frac{\delta_i}{B_0'}.
\]

Here `delta_i` is independent of `B_0'`, so each such term again costs at most `d r_*`. Consequently

\[
|H_n(\lambda)-H_n(\lambda')|
\le r_*[\Delta+(n+2)d]
\le r_*(1+5L_e)\Delta,
\]

because `n<=3`. `square`

---

## 7. The exact degree defect is now locally Lipschitz with an epsilon prefactor

Aïdékon’s speed representation, specialized to (1.3), gives

\[
\ell_\lambda=\frac{M_\lambda-\lambda}{M_\lambda+\lambda},
\tag{7.1}
\]

with

\[
M_\lambda=
\frac{\frac\varepsilon2H_1+2(1-\varepsilon)H_2+rac{3\varepsilon}{2}H_3}
{\frac\varepsilon2H_1+(1-\varepsilon)H_2+rac\varepsilon2H_3}.
\tag{7.2}
\]

Put

\[
K_\lambda:=
\frac\varepsilon2H_1+(1-\varepsilon)H_2+rac\varepsilon2H_3,
\qquad
q_\lambda:=2-M_\lambda.
\tag{7.3}
\]

The inherited exact cancellation is

\[
\boxed{
q_\lambda
=\frac\varepsilon2
\frac{H_1-H_3}{K_\lambda}\ge0.
}
\tag{7.4}
\]

We now make its secants uniform on `[a,c]`.

First, by Lemma 3.2, `0<H_n<=1`. If `epsilon<=1/2`, then

\[
H_2
\ge\frac{e_\lambda}{c+2}
\ge
\frac{b_c}{(1+\varepsilon/2)(c+2)},
\qquad b_c=\frac{2-c}{2}.
\tag{7.5}
\]

Thus the convenient uniform lower bound

\[
\boxed{
K_\lambda\ge K_*:=\frac{2-c}{6(c+2)}>0
}
\tag{7.6}
\]

holds for `epsilon<=1/2`.

Set `N_lambda=H_1-H_3`. Then `0<=N_lambda<=1`, and Lemma 6.1 gives

\[
|N_\lambda-N_{\lambda'}|\le2L_H\Delta,
\qquad
|K_\lambda-K_{\lambda'}|\le L_H\Delta.
\tag{7.7}
\]

Therefore

\[
\left|
\frac{N_\lambda}{K_\lambda}
-
\frac{N_{\lambda'}}{K_{\lambda'}}
\right|
\le L_R\Delta,
\tag{7.8}
\]

where

\[
\boxed{
L_R:=\frac{2L_H}{K_*}+\frac{L_H}{K_*^2}.
}
\tag{7.9}
\]

Combining with (7.4),

\[
\boxed{
0\le q_\lambda\le\frac\varepsilon{2K_*},
\qquad
|q_\lambda-q_{\lambda'}|
\le\frac\varepsilon2L_R\Delta.
}
\tag{7.10}
\]

The crucial point is the explicit **epsilon prefactor** in the derivative-scale control of the environment tilt.

---

## 8. New compact-interior monotonicity theorem

### Theorem 8.1 — every fixed compact subinterval of `(0,2)` is monotone for small epsilon

Fix

\[
0<a<c<2.
\]

There exists `epsilon_{a,c}>0` such that, for every `0<epsilon<=epsilon_{a,c}`, the speed of the offspring law (1.3) is strictly decreasing on `[a,c]`.

#### Proof

Choose `h` by (5.2), and then choose epsilon small enough that all bounds in Sections 4–7 hold. Shrink it further so that

\[
q_\lambda\le\frac12
\tag{8.1}
\]

and

\[
\frac32-\frac{c\varepsilon L_R}{2}>0.
\tag{8.2}
\]

Take a local pair `lambda<lambda'<=lambda+h` in `[a,c]`, with `Delta=lambda'-lambda`. Since `M_lambda=2-q_lambda>=3/2`, exact cross multiplication in (7.1) gives

\[
\ell_\lambda-\ell_{\lambda'}
=
\frac{2(M_\lambda\lambda'-M_{\lambda'}\lambda)}
{(M_\lambda+\lambda)(M_{\lambda'}+\lambda')}.
\tag{8.3}
\]

The numerator bracket satisfies

\[
\begin{aligned}
M_\lambda\lambda'-M_{\lambda'}\lambda
&=M_\lambda\Delta
+\lambda(q_{\lambda'}-q_\lambda)\\
&\ge
\left(\frac32-rac{c\varepsilon L_R}{2}\right)\Delta
>0.
\end{aligned}
\tag{8.4}
\]

Hence every local secant of length at most `h` has the desired strict sign. Any pair in `[a,c]` can be partitioned into finitely many such local steps, so strict monotonicity holds on the whole compact interval. `square`

### Why this is genuinely different from `1700Z`

The old normalized-`W_2` law comparison contracted only when the worst-case coefficient `sqrt(2)/lambda<1`, hence `lambda>sqrt(2)`. The new proof never asks the whole child-sum map to be globally contractive in `W_2`. It uses monotonicity in the parameter to make child increments nonnegative and then pays each increment against an independent sibling. The regular-tree sibling response has factor

\[
\frac{8\lambda}{(\lambda+2)^2}<1
\qquad(0<\lambda<2),
\]

which is strictly contractive throughout every compact subset of the whole transient interval. This removes the previous interior threshold.

---

## 9. Restricted-family full-interval theorem

We can now patch three rigorously distinct intervals.

1. **Published/source interval.** Aïdékon’s result, as recorded in Song–Wang–Xiang, gives strict decrease for every no-leaf offspring law on `0<=lambda<=1/2`.

2. **New compact-interior interval.** Apply Theorem 8.1 with

\[
[a,c]=\left[\frac12,\frac32\right].
\]

Then there is `epsilon_mid>0` such that strict decrease holds throughout `[1/2,3/2]` for `epsilon<=epsilon_mid`.

3. **Inherited terminal interval.** Since `3/2>sqrt(2)`, the `1700Z` P03-A theorem gives `epsilon_top>0` such that strict decrease holds throughout `[3/2,2)` for `epsilon<=epsilon_top`.

Taking

\[
\varepsilon_*:=\min\{\varepsilon_{\rm mid},\varepsilon_{\rm top}\}>0
\tag{9.1}
\]

gives the main conclusion.

### Theorem 9.1 — candidate complete monotonicity for a genuinely random three-point family

There exists `epsilon_*>0` such that for every

\[
0<\varepsilon\le\varepsilon_*,
\]

the Galton–Watson offspring law

\[
P(\nu=1)=P(\nu=3)=\frac\varepsilon2,
\qquad P(\nu=2)=1-\varepsilon
\]

has **strictly decreasing parent-bias speed on its entire transient interval**

\[
\boxed{0\le\lambda<2.}
\tag{9.2}
\]

Equivalently, in the original outward-bias variable `beta=1/lambda`, the speed is strictly increasing throughout the corresponding outward-bias transient range.

This is a full-interval result for one nontrivial perturbative offspring family, **not** a full-source solution. It removes all previously uncaptured lambda-gaps for this family.

---

## 10. Self-checks and exact scope

1. The denominator inequality (3.3) was checked separately on both sides of `lambda=1`; this is the place where a naive bound by `lambda-1` would fail.
2. The sibling factorization in (5.6) uses `j!=i`; `delta_i` is measurable from child subtree `i`, while `B_{lambda',j}` comes from an independent sibling subtree. No same-child independence is assumed.
3. The random-sum coefficient in (5.8) is exact for (1.3):
   \[
   P(\nu=1)=\varepsilon/2,
   \qquad E[\nu\mathbf 1_{\{\nu\ge2\}}]=2-\varepsilon/2.
   \]
4. The compact contraction is genuinely strict because `8c/(c+2)^2<1` for every `c<2`; the loss from `h>0` and `tau_epsilon` can therefore be absorbed by choosing them small in that order.
5. Theorem 8.1 is only perturbative in the offspring law. Its constants deteriorate as `c` tends to `2`, which is why the inherited critical-edge theorem is still required for the global patch.
6. The full-source metric stays unchanged: proving (9.2) for the one-parameter family (1.3) does not settle arbitrary no-leaf offspring laws.

No independent audit has yet checked every line of this candidate theorem. Under the owner directive, that does not freeze research, but the status remains PROVED PARTIAL rather than a claim of established literature.

---

## 11. Remaining gap and next analytic attack

The strongest new obligation is no longer a lambda-interval gap for the symmetric near-binary family. It is an **offspring-law gap**:

- remove the small-`epsilon` restriction along the whole symmetric `{1,2,3}` line;
- then perturb away from the exact symmetry `p_1=p_3` to an open two-dimensional region of the `{1,2,3}` simplex;
- ultimately replace the bounded-support sibling bound by an aggregate finite-variance version.

The next attack should retain the sibling-decoupling mechanism rather than return to the old worst-case `W_2` contraction. For general `{1,2,3}` weights the law-change coefficient becomes a weighted sum of one-child and sibling-controlled terms. The exact Aïdékon defect is already available from the earlier vector identity. The concrete target is to prove a uniform secant matrix inequality for the two branch coordinates in which the one-child mass is charged against the same inverse-escape moment from Lemma 4.1 and the degree-2/3 masses retain the independent-sibling contraction. If the resulting matrix spectral radius stays below one on a nontrivial probability simplex, the full-interval theorem extends from a curve to an open family.

P03-B’s escape-spine score/isometry remains a complementary route if the one-child channel becomes the dominant obstruction; that coupling argument is not duplicated here.

---

## 12. Source locators

- Lyons–Pemantle–Peres source problem: *Biased random walks on Galton–Watson trees*, PTRF 106 (1996), and their 1997 unsolved-problems chapter.
- Ben Arous, Fribergh, Sidoravicius: arXiv:1111.5865.
- E. Aïdékon: *Speed of the biased random walk on a Galton–Watson tree*, arXiv:1111.4313 / PTRF 159 (2014), especially the exact speed formula.
- H. Song, L. Wang, K. Xiang: arXiv:1610.08151; J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`.
- A. Bowditch, Y. Tokushige: arXiv:1906.07913 and arXiv:2006.03433.

No email, Google Drive, publication action, force-push, historical overwrite, or peer overwrite is part of this report.