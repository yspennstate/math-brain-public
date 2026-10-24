# PROB10-06 idea refinement before successful checker — moderate-p rectangle

The first planned route, retaining the upper `h_2/c_2` conditional escape weights in a monotone order polytope, was worked out algebraically after the earlier idea note. It is valid, but on the lower-mixture regime it collapses numerically to the same reverse-Chebyshev upper score already inherited, and its all-mixture gain is only microscopic. I therefore do not spend the run manufacturing a large certificate for that nearly unchanged quantity.

A more useful complementary route is to keep the mixture parameter `p` instead of optimizing it away. The predecessor already proves all `{2,3}` mixtures through parent bias `lambda=1.85527`, and older R02 work proves the lower tail `p<=31/200` through `lambda=1.9`. There is an uncovered moderate-mixture strip immediately above that tail. The target of the exact checker is:

`31/200 <= p <= 1/4`, `1.85527 <= lambda <= 1.87`.

Use the predecessor's quantitative branch-ratio bound

`c_3/c_2 <= (4-lambda)/(2(3-lambda))`

and hence

`theta <= p T/(1-p+pT)` with `T=(4-L)/(2(3-L))` frozen at the candidate endpoint `L=1.87`. On `p<=1/4`, this tilted weight stays strictly left of the maximizer of `g(theta)=theta(1-theta)/(2+theta)`, so `g(theta)` is controlled by the explicit rational endpoint `g(theta_U(p))`; no global irrational majorant is needed. For `h_2/c_2`, use the proved reverse-Chebyshev polynomial upper score. For `h_3/c_3`, retain the 64-vertex monotone lower-score polytope. This leaves only 64 exact one-variable product inequalities on `p in [31/200,1/4]`, plus the lambda-envelope monotonicity checks.

If those pass with a strict cap, stitching with the inherited all-mixture theorem yields a genuine new source-valid region: every `{2,3}` mixture with `p<=1/4` is strictly decreasing at least through `lambda=1.87` (and the smaller tail `p<=31/200` remains known through `1.9`). This is restricted-family progress only; the full source remains OPEN.

The third approach remains the expectation-level derivative contraction through `lambda=2`. I will record an exact obstruction from the currently available inverse-escape moment alone if it cannot produce a coefficient below one.