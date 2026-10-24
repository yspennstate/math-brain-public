# Checks — account01/B03 r33

These are deterministic algebra/constant checks for `REPORT.md`; they are not numerical evidence for the unrestricted conjecture.

## 1. Weighted-selector step: exact density calculation

The retained square-energy factor is justified as follows. Define the complex density on coefficient space

`q_t(c)=p_C(c) E[ exp(i t R(W)) G_{h(W)}(t) | C=c ]`.

Then

`|q_t(c)|^2
 <= p_C(c)^2 E[|G_h(t)|^2 | C=c]
 <= M_C p_C(c) E[|G_h(t)|^2 | C=c]`.

Therefore

`||q_t||_2^2 <= M_C E|G_h(t)|^2 = M_C H(t)`.

Applying the account02/B03 whole-selector Plancherel calculation to `q_t` gives exactly

`|phi_Q(t)|^2 <= M_Z pi^2 |det B|^-1 |t|^-2 ||q_t||_2^2
 <= K^2 |t|^-2 H(t)`.

Thus the `H(t)` factor in the report is not obtained by an invalid pointwise factorization or conditional density cap; it is an `L^2(dc)` bound on the weighted coefficient density.

## 2. Dyadic block coefficient

For `T_j=2^jT_0`,

`int_(T_j)^(2T_j) t^-2 dt = 1/(2T_j)`.

Combining with

`int_(T_j)^(2T_j) H(t)dt <= D^-1 L(DT_j)`

gives

`int_(T_j)^(2T_j)|phi_Q(t)|dt
 <= K /sqrt(2DT_j) sqrt(L(DT_j))`

`= K/(sqrt(2DT_0)) 2^(-j/2) sqrt(L(2^j y))`,

where `y=DT_0`. This confirms the extra factor `1/sqrt(2)` used in the r33 improvement.

## 3. Geometric sums and constants

Let `r=2^(-1/2)`. Exact identities:

`sum_(j>=0) r^j = 1/(1-r)=2+sqrt(2)=3.414213562373096...`

and, using `sqrt(j)<=(j+1)/2`,

`sum_(j>=1) sqrt(j)r^j
 <=(1/2)[r/(1-r)^2+r/(1-r)]`

`=(5+4sqrt(2))/2=5.328427124746193...`.

Further,

`L_0=8+8pi log(3/2)=18.190449639356803...`,

`C_*=(2+sqrt(2))*sqrt(L_0)
    +((5+4sqrt(2))/2)*sqrt(4pi log2)`

`=30.28765360446826...`,

and

`A=1/pi+C_*/(pi sqrt(2))
  =7.1354270657381305... <7.14`.

The associated two-sided `L^1` coefficient is

`2pi A=44.83321049989737...`.

## 4. Choice of optimization scale

For `kappa>=1`, set

`y=kappa^(2/3)(1+log kappa)^(1/3)`.

Then

`log y=(2/3)log kappa +(1/3)log(1+log kappa)`.

Since `log(1+u)<=u` for `u>=0`, `log y<=log kappa`; hence

`y^-1/2 sqrt(1+log y)
 <= kappa^-1/3 (1+log kappa)^(1/3)`.

Multiplying by `kappa` produces exactly the same scale as the first term:

`kappa y^-1/2 sqrt(1+log y)
 <= kappa^(2/3)(1+log kappa)^(1/3)`.

For `kappa<=1`, `y=1` gives a constant `D^-1` bound.

## 5. Stress-test spectrum

For

`Q_eps=X^2+2eps(Z1Y1+Z2Y2)+2Y1Y3`,

the `(Z1,Y1,Y3)` matrix is

`[[0,eps,0],[eps,0,1],[0,1,0]]`.

Its characteristic polynomial is

`-lambda(lambda^2-(1+eps^2))`,

so its eigenvalues are

`0, +sqrt(1+eps^2), -sqrt(1+eps^2)`.

The `(Z2,Y2)` block is `[[0,eps],[eps,0]]`, with eigenvalues `+eps,-eps`, and the `X` block contributes `1`. Thus the full spectrum contains

`1, +sqrt(1+eps^2), -sqrt(1+eps^2), +eps, -eps, 0`,

so the owner target holds for every `0<eps<=1`.

With `B=eps I_2` and unit joint density caps,

`K=pi/sqrt(|det(eps I_2)|)=pi/eps`.

The r33 bound is therefore

`<7.14 (pi/eps)^(2/3)(1+log(pi/eps))^(1/3)`,

whereas r32 gives `10pi/eps`; the ratio is

`<0.714 pi^(-1/3) eps^(1/3)(1+log(pi/eps))^(1/3) ->0`.

## 6. Whole-copy collision integral

For `|phi(t)|^2<=min(1,K^2t^-2)`,

`2 int_0^K t^-1/2 dt =4sqrt(K)`,

`2K^2 int_K^infinity t^-5/2 dt=(4/3)sqrt(K)`,

sum `=(16/3)sqrt(K)`.

This calculation concerns the independent copy of the whole scalar Q and does not manipulate coordinatewise sums/differences.
