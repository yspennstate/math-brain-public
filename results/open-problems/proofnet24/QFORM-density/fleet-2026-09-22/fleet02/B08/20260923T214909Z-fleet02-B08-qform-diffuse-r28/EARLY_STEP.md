SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-23T21:49:09Z.
attacking: an explicit full-matrix physical-pair gate and the near-singular exact-Schur-match remainder of the diffuse/common-plane hybrid.

# Early substantive step — physical-pair gate

Let `L>0` and let the real symmetric matrix `A` have at least three eigenvalues of modulus at least `L`. Choose any two ORIGINAL coordinates `H` for which the physical principal pair `B=A[H,H]` is invertible and indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)`.

Complete the pair exactly. The remaining original coordinates stay independent and the residual quadratic coefficient is the Schur complement `S=A/B`; arbitrary affine terms are retained. The fixed source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` gives two inputs: (i) Schur complement interlacing leaves at least one eigenvalue of modulus at least `L`, hence `||S||op>=L`; (ii) its arbitrary-rank small-ball theorem gives, uniformly in the affine term,

`sup_w P(|R-w|<rho) <= min(1, 5 (rho/L)^(1/4)).`                 (E1)

The physical-pair logarithmic envelope gives for every `r>0`

`p_Q(s) <= 2sqrt(2)/r + D^(-1/2) E log_+(2r^2/(kappa|s-R|)).`   (E2)

For `a=2r^2/kappa`, layer cake and (E1) imply

`E log_+(a/|s-R|) <= int_0^infty min(1,c e^(-u/4)) du`,
`c=5(a/L)^(1/4).`                                                (E3)

If `c>=1`, the last integral is at most `4(1+log c)`. Choose `r=sqrt(2) kappa`. Then

`c=5sqrt(2)(kappa/L)^(1/4)`

and, using `sqrt(D)>=kappa`,

`||p_Q||infty <= [6+4log(5sqrt(2)(kappa/L)^(1/4))]/kappa`.       (E4)

For `kappa/L>=1/64`, the bracket divided by `kappa/L` is decreasing, and at `1/64` equals

`64[6+4log(5/2)] = 618.5704273597...`.

Therefore every indefinite physical pair with

`kappa>=L/64`

pays the FULL ambient form by

`||p_Q||infty <619/L`.                                           (E5)

If `B` is definite, the two-coordinate ellipse estimate gives `||p_Q||infty<=pi/sqrt(D)<=pi/kappa<202/L` at the same gate. Consequently **any invertible physical two-coordinate block with least singular value at least `L/64` is paid by `<619/L`**, with arbitrary remaining spectrum, same-bank curvature, outside couplings, and affine terms.

This leaves only the near-singular physical-pair chamber `sigma_min(B)<L/64` for the common-plane B08 survivor. The next step is to combine this with the newest partner/rank-free first-compound Schur receiver and quantify exactly how close the survivor must be to Schur match.
