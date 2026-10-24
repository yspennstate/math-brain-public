# Independent audit: `BOUNDARY_GRID.md`

**Verdict: the proposed finite-grid theorem passes this audit**, conditional on the earlier joint signed-ray/marked-endpoint initialization law cited in the theorem. The deterministic proof correctly treats actual simultaneous discrete GD and preserves reactivation and negative overshoot. Its scope is a fixed number of boundary steps; this review does not endorse a growing-step or macroscopic nonorthogonal limit.

## Update and normalization

For `f=(aL)^(-1)sum_i W_i(XU_i)_+`, the parameter gradients of half squared loss, multiplied by `L^2` and then by physical step `h=gamma/L`, yield exactly

`Delta U_i=(gamma/a) W_i X^T D(v_i)r`,
`Delta W_i=(gamma/a) r^T(v_i)_+`.

Thus `Delta v_i=gamma(W_i/a)G D(v_i)r`. It updates *all* projected coordinates through `G` even if their own gate is off. The tangent Gram after multiplication by `L^2` is exactly equation (2). No projected-coordinate absorption is inserted, and evaluating `D` at the pre-step state defines the discrete algorithm at zero.

## Fixed-step control and endpoint continuity

The row update is a symmetric block/star matrix in `(W_i,U_i)`, with operator norm of its increment at most `(gamma/a)||X||||r_n||`; the row-energy bound follows. The exact output increment has size `O(gamma ||r_n|| S_m,n/L)` per fixed step, so localization and induction give `r_n-r_0=O(1/L)` and a row-relative displacement `O(1/a)` for a fixed list of steps. This proves both freeze estimates (10). It does not rely on monotone gates or loss descent.

For a fixed `z,r` and gate history, `v_n=Xu+gamma z G sum_{j<n}D_jr`. Each possible coordinate equality `v_{n,l}=0` is an affine hyperplane in the continuously distributed original mark `u`, because the corresponding row of `X` is nonzero. There are finitely many histories through a fixed grid horizon. Independence of the limiting `F` and marked `N` permits conditioning on `r=y-F`, so all retained Poisson atoms have nonzero threshold margins almost surely. Induction through the finite grid then validates endpoint orbit convergence even with repeated activation changes. This is a finite-retained-set statement; the proof does not assume a uniform margin over infinitely many small atoms.

## Exact output and cutoff removal

Multiplying the network output increment by `L` gives the exact identity

`L Delta f = sum_i (W_i,n/a)[(v_i,n+1)_+-(v_i,n)_+]`
`           +(gamma/a^2)sum_i (r_n^T h_i,n)h_i,n+1`.

The second term is `gamma C_m,n r_n+O(gamma^2 ||r_n||^2 S_m,n/a)`, hence tends to `gamma Cr`. For each retained marked output-weight endpoint, the first term tends to `z[(v_{n+1})_+-(v_n)_+]`; summing fixed steps telescopes to the stated `P_n=n gamma Cr+int z[(v_n)_+-(Xu)_+]N`. This is the correct finite-step output limit. Replacing this displacement by `gamma sum K_j r` with the pre-step tangent Gram would miss off-to-on secants.

Small initial output weights are controlled uniformly for each fixed step by their normalized initial squared mass plus the global `O(1/a)S_m,0` squared-weight drift. The expected small mass is `O(epsilon^(2-alpha))`. Both the endpoint kernel and endpoint output displacement obey `O(z^2)` bounds at small `z`; large-`z` endpoints have vanishing occurrence probability as the cutoff grows, and bounded-away-from-zero `z` endpoints with large original marks have vanishing occurrence probability as the mark cutoff grows. Thus the limiting Poisson sums are absolutely convergent almost surely, and the cutoff passage in both `K_n` and `P_n` is justified. No infinite second moment is invoked for the large-`z` tail.

The initialization extension to nonorthogonal `X` uses the previously proved signed-coordinate categories and the two remainder estimates quoted in the theorem; neither estimate requires `G=I`. Full row rank supplies the density of `F` and positive definiteness of `C`. These are dependencies, not results supplied by the finite-grid dynamical argument itself.

The finite list of held path heights converges jointly and all paths jump on the same deterministic `gamma` grid, so the stated product `J1` conclusion follows. Nothing in these bounds permits the number of steps to grow with `m`; in particular it does not establish an averaged sliding kernel or macroscopic training law.

## Deterministic cross-check

`code/e03_chatter_check.py` was executed with exact rational arithmetic; its stdout is saved in `outputs/e03_chatter_check.txt`. For `rho=1/2,z=1,r=(-1,1)`, phases `x0=0` and `x0=gamma/4` have different average secant matrices but both give mean output velocity `(0,3/4)`. The average pre-step tangent matrix predicts `(-1/4,3/4)` when applied to the same frozen residual. This checks the need for the endpoint displacement in `P_n`; it is a deterministic frozen-endpoint check, not a stochastic finite-width simulation or proof of (6).
