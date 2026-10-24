# Deterministic checks — account01/B09 r33

Run: `20260924T081556Z-account01-B09-QFORM-auto11-r33`.

These are finite regressions only; the universal claims in `REPORT.md` are proved algebraically there.

## 1. Cyclic 2x2 crossing identity

Seed `20260924`. QR-orthonormalize a random `6 x 2` Gaussian matrix to obtain orthonormal physical vectors `v,z`. Set

`mu=0.7`, `theta=1.3`, `lambda=-2.2`, `c=mu v+theta z`, and `S={0,1,2}`.

For each distinguished `i in S`, with `{j,k}=S\{i}`, form

`C_i=[[c_j,c_k],[lambda v_i v_j,lambda v_i v_k]]`.

The direct determinants and the formula

`-lambda theta v_i (v_j z_k-v_k z_j)`

were:

- `i=0`: direct `-0.08961279060000658`, formula `-0.08961279060000657`, error `1.39e-17`;
- `i=1`: direct `0.05260242370745902`, formula `0.05260242370745902`, error `0`;
- `i=2`: direct `0.14221521430746560`, formula `0.14221521430746556`, error `2.78e-17`.

The sum of direct determinant squares was

`0.031022634399538042`,

while

`lambda^2 theta^2 sum_i v_i^2 Delta_(S\i)^2`

equaled

`0.031022634399538035`.

## 2. EKR constants used in the compiler

At `rho=1/512`,

`tau=(rho/2)^(1/3)=0.09921256574801247`.

The triangle-mass lower threshold is

`t0=1-rho-tau/(1-tau)=0.8879070551318439`.

With `eta=3/4`,

`t0(t0-eta)=0.12244864720402032`.

Hence one of the three cyclic crossing determinants has magnitude at least

`sqrt(t0(t0-eta)/3) |lambda theta| = 0.202030... |lambda theta|`.

## 3. Partner application

For

`Q_*=2(U+V)^2+2 U Y0+2 V Y1+4((Z1+Z2)/sqrt(2))^2`,

the active coefficient matrix in the orthonormal bookkeeping basis `(U,V,Y0,Y1,q)` is

`[[2,2,1,0,0],
  [2,2,0,1,0],
  [1,0,0,0,0],
  [0,1,0,0,0],
  [0,0,0,0,4]]`.

Its exact eigenvalues are

`{1,-1,2-sqrt(5),2+sqrt(5),4}`.

Thus at least four have modulus at least one.

The account02/B09 r19 constant is

`6*4^(-1/3)=3.77976314968462`.

The mixed rows

`(0,1,0)`, `(0,0,1)`, `(1/sqrt(2),0,0)`, `(1/sqrt(2),0,0)`

have Gram exactly `I_3`. Under `diag(1,1/2,1/2)`, all four augmented leverages are exactly `1/2`.
