# T095 verification and continuation

Checked 15 November 2026. Current repository revision: `4eaee87548250b2682affda7d05d947c05554bae` (30 October 2026), unchanged from both earlier sessions. The claim-scope verdict remains **PARTIAL-CLAIMED**: the relevant preprint claims the entire differentiability conclusion for Gamma laws, including exponential weights. It does not claim the row's quantification over every continuous law. REPORT.md uses the later continuation task's required PARTIAL format.

## Exact main statements

All three actual `build/main.tex` entry files and their introduction sources were reopened through the read-only GitHub connector at the pinned revision. Each entry file names **OpenAI** as its author. The following theorem environments are copied byte-for-byte from the local sources; these statements were also present in the user-specified earlier artifacts.

### Strict convexity and differentiability of the planar exponential first-passage limit shape — September 24, 2026

Opened [the introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex) and `build/main.tex`. Saved source: [source-exponential-introduction.tex](source-exponential-introduction.tex).

```tex
\begin{theorem}[The exponential limit shape]
\label{thm:exponential-shape}
For independent exponential edge weights of any rate $\lambda>0$,
the norm $\mu$ is Fr\'echet differentiable on $\R^2\setminus\{0\}$,
and its unit ball is strictly convex. In particular,
\[
 \mu((1-t)x+ty)<1
 \quad\text{if }x,y\in\partial\Bcal,\ x\ne y,\ 0<t<1,
\]
and $\partial\Bcal$ is a $C^1$ curve with a unique supporting line
at every point.
\end{theorem}
```

```tex
\begin{theorem}[Differentiability for Gamma weights]
\label{thm:gamma-differentiability}
For independent Gamma edge weights with any fixed shape $\kappa>0$
and rate $\lambda>0$, the norm $\mu$ is Fr\'echet differentiable at
every nonzero vector, and $\partial\Bcal$ is a $C^1$ curve.
\end{theorem}
```

### No bigeodesics in planar first-passage percolation — September 24, 2026

Opened [the introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex) and `build/main.tex`. Saved source: [source-no-bigeodesics-introduction.tex](source-no-bigeodesics-introduction.tex).

```tex
\begin{theorem}\label{thm:main}
Suppose that \(G\) has no atoms and that, for independent
\(X_1,X_2,X_3,X_4\) with law \(G\),
\begin{equation}\label{eq:minimum-moment}
 \EE\!\left[\min\{X_1,X_2,X_3,X_4\}^{\,2}\right]<\infty.
\end{equation}
Then, with probability one, there is no sequence
\((v_i)_{i\in\Z}\) of pairwise distinct vertices with consecutive
vertices adjacent and
\[
 \sum_{k=i}^{j-1}t_{\{v_k,v_{k+1}\}}=T(v_i,v_j)
 \qquad\text{for every }i<j.
\]
\end{theorem}
```

### QAOA attains the SK ground-state energy in the thermodynamic-first limit — September 25, 2026

Opened [the introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/build/sections/01-introduction.tex) and `build/main.tex`. Saved source: [source-qaoa-introduction.tex](source-qaoa-introduction.tex).

```tex
\begin{theorem}\label{thm:main}
For the zero-field SK model~\eqref{eq:sk-model},
\begin{equation}\label{eq:main-result}
 \lim_{p\to\infty}Q_p=\Pstar.
\end{equation}
Equivalently, for every $\varepsilon>0$ there exist a finite integer $p$ and
deterministic real vectors $\gamma,\beta\in\R^p$, independent of $n$ and $J$,
such that $v_p(\gamma,\beta)\ge\Pstar-\varepsilon$.
\end{theorem}
```

## Comparison with our exact statement

| Clause in our row | Shape preprint | No-bigeodesics preprint | QAOA preprint |
| --- | --- | --- | --- |
| Undirected nearest-neighbor first-passage percolation | Same model | Same model | Zero-field SK spin glass, a different model |
| On Z² | Same dimension | Same dimension | Thermodynamic spin-system size, not a Z² shape |
| Independent identically distributed nonnegative weights | Same independence, with a particular common law | Same setting; the introduction specifies a law on nonnegative weights | Gaussian spin-glass couplings, not passage times |
| Continuous law | Only exponential and Gamma(shape κ, rate λ), κ,λ>0 | General nonatomic law, agreeing with the row's distributional hypothesis | No matching law quantifier |
| E[min(τ₁,…,τ₄)²]<∞ | Holds automatically for the stated laws: Eτ²=κ(κ+1)/λ² and min²≤τ₁² | Exactly the same minimum-of-four condition | Not the hypothesis |
| Boundary differentiable at every point | Claimed for the Gamma subclass; Fréchet differentiability away from zero and a C¹ boundary have the required everywhere scope | Conclusion rules out doubly infinite geodesics; it does not assert boundary differentiability | Conclusion is the limit of optimized QAOA values as depth tends to infinity |
| Strength and range | Covers all directions for every fixed positive Gamma shape/rate, not all continuous laws; exponential theorem additionally claims strict convexity | No differentiability inference follows just from its stated theorem | Unrelated to the row |

For a concrete uncovered law, Uniform[1,2] is continuous, positive, and satisfies E[min⁲]≤4, but it is not a Gamma law: its support is bounded. The row's minimum-of-four hypothesis can even hold when the ordinary edge mean is infinite, so replacing it by an exponential-moment assumption would also narrow the problem. None of these three statements claims the whole row. The existence of the Gamma differentiability claim changes the old note's assertion that no continuous example is known, if the claim is accepted, but it does not justify closing T095.

## Follow-ups and sources actually opened this session

| Opened source | Finding and limits |
| --- | --- |
| [Latest commit API](https://api.github.com/repos/openai/math/commits?per_page=1) | Still the October 30 snapshot used earlier; no later repository revision located. |
| Scott Armstrong and Ahmed Bou-Rabee, [*Fluctuation bounds for rotationally invariant first-passage percolation*, arXiv:2610.42124](https://arxiv.org/abs/2610.42124), abstract page | Submitted October 30, 2026. Concerns fluctuation bounds for rotationally invariant FPP on Rᵈ, d≥2. It is not the lattice differentiability theorem, an arXiv version of the shape preprint, or a refutation of it. Only the abstract page was reopened this session. |
| [Official Lean scope note](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/212.md), saved as [source-lean-scope.md](source-lean-scope.md) | Describes Gamma differentiability; says strict convexity is outside the selected statements. It contains no all-continuous-law differentiability claim. |
| [Gamma Comparator target](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GammaPassage.lean), saved as [source-gamma-target.lean](source-gamma-target.lean) | Quantifies over every positive Gamma shape/rate and actual iid environments; defines paths and passage time and asks for an actual time-constant norm with differentiability and boundary charts. Its `sorry` is the challenge placeholder. |
| [Actual final Gamma proof](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/GammaPassage/Differentiability.lean), saved as [source-gamma-differentiability.lean](source-gamma-differentiability.lean) | Supplies the separate final proof by calling earlier Gamma no-corner and time-constant results. The dependency chain was not built or fully audited here. |
| [MathVet primary fidelity table at its earlier pinned revision](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv), family 212 | Reports partial headline coverage and `comparator-sandboxed-pass`. Its named selected conclusions include Gamma differentiability; no-bigeodesics and exponential strict convexity are outside those conclusions. This is a checking/scope report, not a referee endorsement of the full manuscript. |
| Shape preprint's [crossing section](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/differentiability/crossings.tex) and [preliminaries](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/differentiability/preliminaries.tex) | Actual sources for the new spot check, saved locally as [source-crossings.tex](source-crossings.tex) and [source-preliminaries.tex](source-preliminaries.tex). Both agree with round 3. |

The five-minute update search used the exact shape title with error, refutation, correction, review, and November 2026; general continuous-law FPP differentiability with OpenAI/2026; GammaPassage and the rare-fast lemma label; and first-passage differentiability after November 13. It located no new general theorem, same-title arXiv version, specific error report, or named expert/referee assessment that changes the earlier picture. This is a bounded negative search finding, not a certification that no such source exists. Search-result catalogues were not used as proof evidence; follow-ups not reopened from the earlier sessions are not presented as newly checked.

## Independent recheck of the earlier result

Read both earlier REPORT.md and LOG.md files and the round 3 PROOF.md and audit.py. The original session has no PROOF.md or scripts. The round 3 audit was run unchanged using `runpy.run_path` from this folder: all four theorem blocks, 36 exact Gamma integrals, 30 edge counts, and 50 attachment-tail identities passed.

Independently, for a multiplicative weight change α=1−δ on M distinct Gamma edges, the sum's Laplace transform gives E[(dQ/dP)²]=[α(2−α)]^(−κM)=(1−δ²)^(−κM). Its logarithm has order Mδ²=O(ns)O(s²/n²)=O(s³/n), bounded at n=s³. Cauchy–Schwarz then transfers rare-fast probability o(1) to the positive-allowance crossing probability o(1), exactly as round 3 asserts. This confirms the earlier conditional claim; it does not by itself prove rare-fast crossings.

## Spot check

The one new piece is `df:cr:rare-fast`, with its finite-dependence oriented-path argument and trial amplification. The complete derivation is in [PROOF.md](PROOF.md), and finite exact checks are in [audit.py](audit.py). No defect was found in this argument under the fixed-law uniform shape theorem stated in the preliminaries.

The calculation fixes k=ceil(4(A+3)+8)+1 before the trial count M and connector factor D₀. At auxiliary sites separated by more than k, the test regions use disjoint internal edge sets; M and D₀ cancel from that comparison. Exact lattice translates give independent trials within each site despite rounding. A bounded-net connection event handles every endpoint pair before a successful trial is selected.

The contour proof gives at least m/8 distinct bad sites and at least m/[8(2k+1)²] mutually independent bad tests along a length-m candidate trail. One explicit sufficient bad-site bound is ζ=2^(−48(2k+1)²), giving total failure probability at most 9Σ_{m≥4}(m+1)²16^(−m)≤3/256<1. PROOF.md gives two derivations of the summation bound. The eventual shape-theorem contradiction takes infinitely many concatenated crossings at one fixed scale, using the uniform origin estimate for their random endpoints.

The local-travel input was also re-derived from that same uniform shape theorem, and interval travel from it and elementary Gamma moments. Thus these two previously conditional crossing inputs are accounted for at the level of this audit. This is not an audit of the entire differentiability proof, and it supplies no replacement for the Gamma-specific change of measure for arbitrary continuous laws.

The command `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py` passed 2,307 finite-set contour cases (all origin-containing subsets of 3×3 and 4×3 grids plus three exceptional geometries), 1,536 exact rational strip-placement cases, 1,734 dependence-coordinate cases, and source/theorem checks. Two exact sum evaluations give 181/48000, below the analytic upper bound 3/256. The run took 0.307 seconds and measured peak RSS 15,974,400 bytes at nice 20; the platform rejected both attempted memory-limit setters, as recorded in LOG.md. These finite checks support the combinatorial and constant bookkeeping; the all-parameter reasoning is in PROOF.md.

## Recommended replacement for “where it stands”

OpenAI's preprint *Strict convexity and differentiability of the planar exponential first-passage limit shape* (September 24, 2026) claims differentiability everywhere for every positive Gamma shape and rate, including exponential weights. Its selected Lean statements cover Gamma differentiability, while the paper's exponential strict-convexity claim is outside those selected statements. The general continuous-law statement under the Cox–Durrett minimum-of-four moment condition is outside these claims; no later resolution was located in this bounded search.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 04:16 Asia/Tbilisi.

