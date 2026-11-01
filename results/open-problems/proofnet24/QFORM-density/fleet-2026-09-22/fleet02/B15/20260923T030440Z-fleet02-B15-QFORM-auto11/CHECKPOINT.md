SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T03:04:40Z.
attacking: the precise rough-law limiting/trace passage for the newest ruled and volume density estimates, with a source-valid obstruction if pointwise conditioning loses uniformity.

# Early substantive checkpoint — rough-source stability under the fractional-volume gate

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.

Source actually used at an equation: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. Its fractional-volume theorem says: for a fixed original-coordinate cross block `M=A[I,J]`, `Z=e_3(M^T M)>0`, `1<=q<3/2`, and third-volume row marginals `alpha_i<=q/2`, every cap-one product law has

`|phi(t)| <= min(1,K |t|^{-b})`,

where

`b=3/(2q)>1`,
`K=[e^3 q^{-3/2} pi^3 Z^{-1/2}]^{1/(2q)}`.

This already pays the height in its stated matrix class. The B15 obligation here is to justify the rough-law passage quantitatively rather than infer it from continuity.

Let `f=prod_i f_i` and `g=prod_i g_i` be two product probability densities with all marginal caps at most one, for the SAME fixed quadratic-plus-affine phase and SAME admissible cross block. Set

`Delta = min(2, sum_i ||f_i-g_i||_1)`.

Then the product-density telescoping inequality gives `||f-g||_1<=Delta`, hence for every frequency

`|phi_f(t)-phi_g(t)| <= Delta`.

Both characteristic functions obey the source envelope, so also

`|phi_f(t)-phi_g(t)| <= 2K |t|^{-b}`.

Consequently

`|phi_f(t)-phi_g(t)| <= min(Delta,2K|t|^{-b})`.

Put `T=(2K/Delta)^{1/b}` (the assertion is trivial for `Delta=0`). Direct integration gives

`int_R |phi_f-phi_g| dt`
` <= 2[Delta T + (2K)/(b-1) T^{1-b}]`
` = 2 b/(b-1) (2K)^{1/b} Delta^{1-1/b}`.

Fourier inversion therefore yields the quantitative source-stability inequality

`||p_f-p_g||_infinity`
` <= b/[pi(b-1)] (2K)^{1/b} Delta^{1-1/b}`
` = [3 e 2^{2q/3}/((3-2q)sqrt(q))] Z^{-1/6} Delta^{(3-2q)/3}.`            (A)

This is an `L^1(source)->L^infinity(output)` Holder modulus in the fractional-volume class. It is NOT a spatial modulus of continuity of the output density.

Application to arbitrary rough marginals: Gaussian-pad each ORIGINAL coordinate, `f_i^eta=f_i*gamma_eta`. This preserves independence and the cap `<=1`, and `||f_i^eta-f_i||_1->0`. Applying (A) to two padding scales makes the smooth output densities uniformly Cauchy. Since each padded output is in `C_0` by the source Fourier theorem, the uniform limit is in `C_0`. Product laws converge in `L^1`, hence pushforwards converge in total variation; this identifies the uniform limit with the density of the original rough output law. Essential boundedness is paid directly by the source estimate, not inferred from this continuity conclusion.

For the newest near-diffuse certificate, `q=4/3`, `Z^{-1/6}<=16/(15a)`, so (A) becomes

`||p_f-p_g||_infinity <= (24 sqrt(3)e/5) 2^{8/9} a^{-1} Delta^{1/9} < 42 a^{-1} Delta^{1/9}.`

Remaining full-target gap: the bare three-large-eigenvalue hypothesis does not force this volume gate. The rough-law passage is now paid when the gate holds; N3/high-leverage/low-cross-rank structural coverage remains separate.
