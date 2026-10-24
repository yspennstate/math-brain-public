# PROB20-14 — zero-excess Palm artifact execution certificate

**Artifact:** `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/zero_excess_palm_check.py`  
**Artifact commit:** `2bca1983a5ace3cc04bff898cfe1011857d25a8b`  
**Artifact blob (SHA-specific readback):** `277f6d628c17a19249d761785ee3a24b0bfaf731`

The script was executed after SHA-specific readback. It uses exact `fractions.Fraction` arithmetic for the algebraic assertions and floating-point conversion only for the displayed renewal-localization ratios.

Test law:

```text
P(xi=0)=11/20
P(xi=1)=1/5
P(xi=2)=3/20
P(xi=5)=1/10
E xi = 1
```

Palm residual test: `n=18`, selected degree `d=5`, residual sample size `N=17`, residual target `N-d=12`.

Exact output / assertions:

```text
a_n = 1014718218066649829403/16384000000000000000000
shifted atom = 87526183002115186461/1638400000000000000000
R_{n,d} = 914589164076438730/1060311617624503479
R_{n,d} ~= 0.8625663897991255
Palm zero/excess states = 10
E[(xi-1)_+] = pi_0 = 11/20
all exact assertions passed
```

The exact assertions verify:

1. the dynamic-programming Palm residual mass sums to the shifted local atom;
2. every residual Palm state satisfies the deterministic identity
   `N0 = d + sum_i (xi_i-1)_+`;
3. `E[(xi-1)_+] = pi_0` for the critical law;
4. on the tested Palm good states and central renewal lengths `|s-d| <= d/4`, the falling-factorial multiplier used in Theorem 5.1 is at least one.

Renewal-localization numerical certificate (not proof evidence):

```text
(d, truncated U(d), central |s-d|<=d/4 mass, fraction)
(10, 1.0063543410296252, 0.44400889800744336, 0.4412053288836289)
(20, 1.0001785281055235, 0.5724893185133585, 0.5723871313231774)
(40, 0.999999937845995, 0.719646188267763, 0.7196462329966586)
(80, 0.9999999999996207, 0.8643839054887368, 0.8643839054890645)
```

These values are consistent with the proved renewal-localization lemma, but the mathematical proof in the run report does not depend on these numerics.

**Execution status:** PASSED.  
**Interpretation:** reproducibility/consistency certificate only; not independent verification of the universal theorem.
