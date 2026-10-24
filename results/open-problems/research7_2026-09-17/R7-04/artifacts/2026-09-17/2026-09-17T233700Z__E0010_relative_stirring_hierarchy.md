Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is not GPT-6 at maximum; GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning telemetry or binding model/effort selector is exposed.

# E0010 — relative harmonicity of disagreements under fast stirring

Target: Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 4.  For the sexual-reproduction process with fixed `beta>4.5`, prove that sufficiently fast nearest-neighbor stirring gives a unique positive/nontrivial stationary phase in the source convention.

This note continues the exact ordered-coupling reduction and the Palm/hypergeometric threshold theorem from the preceding R7-04 reports.  It does **not** close the source problem.  The new point is to remove one genuine relative-error obstruction: the fast-stirring equations themselves admit estimates after division by the *unknown disagreement scale* `Q`, with no `1/Q` loss.

## 1. Setup recalled

Let `eta <= xi` be a stationary basic ordered coupling of a putative positive stationary law with the upper invariant law.  Write

\[
D_x=\xi_x-\eta_x\in\{0,1\},\qquad q_x=\mathbb E D_x,\qquad Q=\sup_x q_x.
\]

If `Q=0` the two laws coincide, so throughout the obstruction analysis assume `Q>0`.

For the source ordered-pair birth rule,

\[
A_x(\zeta)=\frac1{n(n-1)}\sum_{\substack{y,z\in N_x\\y\ne z}}\zeta_y\zeta_z.
\]

The preceding run proved the exact stationary disagreement equation

\[
0=\varepsilon^{-2}\Delta_s q(x)-q_x+\beta\Gamma_x,
\tag{1.1}
\]

where

\[
\Delta_s q(x)=\sum_{w\sim_s x}(q_w-q_x)
\]

is the unit-rate-per-stirring-edge discrete Laplacian and

\[
\Gamma_x=\mathbb E\left[(1-\xi_x)(A_x(\xi)-A_x(\eta))-D_xA_x(\eta)\right].
\tag{1.2}
\]

Also

\[
A_x(\xi)-A_x(\eta)
=\frac1{n(n-1)}\sum_{y\ne z}\bigl(D_y\xi_z+\eta_yD_z\bigr).
\tag{1.3}
\]

## 2. B12 — exact relative flattening of the disagreement profile

The key observation is that the reaction defect in (1.1) is already proportional to `Q`.

### Lemma 1 (uniform reaction bound)

For every site `x`,

\[
-Q\le \Gamma_x\le 2Q.
\tag{2.1}
\]

#### Proof

The second term in (1.2) lies in `[-q_x,0]`, hence in `[-Q,0]`.  The first term is nonnegative.  By (1.3), positivity, and `0<=eta,xi<=1`,

\[
\begin{aligned}
0&\le \mathbb E[(1-\xi_x)(A_x(\xi)-A_x(\eta))]\\
&\le \frac1{n(n-1)}\sum_{y\ne z}
\bigl(\mathbb E D_y+\mathbb E D_z\bigr)\\
&\le 2Q.
\end{aligned}
\]

This proves (2.1). QED.

Since `beta>4.5>1`, equations (1.1) and (2.1) imply the convenient uniform bound

\[
\boxed{\|\Delta_s q\|_\infty\le 2\beta\varepsilon^2 Q.}
\tag{2.2}
\]

(Using the looser constant `1+2 beta` would also suffice.)

Normalize

\[
h(x)=q_x/Q\in[0,1].
\]

Then

\[
\|\Delta_s h\|_\infty\le 2\beta\varepsilon^2.
\tag{2.3}
\]

Let `P_t` be the continuous-time nearest-neighbor random-walk semigroup with generator `Delta_s`.  Duhamel's formula gives, for every `x`,

\[
|h(x)-P_t h(x)|\le 2\beta\varepsilon^2 t.
\tag{2.4}
\]

Consequently, for every lattice displacement `r`,

\[
\boxed{
\sup_x |h(x+r)-h(x)|
\le 4\beta\varepsilon^2t
+\|P_t(x+r,\cdot)-P_t(x,\cdot)\|_{\rm TV}.}
\tag{2.5}
\]

Translation invariance of the walk makes the total-variation term independent of `x`.

### Lemma 2 (merging of two nearest-neighbor stirring walkers)

For each fixed displacement `r`,

\[
\|P_t(r,\cdot)-P_t(0,\cdot)\|_{\rm TV}\longrightarrow0
\qquad(t\to\infty).
\tag{2.6}
\]

#### Proof

Represent the `d` coordinates of the continuous-time nearest-neighbor walk by independent one-dimensional continuous-time symmetric walks.  For each coordinate, couple the two copies by reflection until their coordinates meet and then use identical increments.  The coordinate difference before meeting is a one-dimensional symmetric walk, hence hits zero almost surely.  There are only finitely many coordinates, so the maximum of their coupling times is finite almost surely.  The coupling inequality then gives (2.6). QED.

Choose any `t=t(epsilon)` with

\[
t(\varepsilon)\to\infty,
\qquad
\varepsilon^2t(\varepsilon)\to0.
\]

For example `t=epsilon^{-1}`.  Combining (2.5) and (2.6) yields the main unconditional theorem of this run.

### Theorem 3 (relative local flattening)

For every fixed lattice displacement `r`, uniformly over all stationary ordered couplings with `Q>0`,

\[
\boxed{
\sup_x\frac{|q_{x+r}-q_x|}{Q}\longrightarrow0
\qquad(\varepsilon\downarrow0).}
\tag{2.7}
\]

In particular, if `x_epsilon` is an approximate-maximal disagreement site with

\[
q_{x_\varepsilon}/Q\to1,
\]

then for every fixed `r`,

\[
\boxed{
\frac{q_{x_\varepsilon+r}}{q_{x_\varepsilon}}\to1.}
\tag{2.8}
\]

This strictly improves the preceding use of the crude inequality `q_y/q_x<=1+o(1)` at approximate maxima: all finitely many source-parent ratios now converge to one, *uniformly relative to the unknown disagreement scale*.

## 3. B3 — an approximate-harmonic hierarchy for every discrepancy-tagged moment

The preceding scalar argument extends to all finite color monomials at the generator level.

Use the three ordered-coupling colors

\[
A_x:=\eta_x,\qquad D_x:=\xi_x-\eta_x,\qquad C_x:=1-\xi_x.
\]

Let `alpha=(alpha_1,...,alpha_m)` with each `alpha_i` one of `A,D,C`, and assume at least one `alpha_i=D`.  For pairwise distinct sites `x_1,...,x_m`, set

\[
H_\alpha(\mathbf x)
=\mathbb E\prod_{i=1}^m\alpha_i(x_i).
\tag{3.1}
\]

Let `S_m` be the `m`-label stirring generator on injective tuples: an edge transposition is applied simultaneously to every coordinate of the tuple.  Because the source stirring swaps both coupled configurations at the same edge, it transports every one-site color exactly.  Hence

\[
\mathbb E\,S\left(\prod_i\alpha_i(x_i)\right)
=(S_m H_\alpha)(\mathbf x).
\tag{3.2}
\]

### Lemma 4 (reaction defect is proportional to `Q`)

There is a finite constant `C_{m,beta}` depending only on `m`, `beta`, and the fixed finite interaction neighborhood, but **not** on `epsilon`, `Q`, or the tuple positions, such that

\[
\left|\mathbb E\,R\left(\prod_i\alpha_i(x_i)\right)\right|
\le C_{m,\beta}Q.
\tag{3.3}
\]

One may safely take `C_{m,beta}=4m(1+beta)` for the source graphical construction.

#### Proof

A reaction outside the `m` displayed sites cannot change the product.  At a displayed site that is not carrying the chosen `D` factor, a reaction can change the product only while that `D` factor is present.  The total graphical death-plus-birth mark rate at one site is at most `1+beta`, and the product oscillation is at most one, so its expected contribution is bounded by a constant times `E D <= Q`.

At a site carrying `D`, destruction of an existing discrepancy is again bounded by a constant times `Q`.  The only apparently dangerous event is creation of a discrepancy when `D=0`.  Under the basic coupling its rate is

\[
\beta(1-\xi_x)(A_x(\xi)-A_x(\eta)),
\]

whose expectation is at most `2 beta Q` by the proof of Lemma 1.  Summing over the finitely many displayed sites gives (3.3). QED.

Stationarity of the coupled law under

\[
L_\varepsilon=\varepsilon^{-2}S+R
\]

now yields, from (3.2)-(3.3),

\[
\boxed{
|(S_m H_\alpha)(\mathbf x)|
\le C_{m,\beta}\varepsilon^2Q.}
\tag{3.4}
\]

Thus the normalized moment

\[
h_\alpha(\mathbf x):=H_\alpha(\mathbf x)/Q\in[0,1]
\]

satisfies

\[
\boxed{\|S_m h_\alpha\|_\infty\le C_{m,\beta}\varepsilon^2.}
\tag{3.5}
\]

This is the sought relative estimate: the entire finite tagged-moment hierarchy is approximately harmonic for pure stirring, with an error that stays `O(epsilon^2)` after division by the possibly arbitrarily small `Q`.

If `P_t^{(m)}` denotes the `m`-label stirring semigroup, Duhamel gives

\[
\|h_\alpha-P_t^{(m)}h_\alpha\|_\infty
\le C_{m,\beta}\varepsilon^2t.
\tag{3.6}
\]

Therefore for any two injective labeled tuples `x,x'`,

\[
|h_\alpha(\mathbf x)-h_\alpha(\mathbf x')|
\le 2C_{m,\beta}\varepsilon^2t
+\|P_t^{(m)}(\mathbf x,\cdot)-P_t^{(m)}(\mathbf x',\cdot)\|_{\rm TV}.
\tag{3.7}
\]

For `m=1`, Lemma 2 closes the right side and reproduces Theorem 3.  For the `m=2,3` mixed-color observables entering the Palm reproduction identity, (3.7) isolates a *pure finite-label stirring* question.  No stationary rare-event denominator remains.

## 4. B21 — imported technique and the exact remaining finite-label problem

The relevant analogous-field machinery is now much more specific than generic propagation of chaos.

1. Durrett's current interacting-particle-systems notes/book explains the fast-stirring proof by dual particles: the dual is almost a branching random walk; stirring keeps lineages separated; even in one dimension the number of close encounters is too small to create macroscopic correlation.  The same chapter records mean-field/PDE control on times growing as a small constant times `log(1/epsilon)`.
2. The symmetric-exclusion literature characterizes invariant measures by duality plus successful coupling of finite-particle duals.  Redig--van Wiechen (2023) explicitly describe successful coupling of finite symmetric-exclusion duals as the mechanism that collapses bounded harmonic functions.
3. Finite-graph interchange theory gives sharp spectral-gap information (Aldous' spectral-gap conjecture, proved by Caputo--Liggett--Richthammer), suggesting a finite-box route if a boundary-stable estimate is preferable.

The chain in (3.7) is slightly more specific than ordinary indistinguishable exclusion: different moment labels (`C,D,A`) are carried by distinguished stirring particles, and an edge joining two displayed coordinates swaps their labels.  Therefore this run does **not** silently import an indistinguishable-exclusion theorem as if it already proved the needed labeled statement.

The exact next mathematical lemma is:

> **Finite-label relative mixing lemma.** For the labeled stirring chain that appears in (3.7), prove a quantitative local merging estimate strong enough for `m<=3` and a time scale `t(epsilon)->infinity`, `epsilon^2 t(epsilon)->0`, uniformly for the finitely many tuple geometries in the source birth neighborhood.

If this lemma is obtained, (3.7) upgrades the previous ideal color-exchangeable block calculation to a genuine **relative Palm averaging theorem** with no `1/Q` loss.

## 5. A finite-state perturbation lemma showing that the `1/Q` loss is not intrinsic

Although a finite torus has no nonzero stationary phase for the absorbing source process and therefore does not solve Problem 4, the following exact perturbation lemma is useful because it demonstrates algebraically that relative fast-stirring averaging is possible.

Let `Lambda` be any finite connected graph with `M` sites and let `S` be its three-color interchange generator.  Let `Pi` denote averaging uniformly within each fixed `(A,C,K)` color-count sector.  If a bounded function `f` vanishes on the diagonal sector `K=0`, define the sectorwise Poisson solution

\[
g=-\int_0^\infty(P_t^Sf-\Pi f)\,dt.
\tag{5.1}
\]

The integral is finite because every nontrivial sector is finite and irreducible, and `g=0` on `K=0`.  It solves

\[
Sg=f-\Pi f.
\tag{5.2}
\]

For any stationary ordered coupling of a finite-state dynamics `epsilon^{-2}S+R` in which the diagonal sector is absorbing under the coupled reaction part,

\[
|\mu(f-\Pi f)|
=\varepsilon^2|\mu(Rg)|.
\]

The total reaction-clock rate is at most `M(1+beta)`, while `Rg=0` on `K=0`; hence

\[
|\mu(Rg)|
\le 2M(1+\beta)\|g\|_\infty\,\Pr(K>0).
\]

If `Q=max_x E D_x`, then `Pr(K>0)<=E K<=MQ`, so

\[
\boxed{
\frac{|\mu(f-\Pi f)|}{Q}
\le 2\varepsilon^2M^2(1+\beta)\|g\|_\infty.}
\tag{5.3}
\]

Again there is no `1/Q` blow-up.  The infinite-volume difficulty is quantitative/local: control the relevant Poisson solution or finite-label semigroup while sending the mesoscopic scale to infinity without importing boundary errors of order `epsilon^{-2}`.

## 6. Interaction with the preceding hypergeometric threshold

The preceding run proved that exact color exchangeability with common-one density `a=A/M` gives the normalized disagreement reproduction polynomial

\[
\psi(a,d)=2a-3a^2+d(1-3a)-d^2,
\]

and, for

\[
a_+(\beta)=\frac{1+\sqrt{1-3/\beta}}3,
\]

any fixed margin `a>=a_+(beta)+delta` makes the reproduction number strictly smaller than `1/beta` for large enough `M`.

Theorem 3 and Lemma 4 remove two pieces of the old bridge:

- all local `q_y/q_x` factors at a maximal disagreement become `1+o(1)` **relatively**;
- every tagged two- and three-point numerator has a pure-stirring defect `O(epsilon^2)` after normalization by `Q`.

What remains is not generic factorization.  It is now the conjunction of two explicit statements:

1. prove the finite-label relative mixing lemma for the `m<=3` labeled stirring observables in (3.7); and
2. prove that the resulting discrepancy-Palm environment lies above the explicit common-one threshold `a_+(beta)` by a fixed margin (or prove an averaged inequality strong enough to make the reproduction number `<1/beta`).

Durrett's current notes record that for the **upper invariant measure** the equilibrium density tends to the stable mean-field root

\[
\rho_0(\beta)=\frac{1+\sqrt{1-4/\beta}}2
\]

when `beta>4.5`, and the preceding run proved `a_+(beta)<rho_0(beta)`.  This leaves genuine room for the desired Palm density margin, but the upper-law density convergence by itself does not control a discrepancy-conditioned environment and therefore is not promoted to a proof.

## 7. Status

This run proves a new infinite-volume theorem, (2.7), and a new exact relative moment hierarchy, (3.4)-(3.7).  It does **not** prove uniqueness of the positive stationary phase.

Frozen source metric remains

`Q_SR(beta,epsilon): UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.

So there is **no metric movement**.  The source remains **PARTIAL / OPEN**.
