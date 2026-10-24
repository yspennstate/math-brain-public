Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — Gini covariance sharpening and a three-degree offspring extension

**Status:** PROVED PARTIAL (new repository theorem candidates, not independently audited; no claim of external novelty; the full Lyons–Pemantle–Peres conjecture remains open here).

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `4425a137c14eeb0d7f05bda458b686f46117067f`.

## 1. Source convention, current published baseline, and continuity

Let `nu` be the Galton–Watson offspring variable. The source problem assumes a supercritical Galton–Watson tree without leaves:

\[
P(\nu=0)=0,\qquad m=E\nu>1.
\]

Ben Arous–Fribergh–Sidoravicius use the **outward child-bias** convention `beta`:

\[
P_\beta(x,x^*)=\frac1{1+\beta\nu(x)},\qquad
P_\beta(x,x_i)=\frac{\beta}{1+\beta\nu(x)}.
\]

The conjecture asks that the speed `v(beta)` increase throughout the transient interval `beta>1/m`. I use the reciprocal **parent-bias** parameter

\[
\lambda=1/\beta,
\]

so

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+\nu(x)},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+\nu(x)},
\]

and the conjectural direction is that `ell_lambda=v(1/lambda)` is nonincreasing on `0<=lambda<m`.

A bounded literature refresh on 20 September 2026 recovered no source-wide resolution beyond the current published source-uniform theorem of Song–Wang–Xiang, *Journal of Applied Probability* 62 (2025), DOI `10.1017/jpr.2024.113`: if the minimum offspring is `d>=2`, then `ell_lambda` is strictly decreasing for

\[
0\le \lambda\le \theta_d:=\frac{d}{1+\sqrt{1-1/d}}.
\tag{1.1}
\]

Bowditch–Tokushige (`arXiv:1906.07913`, `arXiv:2006.03433`) give differentiability/analyticity in the ballistic regime but not the missing sign. Aïdékon's speed representation remains the starting identity below.

Repository continuity used rather than re-derived:

* previous P03-A: `2026-09-20T0104Z__adjacent-two-point-weight-optimization.md`, proving every `{d,d+1}` mixture through `lambda<=d-1/4`, and `{2,3}` through `lambda=46/25`;
* P03-B: `2026-09-20T010909Z__sharp-regeneration-bound-and-score-response.md`, whose valid coupling/regeneration results include the repaired sharp deterministic bound `tau<=4B+1` and a score-response identity; I do not duplicate that coupling route;
* P01 bounded-support report `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T00-58-12Z__run-report.md`, which established a tilted-mean covariance bound and examples `2<=nu<=74` through `lambda=6/5` and `2<=nu<=12` through `lambda=4/3`.

The owner registry explicitly makes P03-A complementary; a one-time current ownership search was performed and no peer claim is taken or overwritten here.

The fixed full-source metric remains

`R_full = 1 -> 1`.

## 2. Exact effective-degree derivative identity for arbitrary bounded support

Assume for this run that

\[
d\le \nu\le D\quad\text{a.s.},\qquad 2\le d<D<\infty.
\tag{2.1}
\]

Fix `1<=lambda<d`. Let `B` be the escape probability from a vertex before hitting its parent. For conditional offspring value `n`, let `B_0,...,B_n` be iid copies and set

\[
S_n=\sum_{i=0}^n B_i,
\qquad
A_n=\lambda-1+S_n,
\qquad
c_n=E\left[\frac{S_n}{(n+1)A_n}\right].
\tag{2.2}
\]

Write `U=-B'>=0`, `T_n=sum_i U_i`. Direct differentiation gives

\[
h_n:=-c_n'
=E\left[\frac{S_n+(\lambda-1)T_n}{(n+1)A_n^2}\right],
\qquad
g_n:=\frac{h_n}{c_n}=-\frac{d}{d\lambda}\log c_n.
\tag{2.3}
\]

If `p_n=P(nu=n)` and

\[
C=\sum_n p_n c_n,
\qquad
\pi_n=\frac{p_n c_n}{C},
\qquad
M=\sum_n n\pi_n,
\tag{2.4}
\]

then Aïdékon's formula reduces to

\[
\boxed{\ell_\lambda=\frac{M-\lambda}{M+\lambda}},
\qquad
\boxed{\ell_\lambda'=\frac{2(\lambda M'-M)}{(M+\lambda)^2}}.
\tag{2.5}
\]

Differentiating the tilted weights gives the exact covariance identity

\[
M'=-\operatorname{Cov}_\pi(\nu,g_\nu)
=\sum_{n<m}\pi_n\pi_m(m-n)(g_n-g_m).
\tag{2.6}
\]

Thus all remaining work is to control how much the logarithmic sensitivity `g_n` can decrease with degree.

## 3. Uniform logarithmic-sensitivity envelopes

The standard escape estimates used in the 2025 proof give, for `lambda<d`,

\[
1-\frac\lambda d\le B\le1-\frac\lambda D,
\qquad
0\le U\le \frac{B}{d-\lambda}.
\tag{3.1}
\]

For a realization inside (2.3), divide its `h_n` integrand by its `c_n` integrand. The pointwise ratio is

\[
q_n^{\rm pt}
=\frac{1+(\lambda-1)T_n/S_n}{A_n}.
\tag{3.2}
\]

Since `lambda>=1`, (3.1) implies

\[
1\le 1+(\lambda-1)T_n/S_n
\le \frac{d-1}{d-\lambda}.
\tag{3.3}
\]

Also

\[
A_n\ge \lambda-1+(d+1)(1-\lambda/d)=d-\lambda/d,
\tag{3.4}
\]

and

\[
A_n\le \lambda-1+(D+1)(1-\lambda/D)=D-\lambda/D.
\tag{3.5}
\]

Because `g_n` is the positive `c_n`-integrand-weighted average of (3.2),

\[
\boxed{
q_-(\lambda):=\frac1{D-\lambda/D}
\le g_n\le
q_+(\lambda):=
\frac{d-1}{(d-\lambda)(d-\lambda/d)}
}
\tag{3.6}
\]

for every degree in the support.

For a whole interval `1<=lambda<=L<d`, `q_+` is increasing and `q_-` is increasing, hence the safe uniform oscillation bound

\[
g_n-g_m\le Q^*_{d,D}(L)
:=q_+(L)-q_-(1)
=
\frac{d-1}{(d-L)(d-L/d)}-rac{D}{D^2-1}.
\tag{3.7}
\]

This is inherited envelope information. The new step is to charge the covariance to the exact one-dimensional Gini dispersion of the tilted offspring law rather than to an endpoint-distance bound.

## 4. New lemma: exact Gini decomposition of the covariance loss

Define

\[
G(\pi):=\sum_{n<m}\pi_n\pi_m(m-n).
\tag{4.1}
\]

For `j=d,...,D-1`, put

\[
F_j:=\sum_{n\le j}\pi_n.
\]

Every pair `(n,m)` with `n<m` contributes one unit to `m-n` for exactly the cuts `j=n,...,m-1`. Therefore

\[
\boxed{
G(\pi)=\sum_{j=d}^{D-1}F_j(1-F_j).
}
\tag{4.2}
\]

Since `x(1-x)<=1/4`,

\[
\boxed{G(\pi)\le\frac{D-d}{4}.}
\tag{4.3}
\]

Equivalently, if `N,N'` are iid under the tilted law, then

\[
G(\pi)=\frac12E|N-N'|\le\frac{D-d}{4}.
\]

This is sharper in narrow support than the previous generic estimate

\[
G(\pi)\le \min(M-d,D-M).
\]

Indeed at a 50--50 mixture of the two endpoints, the old right side is `(D-d)/2`, while (4.3) is exactly `(D-d)/4`.

Combining (2.6), (3.7), and (4.3) yields

\[
M'\le Q^*_{d,D}(L)\frac{D-d}{4}
\tag{4.4}
\]

uniformly for `1<=lambda<=L`. Since `M>=d`,

\[
\lambda M'-M
\le
\frac{L(D-d)}4Q^*_{d,D}(L)-d.
\tag{4.5}
\]

Hence:

### Theorem 4.1 — narrow-support Gini covariance criterion

For any offspring law satisfying (2.1), if `1<L<d` and

\[
\boxed{
L(D-d)
\left[
\frac{d-1}{(d-L)(d-L/d)}-rac{D}{D^2-1}
\right]
<4d,
}
\tag{4.6}
\]

then `ell'_lambda<0` for every `1<=lambda<=L`. Combining with (1.1), which extends past `lambda=1`, proves strict decrease on the whole interval `0<=lambda<=L`.

If

\[
\delta_{d,D,L}:=
 d-
\frac{L(D-d)}4Q^*_{d,D}(L)>0,
\]

then the proof gives the explicit uniform margin

\[
\boxed{
\ell'_\lambda\le
-\frac{2\delta_{d,D,L}}{(D+L)^2}.
}
\tag{4.7}
\]

### Relation to the preceding P01 covariance certificate

The P01 endpoint-distance criterion with the same `Q^*` requires

\[
LQ^*(D-d)<D+d.
\]

The Gini criterion requires

\[
LQ^*(D-d)<4d.
\]

Thus the new criterion is strictly stronger whenever `D<3d`, exactly the narrow-support regime targeted here. This is a mechanism gain, not merely a new decimal endpoint.

## 5. First concrete removal of the two-point restriction: every law on `{2,3,4,5}` through `31/20`

Take

\[
d=2,\qquad D=5,\qquad L=\frac{31}{20}.
\]

Then

\[
q_+(L)=\frac{800}{441},
\qquad
q_-(1)=\frac5{24},
\qquad
Q^*=\frac{5665}{3528}.
\]

Therefore

\[
\delta_{2,5,31/20}
=2-rac{31}{20}\frac34\frac{5665}{3528}
=\frac{2509}{18816}>0.
\tag{5.1}
\]

Theorem 4.1 proves:

### Corollary 5.1

For **every** no-leaf offspring distribution supported in

\[
\{2,3,4,5\},
\]

with arbitrary masses on those four degrees, the biased-walk speed is strictly decreasing on

\[
\boxed{0\le\lambda\le\frac{31}{20}=1.55.}
\tag{5.2}
\]

On `1<=lambda<=31/20`, since `M<=5`, the explicit derivative certificate is

\[
\boxed{
\ell'_\lambda
\le -\frac{62725}{10090668}
<-6.21\times10^{-3}.
}
\tag{5.3}
\]

This is genuinely beyond the previous P03-A two-point family and is also deeper in bias than the broad P01 rectangle `2<=nu<=12` through `lambda=4/3`.

## 6. Degree-conditioned refinement: every law on `{2,3,4}` through `7/4`

The common-oscillation theorem deliberately forgets which degree produced which sensitivity. For the three-degree family one can retain that information and go substantially deeper.

Assume now only

\[
P(\nu\in\{2,3,4\})=1,
\qquad 1\le\lambda\le\frac74.
\tag{6.1}
\]

From (3.2) with minimum degree 2,

\[
g_n\le
\frac1{(2-\lambda)[\lambda-1+(n+1)(1-\lambda/2)]}.
\tag{6.2}
\]

Both factors in the denominator decrease in `lambda`, so at the endpoint

\[
g_2\le\frac{32}{9},
\qquad
g_3\le\frac{16}{5}.
\tag{6.3}
\]

For the lower bounds, use only `T_n>=0` and the upper escape bound `B<=1-\lambda/4`. Then

\[
g_n\ge
\frac1{\lambda-1+(n+1)(1-\lambda/4)}.
\tag{6.4}
\]

For `n=3` the denominator is exactly 3, while for `n=4` it is `4-\lambda/4<=15/4`. Hence

\[
g_3\ge\frac13,
\qquad
g_4\ge\frac4{15}.
\tag{6.5}
\]

Consequently, uniformly on (6.1),

\[
g_2-g_3\le\frac{29}{9},
\qquad
g_3-g_4\le\frac{44}{15},
\qquad
g_2-g_4\le\frac{148}{45}.
\tag{6.6}
\]

Let

\[
x=\pi_2,\qquad y=\pi_3,\qquad z=\pi_4,
\qquad x+y+z=1.
\]

By (2.6), (6.6), and `lambda<=7/4`,

\[
\lambda M'-M\le F(x,y,z),
\]

where

\[
F=
\frac74\left(
\frac{29}{9}xy+
\frac{44}{15}yz+
2\frac{148}{45}xz
\right)
-(2x+3y+4z).
\tag{6.7}
\]

Set `z=1-x-y`. Exact expansion gives

\[
F(x,y)=
-\frac{518}{45}x^2
-\frac{1981}{180}xy
-\frac{77}{15}y^2
+\frac{608}{45}x
+\frac{92}{15}y
-4.
\tag{6.8}
\]

Its Hessian is

\[
\begin{pmatrix}
-1036/45 & -1981/180\\
-1981/180 & -154/15
\end{pmatrix},
\]

whose determinant is

\[
\frac{3733751}{32400}>0.
\]

Thus `F` is strictly concave. Its unconstrained critical point has

\[
x=\frac{47088}{76199},
\qquad
y=-\frac{34688}{533393}<0,
\]

so the maximum on the probability triangle lies on its boundary.

The three boundary maxima are exact:

* `y=0`:
  \[
  \max F=-\frac{412}{11655}
  \quad\text{at }x=\frac{152}{259};
  \]
* `z=0`:
  \[
  \max F=-\frac{30575}{29232};
  \]
* `x=0`:
  \[
  \max F=-\frac{2504}{1155}.
  \]

Therefore the global maximum is the first one, and

\[
\boxed{
\lambda M'-M\le-\frac{412}{11655}<0
}
\tag{6.9}
\]

for **every** choice of the three offspring masses and every `1<=lambda<=7/4`.

### Theorem 6.1 — arbitrary `{2,3,4}` mixture

For every offspring law supported on `{2,3,4}`, with no restriction on the mixture probabilities,

\[
\boxed{
\ell_\lambda\text{ is strictly decreasing for }
0\le\lambda\le\frac74.
}
\tag{6.10}
\]

Since `M<=4`, (2.5) and (6.9) also give the uniform certificate

\[
\boxed{
\ell'_\lambda
\le
-\frac{13184}{6165495}
<-2.13\times10^{-3}
}
\tag{6.11}
\]

throughout `1<=lambda<=7/4`.

This is the run's strongest concrete theorem: the previous all-mixture P03-A result allowed only the two adjacent degrees `{2,3}` (though deeper, through `46/25`); the present theorem admits an arbitrary third degree 4 and still reaches `7/4`.

## 7. What moved and what remains

**Full-source metric:** `R_full: 1 -> 1`.

**Intermediate obligation ledger:**

* `O1` source convention/current source-uniform range: DONE.
* `O2` effective-degree reduction: DONE.
* `O3` nontrivial two-point family beyond the published cutoff: DONE previously.
* `O4` remove small-mixture restriction for `{2,3}`: DONE previously through `46/25`.
* `O4b` all adjacent two-point `{d,d+1}` laws: DONE previously through `d-1/4`.
* `O5` remove the two-point restriction: **MOVED SUBSTANTIALLY THIS RUN**. Theorem 4.1 gives an arbitrary bounded-support narrow-width criterion; Corollary 5.1 handles every law on `{2,3,4,5}` through `31/20`; Theorem 6.1 handles every law on `{2,3,4}` through `7/4`.
* `O6` arbitrary finite support with no width restriction: OPEN.
* `O7` minimum offspring 1 / full no-leaf source: OPEN.

No source-wide closure is claimed, and no peer's canonical ownership is changed.

## 8. Failed/limited route and exact next attack

A single common oscillation `q_+-q_-` still becomes too expensive when `D/d` is large. This is not a counterexample; it is the exact place where the current analytic proof loses the environment response.

The next attack is therefore not another endpoint calculation. Keep the pairwise covariance formula (2.6), but derive **degree-conditioned** envelopes `U_n(lambda),L_n(lambda)` for every `n`, then solve

\[
\sum_{n<m}\pi_n\pi_m(m-n)[U_n-L_m]
\]

by a cut decomposition or a monotone transport inequality instead of replacing all pairs by one worst oscillation. The three-degree calculation in Section 6 proves that this extra structure is quantitatively valuable. A second route is to combine the branch-addition inequalities for `c_{n+1}/c_n` with the tilted weights `pi_n`, so that the optimizer cannot freely place all tilted mass at the worst pair of degrees. Either route attacks `O6` directly and does not duplicate P03-B's coupling work.

The exact new remaining gap is: prove a support-independent upper bound on the pairwise sensitivity transport strong enough that

\[
\lambda M'(\lambda)<M(\lambda)
\]

for every finite offspring law, then pass by truncation/uniform integrability to the full no-leaf law under the source assumptions.
