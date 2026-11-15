# T032: verification of the OpenAI Bose-gas preprints

Original dossier: 14 November 2026; round-6 continuation: 15 November 2026. All three main theorem quotations below were checked against introductions freshly opened in round 6. This round independently rechecks round 5’s conditional reference law and verifies Section 8’s Skeleton encounters lemma. It does not judge the full condensation proofs correct. All three manuscripts name **OpenAI** as author. The sources were read through the connected GitHub reader; local copies are under `sources/0`, `sources/1`, and `sources/2` respectively. The source entry points are `build/main.tex`, not `paper.tex`.

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

## Follow-ups actually opened in round 6

The update search was bounded to five minutes. Queries were the exact positive-temperature title, openai/math Bose error, and interacting homogeneous Bose condensation proof 2026. No later settlement, separate arXiv version of the three manuscripts, paper-specific refutation, or completed referee endorsement was found in this search. This is a limited search result, not a claim that none exists.

| Opened source | Finding |
| --- | --- |
| [Repository root](https://github.com/openai/math), [history.md](https://raw.githubusercontent.com/openai/math/main/history.md) | Latest listed history entry remains October 29, 2026. No Bose-family correction or withdrawal appears. |
| [Lean scope note 267](https://raw.githubusercontent.com/openai/math/main/lean/docs/267.md) | Explicitly ground-state condensation, including pure and mixed ground states, without a positive-temperature assertion. The Comparator challenge was read from the inherited local archive; no Lean solution build was run. |
| [arXiv:2611.05293](https://arxiv.org/abs/2611.05293) | Mohamed El Hedi Bahri and Ian Jauslin, *The Lee-Huang-Yang Formula in the Hard-Core Simplified Approach to the Bose gas*, submitted November 3, 2026; the opened page still lists v1 only. It proves asymptotics in a ground-state Simple Equation approximation and does not settle the exact positive-temperature many-body model. |
| All three candidate introductions linked above | Freshly opened with the read-only GitHub reader. All three main theorem quotations agree exactly with the inherited dossier. Local copies: sources/introduction-round6-0.tex, sources/introduction-round6-1.tex, sources/introduction-round6-2.tex. |
| [Positive-temperature groups.tex](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/groups.tex) | Reopened the exposure and allocation definitions and conditional law. The source body agrees with the inherited copy after trailing-newline normalization. |
| [Positive-temperature lattice.tex](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/lattice.tex) | Reopened the explicit skeleton law and Skeleton encounters statement and proof. Raw web opening failed with Cache miss; the connected GitHub reader succeeded. This is the principal source for the new verification. |

The three candidates' OpenAI author declarations, the exact HardSphere Comparator statement, and the temperature-rescaling sources were read from the earlier local archive rather than fetched again. Earlier workers' external reviews are inherited evidence; [ROUND5_VERIFY.md](ROUND5_VERIFY.md) and [PRIOR_VERIFY.md](PRIOR_VERIFY.md) preserve those records without presenting them as new expert endorsements. Round-6 source URLs and saved hashes are recorded in [ROUND6_SOURCES.json](sources/ROUND6_SOURCES.json).

## Independent recheck of round 5

The earlier result holds, assuming the displayed thermal slab density. Section 1 of [PROOF.md](PROOF.md) rederives the conditional law directly by factoring the joint Radon–Nikodym derivative on each exposed fiber. Fixing all eligibility indicators makes the allocation kernel constant; confinement selects exactly one Euclidean winding term; its endpoint weight cancels. Positive fiber mass then gives positive individual and mutual-avoidance normalizers almost everywhere under the sampled exposure. This gives no uniform lower bound and does not make the retained paths independent.

The separate exact finite-state check uses four labels at two sites, four path states, nonuniform weights, variable eligible-list sizes, frozen paths, and both frozen and retained collision checks. It compares normalized conditional laws from the full joint allocation distribution against the proposed factorization by cross multiplication of exact rational masses. It does not execute or modify the round-5 script. The earlier complete argument is preserved in [ROUND5_PROOF.md](ROUND5_PROOF.md).

## Spot check

This round verifies Section 8's Lemma 8.2, Skeleton encounters, for the explicit skeleton law before obstacle detours. [PROOF.md](PROOF.md) quotes the lemma exactly and supplies a full analytic derivation. It checks the source's filtration, including already revealed large blocks, by choosing a fresh aligned block wholly inside every future interval. Its independent transverse uniforms give a conditional density at most C_* k^(-3/2), where C_*=2/c_vel^2. The series over future times is summable.

The folded-time and rounding comparison is deterministic: J_occ is at most 20 times the number of same-unfolded-time tests D_t<=3R+5. The soft count is at most 10 exp(5/(3B)) times the sum of exp(-D_t/(3B)). These comparisons include the endpoints, the shared middle, the at-most-five-step refinement, both signs of the drift, and torus wrapping. Conditioning the final-index sum at the preceding time gives the ordered-product bounds used in the exponential expansion.

Explicit sufficient constants are c_hit=1/[80(1+192C_*)] and C_hit=2 for the hard encounter moment. For the soft moment, xi(B)=1/[40(1+216C_*B^2) exp(5/(3B))] and C(B)=2 suffice. The square-shell and layer-cake calculations independently give the soft integral 72B^2. No gap was found in this lemma. These bounds even hold after the independent opposing array has been fixed; they are not assertions about a fixed common obstacle environment after detours.

The audit command is `nice -n 15 env OMP_NUM_THREADS=1 python3 -B audit.py`; its output is recorded in [LOG.md](LOG.md). It passed 58 positive four-state conditional-law fibers, 65,792 fresh-block checks, 1,800 rational folded/refined path pairs and 998,752 occurrence inequalities, plus constant, quotation and local-link checks. Peak memory was 18,776,064 bytes, with inherited nice 20 and one thread. An initial manifest-path failure and consequent missing-link audit failure were corrected; no mathematical check failed. The script performs no Monte Carlo, many-body calculation, or Lean build.

The detour charging inequality and common-environment component expansion later in Section 8 remain unverified. Thermal certificate estimates in Section 5 also remain unverified; the local checks here do not certify the full positive-temperature proof. The next worker should check the passage from skeleton encounters to adapted good-path encounters, starting at the displayed inequality labelled lattice:detour-charge.

## Recommended replacement “where it stands”

OpenAI's unrefereed preprint *Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas* (October 5, 2026) claims a positive constant-orbital condensate fraction for three-dimensional hard spheres at sufficiently small fixed density and fixed low positive temperatures in the thermodynamic limit. Its documented Lean theorem concerns ground states, and the local lemmas checked here do not verify the full positive-temperature proof. The claim is restricted to dilute hard spheres and does not itself state a pointwise infinite-distance limit of the one-body kernel, so the row in its full generality remains unestablished by this release.
