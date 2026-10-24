Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# I0006: localized susceptibility, terminal-potential representation, and the critical terminal-scale barrier

Status: **proved restricted analytic theorems / PARTIAL relative to canonical I0006**.  
Owner: `R7-06`, native ID `6aabe827777c8191a43330b4a87d481d`.  
Canonical target: `I0006`.  
Admission: `research7_2026-09-17/R7-06/admissions/2026-09-18T100120Z__I0006.md`.  
Run-start master snapshot: `5ed5bf562aee27a6d03422cdf1f4368583c7618f`.  
Pre-artifact fresh master snapshot: `b39f91566e96ebe9bd4b71eda8d78ed10013ead3`.  
Previous report: `research7_2026-09-17/R7-06/runs/2026-09-18/2026-09-18T160200Z__report.md` @ `f5999d3d8e87e1b01369e4504ecd5f080606d419`.

This note executes the precommitted post-STUCK1 methods **B5 / B18 / B25**. It closes the formal localized-envelope gap left by the previous run and reduces the inverse-square susceptibility to a terminal-radius quantity. It does **not** settle the full source or the slowly varying correction.

The source-valid recovery case remains dimension `d=5` with smooth symmetric critical Weibull scenery

\[
\nu(dt)=Z^{-1}e^{-|t|^{5/2}}\,dt.
\tag{1.1}
\]

For deterministic scenery `z`, write

\[
F_n(z)=u_n^z(0)
=\sup_{\tau\le n}\mathbb E_0\sum_{j=0}^{\tau-1}z(X_j),
\tag{1.2}
\]

where immediate stopping is allowed. The previous run proved horizon-independent concentration for `F_n(\zeta)` and showed that negative inverse-square cores are suppressive rather than favorable events. The missing bridge was a rigorous local-penalty interpolation identity. That identity is proved below.

## 1. B5 — localized envelope theorem with ties handled exactly

Fix any finitely supported `h:Z^5->[0,infinity)` and define

\[
F_{n,h}(\lambda;z)=F_n(z-\lambda h),\qquad \lambda\ge0.
\tag{1.3}
\]

Only the finite space-time region reachable before time `n` matters. A deterministic Markov stop/continue policy `\pi` on that finite region has an occupation vector

\[
\mu_\pi(x)=\mathbb E_0\sum_{j<\tau_\pi}{\bf1}_{\{X_j=x\}},
\tag{1.4}
\]

and payoff

\[
L_\pi(z-\lambda h)
=\sum_x\mu_\pi(x)z(x)-\lambda\sum_x\mu_\pi(x)h(x).
\tag{1.5}
\]

There are only finitely many such deterministic Markov policies, and finite-horizon dynamic programming shows that one of them is optimal. Hence `lambda -> F_{n,h}(lambda;z)` is the maximum of finitely many affine functions.

### Theorem 1.1 (exact right derivative for a local penalty)

Let `Opt(lambda,z)` be the finite set of policies optimal at `z-lambda h`. Then

\[
\boxed{
-\partial_{\lambda+}F_{n,h}(\lambda;z)
=
\min_{\pi\in\operatorname{Opt}(\lambda,z)}
\sum_x h(x)\mu_\pi(x).
}
\tag{1.6}
\]

In particular, if `tau_{lambda,h}^z` is an optimal policy chosen to minimize the `h`-weighted occupation among all optimal policies, then

\[
\boxed{
-\partial_{\lambda+}F_{n,h}(\lambda;z)
=
\mathbb E_0\sum_{j<\tau_{\lambda,h}^z}h(X_j).
}
\tag{1.7}
\]

#### Proof

Write the finitely many affine policy values as `a_pi-lambda c_pi`, where

\[
c_\pi=\sum_xh(x)\mu_\pi(x)\ge0.
\]

For the pointwise maximum of finitely many affine functions, the right derivative at `lambda` is the largest slope among the currently active affine functions. Their slopes are `-c_pi`, so the largest slope is `-min_{pi in Opt}c_pi`. This is (1.6), and (1.7) is its stopping-time form. ∎

Now let `zeta` have law (1.1) and define

\[
A_{n,h}(\lambda)=\mathbb E F_{n,h}(\lambda;\zeta),
\qquad
\chi_{n,h}(\lambda)
=
\mathbb E\mathbb E_0\sum_{j<\tau_{\lambda,h}^{\zeta}}h(X_j).
\tag{1.8}
\]

Every stopped occupation satisfies `mu_pi(x)<=g_n(0,x)`, so the difference quotients in (1.6) are bounded by the deterministic finite number `sum_x h(x)g_n(0,x)`. Dominated convergence therefore gives the annealed identity.

### Corollary 1.2 (localized susceptibility sum rule)

For every `lambda>=0`,

\[
\boxed{
-\partial_{\lambda+}A_{n,h}(\lambda)=\chi_{n,h}(\lambda).
}
\tag{1.9}
\]

The map `A_{n,h}` is decreasing and convex and, for every `Lambda>0`,

\[
\boxed{
A_{n,h}(0)-A_{n,h}(\Lambda)
=
\int_0^\Lambda\chi_{n,h}(s)\,ds.
}
\tag{1.10}
\]

This proves the localized interpolation identity requested by the previous report without assuming uniqueness of the optimizer and without a formal-envelope gap.

## 2. B18 — translate local susceptibility into a terminal-potential problem

Take the critical inverse-square profile

\[
w_R(x)=\frac{{\bf1}_{\{|x|<R\}}}{1+|x|^2},
\qquad R\ge4.
\tag{2.1}
\]

Let `G(x,y)=sum_{k>=0}p_k(x,y)` be the infinite simple-random-walk Green kernel on `Z^5`, and define its potential

\[
H_R(y)=\sum_xG(y,x)w_R(x).
\tag{2.2}
\]

Because `w_R` has finite support and the walk is transient, `H_R` is finite and bounded. Moreover

\[
(I-P)H_R=w_R.
\tag{2.3}
\]

Let `tau=lambda` abbreviate the tie-minimal optimal stopping rule `tau_{lambda,w_R}^z`. Dynkin's identity at the bounded stopping time `tau<=n` gives

\[
\mathbb E_0H_R(X_\tau)-H_R(0)
=
\mathbb E_0\sum_{j<\tau}(PH_R-H_R)(X_j)
=-\mathbb E_0\sum_{j<\tau}w_R(X_j).
\]

Thus the local derivative has an exact endpoint representation.

### Theorem 2.1 (terminal-potential representation)

Pathwise in the scenery,

\[
\boxed{
-\partial_{\lambda+}F_{n,w_R}(\lambda;z)
=H_R(0)-\mathbb E_0H_R(X_{\tau_{\lambda,w_R}^z}).
}
\tag{2.4}
\]

After averaging the scenery,

\[
\boxed{
\chi_{n,w_R}(\lambda)
=H_R(0)-\mathbb E_{\zeta,0}H_R(X_{\tau_{\lambda,w_R}^{\zeta}}).
}
\tag{2.5}
\]

Consequently

\[
\boxed{
A_{n,w_R}(0)-A_{n,w_R}(\Lambda)
=
\int_0^\Lambda
\left[
H_R(0)-\mathbb E_{\zeta,0}H_R(X_{\tau_{s,w_R}^{\zeta}})
\right]ds.
}
\tag{2.6}
\]

Equation (2.6) is the desired local bridge in an exact potential-theoretic language: the interpolation loss is controlled entirely by where the optimal stopped path terminates in the potential `H_R`.

### 2.2 Equivalent source-sink flow identity

For a fixed stopping rule `tau`, put

\[
\mu(x)=\mathbb E_0\sum_{j<\tau}{\bf1}_{\{X_j=x\}},
\qquad
q(y)=\mathbb P_0(\tau>0,\ X_\tau=y),
\qquad
c=\mathbb P_0(\tau>0).
\tag{2.7}
\]

Counting every transition once gives

\[
\boxed{
(I-P)\mu=c\,\delta_0-q.
}
\tag{2.8}
\]

Indeed `mu P` counts all arrivals at times `1,...,tau`, while `mu` counts the initial visit when `tau>0` and arrivals only through time `tau-1`. Since `mu` has finite support in the time-`n` reachable ball, convolution with the transient Green kernel yields

\[
\boxed{
\mu(x)=cG(0,x)-\sum_yq(y)G(y,x).
}
\tag{2.9}
\]

Pairing (2.9) with `w_R` gives

\[
\sum_xw_R(x)\mu(x)
=cH_R(0)-\sum_yq(y)H_R(y),
\tag{2.10}
\]

which is exactly (2.4), because on `tau=0` one has `X_tau=0`.

This exposes the missing cancellation explicitly: the raw source term `H_R(0)~log R` is reduced only by the terminal sink `q`.

## 3. The inverse-square potential records logarithmic terminal radius

The standard five-dimensional Green asymptotic has the form

\[
G(0,x)=a_5|x|^{-3}+O(|x|^{-5}),
\qquad |x|\to\infty,
\tag{3.1}
\]

with `a_5>0`. Let

\[
\kappa_5=a_5|S^4|>0.
\tag{3.2}
\]

### Proposition 3.1 (critical convolution geometry)

Uniformly for `R>=4` and `y in Z^5`,

\[
\boxed{
H_R(0)-H_R(y)
=
\kappa_5\log\!\bigl(1+\min\{|y|,R\}\bigr)+O(1),
}
\tag{3.3}
\]

where the `O(1)` constant is independent of `R` and `y`.

#### Proof

First,

\[
H_R(0)
=\sum_{|x|<R}G(0,x)(1+|x|^2)^{-1}
=\kappa_5\log R+O(1).
\tag{3.4}
\]

Indeed the main term is `a_5 sum_{1<=|x|<R}|x|^{-5}=a_5|S^4|log R+O(1)`, while the Green-asymptotic error and the replacement of `(1+|x|^2)^(-1)` by `|x|^{-2}` are absolutely summable.

Now put `r=1+|y|` and first suppose `2r<=R/2`. Split the sum defining `H_R(y)` into `|x|<=2r` and `2r<|x|<R`.

On `|x|<=2r`, split again into `|x-y|<=r/2` and its complement. In the first part, `w_R(x)<=Cr^{-2}` and

\[
\sum_{|x-y|<=r/2}G(y,x)\le Cr^2,
\]

so the contribution is `O(1)`. In the complement, `G(y,x)<=Cr^{-3}` while

\[
\sum_{|x|<=2r}(1+|x|^2)^{-1}\le Cr^3,
\]

again giving `O(1)`.

For `|x|>2r`, one has `|x-y|=|x|(1+O(r/|x|))`. Using (3.1),

\[
G(y,x)=a_5|x|^{-3}+O(r|x|^{-4})+O(|x|^{-5}).
\tag{3.5}
\]

After multiplication by `(1+|x|^2)^(-1)` and summation over shells, the first error contributes

\[
O\left(r\sum_{m>=2r}m^4m^{-6}\right)=O(1),
\]

and the second is summable. Therefore

\[
H_R(y)=\kappa_5\log(R/r)+O(1).
\tag{3.6}
\]

Combining (3.4) and (3.6) gives

\[
H_R(0)-H_R(y)=\kappa_5\log r+O(1)
\]

whenever `r<=R/4`.

If `r>R/4`, a scale-invariant convolution estimate gives `H_R(y)=O(1)`: when `|y|<=2R`, rescale the two singular factors on the single scale `R` and split near `0` and near `y` exactly as above; when `|y|>2R`, use `G(y,x)<=C|y|^{-3}` and `sum_{|x|<R}w_R(x)<=CR^3`. Hence `H_R(y)=O(1)` for `r>R/4`, and (3.4) yields (3.3) there as well. The finitely many cases `|y|=O(1)` are absorbed into the uniform `O(1)`. ∎

Combining Theorem 2.1 with Proposition 3.1 gives the sharpest conceptual reduction of this run.

### Corollary 3.2 (susceptibility equals expected logarithmic terminal scale)

Uniformly in `n`, `R`, and `lambda`,

\[
\boxed{
\chi_{n,w_R}(\lambda)
=
\kappa_5\,
\mathbb E_{\zeta,0}
\log\!\bigl(1+\min\{|X_{\tau_{\lambda,w_R}^{\zeta}}|,R\}\bigr)
+O(1).
}
\tag{3.7}
\]

Thus the critical `log R` is not merely a Green-power count. It is, up to an additive constant, the expected **logarithmic terminal radius of the Bellman-optimal stopped path** under the localized inverse-square penalty.

In particular:

- bounded terminal scale forces bounded inverse-square susceptibility;
- terminal scale `R^{Theta(1)}` produces susceptibility of order `log R`;
- the source-level slowly varying question is therefore tied to localization/delocalization of the terminal sink in (2.9), not only to the raw scenery tail.

## 4. B25 — count the derivative twice using the Weibull score

The smooth recovery law allows a second exact representation of the same susceptibility.

Let

\[
V(t)=|t|^{5/2},
\qquad
\psi(t)=V'(t)=\frac52\operatorname{sgn}(t)|t|^{3/2},
\qquad
\sigma_\psi^2=\mathbb E\psi(\zeta(0))^2.
\tag{4.1}
\]

For a fixed finite horizon and fixed `lambda`, ties between two distinct policy occupation vectors occur on a finite union of nontrivial affine hyperplanes in the reachable scenery coordinates. Since the product law has a density, this has probability zero. Hence `F_{n,h}(lambda;zeta)` is almost surely differentiable in every scenery coordinate and

\[
\partial_{\zeta(x)}F_{n,h}(\lambda;\zeta)
=\mu_{\lambda,h}^{\zeta}(x)
\tag{4.2}
\]

for the unique optimal occupation vector (uniqueness here means uniqueness of the occupation vector; policies with the same vector are immaterial).

The one-dimensional density is proportional to `e^{-V}`. Since `F` is Lipschitz in each coordinate and the density is super-exponential, integration by parts has no boundary term and gives

\[
\boxed{
 m_{\lambda,h}(x)
:=\mathbb E\mu_{\lambda,h}^{\zeta}(x)
=
\mathbb E\left[(F_{n,h}(\lambda;\zeta)-A_{n,h}(\lambda))\psi(\zeta(x))\right].
}
\tag{4.3}
\]

Here `E psi(zeta(x))=0` by symmetry. Therefore

\[
\boxed{
\chi_{n,h}(\lambda)
=\sum_xh(x)m_{\lambda,h}(x)
=
\operatorname{Cov}\left(
F_{n,h}(\lambda;\zeta),
\sum_xh(x)\psi(\zeta(x))
\right).
}
\tag{4.4}
\]

This is the second count promised by B25: the same local derivative is both a stopped occupation and a first-score covariance.

### Proposition 4.1 (uniform first-score energy bound)

There is a finite law-dependent constant `C_occ`, independent of `n`, `lambda`, and `h`, such that

\[
\boxed{
\sum_x m_{\lambda,h}(x)^2\le C_{\rm occ}.
}
\tag{4.5}
\]

#### Proof

The normalized coordinate scores

\[
e_x=\psi(\zeta(x))/\sigma_\psi
\]

form an orthonormal family in the product `L^2` space: they are centered, have norm one, and are independent across distinct sites. By Bessel's inequality and (4.3),

\[
\sum_xm_{\lambda,h}(x)^2
\le
\sigma_\psi^2\operatorname{Var}(F_{n,h}(\lambda;\zeta)).
\tag{4.6}
\]

The previous run proved a finite one-site log-Sobolev constant for (1.1), hence in particular a finite Poincare constant `C_P`, and tensorization gives

\[
\operatorname{Var}(F)
\le C_P\mathbb E\sum_x|\partial_xF|^2.
\tag{4.7}
\]

For every optimal stopping rule, `0<=mu(x)<=g_n(0,x)`. Therefore

\[
\sum_x|\partial_xF|^2
=\sum_x\mu(x)^2
\le\sum_xg_n(0,x)^2
\le G_{2,5}<\infty,
\tag{4.8}
\]

where the last uniform bound was proved in the previous run. Thus (4.5) holds with

\[
C_{\rm occ}=\sigma_\psi^2C_PG_{2,5}.
\]
∎

There is also the pointwise deterministic domination

\[
\boxed{
0\le m_{\lambda,h}(x)\le g_n(0,x)\le G(0,x).
}
\tag{4.9}
\]

Hence for every nonnegative finitely supported `h`,

\[
\chi_{n,h}(\lambda)
\le
\min\left\{
C_{\rm occ}^{1/2}\|h\|_2,
\sum_xh(x)G(0,x)
\right\}.
\tag{4.10}
\]

For the inverse-square profile, the Green bound is the better critical estimate:

\[
\boxed{
\chi_{n,w_R}(\lambda)\le C(1+\log R).
}
\tag{4.11}
\]

Consequently

\[
\boxed{
A_{n,w_R}(0)-A_{n,w_R}(\Lambda)
\le C\Lambda(1+\log R).
}
\tag{4.12}
\]

At the previously identified critical opacity scale

\[
\Lambda\asymp \frac b{\log b},
\qquad
R\asymp\sqrt{\frac b{\log b}},
\tag{4.13}
\]

(4.12) is exactly of order `b`. The localized interpolation route is therefore **critical-scale matched**: the generic influence estimates neither lose an extra power nor produce the strict gain needed to decide the log-log correction.

## 5. A no-go theorem for the current generic first-order information

The new first-score estimate is strong but, by itself, cannot remove the logarithm.

Let dyadic shells be

\[
D_k=\{x:2^k\le|x|<2^{k+1}\},
\]

and write

\[
M_k=\sum_{x\in D_k}m(x),
\qquad
\theta_k=2^{-2k}M_k.
\tag{5.1}
\]

On `D_k`, `w_R(x)\asymp2^{-2k}`, so the shell contribution to inverse-square susceptibility is comparable to `theta_k`. Green domination gives

\[
M_k\le C2^{5k}2^{-3k}=C2^{2k},
\qquad
\boxed{\theta_k\le C.}
\tag{5.2}
\]

On the other hand, if `E_k=sum_{D_k}m(x)^2`, Cauchy-Schwarz gives

\[
E_k\ge\frac{M_k^2}{|D_k|}
\ge c\theta_k^2 2^{-k}.
\tag{5.3}
\]

The weights `2^{-k}` are summable. Therefore the uniform `l^2` estimate (4.5) is perfectly compatible with `theta_k` being bounded below by a positive constant on **every** dyadic scale. Such a profile contributes `Theta(log R)` to (4.11).

This compatibility is not merely formal. For sufficiently small fixed `c>0`, the comparison profile

\[
m^*(x)=cG(0,x)
\tag{5.4}
\]

satisfies both generic constraints

\[
0\le m^*\le G,
\qquad
\sum_xm^*(x)^2\le C_{\rm occ},
\tag{5.5}
\]

because `G(0,.) in l^2(Z^5)`, while

\[
\sum_xw_R(x)m^*(x)=\Theta(\log R).
\tag{5.6}
\]

### Proposition 5.1 (proof-architecture barrier)

No argument that uses only

1. the pointwise occupation domination `m<=G`, and
2. the uniform first-score/`l^2` bound `sum m^2<=C_occ`

can imply `chi_{n,w_R}=o(log R)` uniformly. An additional Bellman-specific constraint is mathematically necessary.

This proposition is a limitation of those two pieces of information, not a claim that the actual Bellman occupation equals the comparison profile (5.4).

The source-sink formula (2.9) says exactly what extra structure has been omitted: actual Bellman occupation is

\[
m=cG-G*\bar q,
\tag{5.7}
\]

where `\bar q` is the annealed terminal sink measure. The missing theorem must control that cancellation across scales.

## 6. What moved mathematically, and what did not

The frozen source metric is

`M_crit(5)` = width of the proved interval containing all subsequential logarithmic exponents `log E[u_t(0)]/log log t` at the admitted critical endpoint.

Before this run: `M_crit(5)=0`.  
After this run: `M_crit(5)=0`.  
Movement: **NO MOVEMENT**.

The run nevertheless proves three new source-relevant structural statements in the smooth endpoint recovery law:

1. the exact localized amplitude derivative with correct tie handling, (1.6)--(1.10);
2. the exact Green-potential/source-sink representation (2.4)--(2.10), with inverse-square susceptibility equal up to `O(1)` to expected logarithmic terminal radius, (3.7);
3. the exact Weibull score representation and a uniform first-score `l^2` bound, together with a proof that these generic constraints alone cannot remove the critical `log R`.

The exact remaining mathematical blocker is now narrower than in the previous report:

> **Terminal-sink localization problem.** For the source-relevant critical localized deformation, prove enough concentration/localization of the optimal terminal measure `q` to force
> \[
> \mathbb E\log(1+\min\{|X_\tau|,R\})=o(\log R)
> \]
> (or prove a matching positive fraction of `log R`, which would support a genuine slowly varying correction).

This is a Bellman/contact-set statement. Raw Green estimates, generic product concentration, and first-score energy bounds do not decide it.

## 7. Dated source/literature check — 2026-09-18

Fresh checks on 2026-09-18 returned:

- Ahmed Bou-Rabee and Christoforos Panagiotis, *Sharpness and critical scaling of parking*, arXiv:2609.02820, submitted 2 September 2026: `https://arxiv.org/abs/2609.02820`;
- Ahmed Bou-Rabee and Christoforos Panagiotis, *Quantitative explosion and percolation of the divisible sandpile*, arXiv:2609.02829, submitted 2 September 2026: `https://arxiv.org/abs/2609.02829`; its current abstract still describes the `d>=5` rate as tail-dependent;
- Ahmed Bou-Rabee, Yuval Peres and Ecaterina Sava-Huss, *Divisible sandpiles via random walks in random scenery*, arXiv:2604.13968, submitted 15 April 2026, remains the nearest general optimal-stopping analogue recovered in the bounded search.

A bounded search on the exact source IDs/titles/authors together with `gamma=d/2`, `borderline`, `critical tail`, `odometer`, and follow-up terms did not surface a later source-matching theorem resolving the endpoint. This is **negative evidence only**, not a novelty certificate or proof of worldwide openness.

## 8. Protocol state

This is the **third consecutive ordinary no-movement run after STUCK1**. Under the owner protocol, the next R7-06 iteration must therefore be **STUCK2: a thinking-only diagnosis**, not another ordinary lemma/checker run. STUCK2 must state the exact blocking formula, all failed recovery routes, the missing ingredient, the simplest unresolved case, and the nearest solved analogue, then select exactly one recovery action and three next Section-B methods.

HARD recovery count remains `1/2` until that diagnosis is actually performed. No handoff or rotation occurs in this artifact.
