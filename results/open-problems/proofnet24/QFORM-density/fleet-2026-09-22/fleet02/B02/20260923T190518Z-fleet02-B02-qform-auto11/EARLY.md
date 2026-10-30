SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-23T19:05:18Z.

# Early calculation — Fisher review + disjoint third-compound Fourier compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T190518Z-fleet02-B02-qform-auto11`  
Status: substantive checkpoint; full QFORM remains OPEN.

## 1. Requested independent check of the projected-Fisher argument

Source: `yspennstate/math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2`, `proofnet24/QFORM-density/interactive/20260923T184054Z-fisher-continuation/FISHER_INFORMATION.md`.

For the B02-assigned analytic scope I obtain PASS.

Let `sqrt(f_i) in H^1`, `S_i=f_i'/f_i` on `{f_i>0}`, `J_E=E|U^T S|^2`, `z=U^T X-z0`, `R=|z|`.

1. `sqrt(f_i) in H^1` implies `f_i in W^{1,1}`, `f_i'=2 sqrt(f_i)(sqrt(f_i))'`, `E S_i=0`, `E S_i^2=I_i`; independence gives `E|U^T S|^2=J_E`.
2. For `W_delta=Uz/(R^2+delta)`,
   `div W_delta = r/(R^2+delta)-2R^2/(R^2+delta)^2 >= (r-2)/(R^2+delta)`.
   With a compact cutoff first, fixed-delta fields are bounded and cutoff errors are `O(N^{-1})` times an integrable/tail factor. Cauchy-Schwarz gives `(r-2)K_delta <= sqrt(J_E K_delta)`, hence `K_delta<=J_E/(r-2)^2`; monotone convergence gives `D=E R^{-2}<=J_E/(r-2)^2`.
3. For `V_delta=U Lambda^{-1}z/[2(R^2+delta)]`, the centering `z0=-(1/2)Lambda^{-1}U^Tb` gives exactly `grad Q . V_delta=R^2/(R^2+delta)`. Orthogonal affine components and the remaining spectrum cancel in this contraction. Also `|div V_delta|<=r/(2sR^2)` and `|V_delta.S|<=|U^TS|/(2sR)`, both integrable by the preceding estimate.
4. For nonnegative smooth compactly supported `psi`, mass `m`, the centered primitive `Phi(t)=int_{-infinity}^t psi-m/2` obeys `||Phi||_infinity<=m/2`. Weak integration by parts therefore yields
   `E psi(Q) <= m [rD+sqrt(J_E D)]/(4s)` after `delta downarrow 0`. The factor `1/4` is exactly the product of the `1/2` in `V_delta` and the centered-primitive `m/2` bound. Domination on all such test functions implies domination of the pushforward measure by this multiple of Lebesgue measure, hence the claimed essential density bound.
5. The cap-one layer-cake constant also checks: the projection density cap `2^(r/2)` gives
   `E R^{-2}<=D_r=2r v_r^(2/r)/(r-2)`.

No moment is used in these cutoff passages. This check does NOT remove the Fisher/H1 hypothesis. The later fleet02/B15 result at `4ae555c379a6f87e7af74c01fff215986650ffb4` strengthens the obstruction: every H1 approximation `f` to `1_[0,1]` with `eta=||f-1_[0,1]||_1<=1/8` has `I(f)>=1/(4 eta)`, so a uniformly bounded Fisher budget cannot close the arbitrary rough cap-one target by approximation.

## 2. New application of the designated partner result

Latest completed compatible `fleet03/B02` result: `QFORM-DISJOINT-COMPOUND-E3-L1-v1` at `c2a842f9cd113aa20d792ca1692a358fdc1be356`.

Put
`D3=V_0(A)=sum_{|I|=|J|=3, I cap J=empty} det A[I,J]^2`.
A fair random physical cut `[n]=L disjoint-union R` has
`E_cut E3(A[L,R])=D3/64`,
so some actual original-coordinate cut has `Z3:=E3(A[L,R])>=D3/64`.

On that LIVE physical block, the reviewed sharp-Hausdorff-Young theorem at `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba` and the completed incident-E3 cascade from the previous B02 receiver give the marginal-free coefficient
`C3*=10.345083232147514`:
`||p_Q||_infinity <= C3* Z3^(-1/6)`,
`int |phi_Q(t)|dt <= 2 pi C3* Z3^(-1/6)`.
Hence

`||p_Q||_infinity <= 20.69016646429503 D3^(-1/6)`,
`int |phi_Q(t)|dt <= 130.00014993155833 D3^(-1/6)`.

Under the exact owner hypothesis `s3(A)>=1`, Cauchy-Binet gives `V_0+V_1+V_2+V_3=e3(A^2)>=1`. Thus if `D3=V_0>=1/4`,

`||p_Q||_infinity < 26.06797625419429`,
`int |phi_Q(t)|dt < 163.7899253882599`.

This strictly sharpens the designated partner's disjoint-stratum coefficient because it inserts the reviewed sharp-HY/marginal-free E3 receiver at the partner's actual random cut.

The same selected block also has the complementary D5 exit
`||p_Q||_infinity <= (5e/sqrt(2)) E5(A[L,R])^(-1/10)`.
Consequently on this live cut one may take the minimum of the E3 and D5 estimates; D5 is smaller whenever
`E5(A[L,R]) >= 0.4788009378679107 Z3^(5/3)`.
No lower bound on this E5 quantity follows from D3 alone, so this is a genuine complementary exit, not an unconditional strengthening of the random-cut theorem.

## 3. New first unpaid implication

If `s3(A)>=1` but `V_0<1/4`, then necessarily
`V_1+V_2+V_3>3/4`.
The next structural obligation is therefore an **overlap-compound receiver**: turn a quantitative portion of these one-, two-, or three-index-overlap third minors into a product-preserving integrated-Fourier packet. The partner r36 `3x2` kernel-curvature theorem pays any literal packet with `|w^T D w|>0`, but no dimension-free extraction of such a packet from aggregate `V_1+V_2+V_3` has yet been proved. The fresh `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` correction forbids replacing this aggregate step by a claimed universally large singleton hub/star.
