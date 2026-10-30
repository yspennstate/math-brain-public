# fleet02/B02 early substantive checkpoint — four-row volume support closes by exact-rank-three Fourier

Programme: `QFORM-DENSITY-3EIG-20260922`. Run: `20260923T061511Z-fleet02-B02-QFORM-auto11`.

Fresh owner control at start: `yspennstate/math-research-brain@d9fd8e166d53646e798760180259479cc10764d2`, revision `2026-09-22.15`. Execution context: `WITHOUT_VERIFIED_BRAIN`.

## First unpaid implication attacked

The preceding B02 run left the quantitative three-volume stability alternative: for a physical original-coordinate cross block `M=A[I,J]`, `Z=E3(M)>0`, either the three-sample integrated-Fourier compiler applies, or one physical row is near-coloop, or a four-row set `H` carries a fixed fraction of `Z`. This checkpoint closes the entire four-row branch.

## Theorem — `QFORM-FOURROW-EXACTRANK3-COMPILER-v1`

Let `H subset I` have exactly four rows and suppose

`E3(M[H,J]) >= kappa Z`, `kappa>0`.

For each `i in H`, write `P_i=M[H\{i},J]`. Every squared `3x3` minor of `M[H,J]` uses exactly one of the four three-row subsets `H\{i}`. Hence Cauchy--Binet gives the exact partition

`E3(M[H,J]) = sum_(i in H) E3(P_i)`.

Therefore some `i` satisfies

`E3(P_i) >= (kappa/4) Z >0`.

The block `P_i` has exactly three physical rows. Since `E3(P_i)>0`, it has rank at least three; because it has only three rows, it has **exact rank three**.

Now apply the completed designated-partner theorem `QFORM-EXACT-RANK3-CROSSBLOCK-FOURIER-v1` from

`yspennstate/math-open-problems`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T230126Z-fleet03-B02-QFORM-r17/REPORT.md`.

That theorem allows arbitrary same-bank quadratic terms and outside couplings, and for an exact-rank-three physical cross block `P` gives

`|phi_Q(t)| <= min(1,(2*pi)^(3/2) E3(P)^(-1/4)|t|^(-3/2))`,
`||p_Q||inf <= 6 E3(P)^(-1/6)`.

Substituting the displayed lower bound yields

`boxed{ ||p_Q||inf <= 6 (4/kappa)^(1/6) Z^(-1/6). }`

The conclusion is obtained from an actual `L1_t` characteristic-function envelope, so this branch has a continuous density vanishing at infinity.

### Consequences

1. For the previous B02 stability constant `kappa=0.834844`, the coefficient is `<7.791`.
2. At the exact four-row-support endpoint (`kappa=1`), the coefficient is `6*4^(1/6)<7.560`.
3. At the exact coloop endpoint, deleting the hub leaves `E3=0`, hence residual cross rank at most two; adjoining the one hub row makes the whole live cross block exact rank three because `Z>0`. The same partner theorem then gives the sharper `||p_Q||inf<=6 Z^(-1/6)`. Thus the entire exact `delta_3=0` endpoint of the preceding three-sample compiler is now paid.

## Analytic-review checkpoint

The newest sharp-Hausdorff--Young coefficient remains consistent at its endpoints: general `k`-volume gives

`e q^(-1/2) k/(k-2q) E_k(M)^(-1/(2k))`

whenever `max alpha_i^(k)<=q/2`, `q>=1`, `k>2q`. Thus for `k=3`, `h<=1/2` uses `q=1` and gives `3e Z^(-1/6)`; for `1/2<h<3/4`, `q=2h` gives `3e/[sqrt(2h)(3-4h)] Z^(-1/6)` and correctly blows up as `h up to 3/4`; and for `k=5`, `q=2` is always admissible and gives `(5e/sqrt(2))E5(M)^(-1/10)`. No endpoint at `h=3/4` is asserted.

## Remaining gap after this checkpoint

The preceding quantitative trichotomy now leaves only the **near-coloop but nonzero residual third-volume** branch. The next calculation should exploit the hub star jointly with its small but nonzero residual exterior volume; repeating a fixed-minor or scalar pointwise-decay argument would violate live corrections.
