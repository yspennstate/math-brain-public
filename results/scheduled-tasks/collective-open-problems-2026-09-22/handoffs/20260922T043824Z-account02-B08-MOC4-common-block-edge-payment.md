# account02/B08 MOC4 handoff — `MOC4-COMMON-BLOCK-EDGE-PAYMENT-v1`

Outcome: **ESSENTIAL_STEP_APPLIED**; full MOC4 remains OPEN.

Canonical scientific source: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account02/B08/B08-20260922T043824Z-r11/REPORT.md`, creation commit `5b63fa9532f8260413cdaf0209f6dd85c486de0b`, Git blob `2a238a6c8015216463d1f3c8e491d3844ff7de6c`.

For any proper common reducing block and any determinant-one `SU(2)` gate mixing one eigen-column from each of two distinct blocks,

`D(U0 G_pq)=c^2 D(U0)+s^2 D(U0 S_pq)`.

The duplicate-column cross terms vanish by block dimension count. Both endpoints remain proper common-block pairs, hence are MOC4-safe by the known `n<=3` block product theorem. The row analogue follows by swapping the two normal matrices. Therefore no common-block counterexample can escape through one eigen-coordinate cross edge.

For a `2+2` boundary `U0=diag(V,W)` and disjoint cross gates `(1,3)` and `(2,4)`, the entire true-unitary torus has exact form

`D = sum_{eps1,eps2} w_eps D_eps + 2 c1 s1 c2 s2 F Re(zeta1 conj(zeta2) kappa)`,  
`F=(a1-a2)(a3-a4)(b3-b1)(b4-b2)`,  
`kappa=v11 v21 w12 w22/(det V det W)`.

The two surviving mixed coefficients are conjugates by the `2x2` unitary identities, so the phase freedom is a one-real-dimensional chord, not a free complex ellipse.

At a support boundary base `L(D00)=M`, define safe endpoint deficits `delta10=M-L(D10)`, `delta01=M-L(D01)`, and `C=|kappa| |L(F)|`. Then

`C^2 <= delta10 delta01`

is necessary and sufficient for local safety within this matched two-edge torus, and is sufficient for global safety on the whole torus. If it fails, arbitrarily small genuine two-gate perturbations give an actual MOC4 support counterexample, not a surrogate failure.

The previous exposed mismatched-circle B08 witness was checked exactly: the two perfect matchings have payment margins `1279` and `1006`, so both complete matched two-edge tori are globally safe; this upgrades the prior tangent-Hessian check.

Named OTHER-account result applied: account03/B09 `MOC4-CYCLE-SEPARATOR-NOGO-v1`, report blob `f0a1e4daf7262912f6d68b8984fb42abc03f5064`. Its genuine `SO(6)` no-go means the remaining multi-edge payment cannot be replaced by a transport-only cycle cut; it must exploit the structured spectral support normal.

First unpaid boundary implication: **`MOC4-COMMON-BLOCK-STRUCTURED-PAYMENT-v1`** — prove the two payment inequalities for both cross perfect matchings at every source-valid support-exposed `2+2` common-block boundary, or exhibit actual spectra/block unitaries/support direction violating one. A violation is already a true-unitary MOC4 counterexample by the theorem above. Even if both payments hold, shared-index/noncommuting multi-edge interactions remain.
