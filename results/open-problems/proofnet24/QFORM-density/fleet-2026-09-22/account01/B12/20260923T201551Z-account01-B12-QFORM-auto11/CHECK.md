# Audit / exact arithmetic for QFORM-SIGNED-LOCAL-SPECTRAL-MASS-RESERVE-v1

Run: `20260923T201551Z-account01-B12-QFORM-auto11`.

## Deterministic proof checks

1. For a PSD matrix `G_tail` with decreasing eigenvalues `mu_j`,
   `(p+1) mu_(p+1) <= sum_(j=1)^(p+1) mu_j <= tr G_tail`, so `mu_(p+1)<=tr(G_tail)/(p+1)`.
2. The selected negative compression has range in `span{P_H v_a:a in B_-}` and therefore rank at most `r_-`, independent of all selected amplitudes.
3. After additionally truncating the first `p` eigenmodes of `G_tail`, the total hostile rank is at most `r_-+p`; rank interlacing gives `lambda_u(K)>=lambda_(u+r_-+p)(C_0+F)`.
4. Since `F>=0`, Loewner monotonicity gives `lambda_j(C_0+F)>=lambda_j(C_0)` for every `j`.
5. Restoring the PSD residual and then arbitrary `T_H` costs at most their operator norms. No random-variable perturbation estimate is used.
6. The negative-side formula is exactly the positive formula applied to `-C=(-C_0)+G-F-T_H`.
7. Conditioning on `H^c` keeps the `H`-coordinates independent with the same scalar density caps; outside couplings become affine coefficients. Thus the finite physical-core receiver is applied in its original-coordinate scope.

## Stress-family arithmetic

With `m=8`, `C_0=diag(4,4,4,4,-4,-4,-4,-4)`, `M_-=M_+=1/2`, `delta_H=1/4`, `r_-=r_+=1`, `u=2`, `v=1`:

Positive reserve denominator:

`4-2-1+1=2`,

so

`Gamma_+ >=4-(1/2)/2-1/4=7/2`.

Negative reserve denominator:

`4-1-1+1=3`,

so

`Gamma_- >=4-(1/2)/3-1/4=43/12`.

Hence `g=7/2`. The physical-core receiver is

`2 sqrt(6*pi*8)/(7/2)=(16/7)sqrt(3*pi)=7.017097425918778...`.

## Designated-partner arithmetic

For the same family, the selected local packet has rank at most two. The unselected local packet is `R=F_tail-G_tail` with both PSD traces at most `1/2`. Since

`-G_tail <=R<=F_tail`,

`||R||op<=1/2`.

Thus

`s_6(C)>=s_8(C_0)-1/2-1/4=13/4`.

The exact block-square identity gives

`lambda_6((A^2)[H,H])>=s_6(C)^2>=(13/4)^2`.

For account02/B12's six-mode compiler, `N_2=binom(8,2)=28` and

`C_8=max{8*28*sqrt(48*pi), 112*pi, 3*400^(1/3)*112^(5/6), 10*sqrt(2e/3)}`

with numerical terms

- `2750.7021909601613...`,
- `351.85837720205683...`,
- `1127.6031248207917...`,
- `13.461752804294704...`.

Therefore

`C_8=2750.7021909601613...`

and

`C_8/(13/4)=846.3699049108188...`.

## Edge cases

- If an active selected footprint span has dimension zero, take `r=0`.
- If no reserve remains beyond the selected packet, `p=0`; the formula remains valid and pays the full residual local mass.
- A zero positive or negative target count is simply omitted from the minimum defining `g`.
- Zero eigenvalues of `E` may be ignored.
- No assumption is made that the spectral vectors `v_a` are coordinate axes or that the rotated random coordinates are independent.
- Arbitrarily large off-core entries are permitted because neither the local eigenvalue certificate nor the physical-core conditioning step treats them as small.

Full QFORM remains OPEN; continuity is not obtained from this branch.
