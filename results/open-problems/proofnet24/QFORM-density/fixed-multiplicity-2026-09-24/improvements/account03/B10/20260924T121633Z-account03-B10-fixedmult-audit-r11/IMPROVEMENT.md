# Same-threshold constant improvement: 10000 -> 4350

Run: `20260924T121633Z-account03-B10-fixedmult-audit-r11`  
Source theorem: `manuscript.tex` blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, initial commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`.

## Theorem

Under exactly the source manuscript's hypotheses — independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A` with `s_17(A)>=s>0`, arbitrary `b,c` — the same proof yields

`||p_(X^T A X+b^T X+c)||_infinity < 4350 K^2/s`.

No input assumption is changed. The conclusion is essential boundedness; this patch does not add global continuity and does not reduce the spectral multiplicity.

## 1. Improve the quarter-power coefficient

The source proof's Gaussian-smoothed small-ball coefficient is

`Cq = 2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)`.

We prove `Cq<35/8` by four elementary inequalities.

First,

`2^(5/8)<31/20`

because `31^8-32*20^8=33,691,037,441>0`.

Second,

`pi^(-1/4)<19/25`.

It suffices to use `pi>3`; the exact comparison

`3*19^4-25^4=338>0`

says `3>(25/19)^4`.

Third,

`e^(3/8)<22/15`.

Indeed

`e=sum_{k>=0}1/k! < 8/3 + (1/24)sum_{j>=0}5^{-j} = 87/32 < 11/4`,

where for `k>=4` the successive reciprocal-factorial ratio is at most `1/5` after the `1/4!` term. Moreover

`64*22^8-1331*15^8=100,848,484,429>0`,

so `(11/4)^3<(22/15)^8`.

Fourth,

`Gamma(3/8)<81/32`.

Split its integral at one. On `[0,1]`, `e^{-x}<=1-x+x^2/2`, hence

`integral_0^1 x^(-5/8)e^{-x} dx <= 8/3-8/11+4/19 = 1348/627`.

On `[1,infinity)`, `x^(-5/8)<=1`, so the tail is at most `e^{-1}<3/8`, since `e>8/3`. Therefore

`Gamma(3/8)<12665/5016<81/32`,

with exact margin `81/32-12665/5016=127/20064`.

Multiplication gives

`Cq < (31/20)(19/25)(22/15)(81/32)=174933/40000<35/8`,

and the final margin is `67/40000`.

Thus the source quarter-power lemma improves to

`P{|R-a|<rho} <= min(1,(35/8)(rho/L)^(1/4))`.

For `L>=1`, layer cake yields

`sup_a E log_+(1/|R-a|) <= 4+4 log(35/8) < 10`.

For the strict last inequality, `e>27/10`, while

`(27/10)^3-(35/8)^2=4339/8000>0`;

hence `35/8<e^(3/2)`.

## 2. Recompute every pivot half-potential branch

The scalar-pivot branch now satisfies

`H_scalar <= eta^(-1/2)(8+3*10)=10*38=380`.

The definite-pair branch is unchanged and remains `<160`.

For the indefinite-pair branch, the source gives exactly

`H_ind <= 10(32+4 log 16)+4/e`.

Use the elementary bounds `log16<14/5` and `4/e<3/2`. For the first, `e>27/10` and

`27^7-1024*10^7=220,353,203>0`,

so `e^7>2^10` and therefore `log2<7/10`. Hence `log16=4log2<14/5`. The second follows from `e>8/3`. Consequently

`H_ind < 10(32+56/5)+3/2 = 433.5 < 434`.

The no-pivot nine-direction branch is unchanged and has full half-potential `<200`. Therefore for every quadratic polynomial with `s_9(A)>=1`,

`H(Q)<434`,

and, adding the tail contribution bounded by one,

`sup_a E|Q-a|^(-1/2)<435`.

## 3. Recompute the main theorem

Normalize first to `K=s=1`, exactly as in the source.

- No pivot: density `<2400`.
- Scalar pivot: `|a_ii|^(-1/2)<=10` and the Schur remainder has at least nine large directions, so density `<10*435=4350`.
- Definite pair: density `<40`.
- Indefinite pair: the source's logarithmic branch is already far below 4350; the improved logarithmic potential only reduces it further.

Hence every normalized branch is `<4350`. Undoing the source scaling gives

`||p_Q||_infinity < 4350 K^2/s`.

If one keeps the unrounded dominant indefinite half-potential instead of replacing it by 434, the scalar-pivot branch is bounded by

`3210+400 log16+40/e = 4333.7506665...`,

but the integer 4350 follows from the elementary inequalities above without numerical transcendental evaluation.

## Scope

Status: **PROVED same-threshold improvement conditional only on the source theorem's already-audited lemmas.** It does not lower 17, does not solve the three-eigenvalue conjecture, and does not add a continuity conclusion to the pivot branches.
