# r37 deterministic arithmetic and rank checks

Run: `20260923T210217Z-account01-B02-qform-auto11-r37`.

These checks use only exact formulas from `REPORT.md`; no simulation or probabilistic numerics enter the proof.

Let

- `C3=10.345084`,
- `E0=11907/16384=0.72674560546875`,
- `delta=2^-19=1.9073486328125e-6`,
- `zeta=2^-30=9.313225746154785e-10`.

Then

`(256/27)^(1/6)=1.4548315146289619`,

`C3*(256/27)^(1/6)=15.05035422468384`,

`2*pi*C3*(256/27)^(1/6)=94.56416453238171`.

The relative-second-scale product floor is

`P0=(1/64)*(63/64-delta)*E0^2
   =0.00812352625896906`.

The partner E3 threshold gives

`C3*zeta^(-1/6)=331.042688`,

`2*pi*C3*zeta^(-1/6)=2080.0025532908357`.

Failure implies

`T0=zeta/P0=1.1464511160867112e-7`,

`sqrt(T0)=0.0003385928404568991`,

`W0=(256/27)*zeta/P0=1.0870055026599928e-6`,

`2*sqrt(W0)=0.0020851911208903543`.

The global tail in the diagonal + rank-20 decomposition obeys

`eps0=sqrt(8*W0+2*T0)=0.002987529789725499`.

For the optional 23-coordinate core with `d=1/8`,

`d-23*eps0=0.05628681483631352>0`,

`2*sqrt(6*pi*23)/(d-23*eps0)=739.8399892431622<740`.

If fewer than 23 residual diagonal entries have magnitude `>=1/8`, absorbing them raises the carrier rank from at most 20 to at most 42 and leaves

`s3(R42) >=1-1/8-eps0=0.8720124702102745`.

## Deterministic rank bookkeeping

On each bank:

- `rank L0<=2`;
- `rank((L0+L0^T)/2)<=4`;
- at most two `ell_i>3/4`, so the matrix absorbing every row/column touching them has rank at most four;
- therefore the bank carrier has rank at most eight.

The symmetric off-diagonal carrier built from a rank-two crossing `M2` has rank at most four. Hence the global carrier rank is at most

`8+8+4=20`.

The residual Frobenius supports are block-orthogonal, hence

`||E0||_F^2=||EL||_F^2+||ER||_F^2+2||EM||_F^2`.

No probabilistic claim uses these numerical checks beyond the inequalities explicitly recorded in the report.
