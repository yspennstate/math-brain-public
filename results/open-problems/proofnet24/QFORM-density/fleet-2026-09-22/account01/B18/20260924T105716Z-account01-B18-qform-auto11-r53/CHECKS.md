# account01/B18 r53 checks

These are finite algebra/constant audits only; the proof is in `REPORT.md`.

## 1. Layer-cake constant

For `A>0`,

`int_0^infinity min(1,A z^(-3/2)) dz`

splits at `z0=A^(2/3)` and equals

`z0 + A*int_z0^infinity z^(-3/2)dz`
`=A^(2/3)+2A*A^(-1/3)=3A^(2/3)`.

With `A=2 M K/(|beta|sqrt(|gamma|))`, this is

`3(2MK)^(2/3)|beta^2 gamma|^(-1/3)`.

For `M=2`, `K=sqrt(2)`, `beta=gamma=1`, the constant is

`3*2^(5/3)=9.524406311809198...`.

## 2. Partner-splice crossing

Set

`A0=2sqrt(pi)=3.5449077018110318...`,
`B0=3*2^(5/3)=9.5244063118091979...`.

Solve on `(0,1)`

`A0 eta^(-1/2)=B0(1-eta)^(-1/3)`.

Numerically,

`eta_*=0.12657584480912131...`,

and the common value is

`9.9639035436760448...`.

Both branches have the stated monotonicities, so this is the maximum of their pointwise minimum on `(0,1)`.

## 3. Exact target-family spectrum

For

`H_eps=[[0,0,1,0],
        [0,0,0,eps],
        [1,0,0,0],
        [0,eps,0,1]]`,

a simultaneous permutation exposes blocks

`[[0,1],[1,0]]`, `[[0,eps],[eps,1]]`.

Hence

`spec(H_eps)={-1,1,(1+sqrt(1+4eps^2))/2,(1-sqrt(1+4eps^2))/2}`.

For `0<eps<1`, the positive root of the second block is `>1`, while the negative root has magnitude `<1`; therefore exactly three eigenvalues have modulus at least one and `s3(H_eps)=1`.

Numerical spot checks:

- `eps=1e-6`: approximately `[-1,-1e-12,1,1.000000000001]`;
- `eps=0.1`: `[-1,-0.00990195,1,1.00990195]`;
- `eps=0.5`: `[-1,-0.20710678,1,1.20710678]`;
- `eps=0.999`: `[-1,-0.61713965,1,1.61713965]`.

## 4. Deterministic currencies in the 2x2 right chamber

For

`H=[[0,D],[D^T,C2]]`, `D=diag(d1,d2)`, `C2=[[c,delta],[delta,gamma]]`,

subtracting `diag(0,C2)` (rank at most two) gives the symmetric cross matrix with operator norm `d1`. Therefore `s3(H)<=d1`.

The completed account02/B18 funnel gives `s3(H)<=d2+||P_v C2 P_v||`; in the SVD-aligned two-dimensional right frame `P_v C2 P_v` is the scalar `gamma`, so `|gamma|>=(s3(H)-d2)_+`.
