# Verification of T078

Checked 2026-11-14. Verdict: **SOLVED-CLAIMED** for the stated spontaneous-magnetization formulation. This is a comparison of published claims with the row, not a finding that the proofs are correct.

## Main theorems, copied exactly

The quotations below are unchanged LaTeX theorem environments from the actual manuscript sources, including their labels and equation references. The surrounding notation is explained after each quotation. Each manuscript names its author as **OpenAI**. Local copies of the complete introduction sources are in [sources/](sources/).

### 1. The spherical magnetization law for the three-dimensional quantum Heisenberg ferromagnet

OpenAI, October 5, 2026. [Opened manuscript source](https://github.com/openai/math/blob/main/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/01-introduction.tex). Theorem 1.1.

```latex
\begin{theorem}[Spherical magnetization law]\label{thm:main}
For each fixed $S$ there is a finite $\beta_0(S)$ such that, for every
fixed finite $\beta\ge\beta_0(S)$, one has $m=m_{S,\beta}>0$ and
\begin{equation}\label{eq:spherical-law}
 \lim_{\substack{L\to\infty\\L\text{ even}}}
  \left\langle
     \exp\!\left(\frac1V\sum_{a=1}^3t_aM_L^a\right)
  \right\rangle_{\beta,L}
   =\frac1{4\pi}\int_{\mathbb S^2}e^{m t\cdot n}\dd\sigma(n)
   =\frac{\sinh(m|t|)}{m|t|}
 \qquad(t\in\R^3).
\end{equation}
Here $\sigma$ is surface-area measure on $\mathbb S^2$, and the quotient
at $t=0$ is interpreted as $1$. In addition,
\begin{equation}\label{eq:second-moment-law}
 \lim_{\substack{L\to\infty\\L\text{ even}}}
   \frac1{V^2}\sum_{x,y\in\Lambda_L}
          \langle S_x\cdot S_y\rangle_{\beta,L}=m^2.
\end{equation}
\end{theorem}
```

Here $S\in\{1/2,1,3/2,\ldots\}$, $\Lambda_L=(\mathbb Z/L\mathbb Z)^3$, $V=L^3$, and $M_L^a=\sum_xS_x^a$. The Hamiltonian is $-\sum_{\{x,y\}\text{ nearest neighbors}}S_x\cdot S_y$, each unordered bond once. The pressure is $p_{S,\beta}(h)=\lim_{L\to\infty,\ L\text{ even}}(\beta V)^{-1}\log\operatorname{Tr}e^{-\beta(H_{S,L}-hM_L^3)}$ and $m_{S,\beta}=p_{S,\beta}'(0+)$. The volume limit precedes field removal.

Comparison: the same quantum, isotropic, nearest-neighbor ferromagnet and every spin in our row, but **only d = 3**. It claims positive spontaneous magnetization at each sufficiently low fixed positive temperature, plus a precise spherical law and a positive limiting volume-averaged two-point function. These are stronger quantities in three dimensions; the theorem itself says nothing about d > 3. It concerns the symmetric zero-field periodic Gibbs states through even cubes and does not assert that their one-point expectation is positive (rotation invariance makes that expectation zero).

### 2. Spontaneous magnetization in the quantum Heisenberg ferromagnet

OpenAI, September 24, 2026. [Opened manuscript source](https://github.com/openai/math/blob/main/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/00-introduction.tex). Theorem 1.1.

```latex
\begin{theorem}\label{thm:main}
For every integer $d\geq3$ and every
$S\in\{\frac12,1,\frac32,\ldots\}$, there is a finite
$\beta_0(d,S)>0$ such that, for every finite $\beta\geq\beta_0(d,S)$,
the dynamics associated with \eqref{eq:hamiltonian} has a
translation-invariant $\beta$-KMS state $\omega$ satisfying
\[
                         \omega(S_0^z)\ge S/4.
\]
\end{theorem}
```

Equation `eq:hamiltonian` is $H_\Lambda=-\sum_{\{x,y\}\subset\Lambda,\ |x-y|_1=1}\sum_{a\in\{x,y,z\}}S_x^aS_y^a$, with each unordered edge counted once, coupling one and free boundaries. The paper defines the infinite-volume zero-field dynamics as the norm limit of the finite-volume Heisenberg dynamics on local observables; equilibrium means the usual bounded analytic-strip KMS condition.

Comparison: **the whole row is claimed**, with exactly the same spin set, every integer d >= 3, the same nearest-neighbor isotropic quantum ferromagnetic Hamiltonian, and all sufficiently low positive temperatures (finite beta). The lower bound S/4 is stronger than merely nonzero magnetization. The threshold may depend on d and S, as our statement permits; neither a large-spin limit nor zero temperature is substituted. This is existence of a selected translation-invariant equilibrium state, not a claim that every state is magnetized or that a symmetric finite-volume state has nonzero one-point expectation. The paper explicitly distinguishes its state assertion from the separate symmetric finite-volume two-point criterion; that distinction does not narrow our stated spontaneous-magnetization formulation.

### 3. Bloch's Law for Finite-Range Heisenberg Ferromagnets in Three Dimensions

OpenAI, October 5, 2026. [Opened manuscript source](https://github.com/openai/math/blob/main/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/01-introduction.tex). Theorem 1.1.

```latex
\begin{theorem}[Bloch's law]
\label{thm:main}
For every fixed $S\in\{\tfrac12,1,\tfrac32,\ldots\}$ and every
interaction satisfying \eqref{eq:interaction},
\begin{equation}
 \lim_{\beta\to\infty}\beta^{3/2}\bigl(S-m_{S,J}(\beta)\bigr)
   =\frac{\zeta(3/2)}{8\pi^{3/2}\sqrt{\det D_{S,J}}}.
 \label{eq:bloch-law}
\end{equation}
\end{theorem}
```

The assumptions referenced as `eq:interaction` are: $J:\mathbb Z^3\to[0,\infty)$ has finite support, $J(0)=0$, $J(z)=J(-z)$, and its positive support generates $\mathbb Z^3$ as an additive group. Here $H^J_{S,N}=-\tfrac12\sum_{x,y\in\Lambda_N}J(y-x)S_x\cdot S_y$ on free cubes, $m_{S,J}(\beta)=\partial_h^+p_\beta(0)$ after the thermodynamic limit, and $D_{S,J}=\tfrac S2\sum_zJ(z)zz^{\mathsf T}$.

Comparison: **d = 3 only**, all spins in our row, with a larger spatial finite-range coupling class that contains the nearest-neighbor model. Setting $J(\pm e_j)=1$ and all other couplings to zero gives exactly our bond normalization and $D_{S,J}=SI$. The theorem claims an exact asymptotic for the magnetization deficit, not just a free-energy bound: $m_{S,J}(\beta)=S-C\beta^{-3/2}+o(\beta^{-3/2})$. Since S > 0 and C is finite, this implies positive pressure-defined spontaneous magnetization for every sufficiently large finite beta. This implication is a direct comparison inference, not a further theorem verified here. The order of limits is volume, positive field down to zero, and then low temperature; d > 3 is outside this theorem.

## Comparison against each phrase of our statement

| Our phrase | September ordering theorem | October spherical theorem | October Bloch theorem |
| --- | --- | --- | --- |
| Quantum spin-S Heisenberg ferromagnet | Same model | Same model | Same model for nearest-neighbor choice of J |
| $H=-\sum_{x\sim y}S_x\cdot S_y$ | Same sign and coupling; unordered edges once | Same sign and coupling; unordered edges once | Same when $J(\pm e_j)=1$; factor 1/2 removes double counting |
| On $\mathbb Z^d$, every $d\ge3$ | Exactly | Only $d=3$ | Only $d=3$ |
| Every $S\in\{1/2,1,3/2,\ldots\}$ | Exactly | Exactly | Exactly |
| Low positive temperature | Every finite $\beta\ge\beta_0(d,S)$ | Every finite $\beta\ge\beta_0(S)$ | Asymptotic implies positivity at all sufficiently large finite beta |
| Spontaneous magnetization | Selected zero-field KMS state; at least S/4 | Positive pressure derivative plus spherical law and averaged two-point order | Pressure derivative with exact deficit coefficient |

No candidate claims a value of the critical temperature, a threshold uniform in S, or a result for all positive temperatures. Those are not required by our row.

## Follow-ups and formalization

The sources opened support the following distinctions as of November 14, 2026.

### Official artifacts and corrections

- [Repository README](https://github.com/openai/math/blob/main/README.md) describes the material as model-produced research outputs at differing verification stages.
- [Repository history](https://github.com/openai/math/blob/main/history.md) records unrelated withdrawals and repairs, but no withdrawal or correction of these three manuscripts. Their individual READMEs supply their titles, author OpenAI, dates and citations, without a withdrawal notice.
- [Lean scope note 271](https://github.com/openai/math/blob/main/lean/docs/271.md) names only the September ordering paper in its coverage statement, despite the broader family heading. Its coverage is magnetized KMS-state existence and convergence of dynamics; it does not claim formal coverage of Bloch's asymptotic or the spherical law.
- Opened [the challenge statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/Heisenberg.lean), [its configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/Heisenberg.json), and [the actual solution module](https://github.com/openai/math/blob/main/lean/OAI/MathematicalPhysics/Heisenberg/Main.lean). The selected theorem is OAI.Heisenberg.spontaneous_magnetization. Its natural-number parameter ell is 2S, so ell >= 1 includes exactly the required spins, and ell/8 is S/4. The statement asserts d >= 3, convergence of dynamics, and existence of a translation-invariant KMS state at every beta above a positive threshold. The challenge ends in sorry because it specifies the task; the solution has a proof invoking its imported development.
- The configuration permits only propext, Quot.sound and Classical.choice, lists no replaceable definitions, and disables the upstream second-kernel option. No Lean compilation or full dependency audit was performed for this report.
- [OpenAI, *The first lattice correction to Bloch's law*, October 5, 2026](https://github.com/openai/math/blob/main/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/01-introduction.tex) is another same-release companion, later than the September paper, not an independent follow-up. Its entry point and introduction were opened: it claims a sharper d = 3 nearest-neighbor deficit expansion. It does not add d > 3 coverage or independent validation.

The read-only GitHub branch endpoint identified the inspected main snapshot as 4eaee87548250b2682affda7d05d947c05554bae, last committed October 30, 2026. These observations concern the available version, not necessarily every historical revision.

### Independent check reports and exposition

| Opened source | What it supplies | Limit |
| --- | --- | --- |
| [mathvet family 271 review](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/fidelity-table.json), generated November 1 | Calls the family's formal coverage partial because the Bloch-law headline is absent, while identifying the all-dimension ordering statement | Family-level partial coverage does not mean T078 is only partially claimed |
| [mathvet challenge status](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/challenge-status.json) and [primary Heisenberg run log](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/evidence/cloud/Heisenberg.comparator.txt) | Reports a sandboxed Comparator pass completed October 8, 17:46:15Z on upstream adc7f124; the log reports Lean-kernel acceptance | A formal-check report; the review's referee-verdict field is empty |
| [mathvet comparison output](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/evidence/cloud/Heisenberg.cmp.txt) | Records theorem and definition comparisons, including Hamiltonian and KMS, with zero reported problems | Does not replace a subject expert's check of the encoding |
| [Community Heisenberg run log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/Heisenberg.log) and [run documentation](https://github.com/mathcommunity/oai-math-revised/blob/main/docs/LEAN_CHECKS.md) | Another acceptance report, from the October 25–26 runs, using the default Lean kernel and standard permitted axioms | The documentation says an AI agent managed the run, modules were precompiled in the same workspace, and statement-to-paper correspondence was not reviewed |
| [Community September-paper page](https://mathcommunity.github.io/oai-math-revised/papers/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/), updated November 9 | Scope summary and links to formal artifacts and exposition | No human notes; automatically collected notes explicitly unreviewed |
| [Azmat, *Quantum Heisenberg Ferromagnet: How OpenAI's Proof Settled a Decades-Old 3D Ordering Problem*, October 15, 2026](https://binaryverseai.com/quantum-heisenberg-ferromagnet-openai-proof/) | An exposition of the loop, pinning, return-estimate and KMS construction | The site says it has not independently compiled or audited the complete formalization; its headline is not evidence of refereeing |

The mathvet review flags the hand-built quantum-spin algebra, dynamics and KMS definitions as needing mathematical comparison. Those definitions were opened here: they are substantive definitions of the nearest-neighbor Hamiltonian and analytic-strip KMS condition, and the theorem separately requires dynamics convergence. This supports the intended scope, without certifying the full encoding or proof.

### Searches with no matching follow-up located

Exact-title searches, including searches restricted to arxiv.org, and searches combining OpenAI/Heisenberg/ferromagnet with error, correction, refutation, referee, review, Ueltschi, Seiringer and Toth did not locate a matching arXiv version, a paper-specific refutation or error report, or an identifiable specialist/referee assessment. This is a bounded search result, not proof that none exists. Search-engine “academia” entries resolved to GitHub manuscripts and supply no arXiv identifier.

The original repository has issues and discussions disabled. A community issue-search link failed to fetch, and the Plectis statement page failed to open despite a useful search excerpt; neither is used as evidence of review. Unrelated hits, including two-dimensional classical Heisenberg work and general discussion of the release, were not treated as T078 follow-ups.

### Opened-source record

All manuscript readings used the connected GitHub read-only contents endpoint https://api.github.com/repos/openai/math/contents/ followed by the path, after web folder/raw-file requests failed. Successful reads comprised:

- Each of the three candidate directories and their build layouts; all three READMEs; all three main TeX entry points; all three introduction sources quoted above.
- The September paper's build/source/sections/03-exposure.tex for the spot check.
- The extra lattice-correction companion's build/main.tex and build/sections/01-introduction.tex.
- The repository root, README.md, history.md, lean/ listing, lean/README.md, lean/docs/ listing, lean/docs/271.md, lean/formalization.yaml, lean/OAI/ listing, lean/OAI/MathematicalPhysics/Heisenberg/ listing, Heisenberg challenge and configuration, solution Main.lean, and Comparator README. No root docs/ directory was found; the relevant documentation is lean/docs/.
- Repository metadata and branches/main.
- The independent pages and raw artifacts in the preceding table, including mathvet's STATUS.md and review-directory listing.

The root paper.tex guesses failed; the actual sources were found through directory listings. Historical references in our original note were not re-audited and are not used as independently checked citations here. Source copies and selected formal-check records are retained in sources/; access failures and search terms are in LOG.md.

## Recommended new “where it stands” text

OpenAI's *Spontaneous magnetization in the quantum Heisenberg ferromagnet* (September 24, 2026) claims the full statement, constructing a translation-invariant zero-field equilibrium state with magnetization at least S/4 for every d >= 3 and every allowed spin at sufficiently low positive temperature. Its *The spherical magnetization law for the three-dimensional quantum Heisenberg ferromagnet* and *Bloch's Law for Finite-Range Heisenberg Ferromagnets in Three Dimensions* (both October 5, 2026) claim stronger three-dimensional magnetization laws. Lean artifacts and independent Comparator acceptance logs exist for the September ordering theorem, but no specialist referee report was located; record the row as solved-claimed.

## Spot check

Selected the September paper's **Proposition 4.3, “Conditional next-pin first moment”**, labelled prop:first-moment in [the exposure-section source](https://github.com/openai/math/blob/main/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/03-exposure.tex). Although called a proposition, it is the load-bearing finite-dimensional lemma converting conditioned cycles into fresh one-particle returns. Without it, subsequent diffusion estimates would concern the wrong law.

For a random permutation matrix Pi, with K = E Pi, the hypothesis is that **all exterior moments** satisfy E[exterior^k Pi] = exterior^k K. For V = J disjoint-union Q, let G mean every cycle meets J. The claimed identities are

\[
 \mathbb P(G)=\det(I-K_{QQ}),\qquad
 \mathbb E[\Sigma\mid G]
 =H:=K_{JJ}+K_{JQ}(I-K_{QQ})^{-1}K_{QJ},
\]

where Sigma is the next-pin permutation on J. This is not a claim about an arbitrary permutation law.

The finite algebra checks under that hypothesis:

1. The exterior-moment assumption gives E det(I-D Pi) = det(I-D K) for each fixed D, by expansion in principal minors.
2. Put D = diag(W,I_Q) with arbitrary W. A cycle wholly in Q supplies a fixed vector of D Pi, making its determinant zero. On G, Pi_QQ is nilpotent, so block elimination gives det(I-D Pi) = det(I-W Sigma), with det(I-Pi_QQ)=1 and no sign factor.
3. Setting W=0 gives the claimed P(G). Positivity makes I-K_QQ invertible. Since K_QQ is finite substochastic, invertibility excludes a closed Q class and implies transience, so its inverse is the nonnegative geometric series.
4. Schur complementation gives E[det(I-W Sigma)|G]=det(I-W H). Substitute tW and compare the linear coefficient. This gives Tr(W E[Sigma|G])=Tr(WH) for every W, recovering **every entry**, including off-diagonal returns to another pin. A trace-only identity would not suffice.
5. The preceding Lemma 4.2's exterior-moment algebra also checks: T-I has rank one for a transposition T, so each minor of I+u(T-I) is affine in u; independence and multiplicativity preserve the identity for products. Applying it to the exposed continuous-time hole process still depends on the earlier disintegration and limiting construction.

An independent exact finite example checks conditioning and matrix orientation. Use three labels, pins J={1,2}, Q={3}, and independent swaps (1 3), then (2 3), each with probability 1/2. The four outcomes have equal weights. Identity fails G; either single swap induces identity on J; the double swap induces the transposition on J. Consequently

\[
 \mathbb P(G)=3/4,\qquad
 \mathbb E[\Sigma\mid G]
 =\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix}.
\]

Direct averaging gives the column-forward mean

\[
 K=\begin{pmatrix}
 1/2&0&1/2\\
 1/4&1/2&1/4\\
 1/4&1/2&1/4
 \end{pmatrix},
\]

whose Schur complement gives the same result. With nonsymmetric W=((2,3),(5,7)), both sides of the stronger determinant identity equal -8. [The exact-arithmetic check](sources/check_next_pin.py) passed for all 25 pairs of swap probabilities in {0,1/4,1/2,3/4,1}, treating zero-probability conditioning separately.

**Finding:** no defect was found in this finite-dimensional bridge under its stated exterior-moment hypothesis. This does not check the exposed-path disintegration, multiscale heat-flow/bootstrap estimates, or construction of the KMS state, and supplies no verdict on the full proof's correctness.



