Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — terminal critical monotonicity from a normalized escape contraction

**Status:** PROVED PARTIAL (new repository theorem candidate; not independently audited; no claim of external novelty; the full Lyons–Pemantle–Peres conjecture remains unresolved).

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Old D0047 history is preserved. Canonical ownership was checked at assignment and is not reopened here.

**Captured master before this write:** `2effacb1f7f0025aa4c8b438e3b19add17302cbc`.

**Inherited analytic checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0603Z__critical-edge-speed-asymptotic.md`, creation commit `76cc4d0d07441f633977c9c2978d13fdce90d1cb`.

**Complementary P03-B checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0618Z__selected-ancestor-stack-envelope.md`.

The fixed full-source metric remains

`R_full: 1 -> 1`.

The intermediate obligation **does move**: the previous report proved only a first-order critical-edge speed asymptotic and fixed-ratio comparisons; this report upgrades that to strict monotonicity on an entire terminal interval below the recurrence boundary, under a finite fourth-moment hypothesis.

## 1. Source normalization and current proved range

Let `nu` be the offspring variable of a supercritical Galton–Watson tree without leaves:

\[
P(\nu=0)=0,\qquad m=E\nu>1.
\]

The source paper of Ben Arous–Fribergh–Sidoravicius uses an outward child-bias `beta`, with

\[
P_\beta(x,x^*)=\frac1{1+\beta\nu(x)},\qquad
P_\beta(x,x_i)=\frac\beta{1+\beta\nu(x)}.
\]

This report uses the reciprocal **parent-bias** parameter

\[
\lambda=\beta^{-1},
\qquad
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+\nu(x)},
\qquad
P_\lambda(x,x_i)=\frac1{\lambda+\nu(x)}.
\tag{1.1}
\]

Thus the transient interval is `0<lambda<m`, and the Lyons–Pemantle–Peres conjecture is that the speed `ell_lambda` is nonincreasing in `lambda` (equivalently increasing in outward `beta`).

The strongest checked broad source-uniform monotonicity theorem remains Song–Wang–Xiang, *Journal of Applied Probability* 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: if the minimum offspring is `d>=2`, then the speed is strictly decreasing for

\[
0\le \lambda\le
\frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

Bowditch–Tokushige, arXiv:1906.07913, prove differentiability where the walk is ballistic and satisfies a CLT, and arXiv:2006.03433 proves analyticity in the ballistic regime; neither result supplies the derivative sign. Ben Arous–Hu–Olla–Zeitouni prove an Einstein relation at the critical point under an exponential-moment hypothesis. That linear response is important prior art: the critical first-order behavior itself should not be treated as novel. What was still missing from our analytic line was a **uniform sign on a whole interval** immediately below `lambda=m`; a mere ratio asymptotic does not imply that sign.

A bounded 20 September 2026 literature refresh did not surface a checked theorem giving this terminal interval for arbitrary no-leaf offspring laws. This is negative evidence only, not a novelty certificate.

## 2. Inherited critical expansion and the new target

Let `B_lambda` be the quenched probability, from a child-root, of never hitting its parent. With iid copies `B_1,B_2,...` and `S_k=sum_{i=1}^k B_i`,

\[
B_\lambda\stackrel d=\frac{S_\nu}{\lambda+S_\nu}.
\tag{2.1}
\]

Write

\[
e_\lambda=EB_\lambda,
\qquad
f_2=E[\nu(\nu-1)].
\]

The preceding P03-A report proved, assuming `E nu^3<infinity`, that as `lambda up m`,

\[
e_\lambda
=\frac{m-1}{f_2}(m-\lambda)+o(m-\lambda),
\tag{2.2}
\]

and, using Aidekon's exact speed representation,

\[
\ell_\lambda
=\frac{m-1}{2f_2}(m-\lambda)+o(m-\lambda).
\tag{2.3}
\]

Equation (2.3) gives fixed-ratio terminal comparisons, but it does **not** justify differentiating the `o(m-lambda)` remainder. The target of this run is therefore quantitative regularity of that remainder.

For the rest of the report assume the slightly stronger hypothesis

\[
\boxed{E\nu^4<\infty.}
\tag{2.4}
\]

No positive minimum offspring larger than one and no bounded-support assumption is imposed.

Put

\[
\delta:=m-\lambda,
\qquad
e_\delta:=e_{m-\delta},
\qquad
r_\delta:=\frac{e_\delta}{\delta},
\qquad
X_\delta:=\frac{B_{m-\delta}}{e_\delta}.
\tag{2.5}
\]

Then `E X_delta=1`. If

\[
Y_\delta:=\sum_{i=1}^{\nu}X_{\delta,i},
\]

the escape recursion becomes the exact normalized fixed-point equation

\[
\boxed{
X_\delta\stackrel d=
F_{\delta,r_\delta}(Y_\delta)
:=\frac{Y_\delta}
{m-\delta+\delta r_\delta Y_\delta}.
}
\tag{2.6}
\]

This normalization is the new route: at `delta=0` the nonlinear escape transform becomes the strict `L^2` branching smoothing contraction `Y -> Y/m`.

## 3. Uniform fourth moments and two-sided control of the escape scale

Let

\[
q_j(\delta):=E X_\delta^j.
\]

Choose `delta_0>0` small enough that `lambda_0=m-delta_0` satisfies

\[
\lambda_0^j>m\quad(j=2,3,4),
\qquad
\lambda_0>1.
\tag{3.1}
\]

This is possible because `m>1`.

From `B<=S_nu/lambda`, the usual moment expansions give

\[
E B^2\le\frac{mEB^2+f_2(EB)^2}{\lambda^2},
\tag{3.2}
\]

\[
E B^3\le\frac{mEB^3+3f_2(EB^2)(EB)+f_3(EB)^3}{\lambda^3},
\tag{3.3}
\]

and

\[
E B^4\le\frac{
 mEB^4+4f_2(EB^3)(EB)+3f_2(EB^2)^2
 +6f_3(EB^2)(EB)^2+f_4(EB)^4
}{\lambda^4},
\tag{3.4}
\]

where `f_j=E[(nu)_j]`. Since the coefficients `lambda^j-m` stay uniformly positive on `[lambda_0,m)`, induction through (3.2)–(3.4) yields

\[
\boxed{
\sup_{0<\delta\le\delta_0}E X_\delta^4<\infty.
}
\tag{3.5}
\]

In particular the normalized second and third moments are uniformly bounded.

There is also a useful deterministic two-sided estimate for `e_delta`. Concavity of `x/(lambda+x)` and `E S_nu=m e` gives

\[
e\le\frac{me}{\lambda+me},
\]
so

\[
\boxed{e_\delta\le\frac\delta m.}
\tag{3.6}
\]

For the reverse direction use

\[
\frac{x}{\lambda+x}\ge\frac x\lambda-\frac{x^2}{\lambda^2}.
\]

Together with (3.2), this gives

\[
\delta\lambda e
\le mEB^2+f_2e^2
\le
f_2e^2\frac{\lambda^2}{\lambda^2-m},
\]
therefore

\[
\boxed{
e_\delta\ge
\delta\frac{\lambda^2-m}{f_2\lambda}.}
\tag{3.7}
\]

Consequently `r_delta` is bounded above and away from zero for sufficiently small `delta`.

## 4. An exact scalar identity for the normalized escape slope

Let

\[
D_\delta(y):=m-\delta+\delta r_\delta y.
\]

Taking means in (2.6) gives

\[
1=E\frac{Y_\delta}{D_\delta(Y_\delta)}.
\tag{4.1}
\]

Since `E Y_delta=m`, multiply the integrand in (4.1) by its denominator:

\[
m
=(m-\delta)E\frac{Y_\delta}{D_\delta(Y_\delta)}
+\delta r_\delta E\frac{Y_\delta^2}{D_\delta(Y_\delta)}.
\]

Using (4.1), cancel `m-delta` and obtain the exact identity

\[
\boxed{
 r_\delta^{-1}
=E\frac{Y_\delta^2}{D_\delta(Y_\delta)}.
}
\tag{4.2}
\]

The preceding critical-asymptotic report already identified

\[
\boxed{
r_\delta\longrightarrow r_0:=\frac{m-1}{f_2}.}
\tag{4.3}
\]

The point of (4.2) is that `r_delta` can now be controlled jointly with the normalized fixed point instead of by differentiating an unnormalized escape probability.

## 5. Pairwise `W_2` contraction: the normalized law is Lipschitz at criticality

### Lemma 5.1

There exist `delta_*>0` and `C<infinity`, depending only on the offspring law, such that for all `0<eta,delta<=delta_*`,

\[
\boxed{
W_2(\mathcal L(X_\delta),\mathcal L(X_\eta))
+|r_\delta-r_\eta|
\le C|\delta-\eta|.
}
\tag{5.1}
\]

#### Proof

Write

\[
w:=W_2(\mathcal L(X_\delta),\mathcal L(X_\eta)),
\qquad h:=|\delta-\eta|,
\qquad \bar\delta:=\max(\delta,\eta).
\]

Couple iid child pairs optimally and use the **same** offspring variable `nu`. Since both normalized variables have mean one, each child difference has mean zero. Hence

\[
\left\|Y_\delta-Y_\eta\right\|_2=\sqrt m\,w.
\tag{5.2}
\]

For fixed `delta,r`,

\[
\frac{\partial}{\partial y}F_{\delta,r}(y)
=\frac{m-\delta}{(m-\delta+\delta r y)^2}
\le\frac1{m-\delta}.
\tag{5.3}
\]

Thus changing only the input law costs at most

\[
\frac{\sqrt m}{m-\delta_*}w.
\]

Choose `delta_*` small enough that

\[
q:=\frac{\sqrt m}{m-\delta_*}<1.
\tag{5.4}
\]

For the parameter changes,

\[
\partial_\delta F_{\delta,r}(y)
=\frac{y(1-r y)}{(m-\delta+\delta r y)^2},
\qquad
\partial_r F_{\delta,r}(y)
=-\frac{\delta y^2}{(m-\delta+\delta r y)^2}.
\tag{5.5}
\]

The uniform fourth-moment bound (3.5), together with the uniform bounds on `r_delta`, therefore yields

\[
\boxed{
w\le q w+C h+C\bar\delta|r_\delta-r_\eta|.}
\tag{5.6}
\]

Now use the scalar identity (4.2). Set

\[
A(\delta,r,\mu)
:=E_\mu\frac{Y^2}{m-\delta+\delta rY},
\]
where `Y` is the `nu`-sum of iid samples from `mu`. The denominator is uniformly bounded below. Its derivative in `y` satisfies

\[
\left|\partial_y\frac{y^2}{m-\delta+\delta r y}\right|
\le C y,
\]
while the parameter derivatives are bounded in expectation by constants times `E(Y^2+Y^3)`. The moment bound (3.5) and (5.2) therefore give

\[
|A_\delta-A_\eta|
\le Cw+Ch+C\bar\delta|r_\delta-r_\eta|.
\tag{5.7}
\]

Because `r_delta` is uniformly bounded above and away from zero, `A_delta=1/r_delta` is also uniformly bounded above and away from zero. Hence (5.7) implies

\[
|r_\delta-r_\eta|
\le Cw+Ch+C\bar\delta|r_\delta-r_\eta|.
\tag{5.8}
\]

Shrink `delta_*` so the last term is absorbed. Then

\[
|r_\delta-r_\eta|\le C(w+h).
\tag{5.9}
\]

Substitute (5.9) into (5.6) and shrink `delta_*` once more so that the resulting coefficient multiplying `w` is strictly below one. This proves (5.1). QED.

Taking `eta downarrow0` and using (4.3) gives the quantitative upgrade

\[
\boxed{
|r_\delta-r_0|\le C\delta.
}
\tag{5.10}
\]

Likewise, from

\[
|EX_\delta^2-EX_\eta^2|
\le\|X_\delta-X_\eta\|_2
\|X_\delta+X_\eta\|_2,
\]
we obtain

\[
\boxed{
q_2(\delta)=\frac{f_2}{m(m-1)}+O_{\rm Lip}(\delta),
}
\tag{5.11}
\]

where `O_Lip(delta)` means not only `O(delta)` but the pairwise estimate

\[
|R(\delta)-R(\eta)|\le C|\delta-\eta|.
\]

A more useful second-order notation below is

\[
R=O_{\rm Lip}(\delta^2)
\quad\Longleftrightarrow\quad
|R(\delta)-R(\eta)|
\le C\max(\delta,\eta)|\delta-\eta|,
\qquad R(0)=0.
\tag{5.12}
\]

Equation (5.10) immediately implies

\[
\boxed{
e_\delta=r_0\delta+O_{\rm Lip}(\delta^2).}
\tag{5.13}
\]

## 6. Second-order Lipschitz expansion of Aidekon's escape tilt

For `lambda>1`, define, as in the inherited exact speed representation,

\[
c_n(\lambda)
:=\frac1{n+1}
E\left[\frac{S_{n+1}}{\lambda-1+S_{n+1}}\right].
\tag{6.1}
\]

Because `S_{n+1}=e_delta Y_{n+1}` with `Y_{n+1}` a sum of normalized escapes, the common factor `e_delta` cancels from the tilted offspring mean. Put

\[
a_\delta:=m-1-\delta,
\]

\[
d_n(\delta)
:=\frac{c_n(m-\delta)}{e_\delta}
=\frac1{n+1}E\left[
\frac{Y_{n+1}}{a_\delta+e_\delta Y_{n+1}}
\right].
\tag{6.2}
\]

Let

\[
C_\delta:=E[d_\nu(\delta)],
\qquad
H_\delta:=E[\nu d_\nu(\delta)],
\qquad
M_\delta:=\frac{H_\delta}{C_\delta}.
\tag{6.3}
\]

Aidekon's speed formula in this normalization is

\[
\boxed{
\ell_{m-\delta}
=\frac{M_\delta-(m-\delta)}{M_\delta+(m-\delta)}.
}
\tag{6.4}
\]

Use the exact identity

\[
\frac y{a+ey}
=\frac ya-\frac{e y^2}{a^2}
+\frac{e^2y^3}{a^2(a+ey)}.
\tag{6.5}
\]

If `N=n+1`, then `EY_N=N`, and

\[
\frac1N EY_N^2=q_2(\delta)+n.
\tag{6.6}
\]

Therefore

\[
C_\delta
=\frac1{a_\delta}
-\frac{e_\delta}{a_\delta^2}
\bigl(q_2(\delta)+m\bigr)+R_0(\delta),
\tag{6.7}
\]

\[
H_\delta
=\frac m{a_\delta}
-\frac{e_\delta}{a_\delta^2}
\bigl(mq_2(\delta)+E\nu^2\bigr)+R_1(\delta).
\tag{6.8}
\]

The remainders are

\[
R_j(\delta)
=\frac{e_\delta^2}{a_\delta^2}
E\left[
\frac{w_j(\nu)}{\nu+1}
\frac{Y_{\nu+1}^3}{a_\delta+e_\delta Y_{\nu+1}}
\right],
\quad w_0=1,\quad w_1=\nu.
\tag{6.9}
\]

The fourth-moment hypothesis is used here a second time. Couple the normalized child arrays as in Lemma 5.1. Since

\[
\left|\partial_y\frac{y^3}{a+ey}\right|\le\frac{3y^2}{a},
\quad
\left|\partial_a\frac{y^3}{a+ey}\right|\le\frac{y^3}{a^2},
\quad
\left|\partial_e\frac{y^3}{a+ey}\right|\le\frac{y^4}{a^2},
\tag{6.10}
\]

uniform fourth moments of `X_delta`, the estimate (5.1), and `E nu^4<infinity` imply that the bracketed expectations in (6.9) are locally Lipschitz and uniformly bounded. Since `e_delta=O(delta)` with the second-order Lipschitz refinement (5.13),

\[
\boxed{R_0(\delta),R_1(\delta)=O_{\rm Lip}(\delta^2).}
\tag{6.11}
\]

Now subtract `m C_delta` from `H_delta`. The entire normalized second-moment term cancels exactly:

\[
H_\delta-mC_\delta
=-\frac{e_\delta}{a_\delta^2}
\operatorname{Var}(\nu)
+O_{\rm Lip}(\delta^2).
\tag{6.12}
\]

Also `C_delta=1/a_delta+O(delta)` and is bounded away from zero. Consequently

\[
M_\delta-m
=-\frac{\operatorname{Var}(\nu)e_\delta}{a_\delta}
+O_{\rm Lip}(\delta^2).
\tag{6.13}
\]

Using (5.13), `a_delta=m-1-delta`, and `r_0=(m-1)/f_2`,

\[
\boxed{
M_\delta
=m-rac{\operatorname{Var}(\nu)}{f_2}\,\delta
+O_{\rm Lip}(\delta^2).
}
\tag{6.14}
\]

This is the central new estimate. The previous run had only an `o(delta)` remainder; the normalized contraction upgrades it to a remainder whose **increments** are quadratic-order.

## 7. Main theorem: a whole terminal interval of strict monotonicity

Recall

\[
f_2
=\operatorname{Var}(\nu)+m(m-1).
\tag{7.1}
\]

Insert (6.14) into (6.4). Since the denominator tends to `2m`, smooth quotient algebra preserves the second-order Lipschitz remainder and gives

\[
\boxed{
\ell_{m-\delta}
=c_*\delta+O_{\rm Lip}(\delta^2),
\qquad
c_*:=\frac{m-1}{2f_2}>0.
}
\tag{7.2}
\]

That is, there are constants `C<infinity` and `delta_*>0` such that for `0<=eta<delta<=delta_*`,

\[
\left|
\bigl(\ell_{m-\delta}-c_*\delta\bigr)
-
\bigl(\ell_{m-\eta}-c_*\eta\bigr)
\right|
\le C\delta(\delta-\eta).
\tag{7.3}
\]

Shrink `delta_*` so that `C delta_*<c_*/2`. Then

\[
\ell_{m-\delta}-\ell_{m-\eta}
\ge
(c_*-C\delta_*)(\delta-\eta)
\ge\frac{c_*}{2}(\delta-\eta)>0.
\tag{7.4}
\]

We have proved:

### Theorem 7.1 — terminal critical monotonicity

Assume

\[
P(\nu=0)=0,\qquad E\nu=m>1,\qquad E\nu^4<\infty.
\]

Then there exists `epsilon=epsilon(L(nu))>0` such that the speed of the parent-biased walk is **strictly decreasing** on

\[
\boxed{m-\epsilon<\lambda<m.}
\tag{7.5}
\]

Equivalently, in the original outward child-bias parameter `beta=1/lambda`, the speed is strictly increasing on the corresponding interval immediately above the critical bias `beta=1/m`.

This theorem does not assume minimum offspring at least two. In particular it covers genuinely random no-leaf laws with `P(nu=1)>0`, which are outside the hypothesis of the 2025 low-parent-bias theorem (1.2).

No differentiability theorem is needed for the sign conclusion: (7.4) is a direct two-parameter comparison. Thus the argument does not infer a derivative sign by illegally differentiating a first-order `o(delta)` expansion.

## 8. Explicit nontrivial family reached by the theorem

Take

\[
P(\nu=1)=1-p,
\qquad
P(\nu=2)=p,
\qquad 0<p\le1.
\tag{8.1}
\]

Then

\[
m=1+p,\qquad f_2=2p,\qquad c_*=\frac14.
\tag{8.2}
\]

Therefore for every fixed `p in (0,1]` there exists `epsilon_p>0` such that

\[
\boxed{
\ell_\lambda\text{ is strictly decreasing on }
(1+p-\epsilon_p,1+p).
}
\tag{8.3}
\]

Moreover the terminal comparison has the quantitative form

\[
\ell_{1+p-\delta}-\ell_{1+p-\eta}
\ge\frac18(\delta-\eta)
\tag{8.4}
\]

for all sufficiently small `0<=eta<delta`, after shrinking the family-dependent terminal interval. This family has minimum offspring one and therefore demonstrates that the new theorem is not just another extension of the `d>=2` low-bias machinery.

## 9. What was actually gained, and what remains

**New proved obligation:** under `E nu^4<infinity`, the critical-edge first-order asymptotic has been upgraded to a two-parameter `O_Lip(delta^2)` expansion, and hence to strict monotonicity on a whole terminal interval `(m-epsilon,m)`.

**Relation to prior art:** the Einstein relation already gives critical linear response under stronger exponential-moment assumptions, so the coefficient-level phenomenon is not asserted as new. The new repository contribution is the normalized fixed-point contraction that controls increments of the remainder strongly enough to force a terminal interval sign, under a fourth-moment assumption and without a minimum-offspring-two condition. This remains a theorem candidate pending independent review and literature comparison.

**Full-source metric:** `R_full: 1 -> 1`. The conjecture still asks for the entire transient interval for every source-admissible no-leaf supercritical offspring law.

**Exact remaining gaps:**

1. The terminal interval size `epsilon` above is qualitative, not explicit.
2. The fourth-moment hypothesis is stronger than the original no-leaf source assumption.
3. For minimum offspring `d>=2`, P03-A now has rigorous intervals from the low-bias side and from the critical side, but an intermediate gap may remain.
4. For minimum offspring one, the new result controls only the terminal side; there is no all-interval theorem.

## 10. Next analytic attack

The next run should **not** repeat the critical first-order expansion. The highest-value next step is one of the following, in order:

1. Quantify the contraction constants in Lemma 5.1 and the tilt remainders for the two-point family `{1,2}` to obtain an explicit `epsilon_p`, starting with `p=1/2`.
2. Replace fourth moments by a truncation/uniform-integrability argument, aiming for a finite `2+epsilon` or finite second-moment terminal theorem.
3. For `d>=2`, combine an explicit terminal endpoint with the earlier harmonic-tail/core-tail low-bias certificates and test whether the two proved intervals overlap for a nontrivial class, which would yield a full-interval restricted-family theorem.

The key reusable lemma for any of these is (5.1): normalized escape laws and the scalar escape slope move Lipschitzly in the criticality defect because the critical smoothing transform has strict `L^2` contraction factor `m^{-1/2}<1`.