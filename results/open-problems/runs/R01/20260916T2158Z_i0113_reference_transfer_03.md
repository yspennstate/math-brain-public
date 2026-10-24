Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but this runtime exposes no model selector, no reasoning-effort selector, and no authenticated runtime telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT IN THE FROZEN METRIC: I0113 `M_3 = 3/3 -> 3/3`, unchanged count `2`; Section-B methods actually used: #6 DEFORM TO A POINT YOU CAN SOLVE, #12 FIND WHAT IS CONSERVED, #21 ASK WHO ELSE HAS THIS SHAPE.**

# R01 — I0113 Salez Problem 2.7: reference-chain transfer and a nonperturbative bounded-block benchmark

Run ID: `20260916T2158Z_i0113_reference_transfer_03`  
Repository/branch: `yspennstate/math-open-problems` / `master`  
Delivery: private GitHub only.

## 1. Continuity: I0024 stays handed off; active R01 claim is I0113

The native schedule title/prompt still names Aldous--Fill Open Problem 3.44 / I0024, but the binding NEW-METHODS contract rotates a CLOSABLE target after six unchanged runs. R01 already reached that threshold and wrote the immutable I0024 handoff

`runs/R01/20260916T1901Z_62d7c9a4.md`.

That handoff expressly forbids a seventh unchanged I0024 research run by R01. Its exact `C=1` flow formula, rational counterexamples to naive scalar candidates, R20 audit, P26 finite-check state and unresolved prior-art/full-P26-audit obligations remain preserved and are not retracted.

The canonical current R01 ownership record is

`operations/claims/I0113.md`,

for Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055, Problem 2.7. The old R01 FEI assignment remains retired; P03 owns FEI.

The immediately preceding complete R01 report is

`runs/R01/20260916T2059Z_i0113_path_entropy_02.md`.

It proved the common all-three perturbative condition

\[
 n\log n\,\Delta_n^2\to0,
\qquad
\Delta_n:=\max_{x,i}|D_i\log(\pi_n/\nu_n)(x)|,
\]

relative to a uniformly nondegenerate product reference `nu_n`, improving the first I0113 run's linear `n log n Delta_n -> 0` condition. It also retained the exact product-target obstruction showing that dependence alone is insufficient when the one-site marginals are allowed to become arbitrarily degenerate.

I do not reprove those results below. This run asks how much of the path-entropy argument survives if the solvable reference is not the uniform/product cube and if the perturbation is anisotropic.

## 2. Mandatory source/repository/current-literature refresh

Before new mathematics I refreshed the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the R-series and NEW-METHODS fleet contracts, the I0113 claim, the newest R01 report, the newest neighboring Salez report R16/I0112, the intake hit for I0113, and the newest complete R02 package relevant to the directed-audit budget.

Repository state relevant here:

- I0113 remains exclusively claimed by R01.
- POSTED.md does not exclude Problem 2.7.
- the shared RESULTS row for R01 is stale at I0024 in a context that recorded denied R-series root edits; the newer canonical claim and immutable R01 reports govern the actual research continuation.
- no durable P26 audit of the I0113 theorem package was found in repository-wide search.

Fresh source/literature checks dated 2026-09-16/17 UTC-window:

1. Salez's live notes at `https://www.ceremade.dauphine.fr/~salez/cutoff.pdf` still display Problem 2.7 verbatim after (2.13): find one weak-dependency condition on `pi_n in P({-1,1}^n)` under which cutoff occurs for the Gibbs, Metropolis and square-root implementations.
2. The same notes' Theorem 4.7 gives a general coordinate-flip rate-influence condition implying nonnegative sectional/Ollivier-type curvature and an MLSI lower bound, but the displayed Bakry--Emery lower bound is explicitly only for the square-root rates. Their Theorem 5.3, which yields cutoff from `alpha t_mix >> log log d`, assumes nonnegative Bakry--Emery curvature. Thus the tempting direct plug-in does not presently produce one all-three theorem.
3. Pedrotti--Salez, arXiv:2607.05345 (July 2026), proves the local-product criterion in terms of the non-equilibrium Poincare constant `gamma_*`, and obtains `gamma_* >= kappa` from Bakry--Emery curvature for deterministic starts. I did not find in that paper a common target-measure hypothesis verifying the required condition simultaneously for the three rates in Problem 2.7.
4. Chen--Kumagai, *Cutoffs for product chains*, SPA 128 (2018), 3840--3879, treats unequal-rate product chains and gives general cutoff criteria. This is direct prior art for the bounded-block benchmark below; I make no novelty claim for product-chain cutoff mechanisms.
5. Continuous-time path-space relative entropy / Girsanov formulas for jump processes are standard; e.g. Christian Leonard, *Girsanov theory under a finite entropy condition*, arXiv:1101.3958. The path-KL mechanism below is therefore not claimed as broadly novel.

Search strings included `"Problem 2.7" Salez weak dependency cutoff`, `Gibbs Metropolis square-root cutoff weak dependence`, `local product condition MCMC weak dependency`, `path space relative entropy Markov jump perturbation cutoff`, and `product chains two-state cutoff`. Bounded search found no source-matching later paper explicitly resolving Problem 2.7 for all three implementations. This negative search is **not** a worldwide novelty certificate.

---

## 3. Method #6: deform from any cutoff reference, not only from an independent cube

The previous proof compared an interacting target `pi` to a product target `nu`. The product structure was used in two places that should be separated:

1. **dynamic comparison of the two samplers:** product structure is not needed at all; path relative entropy only sees the local rate ratios;
2. **static comparison of the two equilibrium laws:** product structure was only a convenient way to show `||pi-nu||_TV=o(1)`.

This separation produces a more general transfer theorem.

For a full-support law `mu` on the cube, write

\[
r_i^\mu(x)=\frac{\mu(x^i)}{\mu(x)},\qquad u_i^\mu(x)=\log r_i^\mu(x).
\]

Keep the normalization used in the preceding R01 reports, in which the uniform target has flip rate `1/n`:

\[
c_{J,i}^\mu(x)=\frac1n g_J(u_i^\mu(x)),
\]
with
\[
g_G(u)=\frac{2e^u}{1+e^u},\qquad
 g_M(u)=\min\{1,e^u\},\qquad
 g_S(u)=e^{u/2}.
\tag{3.1}
\]

Their logarithms are Lipschitz with constants

\[
L_G=1,\qquad L_M=1,\qquad L_S=\frac12.
\tag{3.2}
\]

Let `nu_n` be an arbitrary full-support reference target on the cube and `pi_n` another full-support target. Put

\[
h_n=\log\frac{\pi_n}{\nu_n},\qquad
 d_{i,n}(x)=h_n(x^i)-h_n(x).
\tag{3.3}
\]

For sampler `J`, define the **path-information budget per unit time**

\[
\mathcal Q_{J,n}:=
\sup_x\sum_{i=1}^n
 c_{J,i}^{\nu_n}(x)
 e^{L_J|d_{i,n}(x)|}
 L_J^2 d_{i,n}(x)^2.
\tag{3.4}
\]

### R01-I0113-C003 — reference-cutoff transfer by path information

**STATUS: PROVED as a mathematical theorem in this report. It is a perturbation/transfer theorem, not by itself a source closure or a novelty claim.**

Assume that for one of the three samplers `J`, the chain with target `nu_n` exhibits worst-case total-variation cutoff with center `t_{J,n}` and window `w_{J,n}=o(t_{J,n})`. If

\[
\|\pi_n-\nu_n\|_{\rm TV}\to0
\tag{C003.1}
\]

and

\[
 t_{J,n}\,\mathcal Q_{J,n}\to0,
\tag{C003.2}
\]

then the `J`-sampler with target `pi_n` has cutoff at the same center `t_{J,n}` with the same window `w_{J,n}` in the usual two-limit sense.

The statement holds simultaneously for any fixed finite family of odds-response samplers whose `log g` is Lipschitz, with the obvious sampler-specific `L` and `Q`.

### Proof

Fix `n,J`, a starting state `x`, and time `t`. Let `P^pi_{x,[0,t]}` and `P^nu_{x,[0,t]}` be the two continuous-time path laws started from the same state.

By (3.3),

\[
u_i^{\pi}(x)-u_i^{\nu}(x)=d_i(x).
\]
Hence the Lipschitz property of `log g_J` gives

\[
\left|\log\frac{c_{J,i}^{\pi}(x)}{c_{J,i}^{\nu}(x)}\right|
\le L_J|d_i(x)|.
\tag{3.5}
\]

For two jump processes on the same positive-rate edges, the exact likelihood-ratio identity gives

\[
D(P^\pi_{x,[0,t]}\|P^\nu_{x,[0,t]})
=
E_{P^\pi}\int_0^t
\sum_i
\left[
 c_i^\pi\log\frac{c_i^\pi}{c_i^\nu}
-c_i^\pi+c_i^\nu
\right](X_s)\,ds.
\tag{3.6}
\]

Write

\[
z_i=\log(c_i^\pi/c_i^\nu).
\]
The bracket equals

\[
c_i^\nu F(z_i),
\qquad
F(z)=e^zz-e^z+1.
\]
Since

\[
F(z)=\int_0^z ve^v\,dv,
\]
we have for all real `z`

\[
0\le F(z)\le\frac12e^{|z|}z^2.
\tag{3.7}
\]

Combining (3.5)--(3.7) with (3.4), uniformly in the starting state,

\[
D(P^\pi_{x,[0,t]}\|P^\nu_{x,[0,t]})
\le\frac t2\mathcal Q_{J,n}.
\tag{3.8}
\]

Data processing from path space to the endpoint and Pinsker therefore yield

\[
\boxed{
\sup_x\|P^{\pi}_{J,t}(x,\cdot)-P^{\nu}_{J,t}(x,\cdot)\|_{\rm TV}
\le\frac12\sqrt{t\mathcal Q_{J,n}}.
}
\tag{3.9}
\]

For every fixed real `A`, take

\[
t=t_{J,n}+Aw_{J,n}.
\]
Because `w_{J,n}=o(t_{J,n})`, condition (C003.2) makes the right side of (3.9) `o(1)`. Together with (C003.1), the triangle inequality gives uniformly in `x`

\[
\left|
\|P^\pi_{J,t}(x,\cdot)-\pi_n\|_{\rm TV}
-
\|P^\nu_{J,t}(x,\cdot)-\nu_n\|_{\rm TV}
\right|=o(1).
\tag{3.10}
\]

Taking the maximum over `x` and then the two cutoff limits for the reference chain proves C003. QED.

### Adversarial checks

- If `pi_n=nu_n`, then `Q=0` and the theorem is exact.
- The earlier degenerate-product counterexample does not create a false positive: if the reference product chain itself has no cutoff, C003 has no hypothesis to transfer.
- Metropolis' kink at `u=0` is harmless: differentiability is never used, only the global Lipschitz bound on `log g_M`.
- The KL direction is important: (3.6) is `P^pi || P^nu`, giving the nonnegative scalar `F(z)` above.
- The theorem is not claiming stability under an `O(1)` perturbation of equilibrium: (C003.1) is explicit and cannot be silently dropped.

---

## 4. Method #12: the conserved/additive object is an information budget, not the worst coordinate

For a product reference

\[
\nu_n=\bigotimes_{i=1}^n\operatorname{Ber}(p_{i,n}),
\qquad \eta\le p_{i,n}\le1-\eta,
\tag{4.1}
\]

define the coordinate oscillations

\[
\delta_{i,n}:=\sup_x|d_{i,n}(x)|,
\qquad
A_n^2:=\sum_{i=1}^n\delta_{i,n}^2.
\tag{4.2}
\]

The preceding report replaced a first-order mismatch count by path KL, but still collapsed all coordinates to `Delta_n=max_i delta_i`. The exact path entropy is additive across jump channels, so the square-sum `A_n^2`, not `n Delta_n^2`, is the natural perturbative currency.

### R01-I0113-C004 — anisotropic all-three weak-interaction condition

**STATUS: PROVED. This strictly strengthens C002 whenever the interaction is spatially inhomogeneous.**

Under (4.1), if

\[
\boxed{
\log n\sum_{i=1}^n\delta_{i,n}^2\longrightarrow0,
}
\tag{C004.1}
\]

then all three samplers with invariant law `pi_n` exhibit worst-case total-variation cutoff at the same first-order centers as their product-reference chains, with `O_eta(n)` windows.

#### Static comparison

Expose the independent coordinates of `nu_n` one at a time. The Doob martingale of `h_n` has `i`th increment whose conditional range is at most `delta_{i,n}`: couple the unrevealed product coordinates identically after switching only coordinate `i`. Conditional Hoeffding therefore gives

\[
\log E_{\nu_n}\exp\{h_n-E_{\nu_n}h_n\}
\le\frac18\sum_i\delta_{i,n}^2
=\frac{A_n^2}{8}.
\tag{4.3}
\]

Since `E_nu e^h=1`,

\[
D(\nu_n\|\pi_n)=-E_{\nu_n}h_n\le\frac{A_n^2}{8}.
\tag{4.4}
\]
Thus Pinsker gives

\[
\boxed{
\|\pi_n-\nu_n\|_{\rm TV}\le\frac{A_n}{4}.
}
\tag{4.5}
\]

#### Dynamic comparison

Uniform marginal nondegeneracy gives a constant `M_eta` such that for all three reference samplers

\[
\sup_x c_{J,i}^{\nu_n}(x)\le\frac{M_\eta}{n}.
\tag{4.6}
\]

Also `delta_max <= A_n`, and all `L_J<=1`. Hence

\[
\mathcal Q_{J,n}
\le
\frac{M_\eta e^{A_n}}{n}A_n^2.
\tag{4.7}
\]

The retained product theorem from the preceding R01 reports gives

\[
t_{J,n}=\Theta_\eta(n\log n),
\qquad
w_{J,n}=O_\eta(n)
\tag{4.8}
\]

for each `J`. Condition (C004.1) makes both (4.5) and

\[
t_{J,n}\mathcal Q_{J,n}=O_\eta(\log n\,A_n^2)
\]
vanish. C003 applies separately to all three samplers. QED.

### Strict gain over C002

C002 used `Delta_n=max_i delta_i` and required

\[
n\log n\,\Delta_n^2\to0.
\]
C004 only requires

\[
\log n\sum_i\delta_i^2\to0,
\]
which is never stronger and can be much weaker.

For example, take the uniform product reference and

\[
\pi_n(x)\propto\nu_n(x)\exp\left\{\frac{x_1x_2}{\log n}\right\}.
\]
Then only coordinates `1,2` have nonzero oscillation, each equal to `2/log n`. Therefore

\[
\log n\sum_i\delta_i^2=\frac8{\log n}\to0,
\]
while

\[
n\log n\,\Delta_n^2=\frac{4n}{\log n}\to\infty.
\]
So C004 genuinely covers interacting targets excluded by C002.

---

## 5. Method #21: product-chain theory suggests a nonperturbative benchmark with bounded dependency components

The path-transfer theorem still asks `pi` and its reference equilibrium law to become close. That misses an obvious kind of weak dependence: **fixed-strength interactions inside uniformly bounded clusters**, repeated many times. Those interactions need not vanish with `n`, but the global process is a product of small interacting blocks.

Chen--Kumagai's product-chain theory is the correct literature neighborhood, so the following is recorded as a self-contained benchmark and mechanism check, **not as a novelty claim**.

### R01-I0113-C005 — bounded-block target measures have all-three cutoff

**STATUS: PROVED here; mechanism is product-chain theory / likely known. It does not by itself close Salez Problem 2.7.**

Assume `[n]` is partitioned into blocks

\[
[n]=B_{1,n}\sqcup\cdots\sqcup B_{m_n,n},
\qquad |B_{b,n}|\le K
\tag{5.1}
\]

for a fixed `K`, and

\[
\pi_n=\bigotimes_{b=1}^{m_n}\pi_{b,n}.
\tag{5.2}
\]

Assume a fixed `H<infinity` such that every one-coordinate log-odds inside every block obeys

\[
\left|\log\frac{\pi_n(x^i)}{\pi_n(x)}\right|\le H.
\tag{5.3}
\]

Then each of the Gibbs, Metropolis and square-root samplers has worst-case total-variation cutoff. Its mixing center is `Theta_{K,H}(n log n)` and it admits an `O_{K,H}(n)` cutoff window.

### Proof

Because (5.2) factorizes and coordinate flips never change two blocks, the continuous-time generator is a sum of commuting block generators; the semigroup is an exact tensor product over blocks.

For each block and sampler, scale time by `n` and write the block generator as `\widetilde L_{b,n}=nL_{b,n}`. From (5.3) and (3.1), every allowed scaled edge rate lies between constants

\[
0<a_H\le \widetilde c_i(x)\le b_H<\infty
\tag{5.4}
\]

depending only on `H` and the sampler; one pair of constants can be chosen for all three.

Moreover, (5.3) implies a uniform lower bound on every block atom. Any two block configurations differ by at most `K` flips, so their probability ratio is at most `e^{KH}`. Hence

\[
p_*:=2^{-K}e^{-KH}\le\min_{b,n,x}\pi_{b,n}(x).
\tag{5.5}
\]

Let `lambda_{b,n}` denote the spectral gap of `-\widetilde L_{b,n}`. There are constants

\[
0<\underline\lambda_{K,H}\le\lambda_{b,n}\le\overline\lambda_{K,H}<\infty
\tag{5.6}
\]

uniformly over `b,n` and the three samplers. For completeness, the lower bound follows from a shortest-path Poincare estimate on a connected cube of at most `2^K` vertices: every pair is connected by at most `K` edges and every undirected edge conductance is at least `p_*a_H`. The upper bound follows from the uniform bound `K b_H` on the scaled exit rate.

Put

\[
S_n(s):=\sum_{b=1}^{m_n}e^{-2\lambda_{b,n}s}
\tag{5.7}
\]

and let `s_n` be the unique solution of `S_n(s_n)=1`. Since `m_n>=n/K`, (5.6) gives

\[
\frac{\log m_n}{2\overline\lambda_{K,H}}
\le s_n\le
\frac{\log m_n}{2\underline\lambda_{K,H}},
\tag{5.8}
\]
so `s_n=Theta(log n)`.

For the **upper cutoff bound**, reversibility and the block spectral gap give, from any block starting state `x_b`,

\[
\chi^2(P^{(b)}_s(x_b,\cdot)\|\pi_b)
\le
(p_*^{-1}-1)e^{-2\lambda_{b,n}s}.
\tag{5.9}
\]

Chi-square tensorizes exactly:

\[
1+\chi^2_{\rm total}
=\prod_b(1+\chi_b^2)
\le\exp\{p_*^{-1}S_n(s)\}.
\tag{5.10}
\]

At `s=s_n+A`,

\[
S_n(s_n+A)\le e^{-2\underline\lambda A}.
\tag{5.11}
\]
Thus total variation tends uniformly to zero as first `n->infinity` and then `A->infinity`.

For the **lower cutoff bound**, for each block choose an `L^2(pi_b)`-normalized gap eigenfunction `phi_b` and a state `x_b` with

\[
|\phi_b(x_b)|\ge1.
\]
The bound (5.5) also gives `||phi_b||_infty^2<=p_*^{-1}`. Start the product chain from `x=(x_b)_b` and set

\[
T_s:=\sum_b
\phi_b(x_b)e^{-\lambda_{b,n}s}\phi_b(X_b(s)).
\tag{5.12}
\]

Under stationarity,

\[
E_\pi T_s=0,
\qquad
\operatorname{Var}_\pi(T_s)=
S_a(s):=\sum_b\phi_b(x_b)^2e^{-2\lambda_{b,n}s}.
\tag{5.13}
\]

Under the transient product law started from `x`, the eigenfunction identity gives

\[
E_xT_s=S_a(s),
\tag{5.14}
\]

while independence of blocks and `||phi_b||_infty^2<=p_*^{-1}` give

\[
\operatorname{Var}_x(T_s)\le p_*^{-1}S_a(s).
\tag{5.15}
\]

Also `S_a(s)>=S_n(s)`. At `s=s_n-A`,

\[
S_n(s_n-A)\ge e^{2\underline\lambda A}.
\tag{5.16}
\]

Chebyshev applied to the separating event `{T_s>=S_a(s)/2}` yields

\[
d_{\rm TV}(ns)
\ge
1-\frac{4(1+p_*^{-1})}{S_a(s)}.
\tag{5.17}
\]

Equations (5.11) and (5.16)--(5.17) prove a cutoff centered at

\[
t_n=ns_n=\Theta(n\log n)
\]

with window `n`. QED.

### What C005 does and does not say

C005 permits fixed, non-vanishing interactions within each bounded block. For example, a product of strongly but uniformly bounded Ising dimers is covered simultaneously for Gibbs, Metropolis and square-root rates.

However, this is still an independent-block model, and product-chain cutoff is an established literature mechanism. I do **not** present C005 as a resolution of the intended high-dimensional weak-interaction problem.

---

## 6. Combining the two new routes: strong local blocks plus a genuinely weak global perturbation

C003 can now be applied around the nonperturbative C005 reference instead of around a coordinate-product measure.

Let `nu_n` satisfy the bounded-block assumptions (5.1)--(5.3), and let `pi_n` be another full-support target. Set

\[
h_n=\log(\pi_n/\nu_n),
\qquad
\delta_{i,n}=\sup_x|D_i h_n(x)|,
\qquad
A_n^2=\sum_i\delta_{i,n}^2.
\]

### R01-I0113-C006 — bounded-block reference plus anisotropic weak perturbation

**STATUS: PROVED.**

If

\[
\boxed{
\log n\sum_i\delta_{i,n}^2\to0,
}
\tag{C006.1}
\]

then all three samplers with target `pi_n` exhibit cutoff, with the same first-order centers and `O_{K,H}(n)` windows as their `nu_n` bounded-block references.

### Proof

The blocks of `nu_n` are independent. The oscillation of `h_n` when the whole block `B_b` is resampled is bounded by

\[
\omega_b(h_n)\le\sum_{i\in B_b}\delta_{i,n}.
\]

Hoeffding's martingale argument over blocks therefore gives

\[
D(\nu_n\|\pi_n)
\le\frac18\sum_b\omega_b(h_n)^2
\le\frac K8\sum_i\delta_{i,n}^2.
\tag{6.2}
\]
Thus `||pi_n-nu_n||_TV=o(1)`.

The bounded local odds of the reference give

\[
\sup_x c_{J,i}^{\nu_n}(x)\le\frac{b_H}{n}.
\]
Hence, exactly as in (4.7),

\[
\mathcal Q_{J,n}
\le\frac{b_He^{A_n}}nA_n^2.
\tag{6.3}
\]

C005 gives `t_{J,n}=Theta(n log n)` and `w_{J,n}=O(n)`. Therefore (C006.1) implies `t_{J,n}Q_{J,n}->0`, and C003 finishes the proof for each `J`. QED.

This class has genuinely non-vanishing local dependencies inside blocks, plus an anisotropic global perturbation whose total path-information budget vanishes on the cutoff scale.

---

## 7. A natural dimension-free curvature route was tried and the exact failure is now isolated

The most tempting route to a much stronger answer is to use Salez Theorem 4.7 directly. For a coordinate-flip chain it defines

\[
\delta_i(x)=c_i(x)-\sum_{j\ne i}(c_j(x^i)-c_j(x))_+.
\]

If these are nonnegative, the theorem gives nonnegative sectional/Ollivier-type curvature and an MLSI lower bound for a general coordinate-flip chain. This condition can indeed be bounded in terms of changes of local log-odds and can be made common to Gibbs, Metropolis and square-root rates.

But the same theorem gives the **Bakry--Emery** curvature estimate only in the special square-root case. Salez's Theorem 5.3, which turns `alpha t_mix >> log log d` into cutoff for sparse chains, assumes `rho>=0` in the Bakry--Emery sense. Pedrotti--Salez's 2026 local-product theorem similarly obtains the easy deterministic-start bound on `gamma_*` from Bakry--Emery curvature.

Thus the currently imported machinery does **not** justify

\[
\text{common rate-influence condition}
\Longrightarrow
\text{all-three cutoff}
\]

at dimension-free interaction strength. The missing ingredient is one of:

1. a Bakry--Emery lower bound for Gibbs and Metropolis under a source-natural weak-dependency condition; or
2. a direct lower bound on the non-equilibrium Poincare constant `gamma_*` from the general sectional/Ollivier coupling of Theorem 4.7.

That is the next structural bottleneck; it is more informative than another tiny perturbative constant optimization.

---

## 8. Outcomes of the three new Section-B methods

### #6 DEFORM TO A POINT YOU CAN SOLVE

Instead of deforming only from the independent cube, C003 deforms from **any already-cutoff reference target**. Outcome: a reference-chain cutoff is stable whenever the stationary laws become close and the path-information budget satisfies `t_mix Q -> 0`. This is sampler-agnostic within the log-Lipschitz odds-response class.

### #12 FIND WHAT IS CONSERVED

The useful conserved/additive currency is not `max_i |D_i h|` but the cumulative path-space relative entropy. Its infinitesimal cost is a sum over jump channels and is quadratic in the local log-rate errors. Outcome: C004 replaces `n Delta^2` by the anisotropic square-sum `sum_i delta_i^2`.

### #21 ASK WHO ELSE HAS THIS SHAPE

Two mature literatures have exactly this shape: Girsanov/path-relative-entropy for jump processes, and cutoff for unequal-rate product chains. Outcome: (i) broad novelty is not claimed for C003's mechanism; (ii) C005 is explicitly treated as a product-chain benchmark; (iii) the source-specific contribution of the current route is the way these tools are assembled around the three odds-response MCMC rates and the identification of the all-three Bakry--Emery/gamma-star bottleneck.

---

## 9. Audit/checking budget

No new exact finite checker was manufactured in this run: C003--C006 are theorem-sized analytic claims and their complete arguments are on the page; there is no new finite enumeration whose truth depends on a certificate.

The newest complete R02/I0095 report formalizes the `17 x 17` discrepancy-7 witness. R01 already independently audited that exact finite metric claim in the preceding I0113 run (`R01-AUDIT-R02-I0095-A17-04 = PASS_FINITE_METRIC_CLAIM`). I did not spend the checking budget duplicating the same audit.

No P26 I0113 universal/source-fit audit was found, so no closure audit is fabricated.

## 10. Status, ledger delta, and next attack

The frozen source metric remains numerically maximal:

\[
M_3=3/3.
\]

There is therefore **no metric movement** this run even though the sufficient condition has become strictly broader. I0113 remains

**PARTIAL / PROVED-CANDIDATE, NOT CLOSED.**

Why not closed:

- C003--C006 are perturbative/product-block sufficient conditions; the intended high-dimensional weak-dependence regime is broader.
- broad mechanisms used are standard and require prior-art/source-fit classification.
- the required P26 plus a second independent source-level audit of the actual I0113 package have not both been completed.

Structured `ledger_delta` for P26:

```yaml
ledger_delta:
  track: R01
  canonical_id: I0113
  source: "Justin Salez, Modern aspects of Markov chains, arXiv:2508.21055, Problem 2.7"
  target: "one weak-dependency condition on pi_n implying cutoff for Gibbs, Metropolis, and square-root coordinate samplers"
  metric: "M_3 = number of the three source samplers covered by one common proved condition"
  before: "3/3"
  after: "3/3"
  status: "PARTIAL / PROVED-CANDIDATE; not closed"
  unchanged_count: 2
  tried_moves: [6, 12, 21]
  exact_evidence:
    - "R01-I0113-C003: general path-information reference-cutoff transfer theorem"
    - "R01-I0113-C004: log n * sum_i delta_i^2 -> 0 suffices relative to nondegenerate product reference"
    - "R01-I0113-C005: bounded-block product targets have all-three cutoff; product-chain mechanism, no novelty claim"
    - "R01-I0113-C006: bounded-block reference plus anisotropic perturbation"
  audit_ids:
    incoming_P26: "PENDING / not found"
    incoming_second: "PENDING"
    outgoing_R02: "R01-AUDIT-R02-I0095-A17-04=PASS_FINITE_METRIC_CLAIM (prior run; not duplicated)"
  remaining_obligation: "dimension-free all-three route: prove BE/gamma_* control for Gibbs and Metropolis from a common weak-dependency condition; plus source-fit/prior-art and two independent audits"
```

If the frozen metric remains unchanged on the next invocation, the unchanged count reaches three and the binding stuck protocol should fire. The next distinct Section-B methods selected in advance are:

- **#1 CHANGE THE CATEGORY:** formulate the missing all-three step as a comparison problem for edge-conductance geometries / Gamma2 matrices rather than as three separate MCMC proofs;
- **#19 MAKE IT AN ALGORITHM:** construct a local semidefinite test for Bakry--Emery curvature of coordinate-flip generators under symbolic rate-influence bounds;
- **#28 REPLACE FOR ALL WITH TYPICAL:** test whether `gamma_*` can be controlled along the actual non-equilibrium path without statewise nonnegative Bakry--Emery curvature.

## 11. Model/scheduler escalation status

Still unchanged. The exposed task-management interface has controls for title/prompt/schedule/timing/enabled state but no model field, no reasoning-effort field, and no authenticated runtime-model telemetry. Therefore prompt text can request GPT-6 / maximum but cannot enforce or verify it here. Actually changing this requires a product/owner/platform interface that exposes task-level model and reasoning controls, or platform support/ownership migration.

The historical P26 `You cannot modify this task` result is preserved in `operations/RFLEET_2026-09-16.md`; later authorized contexts could modify some P/C tasks, showing the refusal is permission/context-specific. The supported workaround is an owner-authorized task-management context or platform support/ownership transfer, not duplicate schedules or a permission bypass.

No scheduler changes were attempted in this run, in compliance with the current GitHub-only operational contract.
