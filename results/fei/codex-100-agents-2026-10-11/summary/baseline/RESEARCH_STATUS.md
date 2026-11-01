# Research status and proof boundaries

11 October 2026

## What is established in this manuscript

The threshold theorem covers every deterministic linear threshold function under the uniform input measure. No condition is imposed on weight size, arithmetic structure, margin, or threshold. The stronger class of regular Boolean functions is defined by a total desirability order.

The revised exact coefficient is

$$C_{\rm reg}=\log_2(4+e)+2\log_2(e\pi)<8.937.$$

Its proof uses three explicit estimates:

$$H(|\mathcal S|)\le\log_2(4+e)I(f),$$

$$\mathbb E_\nu\ln\frac r{|T\cap U|+1}\le\sum_{q=1}^{r-1}\frac{2^{-q}\binom q{\lfloor q/2\rfloor}}q\le1+\ln2,$$

and the Euler-product reference

$$Q_k(S)=\frac{(2k+1)!}{\pi^{2k}}\prod_{i\in S}i^{-2},\qquad |S|=k.$$

For multiple coordinate orders a separate Laplace-transform estimate is used. The single-order value $1+\ln2$ is **not** substituted into the multiple-order proof. The exponential tail used in the bounded-overlap theorem remains the original independently valid tail.

The product-measure theorem concerns symmetric thresholds. Arbitrary weighted thresholds at biased internal gates still require the hypotheses stated in the paper.

## The completed overlap continuation

The queue construction admits a reference probability for every successful finite witness. For each Fourier set, the revised statement minimizes the cost over assignments of its coordinates to gates and over valid directed forests. It retains the number of used gates, their overlap congestion, and their root probabilities.

For addressing on $m$ controls, a whole Fourier set uses one gate. The refined queue estimate gives $H(f)<10I(f)$ uniformly in $m$. The direct selector calculation gives the exact stronger statement

$$H(f)=2m=4[I(f)-1],\qquad I(f)=1+m/2.$$

The general selector theorem requires balanced leaves with disjoint nonempty **Fourier supports**. The underlying leaf variable sets may overlap. Removing Fourier-support separation creates interference between coefficient contributions and is not covered by the theorem.

## What remains unresolved

No proof of the unrestricted Fourier entropy–influence conjecture is supplied. For the queue route, the missing estimate is a universal bound on the expected whole-witness cost, including normalization, rank, and sparse-root contributions, in terms of one influence budget.

The limitation can be stated exactly. For balanced arbitrary $g$,

$$M_g=\frac{1+g}{2}y_1+\frac{1-g}{2}y_2$$

satisfies

$$H(M_g)=2+\tfrac12H(g),\qquad I(M_g)=1+\tfrac12I(g).$$

Balancing tensor powers removes the additive terms. Hence a universal FEI bound for this two-cell selector class has exactly the same optimal constant as full FEI.

Likewise, sparsely activating balanced tensor powers produces functions with arbitrarily small influence and arbitrarily small probability of the minority output while preserving any original entropy-to-influence ratio in the limit. The paper credits earlier low-influence reductions and proves the exact identities used here.

The older parity-support and sparsely activated bent-function examples remain consistent with this outcome: they obstruct particular local entropy payments without refuting FEI. They do not become proofs of a universal bound by changing the accounting terminology.

## Review and computational scope

The revised rank argument, the original bounded-overlap argument, the biased symmetric-threshold proof, and the exact composition identities were analytically reviewed. The new queue, selector, and sparse-activation identities were separately checked. The paper's AI declaration describes the assistance; these reviews are not external peer review or proof-assistant certification.

The scripts retain exact integer or rational checks where the quantities are algebraic. Logarithmic entropy identities are checked numerically with stated tolerances. Their complete finite coverage and outputs are recorded in the accompanying JSON files. No enumeration is used to infer an all-dimensional theorem.

The principal qualitative contribution remains the all-threshold theorem and the structured extensions. The improved constant and joint-description results strengthen that contribution. Publication priority for the individual auxiliary identities is not asserted.

