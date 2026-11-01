# Deterministic checks — fleet01/B09 `20260923T214821Z-fleet01-B09-QFORM-auto11`

Status: `PASS` for the identities and numerical regressions recorded below. These are checks of the written proof, not evidence for the unrestricted conjecture.

## 1. Third-compound ledger

For a fixed-seed random real symmetric `7 x 7` matrix, direct enumeration of squared `3 x 3` minors by overlap size gave

- `Omega_0 = 119.86374376185951`;
- `Omega_1 = 767.5779016603002`;
- `sum_r Omega_r = 1694.732521586291`.

Independent Gram/compound evaluations gave

- `sum_{|S|=3} det(A[S,S^c] A[S,S^c]^T) = 119.86374376185955`, absolute discrepancy `4.26e-14`;
- `sum_{|S|=3} tr(P_S^2 adj(G_S)) = 767.5779016603002` to displayed precision;
- `e3(A^2) = 1694.7325215862948`, discrepancy `3.64e-12`.

These numerics agree with the exact identities

`Omega_0=sum_S det G_S`,

`Omega_1=sum_S tr(P_S^2 adj G_S)`,

and

`sum_r Omega_r=e3(A^2)`.

## 2. One-overlap correction family

For

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`

with even `m`, exact counting gives

`Omega_(1,h)=m^2(m-1)^2/m^4=((m-1)/m)^2`.

Values checked:

- `m=4`: `0.5625`;
- `m=6`: `0.6944444444444444`;
- `m=8`: `0.765625`;
- `m=16`: `0.87890625`.

The balanced literal cut splits each `m`-bank into halves. Its Schur cross matrix has singular values `1/2,1/2`, hence

`Z2=(1/2)^4=1/16`.

The two-volume determinant law chooses one row from each half-bank, so every row marginal is exactly `2/m`, respectively `1/2,1/3,1/4,1/8` in the four checks above.

Therefore the clean fractional half-Riesz receiver gives

`4 sqrt(2e) Z2^(-1/8)=4 sqrt(2e) sqrt(2)=8 sqrt(e)`

and

`8 sqrt(e)=13.189770165601026`.

## 3. Omega0 dominant constant

With `Omega_0>=1/4`, random two-coloring gives a cut with `Z3>=1/256`. Thus

`C3 Z3^(-1/6)
 <= [3*2^(4/3)*e^(1/3)]*256^(1/6)
 =26.58475958065858`.

## 4. Designated partner target regression

For

`A5=[[0,0,1,1,0],
     [0,0,2,0,1],
     [1,2,0,0,0],
     [1,0,0,0,0],
     [0,1,0,0,0]]`,

the exact characteristic polynomial was checked symbolically as

`lambda(lambda-1)(lambda+1)(lambda^2-6)`.

Thus the spectrum is `{sqrt(6),1,0,-1,-sqrt(6)}`.

For `L={1,2,3}`, `R={4,5}`, the cross columns are `e1,e2`, so `w=e3`, `Pw=(1,2,0)`, and

`||w|| ||Pw||=sqrt(5)`.

Using fleet02/B09 constant

`C_KD=5*6^(3/5)/2^(11/10)=6.834830666196632...`,

the receiver gives

`C_KD*5^(-1/10)=5.818764209802524`.

## 5. Scope / correction audit

Checked that the report does **not** use any of the following invalid shortcuts:

- law-uniform pointwise quadratic-phase decay;
- independence after a spectral rotation;
- a uniformly good single physical triple/minor;
- arbitrary-joint rank-three coarea/projection density as a QFORM bound;
- deletion of a small coefficient residual as a small random quadratic error;
- square-root small-ball conversion at the final step.

The one-overlap theorem explicitly leaves a near-coloop branch rather than claiming it away. The unrestricted theorem and full-target continuity remain open.
