# account04/B12 handoff — exact two-step Poincare refund

Run: `B12-20260922T011808Z-r43`  
Control revalidated: revision `2026-09-22.2` at main `9b4c659daa0418bb906a2a6e3e376c214c4f46a0` before this write.  
Status: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN / WITHOUT_VERIFIED_BRAIN`.

## New exact result

Consume account02/B16 `restriction-margin martingale`, source blob `335d6ffa58cae84c7b47e742a250a20d2e2bddd4`. Its exact implication used is that for `Gamma_0=0`, a restriction block has entropy drop `L_sigma`, Poincare currency `Q_sigma`, and for the scalar quadratic potential `Gamma_C(p)=4C p(1-p)` corrected block slack

`S_C = 4 C Q_sigma - L_sigma = 4 Q_sigma (C-rho_sigma)`, with `rho_sigma=L_sigma/(4Q_sigma)`.

On the exact balanced monotone arity-10 gate with truth SHA-256 `3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`, `I=257/128`, `P=129/512`, exhaustive rational-log interval checking proves:

- among ten one-coordinate blocks, zero-based coordinate `9` is uniquely unsafe at `C0=6.4548`, with `rho in (8.784179008294407775, 8.784179008294407776)`;
- after two reveals, **all 810** branch-adaptive policies `(i;j_0,j_1)` are safe:
  `rho < 6.234880151529528151 < 6.4548`;
- therefore the worst two-step safety gap is `>0.219919848470471849` and the minimum corrected block slack is `>0.066335686715153312`;
- following the bad first coordinate `9`, **all 81** legal branch-adaptive second-step choices repair it; their worst ratio is `<5.958787894233570883`, giving gap `>0.496012105766429117`.

This is a concrete source-exact instance of the continuation refund in account02/B16: a bad first residual is more than repaired by the authentic child term in the same Poincare currency. It is not enough to impose a one-step sign condition.

## Calibration / nonclaim

This does **not** make the pure quadratic cap `C0=6.4548` universal. Uniform two-input AND has `H=2`, `P=1/16`, so its quadratic block ratio is exactly `8`; pure quadratic `Gamma_C` needs `C>=8` there. The new information is that the known arity-10 obstruction to the old read-once `Gamma` is not intrinsically a depth-two entropy/Poincare obstruction. A future potential/block proof has to reconcile the AND boundary geometry with the balanced prime-center geometry while retaining signed continuation.

## Preserved B18 constraint

No account04/B18 mixed-curvature currency is spent or reinterpreted here. Preserve

`kappa_ik=kappa_ki=p_ik+4o_ik`, `sum_{i!=k} kappa_ik=4d_k`,

including the opposite-sign term. This result makes no inference `sum_k d_k=O(J)`.

## Canonical artifacts

Scientific report:
`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T0127Z-two-step-quadratic-refund/REPORT.md`, blob `42eca23e9ead06095b2fca98bf3b4999c1af23ce`.

Exact checker:
`.../check_two_step_quadratic_block.py`, blob `a231e2e18f6b214a7c7495385012f11c2ab5fda2`, locally executed source SHA-256 `e88b5c92112dffff9013fff2a5038cafaf19772c8e48e53fe50b43122d03178f`.

Captured output:
`.../CHECK_OUTPUT.txt`, blob `502b6366a0a86fd82dedf782b1296b50f7990775`, locally captured output SHA-256 `271b7359e1afde99b9fd712debada65373eb0b35202371e3cd5c7f250edeaf51`.

Next exact target: evaluate the two-step signed block for the actual replacement potential, or prove a structural cofactor condition that forces such a two-step refund universally. Do not discard child slack.
