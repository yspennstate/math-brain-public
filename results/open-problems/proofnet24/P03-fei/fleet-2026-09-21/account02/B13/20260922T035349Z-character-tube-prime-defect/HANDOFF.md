# Source-bound handoff — account02/B13 character-tube payment

Full FEI remains open.

Sources actually consumed:

- account01/B18 `20260922T002302Z-gate-refutation-balanced-excess`, commit `64935432d83bb0c759225a6149535980157f1a62`: exact `FEI(C) <=> H(g)<=C[I(g)-1]` for every balanced Boolean `g`.
- account04/B18 `20260922T021124Z-all-block-safe-split-barrier`, commit `1ea788b0a5f8839c29baeeca5680d3647170b04b`: a minimum scalar-corrected gate obstruction is composition-prime and bad for every nonempty physical block.
- account01/B18 `20260922T0325Z-addressing-star-cdagger`, commit `c0faef50ba04f6aea9711fccd6aed2ba3fa71c9d`: stable candidate `C^dagger=6.521851214` and remaining prime/all-bias gate implication.

New reusable theorem. For Boolean `g`, nonempty physical character `chi_T`, `k=|T|`, choose a sign so `alpha=Pr[g != sigma chi_T]<=1/2`, and let `h=sigma chi_T g`. Then

`H(g)=H(h)`,

`I(g)-1 = I(h)+k-1-2 sum_{i in T} Inf_i(h)`,

`H(g) <= h2(m)+m log2(2^n-1)`, with `m=4 alpha(1-alpha)`,

and by cube edge isoperimetry plus `Inf_i(h)<=2 alpha`,

`I(g)-1 >= k-1+2 alpha[log2(1/alpha)-2k]`.

In particular, if `g` is balanced and for some original coordinate `i`

`0<Pr[g != sigma chi_i] <= 2^{-n/2-3}`,

then

`H(g) < 6 [I(g)-1]`.

Hence every balanced witness to failure at any `C>6`, including the current `C^dagger`, has distance strictly greater than `2^{-n/2-3}` from both signs of every original-coordinate dictator.

Counterexample to a tempting shortcut. For every `n>=3`, take `g_n=chi_1` with the values at `0^n` and `1^n` flipped. Then `g_n` is balanced, all variables are essential, and it is composition-prime (every proper block of size at least two produces at least three distinct restrictions, whereas a Boolean child bit permits at most two). Yet `Pr[g_n != chi_1]=2^{1-n}->0` and `I(g_n)-1=4(n-2)/2^n->0`. Its exact Fourier support is the odd parity class, with `hat g({1})=1-4/2^n` and every other odd coefficient `-4/2^n`. Nevertheless `H(g_n)/(I(g_n)-1)<6` for every `n>=3`, tending to `4`.

Interpretation for Campaign A: **primitivity alone cannot supply a fixed Hamming/spectral gap from characters or a fixed positive excess-influence gap.** Criticality is essential. The valid next split is: pay the near-original-dictator tube by the theorem above, and attack the common physical-block potential only on the complementary region. Do not replace minimum obstruction by prime gate and then assume a primitive character gap.

Primary report: `proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T035349Z-character-tube-prime-defect/REPORT.md`.
