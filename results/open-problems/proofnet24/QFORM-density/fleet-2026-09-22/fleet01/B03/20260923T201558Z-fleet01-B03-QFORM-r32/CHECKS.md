# Deterministic checks for B03 r32

These checks verify arithmetic and finite-dimensional identities only; they are not evidence for the unrestricted conjecture.

- `A0 = 8+8*pi*log(3/2) = 18.190449639356803`.
- `B0 = 4*pi*log(2) = 8.710344361214409`.
- With `r=2^(-1/2)`,
  `sqrt(A0)/(1-r)+sqrt(B0)*sqrt(r/(1-r)^3) = 30.218265050697436`.
- Hence `(1+S)/pi = 9.93708239514291 < 10` and the whole-time L1 coefficient before dividing by `2*pi` is `2(1+S)=62.43653010139487`.
- Monotonicity margin at the worst endpoint is
  `L(1)-4*pi = 5.624079024997631 > 0`; since `uL'(u)<4*pi`, this confirms `(L(u)/u)'<0` for every `u>=1`.

For the target-valid family

`Q_c=(X-cY1)^2+2Z1Y1+2Z2Y2`,

the coefficient matrix in order `(X,Y1,Z1,Y2,Z2)` is

```
[[1,-c,0,0,0],
 [-c,c^2,1,0,0],
 [0,1,0,0,0],
 [0,0,0,0,1],
 [0,0,0,1,0]].
```

The final 2x2 block has exact eigenvalues `+1,-1`, and the Rayleigh quotient of the first block at `e_X` equals `1`, so its largest eigenvalue is at least `1`. Thus the full matrix has at least three eigenvalues of modulus at least one for every real `c`.

As a numerical regression only, sampled `c=0,0.1,1,10,100` gave respectively at least `5,3,3,3,3` eigenvalues with modulus at least one (up to `1e-10` tolerance), agreeing with the exact argument.

CHECK STATUS: `QFORM_B03_RANDOM_CENTER_DYADIC_PASS`.
