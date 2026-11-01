# Seed lemmas for the full-FEI campaign

**Status:** direct derivations, reviewed internally; separate from the completed threshold manuscript. These are not claims of novelty, external peer review, or a proof of full FEI. The hypotheses below are part of each statement. The effective-piece argument and prior mixture are useful interfaces; a dimension-independent bound on their complete expected cost remains an additional obligation.

**Prepared:** 11 October 2026. **Research roles concerned:** F01–F04 for reference distributions and piece costs; F15 and F17 for reductions and asymptotic diagnostics; F19 for independent reconstruction.

Throughout, Fourier expansions use the uniform probability measure on a finite cube. Write \(\widehat d(T)=\mathbb E[d\chi_T]\), so Parseval gives \(\|d\|_2^2=\sum_T\widehat d(T)^2\). Entropy and code lengths use \(\log_2\). The rank variable \(G\), Laplace parameter, and Euler constant \(\gamma\) use natural logarithms.

## 1. Effective piece count in the multi-order rank estimate

### Statement with explicit structural hypotheses

Let \(d_1,\ldots,d_m:\{-1,1\}^N\to\{0,\pm1\}\) be nonzero functions with pairwise disjoint physical supports. Thus \(d_l(x)d_k(x)=0\) for every \(x\) when \(l\ne k\). Put

\[
d=\sum_{l=1}^m d_l,\qquad
\alpha_l=\|d_l\|_2^2>0,\qquad
\alpha=\|d\|_2^2=\sum_l\alpha_l,
\qquad a_l=\alpha_l/\alpha.
\]

For each \(l\), let \(U_l\subseteq[N]\) have size \(r_l-1\), where \(r_l\ge1\). Assume that, for every fixed assignment of the coordinates outside \(U_l\), the support of \(d_l\) in the remaining \(U_l\)-cube is an antichain, in one fixed orientation for that piece. The orientations and coordinate sets may differ between pieces.

Define the probability laws and rank quantities

\[
\nu_l(T)=\frac{\widehat d_l(T)^2}{\alpha_l},\qquad
\nu(T)=\frac{\widehat d(T)^2}{\alpha},\qquad
\kappa_l(T)=|T\cap U_l|,
\]

\[
G(T)=\min_l\ln\frac{r_l}{\kappa_l(T)+1},\qquad
Z(T)=e^{-G(T)}=\max_l\frac{\kappa_l(T)+1}{r_l},
\qquad
K_{\mathrm{eff}}=\left(\sum_l\sqrt{a_l}\right)^2.
\]

Then

\[
1\le K_{\mathrm{eff}}\le m,
\qquad
\mathbb E_\nu e^{-tZ}\le\min\{1,K_{\mathrm{eff}}t^{-1/2}\}
\quad(t>0),
\]

and

\[
\boxed{\mathbb E_\nu G\le 2+\gamma+2\ln K_{\mathrm{eff}}.}
\]

Zero pieces may be omitted. Adding further coordinate orders to the minimum defining \(G\) can only decrease \(G\), so it does not invalidate the conclusion. Multiplication of every piece by the same coordinate character preserves the hypotheses.

### Proof of the piecewise estimate

For \(0<u\le1\), resample each coordinate in \(U_l\) independently at rate \(u\). If \(B\sim\operatorname{Bin}(r_l-1,u)\), the antichain density estimate in the resampled subcube gives

\[
\mathbb E_{\nu_l}(1-u)^{\kappa_l}
\le \mathbb E\frac1{\sqrt{B+1}}
\le \frac1{\sqrt{r_lu}}.
\]

The first step also holds for arbitrary signs on the support: bound the signed noise inner product by the probability that both evaluations lie in the support. For the second step, Cauchy–Schwarz and

\[
\mathbb E\frac1{B+1}
=\frac{1-(1-u)^{r_l}}{r_lu}
\le\frac1{r_lu}
\]

give the displayed bound. This is precisely the signed relative-noise lemma from the baseline manuscript.

Set \(u=1-e^{-t/r_l}\). Since \(1-e^{-s}\ge se^{-s}\) for \(s\ge0\),

\[
\mathbb E_{\nu_l}e^{-t(\kappa_l+1)/r_l}
\le \frac{e^{-t/r_l}}{\sqrt{r_l(1-e^{-t/r_l})}}
\le t^{-1/2}.
\]

Consequently, because \(Z\ge(\kappa_l+1)/r_l\),

\[
\sum_T e^{-tZ(T)}\widehat d_l(T)^2
\le\alpha_l t^{-1/2}.
\]

### Proof of the effective-piece refinement

Let \(M_t\) be the positive Fourier multiplier whose multiplier at \(T\) is \(e^{-tZ(T)}\). The preceding inequality says

\[
\|M_t^{1/2}d_l\|_2\le\sqrt{\alpha_l}\,t^{-1/4}.
\]

The triangle inequality, applied before squaring, now gives

\[
\begin{aligned}
\mathbb E_\nu e^{-tZ}
&=\frac{\|M_t^{1/2}\sum_l d_l\|_2^2}{\alpha}\\
&\le \frac{\left(\sum_l\|M_t^{1/2}d_l\|_2\right)^2}{\alpha}\\
&\le\frac{(\sum_l\sqrt{\alpha_l})^2}{\alpha}\,t^{-1/2}
=K_{\mathrm{eff}}t^{-1/2}.
\end{aligned}
\]

The bound by one follows since \(\nu\) is a probability law. Because \(a_l\ge0\) and \(\sum_l a_l=1\), squaring \(\sum_l\sqrt{a_l}\) gives the lower bound one, and Cauchy–Schwarz gives the upper bound \(m\).

We have \(0<Z\le1\). Pointwise Frullani integration and nonnegative integration therefore give

\[
\mathbb E_\nu G
=\int_0^\infty\frac{\mathbb E_\nu e^{-tZ}-e^{-t}}t\,dt.
\]

With \(K=K_{\mathrm{eff}}\) and \(A=K^2\), this is at most

\[
\begin{aligned}
&\int_0^A\frac{1-e^{-t}}t\,dt
+\int_A^\infty\frac{Kt^{-1/2}-e^{-t}}t\,dt\\
&\hspace{2em}=\ln A+\gamma+\frac{2K}{\sqrt A}
=2\ln K+\gamma+2.
\end{aligned}
\]

The integral identity used here is
\(\int_0^A(1-e^{-t})\,dt/t-\int_A^\infty e^{-t}\,dt/t=\ln A+\gamma\).

### Scope and limits

The multiplier argument only needs orthogonality of the pieces and the displayed piecewise Laplace estimate. Disjoint physical supports and signed fiber antichains are concrete sufficient conditions supplied by the baseline derivative partition. Orthogonality by itself does not supply the piecewise estimate.

Equal masses give \(K_{\mathrm{eff}}=m\). The lemma can improve a mass-concentrated derivative decomposition; it does not prove that every Boolean function admits such a decomposition, pay the remaining reference normalizer, or establish \(\sum_i I_i\ln K_{\mathrm{eff},i}=O(I)\). Any claimed FEI consequence must account for those terms separately in the complete description bound.

**Source pointers.** The baseline manuscript `main.tex`, SHA256 `3a395e98153f826fa9160c348e45779f204d3ea77376f40cd71ee57440ba8193`, has the signed relative-noise lemma at LaTeX label `lem:antichain-noise`, the derivative partition at `eq:pieces`, and the original multi-order proof at `lem:multi-rank`. Its archived copy is retained under `baseline/`. The direct effective-piece derivation was recorded in `supporting/joint_strategy.md`, Workstream B. The working source before campaign assembly was `final/fourier-entropy-threshold-functions/paper/main.tex`.

## 2. A normalized prior over complete reference laws

### General statement

Let \(P\) be a probability law on the subsets of a finite set and let
\(v=P(\mathcal S\ne\varnothing)\). For every index \(j\) in a finite or countable set, let \(Q_j\) be a subprobability law on the nonempty subsets:

\[
Q_j(A)\ge0,\qquad \sum_{A\ne\varnothing}Q_j(A)\le1.
\]

Choose weights \(w_j\ge0\) with \(\sum_jw_j\le1\), fixed across the Fourier sets being described, and put

\[
Q_{\mathrm{mix}}(A)=\sum_jw_jQ_j(A).
\]

For every \(j\) with \(w_j>0\), suppose a complete cost bound \(b_j(A)\) is known:

\[
Q_j(A)\ge2^{-b_j(A)}.
\]

Infinite costs are allowed where the reference provides no support. Then

\[
\boxed{
H(P)\le h_2(v)+\sum_{A\ne\varnothing}P(A)
\inf_{j:w_j>0}\left[b_j(A)+\log_2\frac1{w_j}\right].
}
\]

If the family is finite, the infimum is a minimum. For a countable family of nonnegative costs it is also attained whenever it is finite, since only finitely many weights can exceed any fixed positive threshold. Writing an infimum avoids needing this attainment observation.

### Proof

Nonnegative summation gives

\[
\sum_{A\ne\varnothing}Q_{\mathrm{mix}}(A)
=\sum_jw_j\sum_{A\ne\varnothing}Q_j(A)
\le\sum_jw_j\le1.
\]

When \(v>0\), let \(R(A)=P(A)/v\) be the conditional law given a nonempty set. Gibbs' inequality for a subprobability reference gives

\[
H(R)\le\sum_{A\ne\varnothing}R(A)\log_2\frac1{Q_{\mathrm{mix}}(A)}.
\]

This follows by normalizing \(Q_{\mathrm{mix}}\), applying nonnegativity of KL divergence, and observing that the logarithm of its total mass is nonpositive. If a required reference probability is zero, the bound is simply infinite.

For every positive-weight index,

\[
Q_{\mathrm{mix}}(A)\ge w_jQ_j(A)\ge w_j2^{-b_j(A)}.
\]

Take negative base-two logarithms, optimize over \(j\), and use
\(H(P)=h_2(v)+vH(R)\). The case \(v=0\) is immediate: \(P\) is concentrated at the empty set and has zero entropy.

### Application to the queue references

For a fixed gate construction and each global \(\lambda_j>0\), the completed finite-witness proposition provides a subprobability law \(Q_{1,\lambda_j}\) and

\[
b_j(A)=\Lambda_{\lambda_j}
+\min_{\tau,\mathcal T}\mathcal C_{\lambda_j}(A;\tau,\mathcal T),
\qquad
\Lambda_\lambda=\sum_l\log_2(1+\lambda\pi_l).
\]

Here \(\mathcal C\) is the full cost of a terminating queue witness: root odds, subset sizes and normalizers, subset weights, attachment multisets, child counts, and child-gate labels. The proposition proves that each such witness has probability exactly \(2^{-\Lambda_\lambda-\mathcal C_\lambda}\). Optimizing finite witnesses is valid because they all lower-bound the same reference mass.

Applying the general statement with \(P(A)=\widehat f(A)^2\) therefore gives

\[
\begin{aligned}
H(f)\le h_2(v)+\sum_{A\ne\varnothing}\widehat f(A)^2
\inf_{j:w_j>0}\bigg[
&\Lambda_{\lambda_j}
+\min_{\tau,\mathcal T}\mathcal C_{\lambda_j}(A;\tau,\mathcal T)\\
&+\log_2\frac1{w_j}\bigg].
\end{aligned}
\]

Every term inside the brackets belongs to the selected complete reference. In particular, \(\Lambda_{\lambda_j}\) cannot be optimized separately from its witness cost, and the scale-selection charge cannot be discarded.

### An explicit dyadic prior

For \(j\in\mathbb Z\), let

\[
\lambda_j=2^j,\qquad
w_j=\frac{2}{3(|j|+1)(|j|+2)}.
\]

These weights sum to one: the \(j=0\) weight is \(1/3\), and each positive or negative half-line has total mass \(1/3\), by telescoping. The selector penalty is exactly

\[
\log_2\frac1{w_j}
=\log_2\frac32+\log_2(|j|+1)+\log_2(|j|+2).
\]

This is a legitimate logarithmic penalty in the scale index. It does not by itself bound its spectral expectation by influence. A successful application must prove that expectation estimate, including the variance term and all sparse-root costs.

**Source pointers.** The same baseline manuscript supplies `eq:gibbs`, the queue-generation subsection in Section 5, and `prop:joint-witness`. The generalized root odds and exact finite-run proof were also recorded in the working file `joint_charging/variational_witness.tex`. The prior mixture is a direct subprobability/Gibbs argument, recorded separately from the baseline during preparation of the campaign report. It is not an additional theorem attributed to the completed manuscript.

## 3. Every fixed spectral Rényi order below one fails on a point defect

### Exact family and Fourier law

For an integer \(r\ge1\), fix \(x_0\in\{-1,1\}^r\) and let

\[
f_r(x)=1-2\mathbf1_{\{x=x_0\}},\qquad p=2^{-r}.
\]

The indicator has Fourier coefficient \(p\chi_S(x_0)\) at every \(S\). Therefore

\[
\widehat f_r(\varnothing)=1-2p,\qquad
\widehat f_r(S)=-2p\chi_S(x_0)\quad(S\ne\varnothing),
\]

and its spectral probabilities are

\[
P_\varnothing=(1-2p)^2,\qquad
P_S=4p^2\quad(S\ne\varnothing).
\]

There are \(p^{-1}-1\) nonempty subsets, and their mass together with the empty coefficient sums to one. For each coordinate, exactly \(2^{r-1}\) subsets contain it, giving

\[
I_i(f_r)=2^{r-1}4p^2=2p,\qquad
I(f_r)=2rp.
\]

### Rényi entropy and all three regimes

Fix \(0<\alpha<1\), independently of \(r\). By definition,

\[
H_\alpha(f_r)=\frac1{1-\alpha}\log_2 Z_\alpha,
\]

where the exact moment is

\[
\begin{aligned}
Z_\alpha
&=(1-2p)^{2\alpha}+(p^{-1}-1)(4p^2)^\alpha\\
&=(1-2p)^{2\alpha}+4^\alpha(1-p)p^{2\alpha-1}.
\end{aligned}
\]

If \(1/2<\alpha<1\), then \(0<2\alpha-1<1\) and \(p=o(p^{2\alpha-1})\). Expanding the empty term and then \(\ln(1+x)\) gives

\[
Z_\alpha=1+4^\alpha p^{2\alpha-1}+o(p^{2\alpha-1}),
\]

\[
H_\alpha(f_r)\sim
\frac{4^\alpha}{(1-\alpha)\ln2}\,p^{2\alpha-1},
\]

and hence

\[
\frac{H_\alpha(f_r)}{I(f_r)}
\sim\frac{4^\alpha}{2(1-\alpha)\ln2}
\frac{p^{2\alpha-2}}r\longrightarrow\infty.
\]

If \(\alpha=1/2\), then \(1-2p\ge0\) and the exact simplification is

\[
Z_{1/2}=3-4p,\qquad
H_{1/2}(f_r)=2\log_2(3-4p)\longrightarrow2\log_2 3>0.
\]

Since \(I(f_r)\to0\), its entropy-to-influence ratio also diverges.

If \(0<\alpha<1/2\), the nonempty contribution dominates, so

\[
\log_2 Z_\alpha=(1-2\alpha)r+2\alpha+o(1),
\qquad
H_\alpha(f_r)\sim\frac{1-2\alpha}{1-\alpha}\,r.
\]

This gives a divergent ratio as well. Thus

\[
\boxed{
\text{For every fixed }0<\alpha<1,\quad
\frac{H_\alpha(f_r)}{I(f_r)}\longrightarrow\infty.
}
\]

### The Shannon ratio and the precise obstruction

At Shannon entropy the exact expression is instead

\[
H(f_r)
=(1-2p)^2\log_2\frac1{(1-2p)^2}
+8p(1-p)(r-1).
\]

The first term is \(4p/\ln2+O(p^2)\), so

\[
\frac{H(f_r)}{I(f_r)}\longrightarrow4.
\]

The family refutes a universal inequality \(H_\alpha(f)\le C_\alpha I(f)\) for every fixed \(\alpha<1\), even when \(C_\alpha\) may depend on that fixed order. It does not refute Shannon FEI, estimates whose order or correction depends on scale, or Rényi quantities of an auxiliary piece distribution such as \(K_{\mathrm{eff}}\). These are different mathematical statements.

**Source pointers.** This calculation is obtained directly from the displayed truth table and Walsh expansion. It was recorded in `supporting/joint_strategy.md`, Workstream D, and the campaign report's asymptotic diagnostics. The historical Brain also records failures of fixed Rényi strengthenings; the campaign source manifest supplies the recovered records and their original pins. No novelty claim is made, and no appeal to a historical calculation is needed for the proof above.

## 4. Review and acceptance boundaries

The displayed statements were checked algebraically against the baseline's signed antichain and queue interfaces. Finite computations are not used as a substitute for the proofs. The report audit also independently verified the point-defect asymptotics and the need to retain each normalization term.

An application is a separate claim. It must state which representation is chosen, which ranks and pieces satisfy Section 1, which complete laws and fixed priors satisfy Section 2, and how the entire resulting expectation is paid. The existence of a valid reference and a bound on one of its components does not settle the full entropy-influence inequality.
