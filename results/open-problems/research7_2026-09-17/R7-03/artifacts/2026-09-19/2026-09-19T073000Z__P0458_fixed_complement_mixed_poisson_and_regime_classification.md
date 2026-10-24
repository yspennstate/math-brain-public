Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise.** No authenticated runtime model/effort telemetry or binding selector was exposed.

# P0458 — fixed-complement boundary law and regime-complete standardized-degree classification

Source target: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (2026), §1.1, first additional question: characterize the limiting distribution of

\[
\frac{D-\mathbb E D}{\sqrt{\operatorname{Var}D}}
\]

for the degree `D` of a vertex in `LK(n,k)`.

Canonical target: `P0458`.  
Worker: `R7-03`.  
Status before this artifact: PARTIAL, with the interior growing regime `k→∞, n-k→∞` proved in `2026-09-19T070300Z__P0458_full_interior_growth_degree_law.md` and the dense boundary `n-1-k=O(1)` still open.  
Frozen metric before: `R_unresolved=1`.

This artifact proves the dense boundary completely, shows that the boundary laws are mixed Poisson and genuinely depend on the finite complement, glues them back to the interior law as the complement tends to infinity, and gives the resulting regime classification. The source-level mathematical endpoint is therefore reached, subject to independent proof audit and packaging.

The three Section-B methods used here are:

- **B29 ADD THE POINTS AT INFINITY:** zoom into the upper score endpoint by the coordinate `y=n(1-U)`;
- **B30 ONE SCALE / ONE DIRECTION AT A TIME:** localize all dependence to finitely many upper-tail candidate edges and show their shared edges disappear at scale `1/n`;
- **B7 TAKE THE LIMIT:** identify the limiting marked Poisson process and then let the finite complement `r` itself grow to recover the interior non-Gaussian law.

These differ from the immediately previous P0458 triple B18/B25/B3.

---

## 1. Model and exact deficit representation at fixed complement

Use the equivalent score orientation in which all undirected edge scores

\[
U_{ij}=U_{ji}\sim \operatorname{Uniform}(0,1)
\]

are independent and **smaller is preferred**. Vertex `i` proposes its `k` incident edges of smallest score, and `(i,j)` is retained iff both endpoints propose it.

Fix the root `0`. For a fixed integer

\[
r\ge 1,
\]

put

\[
k=n-1-r.
\]

Thus every vertex rejects exactly its `r` incident edges of **largest** score.

Let `D_n` be the degree of the root. The root itself rejects exactly `r` edges. Among the other `k` root-proposed edges, some are rejected by their opposite endpoint. Let

\[
H_n:=k-D_n.
\]

Then `H_n` is exactly the number of root-proposed edges which fail bilateral acceptance, and

\[
D_n=k-H_n.
\]

For each `i≠0`, introduce the upper-tail coordinate

\[
Y_i^{(n)}:=n(1-U_{0i}).
\]

Large edge scores correspond to small `Y` values. Let

\[
A_{n,r}:=\text{the }r\text{th smallest value among }\{Y_i^{(n)}:i\ne0\}.
\]

Since ties have probability zero, the root rejects precisely the `r` edges corresponding to the `r` smallest `Y` values. Hence the root proposes `(0,i)` iff

\[
Y_i^{(n)}>A_{n,r}.
\]

Now let `J_i^{(n)}` be the indicator that endpoint `i` rejects the root edge `(0,i)`. If `Y_i^{(n)}=y`, then

\[
U_{0i}=1-y/n.
\]

Endpoint `i` rejects `(0,i)` iff this edge is among its `r` largest incident scores, i.e. iff at most `r-1` of its `n-2` other incident scores exceed `U_{0i}`. Therefore, exactly,

\[
\mathbb P(J_i^{(n)}=1\mid Y_i^{(n)}=y)
=b_{n,r}(y),
\]

where

\[
b_{n,r}(y):=
\mathbb P\{\operatorname{Bin}(n-2,y/n)\le r-1\},
\qquad 0\le y\le n.
\]

Consequently

\[
\boxed{
H_n=\sum_{i\ne0}{\bf 1}_{\{Y_i^{(n)}>A_{n,r}\}}J_i^{(n)}.
}
\tag{1.1}
\]

The problem is now a marked upper-tail point-process problem.

---

## 2. B29 — the upper endpoint becomes a Poisson point process

Define the unmarked root point process

\[
\Pi_n:=\sum_{i\ne0}\delta_{Y_i^{(n)}}.
\]

Because the `Y_i^{(n)}` are independent with density `1/n` on `(0,n)`, for each bounded Borel set `B⊂(0,∞)`,

\[
\#\{i:Y_i^{(n)}\in B\}\sim
\operatorname{Bin}(n-1, |B|/n).
\]

Thus

\[
\Pi_n\Longrightarrow \Pi,
\]

where `Π` is a rate-one Poisson point process on `(0,∞)`.

Let `A_r` be the `r`th arrival time of `Π`. Then

\[
A_{n,r}\Longrightarrow A_r,
\qquad
A_r\sim \operatorname{Gamma}(r,1).
\tag{2.1}
\]

Define

\[
p_r(y):=e^{-y}\sum_{j=0}^{r-1}\frac{y^j}{j!}.
\tag{2.2}
\]

For every fixed `y`, the binomial-to-Poisson limit gives

\[
b_{n,r}(y)\longrightarrow p_r(y).
\]

Equivalently, if `G_r∼Gamma(r,1)`, then

\[
p_r(y)=\mathbb P(G_r>y).
\tag{2.3}
\]

The remaining issue is that the marks `J_i^{(n)}` are not exactly independent: for two candidate vertices `i,j`, both rejection decisions inspect the shared edge `(i,j)`. The next lemma shows that this is the **only** local dependence and vanishes in the bounded upper-tail window.

---

## 3. B30 — finite-window marked-process lemma

### Lemma 3.1 (asymptotically independent rejection marks on every bounded upper-tail window)

Fix `L<∞` and an integer `m≥1`. Consider `m` distinct root-neighbor labels `i_1,...,i_m`, and condition on

\[
Y_{i_a}^{(n)}=y_a\in[0,L],
\qquad a=1,\ldots,m.
\]

Then, uniformly for `(y_1,...,y_m)∈[0,L]^m`, the vector

\[
(J_{i_1}^{(n)},\ldots,J_{i_m}^{(n)})
\]

converges in law to independent Bernoulli variables with success probabilities

\[
p_r(y_1),\ldots,p_r(y_m).
\]

#### Proof

Remove, temporarily, the `\binom m2` edges whose two endpoints both belong to the candidate set `I={i_1,...,i_m}`.

For candidate `i_a`, the number of remaining non-root incident edges whose score exceeds its root-edge score is

\[
C_a^{(n)}\sim
\operatorname{Bin}(n-m-1,y_a/n).
\]

The variables `C_1^{(n)},...,C_m^{(n)}` are independent because after the candidate-candidate edges have been removed they are functions of disjoint collections of independent edge scores. Uniformly for `y_a∈[0,L]`,

\[
C_a^{(n)}\Longrightarrow \operatorname{Poisson}(y_a).
\]

The removed candidate-candidate edges can affect the mark at endpoint `i_a` only if one of them has score larger than

\[
U_{0i_a}=1-y_a/n.
\]

For one internal edge `(i_a,i_b)`, the probability that it exceeds at least one of the two relevant thresholds is at most

\[
\frac{\max(y_a,y_b)}{n}\le \frac Ln.
\]

Therefore

\[
\mathbb P\{\text{some internal candidate edge affects some mark}\}
\le \binom m2\frac Ln
=o(1),
\]

uniformly on `[0,L]^m`.

On the complementary event, candidate `i_a` rejects the root edge iff

\[
C_a^{(n)}\le r-1.
\]

Hence the joint law factorizes asymptotically, with limiting success probability

\[
\mathbb P\{\operatorname{Poisson}(y_a)\le r-1\}=p_r(y_a).
\]

This proves the lemma. ∎

### Corollary 3.2 (marked Poisson convergence on compacts)

Let

\[
\mathcal M_n:=\sum_{i\ne0}J_i^{(n)}\delta_{Y_i^{(n)}}.
\]

Jointly with `Π_n`, the marked process `\mathcal M_n` restricted to every compact interval `[0,L]` converges to the following marking of `Π`:

- conditional on `Π`, a point at position `y` receives mark `1` independently with probability `p_r(y)`;
- different points receive independent marks.

This follows from the usual factorial-moment characterization of a marked Poisson process: the root point locations contribute the standard binomial-to-Poisson factorial intensities, while Lemma 3.1 gives the required uniform factorization of every fixed finite collection of marks.

---

## 4. Removing the finite-window cutoff

For `L>0`, define the truncated deficit

\[
H_{n,L}:=
\sum_{i\ne0}
{\bf 1}_{\{A_{n,r}<Y_i^{(n)}\le L\}}J_i^{(n)}.
\]

By Corollary 3.2 and the continuous mapping theorem,

\[
H_{n,L}\Longrightarrow H_{r,L},
\]

where `H_{r,L}` is the number of marked points of the limiting process in `(A_r,L]`.

It remains to show that marked points with `Y>L` contribute negligibly, uniformly in `n`.

For fixed `r` and all sufficiently large `n`, for `0≤y≤n` we have

\[
\begin{aligned}
b_{n,r}(y)
&=\sum_{j=0}^{r-1}
\binom{n-2}{j}(y/n)^j(1-y/n)^{n-2-j}\\
&\le e^{-y/2}\sum_{j=0}^{r-1}\frac{y^j}{j!}.
\end{aligned}
\tag{4.1}
\]

Indeed `\binom{n-2}{j}(y/n)^j≤y^j/j!`, and for fixed `r` and large `n`, `n-2-j≥n/2`, so

\[
(1-y/n)^{n-2-j}\le e^{-(n-2-j)y/n}\le e^{-y/2}.
\]

Ignoring the root-selection indicator can only increase the count. Therefore

\[
\begin{aligned}
\mathbb E(H_n-H_{n,L})_+
&\le \sum_{i\ne0}
\mathbb E[ J_i^{(n)}{\bf1}_{\{Y_i^{(n)}>L\}}]\\
&=\frac{n-1}{n}\int_L^n b_{n,r}(y)\,dy\\
&\le
\int_L^\infty
 e^{-y/2}\sum_{j=0}^{r-1}\frac{y^j}{j!}\,dy.
\end{aligned}
\tag{4.2}
\]

The last expression tends to zero as `L→∞`, uniformly in `n`.

The same tail bound holds for the limiting process because `p_r(y)≤e^{-y/2}\sum_{j<r}y^j/j!` for all sufficiently large `y`.

Hence the truncation may be removed:

\[
\boxed{H_n\Longrightarrow H_r.}
\tag{4.3}
\]

---

## 5. Exact limiting law: a Gamma-mixed Poisson variable

Conditional on `A_r=a`, the points of the rate-one Poisson process after `a` form an independent rate-one Poisson process on `(a,∞)`. Independent thinning at location `y` with probability `p_r(y)` therefore gives

\[
H_r\mid A_r=a
\sim \operatorname{Poisson}(\Lambda_r(a)),
\tag{5.1}
\]

where

\[
\Lambda_r(a):=\int_a^\infty p_r(y)\,dy.
\]

Using

\[
p_r(y)=e^{-y}\sum_{j=0}^{r-1}\frac{y^j}{j!}
\]

and the integer incomplete-gamma identity,

\[
\int_a^\infty e^{-y}\frac{y^j}{j!}\,dy
=e^{-a}\sum_{\ell=0}^{j}\frac{a^\ell}{\ell!},
\]

we obtain the explicit polynomial form

\[
\boxed{
\Lambda_r(a)
=e^{-a}\sum_{\ell=0}^{r-1}
(r-\ell)\frac{a^\ell}{\ell!}.
}
\tag{5.2}
\]

Thus the fixed-complement boundary law is completely characterized by

\[
\boxed{
A_r\sim\operatorname{Gamma}(r,1),
\qquad
H_r\mid A_r\sim\operatorname{Poisson}(\Lambda_r(A_r)).
}
\tag{5.3}
\]

Equivalently, its probability generating function is

\[
\boxed{
\mathbb E[s^{H_r}]
=\frac1{(r-1)!}
\int_0^\infty
 a^{r-1}e^{-a}
 \exp\!\bigl(-(1-s)\Lambda_r(a)\bigr)\,da,
\qquad 0\le s\le1.
}
\tag{5.4}
\]

---

## 6. First two moments converge, so standardization is legitimate

Distributional convergence alone is not enough to standardize. We therefore record the moment argument explicitly.

For two distinct candidate vertices `i,j`, condition on their upper-tail coordinates `Y_i=y`, `Y_j=z`, and then condition on their unique shared non-root edge `W=U_{ij}`. Given `W`, the two endpoint-rejection events are independent, because their remaining edge sets are disjoint.

Let

\[
c_{n,r}(y):=
\mathbb P\{\operatorname{Bin}(n-3,y/n)\le r-1\}.
\]

For every fixed value of `W`, the conditional probability that endpoint `i` rejects the root edge is at most `c_{n,r}(y)`: if `W` itself exceeds the root-edge threshold, the admissible outside count becomes `r-2`, which only decreases the probability. Hence

\[
\mathbb P(J_i^{(n)}=J_j^{(n)}=1\mid Y_i=y,Y_j=z)
\le c_{n,r}(y)c_{n,r}(z).
\tag{6.1}
\]

The same exponential-polynomial estimate as (4.1) bounds `c_{n,r}` uniformly by an integrable function of `y`.

Consequently:

1. the first-moment contribution from `Y>L` tends to zero uniformly by (4.2);
2. the second factorial-moment contribution from pairs for which at least one coordinate exceeds `L` is bounded by a constant times

\[
\left(\int_L^\infty e^{-y/2}\sum_{j<r}\frac{y^j}{j!}\,dy\right)
\left(\int_0^\infty e^{-z/2}\sum_{j<r}\frac{z^j}{j!}\,dz\right),
\]

which also tends to zero.

On `[0,L]^2`, Corollary 3.2 gives convergence of the first and second factorial moments. Letting `L→∞` therefore yields

\[
\mathbb E H_n\to \mathbb E H_r,
\qquad
\mathbb E[H_n(H_n-1)]\to
\mathbb E[H_r(H_r-1)].
\tag{6.2}
\]

Hence

\[
\boxed{
\operatorname{Var}(H_n)\to\operatorname{Var}(H_r).
}
\tag{6.3}
\]

Because `D_n=k-H_n`, the same variance is `Var(D_n)`.

---

## 7. Explicit mean and variance constants

Write

\[
\mu_r:=\mathbb E H_r,
\qquad
\nu_r:=\operatorname{Var}(H_r).
\]

Since `H_r` is mixed Poisson,

\[
\mu_r=\mathbb E\Lambda_r(A_r),
\qquad
\nu_r=\mu_r+\operatorname{Var}(\Lambda_r(A_r)).
\tag{7.1}
\]

### 7.1 Closed form for the mean

Let `A,B` be independent `Gamma(r,1)` variables. Since `p_r(y)=P(B>y)` and `1-p_r(y)=P(A≤y)`, Fubini gives

\[
\mu_r
=\int_0^\infty p_r(y)(1-p_r(y))\,dy
=\frac12\mathbb E|A-B|.
\tag{7.2}
\]

Now write

\[
S=A+B,\qquad Q=A/(A+B).
\]

The beta-gamma algebra gives independent

\[
S\sim\operatorname{Gamma}(2r,1),
\qquad
Q\sim\operatorname{Beta}(r,r).
\]

Thus

\[
\mathbb E|A-B|
=\mathbb E S\,\mathbb E|2Q-1|
=2r\,\mathbb E|2Q-1|.
\]

A one-line beta-density integration gives

\[
\mathbb E|2Q-1|
=\frac{\binom{2r}{r}}{4^r}.
\]

Therefore

\[
\boxed{
\mu_r
=r\frac{\binom{2r}{r}}{4^r}
=\frac{\Gamma(r+1/2)}{\sqrt\pi\,\Gamma(r)}.
}
\tag{7.3}
\]

### 7.2 Explicit finite sum for the mixing second moment

Set

\[
P_r(a):=\sum_{\ell=0}^{r-1}
(r-\ell)\frac{a^\ell}{\ell!},
\]

so that `Λ_r(a)=e^{-a}P_r(a)`. Since `A_r` has density `a^{r-1}e^{-a}/(r-1)!`,

\[
\mathbb E\Lambda_r(A_r)^2
=\frac1{(r-1)!}\int_0^\infty
 a^{r-1}e^{-3a}P_r(a)^2\,da.
\tag{7.4}
\]

Expanding the polynomial gives the exact finite sum

\[
\boxed{
M_{2,r}:=\mathbb E\Lambda_r(A_r)^2
=
\frac1{(r-1)!}
\sum_{\ell,m=0}^{r-1}
\frac{(r-\ell)(r-m)(r+\ell+m-1)!}
{\ell!\,m!\,3^{r+\ell+m}}.
}
\tag{7.5}
\]

Hence

\[
\boxed{
\nu_r=\mu_r+M_{2,r}-\mu_r^2>0.
}
\tag{7.6}
\]

The strict positivity is immediate because `H_r` is a nondegenerate mixed Poisson random variable.

---

## 8. Fixed-complement standardized-degree theorem

### Theorem 8.1

Fix an integer `r≥1` and put `k=n-1-r`. Then

\[
H_n=k-D_n\Longrightarrow H_r,
\]

with convergence of the first two moments, where `H_r` is given by (5.3). Therefore

\[
\mathbb E D_n
=k-\mu_r+o(1),
\tag{8.1}
\]

\[
\operatorname{Var}(D_n)
=\nu_r+o(1),
\tag{8.2}
\]

and

\[
\boxed{
\frac{D_n-\mathbb E D_n}
{\sqrt{\operatorname{Var}(D_n)}}
\Longrightarrow
L_r:=\frac{\mu_r-H_r}{\sqrt{\nu_r}}.
}
\tag{8.3}
\]

This is a discrete, non-Gaussian boundary law whose parameters depend on the fixed complement `r`.

---

## 9. Two explicit boundary laws and a no-universal-limit consequence

### `r=1`

Here

\[
\Lambda_1(a)=e^{-a},
\qquad A_1\sim\operatorname{Exp}(1).
\]

Therefore `e^{-A_1}∼Uniform(0,1)`, so

\[
H_1\mid V\sim\operatorname{Poisson}(V),
\qquad V\sim\operatorname{Uniform}(0,1).
\]

Moreover

\[
\mu_1=\frac12,
\qquad
M_{2,1}=\frac13,
\qquad
\boxed{\nu_1=\frac7{12}}.
\tag{9.1}
\]

### `r=2`

Here

\[
\Lambda_2(a)=e^{-a}(a+2),
\qquad A_2\sim\operatorname{Gamma}(2,1),
\]

and

\[
\mu_2=\frac34,
\qquad
M_{2,2}=\frac{22}{27},
\qquad
\boxed{\nu_2=\frac{433}{432}}.
\tag{9.2}
\]

The standardized laws `L_1` and `L_2` are different. A simple invariant is their finite upper endpoint, attained when `H_r=0` (which has positive probability):

\[
\sup\operatorname{supp}(L_r)=\frac{\mu_r}{\sqrt{\nu_r}}.
\]

For `r=1`, the square of this endpoint is

\[
\frac{(1/2)^2}{7/12}=\frac37,
\]

whereas for `r=2` it is

\[
\frac{(3/4)^2}{433/432}=\frac{243}{433}.
\]

These are unequal. Thus, for example, the sequence

\[
r_n=
\begin{cases}
1,&n\text{ even},\\
2,&n\text{ odd},
\end{cases}
\qquad
k_n=n-1-r_n,
\]

has **no single standardized-degree limit**: its even and odd subsequences converge to different laws.

This is important for the source wording. Since the source allows general `k=k(n)`, there cannot be one universal limiting law without specifying the asymptotic regime.

---

## 10. B7 — the fixed-complement family glues to the interior law as `r→∞`

The boundary family is not disconnected from the interior theorem. It converges to exactly the same continuous non-Gaussian law when the complement parameter itself tends to infinity.

Let

\[
A_r,G_r\stackrel{\text{iid}}\sim\operatorname{Gamma}(r,1).
\]

Since

\[
\Lambda_r(a)=\int_a^\infty \mathbb P(G_r>y)\,dy
=\mathbb E[(G_r-a)_+],
\]

we have

\[
\frac{\Lambda_r(A_r)}{\sqrt r}
=
\mathbb E\left[
\left.
\left(\frac{G_r-r}{\sqrt r}
      -\frac{A_r-r}{\sqrt r}
\right)_+
\right|A_r
\right].
\tag{10.1}
\]

The gamma central limit theorem and uniform integrability imply convergence in Wasserstein distance:

\[
\frac{G_r-r}{\sqrt r}\Longrightarrow Z',
\qquad
\frac{A_r-r}{\sqrt r}\Longrightarrow Z,
\]

with independent standard normals in the limit. Positive part is one-Lipschitz, so the conditional expectation in (10.1) converges to

\[
\mathbb E[(Z'-Z)_+\mid Z]
=
\phi(Z)-Z\Phi(-Z)
=g(-Z),
\]

where

\[
g(z)=\phi(z)+z\Phi(z).
\]

Because `-Z` is again standard normal,

\[
\frac{\Lambda_r(A_r)}{\sqrt r}
\Longrightarrow g(Z).
\tag{10.2}
\]

The mixed-Poisson noise is smaller. Conditional on `A_r`,

\[
\mathbb E[(H_r-\Lambda_r(A_r))^2\mid A_r]
=\Lambda_r(A_r).
\]

Using `\mu_r∼\sqrt{r/\pi}` from (7.3),

\[
\mathbb E\left[
\left(
\frac{H_r-\Lambda_r(A_r)}{\sqrt r}
\right)^2
\right]
=\frac{\mu_r}{r}
\longrightarrow0.
\]

Therefore

\[
\boxed{
\frac{H_r}{\sqrt r}\Longrightarrow g(Z).
}
\tag{10.3}
\]

The same gamma moment bounds give convergence of the first two moments, hence

\[
\frac{\mu_r}{\sqrt r}\to\frac1{\sqrt\pi},
\qquad
\frac{\nu_r}{r}\to
v:=\frac13+\frac{\sqrt3-2}{2\pi}.
\tag{10.4}
\]

Thus

\[
\boxed{
L_r\Longrightarrow
L_\infty:=
\frac{1/\sqrt\pi-g(Z)}{\sqrt v}
\qquad(r\to\infty),
}
\tag{10.5}
\]

which is exactly the interior growing-budget standardized law proved in the preceding R7-03 artifact. This supplies a consistency check across the corner `n→∞` first, then `r→∞`.

---

## 11. Regime-complete answer to the source degree-law question

The source asks for the limiting distribution of the standardized degree while allowing `k=k(n)`. The correct answer is a **regime classification**, not one universal law.

### Regime A: fixed finite `k=κ`

This is published prior art through the Erlang weighted tree local weak limit of Moharrami–Subramanian–Liu–Sundaresan. For deterministic `κ`, the limiting root degree `D_κ^{EWT}` is explicit. In the notation of their root degree formula,

\[
X_\kappa\sim\operatorname{Gamma}(\kappa+1,1),
\]

and conditional on `X_κ=x`,

\[
D_\kappa^{EWT}
\sim
\operatorname{Bin}\!\left(
\kappa,
\eta_\kappa(x)
\right),
\qquad
\eta_\kappa(x)=
\frac1x\int_0^x \overline F_\kappa(y)\,dy,
\]

where `\overline F_κ` is the survival function of `Gamma(κ,1)`. Since finite-graph degrees are bounded by `κ`, local weak convergence also gives convergence of first two moments. Therefore the standardized finite-`κ` law is the standardized EWT root-degree law. This is **KNOWN**, not claimed as new here.

### Regime B: `k→∞` and `n-k→∞`

The preceding R7-03 artifact proved

\[
\frac{k-D}{s_n}\Longrightarrow g(Z),
\qquad
s_n^2=\frac{k(n-k)}n,
\]

with first-two-moment convergence. Hence

\[
\boxed{
\frac{D-\mathbb ED}{\sqrt{\operatorname{Var}D}}
\Longrightarrow L_\infty
=
\frac{1/\sqrt\pi-g(Z)}{\sqrt v}.
}
\]

This includes sparse, proportional-density, and near-complete sequences whenever both `k` and `n-k` diverge.

### Regime C: fixed complement `r=n-1-k≥1`

Theorem 8.1 gives

\[
\boxed{
\frac{D-\mathbb ED}{\sqrt{\operatorname{Var}D}}
\Longrightarrow L_r
=
\frac{\mu_r-H_r}{\sqrt{\nu_r}},
}
\]

with `H_r` given by the Gamma-mixed Poisson law (5.3).

### Regime D: complete graph `k=n-1`

Then

\[
D=n-1
\]

deterministically, so

\[
\operatorname{Var}(D)=0.
\]

The standardized variable is undefined. This is a degenerate exception, not a missing probabilistic regime.

### Arbitrary sequences

Every integer sequence `k(n)` has subsequences falling into the classes above after, if necessary, passing to a further subsequence:

- bounded `k` has a constant-`κ` subsequence;
- unbounded `k` has a subsequence with `k→∞`;
- along `k→∞`, either `n-k→∞` or `r=n-1-k` is bounded;
- bounded integer `r` has a constant-`r` subsequence.

Therefore the preceding three nondegenerate families classify all subsequential standardized-degree limits. A full sequence need not converge if it moves between distinct boundary classes; the alternating `r=1,2` construction above is an explicit example.

This is the regime-complete characterization required by the P0458 admission record.

---

## 12. Literature and scope check, dated 2026-09-19

Controlling source:

- H. Dabirian and V. Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2), 552–579 (2026), published online 18 December 2025, DOI `10.1017/jpr.2025.10051`.
- Final Cambridge article URL: `https://www.cambridge.org/core/journals/journal-of-applied-probability/article/connectivity-of-a-family-of-bilateral-preference-random-graphs/0A1D5D7560AB2DC6C8255F1522DC3BB2`.

Fixed-`k` prior art:

- M. Moharrami, V. Subramanian, M. Liu, R. Sundaresan, *The Erlang weighted tree, a new branching process*, Random Structures & Algorithms 64 (2024), 537–624, DOI `10.1002/rsa.21180`. Their Theorem 5.1 gives the EWT root-degree distribution used above.

A bounded search through 2026-09-19 for the exact standardized-degree question, `LK(n,k)` degree variance/distribution, the paper title, and later Dabirian/Subramanian work recovered the final Cambridge paper and the EWT fixed-degree result, but no later paper stating the interior universal law or the fixed-complement mixed-Poisson classification above. This is negative evidence only. It does **not** certify novelty or worldwide openness.

---

## 13. Status and remaining non-mathematical obligations

The frozen mathematical metric moves

\[
\boxed{R_{\rm unresolved}:1\to0.}
\]

The source-level mathematical classification is now **PROVED**, combining:

1. published fixed-`k` EWT prior art;
2. the previous R7-03 theorem for all `k→∞, n-k→∞`;
3. the fixed-complement mixed-Poisson theorem proved here;
4. the explicit zero-variance complete-graph exception;
5. the subsequential classification showing why arbitrary `k(n)` need not have one universal limit.

Protocol closure is **not** yet claimed. Still required by the repository rules:

- dedicated citation-level prior-art review of the new boundary/interior mechanism;
- actual P26 independent full-proof audit;
- one distinct OTHER-track independent full-proof audit;
- a self-contained `paper_<name>/` package with proof/source-scope README.

No self-check or coordinator reconciliation is counted as either independent audit.
