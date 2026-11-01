# Hypothesis clarification for QFORM-INFINITESIMAL-BANK-NOESCAPE-v1

The phrase “coefficient normalization and infinitesimality (2.2)” in the main report is shorthand and should be read with the full Section 2 hypothesis, not as a claim that (2.2) alone implies infinitesimality.

For each row there must exist deterministic termwise centers `c_{m,k}` such that the independent array

`Z_{m,k}=a_{m,k}X_{m,k}-c_{m,k}`

is infinitesimal in the standard triangular-array sense:

`max_k P(|Z_{m,k}|>eps) -> 0` for every `eps>0`,

and the centered row sums converge in distribution (the row-level centering may absorb `sum_k c_{m,k}`). Together with `sum_k a_{m,k}^2=1` and `max_k |a_{m,k}|->0`, these are the hypotheses used to invoke the Levy triangular-array theorem and its canonical small-jump covariance formula.

No assertion is made that diffuseness of the deterministic coefficients by itself forces probabilistic infinitesimality for arbitrary cap-one laws. Non-infinitesimal/mixed-leverage arrays remain an explicit escape mechanism in Section 5.
