# Audit 4: path quantifiers, tree roots, and sampling sharpness

**Outcome: the stated consequences passed review; their scope remains explicit.**

## Full and sampled paths

For a prescribed full path, the chosen scale $k$ determines a prospective index near $(1+4\delta)k/\lambda$. The assumption $m_n/n\to\lambda$ alone puts the resulting pair into the mass window. No hitting argument, bounded upward increment, or monotonicity of the path is needed.

For a sampled set with successive-index ratio tending to one, its first point above this prospective index is asymptotically at the same location. This justifies the dense-sampling extension. It does not apply to every arbitrary subsequence. A further thinning can make selected indices strictly increasing, because the prospective indices tend to infinity.

The whole-interval consequence is also valid. The path error $m_n-\lambda n=o(n)$ is uniformly small over every sufficiently remote interval whose endpoints are fixed multiples of $k$. The narrower interval in equation (31) leaves positive margin inside the mass slab. Its cardinality is asymptotic to $\delta k/\lambda$. The paper does not claim a density of such intervals among all integers or a law-uniform convergence rate.

Expectation convergence follows from the deterministic bound $0\le Y_{(1)}/m_n\le1$, and the second-largest-box bound follows from $Y_{(2)}\le m_n-Y_{(1)}$. These arguments do not need an additional uniform-integrability hypothesis.

## Allocation-to-tree transfer and the root

For total degree $n-1$, the cyclic lemma identifies the allocation degree-count law with the simply generated tree degree-count law. Rotation preserves the product weight and the maximum. A nontrivial period cannot occur for the full degree sequence because the sum of degree-minus-one increments is $-1$.

Conditioned on the degree counts $A_j$, the number of plane trees is $(n-1)!/\prod_jA_j!$. Removing a root of degree $j$ leaves an ordered forest of $j$ trees, giving $j(n-2)!/((A_j-1)!\prod_{i\ne j}A_i!)$ possibilities. Their ratio is $jA_j/(n-1)$. This is the known size-biased root identity, not a new identity. The final paper explicitly takes $n\ge2$ before using its denominator and cites the correct preprint locator.

On the event that the maximum degree exceeds $(n-1)/2$, it is unique. Its conditional probability of occurring at the root is $D/(n-1)$. The final manuscript includes the error bound

$$
\Pr(D\le(n-1)/2)+\mathbb E[1-D/(n-1)],
$$

which tends to zero on the condensation subsequence. The number of vertices at depth at least two is exactly $n-1-d^+(o)$, giving the final geometric consequence. The independent calculation method in the new checker enumerated 23,713 plane trees of sizes 2 through 11 and verified 422 root identities across 138 degree-count classes. This is not a new independent reviewer.

## Necessity of the sampling criterion

When infinitely many sampled gaps have ratio at least $\theta>1$, the constructed support consists of zero, one, and their left endpoints. The weights at large supported values are $e^{k^2}$, so they form one fixed zero-radius sequence. The path $m_n=n-1$ is admissible via zeros and ones.

A supported left endpoint $k$ is unavailable at $n=k$ because the total is $n-1$. At any later sampled index it satisfies $n\ge\theta k$. Hence every configuration has maximum at most $\max(1,n/\theta)$, ruling out near-total condensation on that sampled set. With unbounded gap ratios, the same argument separates a finite initial support from later points and forces a deterministic vanishing maximum fraction.

This disproves universality when the sampling condition fails; it does not say that every individual law fails. The deterministic powers-of-two, factorial, and irregular-gap tests were rerun, including equality at the gap threshold. The published source's sparse-support examples remain consistent with both directions.
