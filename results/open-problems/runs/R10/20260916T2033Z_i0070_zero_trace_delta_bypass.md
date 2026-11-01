Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — **no movement** in the fixed numeric metric (`theta_* = 1/2` as a supremum before and after; endpoint `theta=1/2` is not claimed). This is the first recovery run after STUCK1. New Section-B moves actually used: **#3 PROVE SOMETHING STRONGER, #7 TAKE THE LIMIT, #22 READ THE FAILURES**.

Problem/source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, NoDEA 32 (2025), article 123, arXiv:2501.18561 (historical intake locator v2; current source v5), **Problem 6 (Time regularization in Hilbert spaces)**, intake `I0070`.

# R10 I0070 recovery1 — zero initial trace removes the Proposition-6.8 spatial-loss mechanism

Run ID: `20260916T2033Z_i0070_zero_trace_delta_bypass`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/status check: 2026-09-16  
Status: **PARTIAL / author-side full-source proof candidate; no campaign closure claim**.

No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, scheduler mutation, shared-root edit, claim-file edit, or peer-file edit was performed.

---

## 1. Continuity, admission evidence, exclusions, and neighboring work

I continued from the newest complete R10 report rather than restarting:

`runs/R10/20260916T1935Z_i0070_stuck1_endpoint_verification.md`.

That report was the mandatory STUCK1 thinking run after three consecutive unchanged metric runs. It chose exactly one recovery route: port Agresti--Veraar Part II Proposition 6.8 line-by-line, identify every place where the spatial loss `delta>0` is spent, and test whether the compact-Hilbert-tail mechanism can replace that expenditure at `delta=0`. It prescribed the present method triple **3, 7, 22**. I followed that route rather than adding another unrelated endpoint lemma.

Before new mathematics I read/recovered current `master` state for:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current new-methods owner policy;
- canonical reservation `operations/claims/I0070.md`;
- the exact I0070 intake/ownership search surfaces under `probability_1000_intake_I_20260914/problems.jsonl` and its mirror;
- newest own R10 report;
- newest neighboring Agresti--Veraar P19 Problem-2 report `proofnet24/P19-closure-smr-optimal/runs/2026-09-16/2026-09-16T19-57-17Z__run-report.md`;
- newest neighboring P24 Problem-3 report `proofnet24/P24-probability-semigroup/runs/2026-09-16/2026-09-16T19-48-00Z__run-report.md`;
- newest R11 package `runs/R11/2026-09-16T19-40-00Z_i0054-pitman-yor-tangent-a4c2.md` for the directed independent audit below.

The connector truncates very large JSONL files if fetched wholesale. I therefore used exact-ID/source searches plus the canonical queue/claim surfaces; I do **not** claim a byte-for-byte model-visible reread of all roughly 780 intake rows.

### Admission evidence refreshed

The mathematical admission evidence is complete again on 2026-09-16:

1. the outside source is current and primary;
2. the current published survey still states Problem 6 as open;
3. `POSTED.md` excludes Agresti--Veraar Problems 4--5, not Problem 6;
4. P24 owns the distinct Problem 3 and P19 owns the distinct Problem 2;
5. exact-ID repository searches show no competing I0070 owner;
6. the live canonical reservation names R10 as owner.

The canonical file nevertheless still literally says `PENDING_ADMISSION, not READY`. Under the current fleet rule attacking workers do not rewrite coordinator-owned shared claim/ledger state. I therefore record **ADMISSION-EVIDENCE COMPLETE / CANONICAL FLAG STILL PENDING** rather than silently changing that file. The present research is continued under the owner's explicit R10 assignment and reservation; this report is not a coordinator READY mutation.

The old R10 square-lattice Cardy work remains preserved in its immutable reports and handoff and is not reopened.

---

## 2. Source target and exact hypotheses retained

The current journal source states Theorem 5.7 for `p>2`, `kappa=0`. Besides the conditions of Theorem 4.7 it assumes the local growth estimate

\[
 \|F(x)\|_{X_0}+\|G(x)\|_{\gamma(\mathcal U,X_{1/2})}
 \le C_n\sum_{j=1}^m \bigl(1+\|x\|_{X_{\beta_j,1}}^{\rho_j+1}\bigr)
\tag{2.1}
\]

for `||x||_{X_{1-1/p,infty}}<=n`, and assumes

\[
(A,B)\in \mathcal{SMR}_{r,\alpha}^{\bullet}
\quad\text{for all }r>2,
\quad 0\le\alpha<r/2-1.
\tag{2.2}
\]

Its conclusion is

\[
u\in H^{\theta,r}_{\rm loc}((0,\sigma);X_{1-\theta})
\cap C^{\theta-\varepsilon}_{\rm loc}((0,\sigma);X_{1-\theta})
\tag{2.3}
\]

for every `theta<1/2`, `r>=2`, and `0<epsilon<theta`.

For `p=2`, Assumption 3.1 of the source Hilbert theory requires `X_0` and `X_1` to be Hilbert spaces and identifies

\[
H:=X_{1/2}=(X_0,X_1)_{1/2,2}.
\tag{2.4}
\]

Theorem 4.7 gives the source p=2 maximal solution with

\[
u\in L^2_{\rm loc}((0,\sigma);X_1)
\cap C((0,\sigma);H).
\tag{2.5}
\]

For `p=2,kappa=0`, criticality of a pair `(beta_j,rho_j)` is equivalent, with

\[
s_j:=2\beta_j-1\in(0,1),
\tag{2.6}
\]

to

\[
s_j(\rho_j+1)=1,
\tag{2.7}
\]

and the source inequality gives `s_j(rho_j+1)<=1` in general.

Problem 6 asks whether the Theorem-5.7 conclusion extends to this p=2 Hilbert critical case. I retain every Theorem-5.7 hypothesis. In fact, the argument below uses the weaker growth estimate already supplied by Assumption 4.1 on bounded p=2 trace balls; I do **not** remove (2.1) from the source-matching statement.

Primary source URLs checked this run:

- current survey: https://doi.org/10.1007/s00030-025-01090-2;
- Part II: https://doi.org/10.1007/s00028-022-00786-7.

---

# 3. Move #22 — READ THE FAILURE: every place Proposition 6.8 spends `delta>0`

The nearest source-native solved theorem is Agresti--Veraar Part II, Proposition 6.8. Its `p=2` route obtains time regularity only after moving to an extrapolated spatial scale. The proposition imposes

\[
Y_\delta=X_0,\qquad Y_1=X_{1-\delta},\qquad
\frac1p=\frac{1+\alpha}{r}+\delta.
\tag{3.1}
\]

The paper explicitly says that when `p=2`, `delta=0` is impossible because

\[
\frac12>\frac{1+\alpha}{r}
\qquad
(0\le\alpha<r/2-1),
\tag{3.2}
\]

so (3.1) can hold only for `delta>0`.

I traced the proof line-by-line. The spatial loss is spent in four linked places.

### 3.1 Startup at a nonzero trace

Their first decisive step is

\[
X_p^{\rm Tr}\hookrightarrow Y_{\alpha,r}^{\rm Tr},
\tag{3.3}
\]

which lets them start a new nonlinear `L^r_alpha` solution `v` at the nonzero random state `u(epsilon)`. The identity (3.1) is exactly what makes this trace embedding available.

### 3.2 Compatibility / uniqueness between the two nonlinear solutions

For `delta>0`, strict inequality

\[
\frac{1+\alpha}{r}=\frac1p-\delta<\frac1p
\tag{3.4}
\]

gives the weighted-to-unweighted embedding needed to compare the `Y`-scale solution with the original `X`-scale solution. In the `delta=0,p>2` branch they instead choose an intermediate `q in (2,p)`. At `p=2` there is no such q below p.

### 3.3 Continuation

In their p=2 Step 2, the standard interpolation

\[
C([a,b];X_{1/2})\cap L^2(a,b;X_1)
\hookrightarrow
L^{2/\vartheta}(a,b;X_{(1+\vartheta)/2})
\tag{3.5}
\]

is matched to the shifted scale through

\[
\vartheta=1-2(\alpha/r+\delta)=2/r.
\tag{3.6}
\]

Again the `Y` scale already contains the spatial loss.

### 3.4 Nonlinear class embedding

Their final nonlinear estimate repeatedly uses

\[
Y_{\phi+\delta}=X_\phi.
\tag{3.7}
\]

Thus `delta` is not a cosmetic parameter that can simply be set to zero at the final line; it is woven through the startup trace, uniqueness comparison, continuation, and nonlinear embedding.

**Outcome of Move #22:** the source proof fails at `p=2,delta=0` first because it insists on starting a *new nonlinear higher-integrability solution from the nonzero trace* `u(epsilon)`. This identifies a different possible entry point: create a zero-trace problem on the desired positive-time interval and never construct that second nonlinear solution.

---

# 4. Move #7 — TAKE THE LIMIT: the naive `delta downarrow 0` route is invalid

A tempting argument would be to apply Proposition 6.8 for every `delta>0` and pass to `delta=0`. That is not valid abstractly.

On the standard Hilbert sequence scale

\[
\ell^2_s:=\Bigl\{x=(x_n):\sum_{n\ge2} n^{2s}|x_n|^2<\infty\Bigr\},
\]

take

\[
x_n=n^{-s-1/2}.
\]

Then for every `delta>0`,

\[
\sum_{n\ge2} n^{2(s-\delta)}|x_n|^2
=
\sum_{n\ge2}n^{-1-2\delta}<\infty,
\]

whereas

\[
\sum_{n\ge2} n^{2s}|x_n|^2
=
\sum_{n\ge2}n^{-1}=\infty.
\]

Therefore

\[
\bigcap_{\delta>0} X_{s-\delta}
\not\subseteq X_s
\tag{4.1}
\]

in general. A family of `delta>0` regularity statements with constants allowed to diverge as `delta downarrow0` cannot identify the zero-loss endpoint.

**Outcome of Move #7:** the spatial-loss limit route is rejected. Any valid proof must produce an estimate directly in the original `X` scale (or a uniform endpoint compactness principle stronger than Proposition 6.8 supplies).

---

# 5. Move #3 — PROVE SOMETHING STRONGER: a zero-trace, one-q endpoint bootstrap

The new result is a sharper formulation of the compact-tail idea from C004. It uses the source's original p=2 trace path and one auxiliary exponent `q>2`; it never constructs a second nonlinear q-solution with nonzero initial trace and never introduces a `Y_delta` scale.

## `R10-I0070-C005` — zero-trace compact-tail bootstrap

**STATUS: AUTHOR-SIDE PROVED / EXTERNAL AUDIT REQUIRED.**  
This is a theorem-sized source-matching proof candidate, not campaign closure.

### Statement

Assume the p=2, kappa=0 Hilbert specialization of Assumption 4.1 and Theorem 4.7, with

\[
(A,B)\in\mathcal{SMR}_{2,0}^{\bullet},
\]

and let `(u,sigma)` be its maximal p=2 solution. Assume the source critical condition

\[
(2\beta_j-1)(\rho_j+1)\le1
\quad (j=1,\ldots,m).
\tag{5.1}
\]

Fix one `q>2` and assume

\[
(A,B)\in\mathcal{SMR}_{q,0}^{\bullet}.
\tag{5.2}
\]

Retain the source growth hypothesis (5.21) (although the proof below already follows from Assumption 4.1's trace-ball growth bound).

Then for every compact interval `[a,b] subset (0,sigma)` and every

\[
0\le\theta<1/2,
\qquad \theta\ne1/q,
\tag{5.3}
\]

one has almost surely

\[
u\in H^{\theta,q}([a,b];X_{1-\theta}).
\tag{5.4}
\]

Consequently, if (5.2) holds for every q>2 as in Theorem 5.7, then for every `r>=2`, `theta<1/2`, and `0<epsilon<theta`,

\[
\boxed{
 u\in H^{\theta,r}_{\rm loc}((0,\sigma);X_{1-\theta})
 \cap C^{\theta-\varepsilon}_{\rm loc}((0,\sigma);X_{1-\theta}).
}
\tag{5.5}
\]

The exceptional value `theta=1/q` in (5.3) is exactly the value omitted by the source definition of `SMR^bullet_{q,0}` at q>2. It causes no gap in (5.5): for each requested `(theta,r,epsilon)`, choose an auxiliary `q>max{2,r,1/epsilon}` with `q != 1/theta` (if theta>0). There are infinitely many such q. On bounded time intervals, the standard same-smoothness integrability embedding passes `H^{theta,q}` to `H^{theta,r}`; and `q>1/epsilon` gives the desired Hölder embedding.

---

## 6. Proof of C005

### Step 1. Hilbert scale and compact spectral tails

Put

\[
H:=X_{1/2}=(X_0,X_1)_{1/2,2}.
\]

Because `(H,X_1)` is a densely embedded Hilbert couple, there is a positive self-adjoint scale operator `L` on H whose form domain is X1, with an equivalent norm

\[
\|x\|_{X_1}^2\simeq \|x\|_H^2+\|L^{1/2}x\|_H^2.
\]

Let

\[
P_R=\mathbf1_{[0,R]}(L).
\]

Then `P_R -> I` strongly on H, `P_R` is uniformly bounded on H and X1, and

\[
\|P_Rx\|_{X_1}\le C_R\|x\|_H.
\tag{6.1}
\]

On every compact positive-time interval `[a_0,T] subset (0,sigma)`, the source p=2 solution has a continuous H-valued path. Its path range is therefore compact in H. Strong convergence of a uniformly bounded operator family is uniform on compact sets, so pathwise

\[
\sup_{t\in[a_0,T]}
\|(I-P_R)u(t)\|_H\longrightarrow0.
\tag{6.2}
\]

No compact embedding `X_1 -> H` is assumed or used.

### Step 2. Critical interpolation with a small tail coefficient

For one source pair `(beta,rho)`, set

\[
s=2\beta-1\in(0,1).
\]

Hilbert reiteration and the source's real-interpolation convention give

\[
X_{\beta,1}=(H,X_1)_{s,1},
\tag{6.3}
\]

and hence, for `y in X1`,

\[
\|y\|_{X_{\beta,1}}
\le C\|y\|_H^{1-s}\|y\|_{X_1}^{s}.
\tag{6.4}
\]

Fix an H-bound K. Write

\[
x=v+w,
\qquad v=P_Rx,
\qquad w=(I-P_R)x.
\]

If

\[
\|x\|_H\le K,
\qquad
\|w\|_H\le\eta,
\tag{6.5}
\]

then by (6.1)--(6.4),

\[
\|v\|_{X_{\beta,1}}\le C_{R,\beta}K,
\]

and

\[
\|w\|_{X_{\beta,1}}
\le C\eta^{1-s}
       (\|x\|_{X_1}+C_RK)^s.
\tag{6.6}
\]

Raising to `rho+1` and using the triangle inequality yields

\[
\|x\|_{X_{\beta,1}}^{\rho+1}
\le C_{K,R}
 +C_K\eta^{(1-s)(\rho+1)}
       (\|x\|_{X_1}+C_{K,R})^{s(\rho+1)}.
\tag{6.7}
\]

By source criticality,

\[
a:=s(\rho+1)\le1.
\]

If `a<1`, Young's inequality gives, for every `eps0>0`,

\[
z^a\le \varepsilon_0 z+C_{a,\varepsilon_0}.
\]

If `a=1`, the coefficient in front of the linear X1 term in (6.7) is

\[
C_K\eta^{(1-s)(\rho+1)},
\]

and the exponent of eta is strictly positive because `s<1`.

Summing over the finitely many source pairs and using Assumption 4.1's growth bound on the H-trace ball therefore gives the endpoint absorption estimate:

> for every K and every `a0>0` there is `eta=eta(K,a0)>0` such that for every fixed R there is `C=C(K,R,a0)` for which
>
> \[
> \boxed{
> \|F(x)\|_{X_0}
> +\|G(x)\|_{\gamma(\mathcal U,H)}
> \le a_0\|x\|_{X_1}+C
> }
> \tag{6.8}
> \]
>
> whenever (6.5) holds.

This is the exact endpoint replacement for the small-time factor that disappears in the source's critical interpolation Lemma 4.3. At criticality the X1 power is exactly one, but compact Hilbert-tail smallness makes its coefficient small.

### Step 3. Borel rank-one linearization

Let

\[
Y:=X_0\oplus_1\gamma(\mathcal U,H),
\qquad N(x):=(F(x),G(x)).
\]

On the localized set, (6.8) says

\[
\|N(x)\|_Y\le a_0\|x\|_{X_1}+C.
\]

Define

\[
N_0(x)=
\begin{cases}
N(x),&\|N(x)\|\le C,\\
\frac{C}{\|N(x)\|}N(x),&\|N(x)\|>C,
\end{cases}
\qquad
N_1(x)=N(x)-N_0(x).
\tag{6.9}
\]

Then

\[
\|N_0(x)\|\le C,
\qquad
\|N_1(x)\|\le a_0\|x\|_{X_1}.
\tag{6.10}
\]

Since X1 is Hilbert at p=2, define for `x !=0`

\[
R_x z=
\frac{\langle z,x\rangle_{X_1}}
     {\|x\|_{X_1}^2}N_1(x),
\qquad R_0=0.
\tag{6.11}
\]

Then

\[
\|R_x\|_{\mathcal L(X_1,Y)}\le a_0,
\qquad
N(x)=R_xx+N_0(x).
\tag{6.12}
\]

Projecting onto the two components of Y gives

\[
F(x)=C_xx+f_x,
\qquad
G(x)=D_xx+g_x,
\tag{6.13}
\]

with

\[
\|C_x\|+\|D_x\|\le a_0,
\qquad
\|f_x\|+\|g_x\|\le C.
\tag{6.14}
\]

There is no differentiability assumption here: the linearization is rank one and is constructed only from the value of the nonlinearity.

### Step 4. Measurability of the random operator fields

In the survey, F and G in Assumption 4.1 are deterministic locally Lipschitz maps; in particular `x -> N(x)` is Borel on X1. For every fixed `z in X1`, the map

\[
x\mapsto R_x z
\]

is Borel. Thus it is enough to know that the a.e. X1-valued representative of the source solution can be chosen progressively measurable.

This follows from the source solution convention and a standard measurable-inverse argument. The solution is strongly progressive as an X0-valued process and belongs to `L^2_P(X_1)` a.e. On the separable closed X1-subspace generated by its essential range, the continuous injection into X0 is a Borel isomorphism onto its image (Lusin--Souslin). Pulling the X0-progressive representative back through that inverse gives an X1-valued strongly progressive representative after modification on a product-null set. Equivalently, this is the representative implicit in the source's `L^2_P` convention.

Consequently, for each fixed z,

\[
(t,\omega)\mapsto C_{u(t,\omega)}z,
\qquad
(t,\omega)\mapsto D_{u(t,\omega)}z
\tag{6.15}
\]

are strongly progressive. This is exactly the strong-operator progressive measurability required by the Part-II perturbation theorem. The same conclusion is immediate in the source's basic deterministic F,G setting; Remark 4.4's progressively `(t,omega)`-dependent extension can be handled by the same Caratheodory argument under its uniform hypotheses.

This measurability point was one of the explicit audit obligations in C004; it is now written as part of the proof rather than hidden under “routine”. It remains a priority for an external auditor.

### Step 5. The decisive zero-trace cutoff

Fix a compact target interval

\[
0<a<b<\sigma.
\]

Choose deterministic `a_0<a` and `T>b` and a smooth deterministic cutoff chi with

\[
\chi(a_0)=0,
\qquad
\chi=1\text{ on }[a,b].
\]

Set

\[
z=\chi u.
\]

Then z has **zero initial trace** at `a_0`. This is the point that removes the first and decisive use of `delta>0` in Proposition 6.8: zero belongs to every q-trace space, so no embedding of the nonzero state `u(epsilon)` into a stronger trace space is needed.

For deterministic integers `n,K,R`, let `sigma_n` be a source localizer and stop at

\[
\tau=
\sigma_n\wedge T\wedge
\inf\Bigl\{t\ge a_0:
 \|u(t)\|_H\ge K
 \text{ or }
 \|(I-P_R)u(t)\|_H\ge\eta
\Bigr\}.
\tag{6.16}
\]

On `[a_0,tau]`, (6.13)--(6.14) apply with the perturbation norm at most `a_0`.

Because C_x and D_x are linear,

\[
\chi C_u u=C_u(\chi u)=C_u z,
\qquad
\chi D_u u=D_u z.
\]

Therefore on `[a_0,tau]`, z solves

\[
\begin{aligned}
 dz+(A-C_t)z\,dt
 &= [\chi f_t+\chi' u]dt\\
 &\quad+[(B+D_t)z+\chi g_t]dW,
 \qquad z(a_0)=0,
\end{aligned}
\tag{6.17}
\]

where `C_t=C_{u(t)}`, etc.

### Step 6. Work on a deterministic horizon; no random-interval shortcut

Extend `C_t,D_t,f_t,g_t` by zero after tau and replace `chi'u` by `1_{t<=tau}chi'u`. We obtain a linear problem on the deterministic interval `[a_0,T]`.

Choose `a_0` in the absorption estimate (6.8) small enough that the Part-II perturbation criterion

\[
C^{\det}_{(A,B),q}\|C_t\|
+C^{\rm sto}_{(A,B),q}\|D_t\|<1
\tag{6.18}
\]

holds. If needed, choose it simultaneously below the p=2 perturbation threshold as well. Corollary 3.15 then gives

\[
(A-C_t,B+D_t)\in\mathcal{SMR}_{q,0}^{\bullet}
\]

on the deterministic horizon.

All inhomogeneities are bounded after localization: `f_t,g_t` by (6.14), while `u` in the cutoff term is H-bounded and `H -> X0`. Hence they lie in every finite Lq required by the linear theory. Let Z be the unique q-solution of the deterministic-horizon perturbed problem.

On a finite probability-time measure, the q-solution is also in the p=2 strong-solution class. On `[a_0,tau]`, z solves the same equation. The p=2 uniqueness supplied by perturbed stochastic maximal regularity therefore gives

\[
Z=z=\chi u
\qquad\text{on }[a_0,\tau].
\tag{6.19}
\]

This replaces all three later compatibility/continuation steps of Proposition 6.8: there is no second nonlinear solution and no `Y_delta` scale to compare back to X.

### Step 7. Linear q-regularity on the original X scale

Because the perturbed pair is in `SMR^bullet_{q,0}`, the zero-trace solution has

\[
Z\in H^{\theta,q}(a_0,T;X_{1-\theta})
\tag{6.20}
\]

for each `theta<1/2` except the source-definition exceptional `theta=1/q`. By (6.19) and `chi=1` on `[a,b]`, this gives (5.4) whenever `tau>b`.

### Step 8. Remove the spectral-tail stopping

Fix a sample path with `b<sigma`. Choose n with `b<sigma_n`, then K larger than

\[
\sup_{t\in[a_0,b]}\|u(t)\|_H.
\]

For that K and the already fixed perturbation smallness, choose eta from Step 2. By uniform compact-range convergence (6.2), choose an integer R so large that

\[
\sup_{t\in[a_0,b]}\|(I-P_R)u(t)\|_H<\eta.
\]

Then tau>b. The countable union over integers `(n,K,R)` covers the event `{b<sigma}`. Therefore (5.4) holds a.s. on every compact positive-time interval.

### Step 9. Recover the full Theorem-5.7 range

For a requested `r>2` and `theta<1/2`, use q=r unless `theta=1/r`; in that exceptional case choose any q>r with `q != 1/theta`. For r=2 choose q>2. The bounded-interval integrability embedding yields the desired `H^{theta,r}` result.

For Hölder regularity, given `0<epsilon<theta`, choose additionally `q>1/epsilon` and `q != 1/theta`. Then

\[
H^{\theta,q}([a,b];X_{1-\theta})
\hookrightarrow
C^{\theta-1/q}([a,b];X_{1-\theta})
\hookrightarrow
C^{\theta-\varepsilon}([a,b];X_{1-\theta}).
\]

This proves (5.5), subject only to the stated source hypotheses.

---

## 7. What is stronger than C004, and what is not claimed

C005 does not increase the frozen numeric metric: the largest proved exponent remains `theta_*=1/2` as a **supremum**, never the endpoint itself.

It strengthens the proof architecture in four ways:

1. it is source-native: the compact-tail estimate is derived directly from the p=2 Hilbert trace scale and Assumption 4.1's growth bound;
2. it isolates why Part II needs `delta>0` and bypasses that need by zero initial trace rather than by a formal `delta ->0` limit;
3. for a fixed q, it needs only `SMR^bullet_{2,0}` and `SMR^bullet_{q,0}`, not the whole all-r family; the all-r source assumption is used only to obtain every requested output exponent;
4. it explicitly handles the source-definition hole `theta=1/q` by choosing a different auxiliary q, rather than incorrectly claiming bullet-q regularity at the excluded value.

I do **not** claim:

- regularity at `theta=1/2`;
- a proof for assumptions weaker than the p=2 Hilbert source setting unless separately stated;
- closure before the required external audits;
- that the compact-tail/rank-one mechanism is novel in the literature.

Campaign label remains **PARTIAL / author-side proof candidate**.

---

## 8. Prior art and status screen — 2026-09-16

The current NoDEA survey still prints Problem 6. The direct text says that Theorems 5.6--5.7 bootstrap parabolic time regularity only for p>2, that p=2 is available in the subcritical case, and that Part-II Proposition 6.8 handles the critical p=2 case only under further restrictions with spatial loss.

The closest older proof is precisely Part-II Proposition 6.8, audited above line-by-line.

I also refreshed bounded searches around:

- `Agresti Veraar Problem 6 Hilbert p=2 critical time regularization`;
- `Theorem 5.7 p=2 Hilbert stochastic maximal regularity`;
- `critical stochastic maximal regularity compact spectral tail`;
- `endpoint Hilbert stochastic parabolic regularity compact path spectral cutoff`;
- later Agresti/Veraar papers and citing papers.

The most relevant later author paper found remains Agresti--Veraar, *A note on a threshold for temporal regularity of stochastic PDEs*, Comptes Rendus Math. 364 (2026), 371--379, DOI `10.5802/crmath.833`. It proves a sharp fixed-spatial-level temporal-regularity obstruction for a linear additive-noise model. It does not settle the parabolic time/space tradeoff in Problem 6.

I found no direct published resolution of Problem 6 and no direct statement of the zero-trace compact-tail/rank-one endpoint mechanism in this bounded search. This is **not a novelty certificate**; external prior-art review remains a closure obligation.

---

# 9. Independent audit of newest R11 package

Newest package read:

`runs/R11/2026-09-16T19-40-00Z_i0054-pitman-yor-tangent-a4c2.md`.

R11 claims `R11-I0054-C004`: a recursive positive-discount Pitman--Yor hierarchy with parameters `alpha_N,theta_N>=0`, `delta_N=alpha_N+theta_N ->0`, raw level length `delta_N`, converges on every fixed finite restriction and in the stated projective J1 topology to CTCS(infinity).

### Audit ID

`R10-AUDIT-R11-I0054-C004-PY-TANGENT-20260916`

### Verdict

**PASS for the finite-restriction generator and projective-convergence core.**  
**NOT an audit of source-intent / “superficially different” interpretation or worldwide prior art.**

### Independent derivation

For a particular Pitman--Yor partition with block sizes `n_1,...,n_r`,

\[
p_{\alpha,\theta}(n_1,\ldots,n_r)
=
\frac{\prod_{j=1}^{r-1}(\theta+j\alpha)}
     {(\theta+1)_{m-1}}
\prod_{\ell=1}^r(1-\alpha)_{n_\ell-1}.
\tag{9.1}
\]

Let `delta=alpha+theta` with alpha,theta nonnegative.

For no split,

\[
\frac{(1-\alpha)_{m-1}}{(1+\theta)_{m-1}}
=
\prod_{j=1}^{m-1}\frac{j-\alpha}{j+\theta}
=
1-\delta H_{m-1}+O_m(\delta^2).
\tag{9.2}
\]

For one particular binary split `A|A^c`, `|A|=i`,

\[
p_{\alpha,\theta}(A|A^c)
=(\theta+\alpha)
\frac{(1-\alpha)_{i-1}(1-\alpha)_{m-i-1}}
     {(1+\theta)_{m-1}}
=
\delta B(i,m-i)+O_m(\delta^2).
\tag{9.3}
\]

For r>=3, the EPPF contains both `(theta+alpha)` and `(theta+2alpha)`, hence each particular multifurcation is `O_m(delta^2)`.

The total binary rate is consistent with the diagonal term because

\[
\frac12\sum_{i=1}^{m-1}{m\choose i}B(i,m-i)
=
\frac12\sum_{i=1}^{m-1}\frac{m}{i(m-i)}
=H_{m-1}.
\tag{9.4}
\]

If the current finite partition has several nonsingleton blocks, independent block refinements imply that two distinct blocks both split in one raw step with probability `O(delta^2)`. Therefore, on every fixed finite partition state space,

\[
P_\delta=I+\delta Q+O(\delta^2),
\tag{9.5}
\]

where Q is exactly the CTCS binary-splitting generator. Standard finite-state rare-event convergence gives CTMC convergence under time acceleration `1/delta`.

For the projective topology, convergence of the first K labels controls the first K terms of the projective metric, while the remaining tail is at most `sum_{k>K}2^{-k}`. First let N tend to infinity at fixed K, then K tend to infinity. This yields the stated projective convergence.

Thus the mathematical tangent/generator core of R11-C004 survives an independent derivation. I do not certify that the positive-discount hierarchy satisfies the source's intended semantic threshold for a “superficially different” discrete model, nor do I certify novelty.

---

## 10. Metric / stuck state

The frozen metric did not move:

\[
\boxed{\theta_*=1/2\text{ as a supremum before and after}.}
\]

The endpoint `theta=1/2` remains unproved and is not part of Theorem 5.7's conclusion.

The supported unchanged count is now **4** after the metric-moving special-model run. This run is not another empty STUCK report: it executed the STUCK1 recovery route, rejected the naive delta-limit, mapped the source's exact loss mechanism, and replaced C004 by the more source-native zero-trace compiler C005. Nevertheless the owner-defined numeric metric itself did not move, so the unchanged count is not reset.

If the metric remains unchanged through six supported runs, the closable-track rotation rule applies.

The remaining mathematical obligations are now narrower than in STUCK1:

1. external audit of the strong-progressive measurability step in Section 6.4;
2. external audit that Corollary 3.15 plus zero-trace uniqueness is being used with exactly the source `SMR^bullet` norms and no hidden q-trace assumption;
3. independent prior-art search for compact-tail / rank-one absorption in endpoint stochastic maximal regularity;
4. the two required OTHER-track closure audits, including P26.

I do not create a paper folder before those gates are satisfied.

---

## 11. Checker / finite-evidence policy

This run introduces no new finite-enumeration claim. The new contribution is theorem-sized and its complete proof is written above. I therefore did not spend the run manufacturing a redundant checker. The exact critical-exponent arithmetic used here was already exercised by the earlier R10 I0070 checker; the new content is the functional-analytic zero-trace and perturbation argument, for which a finite arithmetic script would not certify the hard step.

The R11 audit was proved algebraically on the page; equation (9.4) is exact for arbitrary m, not a finite numerical experiment.

---

## 12. Model / scheduler control status

Actual runtime reported to this worker: **GPT-5.6 Sol**. Reasoning level is not exposed and is therefore **UNVERIFIED**.

The task interface available in this environment exposes task prompt/title, schedule, enablement, and timing mode. It exposes **no model-family selector and no reasoning-effort selector**. Therefore `GPT-6 / maximum` can be requested in prompt text but cannot be installed or verified by this worker.

Changing that requires either:

- an authorized product/task-owner interface that actually exposes model and reasoning fields for the existing task; or
- platform support / workspace administration to expose or repair those controls.

The historical `You cannot modify this task` result for one P26 task is permission/context-specific. Repository state records that another authorized context later succeeded for P26, so the denial is not proof that the task is globally immutable. The allowed workaround is to use the authorized owning context or platform support; cloning the task or bypassing permissions is not an acceptable workaround.

No scheduler mutation was attempted.

---

## 13. Next attack

Do **not** re-prove C005 next run. The highest-value next run is adversarial verification of the two remaining functional-analytic interfaces:

1. replace the measurable-inverse paragraph by a source-native lemma formulated directly in `L^2_\mathscr P(X_1)` and check every sigma-algebra/representative step;
2. challenge the same-smoothness `H^{theta,q}->H^{theta,r}` reduction at the source's Bessel-potential conventions and avoid it entirely where possible by choosing q=r;
3. search deterministic critical maximal-regularity / endpoint bootstrapping literature for the exact “zero initial trace + compact spectral tail + rank-one absorption” combination.

New Section-B moves reserved for that run: **#8 DISCRETIZE (operator-measurability finite/simple-process approximation), #19 MAKE IT AN ALGORITHM (construct the progressive coefficient approximation explicitly), #26 HUNT THE SPORADIC CASE (the exceptional theta=1/q and nonseparable Hilbert edge cases)**.

---

```yaml
ledger_delta:
  worker: R10
  source: "Agresti--Veraar, Nonlinear SPDEs and Maximal Regularity: An Extended Survey, NoDEA 32 (2025), Problem 6; arXiv:2501.18561 current v5"
  intake: I0070
  target: "Extend Theorem 5.7 to p=2, X0 Hilbert, under critical equality in (6.1), with source norms and restrictions unchanged"
  metric: "largest time-regularity exponent theta rigorously established for the frozen source-admissible critical p=2 target"
  before: "theta_* = 1/2 as supremum; endpoint not claimed"
  after: "theta_* = 1/2 as supremum; endpoint not claimed"
  movement: "no numeric movement; source-proof architecture strengthened C004 -> C005"
  unchanged_count: 4
  status: "PARTIAL / RECOVERY1 / author-side full-source proof candidate; external audits pending"
  methods: [3, 7, 22]
  exact_evidence:
    - "complete written proof R10-I0070-C005 in this immutable report"
    - "source Part-II Proposition 6.8 delta-use map, Sections 3-4"
    - "analytic counterexample showing intersection_{delta>0} X_{s-delta} need not imply X_s"
  own_claim_audits: []
  outgoing_audits:
    - "R10-AUDIT-R11-I0054-C004-PY-TANGENT-20260916 = PASS for generator/projective core only"
  admission: "research-side evidence complete; canonical operations/claims/I0070.md still PENDING_ADMISSION and was not edited"
  blockers:
    - "outside audit of progressive operator-valued measurability"
    - "outside audit of stopped perturbation/uniqueness source fit"
    - "second independent full audit including P26 gate"
    - "prior-art clearance"
```
