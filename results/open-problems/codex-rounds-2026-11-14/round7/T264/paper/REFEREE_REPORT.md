MINOR — Theorem 1.1 is proved in substance, including its width and measurable-selection quantifiers, but a displayed estimate in Proposition 4.3 needs an elementary repair and the introduction needs more careful statements about the literature and norm conventions.

I read all of `paper/main.tex`, `paper/notation.tex`, and `paper/check_tents.py`. References below give the source line as well as the printed theorem or equation number where available. I have not edited `paper`. This review was conducted without network access. The proof assessment is independent of the paper's declarations of previous checking. The literature assessment has a material limitation: I could not locate local primary texts of the six research references, so I cannot certify their exact theorem statements or an exhaustive priority search through November 2026. I distinguish that limitation from an identified mathematical error below.

## 1. Errors and gaps requiring correction

### 1.1. Proposition 4.3: the last displayed chain uses an unjustified sum estimate

**Place:** Section 4, Proposition `local` (4.3), the unnumbered display after (4.2), `main.tex:213–215`.

The proof writes

\[
\|\theta f_\theta+2\sigma(-e_2\cdot {})\|_\infty
\le E_\theta+A_\theta+|B_\theta-2|
\le(1+\kappa^{-1})E_\theta+\theta H/\kappa+U_\theta-2.
\]

The second inequality is not the scalar consequence of the preceding bounds that the text suggests. The proof knows

\[
2\le M_\theta=A_\theta+B_\theta\le U_\theta,
\qquad A_\theta\le(\theta H+E_\theta)/\kappa.
\]

When $B_\theta<2$, the sum $A_\theta+|B_\theta-2|$ is $2A_\theta+2-M_\theta$; bounding $A_\theta$ once does not justify the displayed substitution. This is a flaw in that inference, not a counterexample to localization.

**Repair:** actually use the disjoint supports mentioned immediately before the display. The correct estimate is

\[
\begin{aligned}
\|\theta f_\theta+2\sigma(-e_2\cdot {})\|_\infty
&\le E_\theta+\max\{A_\theta,|B_\theta-2|\}\\
&\le E_\theta+A_\theta+U_\theta-2\\
&\le(1+\kappa^{-1})E_\theta+\theta H/\kappa+U_\theta-2.
\end{aligned}
\]

Indeed $B=M-A$, with $2\le M\le U$, gives $2-B\le A$ and $B-2\le U-2$. This proves the middle bound. No claimed limit or tail constant changes. Alternatively, the text has already established $A_\theta\to0$ and $B_\theta\to2$, which suffices without the last quantitative substitution. This is a minor, completely repairable proof error.

### 1.2. The positive-moment domain should be explicit in Theorem 1.1

**Place:** Section 1, Theorem 1.1, sentence after (1.2), `main.tex:60`.

“$\mathbb E R_n^r<\infty$ if and only if $0<r<\alpha$” should be preceded by “For $r>0$.” Taken as a statement about unrestricted real $r$, it is false at $r=0$, since $R_n>0$ almost surely and $\mathbb E R_n^0=1$. The intended positive-moment assertion is proved, including divergence at the endpoint. This is a domain clarification, not a failure of the tail result.

I found no further substantive mathematical gap. In particular, the Carathéodory reduction, compactness argument, restricted spanning argument, choice of $\theta_1$, event probability, and constants in the upper and lower tail bounds survive independent derivation. Details follow so that this conclusion can be checked.

## 2. Independent derivation of the load-bearing steps

### 2.1. Atomic cost, reduction, existence, and risk

**Places:** Section 2, (2.1), Lemmas 2.1 `risk` and 2.2 `reduce`, `main.tex:80–100`.

For each nonzero hidden weight, homogeneity gives $\gamma=a\|w\|$ and $u=w/\|w\|$. The inequality

\[
\tfrac12(a^2+\|w\|^2)\ge |a|\|w\|=|\gamma|
\]

is sharp at the balanced realization printed in the paper. Thus finite atomic interpolation and parameter interpolation have the same minimum cost. Minimizing $Q$ is also equivalent to minimizing the Euclidean parameter norm, since $Q$ is half its square.

The reduction really gives **$n$** atoms, not merely $n+1$. For a dependence $\nu$ among the signed evaluation vectors, orienting it so that $\sum\nu_j\ge0$ ensures that some $\nu_j>0$. The proposed step preserves evaluations, preserves nonnegativity, deletes a positive coefficient, and changes the cost by $-\lambda\sum\nu_j\le0$. Iteration proves the claim. It preserves the function on the sample, not necessarily elsewhere; the subsequent proof does not assume otherwise.

There is no fatal circularity between Lemma 2.2 and Proposition 3.3. The algebraic reduction is proved first. The tents provide a finite feasible representation; that already established reduction gives feasibility at width $n$. Closed interpolation constraints and compact $Q$-sublevels then give a minimizer at fixed width. Reduction and balancing show that the minimum over all finite widths equals the width-$n$ minimum; zero units allow every fixed $m\ge n$.

For a unit direction, $\mathbb E\sigma(u\cdot X)^2=1/(2d)$, by symmetry and isotropy. Minkowski gives

\[
\sqrt{R(f)}\le\sum_j|\gamma_j|/\sqrt{2d},
\qquad R(f)\le T^2/(2d)\le Q^2/(2d).
\]

There is no missing factor of two or square here.

### 2.2. Gaussian tangent direction and the tents

**Places:** Section 3, Lemmas 3.1 `tangent` and 3.2 `tent`, (3.1), Proposition 3.3 `tents`, `main.tex:110–137`.

At $\varepsilon=1/(4N)$, the small-ball union bound is at most $\sqrt{2/\pi}/4$. The norm failure probability is at most $1/4$. Their sum is approximately $0.44947114<1/2$. On the complementary event, division by $2\sqrt D$ gives $1/(8N\sqrt D)$. No independence between the scalar Gaussian projections is needed, and $D=1$ is allowed. Consequently the stated

\[
C=8(n-1)\sqrt{d-1}
\]

is valid.

The tent identity follows exactly from

\[
|\phi+\psi|+|\phi-\psi|=2\max(|\phi|,|\psi|).
\]

At the target input, the constructed tent is one. At another input, its negative term has magnitude at least $s_{ij}/\delta_i\ge1\ge|x_i\cdot x_j|$, so it is zero. Evenness causes no interpolation conflict under the nonparallel assumption.

For each three-atom tent, the explicit representation costs

\[
2\sqrt{1+\mu_i^2}+2\mu_i
\le2+4\mu_i
\le(2+4C)/\delta_i.
\]

Multiplying by the bounded labels and summing gives exactly

\[
K_{n,d}=n\bigl(2+32(n-1)\sqrt{d-1}\bigr),
\qquad Q_{\min}\le HK_{n,d}/\delta.
\]

The initial construction has up to (3n) atoms; Lemma 2.2 is what permits comparison with a minimum at width $n\le m$. That step is present and valid.

### 2.3. Beta integral, upper tail, and final limsup constant

**Places:** Section 3, Theorem 3.4 `upper`, (3.2)–(3.3), `main.tex:142–163`; Section 1, `main.tex:63`.

The angular normalizer is

\[
C_d^{-1}=B((d-1)/2,1/2).
\]

Writing $A=H^2K_{n,d}^2/(2d)$, one has $R\le A\delta^{-2}$. The maximum of the pairwise inverse powers is bounded by their sum, so the moment estimate is exactly

\[
\mathbb E R^r\le A^r\binom n2
\frac{B((d-1-2r)/2,1/2)}{B((d-1)/2,1/2)}.
\]

The integral is finite for $2r<d-1$. At $r=1$, the two gamma recurrences give $(d-2)/(d-3)$, not its reciprocal.

For one pair, the exact small-$u$ asymptotic is

\[
\mathbb P(\sin\Theta<u)
=2C_d\int_0^{\arcsin u}\sin^{d-2}\theta\,d\theta
\sim\frac{2C_d}{d-1}u^{d-1}.
\]

For $u\le1/2$, the paper's larger bound, obtained from $\arcsin u\le2u$, is valid. Substitution of $u=\sqrt{A/t}$, followed by the pair union bound, gives (3.3), including every power of two. Thus the introduction's limsup bound with $H=1$ is correct:

\[
C_U=\binom n2\frac{2C_d}{d-1}\,2^{d-1}
\left(\frac{K_{n,d}^2}{2d}\right)^{(d-1)/2}.
\]

It is conservative. The exact one-pair asymptotic would remove $2^{d-1}$ from a limsup bound, but the paper does not claim optimal constants. For fixed $d$, this stated upper constant grows as $n^{2d}$; its description as polynomial in $n$ is correct.

### 2.4. Spanning, uniformity, and the competitor

**Places:** Section 4, Lemmas 4.1 `span` and 4.2 `competitor`, `main.tex:177–190`.

Within the positive hemisphere, distinct unit (z_i) cannot be parallel. The proposed point of $z_i^\perp$ has strictly negative (e_1)-coordinate because $z_i\cdot e_2>0$. A point in that relatively open portion can avoid every other kink hyperplane. The derivative jump across $u\cdot z_i=0$ is then exactly $\chi_i$. This proves spanning. The argument also works in ambient dimension two and for arbitrarily many distinct extra inputs; it does not require $k\le d$.

At each fixed configuration, one can select $k$ directions with invertible evaluation matrix. Its determinant stays nonzero in a sufficiently small neighborhood, and its inverse is bounded on a smaller neighborhood. A finite cover of the compact separated set supplies a minimum positive margin $\eta$ and a maximum finite inverse bound $\Lambda_*$. The directions may vary from patch to patch; no single common matrix or measurable choice of correction directions is required for the cost comparison.

The choice

\[
\theta_1=\min(1,\eta,\kappa/2)
\]

is sufficient. It gives $a\ge3/4$, $b\le\eta/2$, and $b\le\kappa/4$. Hence the correction atoms vanish at both pair inputs, and $v\cdot z_i\le b-a\kappa<0$.

The vector $v=be_1-ae_2$ is unit. Its pair evaluations are zero and $s=2ab$. Therefore (F_0) has labels (1,-1), and its other evaluations are $\sigma(\xi_i)/a$. The correction right-hand side has supremum norm at most $H+2$, and

\[
\sum_j|c_j|\le\Lambda_*(H+2).
\]

The total number of units is $2+k=n$, and their balanced cost is at most

\[
\frac1a+\frac1{ab}+\Lambda_*(H+2)
\le\frac2{\sin\theta}+2+\Lambda_*(H+2).
\]

Both the leading coefficient (2) and the (O(1)) remainder are justified uniformly on the specified compact set.

### 2.5. Localization and risk limit

**Place:** Section 4, Proposition 4.3, (4.1)–(4.2), `main.tex:201–217`.

Monotonicity and the Lipschitz property give the printed bounds on (g(u)), because the pair difference is (2be_2) and $s=2ab$. Splitting according to the sign of $\varsigma q$ proves (4.1) with constant (4). Summing against $\theta|\gamma_j|$, and using the interpolated label difference (2), gives exactly

\[
\sum_j\theta|\gamma_j|\|u_j-\varsigma_j e_2\|^2
\le4(M_\theta-\theta/b).
\]

The sandwich

\[
2\le\theta/b\le M_\theta\le2\theta/s+K\theta
\]

therefore implies $M_\theta\to2$ and the claimed $O(\sqrt\theta)$ approximation by $G_\theta$. It uses only $T\le Q$; it does not assume an unproved equality of these costs for a selected representation.

One extra point on the positive side suffices to give

\[
A_\theta\le(\theta H+E_\theta)/\kappa\to0,
\qquad B_\theta=M_\theta-A_\theta\to2.
\]

This is why $k\ge1$, hence $n\ge3$, occurs in this argument. With the correction in item 1.1, uniform convergence on the unit ball follows. It implies convergence of squared risk: if the uniform error is $\epsilon_\theta\$, the difference of the squared integrals is bounded by $\epsilon_\theta(4+\epsilon_\theta)$. Finally,

\[
\mathbb E[2\sigma(-e_2\cdot X)]^2=4/(2d)=2/d.
\]

The negative-side statement follows from the transformation described in the paper and has the asserted sign. Negating all labels also covers the opposite ordering of the pair labels. These transformations carry minimizers to minimizers, without requiring that the chosen selection itself respect them.

### 2.6. The lower event and its constant

**Place:** Section 4, Theorem 4.5 `lower`, `main.tex:232–236`.

Conditional on the pair, each extra point independently has either sign of its (e_2)-coordinate with probability $1/2$. Thus the two disjoint same-side possibilities have probability

\[
2(1/2)^{n-2}=2^{3-n}.
\]

The positive-margin and distinct-point restrictions lose no limiting probability: for finitely many independent sphere points, no coordinate is zero and no two points coincide almost surely. Taking $\kappa=\rho=1/j\downarrow0$ exhausts that event. Within either hemisphere, distinctness also rules out antipodal coincidences. No additional label pattern, isolation of the close pair as the globally closest pair, or separation from an unspecified hyperplane is being imposed.

The pair labels are opposite with probability $1/2$, independently of all geometry. The remaining labels are unrestricted Rademacher labels and need no further probability factor. For fixed $\kappa,\rho,\zeta$, the uniform localization threshold applies to every configuration in the compact event. Integrating only the small-angle cap $\theta\approx0$, rather than both projective caps, gives

\[
\liminf_{t\to\infty}t^\alpha\mathbb P(R_n>t)
\ge\frac{P_{\kappa,\rho}C_d}{2(d-1)}(2/d-\zeta)^\alpha.
\]

First take the tail limit at fixed margins, then send $\zeta\downarrow0$ and $j\to\infty$. This order is legitimate even if the compact-set constants deteriorate with $j$. The resulting lower constant is exactly

\[
C_L=\frac{2^{2-n}C_d}{d-1}(2/d)^\alpha.
\]

In particular, the paper has neither omitted a label factor nor incorrectly doubled the small-angle cap. Integrating this positive lower tail against $r t^{r-1}$ gives divergence for $r\ge\alpha$, including logarithmic divergence at equality. The upper moment estimate gives the other direction for every positive $r<\alpha$.

### 2.7. Remark 4.4 and the theorem's quantifiers

**Places:** Remark `sides`, `main.tex:220–221`; Theorem 1.1 and its proof, `main.tex:56,239–240`.

Remark 4.4 is appropriately limited. If a bounded-excess-cost sequence existed with extra observations on both sides at fixed margin, the same localization estimates would force $M_\theta\to2$, while the two observations would force $A_\theta\to0$ and $B_\theta\to0$. This is a contradiction. A subsequence argument gives that the excess above $2/s$ tends to $+\infty$ for such configurations. The remark expressly declines to infer a risk conclusion, which is correct.

Both tail estimates are pointwise in every minimizer before probabilities are taken. The competitor fits into every fixed width $m\ge n$. Lemma 2.2 establishes equality with the optimum over all **finite** widths, exactly as defined in the setting. Nothing requires uniqueness, minimum-risk tie-breaking, rotational equivariance, or a width bound on the selected all-width minimizer. Thus the measurable-selection quantifier is justified.

The paper assumes a measurable selection rather than proving a selection theorem. This is not a missing statistical estimate. If desired, a short standard measurable-selection justification can be added: for fixed $m\ge n$, the feasible/optimal parameter graph is Borel with nonempty compact optimal sections. To see the value function is Borel, each bounded-cost feasibility sublevel is closed under convergent datasets by compactness of the parameter ball. A Borel selector can then be chosen on the nonparallel locus. Width $n$ supplies a selector for the all-finite-width problem as well. Null degenerate datasets can be defined arbitrarily.

## 3. Literature, citations, and novelty

### 3.1. The architecture and norm conventions must be distinguished

**Places:** Abstract, `main.tex:34`; Section 1, `main.tex:39–41`; Section 5, `main.tex:246`; AI declaration, `main.tex:257`.

The introduction moves too quickly from minimum Euclidean parameter norm to the norms in Savarese–Evron–Soudry–Srebro and Ongie–Willett–Soudry–Srebro. Those works concern function-space descriptions with translated ReLU ridges and particular treatments of biases and affine components. Here the allowed ridges are exclusively $\sigma(u\cdot x)$, with neither biases nor an affine skip term. Identifying all these optimization problems without qualifications is unjustified. The paper's self-contained atomic argument is valid and does not need that identification.

A concrete reason the convention matters: for the model in this paper, a global linear function $f(x)=v\cdot x$ has minimum atomic cost $2\|v\|$. The identity $f(x)-f(-x)=\sum_j\gamma_j u_j\cdot x$ gives the lower bound $\sum_j|\gamma_j|\ge2\|v\|$, and two opposite ReLUs attain it. A Radon seminorm with a free affine component instead annihilates this function. Thus any citation to an affine-quotient seminorm must not be treated as literal equality with the present cost. State which norm variant is meant, including bias penalties and affine terms.

The same issue affects the phrase “such interpolants” in the abstract's reference to Joshi–Vardi–Srebro. A bias-free shallow network on a scalar input is just $A\sigma(x)+B\sigma(-x)$; it cannot generally interpolate arbitrary noisy data on a positive interval. JVS's univariate interpolation result necessarily concerns a different architecture. The comparison is useful, but say so explicitly and state its input/noise assumptions.

### 3.2. Assessment of the six cited research papers

The following is an assessment from established knowledge and the supplied bibliography, **not a claim that I opened the originals during this offline review**.

| Reference | Relevant scope and what it does or does not support |
| --- | --- |
| Joshi–Vardi–Srebro, ICLR 2024, arXiv:2307.15396 | The univariate, loss-dependent distinction between tempered behavior below $p=2$ and catastrophic behavior at/above $p=2$ is the relevant predecessor. Qualify the architecture and distribution/noise assumptions; I have not reverified the exact finite-$n$, infinite-expectation statement against its theorem text. It is not, simply by citation, the multivariate spherical tail theorem here. |
| Ongie–Willett–Soudry–Srebro, ICLR 2020, arXiv:1910.01635 | A multivariate function-space/representation-cost characterization involving the Radon transform. This is substantial prior multivariate minimum-norm theory, so the introduction should not suggest that multivariate theory itself was absent. It does not, to my knowledge, establish the displayed fixed-$n$ stochastic risk tail. Norm conventions require the qualification above. |
| Savarese–Evron–Soudry–Srebro, COLT 2019, arXiv:1902.05040 | Relevant univariate function-space and representation-cost theory, not a proof of the current multivariate risk distribution. Again, distinguish architecture and affine-term conventions. |
| Mallinar et al., NeurIPS 2022, arXiv:2207.06569 | The taxonomy is relevant to sample-size asymptotics. The paper correctly says its fixed-$n$ result does not settle that asymptotic classification. Infinite expectation at a fixed $n$ is not by itself catastrophic behavior in probability as $n\to\infty$. |
| Kornowski–Yehudai–Shamir, NeurIPS 2023, arXiv:2305.15141 | The cited dimension-dependent classification results are a different setting from this squared-regression-risk theorem. The introduction's explicit “for classification” qualification is appropriate. They should not be represented as determining the current fixed-$n$ tail. |
| Karhadkar–Sietsema–Needell–Montúfar, arXiv:2602.00825 | I cannot independently verify this 2026 citation, its bibliographic details, or the exact asserted theorem without its text. Treat it as unverified here, not as a demonstrated false citation. A result about near-minimal Sobolev interpolants does not automatically apply to this ReLU atomic norm: a suitable norm comparison and compatible optimality assumptions would be needed. The manuscript only uses it for context/speculation, so the proof does not depend on it. |

The supplied author names, titles, and venue/year combinations for the five older references are consistent with the works I know. That is weaker than checking the exact quoted claims in their primary texts. The author should provide precise theorem references for the JVS summary and the KSNM summary before publication. I have not verified the software repositories or the Math Brain paper; they are not premises of the mathematical proof.

### 3.3. Novelty should be stated narrowly

**Place:** Section 1, last sentence of `main.tex:41`, and novelty claims at `main.tex:43,257`.

“For the minimum-norm ReLU interpolant of regression data in several variables the size of the risk has not ... been determined” is too broad as a priority claim. It should specify fixed ambient dimension, fixed sample size, bias-free homogeneous architecture, spherical random design, the precise parameter norm, and the distributional tail rather than generic risk information. Existing multivariate norm characterizations, generalization bounds, and results for other optimizers or high-dimensional regimes should not be swept into an absence claim.

I do not know a previous theorem giving this exact fixed-$n$, two-sided $t^{-(d-1)/2}$ tail uniformly over all minimum-$Q$ selections in the stated model. None of the older results summarized above supplies it. However, absence of a known result is not a verified exhaustive novelty search, especially through November 2026 under the offline restriction. The KSNM paper in particular has not been source-checked here.

A defensible formulation would be: “We are not aware of a two-sided fixed-sample-size risk-tail bound, uniform over minimum-weight-norm interpolants, for this bias-free spherical regression model.” The claimed contributions should be the uniform one-sided collision localization, the projective-gap interpolation-cost bound, and their combination into the tail and moment thresholds. The atomic reformulation, finite-support reduction, and scalar ReLU finite-difference identity are not new general principles.

### 3.4. Additional relevant background citations

The convex atomic viewpoint and support reduction have a broader history than the two ReLU-specific norm papers. Useful background additions are Francis Bach, *Breaking the Curse of Dimensionality with Convex Neural Networks* (2017), and Rahul Parhi and Robert D. Nowak, *Banach Space Representer Theorems for Neural Networks and Ridge Splines* (2021). Rosset, Swirszcz, Srebro, and Zhu's *$\ell_1$ Regularization in Infinite Dimensional Feature Spaces* (2007) is another relevant precursor to finite-support arguments. These are background citations to check and add where appropriate, not claims that any of them contains Theorem 1.1. I have not reverified their bibliographic metadata or theorem details offline.

## 4. Minor corrections and exposition

1. **Representation-dependent notation:** Section 2, (2.1), `main.tex:83`, and the corresponding notation-table row. As defined, $T(f)=\sum|\gamma_j|$ depends on the representation, not just on $f$: adding two canceling atoms changes that sum. Write $T(\gamma,u)$, call it the cost of the displayed representation, or separately define a function-level infimum. The proof only needs representation costs, so this is readily repaired.

2. **Inner/outer weights:** Proposition 3.3, `main.tex:137`. The vectors $\mu_i z_i\pm x_i$ are the **inner** weight vectors, not the outer weight vectors. The third inner vector has norm $\mu_i$; the two other ones have norm $\sqrt{1+\mu_i^2}$. The cost calculation itself is correct.

3. **Wrong theorem numbers in the check script:** `check_tents.py:5,7,44`. Proposition `tents` is 3.3, not 3.4, and Theorem `upper` is 3.4, not 3.5. Update the docstring/comments accordingly.

4. **Gap exponent wording:** Section 1, `main.tex:43`, last sentence. The small-distance probability exponent is $d-1$; the inverse-square distance has upper-tail exponent $(d-1)/2$. Say “the exponent of the inverse square of the smallest projective distance.” Section 5 already uses the correct formulation.

5. **Slope versus spike:** Section 1, `main.tex:41`. A nearby opposite-label pair forces a slope of reciprocal-distance size. It does not by itself force a spike of that height *between those two points*. State the geometric extension mechanism and its other constraints rather than describing this as a consequence of the two labels alone. In this paper the rigorously established large-amplitude limit is on an entire half-sphere under the one-sided event.

6. **Weight-decay limit:** Section 1, `main.tex:39`. Qualify “is the limit of weight decay” as a statement about accumulation points of **global minimizers** of a regularized interpolation-compatible objective as the penalty vanishes. The manuscript neither proves convergence of every regularization path nor identifies a gradient-descent limit.

7. **Abstract assumptions:** `main.tex:34`. Specify Rademacher labels when describing the two-sided tail theorem. “Noisy labels” alone is broader than the proved lower-bound model, and arbitrary unbounded label noise could change the tail.

8. **What the constant-probability event means:** Section 5, `main.tex:244`. “On an event of probability $2^{2-n}$, exactly that bad” should explicitly mean the opposite-label/same-side event, **as the pair angle tends to zero**. That event is not a fixed-positive-probability event on which the risk exceeds every large threshold. The formal lower-tail proof handles this correctly.

## 5. Numerical checks and audit limits

The supplied `paper/check_tents.py` reports `ALL PASS`. It checks the advertised elementary identities and constructions, but it does not test the localization proof, minimizer selection, or novelty. Its competitor cases also restrict the number of extra points, and so do not exercise the spanning claim for $k>d$. NumPy emitted matrix-multiplication floating-point warnings on this host during that supplied script; the reported numerical checks nevertheless passed. The verdict rests on the derivations above.

I added `audit_checks.py` outside `paper`. It passes independent checks of the tent identity in exact rational arithmetic, the Gaussian probability budget, the beta integrals and cap constants, (4.1), the repaired maximum estimate, the probability factors, and a restricted-cone correction construction with $d=2,k=7>d$. For that explicit competitor, the computed $\theta^2R$ values at $\theta=10^{-2},10^{-3},10^{-4}$ are approximately 0.958991, 0.995841, and 0.999584, approaching $2/d=1$. These are construction checks, not numerical certification that a solver found a continuum minimum.

An offline TeX build was attempted with `tectonic --only-cached`, directing outputs to a temporary directory. It stopped because this machine's cache lacks `longtable.sty`. I did not download it. This is an environment limitation, not an identified LaTeX source error. Numbered references in this report were obtained from the source's theorem/equation counters.

Source SHA-256 hashes reviewed:

```text
main.tex        a343c762d8d7666e41d8d0f9c95a95c60b86b91ac36bff954cfeb3cbd3d4fce2
notation.tex    641f436dfd52eeb6c08e72b6ead857b5b1be4788bac941266ec15df86376e5b7
check_tents.py  34f33c25fa509c118e26002d90bfe5d8e6097c3a7c8a09c482c51d3c393011c2
```

Task: “Write REPORT.md in this folder” — received 15 November 2026, 21:58, Asia/Tbilisi.
