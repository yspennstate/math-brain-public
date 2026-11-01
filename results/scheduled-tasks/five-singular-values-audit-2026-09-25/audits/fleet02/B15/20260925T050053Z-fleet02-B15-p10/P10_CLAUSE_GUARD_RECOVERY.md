# P10 clause-supplement recovery

Source: short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8. Pass P10. The larger JSONL writes for clause rows 83-114 were blocked by the platform write guard; the clauses were nevertheless audited directly. This compact record preserves their coverage.

- L218 c1-c4, PDF p5 — PASS. Orthogonal completion, density formula, and d=n/d<n split checked; deterministic rotation is only a change of variables.
- L222 c1-c6, PDF p5 — PASS. beta identities, zero-beta factors, frame normalization, BL application, f^(1/beta)<=f, and integral scaling checked. The phrase "factors ... are at most one" is a value bound (<=1), not a cardinality claim; clearer wording would be "bounded by 1".
- L228 c1-c3, PDF p5 — PASS. SVD factorization, Jacobian det(Sigma)=sqrt(det(BB^T)), and d=1 specialization checked.
- L240 c1-c7, PDF p5 — PASS. Difference-density cap, m=floor(p/2), exponent comparison, characteristic-function identification, L2 integrability, continuous inversion at zero, and projection constant checked.
- L245 c1-c3, PDF p6 — PASS. Section hypotheses, fixed partition, and crossing-volume definitions checked.
- L249 c1-c2, PDF p6 — PASS. Theta_l(H) and omega definitions checked including H=empty.
- L261 c1-c2, PDF p6 — PASS. Entropy-lemma probability/marginal definitions and zero convention checked.
- L268 c1-c3, PDF p6 — PASS. Marginal rewrite, Jensen/concavity of log, multinomial comparison and sum alpha_i=m checked.
- L283 c1-c2, PDF p6 — PASS. Independent-row implication from positive Gram minor, projection decomposition, and Gram-factorization dependency checked.

No defect or independence leak was found in these recovered clauses.
