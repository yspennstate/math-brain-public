# Independent analytic review and verification record

Date: 2026-09-30. Full FEI remains open.

## Written report

The coordinating researcher read the complete written REPORT.md and independently checked:

- The conditional DTC decrement identity and the entropy-priced fixed-coordinate-set selection
- Zero-entropy handling and the averaged terminal total-correlation bound
- The exact collective projection identities from partial Walsh inversion of f²=1
- The conditional sufficiency calculation, without asserting the missing payment theorem
- The exact Boolean locking transform, its product Fourier law, physical-child parity law, and DTC/influence identities
- The clipped-potential counterexample criterion and its explicit limitations

One scope correction was requested: the optional all-block estimate requires ratio maximality over all physical descendants, not merely a bound on immediate children. Section 3 now states that stronger hypothesis from the outset and notes the distinction. With this clarification, the reviewer judged the written analytic statements correct.

This is independent mathematical review, not proof-assistant certification and not a priority determination.

## Componentwise countertheorem

The coordinating researcher separately checked the mathematical construction in COMPONENT_OBSTRUCTION.md: the union bound with `t²=2(n+2)ln2`, dyadic scaling via minimal K, the norm interval, and exact Boolean-mean realization over K+1 bits. The asymptotic entropy/influence separation and the componentwise-only scope were retained.

The signs are established by a finite probabilistic existence proof for arbitrary M. The package supplies an actual deterministic seeded realization only for M=2; it does not claim explicit sign lists for every M. Other projection components can carry additional entropy and influence, so this is not a counterexample to the collective target or to FEI.

## Executed checks

The author executed the final check.py after the scope correction and code cleanup. It passed:

- 728 direct-Walsh locking cases
- 2,184 fixed-set wringing cases
- 56,766 pointwise all-shift projection checks
- Six exact clipped-potential examples built from tensor powers of a two-bit bent seed

Maximum identity error: 1.3766765505351941e-14. No positive bound violation was recorded.

The author also executed check_component.py. Its M=2 realization has n=16, K=21, exact squared Fourier numerator sum Z=152587890625, squared norm 0.03469446951953614 and sup norm 0.789374828338623. The bounded dyadic truth values and the integer counts defining the Boolean conditional mean were checked directly. The remaining table evaluates the analytic lower bound, not truth tables in enormous dimensions.

The independent reviewer did not rerun the checker bytes. Numeric regression, exact integer checks, and all-dimensional analytic arguments are distinct evidence levels.
