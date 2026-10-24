# Checks for exact-constant compactification / affine homogenization

## Check 1: cap-preserving tail completion

For `delta = int_{|x|>R} f`, define `J=[R+1,R+1+delta]` and

`g=f 1_{[-R,R]}+1_J`.

Then `0<=g<=1`, `int g=1`, and

`||g-f||_1 = int_J(1-f)+int_{tail\J}f = 2(delta-int_J f) <= 2 delta`.

Hence `d_TV(g dx,f dx)<=delta`.

## Check 2: product total variation

For probability measures `mu_i,nu_i`, telescoping

`tensor mu_i - tensor nu_i = sum_k (tensor_{i<k} nu_i) tensor (mu_k-nu_k) tensor (tensor_{i>k} mu_i)`

gives

`d_TV(tensor mu_i,tensor nu_i) <= sum_i d_TV(mu_i,nu_i)`.

Measurable pushforward is a contraction, so the same bound holds after `x -> x^T A x+b^T x+c`.

## Check 3: spectral perturbation in affine homogenization

Write

`B_T = D_T+E_T`,

`D_T=diag((1+delta_T)A,0)`,

`E_T=[[0,b/(2T)],[b^T/(2T),0]]`.

The only nonzero eigenvalues of `E_T` are `+||b||/(2T)` and `-||b||/(2T)`, so

`||E_T||op=e_T=||b||/(2T)`.

Set `delta_T=2e_T`. If `A` has `p` eigenvalues >=1 and `q` eigenvalues <=-1 with `p+q>=3`, then `D_T` has at least `p` eigenvalues >=`1+2e_T` and at least `q` eigenvalues <=`-1-2e_T`. Weyl/min-max gives `B_T` at least `p` eigenvalues >=`1+e_T` and at least `q` eigenvalues <=`-1-e_T`. Thus `B_T` has at least three eigenvalues of absolute value strictly greater than one whenever `b!=0`.

## Check 4: almost-sure limit uses no moments

With `Y_T=T+U`, `U in [0,1]`,

`Qtilde_T=(1+delta_T)X^TAX+(1+U/T)b^T X`.

For every sample `X in R^n`, both `X^TAX` and `b^TX` are finite and the scalar coefficients converge to one. Thus `Qtilde_T -> X^TAX+b^TX` pointwise/almost surely; no expectation, variance, or tail moment is invoked.

## Check 5: passing the density cap through weak convergence

If `mu_T => mu` and `mu_T(I)<=C|I|` for every bounded open interval, Portmanteau gives

`mu(I)<=liminf_T mu_T(I)<=C|I|`.

Countable decomposition extends this to open sets; outer regularity gives `mu(B)<=C|B|` for Borel `B`. Therefore `mu<<Leb` and its Radon-Nikodym density is <=`C` a.e.

## Check 6: partner constant

Account04/B14 r7 gives `C0=4+2 log 8` on its target-level conjugate-shear family. Numerically

`4+2 log 8 = 8.158883083359672... < 8.159`.

The compactification inequality is

`P(Q in I) <= C0 |I| + sum_{j=1}^4 P(|X_j|>R)`.

The second term tends to zero for every probability law, independently of moments.

## Scope check

No continuity passage is claimed. Uniform `L^infinity` bounds under TV/weak limits yield essential boundedness but not continuity. No bounded-diameter or finite-fragment reduction is asserted.
