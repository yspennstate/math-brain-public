# Audit 2: insertion, multiplicities, and supported residuals

**Outcome: finite arguments passed rederivation and exact stress tests.**

This pass rederived the finite comparisons without relying on numerical agreement alone. The sharper insertion lemma permits total mass $m\ge2k$; its images contain exactly one size-$k$ box by construction, not because the total excludes two such boxes.

## Occupation-count calculation

For a positive-weight background with counts $a_j$, insert the giant and a fixed list of residual pieces into empty coordinates. With $Q=1+\sum_j r_j$, the image satisfies $b_0=a_0-Q$, $b_k=1$, and $b_j=a_j+r_j$ for $0<j<k$. This map on count vectors is injective. Its permutation-weight ratio, after normalization $w_0=1$, is

$$
w_k W_r\frac{(a_0)_{\underline Q}}
 {\prod_j(a_j+r_j)_{\underline{r_j}}}.
$$

Every background has $a_0\ge n-t$, while every image has $b_j\le\min(n,\lfloor m/j\rfloor)$. Monotonicity of the nonnegative falling factorial in its first integer argument yields the sharp bound in Lemma 3.1. The denominator is positive: the fixed residual list and $Q\le n$ guarantee that each multiplicity fits its occupancy upper bound.

The coarse bound was checked separately. If $t+Q\le n/2$, every numerator factor is at least $n/2$. Each factor corresponding to a large piece is at most $m/K$, and each terminal-piece factor is at most $n$. This produces $n2^{-(C+1)}(nK/(2m))^R$. The condition $nK\ge2m$ makes the last factor at least one. A size may occur in both roles; assigning its factorial factors to the two roles in a fixed order preserves both upper bounds.

An independent counting *method*, not an independent reviewer, was also used: enumerate ordered choices of empty labelled coordinates. A target has one giant location and at most the displayed product of falling-factorial residual choices. Deleting those choices may produce an invalid background, which only lowers the inverse multiplicity and cannot invalidate the upper bound.

## Supported residual construction

A finite subset of the positive support has the same gcd as the full support. After dividing by this gcd, the nonnegative semigroup of that finite subset contains all sufficiently large integers. The finite terminal representations therefore exist without assuming $w_1>0$.

At a greedy stage, $s_i\le a^i\le x/2$ and $h_*\le a^i$. Hence $q=\lfloor(x-h_*)/s_i\rfloor\ge1$. The new residual lies in $[h_*,h_*+s_i)$, so it is strictly below $2a^i$; the geometric index strictly decreases. The terminal set is finite, all terminal weights are positive, and its cost bound is fixed before the large-scale limit. The manuscript makes the nonnegative integer domain, empty-product convention, and zero-order falling factorial explicit.

## Executed checks

The new standalone stress checker tested 18,000 exact count-vector comparisons, including 14,862 cases with $m\ge2k$. Of these, 13,240 met the coarse-bound conditions, including 1,573 with the same residual size in both roles. Equality occurred in the sharp-bound comparison, so the checks do include boundary cases rather than only generous slack.

Three fully labelled examples enumerated 2,100, 11,760, and 45,360 insertion records. Their inverse multiplicities and image counts obey the sharp double-counting bound. The earlier 12 occupation-count examples and 391 supported greedy energy checks were also rerun. All final assertions passed with integer or rational arithmetic. These tests support the finite derivations; they do not establish the asymptotic theorem by computation.
