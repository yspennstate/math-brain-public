SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-23T18:11:24.900489Z.
attacking: the four-anchor diagonal-plus-rank-four plus zero-diagonal max-norm twist chamber: derive a product-preserving finite-anchor payment or a sharper obstruction without treating small coefficients as a perturbation.

# Early checkpoint: unconditional D5-to-skeleton route

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN. Execution: WITHOUT_VERIFIED_BRAIN.

The latest designated partner account03/B13 r30 (`feda06c104c0d8c62661daf01eed33c10f55fa99`) obtains, conditional on its still-pending projected-crossing receiver, a global `V_3=O(rho^-6)` estimate and then a diagonal + rank <= 8 + `O(rho^-1)` Frobenius skeleton. I am replacing that conditional `V_3` input by the unconditional pinned `D_5` theorem and telescoping all four skeleton ratios.

Let

`rho = P{X^T A X in J}/|J|`,

`V_r(A)=sum det(A[S,T])^2`

over ordered disjoint physical r-sets `S,T`, and put `C5=5 sqrt(2e)`.

The pinned Fourier theorem `D_5` at `e5f71d79eff325201dd0274053d20268ce65b837` gives for every physical cut `L sqcup R`

`e_5(A[L,R]^T A[L,R]) <= (C5/rho)^10`.

A Bernoulli cut contains any fixed ordered disjoint 5-pair with probability `4^-5`; therefore

`V_5(A) <= 4^5 C5^10 rho^-10`.                                      (E1)

The same pinned source's localized three-coordinate Theorem A says that if a physical principal 3x3 block has all eigenvalues of modulus at least `c`, then the full ambient density is at most `6 sqrt(pi)/c`, uniformly in outside conditioning/affine terms. Hence if `rho>2+6 sqrt(pi)`, then necessarily

`V_1(A)=||A-diag(A)||_F^2 >= rho^-2`.                               (E2)

Indeed, otherwise the off-diagonal operator norm is `<rho^-1`; since `s_3(A)>=1`, three diagonal entries have modulus `>1-rho^-1`, and the corresponding physical 3x3 block has smallest singular value `>1-2/rho`, contradicting Theorem A.

If some `V_{r+1}=0` for `1<=r<=4`, the Claude skeleton theorem at `c4c23b784395630c094ba299a50712209921d1ae` already yields an exact diagonal + rank <=16 representation. Otherwise

`prod_{r=1}^4 V_{r+1}/V_r = V_5/V_1 <= 4^5 C5^10 rho^-8`,

so for some `r in {1,2,3,4}`

`V_{r+1}/V_r <= 2^(5/2) C5^(5/2) rho^-2`.                          (E3)

Corollary 3.2 of the proved skeleton identity then gives

`A=D+R+E`, `rank(R)<=4r<=16`, `E` symmetric zero-diagonal, and

`||E||_F <= 3(r+1) sqrt(V_{r+1}/V_r)
          <= 15*2^(5/4)*C5^(5/4) rho^-1
          = 768.5445683103545... rho^-1`.                           (E4)

Thus a high-density witness admits an UNCONDITIONAL diagonal + rank <=16 + O(rho^-1) Frobenius skeleton, without using the partner r30 projected-crossing receiver. The residual is retained as an actual quadratic form; it is not perturbatively deleted.

First unpaid implication: `QFORM-DIAG-RANK16-FROB-TWIST-ROUGH-GLUE-v1`: pay the rough product law for `D+R+E`, `rank R<=16`, `||E||_F=O(rho^-1)`, without support/moment assumptions, or construct a genuine finite-union product-indicator counterexample. The no-attainment purification theorem will be used only as a supremum/approximation transfer, never as existence of an optimizer.

Changed-file privacy check: manual allowlist review of this single mathematical file; it contains only public/pure-math source pins, formulas, constants and logical account/slot labels, with no credentials, scheduler identifiers, machine paths or unrelated data.
