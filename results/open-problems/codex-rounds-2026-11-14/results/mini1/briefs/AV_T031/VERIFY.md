# T031 — literature verification

Checked 14 November 2026. **Recommendation: SOLVED-CLAIMED for both parts**, interpreting the row in its usual nearest-neighbor RWRE sense. This records the scope of OpenAI's claims, not an assessment that the proofs are correct.

## 1. A directional zero–one law for finite-range-dependent random environments

Author: **OpenAI**. Date: **October 5, 2026**. Opened the [manuscript TeX](https://github.com/openai/math/blob/main/preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/build/manuscript/main.tex) itself, its directory listing and README. The PDF is named `directional-zero-one-finite-range.pdf`, rather than `paper.pdf`. Exact source snapshot: `sources/preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/build/manuscript/main.tex`; GitHub blob SHA `f92ce49a8ebf3997c744c154dfbddea0f7b6e454`.

### Exact main theorem

Theorem 1.1, including the original TeX notation and label:

```tex
\begin{theorem}[Directional zero--one law]\label{thm:main}
Under assumptions \textup{(i)--(iii)}, for every fixed
$\ell\in\RR^d\setminus\{0\}$,
\[
 P_0(A_\ell)\in\{0,1\}.
\]
\end{theorem}
```

Here `\RR` means ℝ, and the immediately preceding definition is `A_\ell=\{X_n\cdot\ell\longrightarrow+\infty\}`. The hypotheses referred to in the theorem are reproduced exactly below; the ambient model has d ≥ 3 and steps U = {±e₁,…,±e_d}:

```tex
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Stationarity and ergodicity.}
For $z\in\ZZ^d$, define
$(\theta_z\omega)(x,e)=\omega(x+z,e)$. The law $Q$ is invariant under
every $\theta_z$, and every event invariant modulo null sets under all
these translations has probability zero or one.
\item \emph{Uniform ellipticity.}
For some deterministic $\kappa>0$,
\[
 Q\bigl(\omega(x,e)\ge\kappa
          \text{ for every }x\in\ZZ^d,\ e\in U\bigr)=1.
\]
\item \emph{Finite-range dependence.}
For some deterministic integer $R\ge0$, the sigma-fields
\[
 \mathcal F_A=\sigma\bigl(\omega(x,e):x\in A,\ e\in U\bigr),
 \qquad \mathcal F_B=\sigma\bigl(\omega(x,e):x\in B,\ e\in U\bigr)
\]
are independent whenever the nonempty deterministic sets
$A,B\subseteq\ZZ^d$ satisfy
\begin{equation}\label{eq:finite-range}
 \dist_\infty(A,B):=
 \inf_{a\in A,\,b\in B}\norm{a-b}_\infty>R.
\end{equation}
This condition includes infinite sets.
\end{enumerate}
```

### Comparison with our part (a)

| Our words | What the theorem says | Coverage |
| --- | --- | --- |
| iid environment | Stationary, ergodic, finite-range-dependent full transition rows | Includes iid rows: their product law is stationary and ergodic, and R=0 gives independence for disjoint deterministic site sets, including infinite sets. |
| uniformly elliptic | One deterministic κ>0 bounds every allowed transition below | Same assumption. No independence between entries of a row is required. |
| RWRE on ℤ^d | One environment sampled and retained; nearest-neighbor steps ±e_i | Same standard model. No claim for arbitrary long-range jumps. |
| every direction ℓ | Every fixed nonzero real direction, including irrational ones | Same quantifier. ℓ=0 is trivial with escape probability zero. No simultaneous pathwise assertion is needed. |
| P(X_n·ℓ→∞)∈{0,1} | P₀(A_ℓ)∈{0,1} under the annealed law | Exactly the requested one-sign law, not merely the law for A_ℓ∪A_{−ℓ}. |
| missing dimensions d≥3 | All d≥3 | Covers the missing dimensions of (a). It does not itself supply a planar finite-range theorem; our row's planar iid case is already known. |

This theorem alone says nothing about speed and does not cover part (b). Its extension to correlated finite-range environments is stronger than the iid assertion in our row.

## 2. Directional transience implies ballisticity

Author: **OpenAI**. Date: **September 23, 2026**. Opened [build/main.tex](https://github.com/openai/math/blob/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/build/main.tex), [the introduction](https://github.com/openai/math/blob/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/build/01-introduction.tex), the README, and the geometric/speed reduction. Exact theorem-source blob SHA: `f3d2c1e089fee48a3477bdb10042311a1337a67e`.

### Exact main theorem

Theorem 1.1:

```tex
\begin{theorem}[Directional transience implies ballisticity]\label{thm:main}
Let $d\ge2$ and let $P=\nu^{\otimes\mathbb Z^d}$ be an iid law of
nearest-neighbor transition rows satisfying uniform ellipticity. If
$\ell\in S^{d-1}$ and $P_0(A_\ell)=1$, then there exists a deterministic
vector $v=v(\nu)\in\mathbb R^d$ such that
\[
 v\cdot\ell>0,
 \qquad
 P_0\!\left(\lim_{n\to\infty}\frac{X_n}{n}=v\right)=1.
\]
In particular, the walk is ballistic in the same direction $\ell$.
\end{theorem}
```

The paper defines A_ℓ={X_n·ℓ→+∞}, and defines directional transience by P₀(A_ℓ)=1. Its environment law is the product law of transition **rows**, not independent probabilities within a row.

The directly relevant positive-probability extension, Corollary 1.2, reads:

```tex
\begin{corollary}[Positive-probability transience and the velocity hemisphere]\label{cor:positive-transience}
Let $d\ge3$ and let $P=\nu^{\otimes\mathbb Z^d}$ be an iid law of
nearest-neighbor transition rows satisfying uniform ellipticity. For a
fixed $\ell\in\mathbb R^d\setminus\{0\}$, set
$A_\ell=\{X_n\cdot\ell\longrightarrow+\infty\}$. If $P_0(A_\ell)>0$,
then there is a deterministic nonzero vector $v=v(\nu)$ such that
\[
 v\cdot\ell>0,
 \qquad
 P_0\!\left(\lim_{n\to\infty}\frac{X_n}{n}=v\right)=1.
\]
If such a direction exists, then the deterministic sets of directions
satisfy
\[
 \{u\in S^{d-1}:P_0(A_u)=1\}
 =\{u\in S^{d-1}:P_0(A_u)>0\}
 =\{u\in S^{d-1}:v\cdot u>0\}.
\]
In particular, $P_0(A_u)=0$ for each fixed $u\in S^{d-1}$ with
$v\cdot u\le0$, including every equator direction. The equality concerns
annealed probabilities for each fixed deterministic direction, not a
simultaneous pathwise assertion over all directions.
\end{corollary}
```

### Comparison with our part (b)

| Our words | What Theorem 1.1 says | Coverage |
| --- | --- | --- |
| iid uniformly elliptic | iid nearest-neighbor transition rows, uniformly elliptic | Exact match in the standard model. |
| d≥2 | Every d≥2 | Exact dimension range. No one-dimensional claim. |
| transience in direction ℓ | Almost-sure escape in one fixed direction | Matches the standard meaning; it does not assume transience in a neighborhood of directions. |
| every direction | Any fixed real unit vector | Normalizing a nonzero real ℓ changes neither escape nor positivity of the velocity projection. |
| ballisticity, nonzero limiting velocity | Almost-sure convergence of X_n/n to deterministic v with v·ℓ>0 | Full limiting velocity, with positive projection in the same direction; stronger than merely v≠0 or a positive liminf. |
| general case beyond (T)/(T′) | No extra exit, drift, symmetry, reversibility or regeneration-moment hypothesis | Claims the full missing implication, not a perturbative or quantitative-criterion special case. |

Theorem 1.1 assumes P₀(A_ℓ)=1, not just P₀(A_ℓ)>0. Corollary 1.2 explicitly covers the latter for d≥3 using the companion zero-one claim; the already known planar iid zero-one law in our row supplies the same upgrade in d=2. Neither result claims ballisticity for general correlated finite-range environments.

## 3. Renewal and changes of law for critical honeycomb walks

Author: **OpenAI**. Date: **26 September 2026**, as printed on the paper. Opened [build/main.tex](https://github.com/openai/math/blob/main/preprints/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/build/main.tex), its introduction, [renewal section](https://github.com/openai/math/blob/main/preprints/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/build/sections/renewal.tex), [exact-length section](https://github.com/openai/math/blob/main/preprints/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/build/sections/exact.tex) and README. The PDF is named `main.pdf`.

This paper has several principal conclusions, rather than one main theorem in its introduction. Here are the exact principal infinite-path and fixed-length bridge statements.

```tex
\begin{theorem}[Infinite spatial law]\label{R:renew:infinite}
Concatenate independent irreducibles of law $p$, and enumerate the resulting vertices as $\gamma_1,\gamma_2,\ldots$. Almost surely,
\[
 |\gamma_n-\gamma_1|=n^{3/4+o(1)},\qquad
 \#\{n:|\gamma_n-\gamma_1|\le R\}=R^{4/3+o(1)}.
\]
\end{theorem}
```

```tex
\begin{theorem}\label{R:exact:bridge}
Choose a strict bridge uniformly from all bridges with $n$ visited vertices, rooted at a fixed bottom port, with terminal height and port free. For every $\xi>0$, along every sufficiently large even integer $n$,
\[
 \Prob_n\{n^{3/4-\xi}\le A\le D\le n^{3/4+\xi}\}\longrightarrow1.
\]
Here $A$ is the Euclidean distance between the ports and $D$ the diameter of the visited trace together with its ports. Replacing either by its vertex-endpoint convention changes it by a bounded amount.
\end{theorem}
```

For completeness, its fixed-height principal theorem is:

```tex
\begin{theorem}\label{R:exact:height}
Under critical weights normalized on strict bridges of exact height $h$ with free terminal port,
\[
 L=h^{4/3+o(1)},\qquad D=h^{1+o(1)}
\]
in probability as every integer $h\to\infty$. The same holds after restricting to any event whose critical mass is at least a fixed positive fraction of $B_h$.
\end{theorem}
```

The law p is the critical irreducible-bridge law on the regular planar honeycomb lattice, with weights ρ^L and ρ=(2+√2)^(−1/2). The introduction also distinguishes thermal laws at every large discount scale from uniform unrestricted walks, whose endpoint lower law is stated only on a common density-one set of lengths.

**Candidate verdict: NOT-THIS.** There is no iid field of quenched nearest-neighbor transition rows on ℤ^d, no directional escape zero-one law, and no assertion that transient RWRE has a nonzero linear velocity. The exponent 3/4 concerns sublinear spatial growth of self-avoiding walks and bridges under specified sampling laws. Terms such as renewal and ballisticity do not make these models interchangeable.

## 4. Follow-ups and formalization actually opened

### Primary repository records

- [OpenAI README](https://github.com/openai/math/blob/main/README.md) attributes the manuscripts and supporting artifacts to an unnamed internal model and describes them as raw research data at differing verification stages.
- [OpenAI history](https://github.com/openai/math/blob/main/history.md), with entries through October 29, names no withdrawal or correction for either relevant RWRE manuscript or the honeycomb candidate. The three candidate READMEs have no withdrawal/version notice in the snapshots read.
- [Family 220 Lean scope](https://github.com/openai/math/blob/main/lean/docs/220.md) explicitly covers iid strictly elliptic zero-one laws for d≥3, iid uniformly elliptic ballisticity for d≥2, and the d≥3 positive-probability/velocity-hemisphere refinement. It does **not** claim formalization of the stationary finite-range-dependent extension.
- For the honeycomb candidate, opened [family 237 scope](https://github.com/openai/math/blob/main/lean/docs/237.md) and [HoneycombFreeEnergy.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HoneycombFreeEnergy.lean). The selected free-energy formalization concerns existence of a limit, not the small-force exponent, correlation scale, or the 3/4 spatial and moment laws. Other family artifacts cover supporting bridge finiteness and strip/bridge-mass estimates. The [community honeycomb page](https://mathcommunity.github.io/oai-math-revised/papers/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/) was also opened; its catalogue notes are not a referee report.
- Opened [DirectionalWalk specification](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/DirectionalWalk.lean) and [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/DirectionalWalk.json), [DirectionalBallisticity specification](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/DirectionalBallisticity.lean) and [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/DirectionalBallisticity.json), and [VelocityHemisphere specification](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/VelocityHemisphere.lean).
- Opened the actual proof entry points [DirectionalWalk/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/DirectionalWalk/Main.lean) and [Ballisticity/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/Ballisticity/Main.lean), plus the Lean README, comparator README and formalization catalogue. The specification files intentionally end in `sorry`; the configurations point to separate proof modules. The two inspected configurations allow only propext, Quot.sound and Classical.choice, have empty `definition_names`, and disable nanoda. Their model definitions retain a fixed environment in the state; `infinitePi` defines iid site rows.

The additional companion [A directional zero–one law under strict ellipticity](https://github.com/openai/math/blob/main/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/build/01-introduction.tex), **OpenAI, September 23, 2026**, was also opened at its introduction and main TeX. Its exact main theorem is:

```tex
\begin{theorem}\label{thm:main}
Let $d\ge3$, let $\PP$ be an independent and identically distributed
law of nearest-neighbor transition rows on $\ZZ^d$ satisfying
\eqref{eq:ellipticity}, and let $\ell\in\RR^d\setminus\{0\}$.
Then
\[
 P_0(A_\ell)\in\{0,1\}.
\]
\end{theorem}
```

Its displayed assumption (eq:ellipticity) requires every allowed row entry to be positive almost surely. This is weaker than uniform ellipticity, so its iid claim also contains our part (a) in d≥3, and explains the scope of the corresponding Lean statement.

### External checking and comments

| Opened source | What it actually supplies | Limitation |
| --- | --- | --- |
| [mathcommunity finite-range page](https://mathcommunity.github.io/oai-math-revised/papers/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/) and [ballisticity page](https://mathcommunity.github.io/oai-math-revised/papers/Directional-transience-implies-ballisticity-September-23-2026/) | Catalogue notes and reported October 26 comparator acceptance for DirectionalWalk, DirectionalBallisticity and VelocityHemisphere | Automatically collected notes are unreviewed; no human check of the paper/Lean match is claimed. |
| [Comparator methodology](https://github.com/mathcommunity/oai-math-revised/blob/main/docs/LEAN_CHECKS.md) and individual [zero-one log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/DirectionalWalk.log), [ballisticity log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/DirectionalBallisticity.log), [hemisphere log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/VelocityHemisphere.log) | Each log records acceptance by Lean's default kernel. Methodology pins the tested Lean tree to OpenAI fd4aeeb, Lean v4.34.1. | Runs were prepared by an AI agent; proof modules were precompiled in the same workspace, a disclosed departure from the strictest adversarial configuration. These are external records, not a local rebuild or a human proof review. |
| [MathVet table](https://math.vet/openai-math/) and [family 220 data](https://math.vet/openai-math/data.json) | At upstream 4eaee875, reports sandboxed comparator PASS and labels the **family** partial because the finite-range-dependent extension is absent from Lean | Explicitly pre-referee, one model-assisted reading; no named referee verdict. “Partial” here does not mean our iid row is only partly claimed. |
| [OSVerify honeycomb report](https://osverify.github.io/cases/renewal-and-changes-of-law-for-critical-honeycomb-walks.html) | One minor citation-locator error in Section 11.1: cited propositions should be 10.1 and 10.7 | No released major finding; this is about the unrelated honeycomb paper, not RWRE. The companion cited there was not independently checked here. |
| [Quantitative sub-ballisticity of self-avoiding walk on ℤ^d](https://arxiv.org/abs/2610.40520), Ekin Arikök, Christoforos Panagiotis, Nicholas Pischke, Thomas Powell; submitted October 29, 2026; [full HTML](https://arxiv.org/html/2610.40520v1) opened | Introduction footnote 1 acknowledges OpenAI's claimed honeycomb exponent improvement | A cautious mention of family 237; neither a verification nor a refutation of it, and unrelated to T031's RWRE model. |

**Search result as of this check:** no arXiv version of the two relevant OpenAI manuscripts, targeted refutation/error report, named expert endorsement, or referee report was found in the searches made. This is a bounded search result, not proof that none exists. GitHub issue searches in openai/math for ballisticity and for “zero” plus “one” returned empty lists. Later mechanical-check records above are stronger evidence than early catalogue snippets that merely report claimant-supplied Lean.

Search queries and access failures are in LOG.md. DiscoverIA, AIProofWatch and Prove2Me appeared in search results, but direct opens failed; their snippets were not treated as verified expert assessments. Background arXiv pages [Selected Topics in Random Walk in Random Environment](https://arxiv.org/abs/1309.2589), **Alexander Drewitz and Alejandro F. Ramírez**, and [Almost exponential decay for the exit probability from slabs of ballistic RWRE](https://arxiv.org/abs/1406.4537), **Enrique Guerra and Alejandro F. Ramirez** (names as printed there), were opened for context, not counted as follow-ups. The older bibliography supplied in our row has not been independently re-audited in full.

## Recommended replacement “where it stands”

OpenAI claims the missing higher-dimensional zero-one law in “A directional zero–one law for finite-range-dependent random environments” (October 5, 2026), whose theorem includes iid uniformly elliptic environments, and claims the full d≥2 transience-to-positive-speed implication in “Directional transience implies ballisticity” (September 23, 2026). Lean artifacts cover the iid zero-one and ballisticity claims, with external comparator acceptance records, but not the finite-range-dependent extension. Record T031 as solved-claimed in the standard nearest-neighbor model, pending mathematical scrutiny; this verification does not judge either proof correct.

## Source preservation

Exact TeX excerpts above are copied without editorial changes from the opened sources, including their labels and macros. OpenAI's repository is Apache-2.0; a copy is saved as `sources/LICENSE`. Local source copies and their GitHub blob hashes are indexed in `sources/SOURCE_INDEX.json`; these are snapshots of files read, not a repository checkout.

## Spot check

**Selected lemma:** “No positive stationary normalization rate,” label `profile-no-growth`, in [Section 8](https://github.com/openai/math/blob/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/build/08-stationary.tex). This is the final obstruction used to rule out the bad-environment sequence and obtain the paper's decisive crossing estimate (5), P(a_N<N^(−β))<N^(−D₀) eventually for every finite D₀>0. It is conditional on the profile construction and the outward-order estimate; it is not a replacement proof of ballisticity.

Exact statement:

```tex
\begin{proposition}[No positive stationary normalization rate]
\label{profile-no-growth}
Suppose a stationary marked profile law has full-support subprobability
profiles and nonnegative marks $c_i$, positive integer marks $h_i$, with
\[
 E[c_0+\log(1+h_0)]<\infty.
\]
Assume the coordinatewise update \eqref{eq:43}, the finite
entropy property \eqref{eq:45} for every fixed $m$, and
the outward-order estimate \eqref{eq:33}, including its uniform local
approximation property. Then $Ec_0=0$.
\end{proposition}
```

Read the complete proof, its stationary-profile context, and the precise [outward-order hypothesis (33)](https://github.com/openai/math/blob/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/build/06-kernels.tex), including the uniform approximation of capped remainders by functions of finitely many nearby rows. The checks below concern this conditional proposition.

1. **The two-tail statistic is usable.** For a full-support subprobability w, the statistic T_R(w)=max_j min{w(z₂≤j),w(z₂≥j+R)} is positive and attains its maximum: its values tend to zero as j tends to either infinity. Any maximizing cuts must satisfy j_R→−∞ and j_R+R→+∞. Otherwise a shift by one site strictly increases the small tail while the other stays bounded away from zero; full support supplies the strict increase. Thus both sampled tails leave every fixed neighborhood of the representative origin.

2. **The factor 2 in the cut argument checks out.** Let Q_R be the endpoint-pair mass with signed gap at least R, and let ν_−,ν_+ be the two endpoint subprobabilities. Choose the least integer j with ν_−(u₂≤j)≥Q_R/2. If ν_+(v₂≥j+R)<Q_R/2, split the ordered-pair event into u₂<j and u₂≥j. Each part has mass less than Q_R/2, since the other marginal has mass at most one. This contradicts its total mass Q_R. Combined with the coordinatewise update, this gives the stated inequality
   log T_R(w_m)−log T_R(w_0) ≥ C_m−A_→ log(1+H_m)−Z_R−log 2.
   In particular the signs of the normalization term and the logarithmic cost agree with the intended contradiction.

3. **The delicate step is the change of law in (48).** A finite entropy density f_m relative to the current-data marginal times an iid upper field does not make the actual upper field independent. The proof instead fixes m, truncates f_m and the remainder, approximates the bounded density using finitely many rows near the origin, and approximates the capped remainder uniformly by rows near the two sampled tail sites. The reference law makes these sets independent once the tails leave the origin box; the tail sites are sampled from the current profile data, independently of the reference field. The uniform exponential moment controls the discarded density tail using λ f_m Z ≤ f_m log f_m+exp(λZ); Cauchy–Schwarz and P(f_m>B)≤1/B control the second term. These estimates justify the claimed limsup E Z_R≤sup_(x,y) E_P Z(x,y), for fixed m, under the stated uniform locality hypothesis. The order R→∞ first, m→∞ second is essential.

4. **Stationarity does not require integrability of log T_R itself.** If X,Y are the two finite nonpositive log statistics, their distributions coincide. The lower bound above controls the negative part of Y−X by an integrable variable. For the clipped variables max(X,−B), max(Y,−B), the mean difference is zero and the positive and negative difference parts increase to the corresponding parts of Y−X. This supplies both integrability of the difference and zero mean; it avoids an unjustified subtraction of two possibly infinite expectations.

5. **The final sublinear estimate needs no independence.** Put Z_i=log(1+h_i). Stationarity and the pointwise bound max_(i<m) Z_i≤T+Σ_(i<m) Z_i 1_{Z_i>T} give
   E log(1+H_m)/m ≤ log(m)/m+T/m+E[Z_0 1_{Z_0>T}].
   First let m→∞ and then T→∞. The logarithmic moment makes this vanish. The preceding expected inequality then forces E c_0=0, as stated.

**Finding:** no error was identified in this conditional obstruction during the spot check. Its crucial inputs—construction of the stationary marked law, the finite entropy property after marking, and the outward-order bound—remain separate proof obligations; the spot check does not establish them or certify the main theorem. The exact section and input source are preserved locally.


