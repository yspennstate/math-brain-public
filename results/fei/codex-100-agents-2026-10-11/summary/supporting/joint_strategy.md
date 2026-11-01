# Full-FEI campaign: joint descriptions, selectors, and rare activation

## Purpose and standard of success

The completed paper supplies useful FEI estimates for regular functions, combinations of structured gates, bounded-overlap unions, and certain compositions. Its new joint witness and selector results identify several places where a coarse argument loses information. A ten-day campaign should attack those explicit losses while independently checking every proposed replacement. It should not treat the existence of many agents as evidence that a full solution is likely.

The main target remains a universal constant \(C\) such that

\[
H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2}
\le C I(f),\qquad
I(f)=\sum_S|S|\widehat f(S)^2,
\]

for every Boolean function on every finite uniform cube. Every task must use this normalization or state its conversion explicitly. Results for min-entropy, a bounded number of gates, low arity, or a fixed overlap parameter must remain visibly distinguished from full FEI.

Three outcomes would justify the effort even if full FEI remains open: a new dimension-free FEI theorem for a broad class beyond the completed paper; a strictly stronger structural inequality with a proof and a demonstrated application; or an explicit counterexample eliminating a proposed route that otherwise would have consumed substantial effort. A reformulation equivalent to full FEI is a useful map of the problem, but it is not counted as a solved intermediate case.

This document recommends six mathematical workstream families. Each family has five distinct logical research roles. For the requested 20 schedules and 100 research roles, the six families can be divided into 20 different five-role pods, as specified near the end. Actual simultaneous execution is an operational question: the campaign ledger must record workers that actually ran, not infer 100 concurrent processes from 20 prompts containing five roles.

## 1. Facts that every worker should inherit

### 1.1 The queue construction now has an exact joint cost

Fix the gate supports \(R_l\), probabilities \(p_l\), \(\pi_l=\min(p_l,1/2)\), and \(b_l=\log_2(1/\pi_l)\). Root odds may be \(\lambda\pi_l\), for any \(\lambda>0\), with normalizing cost

\[
\Lambda_\lambda=\sum_l\log_2(1+\lambda\pi_l).
\]

For a Fourier set \(A\), assign each coordinate to a gate containing it. This gives a partition \(A=\bigsqcup_l A_l\), a set of used gates \(\mathcal F\), and an incidence forest \(\mathcal T\). The finite-run cost \(\mathcal C_\lambda(A;\tau,\mathcal T)\), including every root, subset, size, multiset, and child-label probability, satisfies

\[
H(f)\le h_2(v)+v\Lambda_\lambda+
\sum_{A\ne\varnothing}\widehat f(A)^2
\min_{\tau,\mathcal T}\mathcal C_\lambda(A;\tau,\mathcal T),
\qquad v=\operatorname{Var}(f).
\]

The improved estimate retains

\[
|\mathcal F(A)|\log_2 k
\quad\text{and}\quad
L(A,\tau)=\sum_l|A_l|\log_2\frac{|A\cap R_l|}{|A_l|}
\]

instead of replacing both by multiples of \(|A|\log_2 k\). Dense-root rarity costs are controlled by disjoint root intersections. Sparse-root costs remain an explicit obligation.

**Status:** proved in the completed continuation. The existence of this reference measure is not the missing full-FEI theorem. The missing theorem would control its expected joint cost, after an appropriate choice of representation, without a growing structural parameter.

### 1.2 The addressing benchmark distinguishes joint and repeated charges

For \(m\) address bits and \(2^m\) data bits,

\[
f(a,y)=y_a,\qquad H(f)=2m,\qquad I(f)=1+m/2.
\]

Every nonzero Fourier set is \(T\cup\{y_a\}\). A single conjunction gate contains that whole set, so a witness can have \(|\mathcal F|=1\) and \(L=0\). The refined original queue method gives \(H(f)<10I(f)\); the exact spectrum gives \(H(f)=4(I(f)-1)\).

Any proposed universal budget that charges an \(m\)-bit address separately for a positive fraction of the \(m\) control coordinates fails this test. Such a budget can cost order \(m^2\) even though the actual entropy is \(2m\).

### 1.3 Selector identities and a proved strong closure

Let \(A_j\) partition the control cube, let \(p_j=\Pr(A_j)\), and let balanced Boolean leaves \(g_j\) depend on a data cube disjoint from the control cube. If the leaves have pairwise disjoint Fourier supports, their variable supports may overlap arbitrarily. For

\[
F(z,y)=\sum_j1_{A_j}(z)g_j(y),\qquad
q_j(T)=\widehat{1_{A_j}}(T)^2/p_j,
\]

the exact identities are

\[
H(F)=H(p)+\sum_jp_j[H(q_j)+H(g_j)],\qquad
I(F)=\sum_jp_j[\mathbb E_{q_j}|T|+I(g_j)].
\]

Write \(h_j=2\,1_{A_j}-1\),

\[
D=\frac14\sum_jI(h_j),\qquad
B=\frac14\sum_j\operatorname{Var}(h_j)=\sum_jp_j(1-p_j).
\]

The selector cost is exactly

\[
H(p)+\sum_jp_jH(q_j)=\frac14\sum_jH^+(h_j)+R(p),
\]

where

\[
R(p)=2\sum_jp_j(1-p_j)+2\sum_jp_j^2\log_2(1/p_j)
\le4B.
\]

Thus cell bounds \(H^+(h_j)\le C_s[I(h_j)-\operatorname{Var}(h_j)]\) and leaf bounds \(H(g_j)\le C_g[I(g_j)-1]\) imply

\[
H(F)\le\max\{C_s,C_g,4\}[I(F)-1].
\]

For affine-subspace cells of codimensions \(c_j\), let \(r_j\) be the number of coordinates in the support of the dual linear subspace. Then

\[
H(F)=2\sum_jp_jc_j+\sum_jp_jH(g_j),\qquad
I(F)=\frac12\sum_jp_jr_j+\sum_jp_jI(g_j).
\]

Since \(r_j\ge c_j\), this gives the sharp constant \(4\) for the corresponding selector class with character leaves.

### 1.4 Two different ways unrestricted selectors contain full FEI

For an arbitrary balanced \(g\),

\[
M_g=\frac{1+g}{2}y_1+\frac{1-g}{2}y_2
\]

has

\[
H(M_g)=2+H(g)/2,\qquad I(M_g)=1+I(g)/2.
\]

For arbitrary \(f\), balance its tensor power with one fresh sign:

\[
g_t=z\prod_{r=1}^t f(x^{(r)}),\qquad
H(g_t)=tH(f),\quad I(g_t)=tI(f)+1.
\]

A full-FEI bound on every \(M_{g_t}\) yields full FEI with the same constant after division by \(t/2\) and passage to the limit. Therefore arbitrary selector cells are not a simpler unrestricted target merely because there are only two of them.

There is a second reduction. Partition the control cube into points, and assign the leaf \(f(z)y\) at control point \(z\). Every cell is an affine subspace and every leaf is a signed dictator, but their Fourier supports are reused. The resulting function is \(f(z)y\), with

\[
H(fy)=H(f),\qquad I(fy)-1=I(f).
\]

Consequently, a dimension-free strong affine-selector conclusion for arbitrary shared leaves, with some universal constant, would also solve full FEI. Retaining the sharp constant 4 from the disjoint-spectrum theorem in this unrestricted extension is already impossible: it would give full FEI with constant 4, whereas O'Donnell--Tan exhibit ratios at least 6.278. This is a precise reason to study controlled leaf overlap, not to announce that arbitrary shared leaves are a routine extension.

### 1.5 Rare activation preserves the full entropy/influence difficulty

Let \(A_r\) be a conjunction of \(r\) fresh activation bits, \(p=2^{-r}\), and \(g\) balanced. Then

\[
F=1+A_r(g-1)
\]

satisfies

\[
I(F)=p[I(g)+r],
\]

\[
H(F)=pH(g)+2rp(2-p)
+(1-p)^2\log_2\frac1{(1-p)^2}.
\]

Take \(g_t=z\prod_{s=1}^t f(x^{(s)})\) and \(r_t=\lceil2\log_2t\rceil\). For nonconstant \(f\),

\[
I(F_t)\longrightarrow0,\quad
\Pr(F_t=-1)\longrightarrow0,\quad
\max_i I_i(F_t)\longrightarrow0,
\quad
\frac{H(F_t)}{I(F_t)}\longrightarrow\frac{H(f)}{I(f)}.
\]

For sufficiently large \(t\), every coordinate influence is at most \(1/2\), so \(D(F_t)=I(F_t)\). The variance is negligible relative to \(I(F_t)\), and the ratio with \(I(F_t)-\operatorname{Var}(F_t)\) has the same limit. This prevents a campaign from mistaking tiny variance, small individual influences, or a rare activation event for a general simplification.

**Literature status:** the reduction of FEI to low-influence classes is known, including the stronger dimension-scaled result of Shalev. Exact identities and constant-preserving limits can be useful refinements, but the underlying reduction is not new.

## 2. Workstream A: joint queue descriptions and witness sums

### Research question

Can a useful family of Boolean functions be represented so that the expected complete witness cost is bounded by influence, with no dependence on the number of gates or the maximum number of gate occurrences at one coordinate?

The objective must include the normalization, roots, local subsets, incidence forest, rank costs, and rare-root terms. An estimate that removes only the visible gate-label logarithm does not finish the argument.

### Five research roles

1. **Probability-law constructor:** design normalized or subnormalized reference processes, explicitly accounting for nontermination, repeated visits, and empty outputs.
2. **Forest and cover analyst:** optimize the assignment of whole Fourier sets to gate supports, including \(|\mathcal F|\), \(L(A,\tau)\), roots, and attachments.
3. **Witness-sum analyst:** exploit many valid runs with the same output instead of keeping only the cheapest one; prove that the counted events are disjoint or handle their overlap exactly.
4. **Expected-cost analyst:** connect the resulting cost to derivative laws and influence, with all measure changes stated.
5. **Adversarial verifier:** search for representations where a proposed normalization, forest estimate, or cost comparison fails; maintain exact addressing and rare-activation benchmarks.

### Concrete targets

**A1 — proved interface, to be implemented faithfully.** For any explicitly defined finite family \(\mathcal W(A)\) of distinct successful runs,

\[
Q(A)\ge\sum_{w\in\mathcal W(A)}\Pr(w).
\]

The single-witness estimate can therefore be improved by a logarithmic multiplicity credit. A worthwhile first result is a family where this credit removes a known loss, with the run family explicitly enumerated or counted.

**A2 — candidate structural inequality, not established.** Seek a named class and a specified representation for which

\[
v\Lambda_\lambda+
\mathbb E\!\left[1_{\{\mathcal S\ne\varnothing\}}
\min_{\tau,\mathcal T}\mathcal C_\lambda(\mathcal S;\tau,\mathcal T)\right]
\le C I(f).
\]

The class must be fixed before testing. Full generality is a sufficient route to full FEI, not a theorem already supplied by the reference construction. The converse is not automatic: FEI does not imply that this particular queue representation is efficient.

**A3 — learned priors as diagnostics.** If \(q_l\) is the unconditional probability that gate \(l\) is selected as a root under a proposed spectral assignment, the optimal independent root Bernoulli parameters minimize

\[
v\sum_l\log_2(1+u_l)+\sum_lq_l\log_2(1/u_l).
\]

The optimizer has root probability \(q_l/v\), and its value is \(v\sum_lh_2(q_l/v)\). A joint root-set prior could instead cost \(vH(\mathcal R\mid\mathcal S\ne\varnothing)\). These formulas identify wasted independence assumptions. They are diagnostic identities, not influence bounds. A proof must supply analytically controlled priors; choosing the spectral law itself as the optimal prior is circular.

### Benchmarks and pivot rule

Use addressing, nested selectors, read-once AND/OR formulas, heavily overlapping conjunctions, duplicate gates, and rare activated tensors. If a proposed cost is still order \(m^2\) on \(m\)-bit addressing, stop and locate the repeated information charge before enlarging the proof. If duplicate gates can change the claimed intrinsic bound arbitrarily, either canonicalize the representation or label the theorem as representation-dependent.

A valid theorem for bounded expected witness size, controlled witness congestion, or a new overlap geometry is significant even if it does not cover all Boolean functions.

## 3. Workstream B: tilted derivative pieces and effective complexity

### Research question

The multi-rank proof uses a sum over normalized signed pivotal pieces. When can the cost of this sum be controlled by their actual geometry or mass distribution rather than by the number of pieces?

### Five research roles

1. **Weighted-piece analyst:** derive sharp mass-sensitive replacements for the crude number-of-pieces estimate.
2. **Gram-matrix analyst:** study correlations of the pieces after the positive Fourier multiplier used in the rank proof.
3. **Antichain and order analyst:** identify which common, compatible, or adaptive order structures actually yield an improvement.
4. **Queue-coupling analyst:** transfer any local improvement into the complete joint witness cost without reintroducing repeated gate labels.
5. **Counterexample analyst:** generate coherent-piece examples and bad representations, including globally relevant padding constructions.

### A proved refinement available immediately

Let \(d=\sum_l d_l\) have pairwise disjoint physical supports, \(\alpha_l=\|d_l\|_2^2\), \(\alpha=\sum_l\alpha_l\), and \(a_l=\alpha_l/\alpha\). Define

\[
K_{\mathrm{eff}}=\left(\sum_l\sqrt{a_l}\right)^2\in[1,m].
\]

Use the same rank variable

\[
G(T)=\min_l\ln\frac{r_l}{|T\cap U_l|+1},\qquad Z=e^{-G}.
\]

The completed proof gives, for every piece,

\[
\sum_T\widehat d_l(T)^2e^{-tZ(T)}\le\alpha_l t^{-1/2}.
\]

The triangle inequality in the norm defined by the nonnegative multiplier \(e^{-tZ}\) gives

\[
\mathbb E_\nu e^{-tZ}
\le\alpha^{-1}\left(\sum_l\sqrt{\alpha_l}\,t^{-1/4}\right)^2
=K_{\mathrm{eff}}t^{-1/2}.
\]

Together with the bound by one and the same Frullani integral, this proves

\[
\boxed{\mathbb E_\nu G\le2+\gamma+2\ln K_{\mathrm{eff}}.}
\]

This is a proved consequence of the existing method, supplied here as a campaign seed. It is not included in the completed paper unless separately integrated and checked. It improves the estimate when the pivotal pieces have concentrated masses. Equal piece masses give \(K_{\mathrm{eff}}=m\), so it does not by itself repair addressing.

### Concrete next targets

**B1 — find a nontrivial application.** Identify a class for which the influence-weighted quantity

\[
\sum_i I_i(f)\ln K_{\mathrm{eff},i}
\]

is genuinely smaller than \(I(f)\ln m\), and combine it with an efficient joint reference. Merely replacing \(m\) by a new parameter that equals \(m\) on all relevant examples is not a useful endpoint.

**B2 — candidate Gram bound.** With

\[
\Gamma_{lm}(t)=
\frac{\langle d_l,M_t d_m\rangle}{\sqrt{\alpha_l\alpha_m}},
\qquad \widehat{M_tu}(T)=e^{-tZ(T)}\widehat u(T),
\]

seek a specified structural condition implying

\[
\bigl\langle\sqrt a,\Gamma(t)\sqrt a\bigr\rangle
\le C t^{-1/2}.
\]

This would remove the piece-count term from the rank mean under that condition. The condition must be explicit and independently verifiable. It cannot simply assert the desired operator norm bound under a new name.

**B3 — an explicit obstruction to a bound for every supplied order.** Let \(r\ge2\), let \(B_r\) be the conjunction of \(r\) control bits, let \(A\) be the conjunction of two data bits \(x_1,x_2\), and let \(f_r=A\vee B_r\). Put \(\varepsilon=2^{-r}\). Every coordinate is relevant, while

\[
I(f_r)=1-\varepsilon+\tfrac32r\varepsilon\longrightarrow1.
\]

Order all control coordinates before \(x_1,x_2\), and encode the inputs by the corresponding superincreasing binary score. Represent \(f_r\) by thresholds at its changes along that score, giving \(2^{r+1}-3\) threshold gates. Give every gate that same valid coordinate order, including its irrelevant coordinates at the end in their inherited order. Then \(r_l(x_1)=r+1\) for every gate. The Fourier coefficients of \(f_r\) at \(\{x_1\}\) and \(\{x_1,x_2\}\) both have magnitude \((1-\varepsilon)/2\), while \(I_{x_1}(f_r)=(1-\varepsilon)/2\). Under the derivative law, those two sets together therefore have mass \(1-\varepsilon\). Neither contains a predecessor of \(x_1\), after \(x_1\) is removed. Thus

\[
\mathbb E_{\nu_{x_1}}G_{x_1}\ge(1-\varepsilon)\ln(r+1),
\]

and the ratio \(\sum_i I_i(f_r)\mathbb E G_i/I(f_r)\) diverges. This is not a counterexample to FEI: the original two-conjunction representation is simple. It rules out a uniform rank-mean bound for every supplied threshold representation and fixed order, even when all output coordinates are relevant. Optimizing the representation or the permitted orders can escape it, which is precisely the additional theorem the team must prove.

### Stop/pivot rule

If a proposed improvement uses only piece counts or masses and ignores the correlations demonstrated by addressing, send it immediately to the whole-set team for a joint-code check. If a claimed Gram estimate fails on a simple padded function, do not continue accumulating lemmas around it. Record the counterexample, state the failed quantifier, and reformulate the structural hypothesis.

## 4. Workstream C: selectors with controlled shared spectra

### Research question

The proved selector closure assumes Fourier-disjoint leaves. Can it be extended to orthogonal leaves, bounded spectral overlap, or another condition that permits substantial variable sharing while preventing complete cancellation of selector energy?

### Five research roles

1. **Selector entropy analyst:** derive entropy bounds for the Fourier coefficient sums when leaf spectra overlap.
2. **Boundary-energy analyst:** express and estimate the exact control influence through correlations between neighboring selector leaves.
3. **Affine-partition analyst:** attack the candidate entropy inequality below for affine cells, beginning with cases already implied by recursive partitions.
4. **Low-overlap analyst:** test fixed overlap multiplicity, bounded correlation, and structured character reuse as distinct hypotheses.
5. **Reduction and adversarial analyst:** check whether each proposed extension already contains full FEI through repeated signed dictators or arbitrary two-cell selectors.

### Exact influence identity without Fourier-disjointness

Let \(J(z)\) be the selector label. For arbitrary Boolean leaves, including overlapping variable sets and overlapping spectra,

\[
I(F)=\mathcal E_{\rm control}+\sum_jp_jI(g_j),
\]

where

\[
\mathcal E_{\rm control}
=\frac12\sum_i\mathbb E_z
\left[1-\langle g_{J(z)},g_{J(z^{\oplus i})}\rangle\right].
\]

The inner product is under the uniform data law. This follows directly because the probability that two Boolean leaves differ is half of one minus their correlation. It exposes precisely why selector energy can disappear when leaves are reused.

### Candidate entropy lemma: explicitly unproved

**C1.** For an affine-subspace partition with cell codimensions \(c_j\), and arbitrary Boolean leaves on the separate data cube, investigate

\[
H\!\left(\sum_j1_{A_j}g_j\right)
\stackrel{?}{\le}2\sum_jp_jc_j+\sum_jp_jH(g_j).
\]

This is an exact equality in the proved Fourier-disjoint setting. For point selectors it follows from elementary entropy bounds for the data marginal and the finite control block. For recursive coordinate decision-tree partitions, the usual two-branch entropy estimate can be iterated to obtain the corresponding upper bound. The general affine-partition version must be checked against the literature on unambiguous parity certificates and then proved or refuted; it is not asserted here as a theorem.

**C2 — conditional consequence of C1.** Suppose the leaves are balanced and satisfy strong FEI with constant \(C_g\), and every pair of distinct labels that can be adjacent in the control cube satisfies

\[
\langle g_j,g_l\rangle\le1-\delta
\]

for a fixed \(\delta>0\). Then \(\mathcal E_{\rm control}\ge\delta D\). If C1 holds, it would give

\[
H(F)\le\max\{4/\delta,C_g\}[I(F)-1].
\]

Pairwise orthogonal leaves correspond to \(\delta=1\) and would extend the completed theorem beyond Fourier-disjointness. This is a meaningful intermediate target with a direct influence conclusion. It should be tested first for small shared-variable leaf systems whose Fourier supports overlap but whose functions are orthogonal.

**C3 — bounded spectral overlap.** If every data Fourier coefficient is present in at most \(b\) leaves, a Cauchy bound introduces \(b\), but that alone does not compare the entropy or influence after interference. Seek an explicit entropy-and-energy estimate depending on \(b\) and the boundary correlations. Record whether the resulting coefficient is logarithmic, polynomial, or constant in \(b\). Do not infer a Shannon entropy comparison merely from a pointwise likelihood-ratio bound.

### Mandatory counterexamples

If all leaves equal the same dictator \(y\), then \(F=y\) regardless of the selector partition. The exact Fourier-disjoint entropy formula is therefore false without its hypothesis. The selector contribution to influence also vanishes. If leaves are arbitrary signs of that same dictator at point cells, the output is an arbitrary \(f(z)y\). Any unrestricted closure with a universal constant here contains full FEI, and the proposed value 4 is ruled out by known FEI lower bounds.

There is also an exact algebraic obstruction to treating a coherent Fourier sum as an ordinary mixture, even when its component vectors are orthogonal. In \(\mathbb R^{65}\), let

\[
v_+=(2^{-1/2},128^{-1/2},\ldots,128^{-1/2}),\qquad
v_-=(-2^{-1/2},128^{-1/2},\ldots,128^{-1/2}),
\]

with 64 equal tail entries. Both vectors have norm one and their inner product is zero. Each squared-amplitude distribution has entropy 4 bits. But \(w=(v_++v_-)/\sqrt2\) has squared-amplitude distribution uniform on the 64 tail coordinates, of entropy 6 bits, exceeding the putative mixture cost \(1+(4+4)/2=5\). Zero-padding embeds the example in dimension 128. This refutes an unrestricted coherent-sum entropy lemma; these vectors have not been shown to arise from Boolean leaves or disjoint pivotal pieces. It therefore does not refute C1. Any use of the putative lemma in a Boolean setting requires a separate structural proof, rather than an appeal to orthogonality alone.

### Stop/pivot rule

If C1 fails, preserve the smallest exact counterexample and determine whether orthogonal leaves, recursive partitions, or bounded spectral overlap repair it. If a proposed hypothesis excludes the counterexample only by requiring the desired FEI inequality for the final output, reject it as circular. A proved orthogonal-leaf or fixed-overlap theorem is an adequate significant result; no claim of full FEI should be attached to it.

## 5. Workstream D: activation, restrictions, and telescoping budgets

### Research question

Can entropy increments be allocated across a sequence of restrictions without losing a logarithm on rare events? Exact activation formulas provide a stringent test of every local budget.

### Five research roles

1. **Exact identity analyst:** maintain activation formulas for arbitrary mean, variance, full entropy, nonempty entropy, and influence.
2. **Tensor-limit analyst:** test constant preservation and quantify limits under balancing, tensorization, and rare activation.
3. **Restriction-budget analyst:** formulate global telescoping inequalities whose charges include rare-event normalization terms explicitly.
4. **Counterexample analyst:** construct parameterized rare-event families and compare all terms asymptotically, not just numerically at one parameter.
5. **Noncircularity analyst:** classify each proposed small-influence theorem as a new proved subclass, an equivalent reformulation, or a sufficient but stronger statement.

### Arbitrary-mean activation formula

For \(\mu=\mathbb Eg\), \(c=1-\mu\), \(p=2^{-r}\), and \(u=1-pc\), direct Fourier expansion gives

\[
I(1+A_r(g-1))=p[I(g)+r(1-\mu)],
\]

\[
\begin{aligned}
H(1+A_r(g-1))={}&pH^+(g)+2rp(1-\mu^2)\\
&+(p-p^2)c^2\log_2\frac1{p^2c^2}
+u^2\log_2\frac1{u^2}.
\end{aligned}
\]

Zero-mass terms have their continuous value zero. The formula follows by separating Fourier sets with nonempty data part, activation-only sets, and the empty set. This provides a direct cross-check for the balanced formula and for any use of nonempty entropy.

### Concrete targets

**D1 — falsifiable local-budget test.** Any proposed estimate that replaces a conditional entropy cost on an event of probability \(p\) by a constant times \(p\), while omitting its \(p\log(1/p)\) normalization contribution, must be tested against the activation formula. A successful global proof may pay this logarithm from activation influence, combine it with other levels, or cancel it through an exact corrected entropy. It may not discard it.

**D2 — candidate global budget, not established.** Design a restriction tree with a completely specified entropy identity and prove that the sum of its local correction terms is bounded by \(CI(f)\). First settle finite-depth versions with constants independent of the ambient dimension and explain exactly which structural parameter remains. The identity for the sum must be verified before proving bounds on its individual terms.

**D3 — detect concealed full-FEI assumptions.** If a hypothesis covers all sufficiently rare activations of arbitrary balanced tensor products, the constant-preserving reduction above recovers full FEI. Such a hypothesis should be labeled a reformulation or a full-strength sufficient condition, not a technical lemma that can be assumed temporarily without consequence.

### Stop/pivot rule

If the same missing logarithmic charge recurs after two reformulations, stop changing notation and ask which level of the restriction process could pay it. If no cross-level identity is available, pivot to a structural subclass. A theorem for a fixed activation grammar or a proof that a proposed local principle is false is useful. Repeating a known low-influence equivalence is not progress by itself.

### A fixed Rényi strengthening is false: the point-defect diagnostic

Let \(f_r=1-2\,1_{\{x=x_0\}}\) on an \(r\)-dimensional cube and put \(p=2^{-r}\). Its total influence is \(I(f_r)=2rp\). Its spectral probabilities are

\[
P_0=(1-2p)^2,\qquad P_S=4p^2\quad(S\ne\varnothing).
\]

For any fixed \(0<\alpha<1\), its spectral Rényi entropy is

\[
H_\alpha(f_r)=\frac1{1-\alpha}\log_2\left[(1-2p)^{2\alpha}
+4^\alpha(1-p)p^{2\alpha-1}\right].
\]

Consequently \(H_\alpha(f_r)/I(f_r)\to\infty\) for every fixed \(\alpha<1\). The asymptotics make all three regimes explicit:

- If \(0<\alpha<1/2\), then \(H_\alpha(f_r)\sim[(1-2\alpha)/(1-\alpha)]r\).
- If \(\alpha=1/2\), then \(H_{1/2}(f_r)=2\log_2(3-4p)\to2\log_2 3\).
- If \(1/2<\alpha<1\), then
  \[
  H_\alpha(f_r)\sim\frac{4^\alpha}{(1-\alpha)\ln2}p^{2\alpha-1},\qquad
  \frac{H_\alpha(f_r)}{I(f_r)}
  \sim\frac{4^\alpha}{2(1-\alpha)\ln2}\frac{p^{2\alpha-2}}r\to\infty.
  \]

Thus a proposed uniform bound \(H_\alpha(f)\le CI(f)\) at a fixed spectral Rényi order below one is not a stronger open version of FEI; it is false. A moment method must use a more delicate, possibly scale-dependent statement. This diagnostic does not rule out Rényi quantities for auxiliary piece distributions, such as \(K_{\mathrm{eff}}\) in §3. No novelty claim is made for the point-defect example.

## 6. Workstream E: representations and broad intermediate classes

### Research question

Which concrete representation choices make the completed estimates efficient, and can one prove that every function in a substantially larger class admits such a representation?

### Five research roles

1. **Representation constructor:** build gate and selector representations with controlled whole-set costs, rather than merely small syntactic size.
2. **Composition analyst:** determine which representation bounds survive tensor products, restrictions, character multiplication, and balanced substitution.
3. **Normal-form analyst:** remove duplicate gates, irrelevant coordinates, and avoidable choices while proving that the represented function is unchanged.
4. **Structural theorem analyst:** prove existence of efficient representations under a stated, independently checkable hypothesis.
5. **Separation analyst:** exhibit functions for which syntactic gate count, variable overlap, and actual Fourier description cost differ substantially.

### Concrete targets

**E1.** Prove closure of an explicitly defined efficient-witness class under one operation not already covered by the paper. The operation and cost transformation must be written as a theorem, including the behavior of empty coefficients and strong deficits.

**E2.** Seek an intrinsic upper bound for the minimum witness cost over a specified finite family of representations. Optimizing over all imaginable codes is not a structural result: an optimal Shannon code for the spectral set has cost approximately \(H(f)\), so the resulting statement can simply restate FEI.

**E3.** A useful intermediate theorem could cover selector compositions with constant correlation gap, a new family of overlapping structured unions, or a representation whose expected number of used gate labels is small despite large worst-case overlap. The importance of such a theorem should be judged by the functions newly covered, not just by a smaller numerical constant on the old class.

### Stop/pivot rule

Reject representation statistics that can be inflated arbitrarily by adding duplicate gates unless the theorem minimizes over representations or includes a canonicalization rule. Conversely, do not claim an intrinsic statistic is efficiently computable without an algorithm and a complexity bound. A structural existence theorem may be valuable even when finding the representation is computationally difficult.

## 7. Workstream F: proof integration, counterexample registry, and novelty audit

### Research question

Which combination of independently verified statements actually implies the full target, and where does a proof chain still require a full-strength unproved assertion?

### Five research roles

1. **Dependency-graph reviewer:** turn every proposed argument into a graph of formal statements with explicit assumptions and constants.
2. **Independent proof reviewer:** rederive decisive lemmas without reading the originating agent's proof first, then reconcile differences.
3. **Exact finite verifier:** maintain Walsh-transform and rational-arithmetic checks for identities, counterexamples, normalizations, and low-dimensional special cases.
4. **Literature reviewer:** verify primary sources, theorem scope, constants, corrections, and whether a purported improvement is already known.
5. **Synthesis reviewer:** produce a concise theorem-and-proof handoff and a separate account of unresolved obligations; never merge a conjectural lemma into an unconditional theorem.

### Required claim record

Every claim should have a unique identifier; its exact statement; quantifiers; logarithm base; measure and normalization; status; proof or counterexample; dependencies; tests; primary-source comparison; and next decisive action. The allowed statuses are proved, independently checked, conjectured, disproved, equivalent to full FEI, sufficient for full FEI, or blocked on a named statement. A statement may have multiple status fields, for example proved but not independently checked.

Every counterexample should include its truth-table or formula family, parameter regime, exact or certified Fourier calculation, the failed inequality, and the smallest known instance. Asymptotic examples must include the ratio that diverges. Descriptions such as 'the local cost seems too high' are insufficient.

### Mandatory benchmark suite

Include constants and characters; conjunctions and disjunctions; majority and small weighted thresholds; arbitrary character shifts; addressing; unequal subcube selectors; affine-subspace selectors; shared-variable leaves with disjoint spectra; shared spectra with orthogonal functions; identical leaves; repeated signed-dictator leaves encoding arbitrary functions; rare activated tensors; duplicate-gate representations; and carefully chosen bad coordinate orders.

The previously recorded Brain counterexamples about local spectral entropies and rare restrictions should be imported by their exact artifacts and statements before being cited. Their informal summaries are not enough to define a test. This report relies only on the explicit addressing, selector, and activation obstructions written above.

### Stop/pivot rule

No apparent full solution advances to manuscript status until two independent proof reviewers have checked its decisive new lemma, the reduction team has identified every assumption, and the exact benchmark suite has passed. Passing finite tests cannot certify a universal theorem. Conversely, a valid proof should not be delayed by endless optional enumeration once its concrete normalization risks have been resolved.

## 8. Mapping the six families to 20 schedules and 100 roles

The authoritative campaign roster is `campaign/teams.json`, maintained by the root coordinator. The following is a mathematical coverage suggestion, not a replacement roster or an instruction to change team identifiers. It shows how the six families could supply 20 different five-role pods. The actual assignments must follow the canonical roster, with distinct claims or regimes rather than duplicate broad 'solve FEI' prompts.

| Family | Pods | Distinct assignments |
|---|---:|---|
| A: joint queue descriptions | 4 | Exact forest optimization; witness multiplicity sums; joint root/child priors; structured overlap families |
| B: tilted derivative pieces | 4 | Effective mass bound applications; Gram bounds; compatible/adaptive orders; local-to-joint cost transfer |
| C: shared-spectrum selectors | 4 | Affine entropy candidate C1; orthogonal leaves; fixed spectral overlap; correlation-gap closure |
| D: rare activation and restrictions | 3 | Arbitrary-mean identities and limits; local-budget counterexamples; global restriction telescoping |
| E: efficient representations | 3 | Canonical forms; composition stability; new structural existence theorems |
| F: proof integration and review | 2 | Independent proof and dependency audit; exact benchmark and literature audit |
| **Total** | **20** | **100 logical research roles** |

A coordinator should give each of its five roles a finite assignment and require a written handoff during that invocation. It should not assume that a subagent persists after the invocation ends. Every new run should read the current claim ledger, unresolved reviewer requests, and the previous handoff before opening a new direction. The actual model, invocation count, completed proof obligations, and saved outputs should be reported accurately by the operational coordinator.

## 9. Ten-day decision schedule

### Days 1–2: define and attack the exact claims

Freeze the normalization and baseline formulas. Import the completed paper and exact Brain counterexamples. Assign one falsifiable intermediate claim to each pod. Run the smallest decisive tests first. Establish which proposed targets are already known or equivalent to full FEI. At the end of day 2, each pod must have a proof, a counterexample, a reduced unresolved lemma, or a clear reason to pivot; a narrative progress note alone is insufficient.

### Days 3–5: prove structural improvements

Prioritize claims that survive adversarial tests and would expand the covered function class. Transfer local improvements into a complete entropy bound immediately, so that hidden normalizers or repeated labels are discovered early. For each promising statement, assign a reviewer from a different family. If an estimate only improves a constant in a class already covered, keep it as a bounded side task and return the main workers to the full-FEI obstruction.

### Days 6–8: combine compatible results

Build the dependency graph for the strongest unconditional theorem available. Test tensor stability, rare-activation behavior, and character centering. Try the proposed full-FEI reduction only after all of its component estimates are proved. If one remaining lemma is equivalent to full FEI, state that plainly and give it the concentrated effort; do not present the surrounding argument as an almost-complete proof with a minor gap.

### Days 9–10: independent reconstruction and final result

Reconstruct the strongest argument from its statements without relying on earlier explanatory prose. Resolve reviewer objections and reproduce exact checks. Deliver the full theorem or the strongest proved partial theorem, all necessary proofs and references, the counterexample registry, and the precise remaining obstacle. If full FEI is not solved, the final report should say so directly and explain which mathematical capability is still missing.

## 10. Sources and novelty boundaries

- The completed local manuscript: `final/fourier-entropy-threshold-functions/paper/main.tex`, including the exact joint witness, selector, and activation sections. Its mathematical claims are the campaign's working foundation; independent review remains appropriate.
- Andrew Wan, John Wright, Chenggang Wu, *Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture*: https://arxiv.org/abs/1312.3003. Relevant for spectral communication, decision-tree coding, composition, and activation reductions.
- Ryan O'Donnell and Li-Yang Tan, *A Composition Theorem for the Fourier Entropy-Influence Conjecture*: https://arxiv.org/abs/1304.1347. Relevant for FEI+ and disjoint substitution.
- Srinivasan Arunachalam, Sourav Chakraborty, Michal Koucký, Nitin Saurabh, Ronald de Wolf, *Improved Bounds on Fourier Entropy and Min-Entropy*: https://arxiv.org/abs/1809.09819. Relevant for average unambiguous parity-certificate entropy bounds and for checking candidate C1 against existing methods.
- Guy Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*: https://arxiv.org/abs/1806.03646. In particular, Theorem 3 and Section 3.2 show that low-influence reductions retain the full problem.
- María José González, Paul MacManus, María Cristina Pereyra, *Further Evidence Towards the Fourier Entropy-Influence Conjecture*: https://arxiv.org/abs/2606.00246. Relevant to restriction increments and stopping trees; current exact theorem scope should be checked before assigning a novelty claim.

The weighted effective-piece lemma in §3 is derived above from the completed rank proof. Candidate C1, a general influence bound for the joint queue cost, and a dimension-free global restriction budget are deliberately labeled research targets. None is assumed in any stated unconditional consequence.
