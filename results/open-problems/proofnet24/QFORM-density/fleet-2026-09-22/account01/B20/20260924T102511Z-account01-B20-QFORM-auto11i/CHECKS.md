# Checks — account01/B20 r53 tiny-diagonal compiler

Run: `20260924T102511Z-account01-B20-QFORM-auto11i`.

All checks below are deterministic coefficient checks. No probabilistic simulation is used as proof.

## Constants

- `d=1/64=0.015625`.
- account02/B20 r52: `D0=9.530157744638501e-7`, `kappa0=6.075614261408114e-5`.
- `beta=d+kappa0=0.01568575614261408114`.
- `alpha=1007/4096=0.245849609375`.
- `sigma=63/64=0.984375`.

### Pair-gate slack

`beta^2-d^2-D0 = 9.4930499109152809126e-7 > 0`.

Thus an off-diagonal coefficient `|b|>=beta` in the all-tiny-diagonal chamber gives both `|det B|>D0` and, by Weyl, `s_min(B)>kappa0`, so the completed r52 indefinite-pair receiver fires.

### Diffuse-star atom slack

`beta^2/alpha^2 = 0.00407072601657810218... < 1/240 = 0.00416666666...`.

Equivalently

`alpha^2/240-beta^2 = 5.7988476921116547e-6 >0`.

Hence on a star of total squared mass `S>alpha^2`, every atom is `<S/240`, which is exactly what the fifteen-group greedy construction needs.

### S3 tetrad currency

`W_* = 3 sigma^2 (sigma^2-alpha^2)`
`    = 2.641145013694767840206623077392578125`.

Thus

`c2 = W_*/16`
`   = 0.1650715633559229900129139423370361328125`.

### E3 / rank-two collar

Using `zeta=2^-24`, the exterior-volume inequality gives

`sqrt(3 zeta/c2) = 0.00104079344223257228112...`.

The source-pinned physical-E3 theorem has

`C3=3*2^(4/3)*e^(1/3)=10.550168831164775...`,

so at `e3>=2^-24`,

`C3*(2^-24)^(-1/6) = 16*C3 = 168.8027012986364 <169`.

## Algebraic audit of the new S3 tetrad lemma

Let squared singular values satisfy `x1>=x2>=x3>=s=sigma^2`, and let `T=sum x_r`, `S=x1+x2+x3`, `R=T-S`.

For fixed `S`, the minimum of `x1x2+x1x3+x2x3` subject to `x1,x2,x3>=s` occurs at `(S-2s,s,s)` and equals `2sS-3s^2`.

The top-three/tail cross contribution is `S R >=3sR`, so

`e2 >= 2sS-3s^2+3sR = 3sT-sS-3s^2 >= 2sT-3s^2`.

Subtracting the non-disjoint minor contribution `<=rho^2 T` gives

`W2 >= (2s-rho^2)T-3s^2`.

When `rho<sigma`, `2s-rho^2>0`; since `T>=3s`,

`W2 >=3s(s-rho^2)`.

This is the claimed `QFORM-ZERODIAG-S3-TETRAD-LOWERBOUND-v1`.

## Exterior-volume inequality audit

For nonnegative sorted squared singular values `y1>=y2>=...`, put `Ttail=sum_{r>=3}yr`. Then

`3e3 = sum_{i<j} yi yj sum_{k!=i,j} yk`.

Because `yi+yj<=y1+y2`, every inner sum is at least `Ttail`. Therefore

`3e3 >= e2*Ttail`,

which is precisely

`dist_F(M,rank<=2)^2 * e2(MM^T) <= 3 e3(MM^T)`.

## Greedy fifteen-arm audit

If each star atom is `<S/240`, a group stopped at first mass `>=S/16` has mass `<S/16+S/240=S/15`. Fourteen completed groups consume `<14S/15`, leaving `>S/15>S/16`, so a fifteenth group can still be completed. Thus all fifteen groups exist and each has Euclidean arm norm at least `sqrt(S/16)=rho/4>alpha/4`.

No line above uses post-rotation independence, tail deletion, or an unproved density inequality.
