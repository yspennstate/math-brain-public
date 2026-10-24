Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-01 / T08 — automorphism-memory semidirect cutoff transfer

Status: **PARTIAL / OPEN at the source level; CANDIDATE_FULL restricted theorem and explicit new class, pending later independent review; publication novelty UNVERIFIED.**

The original Salez target does **not** move from OPEN: Problem 2.3 of `arXiv:2508.21055v1` asks for cutoff for all bounded-degree vertex-transitive expander sequences.  This run enlarges the proved restricted scope and removes one concrete transitivity-specific obstruction.  All random walks below use the source rate-one continuous-time convention

\[
H_t=\exp\{t(P-I)\}.
\]

## 0. LIVE20 continuity and short handoff

I followed `operations/PROGRESS20_2026-09-20.md` rather than the superseded intake-only/audit loop.  I read the latest complete NM13-01 proof report, the newer provisional NM13-01 artifacts, the latest relevant P26 T08 report, and the proof dependencies used below rather than rereading the whole repository.

The latest complete NM13-01 report before this run was

`2026-09-20T07-22-00Z__reversal-arc-orbit-likelihood.md`.

It proved a reversal-augmented oriented-edge cutoff class and, more importantly for the parent conjecture, the exact root-stabilizer likelihood identity

\[
V_{\rm KL}(t)
=
\operatorname{Var}_{\nu_t}\!\left(\log\frac{\nu_t}{\bar\pi}(Y_t)\right),
\]

so stabilizer-orbit rank and orbit-size heterogeneity are not by themselves the missing varentropy estimate.

A later same-namespace partial persistence at tag `08-02-33Z` consists of a checker, its output, and a ledger delta but **no substantive report**.  It proposed a semidirect strong-product class and a useful phase-coexistence necessity for hypothetical non-cutoff.  I preserve that state, but this run found that the proposed semidirect strong-product toy is gauge-trivial; Section 2 below records the correction before counting any new theorem.

The newest relevant P26 work remains on the complementary Green/spherical/radial-clock side, now including biregular exact-distance-four halved graphs.  The construction here instead uses a finite automorphism memory and an exact pathwise skew-product contraction; it does not use P26's shell Green-function transfer.

The prewrite master observed before this run's files was

`3f09cb4cd251f4fe7db5aba59bcb3cdb9526ceee`.

## 1. Source and current primary boundary

The source is Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, `arXiv:2508.21055`, Problem 2.3:

`https://arxiv.org/abs/2508.21055`.

The relevant current positive boundary is Dylan Altschuler, *Long-range expanders: construction and cutoff*, `arXiv:2609.14945`, submitted 14 September 2026:

`https://arxiv.org/abs/2609.14945`.

Altschuler proves that every fixed-degree long-range expander has the Ramanujan cutoff location and a Gaussian profile, and proves the strict hierarchy

\[
\text{Ramanujan}\Longrightarrow\text{LRE}\Longrightarrow\text{spectral expansion},
\]

with neither converse.  Thus LRE is not interchangeable with Salez's arbitrary spectral-expander hypothesis.

A second current general mechanism is Pedrotti--Salez, *The local product condition implies cutoff*, `arXiv:2607.05345`:

`https://arxiv.org/abs/2607.05345`.

It does not derive cutoff from vertex transitivity plus ordinary spectral expansion alone.

For the explicit family in Section 7 I use Kaufman--Lubotzky, *Edge Transitive Ramanujan Graphs and Highly Symmetric LDPC Good Codes*, `arXiv:1108.2960`:

`https://arxiv.org/abs/1108.2960`.

Their construction gives fixed-degree edge-transitive Ramanujan Cayley graphs whose generating set is an orbit of a fixed torus action.  For `q=5`, the torus has order `q+1=6`.

Bounded searches on 20 September 2026 for `semidirect random walk cutoff finite automorphism fiber`, `skew product Cayley cutoff`, and combinations with the above sources did not locate this exact transfer theorem.  That is bounded negative evidence only; **publication novelty is UNVERIFIED**.

## 2. Correction to the provisional 08:02 semidirect strong product

Before claiming a new class, I checked whether the preceding provisional semidirect strong-product construction was genuinely new.

Let a group `A` act by automorphisms `theta_a` on a group `Lambda`, and suppose a symmetric fiber generating set `T` is invariant under the action.  On the semidirect product `A semidirect Lambda`, consider the natural strong-product-style generators

\[
(S_A\times\{e\})\cup(\{e\}\times T)\cup(S_A\times T).
\]

In the convention used by the 08:02 checker, the moving-frame bijection

\[
\boxed{\Phi(a,x)=(a,\theta_{a^{-1}}x)}
\tag{2.1}
\]

conjugates adjacency exactly to the ordinary direct strong product

\[
\operatorname{Cay}(A,S_A)\boxtimes\operatorname{Cay}(\Lambda,T).
\tag{2.2}
\]

Indeed, after applying (2.1), a semidirect multiplication by a base-only, fiber-only, or simultaneous generator becomes respectively a base-only, fiber-only, or simultaneous direct-product step because `theta_a(T)=T`.  The current exact checker verifies the equality of all adjacency entries on the 18-state `C_2 semidirect (C_3)^2` toy used by the provisional artifact.

Therefore the 08:02 **graph class is not counted as new**.  Its phase-coexistence lemma remains a separate mechanism-level statement, but its strong-product example is gauge-equivalent to an already understood direct product.

This correction motivates changing which coordinate carries the memory.  In the new construction below, the hidden finite state acts on the **base generator label itself**.  The same moving-frame trick no longer turns vertical hidden moves into holds on the base; instead they induce nontrivial global base automorphisms.

## 3. New class: automorphism-memory semidirect lifts

Let

\[
G_n=\operatorname{Cay}(\Gamma_n,S_n)
\]

be a connected `d`-regular Cayley graph with `S_n=S_n^{-1}`.  Let `K` be a fixed finite group and

\[
\rho_n:K\longrightarrow\operatorname{Aut}(\Gamma_n)
\]

an action satisfying

\[
\rho_n(k)S_n=S_n\qquad(k\in K).
\tag{3.1}
\]

Let

\[
F=\operatorname{Cay}(K,T),\qquad T=T^{-1},\qquad |T|=s,
\]

be fixed, connected, and let `W` be its normalized SRW kernel with one-sided gap

\[
\gamma_F=1-\lambda_2(W)>0.
\]

Fix an involution `tau in K`, `tau^2=e`.  Form the semidirect product with multiplication

\[
(g,k)(h,\ell)=(g\,\rho_n(k)h,k\ell),
\]

and define

\[
H_n=\operatorname{Cay}(\Gamma_n\rtimes_{\rho_n}K,\Sigma_n)
\]

with

\[
\boxed{
\Sigma_n
=
\{(u,\tau):u\in S_n\}
\cup
\{(e,t):t\in T\}.
}
\tag{3.2}
\]

Put

\[
D=d+s,\qquad a=\frac dD,\qquad b=\frac sD.
\tag{3.3}
\]

### Elementary graph properties

The cross set in (3.2) is inverse-closed because

\[
(u,\tau)^{-1}
=(\rho_n(\tau)(u^{-1}),\tau),
\]

and (3.1) plus `S_n=S_n^{-1}` keeps the first coordinate in `S_n`.  The vertical set is inverse-closed by symmetry of `T`.

The graph is connected.  Vertical words generate every `(e,k)`, hence in particular `(e,tau^{-1})`.  Multiplying `(u,tau)` by `(e,tau^{-1})` yields `(u,e)`.  Since `S_n` generates `Gamma_n`, (3.2) generates the full semidirect product.

Thus `H_n` is a connected `D`-regular Cayley graph, hence vertex-transitive.

A cross move from `(g,k)` is

\[
(g,k)\longmapsto
(g\rho_n(k)u,k\tau),
\qquad u\sim\operatorname{Unif}(S_n).
\tag{3.4}
\]

This is the key skew feature: the current hidden state relabels the macroscopic generator before every cross step.

## 4. Main theorem: exact TV sandwich with noncommuting memory

Let `P_n` be SRW on `G_n`, and let `Q_n` be SRW on `H_n`.  Write their source-convention continuous-time worst-start TV curves as `d_G(t)` and `d_H(t)`.

### Theorem A — automorphism-memory transfer

For every `n` and every `t>=0`,

\[
\boxed{
 d_G(at)
 \le d_H(t)
 \le d_G(at)
 +\frac12\sqrt{|K|-1}\,e^{-b\gamma_F t}.
}
\tag{4.1}
\]

Consequently, if `G_n` has continuous-time cutoff at `T_n -> infinity` with window `w_n=o(T_n)`, then `H_n` has cutoff at

\[
\boxed{T_n^H=\frac{T_n}{a}=\frac{d+s}{d}T_n}
\tag{4.2}
\]

with window

\[
O(w_n+1).
\tag{4.3}
\]

If `w_n->infinity` and the base TV curve has a limiting profile at scale `w_n`, then the same profile transfers after the deterministic time rescaling by `1/a`.

### Proof

Split the rate-one Poisson jump process by generator type.  Cross events form an independent Poisson process of rate `a`; vertical events form one of rate `b`.

**Step 1: exact macroscopic lumping.**  Conditional on hidden state `k`, the actual base increment in (3.4) is `rho_n(k)u`.  By (3.1), `u -> rho_n(k)u` is a permutation of `S_n`.  Hence the actual increment is uniform on `S_n`, independently of `k`.  Vertical events do not change `g`.  Therefore the base coordinate is exactly rate-`a` continuous-time SRW on `G_n`:

\[
\operatorname{Law}(G_t\mid G_0=g)
=\delta_g e^{at(P_n-I)}.
\tag{4.4}
\]

Projection contracts TV, proving the lower bound in (4.1).

There is a stronger independence statement needed for the upper bound.  At each cross time, if `V_i=rho_n(K_{i-})U_i` is the actual base increment, then conditional on the entire hidden history `K`, the variables `V_i` are still iid uniform on `S_n`: each map `U_i -> V_i` is a bijection of `S_n`.  Thus the realized base labels reveal no information about the hidden state beyond the already fixed cross clock.

**Step 2: condition on the cross clock and realized base increments.**  On the hidden coordinate, every cross event acts by the fixed right permutation

\[
R_\tau:k\mapsto k\tau.
\]

Between consecutive cross times, the hidden coordinate evolves under the vertical continuous-time semigroup

\[
e^{u b(W-I)}.
\]

On mean-zero `L^2(u_K)`, each vertical interval contracts by at most `e^{-b gamma_F u}`.  The interspersed operators `R_tau` are uniform-measure-preserving isometries.  **No commutation between `R_tau` and `W` is used.**  Since the vertical interval lengths sum to `t`, the conditioned terminal hidden law `eta_t` satisfies

\[
\left\|\frac{\eta_t}{u_K}-1\right\|_{L^2(u_K)}
\le
\sqrt{|K|-1}\,e^{-b\gamma_Ft}.
\tag{4.5}
\]

Hence

\[
\|\eta_t-u_K\|_{TV}
\le
\frac12\sqrt{|K|-1}\,e^{-b\gamma_Ft}.
\tag{4.6}
\]

**Step 3: remove conditioning.**  Replace the conditioned terminal hidden law by `u_K` while leaving the cross clock and realized base path fixed.  Averaging the modified law gives exactly

\[
(\delta_g e^{at(P_n-I)})\otimes u_K.
\]

Convexity of TV and (4.6) imply

\[
\left\|
\delta_{(g,k)}e^{t(Q_n-I)}
-(\delta_g e^{at(P_n-I)})\otimes u_K
\right\|_{TV}
\le
\frac12\sqrt{|K|-1}e^{-b\gamma_Ft}.
\tag{4.7}
\]

Uniform lifting preserves TV, so the triangle inequality gives the upper bound in (4.1).  Equations (4.2)--(4.3) follow because the error in (4.1) vanishes exponentially on every diverging cutoff scale. `QED`

The exact checker deliberately uses `K=S_3`, `tau=(12)`, and vertical generators `{(12),(23)}`.  The hidden cross permutation and vertical kernel have exact commutator maximum `1/2`, so the theorem is not secretly relying on commuting factors.

## 5. Spectral expansion transfers

Assume

\[
1-\lambda_2(P_n)\ge\gamma_G>0.
\]

### Theorem B — explicit gap transfer

\[
\boxed{
\operatorname{gap}(H_n)
\ge
\min\{a\gamma_G,b\gamma_F\}.
}
\tag{5.1}
\]

### Proof

For `f:Gamma_n x K -> R`, let

\[
\bar f(g)=\frac1{|K|}\sum_{k\in K}f(g,k).
\]

Variance decomposes as

\[
\operatorname{Var}(f)
=
\operatorname{Var}_g(\bar f)
+\mathbb E_g\operatorname{Var}_k(f(g,k)).
\tag{5.2}
\]

The vertical Dirichlet form obeys

\[
\mathcal E_V(f,f)
\ge
\gamma_F\,\mathbb E_g\operatorname{Var}_k(f(g,k)).
\tag{5.3}
\]

For the cross form, write `v=rho_n(k)u`.  For fixed `(g,v)`, Jensen in the hidden coordinate gives

\[
\frac1{|K|}\sum_k
\left[f(g,k)-f(gv,k\tau)\right]^2
\ge
\left[\bar f(g)-\bar f(gv)\right]^2,
\tag{5.4}
\]

because `k -> ktau` is a permutation of `K`.  Summing over `g` and uniform `v in S_n` gives

\[
\mathcal E_C(f,f)
\ge\mathcal E_{P_n}(\bar f,\bar f)
\ge\gamma_G\operatorname{Var}_g(\bar f).
\tag{5.5}
\]

Since `E_Q=aE_C+bE_V`, combining (5.2)--(5.5) gives (5.1). `QED`

Thus a base spectral-expander sequence produces another bounded-degree vertex-transitive spectral-expander sequence.

## 6. The output can be far outside long-range expansion

Every output step changes the `Gamma_n` coordinate by either one base edge or zero.  Therefore for every start `(g,k)` and radius `r`,

\[
B_{H_n}((g,k),r)
\subseteq
B_{G_n}(g,r)\times K.
\tag{6.1}
\]

The degree bound on `G_n` gives

\[
|B_{H_n}((g,k),r)|
\le C_{d,K}(d-1)^r.
\tag{6.2}
\]

But the output degree is `D=d+s`, so its LRE tree benchmark is `(D-1)^r`, and `D-1>d-1`.  With `N_n=|V(H_n)|`, choose

\[
r_n=\left\lfloor\frac12\log_{D-1}N_n\right\rfloor.
\]

Then `(D-1)^{r_n}=N_n^{1/2+o(1)}`, still below the saturation scale in the LRE definition, while

\[
\frac{|B_{H_n}((g,k),r_n)|}{(D-1)^{r_n}}
\le
C_{d,K}\left(\frac{d-1}{D-1}\right)^{r_n}
\longrightarrow0.
\tag{6.3}
\]

Hence no fixed positive LRE constant can hold on the output family.

So Theorem A produces genuinely source-relevant spectral expanders outside Altschuler's hypothesis, rather than merely reapplying the LRE theorem to the output.

## 7. Explicit degree-10 family from Kaufman--Lubotzky

Take the `q=5` Kaufman--Lubotzky Ramanujan Cayley family.  Let

\[
G_n=\operatorname{Cay}(\Gamma_n,S_n),
\qquad |S_n|=6.
\]

Their construction supplies a torus `K=C_6` of automorphisms whose orbit is `S_n`; hence (3.1) holds.  Let `t` generate `C_6`, choose

\[
\tau=t^3,
\qquad
T=\{t,t^{-1},t^2,t^{-2}\}.
\]

Then the hidden Cayley graph is 4-regular.  Its normalized eigenvalues are

\[
1,\ 0,\ 0,\ -\frac12,\ -\frac12,\ 0,
\]

so its one-sided gap is

\[
\gamma_F=1.
\tag{7.1}
\]

Here

\[
d=6,\quad s=4,\quad D=10,\quad a=\frac35,\quad b=\frac25.
\tag{7.2}
\]

Altschuler proves Ramanujan implies LRE and proves the LRE cutoff theorem.  In the source rate-one continuous-time convention, Poissonizing the same radial/NBRW argument gives the same first-order center and an `O(sqrt(log n))` window; the Poisson clock contributes only another `sqrt(log n)` fluctuation.  Therefore the degree-six base has center

\[
T_n^G=\frac6{6-2}\log_5n
=\frac32\log_5 n
\tag{7.3}
\]

with `O(sqrt(log n))` window.  Theorem A yields

\[
\boxed{
T_n^H
=\frac{1}{a}T_n^G
=\frac52\log_5 n.
}
\tag{7.4}
\]

Since `|K|=6`, the output size is `N_n=6n`, so equivalently

\[
\boxed{
T_n^H
=\frac52\log_5(N_n/6),
\qquad
w_n^H=O(\sqrt{\log N_n}).
}
\tag{7.5}
\]

The output gap is explicit.  Ramanujan gives

\[
\gamma_G
\ge1-\frac{2\sqrt5}{6}
=1-\frac{\sqrt5}{3}.
\]

Hence Theorem B gives

\[
\boxed{
\operatorname{gap}(H_n)
\ge
\min\left\{
\frac35\left(1-\frac{\sqrt5}{3}\right),\frac25
\right\}
=
\frac{3-\sqrt5}{5}.
}
\tag{7.6}
\]

Finally, (6.2) grows on the `5^r` scale while the degree-10 output LRE benchmark grows on the `9^r` scale.  Thus the family is vertex-transitive, a uniform spectral expander, has the source continuous-time cutoff with the quantitative window (7.5), and is not a fixed-constant long-range expander.

This class is not the earlier direct-product twisted-fiber class.  Here hidden state changes which base generator is actually traversed; the base marginal stays Markov only because transitivity supplies an automorphism action that permutes the full generator orbit.  The finite checker also finds a spectrum different from the obvious direct Cartesian comparison in a noncommuting `S_3` toy.

## 8. General-conjecture obstruction removed

The theorem isolates and removes a concrete potential obstruction to Salez Problem 2.3:

> **A bounded hidden automorphism memory that dynamically relabels every macroscopic generator cannot destroy cutoff, provided that the hidden coordinate has a fixed spectral gap.**

This is stronger than saying a fixed decoration is harmless.  The visible jump at time `t` depends on the current hidden state, and hidden cross and vertical operators may fail to commute.  Transitivity is exactly what neutralizes the feedback: `rho(k)` permutes the entire generator orbit, so the visible increment remains uniform and independent of the hidden state, while the hidden memory loses information exponentially between the isometric cross kicks.

Consequently, a counterexample architecture to the full vertex-transitive-expander conjecture cannot be obtained merely by attaching a **fixed** automorphism state that steers generator labels.  To survive this argument it must use at least one genuinely harder feature, for example:

- memory whose effective state space grows with `n` quickly enough that the `sqrt(|K|)` prefactor is no longer negligible;
- nonuniform steering that destroys exact visible lumping;
- hidden dynamics without uniform contraction; or
- no macroscopic cutoff factor at all.

This complements the 08:02 phase-coexistence necessity.  That result says hypothetical non-cutoff forces macroscopic likelihood separation rather than merely local spikes; the present theorem shows that bounded transitive steering memory cannot supply such persistent macroscopic separation.

The full conjecture is **not** proved: an arbitrary vertex-transitive spectral expander need not admit any semidirect factorization of the form above.

## 9. Executed sanity checks

The checker is

`2026-09-20T08-55-00Z__automorphism-memory-checker.py`

with archived output

`2026-09-20T08-55-00Z__automorphism-memory-checker.out`.

It checks three things.

First, on a 48-state noncommuting toy with base `Gamma=(F_2)^3`, hidden group `K=S_3`, `tau=(12)`, and vertical generators `{(12),(23)}`, it verifies exactly:

- inverse closure and regularity;
- the cross identity after generator relabeling;
- exact strong lumping of the base coordinate;
- hidden cross/vertical commutator maximum `1/2`.

Numerically it finds

\[
\gamma_G=8/7,\qquad
\gamma_F=1/2,\qquad
\gamma_H\approx0.1611295072,
\]

against the theorem lower bound `1/9`, and verifies (4.1) at six continuous times.  The skew output has second eigenvalue about `0.83887049`, whereas the obvious direct Cartesian comparison has `8/9`, providing a basic non-product stress check.

Second, it verifies entry-by-entry that the previous 18-state 08:02 semidirect strong-product toy becomes the ordinary direct strong product under the moving-frame gauge (2.1).

Third, it checks the degree-10 `q=5` constants

\[
a=3/5,\quad b=2/5,\quad
T_n^H=(5/2)\log_5 n,\quad
\operatorname{gap}(H_n)\ge(3-\sqrt5)/5,
\]

and the growth-base separation `5<9`.

The archived output ends

`ALL_CHECKS_PASS`.

These finite computations are sanity checks only; the asymptotic cutoff transfer, gap bound, and non-LRE assertion are proved above.

## 10. Source-level versus mechanism-level movement

**Original Salez problem:**

- before: `PARTIAL / OPEN` — arbitrary bounded-degree vertex-transitive spectral expanders unresolved;
- after: `PARTIAL / OPEN` — unchanged.

**Restricted theorem scope:** strictly enlarged by the automorphism-memory semidirect lift and the explicit degree-10 Kaufman--Lubotzky-derived non-LRE family with center `(5/2) log_5(N/6)` and `O(sqrt(log N))` window.

**Mechanism progress:** bounded finite automorphism memory with noncommuting local noise is now proved harmless for cutoff; the provisional 08:02 semidirect strong-product example is corrected as gauge-trivial rather than silently counted as progress.

## 11. Next attack

Two routes are now sharply defined.

The parent-conjecture route is to combine the 08:02 phase-coexistence necessity with transitive boundary flow: if two root-stabilizer-invariant likelihood phases each carry positive heat mass and are separated by `Theta(log n)` in log-likelihood, use automorphic translates plus the expander boundary to force either a large instantaneous entropy dissipation or too much inter-phase flow for coexistence at mixing time.

The transfer route is to replace the `sqrt(|K|)` `L^2` prefactor in (4.1) by a genuinely `TV` or log-Sobolev hidden-memory estimate.  That would locate the threshold at which a **growing** automorphism memory can still be ruled out as a source of non-cutoff.

No source-level closure claim is made, and no audit is presumed.

## 12. Ledger delta

The machine-readable companion `2026-09-20T08-55-00Z__ledger_delta.json` records the same source-level/open status, the new restricted theorem and constants, the gauge correction, the removed obstruction, checker result, and next step.
