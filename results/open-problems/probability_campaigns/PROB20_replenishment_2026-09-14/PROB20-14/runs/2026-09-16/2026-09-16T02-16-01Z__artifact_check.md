# PROB20-14 — factorial replication artifact execution certificate

**Status:** consistency check only; not proof evidence for the universal infinite-variance theorem.

Artifact:
`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/factorial_replication_shell_check.py`

Artifact creation commit: `e48781ae374683577abedb0e4bad53e5ac741055`  
Artifact SHA-specific readback blob: `85ddc130f4e9a87c79e166a235d49d8ad5418579`

The checker was executed after the mathematical Markdown report had already been committed. It uses exact `Fraction` arithmetic for the finite combinatorial identities and inequalities, and floating-point arithmetic only for a grid lower bound on the Legendre transform in the optional Chernoff consistency check.

Test law:
\[
\Pr(\xi=0)=11/20,\quad
\Pr(\xi=1)=1/5,\quad
\Pr(\xi=2)=3/20,\quad
\Pr(\xi=5)=1/10,
\]
which has exact mean one. The test uses `n=18`, `A={2,5}`, `d=2`, and factorial order `m=2`.

Execution output:

```text
critical_mean=1
n=18 A=[2, 5] m=2 d=2
central_atom=0.0619334849894195
conditional_mu_A=4.3189399196857
factorial_moment=15.3636260781124
jensen_lower=11.0153621904833
replication_upper=112.895999501043
singleton_factorial_identity=7.03963988287201
H_grid=0.00826236729788535 at t=0.092
residual_lower_tail=0.365597003422922
chernoff_grid_upper=0.876167604712737
replication_log_lhs=-0.734214594154641
replication_log_rhs_grid=1.32474820790421
Lambda(t)/t^q samples:
  t=0.2: 0.433275307237033
  t=0.1: 0.333488081780072
  t=0.05: 0.246217877593968
  t=0.025: 0.177921764036801
ALL_ASSERTIONS_PASSED
```

The exact assertions verify:

1. criticality of the test law;
2. the Jensen/falling-factorial lower bound;
3. the high-degree-set factorial upper bound by an unconditioned residual lower-tail probability;
4. the exact singleton factorial-moment identity when the selected degrees are deterministic;
5. a numerical Chernoff upper bound using a grid lower bound on the exact Legendre supremum; and
6. the corresponding numerical version of the replication log inequality.

The decreasing sampled values of `Lambda(t)/t^q` are only a sanity check and are not used as proof of the asymptotic lemma, which is proved analytically in the report.
