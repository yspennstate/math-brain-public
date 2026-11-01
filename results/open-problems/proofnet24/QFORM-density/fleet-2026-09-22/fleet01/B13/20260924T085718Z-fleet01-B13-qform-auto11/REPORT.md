SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-24T08:57:18.267928Z.
attacking: extremal product-law purification and a product-set geometric receiver; apply the newest completed fleet02/B13 result to an explicit slab inequality without rotating independent coordinates.

# fleet01/B13 — finite-certificate purification and conditional-covariance escape

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T085718Z-fleet01-B13-qform-auto11`  
Role: extremal product laws / analytic derivation and exact structural identities  
Status: **NEW SUPPORTING THEOREMS / FULL QFORM OPEN / CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full target remains: for independent real coordinates with densities at most one and symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^TAX`, or produce a valid counterexample. Nothing below claims the unrestricted theorem is closed.

The live corrections used here are essential: no law-uniform pointwise quadratic oscillatory decay; no independence after rotating the random coordinates; no projection-density-only solution of the indefinite pushforward; no bounded-diameter, single-interval, centered-uniform, or fixed-fragment extremality assumption. All changes of basis below, when mentioned, are deterministic coefficient manipulations only. The main new work instead stays in the original product coordinates.

## 1. Completed partner result actually used

The newest completed designated-partner result available at refresh was fleet02/B13 run

`20260924T065522Z-fleet02-B13-qform-r11`,

canonical mathematics

`yspennstate/math-open-problems@c8bbb166c448ccd194451b47524b13d5de3eaed5`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260924T065522Z-fleet02-B13-qform-r11/REPORT.md`.

Its theorem `QFORM-TRANSLATION-INVARIANT-DIAMETER-ESCAPE-v1` is used below at an actual slab inequality. In the current high-density endpoint it supplies a decomposition

\[
A=M+F,
\qquad
M=D_C+\lambda_1vv^T,
\qquad |C|\le4,
\]

\[
F=E_{\rm sep}+E_{\rm ent},
\qquad
E_{\rm ent}=\lambda_2ww^T,
\qquad \|w\|_2=1,
\]
with

\[
\|E_{\rm sep}\|_{op}\le {C_D\over\rho},
\qquad
C_D=2\sqrt{30\pi}=19.41625912555699\ldots,
\tag{1.1}
\]

and, in the partner high-density branch,

\[
|\lambda_2|\le K_{\rm ent}\rho^{-7/6}
\tag{1.2}
\]
for a universal finite `K_ent`. Once `s_3(M)>=1/2`, every affine `M`-form under arbitrary translated cap-one product inputs has density at most

\[
\boxed{
C_M=500e\cdot5(8+\log5)
=65302.90114768759\ldots .
}
\tag{1.3}
\]

The partner uses this affine-uniform core to force large centered support width. The new result below replaces essential support width by **actual variance of the points already inside the high-density slab**. This is stronger in the precise sense that a tiny remote fragment cannot satisfy the new conclusion merely by making an essential diameter enormous.

## 2. Exact finite-certificate product purification

The first result strengthens the extremal-product interface in a direction useful for geometric sublevel sets. It does not assert that intervals, centered intervals, or boundedly many fragments are extremal.

### Theorem 2.1 — `QFORM-FINITE-CERTIFICATE-PRODUCT-PURIFICATION-v1`

Let `B_i subset R` be bounded measurable sets of finite measure. Let

\[
0\le f_i\le1,
\qquad \int_{B_i}f_i=1,
\qquad \operatorname{supp}f_i\subseteq B_i,
\]

and let `Phi_1,...,Phi_m` be bounded measurable functions on

\[
B=B_1\times\cdots\times B_n.
\]

Then there exist measurable sets `E_i subset B_i`, each of Lebesgue measure one, such that simultaneously for every `r=1,...,m`,

\[
\boxed{
\int_B \Phi_r(x)\prod_{i=1}^n 1_{E_i}(x_i)\,dx
=
\int_B \Phi_r(x)\prod_{i=1}^n f_i(x_i)\,dx.
}
\tag{2.1}
\]

In particular the marginals can be purified to unit-measure indicators while preserving any prescribed **finite list of bounded integral certificates exactly**.

#### Proof

Purify the coordinates one at a time. Suppose coordinates before `i` have already been replaced by indicators and coordinates after `i` still carry their original densities. Denote the current one-dimensional factors by `g_j`, with

\[
0\le g_j\le1,
\qquad \int g_j=1.
\]

For each certificate define the bounded fiber function

\[
h_{i,r}(t)
=
\int \Phi_r(x_1,\ldots,x_{i-1},t,x_{i+1},\ldots,x_n)
\prod_{j\ne i}g_j(x_j)\,dx_{-i}.
\tag{2.2}
\]

On the finite-measure atomless space `B_i`, define the finite vector measure

\[
\mu_i(A)
=
\int_A G_i(t)\,dt,
\qquad
G_i(t)=(1,h_{i,1}(t),\ldots,h_{i,m}(t))\in\mathbb R^{m+1}.
\tag{2.3}
\]

The functions in `G_i` are integrable. By Lyapunov's convexity theorem, the range

\[
\mathcal R_i=\{\mu_i(A):A\subseteq B_i\text{ measurable}\}
\]

is compact and convex.

Now use the layer-cake representation

\[
g_i(t)=\int_0^1 1_{\{g_i(t)>s\}}\,ds.
\]

Therefore

\[
\int_{B_i}g_i(t)G_i(t)\,dt
=
\int_0^1 \mu_i(\{g_i>s\})\,ds.
\tag{2.4}
\]

The right-hand side is a barycenter of points of the closed convex set `mathcal R_i`, hence belongs to `mathcal R_i`. Consequently there is a measurable `E_i subset B_i` with

\[
\mu_i(E_i)=\int g_iG_i.
\tag{2.5}
\]

Its first coordinate gives `|E_i|=1`. The remaining coordinates say that replacing `g_i` by `1_{E_i}` preserves all `m` global certificate integrals exactly. Repeat this for `i=1,...,n`. At the end every factor is an indicator and all prescribed certificates still have their original values. `QED`

### QFORM certificate corollary

Fix a symmetric `A` and interval `J`, and put

\[
K(x)=1_{\{x^TAx\in J\}}.
\]

For bounded-support inputs, apply Theorem 2.1 to the finite list

\[
K,\qquad x_iK\ (1\le i\le n),\qquad x_ix_jK\ (1\le i\le j\le n).
\tag{2.6}
\]

Then the product-indicator witness has exactly the same slab mass

\[
p=\Pr\{X^TAX\in J\},
\]

the same unnormalized slab first moments, and the same unnormalized slab second moments. Therefore, when `p>0`, it has **exactly the same conditional slab mean and covariance matrix** as the original product law:

\[
\boxed{
\operatorname{Cov}(X\mid X^TAX\in J)
\quad\text{is preserved exactly.}
}
\tag{2.7}
\]

This is the interface needed below. It is stronger than merely selecting an indicator witness with at least as much slab mass.

Scope note: Theorem 2.1 is stated for bounded supports so that the finite vector measure includes the mass coordinate and all selected certificates are bounded. For arbitrary unbounded laws, the already completed optimizer-free truncation/finite-mixture reduction gives arbitrarily small loss on a strict slab witness. If the conditional second moments are finite, bounded truncation also approximates the moment certificates; if they are infinite, the variance lower bounds below hold in the extended-value sense. No exact unbounded-support moment-preserving assertion is used here.

Bounded measurable `E_i` may subsequently be approximated in measure by bounded finite unions of intervals; because the certificates in (2.6) are bounded on `B`, all their integrals then change by arbitrarily little. There is no uniform fragment-count conclusion.

## 3. A full slab-tail profile for an affine-uniform core

The partner diameter theorem uses one deterministic support bound. A more informative statement is available without any support restriction.

### Theorem 3.1 — `QFORM-AFFINE-CORE-SLAB-TAIL-PROFILE-v1`

Let `Q=Q_0+R` be real random variables on the same probability space. Suppose `Q_0` has density bounded by `C`. Let `J` be an interval of length `ell`, let

\[
p=\Pr\{Q\in J\},
\qquad
a=(p-C\ell)_+.
\tag{3.1}
\]

Then for every `t>=0`,

\[
\boxed{
\Pr\{Q\in J,\ |R|>t\}
\ge
[p-C(\ell+2t)]_+.
}
\tag{3.2}
\]

Equivalently, for `0<=t<=a/(2C)`,

\[
\Pr\{Q\in J,\ |R|>t\}\ge a-2Ct.
\tag{3.3}
\]

For every `q>0`, this implies the moment hierarchy

\[
\boxed{
\mathbb E\left[|R|^q1_{\{Q\in J\}}\right]
\ge
{a^{q+1}\over(q+1)(2C)^q}.
}
\tag{3.4}
\]

In particular

\[
\boxed{
\mathbb E\left[|R|1_{\{Q\in J\}}\right]
\ge {a^2\over4C}.
}
\tag{3.5}
\]

#### Proof

On the event `{Q in J, |R|<=t}`, one has

\[
Q_0=Q-R\in J+[-t,t].
\]

The latter interval has length `ell+2t`, so

\[
\Pr\{Q\in J,|R|\le t\}\le C(\ell+2t).
\]

Subtract from `p` and truncate below at zero to get (3.2). For (3.4), use the layer-cake identity and integrate (3.3):

\[
\begin{aligned}
\mathbb E[|R|^q1_{\{Q\in J\}}]
&=q\int_0^\infty t^{q-1}\Pr\{Q\in J,|R|>t\}\,dt\\
&\ge q\int_0^{a/(2C)}t^{q-1}(a-2Ct)\,dt\\
&={a^{q+1}\over(q+1)(2C)^q}.
\end{aligned}
\]

`QED`

This theorem does not call a coefficient-small remainder probabilistically negligible. It quantifies how large the remainder must actually be on the high-density slab when the paid core alone cannot explain the slab mass.

## 4. Double-slab conditional-covariance escape

Now apply Theorem 3.1 to the partner's affine-uniform core in a translation-free way.

### Theorem 4.1 — `QFORM-DOUBLESLAB-CONDITIONAL-COVARIANCE-ESCAPE-v1`

Let `X=(X_1,...,X_n)` have independent cap-one densities and let

\[
A=M+F
\tag{4.1}
\]
be symmetric. Assume the following affine-uniform hypothesis for `M`:

> for every deterministic vector `b`, scalar `c`, and every coordinatewise translation of the cap-one product law, the random variable
> \[
> Y^TMY+b^TY+c
> \]
> has density at most `C_M`.

Let

\[
Q(X)=X^TAX,
\qquad
S=\{Q(X)\in J\},
\qquad
\ell=|J|,
\]

\[
p=\Pr(S)=\rho\ell,
\qquad
a=(p-C_M\ell)_+.
\tag{4.2}
\]

Let `X'` be an independent copy and `S'={Q(X') in J}`. Then for every

\[
0\le t\le {a\over2C_M},
\]

\[
\boxed{
\Pr\left\{S,S',\ |(X-X')^TF(X-X')|>t\right\}
\ge
p(a-2C_Mt).
}
\tag{4.3}
\]

Consequently

\[
\boxed{
\mathbb E\left[
|(X-X')^TF(X-X')|\,1_{S}1_{S'}
\right]
\ge
{p a^2\over4C_M}.
}
\tag{4.4}
\]

If the conditional second moment is finite, then

\[
\boxed{
\operatorname{tr}\operatorname{Cov}(X\mid S)
\ge
{a^2\over8C_M\|F\|_{op}\,p}.
}
\tag{4.5}
\]

If the conditional second moment is infinite, (4.5) is interpreted in the extended-value sense and is automatic.

When `rho>=2C_M`, `a>=p/2`, so

\[
\boxed{
\operatorname{tr}\operatorname{Cov}(X\mid S)
\ge
{\rho\ell\over32C_M\|F\|_{op}}.
}
\tag{4.6}
\]

In particular, if `||F||op<=C_F/rho`,

\[
\boxed{
\operatorname{tr}\operatorname{Cov}(X\mid S)
\ge
{\rho^2\ell\over32C_MC_F}.
}
\tag{4.7}
\]

#### Proof

Fix any `x' in S` and put `Y=X-x'`. Expand the actual form:

\[
\begin{aligned}
Q(X)
&=Y^TAY+2(Ax')^TY+x'^TAx'\\
&=\underbrace{Y^TMY+2(Ax')^TY+x'^TAx'}_{Q_{0,x'}(Y)}
+Y^TFY.
\end{aligned}
\tag{4.8}
\]

The law of `Y` is still a product of coordinatewise translated cap-one densities. By the affine-uniform hypothesis, `Q_{0,x'}` has density at most `C_M`, uniformly in `x'`. Theorem 3.1 therefore gives, for every fixed `x' in S`,

\[
\Pr_X\{S, |(X-x')^TF(X-x')|>t\}
\ge a-2C_Mt
\tag{4.9}
\]
for `0<=t<=a/(2C_M)`.

Integrate (4.9) with respect to the independent `X'`, restricted to `S'`. Since `P(S')=p`, this gives (4.3). Integrating (4.3) in `t` gives (4.4).

Conditioned on `S,S'`, the two variables are independent draws from the same conditional law `Law(X|S)`. Therefore

\[
\mathbb E[\|X-X'\|_2^2\mid S,S']
=2\operatorname{tr}\operatorname{Cov}(X\mid S).
\tag{4.10}
\]

On the other hand

\[
|(X-X')^TF(X-X')|
\le \|F\|_{op}\|X-X'\|_2^2.
\tag{4.11}
\]

Divide (4.4) by `p^2` and combine (4.10)-(4.11):

\[
{a^2\over4C_Mp}
\le
2\|F\|_{op}\operatorname{tr}\operatorname{Cov}(X\mid S),
\]
which is (4.5). If `rho>=2C_M`, then `a=p-C_M ell>=p/2`, yielding (4.6); substituting `||F||op<=C_F/rho` gives (4.7). `QED`

### Exact narrow bilinear identity on the same slab pairs

Every pair of points in `S` also satisfies

\[
\boxed{
|(X-X')^TA(X+X')|
=|Q(X)-Q(X')|
\le \ell.
}
\tag{4.12}
\]

Thus (4.3)-(4.7) do not merely say that the support is broad. They force actual pairs of points **inside the same high-density quadratic slab** to have large difference energy while those same pairs obey the narrow bilinear constraint (4.12).

Before conditioning on `S,S'`, the difference coordinates `U_i=X_i-X_i'` are independent and each has density at most one:

\[
g_i(u)=\int f_i(x)f_i(x-u)\,dx\le\|f_i\|_\infty\int f_i\le1.
\tag{4.13}
\]

Conditioning on the double slab destroys that independence; (4.13) is retained only as original-product provenance for a future decoupling/smoothing receiver, not as a conditional-independence assertion.

## 5. Application to the completed fleet02/B13 endpoint

Use the partner decomposition from Section 1 and define the conditional slab variances

\[
V_{\rm tail,S}
=\sum_{i\notin C}\operatorname{Var}(X_i\mid S),
\tag{5.1}
\]

\[
V_{w,S}
=\operatorname{Var}(w^TX\mid S).
\tag{5.2}
\]

Write the diagonal entries of `E_sep` as `e_i`. From (1.1),

\[
|e_i|\le {C_D\over\rho}.
\tag{5.3}
\]

For two independent slab-conditioned copies and `U=X-X'`,

\[
\mathbb E[|U^TE_{\rm sep}U|\mid S,S']
\le
2\sum_{i\notin C}|e_i|\operatorname{Var}(X_i\mid S),
\tag{5.4}
\]

and

\[
\mathbb E[|U^TE_{\rm ent}U|\mid S,S']
=
2|\lambda_2|\operatorname{Var}(w^TX\mid S).
\tag{5.5}
\]

Combining (4.4), the triangle inequality, and (5.4)-(5.5) gives the **actual partner inequality**

\[
\boxed{
\sum_{i\notin C}|e_i|\operatorname{Var}(X_i\mid S)
+|\lambda_2|V_{w,S}
\ge
{a^2\over8C_Mp}.
}
\tag{5.6}
\]

For `rho>=2C_M`, use `a>=p/2`, `p=rho ell`, and (5.3):

\[
\boxed{
{C_D\over\rho}V_{\rm tail,S}
+|\lambda_2|V_{w,S}
\ge
{\rho\ell\over32C_M}.
}
\tag{5.7}
\]

Equivalently,

\[
\boxed{
C_DV_{\rm tail,S}
+\rho|\lambda_2|V_{w,S}
\ge
{\rho^2\ell\over32C_M}.
}
\tag{5.8}
\]

Therefore every sufficiently high-ratio survivor in this partner chamber satisfies at least one of

\[
\boxed{
V_{\rm tail,S}
\ge
{\rho^2\ell\over64C_MC_D},
}
\tag{5.9}
\]

or

\[
\boxed{
V_{w,S}
\ge
{\rho\ell\over64C_M|\lambda_2|}.
}
\tag{5.10}
\]

The first explicit denominator is

\[
64C_MC_D
=81148035.22138466\ldots .
\tag{5.11}
\]

Using the partner source-minimal estimate (1.2), the second branch gives

\[
\boxed{
V_{w,S}
\ge
{\rho^{13/6}\ell\over64C_MK_{\rm ent}}.
}
\tag{5.12}
\]

This is the main advance of the run: partner r11 had already proved that essential centered support widths must diverge. Equations (5.9)-(5.12) show that a fixed amount of the escape must be present in the **conditional geometry of actual slab points**. A set of extremely remote but vanishingly small fragments cannot by itself account for these conditional-variance lower bounds.

## 6. Product-set geometric form and compatibility with purification

For a unit product set

\[
E=E_1\times\cdots\times E_n,
\qquad |E_i|=1,
\]
let

\[
S_E=\{x\in E:x^TAx\in J\},
\qquad p=|S_E|.
\]

The conditional slab mean is

\[
\bar x={1\over p}\int_{S_E}x\,dx,
\]
so

\[
\operatorname{Cov}_E(x\mid S_E)
={1\over p}\int_{S_E}(x-\bar x)(x-\bar x)^T\,dx.
\tag{6.1}
\]

Thus the partner endpoint plus Theorem 4.1 becomes a genuine geometric sublevel-set statement: for `rho=p/ell>=2C_M`, either

\[
\boxed{
{1\over p}\int_{S_E}
\sum_{i\notin C}(x_i-\bar x_i)^2\,dx
\ge
{\rho^2\ell\over64C_MC_D},
}
\tag{6.2}
\]

or

\[
\boxed{
{1\over p}\int_{S_E}
\bigl(w^T(x-\bar x)\bigr)^2\,dx
\ge
{\rho^{13/6}\ell\over64C_MK_{\rm ent}}.
}
\tag{6.3}
\]

For bounded-support arbitrary cap-one inputs, Theorem 2.1 can preserve exactly the certificate family (2.6), hence exactly `p`, `bar x`, and the covariance matrix in (6.1). Therefore this covariance escape is **not an artifact of replacing the product law by indicator marginals**. It survives exact finite-certificate purification.

This is stronger than an extremal support-diameter statement but still falls short of the full target because conditioning on the slab has destroyed coordinate independence. The next receiver must use the original product provenance before conditioning, or an exact double-slab/decoupling identity, rather than pretending that the conditional law remains product.

## 7. First unpaid implication

The first unpaid implication is now

`QFORM-CONDITIONAL-COVARIANCE-BANK-TO-BILINEAR-SMOOTHING-v1`:

> Combine the forced slab-conditioned variance in either (6.2) or (6.3) with the exact narrow double-slab bilinear identity
> \[
> |(X-X')^TA(X+X')|\le |J|
> \]
> and the ambient cap-one product provenance of the independent differences before slab conditioning, to obtain a dimension-free small-ball/density payment while retaining both `E_sep` and the secondary rank-one carrier in the phase.

A proof must not assume conditional independence, bounded support diameter, a single interval per marginal, or that the coefficient-small tails may be dropped. No such glue is claimed here.

## 8. Scope and status

- `QFORM-FINITE-CERTIFICATE-PRODUCT-PURIFICATION-v1`: **proved** in the stated bounded-support finite-certificate scope.
- `QFORM-AFFINE-CORE-SLAB-TAIL-PROFILE-v1`: **proved** abstractly.
- `QFORM-DOUBLESLAB-CONDITIONAL-COVARIANCE-ESCAPE-v1`: **proved** under the explicitly stated affine-core hypothesis.
- Application (5.6)-(5.12): **proved conditional on the completed partner endpoint**, with the partner constants and scope retained exactly.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.

No scheduler/task mutation, email/push action, cross-account authentication, paid call, public release, remote workflow, permission expansion, rotation of the independent random variables, or production-memory mutation is part of this run.

## 9. Source/provenance notes

Fresh source control used: `yspennstate/math-research-brain` main, owner-control revision `2026-09-22.15`; initial fresh-main observation `b888aca01e194c4ab6d4509501444898e75668cd`, with main re-read before publication after concurrent fleet writes. The current programme files `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and assignment `fleet01/B13.json` were read before deriving the results.

Designated partner proof used at source pin:

`yspennstate/math-open-problems@c8bbb166c448ccd194451b47524b13d5de3eaed5:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260924T065522Z-fleet02-B13-qform-r11/REPORT.md`.

Changed-file review for this mathematical repository write: only this run-owned `REPORT.md`; no credentials, account secrets, private personal archives, financial/trading material, benchmark answers, or unrelated data are present. No repository-integrated secret scanner was exposed through the connector, so the privacy check for this write is a manual narrow changed-file review rather than a claim of a full repository scan.
