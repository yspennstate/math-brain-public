Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but authenticated runtime metadata does not establish that setting, so I do not claim otherwise.

# P26 / LIVE20 T08 — distance-set shell/profile transfer and a new non-LRE transitive cutoff class

**Status:** `CANDIDATE_FULL` for the restricted transfer theorem and explicit distance-{1,3} application proved below, pending later independent review; **PARTIAL / OPEN** for Salez Problem 2.3. Worldwide publication novelty is **UNVERIFIED**.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Report root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.
Pre-write master observed before the first artifact writes: `55c33878f7188489e5df4c2211c9ebe992952475`.

## 0. Compact handoff and coordination

The previous P26 T08 run proved an entropy-cleanup criterion and applied it to ordinary graph squares `G^2`, giving a same-vertex non-LRE transitive cutoff class. Earlier P26 runs gave exact line-graph and finite-fiber transfers. I do not re-prove those constructions here.

Relevant current dependencies read this run:

- own newest substantive report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_05-01-42__graph-square-shell-entropy-transfer.md`;
- historical-C28 successor / live companion `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T02-15-00Z__twisted-cayley-fiber-cutoff.md`, which now develops twisted finite-group Cayley extensions and finite-orbit entropy disintegration rather than same-vertex isotropic distance kernels;
- current neighboring PROB10-08 report `runs/prob10_2026-09-20/PROB10-08/2026-09-20T01-48-49Z_pre-entropic-lre-cutoff_4f2a.md`, which proves that an NBRW entropy front already follows from tree-rate growth only to the pre-entropic scale and records the two-copy obstruction to deriving such growth from transitivity plus a spectral gap.

Thus the division of labor is non-duplicative: `NM13-01` owns twisted/local-state extensions and orbital memory; P26 develops **same-vertex finite-range isotropic distance kernels and shell entropy/profile transfer**.

The new route below strictly extends the preceding square theorem: instead of the ordinary power using all distances `1,...,m`, it treats arbitrary fixed distance sets `J` containing distance `1`, proves a general Gaussian profile transfer, and applies it to the new distance set `J={1,3}`. This application is not an ordinary graph square, cube, line graph, lexicographic blow-up, truncation, or twisted finite extension.

## 1. Exact source convention and current literature boundary

Justin Salez, arXiv:2508.21055v1 (28 August 2025), uses the rate-one continuous-time semigroup

\[
H_t=e^{t(P-I)}=e^{-t}\sum_{k\ge0}\frac{t^kP^k}{k!}.
\tag{1.1}
\]

Problem 2.3 asks:

> Prove that all vertex-transitive expanders exhibit cutoff.

The current relevant exact-scope results checked on 20 September 2026 are:

1. **Altschuler, arXiv:2609.14945v1, 14 September 2026.** Every fixed-degree long-range-expander sequence has cutoff, with the tree/Ramanujan Gaussian profile. The same paper proves
   \[
   \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
   \]
   with neither converse. Long-range expansion is therefore strictly stronger than the source hypothesis.
2. **Pedrotti--Salez, arXiv:2607.05345, 6 July 2026.** Their local-product criterion gives a universal cutoff-window bound in terms of a non-equilibrium Poincare constant `gamma_*`; no currently recovered theorem derives the needed lower bound from vertex transitivity plus an ordinary spectral gap alone.
3. A fresh bounded search for `graph power random walk cutoff expander`, `graph cube random walk cutoff Ramanujan`, and `distance-3 random walk cutoff` recovered graph-power expansion work such as Kwok--Lau (APPROX/RANDOM 2014), but no theorem matching the continuous-time distance-set shell/profile transfer below. This is bounded negative evidence only, not a priority certificate.

The only external input used for the explicit application is the NBRW endpoint entropy front supplied by Altschuler for fixed-degree long-range expanders. In entropy language, if `q=d-1` and

\[
\ell_n:=\min\{r\ge1:dq^{r-1}\ge n\},
\tag{1.2}
\]

then uniformly in the start vertex and all `r>=ell_n`,

\[
D(K_r(x,\cdot)\|\pi_n)
=\log n-H(K_r(x,\cdot))
\le a_n,
\qquad a_n=O(\log\log n).
\tag{1.3}
\]

The theorem below is stated for any deficit `a_n=o(sqrt(ell_n))`, so it also accepts stronger future entropy/Green-function inputs.

## 2. Parent problem before / after

### Before

Salez Problem 2.3 was OPEN. P26 had already enlarged the positive class to several non-LRE transitive constructions, including ordinary graph squares of suitable high-girth entropy-rich bases, with an `O(sqrt(log n))` continuous-time window. That theorem did not yet provide the limiting profile for general finite-range same-vertex rewiring, nor did it treat sparse distance sets such as `{1,3}`.

### After

Salez Problem 2.3 remains **OPEN**. The proved source-compatible scope is enlarged as follows.

> **Fixed distance-set theorem.** Fix `d>=3` and a finite set `J` of positive integers with `1 in J` and `m=max J>=2`. Let `(G_n)` be `d`-regular vertex-transitive graphs with girth `>2m`, uniform spectral gap, and an NBRW endpoint entropy deficit `a_n=o(sqrt(log n))` at and beyond the entropic radius. Let `X_n=X_J(G_n)` be the graph on the same vertices with `x~y` iff `dist_G(x,y) in J`. Then rate-one continuous-time SRW on `X_n` has cutoff with an explicit Gaussian profile in a `Theta(sqrt(log n))` window.

Applied to a fixed degree-six LPS Ramanujan Cayley family and `J={1,3}`, this gives a **156-regular vertex-transitive Cayley spectral-expander sequence** which is provably not long-range expanding and nevertheless has continuous-time cutoff at

\[
\boxed{\frac{39}{98}\log_5 n+O(1)}
\tag{2.1}
\]

with `Theta(sqrt(log n))` Gaussian window. This output family is distinct from the prior graph-square family (degree 36), from the ordinary graph cube (degree 186), and from all local-fiber constructions used earlier in the project.

This is a theorem/class gain, not a checker or receipt gain.

## 3. Entropy cleanup, upgraded to a profile-transfer criterion

Let `X_n` be regular graphs with uniform stationary law `pi_n`, rate-one semigroup `H_t`, and spectral gaps bounded below by `eta>0`.

The previous run proved the elementary entropy-cleanup estimate

\[
\|\mu H_s-\pi\|_{TV}
\le \sqrt{\frac{D(\mu\|\pi)}{4\eta s}}.
\tag{3.1}
\]

For completeness, it follows from entropy dissipation,

\[
-\frac d{dt}D(\mu H_t\|\pi)
=\mathcal E(f_t,\log f_t)
\ge4\mathcal E(\sqrt{f_t},\sqrt{f_t})
\ge4\eta\operatorname{Var}_\pi(\sqrt{f_t}),
\]

and `TV^2 <= Var_pi(sqrt(f_t))`, integrated using monotonicity of TV.

The new point is a **profile version**.

### Theorem 3.1 — shell entropy plus radial CLT transfers the Gaussian profile

Suppose for each `n` and start `x` that at every time `t`

\[
\delta_xH_t=\sum_{r\ge0}p_t(r)\nu_{n,r,x},
\tag{3.2}
\]

where `p_t` is the law of a radial variable `R_t`. Assume:

1. there are radii `ell_n->infinity` and deficits `a_n=o(sqrt(ell_n))` such that
   \[
   D(\nu_{n,r,x}\|\pi_n)\le a_n
   \quad\text{for every }r\ge\ell_n,
   \tag{3.3}
   \]
   uniformly in `x`;
2. for constants `v>0` and `sigma^2>0`, uniformly on bounded `z`,
   \[
   \frac{R_{\ell_n/v+z\sqrt{\ell_n}}-
          v(\ell_n/v+z\sqrt{\ell_n})}
        {\sqrt{\sigma^2\,\ell_n/v}}
   \Longrightarrow N(0,1);
   \tag{3.4}
   \]
3. for every sequence `h_n->infinity` with `h_n=o(sqrt(ell_n))`, the union of all states reachable by shells `r<=ell_n-h_n` has stationary mass `o(1)`.

Then, with

\[
T_n=\ell_n/v,
\qquad
\tau=\frac{\sqrt{\sigma^2}}{v^{3/2}},
\tag{3.5}
\]

we have for every fixed real `z`,

\[
\boxed{
\|\delta_xH_{T_n+z\sqrt{\ell_n}}-\pi_n\|_{TV}
\longrightarrow
\Phi(-z/\tau)
}
\tag{3.6}
\]

uniformly in `x` whenever the graphs are transitive. In particular the cutoff window is `Theta(sqrt(ell_n))`.

#### Proof

Choose `s_n` so that

\[
a_n\ll s_n\ll\sqrt{\ell_n}.
\tag{3.7}
\]

At time `t-s_n`, split (3.2) into shells below and above `ell_n`, then evolve for the remaining `s_n`. By (3.1), convexity of TV, and (3.3),

\[
\|\delta_xH_t-\pi_n\|_{TV}
\le
\Pr(R_{t-s_n}<\ell_n)
+\sqrt{\frac{a_n}{4\eta s_n}}.
\tag{3.8}
\]

The error tends to zero and `s_n=o(sqrt(ell_n))`, so (3.4) yields

\[
\limsup d_n(T_n+z\sqrt{\ell_n})
\le\Phi(-z/\tau).
\tag{3.9}
\]

For the lower bound choose `h_n->infinity`, `h_n=o(sqrt(ell_n))`, and let `A_n` be the reachable set of shells up to `ell_n-h_n`. Then

\[
\delta_xH_t(A_n)\ge\Pr(R_t\le\ell_n-h_n),
\]

while `pi_n(A_n)=o(1)` by assumption 3. Hence

\[
\liminf d_n(T_n+z\sqrt{\ell_n})
\ge\Phi(-z/\tau),
\tag{3.10}
\]

again because the `h_n` shift is negligible on the `sqrt(ell_n)` scale. This proves (3.6). `QED`

This criterion is stronger than the preceding window-only criterion: it transports the **entire Gaussian profile** whenever the shell entropy defect is little-o of the radial fluctuation scale.

## 4. Fixed distance-set graphs

Fix `d>=3`, write `q=d-1`, and fix a finite set

\[
J\subset\{1,2,\dots,m\},
\qquad 1\in J,
\qquad m=\max J\ge2.
\tag{4.1}
\]

For a `d`-regular graph `G` of girth `>2m`, define `X_J(G)` on `V(G)` by

\[
x\sim_J y
\quad\Longleftrightarrow\quad
\operatorname{dist}_G(x,y)\in J.
\tag{4.2}
\]

Because every radius-`m` geodesic is unique, the number of vertices at base distance `j<=m` is exactly

\[
N_j=dq^{j-1}.
\tag{4.3}
\]

Therefore `X_J(G)` is regular of degree

\[
\boxed{D_J=\sum_{j\in J}dq^{j-1}.}
\tag{4.4}
\]

Every automorphism of `G` preserves distance, so vertex transitivity passes to `X_J(G)`. If `G` is Cayley, then `X_J(G)` is again Cayley.

### 4.1 Exact distance-polynomial algebra

Let `A_j` denote the matrix connecting pairs at base distance exactly `j`. Under girth `>2m`,

\[
A_0=I,\qquad A_1=A,
\]

\[
A_2=A^2-dI,
\qquad
A_{j+1}=AA_j-(d-1)A_{j-1}\quad(j\ge2).
\tag{4.5}
\]

Thus

\[
A_{X_J}=\sum_{j\in J}A_j
\tag{4.6}
\]

is a fixed polynomial in the base adjacency matrix. This is useful algebraically, but the spectral-gap proof below is simpler.

### 4.2 Uniform spectral-gap transfer

Let `P` be base SRW and `Q_J` SRW on `X_J(G)`. Because `1 in J`, every base edge is an output edge. For every function `f`,

\[
\mathcal E_{Q_J}(f,f)
\ge\frac d{D_J}\mathcal E_P(f,f).
\tag{4.7}
\]

Hence if `gap(P)>=gamma`, then

\[
\boxed{\operatorname{gap}(Q_J)\ge\frac d{D_J}\gamma.}
\tag{4.8}
\]

No lower spectral bound away from `-1` is needed in continuous time.

## 5. Exact shell representation on the universal tree

The universal cover `T_d -> G` induces a covering

\[
T_d^J\longrightarrow X_J(G),
\tag{5.1}
\]

where `T_d^J` connects tree vertices whose ordinary tree distance belongs to `J`. The girth condition makes the radius-`m` neighbor map locally bijective.

Lift rate-one continuous-time SRW on `X_J(G)` to rate-one SRW on `T_d^J`, start at the tree root `o`, and let

\[
R_t=d_{T_d}(o,Y_t).
\]

The root stabilizer acts transitively on each ordinary tree sphere and preserves the lifted chain. Therefore, conditional on `R_t=r`, the lifted endpoint is uniform on the sphere of radius `r`. Projecting that sphere to `G` is exactly the length-`r` NBRW endpoint law `K_r(x,.)`. Thus

\[
\boxed{
\delta_xH_t^{X_J}
=\sum_{r\ge0}\Pr(R_t=r)K_r^G(x,\cdot).
}
\tag{5.2}
\]

This is the entropy-transfer identity: the finite-range output walk inherits the **same NBRW shells** as the base, with only a different radial clock.

## 6. Radial increment law and CLT

Suppose the current tree radius is at least `m`. Condition on choosing an output jump whose ordinary tree length is `j in J`. There are `N_j=dq^{j-1}` such destinations.

If the geodesic to the destination initially follows the path toward the root for `a` edges, then the radial increment is `j-2a`. The exact counts are

\[
 c_{j,0}=q^j,
\tag{6.1}
\]

\[
 c_{j,a}=(q-1)q^{j-a-1}
 \quad(1\le a\le j-1),
\tag{6.2}
\]

\[
 c_{j,j}=1.
\tag{6.3}
\]

Their sum is `dq^{j-1}`. Define the translation-invariant increment `xi_J` by

\[
\Pr(\xi_J=j-2a)=\frac{c_{j,a}}{D_J}
\quad(j\in J,\ 0\le a\le j),
\tag{6.4}
\]

with contributions at equal increments added. Put

\[
v_J=\mathbb E\xi_J,
\qquad
\sigma_J^2=\mathbb E\xi_J^2.
\tag{6.5}
\]

For a fixed jump length `j`, direct summation gives

\[
\mu_j
:=\mathbb E[\Delta R\mid j]
=j-\frac{2q(1-q^{-j})}{q^2-1}>0.
\tag{6.6}
\]

Therefore

\[
\boxed{
v_J
=\frac{\sum_{j\in J}dq^{j-1}\mu_j}{D_J}>0.
}
\tag{6.7}
\]

### Lemma 6.1 — boundary effects are tight

For the discrete jump chain of `R_t`, the transition increment equals `xi_J` whenever the radius is at least `m`. Since `v_J>0`, choose `theta>0` small enough that

\[
\rho:=\mathbb E e^{-\theta\xi_J}<1.
\tag{6.8}
\]

Until the chain hits `{0,...,m-1}`, `e^{-theta R_k}` is a strict positive supermartingale. Optional stopping gives an exponentially decaying upper bound on the probability of ever returning to the boundary from height `r`. From a boundary state there is a fixed positive probability to make enough maximal outward jumps to reach a large height and never return. By the strong Markov property the number of boundary returns is therefore dominated by a geometric random variable.

Couple the chain to iid increments `xi_1,xi_2,...` whenever it is outside the boundary. Boundary transitions change the cumulative displacement by at most `2m` each, and there are only a tight number of them. Hence, if `N_t` is the independent rate-one Poisson jump count,

\[
R_t=\sum_{k=1}^{N_t}\xi_k+O_{\mathbb P}(1).
\tag{6.9}
\]

The compound-Poisson CLT therefore yields

\[
\boxed{
\frac{R_t-v_Jt}{\sqrt t}
\Longrightarrow N(0,\sigma_J^2).
}
\tag{6.10}
\]

The variance rate is `E xi_J^2`, not `Var(xi_J)`, because the number of jumps itself is Poisson.

## 7. Main distance-set cutoff/profile theorem

Let `(G_n)` be fixed-degree `d`-regular vertex-transitive graphs satisfying:

- `girth(G_n)>2m` eventually;
- `gap(P_n)>=gamma>0`;
- for `ell_n` from (1.2),
  \[
  D(K_r(x,\cdot)\|\pi_n)\le a_n
  \quad\text{for every }r\ge\ell_n,
  \qquad a_n=o(\sqrt{\ell_n}),
  \tag{7.1}
  \]
  uniformly in `x`.

Let `X_n=X_J(G_n)` and define `v_J,sigma_J` by (6.4)--(6.7).

### Theorem T08-P26-DISTANCE-SET

For every fixed real `z`,

\[
\boxed{
\left\|\delta_xH_{T_n+z\sqrt{\ell_n}}^{X_n}-\pi_n\right\|_{TV}
\longrightarrow
\Phi\!\left(-\frac z{\tau_J}\right),
}
\tag{7.2}
\]

where

\[
\boxed{
T_n=\frac{\ell_n}{v_J},
\qquad
\tau_J=\frac{\sqrt{\sigma_J^2}}{v_J^{3/2}}.
}
\tag{7.3}
\]

In particular `X_n` exhibits cutoff with a `Theta(sqrt(log n))` window.

#### Proof

Equation (5.2) supplies the shell decomposition. Equation (4.8) supplies the uniform output spectral gap. Equation (6.10) gives the radial CLT.

For the lower-support condition in Theorem 3.1, if `R_t<=ell_n-h_n` then the endpoint lies in the base ball `B_G(x,ell_n-h_n)`. The universal degree bound gives

\[
|B_G(x,r)|\le1+d\sum_{k=0}^{r-1}q^k\le C_dq^r.
\tag{7.4}
\]

Since `ell_n=log_q n+O(1)`, any `h_n->infinity` gives

\[
\pi_n(B_G(x,\ell_n-h_n))\le C'_dq^{-h_n}=o(1).
\tag{7.5}
\]

All hypotheses of Theorem 3.1 are now verified, proving (7.2). `QED`

For a fixed-constant LRE base, Altschuler gives `a_n=O(log log n)`, which is `o(sqrt(log n))`. The same conclusion also applies to any future or repository-derived entropy-front theorem with that deficit scale.

## 8. The outputs are not long-range expanders

This point is essential because the user instruction explicitly distinguishes long-range expansion from ordinary spectral expansion.

Let `m=max J>=2`. Every output step moves at most base distance `m`, so

\[
B_{X_J(G)}(x,r)\subseteq B_G(x,mr).
\tag{8.1}
\]

Hence

\[
|B_{X_J(G)}(x,r)|\le C_dq^{mr}.
\tag{8.2}
\]

The output degree is `D_J`, whose tree branching factor is `D_J-1`. Since `m in J`,

\[
D_J-1\ge dq^{m-1}-1
=q^m+q^{m-1}-1>q^m.
\tag{8.3}
\]

Choose `r_n` tending to infinity slowly enough that `(D_J-1)^{r_n}=o(n)`. If a fixed LRE constant `c>0` existed for the output sequence, the singleton condition would require

\[
|B_X(x,r_n)|\ge c(D_J-1)^{r_n}.
\tag{8.4}
\]

But (8.2)--(8.3) imply

\[
\frac{|B_X(x,r_n)|}{(D_J-1)^{r_n}}
\le C_d\left(\frac{q^m}{D_J-1}\right)^{r_n}
\longrightarrow0,
\tag{8.5}
\]

a contradiction. Thus these output sequences are **not uniform long-range expanders** even though (4.8) makes them spectral expanders.

## 9. Concrete new class: distance-{1,3} LPS graphs

Take a fixed degree-six LPS Ramanujan Cayley family `(G_n)`. Its girth grows logarithmically, so eventually `girth>6`. Altschuler makes it a fixed-constant LRE family and hence supplies (7.1) with `a_n=O(log log n)`.

Choose

\[
J=\{1,3\},\qquad d=6,\qquad q=5.
\tag{9.1}
\]

Then

\[
D_J=6+6\cdot5^2=156.
\tag{9.2}
\]

The exact radial increment counts are

\[
\begin{array}{c|rrrr}
\Delta R&-3&-1&1&3\\ \hline
\#&1&5&25&125.
\end{array}
\tag{9.3}
\]

Therefore

\[
\boxed{v_J=\frac{98}{39}},
\qquad
\boxed{\sigma_J^2=\frac{97}{13}},
\tag{9.4}
\]

and

\[
\boxed{\tau_J^2=\frac{442611}{941192}}.
\tag{9.5}
\]

Since `ell_n=log_5 n+O(1)`, the cutoff center is

\[
\boxed{
T_n=\frac{39}{98}\log_5 n+O(1),
}
\tag{9.6}
\]

with limiting profile

\[
\boxed{
\Phi\!\left(-\frac z{\tau_J}\right)
}
\tag{9.7}
\]

in the time window `z sqrt(log_5 n)`.

The spectral-gap transfer factor is exactly

\[
\frac d{D_J}=\frac1{26}.
\tag{9.8}
\]

The LRE failure is quantitatively strong: an output radius-`r` ball grows at most on the `5^{3r}=125^r` base-tree scale, whereas a 156-regular LRE graph would demand the `155^r` scale. The ratio is

\[
\left(\frac{125}{155}\right)^r
=\left(\frac{25}{31}\right)^r.
\tag{9.9}
\]

Thus this is a bounded-degree vertex-transitive **spectral-but-not-long-range** cutoff family, with exact Salez-convention continuous time and an explicit Gaussian window/profile.

## 10. Exact sanity checks actually executed

Two exact-arithmetic / integer-matrix scripts were executed before this report.

### Fixed-power checker

Path:
`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_05-56-17__fixed_power_profile_checker.py`

creation commit: `3bde0578bc7e51ec7e119e7d173e459f94595dec`.

Output path:
`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_05-56-17__fixed_power_profile_checker.out`

creation commit: `336e1585f12f8b3a80685683e240d6df60c96702`.

It checks all radial-count identities for `3<=d<=9`, `2<=m<=5`, the strict branching mismatch, and the adjacency distance-polynomial identities through distance three on the 24-vertex cubic McGee graph of girth seven. It also certifies the ordinary-cube `d=6,m=3` constants. Terminal marker:

`P26_T08_FIXED_POWER_EXACT_PASS`.

### Distance-set checker

Path:
`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_05-56-17__distance_set_profile_checker.py`

creation commit: `92abba3884169e8743c078f37a39df551f6fe619`.

Output path:
`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_05-56-17__distance_set_profile_checker.out`

creation commit: `5cab9825295a3fc90f9f3d17a83be03f2a992f4c`.

It checks every fixed distance set containing `1` with `max J>=2`, for `3<=d<=8` and `max J<=5`; verifies positive radial speed and strict branching mismatch; verifies `A_1+A_3` exactly on the McGee graph; and certifies (9.2)--(9.9). Terminal marker:

`P26_T08_DISTANCE_SET_EXACT_PASS`.

These checks validate finite algebra and constants only; the theorem proof is on the page.

## 11. Mechanism-level advance versus parent-problem advance

### Parent-problem advance

Before: known P26 same-vertex transfer covered the ordinary graph square `J={1,2}`.

After: a **whole family of arbitrary fixed distance sets `J` containing `1`** now has a proved cutoff/profile theorem under the same entropy-front input, including the explicit new transitive non-LRE class `J={1,3}`. This is a strict theorem-scope gain within Salez Problem 2.3, while the full conjecture remains open.

### Mechanism-level advance

The previous shell criterion transferred only a quantitative window. This run upgrades it to a **Gaussian profile-transfer theorem** and identifies the universal finite-range radial data:

- exact shell law: the same base NBRW endpoints `K_r`;
- exact speed `v_J` from (6.7);
- exact compound-Poisson variance rate `sigma_J^2=E xi_J^2`;
- profile width `tau_J=sqrt(sigma_J^2)/v_J^(3/2)`;
- entropy loss is negligible whenever `a_n=o(sqrt(log n))`.

The obstruction left for the full conjecture is therefore not finite-range same-vertex geometry. It is the absence, for arbitrary transitive spectral expanders, of a source-level mechanism forcing an NBRW shell entropy deficit `o(sqrt(log n))` or an equivalent Green-function/local-product estimate.

## 12. Failed / pruned routes this run

1. **Derive maximal tree-rate growth from transitivity plus spectral gap:** not retried. The neighboring PROB10-08 report gives the two-copy/matching obstruction, so this route is genuinely blocked at the hypothesis level.
2. **Twisted finite fibers / local port memory:** pruned as active companion duplication. NM13-01 currently owns that route and has moved to twisted Cayley extensions and orbital decomposition.
3. **Only ordinary graph cubes:** superseded inside this run. The cube `J={1,2,3}` works, but the stronger arbitrary-distance-set theorem gives a cleaner genuinely new class `J={1,3}` and isolates exactly which ingredients matter.

No unchanged checker or receipt is counted as progress.

## 13. Residual obstruction and next attack

The remaining T08 obstruction can now be stated sharply:

> Prove, from vertex transitivity plus a uniform spectral gap alone, an NBRW-shell entropy or averaged Green-function estimate strong enough to give
> \[
> D(K_{\ell_n+O(\sqrt{\ell_n})}(x,\cdot)\|\pi_n)=o(\sqrt{\ell_n}),
> \]
> or prove an alternative local-product estimate that survives product-like transitive obstructions where maximal tree-rate volume growth is false.

The next P26 attack will therefore leave graph operations and finite-range lifts behind. It will study the collision quantity

\[
\sum_y K_r(x,y)^2
\]

and its time-averaged / Green-function analogue on the directed-edge chain, seeking a transitivity-plus-gap upper bound that is stable under `H square K_2` and finite local thickenings. An `L^2` collision estimate of order `n^{-1}e^{o(\sqrt{\log n})}` at the entropic radius would immediately imply the entropy deficit required by Theorem 3.1.

This route is complementary to NM13-01's finite-orbit/twisted-fiber program.

## 14. ledger_delta

```text
target: T08 Salez Problem 2.3, vertex-transitive spectral-expander cutoff
source_status_before: OPEN / PARTIAL
source_status_after: OPEN / PARTIAL
parent_scope_before: same-vertex P26 theorem covered ordinary graph squares under NBRW entropy-front input
parent_scope_after: all fixed distance-set graphs X_J(G), 1 in J, max J>=2, under the same entropy-front input; explicit J={1,3} non-LRE Cayley class
mechanism_before: shell entropy -> O(sqrt(log n)) window
mechanism_after: shell entropy + radial CLT -> explicit Gaussian profile, with v_J and tau_J exact
new_concrete_class: degree-156 distance-{1,3} graphs of degree-6 LPS Ramanujan Cayley bases
new_class_cutoff_center: (39/98) log_5 n + O(1)
new_class_window: Theta(sqrt(log n))
new_class_profile_tau2: 442611/941192
new_class_spectral_gap_factor: >= base_gap/26
new_class_LRE_status: FAILS uniformly; singleton branching ratio <= (25/31)^r
mathematical_status: CANDIDATE_FULL restricted theorem/application; parent OPEN
worldwide_priority: UNVERIFIED
failed_or_pruned_routes: maximal-tree-growth-from-gap blocked; twisted fibers peer-owned; cube-only route strictly generalized
next_attack: transitivity-stable NBRW collision / directed-edge Green-function bound
sanity_code_commits: 3bde0578bc7e51ec7e119e7d173e459f94595dec; 92abba3884169e8743c078f37a39df551f6fe619
sanity_output_commits: 336e1585f12f8b3a80685683e240d6df60c96702; 5cab9825295a3fc90f9f3d17a83be03f2a992f4c
```

End of complete P26 substantive T08 report.
