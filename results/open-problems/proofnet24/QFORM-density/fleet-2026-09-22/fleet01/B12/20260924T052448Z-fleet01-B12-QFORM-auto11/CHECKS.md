# Finite sanity checks — not part of the proof

The analytic proof is in `REPORT.md`. I additionally tested the relative-resonance-index inequality on 10,000 random full-column real matrices `M` (9 x 6), arbitrary dense additions `N`, and thresholds `a` sampled from `{0.25,0.5,0.75,1,1.25,1.5}`. For each sample I formed

`K=(M^T M)^(-1/2) M^T N (M^T M)^(-1/2)`,

set `r_a` equal to the number of eigenvalues of `Sym K` below `-1+a`, and checked

`s_(6-r_a)(M+N) >= a s_6(M)`

whenever `6-r_a>=1`. Violations: `0 / 10000`.

A separate 5,000-sample check of the exact stress family

`M1=2I_6+cJ_6`,
`B=diag(-t,p2,...,p6)`,
`M2=M1(I+B)`

with `t,pj>=0` verified `s_5(M2)>=sqrt(4+c^2)` in every sample. The exact proof is the relative-index theorem (and, for this diagonal family, direct singular-value calculation); the numerical experiment is only a consistency check.

Density constant used after `h+delta<=1/64`:

`5*sqrt(2e)/(127/64)=5.875008457567557...`.
