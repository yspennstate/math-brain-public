# T032: verification of the OpenAI Bose-gas preprints

Original dossier: 14 November 2026; round-3 and round-4 continuations: 15 November 2026. This records the claims, their scope, a conditional insertion check and a direct check of its deterministic collision input. It does not judge the full condensation proofs correct. All three manuscripts name **OpenAI** as author. The sources were read through the connected GitHub reader; local copies are under `sources/0`, `sources/1`, and `sources/2` respectively. The source entry points are `build/main.tex`, not `paper.tex`.

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

## Follow-ups opened by the earlier worker

1. **OpenAI's own scope and update records.** Opened the [repository README](https://raw.githubusercontent.com/openai/math/main/README.md), [history](https://github.com/openai/math/blob/main/history.md), each candidate's README, [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), [family 267 scope note](https://github.com/openai/math/blob/main/lean/docs/267.md), [HardSphere statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HardSphere.lean), [Comparator configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HardSphere.json), and [solution entry module](https://github.com/openai/math/blob/main/lean/OAI/Analysis/HardSphere/Main.lean). The scope note restricts the formalization to ground-state condensation. The selected declaration is OAI.HardSphere.condensation_with_mixed; its state variables are ground vectors and ground-supported density operators, not positive-temperature Gibbs states. Neither the positive-temperature conclusion nor the sharp depletion law is covered by that selected statement. The current candidate READMEs contain no withdrawal notices, and the opened repository history contains no Bose-family correction. The solution entry module imports the underlying development; reading it is not a replay or an audit of all its dependencies.

2. **MathVet's statement-scope assessment and machine report.** Opened the primary [fidelity CSV](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/fidelity-table.csv), [fidelity JSON](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/fidelity-table.json), and [challenge-status JSON](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/challenge-status.json). The family-267 assessment says the formal statement is weaker than the family headline: it omits positive temperature and the sharp depletion law. The HardSphere record reports a sandboxed Comparator acceptance completed 8 October 2026. This is a reported check of the selected Lean statement, not a referee endorsement of the positive-temperature manuscript. Family-specific extracts are saved in sources/reviews/.

3. **Carlos Toledo's cert-machine.** Opened the primary [statement assessment](https://github.com/carlostoledo1891/cert-machine/blob/main/certs/openai-math-statements.json) and [kernel report](https://github.com/carlostoledo1891/cert-machine/blob/main/certs/openai-math-kernel.json). Family 267 is assessed as narrower than, and not linked to all of, the headline claims. The HardSphere run is reported accepted by both Lean and nanoda on 10 October 2026, at release revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb. This does not extend the formal theorem's temperature or observable scope. The reports were read; no local Lean build was attempted under the task's compute limit.

4. **Exposition/index.** Opened Plectis Atlas's [HardSphere statement page](https://wcook04.github.io/plectis-atlas/statements/HardSphere.html) and [family 267 page](https://wcook04.github.io/plectis-atlas/families/267.html). They put the paper and formal statements side by side and link the preceding reports. Their descriptions of the paper-to-Lean mapping are explicitly AI-assisted and lack recorded human review; the primary scope note and declarations were checked directly above. This is exposition and evidence indexing, not a new proof or a specialist referee report.

5. **Later mathematical paper and expert comment.** Opened [arXiv abstract 2611.05293](https://arxiv.org/abs/2611.05293) and [the full HTML paper, version 1](https://arxiv.org/html/2611.05293v1): **Mohamed El Hedi Bahri and Ian Jauslin**, *The Lee-Huang-Yang Formula in the Hard-Core Simplified Approach to the Bose gas*, submitted 3 November 2026. Its introduction describes the machine-generated thermodynamic condensation announcement as still under review and not yet published in a scientific journal; reference [28] points to OpenAI's ground-state manuscript and identifies it as unrefereed. Their own theorem concerns the hard-core Simple Equation approximation, not the exact many-body Gibbs state, and is not a verification or refutation of the OpenAI proof.

Searches used each exact title with arXiv, criticism, error, refutation, gap and referee terms, and broader combinations of OpenAI, Bose and hard-sphere. No arXiv version of any of the three OpenAI manuscripts, explicit refutation, paper-specific error report, or completed specialist referee endorsement was located in those searches. This is a bounded search finding as of 14 November 2026, not a guarantee that none exists.

Several other exposition leads appeared in search: AIProofWatch, Math singularity, Closed Form, OpenAI Math Readings, and we-solve. Direct page opens failed with cache or accessibility errors; those snippets are not used as evidence for the verdict. The attempted links and failures are recorded in LOG.md. The initially guessed paper.tex and build/paper.tex URLs also failed; actual main.tex and included introduction.tex files were subsequently opened.

## Round 4: fresh openings and bounded follow-up check

The follow-up search was completed within five minutes of starting this continuation. Web queries included the exact positive-temperature title; `openai/math condensation error correction arxiv`; `openai hard-sphere single replacement error`; and the exact positive-temperature title with `arxiv correction November 2026`. No new settlement, paper-specific correction, separate arXiv version, completed specialist verification or refutation was located. This is a bounded search result, not evidence that no such item exists.

The following were actually reopened in this session:

| Source opened | What was checked |
| --- | --- |
| Each of the three candidate `build/sections/introduction.tex` files linked above | Main theorem blocks match the quotations above exactly. All five freshly fetched introduction/bridge/slab source bodies agree with the previous archive after stripping final newlines. |
| [Positive-temperature bridges.tex](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/bridges.tex) | Entire deterministic collision argument, especially Lemma 6.3, its mesh construction, midpoint quantifier and dependence on regularity. |
| [Positive-temperature slab.tex](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/slab.tex) | Definition 5.2 of regularity and the cutoff inputs; the thermal certificate argument was not verified. |
| [Repository history](https://github.com/openai/math/blob/main/history.md) | No Bose-family correction or withdrawal in the opened current record; latest listed entry is October 29, 2026. |
| [Lean scope note 267](https://github.com/openai/math/blob/main/lean/docs/267.md) | Explicitly restricts the formalization to ground states and says it has no positive-temperature assertion. No Lean build was run. |
| [arXiv:2611.05293](https://arxiv.org/abs/2611.05293), [HTML v1](https://arxiv.org/html/2611.05293v1) | Mohamed El Hedi Bahri and Ian Jauslin, *The Lee-Huang-Yang Formula in the Hard-Core Simplified Approach to the Bose gas*, submitted November 3, 2026, still version 1 on the opened page. Its introduction calls the machine-generated announcement under review; its own condensate result concerns the Simple Equation approximation, rather than the exact many-body Gibbs state. |

Fresh files are named `sources/*-current.*`. Their SHA-256 values are in [ROUND4_SHA256.json](sources/ROUND4_SHA256.json); source URLs are in [ROUND4_SOURCES.json](sources/ROUND4_SOURCES.json). Sources and review records described in the preceding inherited follow-up section were read locally from the earlier dossiers; those external review reports were not fetched again in this round. Search-result expositions were leads only and are not used to assert a proof or an error.

## Independent recheck of the earlier result

The previous result was a conditional transfer from a one-path collision bound and an exact conditional reference law to the hypotheses of the cancellation lemma. Its proof is preserved as [PRIOR_PROOF.md](PRIOR_PROOF.md).

Integrating out either member of a shared-midpoint factor leaves the asserted one-path marginal; a union bound over its two members therefore needs no independence within the factor. Independently, a possible collision between radius-ten confined paths forces integer anchor supremum distance less than 21, so there are at most \(41^3=68921\) possible anchors. The previous looser \(43^3=79507\) count and constant \(2\cdot79507=159014\) are sufficient. The reference and proposal normalizers have the stated lower factors \(0.99\cdot0.9=0.891\) and \(0.98\cdot0.9=0.882\); center separation greater than 30 minus two radius-eleven supports leaves distance greater than eight. The earlier conditional claim survives this independent check.

The archived audit was also rerun as `nice -n 15 env OMP_NUM_THREADS=1 python3 prior_audit.py`; all six checks passed. This corroborates the source quotations and constants, and is separate from the independent derivation just given.

## Spot check

The selected next input is Lemma 6.3, “A single replacement,” of OpenAI's positive-temperature manuscript. Its exact statement and a full derivation are in [PROOF.md](PROOF.md). This is a local estimate under unconditioned free bridge laws with a deterministic regular obstacle; it is not an estimate directly under the interacting thermal law.

For \(r=\alpha/D\), \(h_0=D^{-1}\), and \(\gamma=1/12\), the estimate is

\[
 Q(\mathcal C_v\cap\mathcal H(c))
 \le Ctr+C rD^{3\gamma}/\sqrt{h_0}
 =C\alpha(tD^{-1}+D^{-1/4}).
\]

The direct check establishes this bound for the two stated bridge laws, each fixed \(t>0\), sufficiently large \(D\), and \(K>50\), the large-torus regime used in the argument. For the ordinary duration-\(2t\) bridge the argument actually needs only the second term. Constants are uniform in every deterministic opponent obeying the regularity and endpoint-separation conditions; the lower threshold on \(D\) may depend on \(t\).

The potentially delicate dependence issues have different resolutions in the two halves of a leg. Before its midpoint, the Gaussian conditional residual is independent of the starting position, and its third maximal moment is bounded after division by \(r^3\). After its midpoint, conditioning on the entire centered fluctuation leaves a scaled uniform midpoint with density at most eight; the position and fluctuation increment need not be independent. The proof uses the cutoff to obtain a necessary ball event and then discards it; it never treats the cutoff-conditioned process as Gaussian.

Endpoint windows exclude collisions by separation greater than \(3s_0/4>r\). A collision with the confined trial determines a unique local obstacle lift on each interval, so arbitrary windings of the obstacle do not add a factor depending on volume. The mesh sum is bounded independently in two ways by a constant times \((\tau\sqrt{h_0})^{-1}\), and \(r^2/2\le\tau\le r^2\) gives the displayed power of \(D\). A prescribed midpoint equal to the obstacle's midpoint would force collision; the checked lemma averages over a cell and does not assert such a prescribed-midpoint bound.

The audit command is `nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py`. It passed exact source-quotation checks, 27 rational covariance identities, two independent expansions of the Brownian fourth moment, six direct mesh sums with upper bounds on the omitted tails, the prior normalization/constants check, and source numbering/format checks. Peak resident memory in the recorded run was 19,005,440 bytes; inherited nice was 20. No stochastic simulation, many-body computation or Lean build was used. These checks support the written local derivation and do not certify the full manuscript.

No gap was found in this particular estimate. It removes the single-replacement estimate from the assumptions left unchecked by round 3, while the reference-law construction and the thermal certificate and route encounter estimates remain unchecked. The next focused check is Lemma 7.2, “Exact conditional law”: trace the exposure/allocation procedure and verify that the conditional fiber has exactly the claimed product reference weighted by mutual avoidance, with no additional path-dependent allocation or eligibility weight.

## Recommended replacement “where it stands”

OpenAI's unrefereed preprint *Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas* (October 5, 2026) claims a positive constant-orbital condensate fraction for three-dimensional hard spheres at sufficiently small fixed density and fixed low positive temperatures in the thermodynamic limit. The documented Lean theorem covers ground states, and the local estimates checked here do not verify the full positive-temperature proof. The claim concerns a special interacting model and does not itself state a pointwise infinite-distance limit of the one-body kernel, so this verification does not settle the row in its full generality.
