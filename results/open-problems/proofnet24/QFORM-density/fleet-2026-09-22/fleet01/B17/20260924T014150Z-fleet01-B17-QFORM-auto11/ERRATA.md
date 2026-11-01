# Immutable run errata / precision notes

1. In REPORT.md Section 6.2, the strict derivative statements `p_beta'(t)>0 (t<0)` and `p_beta'(t)<0 (t>0)` are to be read **on the interior of the support where the density is nonzero**. Outside the compact support the derivative is zero. The intended and proved global statement is: `p_beta` is nondecreasing up to zero and nonincreasing after zero, with strict monotonicity on the relevant nonzero interior pieces. Hence the global-mode conclusion and exact norm formula (31) are unchanged.

2. The first immutable `CHECK.py` used structural SymPy equality against a factored polynomial. This can fail syntactically even when the polynomials are identical. `CHECK_v2.py` is the corrected executable checker and is the one validated in-run. No mathematical identity in REPORT.md is changed.
