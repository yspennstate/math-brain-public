# T176: The mixing time of the Thorp shuffle

Verification date: 14 November 2026. This records claims and their scope, not a judgment that the proofs are correct.

## Result for our row

PARTIAL-CLAIMED: all three candidates claim optimal order for decks of size n = 2^d. None claims the corresponding upper bound for arbitrary even n. Our statement quantifies over all even deck sizes, so the whole row should remain open, with a claimed solution of its power-of-two case.

## Candidate 1: Optimal-order mixing of the Thorp shuffle

Author exactly as on the manuscript: OpenAI. Date: September 26, 2026.
Opened the manuscript's [build/main.tex](https://github.com/openai/math/blob/main/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/build/main.tex), including its definition of the chain and Theorem 1.1. The [PDF](https://github.com/openai/math/blob/main/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/paper.pdf) is linked for identification; the exact quotation below was copied from the opened TeX source, not transcribed from a search snippet.

Here n = 2^d, q_d is the law of one complete physical shuffle, U_n is uniform on S_n, and t_mix(d) uses total-variation threshold 1/4. Exact source quotation, including the theorem environment and labels:

```latex
\begin{theorem}[Optimal-order mixing]\label{thm:mixing}
As $d\to\infty$,
\[
 \|q_d^{*(1600d)}-U_n\|_{\mathrm{TV}}\longrightarrow0.
\]
For every integer $t\ge0$,
\[
 \|q_d^{*t}-U_n\|_{\mathrm{TV}}
 \ge 1-\frac{2^{tn/2}}{n!}.
\]
Consequently the mixing time at distance $1/4$ satisfies
\[
 t_{\mathrm{mix}}(d)\ge
 \left\lceil\frac2n\log_2\frac{3n!}{4}\right\rceil
 =2d-O(1),
 \qquad t_{\mathrm{mix}}(d)=\Theta(d).
\]
\end{theorem}
```

The conclusion is an order statement, Θ(log n), along powers of two. It is not an equivalent t_mix ~ c log n, a sharp constant, or a cutoff result. The asserted convergence to zero at 1600d is stronger than a fixed-error upper bound for all sufficiently large d, but is not a claim that the same numerical bound holds for every small d. Translation of the permutation law gives the same distance from every deterministic starting deck.

The introduction explicitly says: “The corresponding optimal-order question for arbitrary even deck sizes is not addressed by the cube argument here.” This rules out treating the title as a claim for every even n.

## Candidate 2: Compatibility entropy and the spectrum of a Thorp sweep

Author: OpenAI. Date: September 26, 2026.
Opened [build/main.tex](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/build/main.tex) and [sections/00-introduction.tex](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/build/sections/00-introduction.tex). The main results are Theorems 1.1 and 1.2; Corollary 1.3 states the mixing consequence. All are copied exactly below.

For Theorem 1.1, n = AD, R = (S_D)^A and C = (S_A)^D. Under U, all row and column permutations are independent and uniform. Compatibility I means that a row-then-column permutation can also be written column-then-row: for each original column j, the values c_{r_i(j)}(i) are distinct. This theorem allows balanced rectangles, not just powers of two; that auxiliary generality is not an extension of the physical shuffle mixing result to arbitrary even decks.

```latex
\begin{theorem}[Weighted compatibility]\label{tra:duality:weighted}\label{tra:duality:weighted-statement}
There are absolute constants $L,C_0>0$ such that the following holds. Put $m=\sqrt n$, assume $m/2\le A,D\le2m$, and take $m$ sufficiently large that $\theta=1-L/\log m>0$. For all nonnegative functions $w_i:S_D\to[0,\infty)$ and $v_k:S_A\to[0,\infty)$,
\begin{equation}\label{tra:duality:eq5}
 \frac{n!}{|R||C|}\,
 \mathbb E_U\!\left[\mathbf1_{\mathcal I}
       \prod_{i=1}^A w_i(r_i)\prod_{k=1}^D v_k(c_k)\right]
 \le e^{C_0n^{.54}}
       \prod_{i=1}^A(\mathbb E w_i^{1/\theta})^\theta
       \prod_{k=1}^D(\mathbb E v_k^{1/\theta})^\theta .
\end{equation}
The expectations on the right are uniform on the indicated symmetric groups, and logarithms are natural.
\end{theorem}
```

For Theorem 1.2, T_n is the convolution operator of one coordinate sweep on ℓ²(S_n); a sweep costs d physical shuffles when n = 2^d. The regular trace is Z_n(p) = Σ_{λ ⊢ n} D_λ Tr[(T_{n,λ}* T_{n,λ})^p], including the regular multiplicity D_λ.

```latex
\begin{theorem}[A bounded regular moment]\label{tra:duality:moment}
There is an absolute finite $p_*>0$ such that, for every dyadic $n$,
\begin{equation}\label{tra:duality:eq7}
 Z_n(p_*)\le1+\frac1{16}.
\end{equation}
For every integer $M\ge p_*$, $M$ independent forward sweeps have worst-start total-variation distance at most $1/8$ from uniform.
\end{theorem}
```

```latex
\begin{corollary}[Singular ranks and full-deck mixing]\label{cor:intro-consequences}
For every nontrivial $\lambda\vdash n$ and $1\le r\le D_\lambda$,
\[
 s_r(T_{n,\lambda})\le(16D_\lambda r)^{-1/(2p_*)}.
\]
If $s_j(T_n)$ denotes the full regular singular list, including all multiplicities and zeros, then
\[
 s_j(T_n)\le j^{-1/(2p_*)}\qquad(1\le j\le n!).
\]
The constant singular value is the first value. The physical Thorp chain has worst-start $1/4$ mixing time $\Theta(d)$; more precisely its lower bound is $2d-O(1)$. For every fixed integer $M>p_*$, the worst-start total-variation distance after $Md$ physical shuffles tends to zero as $d\to\infty$.
\end{corollary}
```

The full mixing consequence has the same model, full permutation law, worst-start total variation and physical time as our row, restricted to n = 2^d. A fixed number of sweeps is O(d) physical shuffles, not O(1) physical shuffles. The reflected positive operator T_n* T_n is an analytic intermediate; the quoted conclusion explicitly concerns repeated forward sweeps. No arbitrary-even upper bound, leading constant, or cutoff is claimed.

## Candidate 3: Routing densities and representation contraction for Thorp sweeps

Author: OpenAI. Date: September 26, 2026.
Opened [build/main.tex](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/build/main.tex) and [sections/00-introduction.tex](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/build/sections/00-introduction.tex). Exact Theorem 1.1:

```latex
\begin{theorem}[Routing density and representation contraction]\label{fac:main}
There are absolute constants $\eta,c,C>0$ such that, with $a=1/1000$,
\[
 \log\E_{y\sim u_{N,k}}R_x(y)^{1+a}
 \le Ck(k/N)^\eta
 \qquad(1\le k\le N),
\]
uniformly over every starting injection $x$. For every sufficiently
large dyadic $N$ and every nontrivial irreducible representation,
\[
 T_N(\lambda)=0\quad\hbox{or}\quad
 \|T_N(\lambda)\|_{\op}\le D_\lambda^{-c}.
\]
Consequently an absolute number of forward sweeps has worst-start
total-variation distance from uniform tending to zero as $d\to\infty$.
\end{theorem}
```

Here N = 2^d, T_N is the average operator of a forward coordinate sweep, K_N = T_N* T_N is a sweep and its reflection with fresh switches, X_{N,k} is the space of ordered k-tuples of distinct positions, u_{N,k} its uniform law, and R_x(y) = (N)_k Pr_{K_N}(x → y). D_λ is the irreducible dimension. Thus the density estimate concerns a reflected pair of sweeps, but the theorem's final sentence is a full-permutation, worst-start TV claim for a constant number of forward sweeps. The introduction combines it with the support lower bound 2d − O(1) to claim Θ(d) physical mixing time.

This is not merely a partial-card theorem or a theorem about a different shuffle. Its final conclusion covers the power-of-two part of our question, and does not cover arbitrary even N.

## Comparison with every clause of our statement

| Our wording | What the candidates claim | Covered? |
| --- | --- | --- |
| “The Thorp shuffle” | The ordinary cut, independent corresponding-pair choices, and interleaving chain; the binary-coordinate representation is a change of frame. | Same model. |
| “on a deck of n cards (n even)” | The physical mixing conclusions impose n = 2^d. | Only a subsequence of even sizes. |
| “cuts the deck into two halves of n/2 cards” | In binary coordinates x = (x_1,u), x_1 selects the half and u selects its corresponding location. | Exact match on dyadic decks. |
| “for each k = 1, …, n/2” | One independent switch for each u in {0,1}^{d−1}. | Exact match. |
| “drops the k-th cards … in an order decided by an independent fair coin” | The physical map is (x_1,u) → (u,x_1 + ξ_u), with independent fair ξ_u, fresh at each step. | Exact match; no extra randomness or padding is required. |
| “order of magnitude” | Upper O(d) plus lower Ω(d), hence Θ(log n). | Claimed on dyadic decks; no asymptotic equivalent is needed by our question. |
| “total-variation mixing time” | Full law on S_n, TV = ½Σ|μ−U|, worst deterministic start, threshold 1/4. | Same quantity, not single-card or fixed-fraction mixing. |
| “as n → ∞” | d → ∞ with n = 2^d. | Restricted limit; no monotonicity or padding argument for other even sizes is supplied. |

For any fixed 0 < ε < 1 the claimed vanishing TV upper bounds imply O_ε(log n), and the support count implies Ω_ε(log n), along powers of two. There is no need to settle cutoff to answer an order-of-magnitude question. Conversely, matching the lower bound on powers of two does not determine the order over all even integers.

## Follow-ups opened and what they establish

Searches used the web search tool, including the three exact titles and combinations of Thorp/OpenAI with arxiv, comment, referee, review, error, gap, correction and refutation. Negative findings below refer to this search, not to an exhaustive proof that no comment exists.

1. Opened the three community manuscript pages: [optimal-order](https://mathcommunity.github.io/oai-math-revised/papers/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/), [compatibility](https://mathcommunity.github.io/oai-math-revised/papers/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/), and [routing](https://mathcommunity.github.io/oai-math-revised/papers/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/). Their notes are expressly automatically collected and unreviewed. Follow-up links were opened separately where discussed below.

2. Opened [Latent Seminar, Optimal logarithmic mixing of the Thorp shuffle](https://lowrank.github.io/latent-seminar/OpenAI-Math/238-thorp-shuffle), dated 6 October 2026. It explains the family and its physical-time convention and explicitly disclaims independent verification of the complete proofs. This is an exposition, not a referee report.

3. Opened [Yunjiang Jiang, A subquadratic upper bound for the mixing time of the Thorp shuffle, arXiv:2610.18884](https://arxiv.org/abs/2610.18884), submitted 3 October 2026, v1. Its abstract gives the dyadic full-deck bound C_* d^{5/3} + O_ε(d^{4/3} log(d+2)), with ordinary-shuffle time. It is the independent comparison in our row, not an arXiv version of an OpenAI candidate.

4. Opened [Ilya Mironov, Mixing Time of the Random-Pair Monte Shuffle, arXiv:2611.03959](https://arxiv.org/abs/2611.03959), submitted 2 November 2026, and its [full HTML paper](https://arxiv.org/html/2611.03959v1), especially §1.3 and reference [19]. It cites OpenAI's optimal-order Thorp preprint as the endpoint of the known-bound progression. Its own theorem concerns a different random-pair Monte shuffle and does not prove or referee the Thorp result, or extend it to all even sizes.

5. Opened [Remark R5: Thorp shuffle 1600d → 24d](https://github.com/acprk/openai-math-remarks/blob/main/remarks/R5-thorp-24d/README.md). The repository note claims 24d using the companion Fourier transfer and 45d using the main paper alone. Its stated premise is correctness of the original papers; it says the reviews were separate AI sessions, not human peer review, and it has no Lean formalization. Attribution is repository acprk; the text literally leaves its author as “[AUTHOR NAME]”. It does not settle the non-dyadic case.

6. Opened the TeX note [The reciprocal-degree constants C_u of the Thorp-shuffle transfer (openai/math family 238): exact values, and the exponent of ε_n](https://github.com/acprk/openai-math-remarks/blob/main/remarks/R25-swapornot-cu-constants/note.tex), dated October 9, 2026 in the note, author literally “[AUTHOR NAME]”. It claims sharper constants and a stronger decay exponent for the first paper's displayed error bound. It describes the weaker published exponent as slack, not a disproof; these computer-assisted claims were not recomputed here.

7. Opened the [cutoff-agenda README](https://github.com/public-observatory/thorp-shuffle-cutoff) and [issue #2, Detect correlations beyond the counting threshold](https://github.com/project-wk/thorp-shuffle-cutoff/issues/2), opened 11 October 2026 by GitHub user isabeldahlgren, zero comments when fetched. It asks for an obstruction after (2+ε)d; it supplies no such obstruction and is not a refutation of the O(d) claim. The agenda leaves the leading constant and cutoff as research questions.

8. Opened [cert-machine's pinned statement audit](https://raw.githubusercontent.com/carlostoledo1891/cert-machine/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json), release fd4aeeb, family 238 (lines 9537 onward). It labels the dyadic full-permutation headline MATCHES through ThorpRemaining. It separately flags definition comparisons for OccupiedOverlap and SpinAngle. Its own description says a reading is not a certificate. Those companion flags should not be represented as a refutation of the mixing theorem.

9. Opened the repository [history](https://github.com/openai/math/blob/main/history.md) and all three candidate README files. No Thorp-specific revision, withdrawal or correction notice appears in those opened records. No arXiv version of these three OpenAI manuscripts, named specialist proof review, referee report, or mathematical refutation of their stated O(d) conclusion was found in the searches. The November citation is evidence of uptake, not independent proof verification.

## Lean artifacts: existence and limits

Opened [family 238 scope](https://github.com/openai/math/blob/main/lean/docs/238.md), [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [Comparator instructions](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md), and these challenge files and their JSON configurations:

- [ThorpRemaining.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThorpRemaining.lean) and [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThorpRemaining.json).
- [ThorpFirstReciprocal.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThorpFirstReciprocal.lean) and [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThorpFirstReciprocal.json).
- [ThorpRouting.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThorpRouting.lean) and [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThorpRouting.json).
- [ThorpWeightedCompatibility.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThorpWeightedCompatibility.lean) and [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThorpWeightedCompatibility.json).

Also opened the configured solution entry files [FullDevelopment.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpResults/FullDevelopment.lean), [FirstMain.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/FirstMain.lean), [ThorpRouting/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpRouting/Main.lean), and [ThorpCompatibility/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpCompatibility/Main.lean).

The scope note reports formalization of the first paper's 1600d convergence and support lower bound. Following the solution imports led to [ThorpShuffle/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/Main.lean), where the exact clock is explicit:

```lean
theorem full_mixing :
    Tendsto (fun d : ℕ => distance d (1600 * d)) atTop (nhds 0) := by
  apply (tendsto_add_atTop_iff_nat 3).mp
  simpa only [Nat.add_assoc] using Block.full_mixing_shift
```

Its main theorem also states worst-start equality, the support lower bound, and IsTheta versus log(2^d). The ThorpRemaining challenge itself uses 2048d and 32800d for some companion propositions and explicitly includes OptimalOrderMain. Its intentional “sorry” is a challenge placeholder to be filled by the configured solution, not evidence of a solution gap. Opened [formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml), whose project review status is “unchecked”; no Lean build or Comparator check was run here.

The solution-import path was opened through [ThorpResults/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpResults/Main.lean), [Statements.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpResults/Statements.lean), [Mixing.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpResults/Mixing.lean), [FixedLists/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/FixedLists/Main.lean), and [FixedLists/FullDeck.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/FixedLists/FullDeck.lean). The separate [FirstFourier.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/FirstFourier.lean) contains the eight-block Fourier estimate.

For Compatibility entropy, the scope note covers weighted compatibility on balanced rectangles; it explicitly excludes the bounded regular moment and other moment/rank conclusions. For Routing densities, it covers nine earlier supporting estimates, with high-height condition J > 2s; changed later statements and six other result blocks are excluded. These are narrower scopes than a claim that each whole manuscript is formally verified. None of the opened formal statements extends physical mixing to arbitrary even n.

## Recommended replacement for “where it stands”

OpenAI's AI-generated preprint “Optimal-order mixing of the Thorp shuffle” (September 26, 2026), with companions “Compatibility entropy and the spectrum of a Thorp sweep” and “Routing densities and representation contraction for Thorp sweeps” of the same date, claims total-variation mixing time of order log n for n a power of two. The repository reports a Lean formalization of the dyadic mixing result, but this verification does not assess the proofs' correctness. The order for arbitrary even n is not determined by these claims, so the full problem remains open.

## Spot check

Selected Proposition 6.1, “Eight-block Fourier bound,” in the short paper as the load-bearing transfer lemma. It turns large-card marginals into control of the whole permutation; without it, mixing 7n/8 cards would not answer the dyadic full-deck question. Its claim is that the eight caps ν(gH_a) ≤ 4|H_a|/|G| imply ‖ν̂(ρ)‖_op ≤ √(32C_1) D^(−5/16).

This check takes C_1 < ∞ from Lemma 5.1 as an input.

1. Restriction to H_1 × ··· × H_8 decomposes into tensor types whose product dimension is at most D. Each type has a factor of dimension at most D^(1/8). Assigning the whole isotypic summand to one such factor gives eight orthogonal invariant spaces E_a, including arbitrary multiplicities.

2. For u_a in E_a, its component of H_a-type π, of degree b, has orbit in the image of End(V_π) → V_π ⊗ A_π, Q ↦ (Q ⊗ I)u_{a,π}. This image has dimension at most b² regardless of multiplicity. Grouping equivalent copies first, as the proof does, gives
   \[
   \dim W_a\le\sum_{b_\pi\le D^{1/8}}b_\pi^2
       \le D^{3/8}\sum_\pi b_\pi^{-1}
       \le C_1D^{3/8}.
   \]
   The middle step is termwise b_π³ ≤ D^(3/8); it does not assume multiplicity one.

3. The coset orientation agrees with the marginal information: two permutations agreeing outside M_a differ by right multiplication by H_a, giving gH_a. Since W_a is H_a-invariant, ρ(gh)W_a = ρ(g)W_a. Thus g ↦ ‖P_{ρ(g)W_a}z‖² is constant on the cosets to which the cap applies.

4. The uniform average of these projections commutes with the irreducible ρ and has trace dim W_a, so it equals (dim W_a/D)I. The cap bounds its ν-average by four times this. Jensen and Cauchy–Schwarz give
   \[
   |\langle z,\widehat\nu(\rho)u_a\rangle|^2
       \le 4C_1D^{-5/8}\|u_a\|^2\|z\|^2.
   \]
   Summing the eight square-root bounds and using Σ_a‖u_a‖ ≤ √8‖u‖ gives √(32C_1) D^(−5/16). Independently, the exponent is (3/8 − 1)/2 = −5/16, and the squared constant is 4 × 8 × C_1.

No defect was found in this transfer lemma under its hypotheses. This check does not establish the earlier conditional-flow estimates, Lemma 5.1, the complete mixing theorem, or any non-dyadic extension. No numerical experiment or Lean build was run.


