# Deterministic checks for account01/B03 r43

These checks are secondary to the analytic proof in `REPORT.md`; no numerical experiment is used as proof of a universal claim.

## 1. Fourier/Plancherel normalization

With `hat h(xi)=int h(u)e^(i xi.u)du`, Plancherel is

`int |hat h(xi)|^2 dxi=(2pi)^r int |h(u)|^2du`.

For `F_t(z)=hat h(2tz)`, the substitution `xi=2tz` gives

`int |F_t(z)|^2dz=(2|t|)^(-r)(2pi)^r int|h|^2=pi^r |t|^(-r) int|h|^2`.

Since `f_U<=1` and `int f_U=1`, `int f_U^2<=1`, giving the normalization used in (2.10).

## 2. Crossover and weighted integrals

Let

`B=pi^(d/2)(K_LK_M)^(1/2)`,
`T=B^(2/d)=pi(K_LK_M)^(1/d)`.

Then the envelope is `|phi|^2<=min(1,B t^(-d/2))` for `t>0`.

Negative-half:

`2 int_0^T t^(-1/2)dt =4T^(1/2)`,

`2B int_T^infinity t^(-(d+1)/2)dt =4/(d-1) T^(1/2)`,

sum `=4d/(d-1) T^(1/2)`.

Positive-half (`d>3`):

`2 int_0^T t^(1/2)dt =4/3 T^(3/2)`,

`2B int_T^infinity t^(-(d-1)/2)dt =4/(d-3) T^(3/2)`,

sum `=4d/[3(d-3)] T^(3/2)`.

One-copy L1 (`d>4`):

`2 int_0^T 1 dt=2T`,

`2B^(1/2)int_T^infinity t^(-d/4)dt=8/(d-4)T`,

sum `=2d/(d-4)T`; dividing by `2pi` gives `d/(d-4)(K_LK_M)^(1/d)`.

## 3. Partner splice constant

The account02/B03 r52 compiler is

`||p_Q||_inf <=(2pi)^(-1)(E A_-)^(1/2)(E A_+)^(1/2)`.

Insert

`E A_- <=8sqrt(pi) A`, where `A=E sqrt(M_-/|gamma|)`,

and

`E A_+ <=C_d pi^(3/2) B`, where
`C_d=4d/[3(d-3)]`,
`B=E (K_LK_M)^(3/(2d))`.

Then

`(2pi)^(-1)sqrt(8sqrt(pi) * C_d pi^(3/2))=sqrt(2C_d)`
`=sqrt(8d/[3(d-3)])`.

At `d=4`, this is

`sqrt(32/3)=4sqrt(2/3)=3.265986323710904...`.

## 4. Exact-target critical family matrix

Order the variables as

`(H0,Z,W,U1,V1,Y1,U2,V2,Y2)`.

The symmetric coefficient matrix for

`Q_*=2H0(Z+W)+2U1(Y1+W)+2U2Y2+2V1Y1+2V2Y2+2U1V1+2U2V2`

has unit entries at the undirected edges

`H0-Z, H0-W, U1-W, U1-Y1, V1-Y1, U1-V1, U2-Y2, V2-Y2, U2-V2`

and zeros elsewhere.

The principal submatrix on `(U1,V1,Y1,U2,V2,Y2)` is `K3 adjacency direct_sum K3 adjacency`, hence has spectrum exactly

`{2,2,-1,-1,-1,-1}`.

Cauchy interlacing therefore proves, without numerics, that the full 9x9 matrix has at least two eigenvalues `>=2` and at least one eigenvalue `<=-1`.

As a finite sanity check only, direct symbolic/numeric diagonalization of the full 9x9 matrix gives eigenvalues approximately

`2.2283282159, 2, 1.3604093371, 0.1858853464, -1, -1, -1, -1, -1.7746228995`,

consistent with the interlacing proof.

## 5. Dense-cross family spectral perturbation

At `E=0`, the hub-to-Y crossing matrix has singular values `sqrt(2),sqrt(2),1`, so the symmetric bipartite matrix has nonzero spectrum

`+sqrt(2),+sqrt(2),+1,-1,-sqrt(2),-sqrt(2)`.

For `E=(1/10)J_(3x2)`,

`||E||_op=(1/10)||J_(3x2)||_op=sqrt(6)/10=0.2449489742783178...`.

Hence

`sqrt(2)-sqrt(6)/10=1.169264...>1`.

Weyl therefore leaves at least two eigenvalues `>1` and two `<-1`.

## 6. Whole-copy constants for Q_*

Direct negative-half budget:

`8sqrt(pi)=14.179630807244127...`.

Riesz conversion:

`8sqrt(pi)/sqrt(2pi)=4sqrt(2)=5.656854249492381...`.

With `M=4sqrt(2/3)=3.265986323710904...`, the posterior cap-to-half-Riesz bound is

`2sqrt(2M)=4sqrt(2)(2/3)^(1/4)=5.111544833970179...`.

Multiplication by `sqrt(2pi)` gives

`8sqrt(pi)(2/3)^(1/4)=12.812742807873674...`.

The difference density cap is at most `M`, so

`P(|Q_*-Q_*'|<=epsilon)<=2M epsilon=6.531972647421808... epsilon`.

## 7. Assumption audit

- no moment assumptions;
- no compactness or connectedness assumptions;
- no Gaussian or log-concave assumption;
- no diagonalization of the input law;
- no conditional density cap for one shared slope given another;
- no separation/independence assertion for coordinatewise copy sums and differences;
- no pointwise van-der-Corput bound;
- no use of Monte Carlo or histogram evidence.

Scoped privacy check: mathematical/control-source content only; no credentials, tokens, scheduler IDs, signed download URLs, unrelated private data or public-release action.
