# fleet02/B15 checkpoint — common Fourier envelope gives quantitative rough-source stability

Programme: QFORM-DENSITY-3EIG-20260922. Full universal theorem remains OPEN.

Let two cap-one product source densities be `F=prod_i f_i` and `G=prod_i g_i` for the same quadratic map `Q=x^T A x` (affine terms may also be present), and put

`Delta = ||F-G||_1 <= min(2, sum_i ||f_i-g_i||_1)`.

Assume a matrix/source-class theorem supplies the same law-uniform Fourier envelope for both outputs,

`|phi_F(t)|, |phi_G(t)| <= min(1,K |t|^{-b})`, with `b>1`.

Then

`|phi_F(t)-phi_G(t)| <= min(Delta,2K |t|^{-b})`.

With `T=(2K/Delta)^(1/b)` (the Delta=0 case is trivial), Fourier inversion gives the exact interpolation estimate

`||p_F-p_G||_infty <= [b/(pi(b-1))] (2K)^(1/b) Delta^(1-1/b)`.

More generally, for `0<alpha<min(1,b-1)`, using `|e^{-ith}-1|<=2^(1-alpha)|t h|^alpha`,

`[p_F-p_G]_{C^{0,alpha}}`
` <= [2^(1-alpha)/pi] [1/(alpha+1)+1/(b-alpha-1)]`
`    *(2K)^((alpha+1)/b) Delta^(1-(alpha+1)/b)`.

Thus a common integrated-Fourier certificate upgrades ordinary product `L1` approximation to uniform output convergence, and even to convergence in every subcritical Holder seminorm. This is a source-limit theorem: the height estimate comes directly from Fourier inversion, not from continuity.

For the current q=4/3 volume envelope used by fleet03/B15 auto13,

`b=9/8`,
`K=e^(9/8)(4/3)^(-9/16) pi^(9/8) Z^(-3/16)`, `Z=e3(M^T M)`,

so

`||p_F-p_G||_infty <= 39.233 Z^(-1/6) Delta^(1/9)`

and, at `alpha=1/16`,

`[p_F-p_G]_{C^{0,1/16}} <= 166.572 Z^(-17/96) Delta^(1/18)`.

This directly supplies a quantitative rough-law bridge for any smooth-padding proof of that volume branch.

Required e5 source application to be completed in the final report: independently pass its ruled one-sheet interval estimate through original-coordinate Gaussian padding in total variation, yielding the same essential-density bound for rough cap-one inputs without any continuity claim.
