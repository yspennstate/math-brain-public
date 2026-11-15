# T032: verification of the OpenAI Bose-gas preprints

Original dossier: 14 November 2026. Continuation and independent source checks: 15 November 2026. This records claims, their scope, and one conditional dependency check; it does not judge the condensation proofs correct. All three manuscripts name **OpenAI** as author. The sources were read through the connected GitHub reader; local copies are under `sources/0`, `sources/1`, and `sources/2` respectively. The source entry points are `build/main.tex`, not `paper.tex`.

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

## Recommended replacement “where it stands”

OpenAI's unrefereed preprint *Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas* (October 5, 2026) claims a positive constant-orbital condensate fraction for three-dimensional hard spheres at sufficiently small fixed density and fixed low positive temperature in the thermodynamic limit. Its available Lean result concerns ground states only, and no completed independent check of the positive-temperature proof was found. These claims cover a special interacting model and the macroscopic-occupation criterion; they do not settle the row in its full generality or state a pointwise infinite-distance limit of the one-body kernel.

## Spot check

The selected load-bearing lemma is **Lemma 9.3, “Cancellation away from an overlap”** (\(\texttt{lem:cancellation}\)) in [Section 9.4](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/comparison.tex). This is the step that replaces a cost proportional to the lengths of two routes by a cost proportional to their encounters. Without that replacement, a fixed positive condensate fraction would not follow from the later route averaging.

The lemma has two changes of a product measure conditioned on checks. Their changed coordinate sets are S,T, split into near sets C_S,C_T and far sets F_S,F_T. The unchanged outside marginal must be retained exactly. Each proposal factor has a primary density g relative to its reference P_i, with 0≤g≤G and ∫g dP_i=1; factors may carry auxiliary coordinates. Uniform insertion of either a reference coordinate or an entire proposal factor succeeds with probability at least 1−χ, including after deletions and for other individually permitted coordinates that need not satisfy pairwise checks. Far factors have no checks with the opposing change. Under these hypotheses the claim is
\[
\int L_SL_T\,d\lambda
\le G^{|S\cap T|}(1-\chi)^{-2(|C_S|+|C_T|)}.
\]

Here is a direct audit of its proof. Fix the coordinates outside U=S∪T, put aχ=1−χ and c=|C_S|+|C_T|, and use the paper's notation: Z for reference check normalizers, Y for proposal check normalizers, and H for primary proposal densities before normalization.

1. The exact likelihood is \(L_S=(Z_S/Y_S)H_S\), and similarly for T. This uses equality of the outside marginal; replacing all conditional normalizations by one global normalization would invalidate the identity. Z_S,Y_S may depend on opposing coordinates; the proof does not assume otherwise.
2. Deleting near checks gives \(Z_S\le Z_{F_S}\). Restoring near proposal factors with the uniform insertion bound gives \(Y_S\ge a_\chi^{|C_S|}Y_{F_S}\), pointwise in opposing coordinates. The corresponding bounds hold for T.
3. The two far reference integrals factor, and at most c distinct near reference coordinates remain. Thus \(Z_U\ge a_\chi^c Z_{F_S}Z_{F_T}\). Since 0<aχ≤1, using c in place of the possibly smaller number of distinct coordinates weakens the lower bound in the correct direction.
4. Deleting proposal checks incident to near factors gives \(H_S\le H_{F_S}\prod_{i\in C_S}g_{S,i}\). After doing this for both changes and dropping the reference admissibility indicator, the far integrals are \(Y_{F_S}Y_{F_T}\). A coordinate appearing once has integral one. If it appears in both changes, \(\int g_{S,i}g_{T,i}\,dP_i\le G\int g_{T,i}\,dP_i=G\). Thus the remaining primary integral is bounded by \(Y_{F_S}Y_{F_T}G^{|S\cap T|}\).
5. Combining these inequalities gives exactly
\[
\frac{a_\chi^{-c}Z_{F_S}Z_{F_T}}{Y_{F_S}Y_{F_T}}
\frac{1}{a_\chi^c Z_{F_S}Z_{F_T}}
Y_{F_S}Y_{F_T}G^{|S\cap T|}
=a_\chi^{-2c}G^{|S\cap T|}.
\]
All four far normalizers cancel, and the bound is independent of the fixed outside data, which can then be integrated.

Two limiting checks agree with this calculation. For disjoint, noninteracting changes with no near coordinates, the conditional product expectation is exactly one and the bound is one. For a single shared coordinate with no checks, the familiar inequality \(\int g_Sg_T\,dP\le G\) supplies precisely one factor G, rather than G².

No algebraic or normalization error was found in this abstract lemma under its stated hypotheses. This is a conditional check of one lemma, not verification of the full proof: in particular, the uniform insertion estimates for every required path instance, the treatment of auxiliary paths in its application, and the random-route encounter estimates remain substantive inputs not established by this spot check.



## Continuation: 15 November 2026

The earlier REPORT.md and LOG.md were read in `~/codex_op_1114/briefs/AV_T032`; that folder has neither PROOF.md nor computation scripts. Its source archive was read and copied here. The preceding follow-up list describes the earlier worker's recorded openings; the table below identifies this session's fresh openings. The three main theorem blocks above were checked against freshly fetched primary sources, exactly, by `audit.py`.

### Bounded check for later developments

Within the initial five-minute check, web searches used the positive-temperature title with refutation/correction/arXiv terms, OpenAI with hard-sphere condensation and November 2026 error terms, and arXiv 2611.05293. The results supplied no resolution after the earlier report, no new paper-specific correction, and no completed expert verification of the positive-temperature proof. This is a bounded search result, not proof that no such report exists. Secondary exposition search hits were leads only; they are not evidence for accepting the proof.

| Fresh opening | What was checked |
| --- | --- |
| [Repository history](https://github.com/openai/math/blob/main/history.md), through web and the read-only GitHub reader | Latest listed entry October 29; no Bose-family correction or withdrawal listed. Saved as `sources/history.md`. |
| [Lean family scope note](https://github.com/openai/math/blob/main/lean/docs/267.md) | Still expressly restricted to ground states; saved as `sources/267.md`. |
| [HardSphere Comparator statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HardSphere.lean) | The concluding declaration quantifies ground vectors and ground-supported density operators. Its placeholder `sorry` is in the challenge statement, not evidence of a defect in the separately supplied solution. No Lean compilation was attempted. Saved as `sources/HardSphere.lean`. |
| Each of the three candidate `build/sections/introduction.tex` files, linked above | Reopened through the GitHub reader; main theorem quotations match exactly. Saved as `sources/introduction-0.tex`, `sources/introduction-1.tex`, `sources/introduction-2.tex`. |
| Positive-temperature manuscript [comparison](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/comparison.tex), [slab](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/slab.tex), [bridges](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/bridges.tex), [groups](https://github.com/openai/math/blob/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/groups.tex), and section directory | Read the normalizer application, single-path estimate, reference/proposal laws, and their geometry. Current comparison and slab sources agree with the earlier copies after stripping terminal newlines. The thermal slab estimates were not audited. |
| [arXiv:2611.05293 abstract](https://arxiv.org/abs/2611.05293) and [version-1 HTML introduction](https://arxiv.org/html/2611.05293v1) | Mohamed El Hedi Bahri and Ian Jauslin, *The Lee-Huang-Yang Formula in the Hard-Core Simplified Approach to the Bose gas*, submitted November 3, 2026. Still only v1 listed; the introduction calls the announcement under review. Their result treats the Simple Equation approximation and does not prove condensation for the exact positive-temperature many-body Gibbs state. |

The supplied positive-temperature GitHub directory failed in the web reader with Cache miss. The connected read-only GitHub reader supplied the actual TeX files and directory listing. All other source passages used in the comparison, including setup and final rescaling, were also read from the earlier local archive. The files in `sources/0`, `sources/1`, `sources/2`, `sources/repository` and `sources/reviews` are inherited archive copies; the flat source files listed in the table are the fresh downloads.

### Independent recheck of the earlier main conclusion

Let physical density be rho, exclusion distance a, and x=s*x_scaled. Independently of the paper's displayed final formulas, the scaled density is D=rho*s^3 and exclusion r=a/s. The condition Dr=alpha0 therefore gives s^2=alpha0/(a*rho) and D=alpha0^(3/2)/sqrt(rho*a^3). A physical temperature tau scales to s^2*tau, so the condition D*T_scaled<=1 gives a positive, volume-independent temperature range.

Specifically, the earlier T0=a^(5/2)*rho^(3/2)/(4*alpha0^(5/2)) makes D*s^2*T0=1/4. This follows both by direct multiplication and by independently adding the a, rho and alpha0 exponents in `audit.py`. For any fixed 0<tau<=T0, the finite-volume parameters converge to these values along every thermodynamic sequence. The local uniformity of the scaled theorem's K threshold then supplies the earlier low-temperature interval, conditionally on that theorem. No monotonicity in temperature or exchange of a zero-temperature and thermodynamic limit is assumed.

The earlier abstract cancellation calculation also holds under its stated hypotheses. At fixed complement, the proposal conditional primary density is H_S/Y_S whereas the reference conditional primary density is its check indicator divided by Z_S; keeping the complement marginal gives L_S=Z_S*H_S/Y_S on reference-admissible configurations. With c=|C_S|+|C_T| and a_chi=1-chi, deleting near checks and restoring factors gives the two ratio bounds with total cost a_chi^(-c), and the union reference normalizer contributes a further a_chi^(-c). Integrating bounded primary densities at shared indices contributes one G each, leaving a_chi^(-2c)*G^(|S intersection T|), as previously reported. The new check below addresses the concrete inputs to these inequalities.

### Spot check: the path-model application of Lemma 9.3

The selected extension is the application in Section 9.5, previously left conditional on path-model hypotheses. [PROOF.md](PROOF.md) verifies the transition from the manuscript's deterministic single-replacement estimate (Lemma 6.3, `lem:single-hit`) and conditional path law (Lemma 7.2, `lem:conditional-law`) to the cancellation lemma's hypotheses. It checks proposal marginal densities, reference insertion for selected accessible labels, whole shared-midpoint factor insertion, all prescribed deletions, preservation of the outside marginal, and separation of far factors.

Each proposal factor has at most two paths in separately constrained copies. Integrating the common midpoint gives each path its own normalized proposal marginal; a union bound therefore requires no independence of the two paths. Every path is confined to radius ten at its recorded anchor. For r<1, any possible opponent anchor is within supremum distance less than 21, so the deliberately larger cube of radius 21 contains at most 43^3=79507 anchors. With at most M labels per anchor, chi_D=2*79507*M*e_D=159014*M*e_D suffices uniformly, even when the fixed opponents fail their mutual avoidance checks.

Deleting factors removes their path instances and incident checks. Retained auxiliary instances remain in their own copies; no original path is put back after deletion of a factor. Thus the same insertion bound holds for every reduced normalizer. Each path lies within distance eleven of its factor center, so the R=30 definition of far factors leaves separation greater than eight, exceeding r. These estimates give the claimed conditional bound G^(|S intersection T|)*(1-chi_D)^(-4*J_30).

The constants were checked a second way: integer anchor distances strictly below 21 give the sharper count 41^3=68921; this is smaller than 79507. Direct enumeration in `audit.py` agrees with both cube formulas. The midpoint Gaussian lower bound, normalization costs, D^(-1/4) exponent, and factor-center separation were also rederived independently. Endpoints, common labels, retained auxiliaries and fixed-midpoint conditioning were examined; no counterexample to this conditional transition was found.

This result verifies one dependency transition. It assumes, rather than verifies, the single-path collision estimate, the exact conditional-law construction, the supply of usable routes and the thermal certificate estimates. It does not establish the main theorem, a pointwise infinite-distance kernel limit, or a positive-temperature Lean formalization. The next focused check is Lemma 6.3 itself, especially the mesh-interval collision bound and its uniformity for every permitted deterministic opponent.

### Status recommendation after this continuation

OpenAI's unrefereed preprint *Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas* (October 5, 2026) claims a positive constant-orbital condensate fraction for three-dimensional hard spheres at sufficiently small fixed density and fixed low positive temperatures in the thermodynamic limit. The documented Lean theorem concerns ground states, and this continuation verifies only a conditional step in the positive-temperature argument. The full row remains unsettled by this verification: these statements concern a special model and do not state a pointwise infinite-distance kernel limit.
