# Fresh-peer addendum — determinant-zero closure of the B13 collar

A new compatible result landed during the required prepublication refresh:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

Its rank-three consequence states: for an exact-rank-three matrix `A=R Lambda R^T`, if physical row `i` has leverage `ell_i=||r_i||^2` and diagonal pivot `a_i=A_ii!=0`, then, with arbitrary induced affine terms/outside couplings,

`||p_Q||_infinity <=128 [ell_i |a_i| |det Lambda|]^(-1/4).`            (A.1)

This theorem is explicitly orientation-free and does **not** require an invertible selected physical `2 x 2` pair.

Apply it to the live nested-heavy B13 collar, where the first row has `ell_i=c>1/2` and the target has `|det Lambda|>=1`. For every `tau>0`,

`|A_ii|>=tau`

implies

`||p_Q||_infinity <128 (tau/2)^(-1/4)`

`=128*2^(1/4) tau^(-1/4)`

`=152.2185107204... tau^(-1/4).`                                    (A.2)

This closes the `det C=0` case omitted from Theorem 4.1 of the main report.

When the selected pair compression `C=A[{i,j},{i,j}]` is invertible, the new B13 theorem in the main report is sharper because `Delta_ij=ch>1/4`:

`||p_Q||_infinity`
` <16 sqrt(30) e^(1/4) tau^(-1/4)`
` =112.5263496208... tau^(-1/4).`                                    (A.3)

Combining (A.2) and (A.3) gives a determinant-free collar conclusion:

`boxed( |A_ii|>=tau  =>  ||p_Q||_infinity <152.219 tau^(-1/4) )`       (A.4)

with **no condition on the selected physical pair determinant**. The same conclusion holds with the second heavy row after swapping.

Therefore any putative unbounded sequence in the current non-leverage-one exact-rank-three collar must satisfy

`A_ii ->0` and `A_jj ->0`

for the two designated heavy rows. The residual obstruction is genuinely the simultaneous heavy-light-cone/product-provenance regime, not a vanishing physical `2 x 2` determinant.

This addendum consumes the fresh compatible theorem at an actual inequality and does not claim that the full QFORM conjecture is solved. Continuity is not added: only an essentially bounded density is certified in this branch.
