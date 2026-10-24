Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `56 -> 57` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #9 RANDOMIZE, #10 DERANDOMIZE.**

# R07 CLOSABLE OUTSIDE — run 57: Gaussian-marginal dependent-pair gate canyons

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Target: Burdzy--Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.8 / intake I0077.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

Overall source status remains **PARTIAL**. New claims T79/T80 below are **SELF_CHECK_ONLY** pending the required two independent OTHER-track audits. Publication novelty remains **UNVERIFIED**.

## 1. Continuity, admission, ownership, and recovered state

I continued from the newest complete R07 report rather than restarting:

`runs/R07/20260919T0021Z_i0077_empirical_increment_law_galleries_56_eil56.md`.

Before new mathematics I re-read/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the searchable R07/I0077 report chain and the immutable old-KPZ handoff;
- newest neighboring R15 report `runs/R15/20260918_2358Z_successor_screen_f0111_adaptive_k2_w69s.md`, which explicitly keeps Burdzy--Scheutzow Problem 7.2 / I0076 retired-handed-off and does not reopen it;
- targeted intake/attempt/history searches for I0077 / arXiv:1302.6958 / Problem 7.8 and for dyadic increment, Gaussian-marginal, binary-tree and bifurcating-Markov-chain mechanisms.

`INDEX.md`/`RANKING.md` settle Burdzy--Scheutzow Problem 7.5, not 7.8. `POSTED.md` contains no exact Problem-7.8 closure. The canonical claim remains `PENDING_ADMISSION, not READY` while reserving I0077 exclusively to R07. I preserve that shared operational label and do not edit shared roots. The old R07 KPZ route remains preserved by immutable handoff and is not reopened or deleted.

The fixed metric is unchanged:

> number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new families.

Entering metric: **56**.  
Entering unchanged count: **0**.

Run 56 proved an obstruction whenever the one-step empirical law of normalized microscopic dyadic increments differs from `N(0,1)`. Its stated next frontier was exact Gaussian one-step marginals with non-Brownian microscopic dependence. This run crosses that frontier.

## 2. Primary source benchmark rechecked completely

The primary PDF was re-read at Definition 2.1, Remark 4.1, Theorem 4.3 and the open-problem page.

For an FBM `X`, Definition 2.1 supplies random witness times `S_j -> -infinity` a.s. such that for every fixed witness index

\[
B^{(j)}_t=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\tag{2.1}
\]

is an **unconditional standard Brownian motion**.

For the parabolic theorem, Burdzy--Scheutzow use

\[
\mathcal C=\{(c_1,c_2):-\infty\le c_1<c_2\le\infty\},
\qquad
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right),
\tag{2.2}
\]

with speed measure `m(dx)=2 exp(-x^2/2) dx`. For the Dirichlet Sturm--Liouville problem on `[c_1,c_2]`, `-lambda_0(c_1,c_2)` is the largest eigenvalue. Their Remark 4.1 records continuity and monotonicity of `lambda_0`.

Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM must asymptotically cross one of the parabolic boundaries, i.e. a.s. either
   \[
   \limsup_{t\to-\infty} X_t/\sqrt{|t|}\ge c_2
   \quad\text{or}\quad
   \liminf_{t\to-\infty} X_t/\sqrt{|t|}\le c_1;
   \]
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM with the reverse asymptotic inequalities;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM satisfying the exact all-negative-time confinement
   \[
   c_1\sqrt{|t|}\le X_t\le c_2\sqrt{|t|},\qquad t\le0,
   \]
   almost surely.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The following forward-Levy question is separately numbered Problem 7.9 and is not part of I0077.

## 3. Fresh current-literature / prior-art pass

Fresh bounded searches on 2026-09-19 used the exact paper title, arXiv id, exact Problem-7.8 wording, later-author/citation combinations, and combinations of `bifurcating Markov chain`, `binary tree empirical measure`, `Gaussian marginals`, `daughter dependence`, and `Wasserstein contraction`.

Relevant prior art recovered:

1. J. Guyon, *Limit theorems for bifurcating Markov chains. Application to the detection of cellular aging*, Ann. Appl. Probab. 17 (2007), arXiv:0710.5434. The framework uses a kernel `P(x,dy dz)` and explicitly permits the two daughters to be conditionally dependent; it proves LLNs/CLTs on binary trees.
2. S. V. Bitseki Penda, M. Escobar-Bach, A. Guillin, *Transportation cost-information and concentration inequalities for bifurcating Markov chains*, Bernoulli 23 (2017), arXiv:1501.06693. It develops concentration/deviation results under Wasserstein contraction.
3. Later BMC work, including the mother-daughters-triangle and `L^2`-ergodic CLTs, confirms that empirical statistics of child pairs are standard objects in that literature.

I use this literature as conceptual prior art for the random-tree derandomization step, **not** as a novelty claim. The proof below is self-contained for the special kernel actually used.

The bounded current searches did **not** surface an accessible later paper explicitly resolving exact Burdzy--Scheutzow Problem 7.8 or stating T79/T80 below. This is negative bounded evidence only and is **not** a worldwide novelty certificate.

## 4. Move #2 — attack the negation: Gaussian one-step increments do not force Brownian microscopic structure

Run 56 leaves open the tempting stronger assertion:

> once a deterministic gate trace has asymptotically standard-Gaussian one-step normalized dyadic increments, microscopic increment statistics can no longer obstruct Brownian gate confinement.

This is false. I construct a compatible binary refinement whose one-step empirical law is **exactly Gaussian in the limit**, while adjacent sibling increments converge to a non-product coupling of two standard Gaussians.

This refutes only the proposed stronger mechanism. It does **not** refute the source's open-ended Problem 7.8.

Let `gamma=N(0,1)` and define the bounded even mean-zero functions

\[
f(x)=\cos x-e^{-1/2},\qquad
 g(x)=\cos(2x)-e^{-2}.
\tag{4.1}
\]

Then

\[
\int f\,d\gamma=\int g\,d\gamma=0,
\quad \operatorname{Lip}(f)\le1,
\quad \operatorname{Lip}(g)\le2.
\tag{4.2}
\]

Put

\[
A(x,d)=f(x)g(d)-g(x)f(d),
\qquad \varepsilon=10^{-2}.
\tag{4.3}
\]

Since `||f||_infty<2` and `||g||_infty<2`,

\[
|A(x,d)|<8,
\tag{4.4}
\]

so

\[
1+\varepsilon A(x,d)>0
\tag{4.5}
\]

for all `x,d`. Define a joint law for `(X,D)` by

\[
\pi(dx,dd)=\gamma(dx)\gamma(dd)
\bigl[1+\varepsilon A(x,d)\bigr].
\tag{4.6}
\]

Both marginals are exactly `gamma`, because integration of the perturbation in either variable gives zero.

Now set

\[
Y_0=\frac{X+D}{\sqrt2},
\qquad
Y_1=\frac{X-D}{\sqrt2}.
\tag{4.7}
\]

The dyadic compatibility identity is automatic:

\[
Y_0+Y_1=\sqrt2 X.
\tag{4.8}
\]

### Lemma 4.1 — each child is exactly standard normal

Both `Y_0` and `Y_1` have law `gamma`.

#### Proof

Write

\[
F(t)=\int e^{itx}f(x)\,\gamma(dx),
\qquad
G(t)=\int e^{itx}g(x)\,\gamma(dx).
\tag{4.9}
\]

Because `f,g` are even and `gamma` is symmetric, `F,G` are even. For `a=t/\sqrt2`, the perturbation in the characteristic function of `Y_0` is

\[
\varepsilon\{F(a)G(a)-G(a)F(a)\}=0.
\tag{4.10}
\]

For `Y_1` it is

\[
\varepsilon\{F(a)G(-a)-G(a)F(-a)\}=0.
\tag{4.11}
\]

The unperturbed orthogonal transform of two independent standard normals is standard normal, so both child marginals are exactly `gamma`. QED.

Let `J` be the law of `(Y_0,Y_1)`. Orthogonal invariance of `gamma\otimes gamma` gives

\[
\frac{dJ}{d(\gamma\otimes\gamma)}(y_0,y_1)
=1+\varepsilon R(y_0,y_1),
\tag{4.12}
\]

where

\[
R(y_0,y_1)=
A\!\left(
\frac{y_0+y_1}{\sqrt2},
\frac{y_0-y_1}{\sqrt2}
\right).
\tag{4.13}
\]

The function `R` is bounded and Lipschitz. It is not identically zero because `f` and `g` are not proportional (they contain different Fourier frequencies). Also

\[
\mathbb E_{\gamma^2}R=0,
\qquad
\mathbb E_JR
=\varepsilon\,\mathbb E_{\gamma^2}R^2>0.
\tag{4.14}
\]

Hence

\[
\boxed{J\ne\gamma\otimes\gamma}
\tag{4.15}
\]

although **both** coordinates of `J` are standard normal and their normalized sum `(Y_0+Y_1)/\sqrt2=X` is also standard normal.

This is the exact obstruction the one-step test of run 56 cannot see.

## 5. A Brownian theorem for adjacent microscopic pairs

For a bounded Lipschitz `Phi:R^2->R`, standard Brownian motion `B`, `n=2^N`, and phase `theta>=0`, define

\[
\mathcal P_N(\theta;\Phi)
=\frac2n\sum_{j=0}^{n/2-1}
\Phi\!\left(
\sqrt n[B_{\theta+(2j+1)/n}-B_{\theta+2j/n}],
\sqrt n[B_{\theta+(2j+2)/n}-B_{\theta+(2j+1)/n}]
\right).
\tag{5.1}
\]

### Lemma 5.1 — uniform adjacent-pair empirical law over all phases

For every bounded Lipschitz `Phi` and finite `A`, almost surely,

\[
\boxed{
\sup_{0\le\theta\le A}
\left|
\mathcal P_N(\theta;\Phi)
-\mathbb E\Phi(Z_0,Z_1)
\right|\longrightarrow0,
}
\tag{5.2}
\]

where `Z_0,Z_1` are independent standard normals. One probability-one event works for all integer `A>=1`.

### Proof

Let `delta_N=n^{-6}` and mesh `[0,A]` by spacing `delta_N`. At each fixed mesh phase, the `n/2` adjacent increment pairs in (5.1) are iid with law `gamma^2`. Hoeffding therefore gives an exponentially small deviation probability `<=2 exp(-c n)` for each fixed positive error threshold. The mesh has only `O_A(n^6)` points, so the union bound is summable in `N`; Borel--Cantelli gives uniform convergence on the mesh.

For arbitrary phases `theta,theta'` with `|theta-theta'|<=delta_N`, every standardized Brownian increment changes by at most

\[
2\sqrt n\,\omega_B(\delta_N),
\tag{5.3}
\]

where `omega_B` is the Brownian modulus on the relevant compact interval. Almost surely,

\[
\omega_B(r)=O\!\left(\sqrt{r\log(1/r)}\right),
\tag{5.4}
\]

hence

\[
\sqrt n\,\omega_B(n^{-6})
=O(n^{-5/2}\sqrt{\log n})\to0.
\tag{5.5}
\]

The Lipschitz property of `Phi` transfers the mesh convergence to every phase. Intersect over integer `A`. QED.

The quantifier order is the point: the Brownian conclusion holds simultaneously for **every phase** before a random FBM witness phase is introduced.

## 6. T79 — adjacent-pair empirical gate obstruction

### Theorem T79

Let `Q in C([0,1])`. Suppose there is a bounded Lipschitz `Phi:R^2->R` and `ell` such that

\[
\frac{2}{2^N}
\sum_{j=0}^{2^{N-1}-1}
\Phi\!\left(
2^{N/2}\Delta_{N,2j}Q,
2^{N/2}\Delta_{N,2j+1}Q
\right)
\longrightarrow \ell,
\tag{6.1}
\]

where

\[
\Delta_{N,k}Q=Q((k+1)2^{-N})-Q(k2^{-N}),
\tag{6.2}
\]

and

\[
\ell\ne\mathbb E\Phi(Z_0,Z_1)
\tag{6.3}
\]

for independent standard normals `Z_0,Z_1`.

Assume a deterministic space-time shape has arbitrarily far unit gate blocks: there are `a_m->infinity` and constants `c_m` such that

\[
K(a_m+s)\subset\{c_m+Q(s)\},
\qquad 0\le s\le1,
\tag{6.4}
\]

with arbitrary fibers between gate blocks. Then every FBM `X` satisfies

\[
\boxed{
\Pr\!\left(
\exists R<\infty:\ X_{-u}\in K(u)\ \forall u\ge R
\right)=0.
}
\tag{T79}
\]

### Proof

Work on the countable intersection over FBM witness indices `j` of the probability-one events from Lemma 5.1 for the unconditional Brownian futures `B^{(j)}` in (2.1).

Assume eventual confinement. Choose a gate `[a_m,a_m+1]` beyond the eventual-confinement age, then a witness `S_j<=-a_m-1`. In the Brownian future starting at `S_j`, the chronological interval `[-a_m-1,-a_m]` begins at the random phase

\[
\theta=-a_m-1-S_j\ge0.
\tag{6.5}
\]

Along that interval, age runs backward through the gate, so confinement forces, up to an additive constant, the time-reversed trace

\[
\widetilde Q(r)=Q(1-r).
\tag{6.6}
\]

At dyadic level `N`, the adjacent normalized increment pairs of `\widetilde Q` are the adjacent pairs of `Q` in reverse block order with both signs reversed. Thus define

\[
\check\Phi(x,y)=\Phi(-y,-x).
\tag{6.7}
\]

Confinement plus (6.1) gives

\[
\mathcal P_N(\theta;\check\Phi)\to\ell.
\tag{6.8}
\]

But Lemma 5.1, valid at the random `theta` because it is simultaneous over every phase, yields

\[
\mathcal P_N(\theta;\check\Phi)
\to \mathbb E\check\Phi(Z_0,Z_1)
=\mathbb E\Phi(Z_0,Z_1),
\tag{6.9}
\]

because the product Gaussian law is invariant under `(x,y)->(-y,-x)`. This contradicts (6.3). QED.

T79 strictly extends the run-56 gate mechanism in a new direction: T77 only sees the one-step empirical marginal; T79 can obstruct a trace whose one-step microscopic law is exactly standard Gaussian.

## 7. Move #9 — randomize: a bifurcating Gaussian-marginal refinement

Use the coupling from Section 4 as a binary-tree transition.

At a node with state `x`, sample `D` with conditional density

\[
k_x(d)=\gamma(d)\,[1+\varepsilon A(x,d)],
\tag{7.1}
\]

and create children

\[
Y_0=(x+D)/\sqrt2,
\qquad
Y_1=(x-D)/\sqrt2.
\tag{7.2}
\]

Conditioned on the current generation, use independent `D` variables at different nodes. Start the root with law `gamma`.

By Lemma 4.1, every node state has marginal `gamma`.

### 7.1 A quantitative contraction

For two parent states `x,x'`, Kantorovich duality and subtraction of the test function at zero give

\[
W_1(k_x,k_{x'})
\le \varepsilon C_0|x-x'|,
\tag{7.3}
\]

where

\[
C_0
=\mathbb E\left[
|Z|\{\operatorname{Lip}(f)|g(Z)|
+\operatorname{Lip}(g)|f(Z)|\}
\right]
<6.
\tag{7.4}
\]

Let `Q` denote the Markov kernel obtained by choosing one of the two children uniformly. Couple the same child sign and an optimal coupling of `D,D'`. Then

\[
W_1(Q_x,Q_{x'})
\le \rho |x-x'|,
\qquad
\rho=\frac{1+\varepsilon C_0}{\sqrt2}
<\frac{1.06}{\sqrt2}<\frac34.
\tag{7.5}
\]

The final strict inequality is exact after squaring:

\[
\left(\frac{53}{50}\right)^2
=\frac{2809}{2500}
<\frac98
=\left(\frac{3\sqrt2}{4}\right)^2.
\tag{7.6}
\]

The standard normal law is invariant for `Q`.

### 7.2 Generation empirical LLN, proved directly

For bounded Lipschitz `h` with `gamma(h)=0`, define

\[
M_n(h)=2^{-n}\sum_{|u|=n}h(X_u).
\tag{7.7}
\]

Let

\[
Qh(x)=\mathbb E[(h(Y_0)+h(Y_1))/2\mid X=x].
\tag{7.8}
\]

Then `gamma(Qh)=0` and

\[
\operatorname{Lip}(Qh)\le\rho\operatorname{Lip}(h).
\tag{7.9}
\]

Conditional independence of different daughter pairs gives

\[
\operatorname{Var} M_{n+1}(h)
\le 2^{-n}\gamma(h^2)
+\operatorname{Var}M_n(Qh).
\tag{7.10}
\]

Iterating and using the Gaussian Poincare inequality,

\[
\gamma((Q^j h)^2)
\le \rho^{2j}\operatorname{Lip}(h)^2,
\tag{7.11}
\]

shows that `Var M_n(h)` decays exponentially and is summable in `n` because `rho<1`. Chebyshev plus Borel--Cantelli therefore yields

\[
M_n(h)\to0\qquad\text{a.s.}
\tag{7.12}
\]

for every fixed bounded Lipschitz `h`. Intersect over a countable convergence-determining bounded-Lipschitz class to obtain almost surely

\[
\boxed{
2^{-n}\sum_{|u|=n}\delta_{X_u}\Longrightarrow\gamma.
}
\tag{7.13}
\]

### 7.3 Sibling-pair empirical law

For bounded Lipschitz `H:R^2->R`, put

\[
S_{n+1}(H)=2^{-n}\sum_{|u|=n}H(X_{u0},X_{u1}).
\tag{7.14}
\]

Given generation `n`, the summands are independent. Their conditional mean is `M_n(PH)`, where

\[
PH(x)=\mathbb E[H(Y_0,Y_1)\mid X=x].
\tag{7.15}
\]

For our smooth bounded kernel, `PH` is bounded Lipschitz. Conditional variances are uniformly bounded, so

\[
S_{n+1}(H)-M_n(PH)\to0
\quad\text{a.s.}
\tag{7.16}
\]

by Chebyshev/Borel--Cantelli. Then (7.13) gives

\[
S_{n+1}(H)\to \int PH\,d\gamma
=\mathbb E_JH.
\tag{7.17}
\]

In particular,

\[
\boxed{
S_n(R)\longrightarrow
\varepsilon\mathbb E_{\gamma^2}R^2>0.
}
\tag{7.18}
\]

## 8. Move #10 — derandomize: freeze one tree realization into a continuous deterministic trace

The random tree was only a construction device. I now fix one realization on the full-probability event where (7.13), (7.18), and the growth bound below all hold.

At level `n`, enumerate node states from left to right as `X_{n,k}`, `0<=k<2^n`, and prescribe dyadic increments

\[
\Delta_{n,k}Q
=2^{-n/2}X_{n,k}.
\tag{8.1}
\]

Compatibility follows exactly from (7.2):

\[
\Delta_{n,k}Q
=\Delta_{n+1,2k}Q
+\Delta_{n+1,2k+1}Q.
\tag{8.2}
\]

Thus the level-`n` data define consistent dyadic piecewise-linear functions `Q_n`.

### Lemma 8.1 — the refinement converges uniformly to a continuous trace

For every node level `n`, all `X_{n,k}` have standard-normal marginals, so a union bound gives

\[
\Pr\left(
\max_{k<2^n}|X_{n,k}|>2\sqrt n
\right)
\le 2^{n+1}e^{-2n},
\tag{8.3}
\]

which is summable. Hence almost surely the generation maximum is `O(sqrt(n))`.

For a parent, the refinement variable satisfies

\[
D=\frac{Y_0-Y_1}{\sqrt2},
\tag{8.4}
\]

so the level-`n` maximum of `|D|` is also `O(sqrt(n))`. The only deviation between `Q_{n+1}` and `Q_n` on a level-`n` dyadic interval occurs at its midpoint, and (7.2) gives exactly

\[
\|Q_{n+1}-Q_n\|_\infty
\le 2^{-n/2-1}\max_{|u|=n}|D_u|
=O(\sqrt n\,2^{-n/2}).
\tag{8.5}
\]

The right side is summable, so `Q_n` converges uniformly to a continuous deterministic `Q`.

For this fixed `Q`, the normalized level-`n` increments are exactly the node states:

\[
2^{n/2}\Delta_{n,k}Q=X_{n,k}.
\tag{8.6}
\]

Therefore

\[
\boxed{
2^{-n}\sum_{k<2^n}
\delta_{2^{n/2}\Delta_{n,k}Q}
\Longrightarrow N(0,1).
}
\tag{8.7}
\]

So **run 56's one-step empirical-law obstruction is completely silent**.

But the adjacent sibling pairs satisfy

\[
\frac{2}{2^n}\sum_{j<2^{n-1}}
R\!\left(
2^{n/2}\Delta_{n,2j}Q,
2^{n/2}\Delta_{n,2j+1}Q
\right)
\longrightarrow
\varepsilon\mathbb E_{\gamma^2}R^2>0,
\tag{8.8}
\]

whereas independent Brownian pairs have mean zero for `R`.

Notice also the useful reversal identity

\[
R(-y_1,-y_0)=R(y_0,y_1),
\tag{8.9}
\]

because in (4.13) the sum coordinate changes sign, the difference coordinate does not, and `f,g` are even. Thus no extra separator is needed after gate time reversal.

## 9. T80 — a genuinely new nonparabolic shape family

Fix the deterministic continuous trace `Q` from Section 8 and take sparse gate locations

\[
a_m=2^{2^m},\qquad m\ge1.
\tag{9.1}
\]

Define a continuous center `h` on `[a_1,\infty)` by

\[
h(a_m+s)=Q(s),\qquad0\le s\le1,
\tag{9.2}
\]

and interpolate linearly from `Q(1)` at `a_m+1` to `Q(0)` at `a_{m+1}` across every gap.

Define a continuous nonnegative radius `r` by `r=0` on every gate block and, on the gap

\[
[b_m,c_m]=[a_m+1,a_{m+1}],
\tag{9.3}
\]

set

\[
r(u)=(u-b_m)(c_m-u).
\tag{9.4}
\]

Finally define the closed space-time shape

\[
\mathcal G_*
=\{(-u,x):u\ge a_1,\ |x-h(u)|\le r(u)\}.
\tag{9.5}
\]

At every gate block the fiber collapses to the rough deterministic graph of `Q`. Between gates it becomes enormous: at the midpoint of a gap of length `L_m=c_m-b_m`,

\[
\operatorname{diam}K(u_m)=\frac{L_m^2}{2}\longrightarrow\infty.
\tag{9.6}
\]

The shape is closed because `h,r` are continuous and the defining inequality is closed.

### Theorem T80 — Gaussian-marginal dependent-pair gate canyon obstruction

For every FBM `X`,

\[
\boxed{
\Pr\!\left(
\exists R<\infty:
(-u,X_{-u})\in\mathcal G_*
\ \forall u\ge R
\right)=0.
}
\tag{T80}
\]

#### Proof

On each unit gate block (9.2), the fiber is the singleton trace required in T79. Equation (8.8), with `Phi=R`, gives a deterministic adjacent-pair limit

\[
\ell=\varepsilon\mathbb E_{\gamma^2}R^2>0,
\tag{9.7}
\]

while for independent standard Gaussian increments

\[
\mathbb E_{\gamma^2}R=0.
\tag{9.8}
\]

Hence T79 applies. QED.

## 10. Why this earns metric point 57 rather than re-counting run 56

The invariant that separates the two families survives the frozen equivalence operations.

- **Run 56:** the normalized one-step empirical increment law itself is non-Gaussian. A bounded one-variable test function separates the gate trace from Brownian motion.
- **Run 57:** the normalized one-step empirical increment law is **exactly standard Gaussian in the weak limit**. No one-variable bounded continuous test can separate it. The first obstruction is the non-product law of adjacent microscopic sibling increments.

Vertical translation does not affect increments. Reflection only changes signs. Time reversal transforms `(x,y)` into `(-y,-x)`; product Gaussianity versus non-product dependence is unchanged. Brownian scaling preserves the distinction after the natural standardization of microscopic increments. Thus no frozen trivial rescaling/reflection/translation can turn the run-57 trace into the run-56 class.

A different value of `epsilon`, a different choice of even mean-zero `f,g`, or a different sparse sequence `a_m` would remain the **same structural family** and is not counted again.

Therefore the fixed metric moves

\[
\boxed{56\longrightarrow57.}
\tag{10.1}
\]

## 11. What the three Section-B moves actually did

### #2 ATTACK THE NEGATION FIRST

I attacked the claim that exact Gaussian one-step normalized increment marginals remove the increment-statistics obstruction. The explicit positive density (4.6) disproves that stronger claim: parent, both children, and every one-step marginal are Gaussian while the sibling pair is non-product. **Succeeded** and identified the next invariant.

### #9 RANDOMIZE

I promoted that coupling to a bifurcating Markov refinement on the infinite binary tree. A direct Wasserstein contraction and variance recursion give generation LLNs and the non-product sibling-pair limit. **Succeeded** and provided a coherent all-scale construction rather than unrelated finite-level couplings.

### #10 DERANDOMIZE

I fixed one full-probability tree realization and used exact dyadic compatibility to obtain a single deterministic continuous trace. The trace has asymptotically Gaussian one-step increments but non-Brownian pair dependence. **Succeeded** and turns the probabilistic construction into a deterministic space-time shape theorem.

The triple differs from the preceding run's `#3,#18,#19`.

## 12. Validation, finite-core policy, and audits

There is **no nontrivial finite computational core** in T79/T80. The only numerical constant is the deliberately crude exact choice `epsilon=1/100`; positivity and the contraction inequality are proved symbolically above. In accordance with the 90/10 rule, I did **not** manufacture a checker merely to certify arithmetic such as `2809/2500<9/8`.

Self-check status:

- coupling positivity and normalization: checked on page;
- exact Gaussian child marginals: characteristic-function proof on page;
- non-product separator: density-ratio proof on page;
- all-scale compatibility and continuity: proof on page;
- Brownian random-phase dependence issue: handled by Lemma 5.1 before witness selection;
- time reversal: handled explicitly by (6.7), and `R` itself is reversal invariant by (8.9).

Independent OTHER-track audits: **0/2**.  
P26 audit: **missing**.  
Distinct second-track audit: **missing**.  
Publication novelty: **UNVERIFIED**.

Hence this is **PARTIAL** source progress, not source closure.

## 13. Remaining frontier

The one-step marginal boundary is now crossed. The natural next boundary is substantially stronger:

> construct a deterministic gate trace whose empirical law of every fixed same-scale block of `r` consecutive normalized increments is iid Gaussian for every fixed `r`, while a genuinely cross-scale statistic remains non-Brownian.

At that point no finite same-scale local window test would separate the trace. The next candidate invariant would have to mix scales (for example a parent/descendant or wavelet-tree statistic) or use a global empirical process. I have **not** proved such a construction and do not record it as a claim.

## 14. Structured `ledger_delta`

```yaml
ledger_delta:
  track: R07
  source: Burdzy-Scheutzow Forward Brownian Motion Problem 7.8
  intake: I0077
  owner: R07
  admission_state: PENDING_ADMISSION_NOT_READY
  fixed_metric: distinct_nonparabolic_shape_families_complete_source_appropriate_theorem
  before: 56
  after: 57
  movement: true
  unchanged_streak_after: 0
  status: PARTIAL
  new_claims:
    - T79_adjacent_pair_empirical_gate_obstruction
    - T80_gaussian_marginal_dependent_pair_gate_canyons
  finite_core: none_nontrivial
  self_check: PASS_ON_PAGE
  other_track_audits: 0/2
  p26_audit: missing
  second_independent_audit: missing
  novelty: UNVERIFIED
  source_refuted: false
  source_closed: false
  previous_triple: [3,18,19]
  actual_methods: [2,9,10]
  shared_roots_modified: false
  scheduler_modified: false
```

## 15. Model / scheduler-control note

The exposed task-control surface still provides prompt/title, schedule/start-offset, enabled state and timing mode, but **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model receipt**. GPT-6/maximum therefore remains prompt-only here. This report truthfully records GPT-5.6 Sol with reasoning level UNVERIFIED.

The historical P26 `You cannot modify this task` event is authorization-context-specific in the repository record; a later authorized context succeeded for P26, while other contexts denied some R-series IDs. A real model-control fix requires persistent model/reasoning routing fields (or an owning-workspace policy that pins them) plus authenticated per-run telemetry. For any task still rejecting modification, the legitimate route is the owning/authorized workspace/account, an authorized ownership/admin correction, or platform support. No permission bypass, duplicate task, or scheduler modification was attempted here.
