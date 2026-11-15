# T032: verification of the OpenAI Bose-gas preprints

Original dossier: 14 November 2026; round-5 continuation: 15 November 2026. The theorem quotations below have been checked against newly opened source files. This round independently rechecks the preceding collision estimate and verifies the exact conditional bridge law after exposure and allocation. It does not judge the full condensation proofs correct. All three manuscripts name **OpenAI** as author. The sources were read through the connected GitHub reader; local copies are under `sources/0`, `sources/1`, and `sources/2` respectively. The source entry points are `build/main.tex`, not `paper.tex`.

## 1. Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas

OpenAI; October 5, 2026. [Manuscript source](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/introduction.tex). Theorem 1.1, copied exactly from the TeX:

```tex
\begin{theorem}\label{thm:main}
For every $a>0$, there is $\rho_*(a)>0$ such that for each fixed
$0<\rho<\rho_*(a)$ there is a fixed temperature $T=T(a,\rho)>0$ for which
\[
 \liminf_{\substack{L\to\infty\\N/L^3\to\rho}}
 \frac{\langle u_{0,L},\gamma^{(1)}_{N,L,T}u_{0,L}\rangle}{N}>0.
\]
The exclusion distance, density, and temperature are held fixed in this
limit.
\end{theorem}
```
## 2. Ground-state condensation in the dilute hard-sphere gas

OpenAI; September 24, 2026. [Manuscript source](https://github.com/openai/math/blob/main/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/build/sections/introduction.tex). Theorem 1.1, copied exactly from the TeX:

```tex
\begin{theorem}[Condensation in every ground state]\label{main:theorem}
There are absolute constants $\varepsilon_0,c_0>0$ with the following
property. Fix $a,\rho>0$ satisfying $\rho a^3<\varepsilon_0$.
For every sequence of particle numbers $N_k$ and lengths $L_k$ such that
\[
 N_k\longrightarrow\infty,\qquad L_k\longrightarrow\infty,
 \qquad \frac{N_k}{L_k^3}\longrightarrow\rho,
\]
and every choice of normalized, possibly complex, bosonic ground
eigenvectors $\Psi_k$ of the hard-sphere Hamiltonians,
\begin{equation}\label{main:limit}
 \liminf_{k\to\infty} B(\Psi_k)\ge c_0.
\end{equation}
\end{theorem}
```

## 3. Quantum Depletion and Momentum Distribution in the Dilute Hard-Sphere Bose Gas

OpenAI; October 5, 2026. [Manuscript source](https://github.com/openai/math/blob/main/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/build/sections/introduction.tex). Theorem 1.1, copied exactly from the TeX:

```tex
\begin{theorem}\label{thm:main}
For every $a>0$, every bounded continuous real function $f$ on $\R^3$,
and every $\eps>0$, there is $\rho_0(a,f,\eps)>0$ with the following
property. Fix $0<\rho<\rho_0$ and put $\eta=\rho a^3$. For every
sequence $N_j,L_j\longrightarrow\infty$ with
$N_j/L_j^3\longrightarrow\rho$,
\begin{equation}\label{intro:main-limit}
 \limsup_{j\to\infty}\ \sup_{\Gamma\in\mathcal G_{N_j,L_j,a}}
 \left|
 \frac{1}{N_j\sqrt\eta}
 \sum_{\substack{k\in(2\pi/L_j)\Z^3\\k\ne0}}
 f\!\left(\frac{k}{\sqrt{8\pi\rho a}}\right)n_{\Gamma,L_j}(k)
       -\int_{\R^3}f\,\dd\nu_{\mathrm{Bog}}
 \right|\le\eps.
\end{equation}
\end{theorem}
```

## Comparison with our statement

Our statement is: “The interacting Bose gas in three dimensions (for example with a repulsive pair potential), in the thermodynamic limit at fixed density, condenses at low temperature: the one-body density matrix has off-diagonal long-range order.”

| Words in our row | Positive-temperature paper | Ground-state paper | Quantum-depletion paper |
| --- | --- | --- | --- |
| “interacting Bose gas” | Exact continuum many-body canonical Gibbs state, not an ideal gas or a permutation surrogate. | Exact continuum bosonic ground eigenvectors; the corollary includes all ground-space density operators. | Exact continuum ground-space density operators, uniformly over pure and mixed ground states. |
| “in three dimensions” | Exactly three, on a periodic flat torus. | Exactly three, same geometry. | Exactly three, same geometry. |
| “for example with a repulsive pair potential” | Hard-sphere exclusion only: infinite repulsion when a pair is too close, zero outside. This is an interacting repulsive model, but no theorem here covers arbitrary repulsive potentials. | Same hard-sphere restriction. | Same hard-sphere restriction. |
| “thermodynamic limit at fixed density” | Yes: N/L³ tends to a fixed positive ρ, with a and positive T also fixed. Only sufficiently small ρa³ is covered. | Yes: a and sufficiently small positive ρa³ are fixed before N,L tend to infinity. | Yes first, then ρa³ tends to zero. The theorem controls all thermodynamic accumulation values; it does not assert a unique occupation limit at each fixed density. |
| “at low temperature” | Main Theorem 1.1 asserts existence of one volume-independent T>0 for each sufficiently small fixed density. The stronger scaled theorem in the body also yields an interval of fixed low positive temperatures; see below. | Zero temperature only; a ground-state theorem alone gives no volume-uniform positive-temperature conclusion. | Zero temperature only. |
| “one-body density matrix” | Yes: trace-N one-body density matrix and its specified constant-mode eigenvalue. | Yes: constant-orbital occupation fraction B(Ψ). | Yes: the full scaled nonzero-momentum occupation measure, including its total mass. |
| “off-diagonal long-range order” | A positive lower limiting constant-mode occupation fraction is asserted. This is macroscopic-mode BEC and spatially averaged long-range coherence. A pointwise infinite-distance kernel limit is not stated. | Same occupation criterion at T=0, not a pointwise kernel-limit theorem. | Stronger dilute asymptotic information on momentum occupations at T=0, but still no stated pointwise infinite-distance kernel limit. |

The hard-sphere Hamiltonian in all three papers is the Dirichlet realization of −ΣᵢΔᵢ on configurations with pair distances greater than a; the ambient box is periodic. Here a denotes the exclusion distance between centers and the scattering length, so it must not silently be read as a geometric sphere radius with diameter 2a. None of these three main theorems covers arbitrary densities, arbitrary pair interactions, a trap, other dimensions, or the critical temperature.

For the ground-state theorem,
\[
B(\Psi)=N^{-1}\langle\varphi_{0,L},\Gamma_\Psi^{(1)}\varphi_{0,L}\rangle,
\qquad \varphi_{0,L}=L^{-3/2}.
\]
It is a positive lower bound, uniform over sufficiently small gas parameters and all ground states. It does not claim B tends to one. The mixed-state conclusion is Corollary 1.2 of that paper.

In the depletion theorem, \(\mathcal G_{N,L,a}\) is the set of positive trace-one operators supported on the lowest bosonic eigenspace, \(n_{\Gamma,L}(k)=\langle u_{k,L},\gamma_\Gamma^{(1)}u_{k,L}\rangle\), and
\[
\nu_{\mathrm{Bog}}(dt)=\frac{(8\pi)^{3/2}}{(2\pi)^3}
\left(\frac{|t|^2+1}{2\sqrt{|t|^4+2|t|^2}}-\frac12\right)dt.
\]
Its total mass is \(8/(3\sqrt\pi)\). Taking f=1 gives the claimed depletion fraction \(1-B=(8/(3\sqrt\pi))\sqrt{\rho a^3}+o(\sqrt{\rho a^3})\), in thermodynamic-then-dilute order. This is an asymptotic for ground states, not a thermal depletion law or an exact fixed-density formula.

### Temperature interval stated in the body

[Section 2 source](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/setup.tex) gives Theorem 2.1, copied exactly:

```tex
\begin{theorem}[Scaled occupation bound]\label{thm:scaled}
There are constants $\alpha_0\ge2$, $D_*<\infty$, and $c_*>0$ such that
$B_{\rm occ}\ge c_*$ whenever the parameters satisfy
\eqref{eq:scaled-parameters}, $D\ge D_*$, and $K$ is sufficiently large.
The lower threshold for $K$ can be chosen locally uniformly for $D$ in
$[D_*,\infty)$, uniformly in $\alpha\in[\alpha_0/2,2\alpha_0]$ and
$0<T\le D^{-1}$.
\end{theorem}
```

Here the scaled parameters are V=K³, D=N/V, r=α/D, α∈[α₀/2,2α₀] and 0<T≤D⁻¹. The [final section](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/conclusion.tex) takes
\[
s_\infty=\sqrt{\frac{\alpha_0}{a\rho}},\qquad
D_\infty=\frac{\alpha_0^{3/2}}{\sqrt{\rho a^3}},\qquad
T_0=\frac{1}{4s_\infty^2D_\infty}
=\frac{a^{5/2}\rho^{3/2}}{4\alpha_0^{5/2}}.
\]
For each fixed physical 0<T≤T₀, the scaled DT tends to a value at most 1/4, hence is eventually below one. Thus Theorem 2.1 and the displayed rescaling also claim a uniform positive occupation bound throughout a low-temperature interval. This is an implication of two explicit statements in the paper; the headline theorem alone only says “there is a fixed temperature.” The constants and density threshold come from the argument; there is no sharp critical-temperature claim.

### The precise ODLRO distinction

For the translation-invariant thermal kernel write \(\gamma^{(1)}_L(x;y)=g_L(x-y)\) and \(\rho_L=N/L^3\). Direct integration gives
\[
\frac{\langle u_{0,L},\gamma^{(1)}_Lu_{0,L}\rangle}{N}
=\frac{1}{\rho_LL^3}\int_{\Lambda_L}g_L(r)\,dr.
\]
The paper therefore addresses the one-body matrix itself, not merely permutation cycles or energy. If our term ODLRO means macroscopic constant-mode occupation, this part of the criterion matches for dilute hard spheres. If it requires an infinite-volume kernel followed by a positive pointwise limit as |x−y|→∞, the quoted results do not state that stronger conclusion or justify those limit exchanges. No claim of a counterexample to such an implication for this gas is made here.

## Follow-ups and sources opened in round 5

The bounded web search used the exact positive-temperature title with OpenAI, the folder name with error, and Bose hard-sphere condensation 2026 proof positive temperature. No later settlement, separate arXiv version of these manuscripts, paper-specific refutation, error report, or completed specialist referee endorsement was located. This records a limited search, not a claim that none exists.

| Actually opened | Observation |
| --- | --- |
| All three candidate `build/main.tex` and `build/sections/introduction.tex` files, linked above | Each author is OpenAI. The main theorem quotations above agree exactly with the freshly opened introductions. |
| [Positive-temperature groups.tex](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/groups.tex) | Read the full exposure/allocation construction, Lemma 7.2 and its proof, and the later accessibility/comparison definitions. This is the principal source for the new check. |
| [Positive-temperature slab.tex](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/slab.tex) | Read the thermal slab density, purification formula and regularity definition. The conditional-law check starts from the displayed density; it does not audit the certificate proof. |
| [Positive-temperature bridges.tex](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/bridges.tex) | Read the single-replacement estimate and its deterministic prerequisites to recheck round 4. Current groups/slab/bridges bodies match the prior archive after stripping trailing newlines. |
| [Repository history](https://github.com/openai/math/blob/main/history.md) | Latest listed entry is October 29, 2026; no Bose-family correction or withdrawal appears. An initial uppercase `HISTORY.md` guess returned 404 and was replaced by this correct path. |
| [Lean scope note 267](https://github.com/openai/math/blob/main/lean/docs/267.md), [HardSphere Comparator challenge](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HardSphere.lean) | Scope is ground-state condensation. The selected theorem `OAI.HardSphere.condensation_with_mixed` quantifies ground vectors and ground-supported density operators; it does not assert positive-temperature condensation or the sharp depletion law. The challenge's terminal `sorry` is a challenge placeholder, not an audit of the separate solution. No Lean build was run. |
| [arXiv:2611.05293](https://arxiv.org/abs/2611.05293), [HTML v1](https://arxiv.org/html/2611.05293v1) | Mohamed El Hedi Bahri and Ian Jauslin, *The Lee-Huang-Yang Formula in the Hard-Core Simplified Approach to the Bose gas*, submitted November 3, 2026, still v1 on the opened page. Its introduction says the machine-generated condensation announcement is under review; its own theorem concerns the hard-core Simple Equation approximation at zero temperature. It neither settles our exact positive-temperature model nor validates the OpenAI argument. |

Fresh source copies use `sources/*-current.*`; [ROUND5_SHA256.json](sources/ROUND5_SHA256.json) records their hashes. Source URLs are given above and in [ROUND5_SOURCES.json](sources/ROUND5_SOURCES.json). The source files for the temperature rescaling were also read locally from the earlier archive: [setup.tex](sources/setup.tex) and [conclusion.tex](sources/conclusion.tex).

Earlier workers opened the repository README, the three candidate READMEs, Lean catalogue and solution entry module, MathVet's fidelity and challenge-status records, Carlos Toledo's cert-machine statement/kernel records, and Plectis Atlas's family/statement pages. Their records distinguish the ground-state formal statement from the positive-temperature and depletion headlines. Those external assessments were not reopened in this round and are not presented as new expert reports; the inherited account and links are preserved in [PRIOR_VERIFY.md](PRIOR_VERIFY.md), with local family extracts in `sources/reviews/`.

## Independent recheck of the earlier result

Round 4's result was Lemma 6.3's deterministic collision estimate, under unconditioned free bridge laws. Its full proof is preserved as [ROUND4_PROOF.md](ROUND4_PROOF.md); round 3's conditional insertion calculation is [ROUND3_PROOF.md](ROUND3_PROOF.md).

A fresh derivation appears in Section 1 of [PROOF.md](PROOF.md). Gaussian conditioning gives the residual covariance and independence needed for early mesh intervals. On late intervals, conditioning on the entire centered fluctuation leaves the uniformly sampled midpoint with density at most eight, without a false independence assertion about increments. The independent integral test gives a mesh sum at most eight divided by tau times the square root of h0; combined with the regularity maximum, this produces the same D to the power minus one quarter. The sum part of regularity gives the other term, of order tr. Endpoint exclusion, fixed-t quantifiers and the unique local lift are retained. The earlier result holds in the stated large-torus regime.

## Spot check

This round checks the next outstanding dependency, Lemma 7.2, “Exact conditional law.” [PROOF.md](PROOF.md) quotes it exactly and gives every step of the local derivation from the displayed thermal slab density.

At fixed endpoint configurations and purification variable, the outer symmetric heat kernels are constants and the remaining free reference is a product of torus bridges weighted by hard avoidance. Every retained label has eligibility indicator one; after the endpoints are fixed, this restricts only its own regularity and confinement. A specified ordered allocation has probability the reciprocal of a falling factorial in the number of eligible labels at each site. These lists are exposed, so this probability is constant on the conditional fiber, even though it varies between fibers. The paths outside the retained group are fixed; their eligibility indicators and mutual avoidance add only fixed factors.

For a retained path, radius-ten confinement on a torus of side greater than twenty selects exactly the near-endpoint Euclidean lift. The winding-mixture weight is the Euclidean heat kernel divided by the torus heat kernel at those endpoints. It is a positive constant and cancels in normalization. Thus the only remaining weights are individual cutoff/frozen-path success indicators and mutual avoidance between retained paths. A positive raw conditional integral implies each individual reference normalizer and the mutual-avoidance normalizer is positive for almost every sampled exposure. This does not give uniform lower bounds, and the resulting law is a conditioned product, with dependencies.

No hidden path-dependent allocation or winding weight was found under the stated exposure. The source explicitly excludes full-sample certificate conditioning; adding such a condition could change the law, as an exact two-variable example in the proof demonstrates. The large-torus hypothesis is also necessary for the particular single-lift argument. Empty groups and null exposed fibers are treated explicitly.

The exact finite-state audit enumerates two sites with three labels each, three path states with nonuniform rational weights, all compatible eligibility vectors and ordered two-group allocations, frozen paths, and both kinds of collision checks. It compares the conditional law obtained from the full joint density with the proposed product law normalized after mutual avoidance. This is an algebraic stress test of the dependence calculation, not a Brownian-path simulation or a proof checker. The analytic path-space derivation supplies the actual lemma verification.

Validation command: `nice -n 15 env OMP_NUM_THREADS=1 python3 -B audit.py`. The audit also checks the theorem/lemma quotations, author lines, Gaussian covariance identities, elementary constants, Lean scope and resource limits. It passed all checks, including agreement on 346 positive exposed fibers (50 admissible path samples and 392 joint allocation records); measured peak RSS was 18,956,288 bytes with inherited nice 20. Its output and two corrected macOS resource-limit setup failures are recorded in LOG.md. No many-body calculation or Lean build was attempted.

The conditional reference-law assumption can now be removed from the earlier local insertion calculation, assuming the displayed thermal slab representation. The thermal certificate estimate in Section 5 and the route encounter estimate in Section 8 remain unverified. A useful next step is Section 8's “Skeleton encounters” lemma (`lem:skeleton`): check the dyadic-block conditional density estimate and its exponential-moment deduction, including the folded-time and periodic-distance comparisons. The subsequent detour argument would still need a separate check.

## Recommended replacement “where it stands”

OpenAI's unrefereed preprint *Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas* (October 5, 2026) claims a positive constant-orbital condensate fraction for three-dimensional hard spheres at sufficiently small fixed density and fixed low positive temperatures in the thermodynamic limit. The documented Lean theorem covers ground states, and the local lemmas checked here do not verify the full positive-temperature proof. This is a claim for a special interacting model and does not itself state a pointwise infinite-distance limit of the one-body kernel, so it does not establish the row in its full generality.
