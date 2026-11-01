# Independent audit of the recovered FEI threshold manuscript

Date: 11 October 2026.

Audited source: `recovered/threshold/fourier-entropy-threshold-functions/paper/main.tex`, recovered from `fourier-entropy-threshold-functions.zip`.

## Decision and scope

I found no mathematical gap in the proof of Theorem A, its regular-function/character-multiple extensions, the logarithmic Boolean-combination estimates, the arbitrary-product symmetric-threshold theorem, or the composition and full-entropy conversions. These results are suitable to retain as theorems in a research preprint on the basis of this audit. No theorem-statement correction is required in these portions.

This is a mathematical reading and finite computational audit, not peer review or a formal proof-assistant certificate. It does not establish unrestricted FEI. In particular, the paper only proves the arbitrary-product FEI+ statement for symmetric thresholds; arbitrary weighted thresholds under arbitrary product laws remain a stated question. The universal witness-cost estimate needed for unrestricted FEI remains missing.

The bounded-overlap section has also received a substantial preliminary check from me: the pivotal path bound, rare-support estimate, queue construction, directed-forest realization, source-component disjointness, root costs, subset costs and ordinary entropy averaging are sound on this reading. Another independent agent is responsible for the consolidated audit of that entire section. The root agent is separately auditing joint witnesses, selectors and activation.

## 1. The all-LTF / regular-function theorem

The claimed constant is

\[
C_{\rm reg}=\log_2(4+e)+2\log_2(e\pi)
 =8.936474657877582\ldots <8.937.
\]

The conclusion is \(H(f)\le C_{\rm reg}D(f)\) for regular Boolean functions, where \(D(f)=\sum_i\min(I_i(f),1-I_i(f))\). Every LTF is regular after orienting its weights and ordering their absolute values. The proof does not assume small maximum weight, bounded weight ratios, balanced output or a nonzero threshold margin.

### Pivotal antichains

The desirability condition has the correct direction. If two comparable predecessor assignments were pivotal for coordinate \(i\), switching any changed predecessor \(j\) from \(-1\) to \(+1\) while switching \(i\) from \(+1\) to \(-1\) would preserve positivity by desirability. Monotonicity then contradicts pivotality at the larger assignment. Equal weights and the chosen sign convention cause no exception.

### Relative noise bound, including signed functions

For a signed indicator \(d\) whose support is an antichain on every predecessor fiber, condition on the original point and on the refresh mask. The refreshed point lands in the support with conditional probability at most the Sperner density \(c_{|R|}\). Thus

\[
\sum_T\widehat d(T)^2(1-t)^{|T\cap U|}
 =\mathbb E[d(X)d(Y)]
 \le \|d\|_2^2\,\mathbb E c_B.
\]

Taking absolute values before the support bound makes this valid for every signing of every subset of the pivotal antichain. This is exactly what character multiplication and partitioned pivotal pieces require. The subsequent bound \(\mathbb E c_B\le (rt)^{-1/2}\) follows from Cauchy–Schwarz and the displayed binomial reciprocal moment; there is no reversed Jensen inequality.

### Harmonic rank estimate

For \(\kappa=|T\cap U|\), integration of the exact Sperner bound gives

\[
\mathbb E h_\kappa\ge\sum_{q=1}^{r-1}\frac{1-c_q}{q}.
\]

The comparison \(\ln(r/(\kappa+1))\le h_{r-1}-h_\kappa\) is in the required direction. The identities \(c_{2j-1}=c_{2j}=4^{-j}\binom{2j}{j}\), \(\sum b_j/(2j-1)=1\), and \(\sum b_j/(2j)=\ln2\) then yield the dimension-free expectation \(1+\ln2\). The \(r=1\) case is handled explicitly.

### Entropy reference and centering

Euler's product gives a subprobability measure on each Fourier level,

\[
Q_k(S)=\frac{(2k+1)!}{\pi^{2k}}\prod_{i\in S}i^{-2}.
\]

For \(S=\{i_1<\cdots<i_k\}\), its logarithmic cost is at most twice the rank discrepancy plus \(k\ln(\pi^2/4)\). The factorial inequality used for this is valid. Applying Gibbs conditionally on the level and summing derivative-conditioned rank expectations charges the cost to total influence.

The level entropy bound \(H(|\mathcal S|)\le\log_2(4+e)I(f)\) is valid. Its only Boolean-specific step is the edge-isoperimetric lower bound; the scalar comparison and choice of geometric reference check algebraically.

After shifting by the character that minimizes influence, a coordinate with original influence above \(1/2\) must have rank one: a predecessor would force pivotal probability at most \(1/2\) on every one-dimensional predecessor fiber. Those coordinates have rank cost zero. All remaining shifted derivatives remain signed indicators on the original antichains. Hence the same argument bounds entropy by \(D(f)\), without an unjustified invariance assertion for derivative spectra.

The universal comparison \(D(f)\le4(I(f)-\operatorname{Var}(f))\) follows from \(|\widehat f(\{i\})|\le I_i(f)\), then \(k\le2(k-1)\) for \(k\ge2\). The two-bit conjunction certifies sharpness of the factor four in that comparison.

### Multiple regular components

The disjoint pivotal-piece decomposition and weighted Cauchy–Schwarz domination are correct, including sign changes. The Frullani integral has the right logarithmic cutoff \(m^2\), yielding \(2+\gamma+2\ln m\). The rank-weight normalizers, the centering bound on the number of high-influence coordinates, and the arithmetic for \(a=6/5\) are consistent. Chain-width and score-transition consequences use precisely the extra normalizer factors stated in the paper.

## 2. Arbitrary-product symmetric thresholds

The normalization is correct: \(\sigma_i^2=4q_i(1-q_i)\), biased Fourier energy is \(\sum |S|P(S)\), and the corrected entropy uses \(\sigma_S^2/P(S)\). A biased dictator has corrected entropy and spectral deficit zero. The paper correctly avoids claiming a uniform biased bound for ordinary Shannon entropy.

### Weak estimate

The mixture of a deterministic bit and an activated fair bit proves the refresh concentration bound for unequal coordinate probabilities. The spectral-rank estimate follows with the stated constant \(3+\ln8\).

The normalization credit is the delicate step. Its relative-entropy decomposition is exact. The single-coordinate divergence bounds use the correct inequalities and factors of four. Tilting to a product law with mean equal to the integer threshold is legitimate for a nontrivial upper-tail event. Under that law,

\[
I/\alpha\ge2\mathbb E_R|N-t|\ge 2v/\sqrt{1+3v},
\qquad
\mathrm{TC}(\mu_A)\le\ln(1/\mathbb P_R(N=t)).
\]

Darroch's theorem applies because the tilted count remains a sum of independent Bernoulli variables and has an integer mean. The mode bound, Chebyshev estimate, monotonicity of the displayed function \(\psi\), and rational endpoint estimate all check. The resulting \(13/4\) coefficient is valid.

The maximum-based spectral reference provides the required negative normalization credit. The inequality comparing its coordinate cost to a positive rank term minus the pivotal-probability term is valid in both sign cases of the latter logarithm. The weak bound is therefore \(\mathcal E_\mu\le A I\), \(A=23+\ln16\).

### Strengthened estimate near a dictator

The proof correctly separates the case in which all pivotal probabilities are at most \(9/10\). In the other case, the most likely configuration of the remaining bits must lie on the pivotal slice. The concentration and one-error arguments imply \(L<1/8\) and the claimed bounds relating \(L\), \(\Lambda'\), and \(\varepsilon\).

The lower bounds for \(J_U\) and \(J_D\) have the correct endpoints and directions. The entropy of coefficients containing the distinguished coordinate is at most \(3J_0\). For coefficients avoiding it, the four families, the coefficient-splitting inequality, the small-bias bounds and the product-sum estimates give the displayed \(23J_U+5J_D\). Combining singleton and nonsingleton contributions yields \(\mathcal E_\mu\le25J\) in this regime, comfortably within \(10AJ\). Consequently

\[
H_\mu^+(f)\le C_T\Delta_\mu(f),\qquad
C_T=80+460/\ln2<744,
\]

is supported by the written proof. Deterministic input coordinates are removed before use, as required.

## 3. Composition and strong full entropy

The exact biased Fourier substitution has a unique decomposition of each nonempty set into its input blocks. Its entropy and deficit identities agree with the O'Donnell–Tan composition framework, including the factors \(I_i^\eta(g)/v_i\). Constant child outputs are explicitly removed, so no division by zero is hidden.

The separate AND/OR and parity computations and scalar induction \(\Phi\le2R\) are valid. The two-bit rare OR asymptotic supports the stated sharp product-measure AND/OR constant \(2+4/\ln2\).

The empty-atom estimate \(h_0(f)\le\sqrt{2/(1-\ln2)}\,\Delta(f)\) follows from the written isoperimetric comparison and \(t\le\sinh t\). The conversions to \(H\le744I\) and \(H\le747\Delta\) are therefore justified. Weighted internal gates are correctly restricted to balanced nonconstant child outputs.

## 4. Reproduced finite checks

I ran the recovered scripts without editing the recovered source:

| Script | Result |
|---|---|
| `computations/verify_rank_improvement.py` | PASS: 1,506 signed-antichain cases; 7,418 exact noise-mask checks; 1,506 exact harmonic-rank checks. |
| `computations/check_signed_derivatives.py` | PASS: 96 function families; 4,720 character-coefficient checks; 321 pivots; 595 modulated pieces; 976 antichain-pair checks; 10,060 exact domination checks. |

The first script uses integer cross multiplication for the actual inequalities. Floating point only reports constants. These checks corroborate the finite bookkeeping; the dimension-free claims rest on the analytical arguments above.

## 5. Literature and citation verification

The following primary sources were opened on 11 October 2026. A root response using web citation tokens must reopen these pages in its own tool context.

| Citation | Verified content | Primary URL |
|---|---|---|
| CKLS16 / ECCC revision | Revision 2 explicitly removes inaccuracies in the earlier LTF argument and states the deterministic bound \(H(f)=O(\sqrt n)\). | https://eccc.weizmann.ac.il/report/2013/052/ |
| Random LTF FEI | Abstract distinguishes FEI for the specified random weight models from the unresolved deterministic LTF class at that time. | https://arxiv.org/abs/1903.11635 |
| O'Donnell–Tan | Biased FEI+ composes under disjoint substitution; bounded-arity read-once formulas follow. | https://arxiv.org/abs/1304.1347 |
| Wan–Wright–Wu | Coding interpretation; read-k decision trees; expected-depth bounds and reductions. | https://arxiv.org/abs/1312.3003 |
| Shalev | Small-influence reductions, including the significance of sublinear exponent restrictions; read-k decision-tree improvement. | https://arxiv.org/abs/1806.03646 |
| Han25 | \(O(I+\sum_i I_i\log(1/I_i))\) entropy bound; v2 acknowledges related prior work. | https://arxiv.org/abs/2312.08271v2 |
| GMP26 | Matching title and authors; v2 dated 9 June 2026, 30 pages; restriction/stopping-tree method. | https://arxiv.org/abs/2606.00246v2 |
| Potapov26 | Matching title/author, 18 September 2026; stated sharp plateaued constant 4 and partially bent constant 2. | https://arxiv.org/abs/2609.21563 |
| Shmalo percolation | Matching title/author, 14 September 2026; abstract states crossing entropy comparisons and spectral/pivotal separation. | https://arxiv.org/abs/2609.15388 |
| Pitman97, Eq. (13) | Darroch's mode rule for a sum of independent Bernoulli variables; an integer mean is a mode. | https://statistics.berkeley.edu/sites/default/files/tech-reports/453.pdf |

The current public percolation GitHub URL could not be fetched by the web tool (a DisabledError). Its current revision date should therefore be checked through the connected GitHub integration. This is not a problem with the verified arXiv citation.

The searches did not locate an intervening published all-LTF FEI theorem. This supports treating the recovered result as potentially substantial, but it is not an exhaustive novelty certification. The manuscript accurately distinguishes the corrected 2013 claim from the established bound; it does not reuse the withdrawn argument.

## 6. Implications for the 100-agent research plan

The first research priority is to preserve these dimension-free structured theorems and attack the precise remaining obstruction. Re-running broad literature searches or proving the same LTF estimate with slightly smaller constants should consume only a small fraction of the budget.

The principal full-FEI task is to bound the cost of a normalized global description of the whole Fourier set. Any proposed universal bound must pass addressing, rare activation and the stored local-entropy/restriction counterexamples before becoming an active proof dependency. An estimate with a hidden dependence on the number of gates, the number of coordinate orders, or tiny event probabilities is still missing the crucial step.

A second high-value direction is weighted-threshold FEI+ under arbitrary product laws. The audited symmetric-threshold proof identifies a precise place to begin: replace the integer slice concentration and integer-mean mode argument by an appropriate weighted-sum statement while retaining the normalization credit and the near-dictator deficit. Ordinary biased Shannon entropy is the wrong quantity, as the dictator calculation already disproves that version.

Counterexamples to sufficient lemmas must be recorded separately from counterexamples to FEI. The selector and activation equivalences show that seemingly restricted reductions can still contain the complete conjecture with its original optimal constant; a large restricted-family label alone does not demonstrate progress.

## Required corrections

None found in the main theorem, Boolean-combination estimates, biased symmetric-threshold proof, or composition section. Do not change the conclusion to a claim of unrestricted FEI. Record this audit alongside the source and preserve the explicit unresolved weighted-product and global-witness questions.

## Addendum: shared-data multiplexer extension

I independently audited the first shared-data section of `recovered/reductions/fei-reductions-and-witness-coding/paper/multiplexers.tex` as a proposed extension to the public threshold paper. The extension is valid.

For a uniform selector \(x\in\{-1,1\}^a\), branches \(g_b\) on a common data cube and \(F(x,y)=g_x(y)\), the recovered formula

\[
H(F)=a+2^{-a}\sum_b H(g_b)
 +\sum_T R_T[H(\nu_T)-H(r_T)]
\]

is exact. Here \(R_T=2^{-a}\sum_b\widehat g_b(T)^2\); \(r_T\) is the conditional physical branch-label law at the data Fourier set \(T\), and \(\nu_T\) is the squared normalized Walsh transform of the conditional signed coefficient vector. The latter is exactly the conditional selector Fourier-set law. This remains correct at \(T=\varnothing\), so unbalanced branches require no omitted correction term.

The chain-rule bound is \(H(F)\le2a+2^{-a}\sum_b H(g_b)\). The data influence is the average branch influence. If every neighboring pair of branches has zero inner product, every selector bit has influence \(1/2\). Thus a common branch FEI constant \(C\) gives \(H(F)\le\max(4,C)I(F)\).

Consequently a finite recursive construction with regular Boolean leaves, a fresh independent selector at each internal node, and orthogonal neighboring branches at each node satisfies

\[
H(F)\le C_{\rm reg} I(F)<8.937 I(F).
\]

Branches may share all or some data variables and selectors from earlier nodes. The selector introduced at a node must not occur among any of that node's branch inputs. A branch may be viewed on the common union of data variables by adding irrelevant coordinates; its entropy and influence are unchanged. This makes the induction valid even with arbitrary branch reuse.

The supplied shared-data example \(g_+=\operatorname{Maj}_3(y_1,y_2,y_3)\), \(g_-=\operatorname{Maj}_3(y_1,-y_2,y_4)\) has cancelling singleton inner-product contributions, and its one-bit multiplexer has exactly \(H=3\), \(I=2\).

When porting, replace the stale constant 13.415 by \(C_{\rm reg}<8.937\), and replace the external companion-manuscript citation by the threshold paper's internal Theorem A. The remark's reference to `prop:bentsplice` does not resolve inside the threshold paper; remove that reference or supply the actual obstruction. No bound on the entropy increment solely by selector influence is proved or needed for this conditional closure theorem.
