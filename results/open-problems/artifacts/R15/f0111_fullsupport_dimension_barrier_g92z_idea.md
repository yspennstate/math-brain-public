# R15 idea first — projective block-size barrier for full-support two-block null directions

Date: 2026-09-19 UTC. Status: SELF_CHECK_ONLY / NOT CLAIMED. This is an idea/proof derivation written before any new checker.

Continue from `runs/R15/20260919_2056Z_successor_screen_f0111_projective_quartic_f91y.md`.

For the F0111 `k=2` hazard `F(t)=sum_i t_i-log S(t)`, `S(t)=sum_i exp(t_i)-(n-1)`, suppose an interior exact global quadratic certificate has a Hessian-null direction of full-support two-block form

`h = a 1_J - b 1_K`,  `J union K=[n]`,  `|J|=M`, `|K|=N`, `a>=b>0`.

Average the certificate over permutations inside `J` and inside `K`. This preserves nonnegative coefficients, global majorization, exact contact at a block-constant contact `q=(u on J, v on K)`, and the null direction. Thus we may assume block symmetry.

Put `m=(a+b)/2`, `delta=(a-b)/(a+b) in [0,1)`, `p=sum r_i h_i`, `z=p/m-delta`, and use the already-derived cubic-null curve. With `x=sum_{i in J} r_i`, `y=sum_{i in K}r_i`, and signed zero-atom mass `k=-(n-1)/S(q)`,

`k = 2 z(1-z^2)/((1-delta^2)(delta+3z))`,

`x = ((delta+z)(1+z)(1+delta+2z))/(2(1+delta)(delta+3z))`,

`y = ((delta+z)(1-z)(1-delta-2z))/(2(1-delta)(delta+3z))`.

For full support `k<0`, so after the prior fourth-order classification only the two outer regimes `z>1` and `z<-1` remain.

Write

`K2=((delta+z)(1-z^2))/(delta+3z)`,

`tJ=(1-z)^2-K2`, `tK=(1+z)^2-K2`,

and

`R=-2(delta+z)(1-z^2)(delta^2 z+3 delta z^2+delta+3 z^3)/(delta+3z)^2`.

Then `D_h^4 log S = m^4 R`, while the projective cubic covector `bvec(v)=D^3 log S[v,h,h]` has block sums

`bvec . 1_J = x m^2 tJ`,  `bvec . 1_K = y m^2 tK`.

The preceding projective theorem gives `D_h^4 log S >= 3 bvec^T H^+ bvec` for the contact Hessian `H>=0`, `Hh=0`. Since `bvec` annihilates `ker H`, Cauchy in the `H/H^+` pairing gives, for any `v`,

`bvec^T H^+ bvec >= (bvec.v)^2/(v^T H v)`.

For the block-symmetric certificate the within-J transverse eigenvalue is `r_J-beta_J>=0`, where `r_J=x/M`. Therefore

`1_J^T H 1_J <= x(M-x)`.

Likewise `1_K^T H 1_K <= y(N-y)`. Hence every such null contact necessarily satisfies

`M >= x(1+3 tJ^2/R)`,

`N >= y(1+3 tK^2/R)`.

Because `u,v>0` and full support gives `S=-(n-1)/k`,

`M < -x(n-1)/k`, `N < -y(n-1)/k`.

After cancellation,

`n-1 > QJ := -k(1+3 tJ^2/R)`,

`n-1 > QK := -k(1+3 tK^2/R)`.

The key remaining algebra is to prove two uniform one-variable barriers:

1. For `0<=delta<1`, `z>1`, `QK >= 256/9`, with equality only in the boundary limit `delta=1/2`, `z downarrow 1`.
2. For `0<=delta<1`, `z<-1`, `QJ >= 48`, with equality only in the boundary limit `delta=0`, `z uparrow -1`.

If these hold, then any full-support two-block Hessian-null exact global certificate must have

- `n>=30` on the `z>1` branch;
- `n>=50` on the `z<-1` branch.

In particular there is no full-support two-block Hessian-null first bifurcation in dimensions `n<=29`. This would strictly strengthen the previous elimination of one `n=4` test point and explain the numerical emergence of the first projective-feasible degeneration near `(delta,z,M,N)=(1/2,1,18,12)`.

For the algebraic proof, set `z=1+s`, `s>0`. After putting `QK-256/9` over its positive-sign denominator, the numerator reduces to a polynomial `P_+(delta,s)`. Its `s^0` coefficient factors as

`8(delta+3)(2delta-1)^2(4delta^2+12delta+11)`.

The `s^1` and `s^2` coefficient polynomials become coefficientwise positive after `delta=t/(1+t)` and clearing `(1+t)^degree`; coefficients for `s^3,...,s^6` are manifestly positive. Thus `P_+>0` for `s>0`.

For `z=-1-s`, the analogous numerator `P_-(delta,s)` for `QJ-48` has every `s^j` coefficient coefficientwise positive after the same `delta=t/(1+t)` substitution; the denominator sign is controlled by rewriting its final factor at `delta=1-r` as

`r^2 s+r^2+3rs^2+4rs+2r+3s^3+6s^2+4s`,

which is positive for `s>0`, `0<=delta<1`.

Next step: verify these symbolic identities exactly, archive only that algebraic self-check, then write the theorem proof in the immutable R15 report. No novelty or closure claim.