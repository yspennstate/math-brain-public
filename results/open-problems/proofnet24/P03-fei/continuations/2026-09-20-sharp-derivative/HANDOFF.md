# FEI handoff: sharp one-step coefficient, full accumulation still missing

20 September 2026. Full FEI is unproved in this continuation.

Read REPORT.md and WORKLOG.md. The exact checker is `verify_continuation.py`; `verification.json` is its actual successful output. Exploratory scripts and raw outputs are separate and use floating-point entropy calculations.

## Positive update

For every Boolean function, in every dimension,

    D_cross(f)=2H(f)-E_z H(f(x)f(x+z)) <= 2 lambda_* M(f) <= 5.394754 M(f),
    5.3947539099 < 2 lambda_* < 5.3947539100.

The last inequality is strict when M(f)>0; when M(f)=0, D_cross(f)=0. Here M is minimum total influence over invertible binary input changes and output characters. This replaces the older universal coefficient six. The scalar extremum is fully proved and rationally certified. The sharp Boolean coefficient is only bracketed: 4 <= C_D < 5.394754. Do not call 5.394754 an upper constant for H(f)/I(f).

## Full-scope issue

The discounted derivative-chain sum of M is unbounded relative to its initial value, already on one-point defects. This remains true with the new one-step coefficient, and would remain an obstruction even if the candidate D_cross<=4M were proved. The universal signed allocation / hereditary erasure payment is still missing. Attack that payment rather than repeatedly optimizing or testing the scalar bound.

The report retains the inherited R32 truth-table entropy formula, with attribution, and records a translated-square form of D_cross. Its fourth-order positive contribution alone can be exponentially larger than M on nondegenerate quadratic phases, despite full D/M=4. Do not discard the negative 2 mod 4 credits. The six-point coefficient also refutes a direct conditionally-negative-definite entropy-kernel shortcut.

The stronger coefficient-four Boolean candidate passed the finite cases checked but has no all-dimensional proof here. Its relaxation to arbitrary real amplitudes is false at the explicit two-amplitude example in the report. Retain actual Booleanity and all signed convolution constraints; the worklog gives a two-coefficient obstruction to omitting even one constraint.

## Preservation

The preceding quadratic-symmetry and constant-four affine-clause theorems keep their original hypotheses and constants. No retired absolute-overlap, pointwise erasure converse, full-resolvent, or universal fixed-coefficient affine-drift target is reintroduced. No independent audit or novelty clearance is claimed. These files were produced as current research, not an assertion that a future worker has read them.
