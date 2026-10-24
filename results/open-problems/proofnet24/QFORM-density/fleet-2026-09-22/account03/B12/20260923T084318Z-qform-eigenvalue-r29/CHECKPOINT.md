SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T08:43:18Z.
attacking: Additional eigenvalue control — full nonseparable spectral tails at matrix level by protecting a three-dimensional complementary Schur shield and charging only leakage into that shield.

# Early substantive checkpoint

Run: `20260923T084318Z-qform-eigenvalue-r29`

Status: worked proof checkpoint; full QFORM still open.

## Candidate theorem: anisotropic three-shield leakage stability

Let `I` be an ORIGINAL-coordinate physical block and choose a deterministic orthogonal decomposition of its Euclidean coordinate space

`R^I = W direct_sum Z`, with `dim Z=3`.

This basis change is used only for deterministic matrix algebra; the random coordinates are never rotated.

Write a baseline compression as

`H0 = [[A0,C0],[C0^T,D0]]`

relative to `W direct_sum Z`. Assume `D0` is invertible and define

`mu0=sigma_min(D0)>0`,
`rho0=||C0 D0^{-1}||op`.

Add an arbitrary symmetric compression

`E = [[G,F],[F^T,EZ]]`.

There is NO bound at all on `G`: arbitrary rank, sign, and norm are permitted. Assume only

`eta=||F||op`, `epsilon=||EZ||op < mu0`.

Set

`mu=mu0-epsilon`,
`rho_bar=(rho0*mu0+eta)/(mu0-epsilon)`,
`ell(r)=(sqrt(r^2+4)-r)/2`.

Then the actual final block `H=H0+E` satisfies

`s3(H) >= gamma := mu * ell(rho_bar)^2`.                     (C.1)

Consequently, using the completed account04/B12 complementary-Schur shield theorem on the final protected `D=D0+EZ` and cross block `C=C0+F`, the full ambient quadratic form obeys

`||p_(X^T A X)||infinity <= 2 sqrt(6 pi |I|)/gamma`,          (C.2)

with arbitrary spectrum and couplings outside `I`. No independent-convolution claim is used.

### Proof of the first essential implication

`D=D0+EZ` gives `sigma_min(D)>=mu` by Weyl. Further,

`C D^{-1}`
`= C0 D0^{-1} (D0 D^{-1}) + F D^{-1}`,

and

`D0 D^{-1}=I-EZ D^{-1}`.

Therefore

`||C D^{-1}||op`
`<=rho0(1+epsilon/mu)+eta/mu`
`=(rho0*mu0+eta)/mu = rho_bar`.                              (C.3)

Now reinterpret the unrestricted `G` as the arbitrary active update in the account04/B12 theorem. Since the complementary block is exactly three-dimensional, all three of its singular values are at least `mu`. The partner theorem yields

`s3(H)>=ell(||CD^{-1}||)^2 mu>=ell(rho_bar)^2 mu`,

because `ell` is decreasing. This is (C.1).

This is stronger than a global small-operator-norm tail assumption: the `W-W` face can be unbounded. Only cross leakage into the three-mode shield and perturbation internal to the shield are charged.

## Spectral-update corollary

If the added matrix is represented as

`R=sum_r tau_r v_r v_r^T`,

and on `I` we decompose `v_r|_I=w_r+z_r` with `w_r in W`, `z_r in Z`, then

`epsilon <= sum_r |tau_r| ||z_r||^2`,
`eta     <= sum_r |tau_r| ||w_r|| ||z_r||`.                  (C.4)

Thus an arbitrarily large collection of added eigenvalues of either sign costs exactly zero when its physical vectors lie in `W` (`z_r=0`). More generally their absolute magnitudes are relevant only through actual leakage into `Z`.

## Concrete constants

Take `|I|=5`, `dim W=2`, `dim Z=3`,

`D0=diag(3,-3,3)`,
`C0=[[1,0,0],[0,1,0]]`,

so `mu0=3`, `rho0=1/3`. Allow arbitrary symmetric `G`, while

`||F||op<=1/4`, `||EZ||op<=1/4`.

Then

`mu=11/4`, `rho_bar=5/11`,
`gamma=(267-5 sqrt(509))/88 = 1.7522142985... >1`,

hence

`||p_Q||infinity <= 2 sqrt(30 pi)/gamma = 11.0809842960...`.   (C.5)

The added active spectrum is completely unrestricted.

## Newest-Claude branch to apply in final report

The required newest volume-stability theorem (`math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`) gives a second, continuous-density tail compiler: for disjoint ORIGINAL-coordinate banks with a protected diffuse cross block `M0`, `s3(M0)>=a`, range leverage at most `1/2`, any added matrix whose ACTUAL cross footprint obeys `||R[I,J]||op<=a/16` gives

`||p_Q||infinity <= 24 sqrt(3) e/(5a) <23/a`,                 (C.6)

while arbitrary self-block spectrum is free. This will be stated as an equation-level application, not as a structural dichotomy.

## Remaining gap

The bare global condition `s3(A)>=1` has not been shown to force either a controlled three-dimensional Schur shield, a diffuse cross-volume certificate, or an already-paid bank/hub/ridge exit. The difficult residue is high leakage into every candidate shield together with failure of the diffuse cross-volume gate. The full conjecture remains OPEN.
