# Two-sided Pluecker-entropy cross-block smoothing with arbitrary self phases

This addendum contains the strongest result of run `a01-b07-20260922T143228Z-qform-r12b`.

**Status:** `NEW SUPPORTING THEOREM / FULL TARGET OPEN`.

## 1. Statement

Let `A` be an arbitrary real symmetric `n x n` matrix and `X_1,...,X_n` independent real random variables with densities bounded by one. Let `I,J` be disjoint sets of ORIGINAL coordinates and put

`B=A[I,J]`.

Assume `rank(B)=3` and take a thin SVD

`B=L Sigma R^T`,

where `L in R^{|I| x 3}`, `R in R^{|J| x 3}` have orthonormal columns and `Sigma` is invertible `3 x 3` diagonal with positive entries.

For coordinate triples `K subset I`, `H subset J`, define the left/right Pluecker laws

`w^L_K=det(L_K)^2`, `w^R_H=det(R_H)^2`.

Each is a probability law by Cauchy--Binet.

More generally, let `pi_L,pi_R` be probability laws supported on nonzero coordinate bases of `L,R`, with inclusion marginals at most `1/2`, and put

`D_L=D(pi_L||w^L)`, `D_R=D(pi_R||w^R)`.

Then the law of

`Q=X^T A X`

has a continuous density vanishing at infinity and

`boxed{ ||p_Q||_infinity <= 3 e |det Sigma|^(-1/3)
       exp((D_L+D_R)/6). }`                                              (1.1)

In particular, define the disjoint-basis masses

`delta_L=sum_{K cap K'=empty} w^L_K w^L_K'`,

`delta_R=sum_{H cap H'=empty} w^R_H w^R_H'`.

If both are positive, conditioning two iid Pluecker bases on disjointness gives the partner entropy bounds `D_L<=log(1/delta_L)`, `D_R<=log(1/delta_R)`, and therefore

`boxed{ ||p_Q||_infinity <=
        3 e |det Sigma|^(-1/3) (delta_L delta_R)^(-1/6). }`                (1.2)

There are **no assumptions on** `A[I,I]`, `A[J,J]`, coordinates outside `I union J`, their couplings to `I,J`, signs of the spectrum, moments, support geometry, or additional eigenvalues. All of those enter only through arbitrary conditional self phases eliminated by the first Cauchy--Schwarz step.

This is therefore a genuine arbitrary-residual upgrade of the assigned partner's exact-rank/separable-phase determinant-weighted mechanism.

## 2. Dependency from the assigned partner

The only nontrivial imported analytic input is account02/B07's proved entropy-basis lemma, canonical source

`yspennstate/math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T123512Z-b07-qform-minors-11/REPORT.md`.

For any `N x 3` matrix `U` with orthonormal columns, Pluecker weights `w_K=det(U_K)^2`, and any basis law `pi` with inclusion marginals `p_i<=1/2`, that result proves

`int_{R^3} prod_i |hat f_i(<u_i,xi>)| dxi
 <=(2pi)^3 e^(3/2) exp(D(pi||w)/2)`                                    (2.1)

for arbitrary cap-one probability densities `f_i` (and even coordinate-separable phases).

It also proves that conditioning two iid `w`-bases on disjointness yields a basis law with all marginals at most `1/2` and entropy at most `log(1/delta)`.

## 3. First Cauchy--Schwarz: arbitrary self phases disappear

Condition on every coordinate outside `I union J`. For the remaining original coordinates write the conditional quadratic form as

`q_I(X_I)+q_J(X_J)+2 X_I^T B X_J+c`,                                  (3.1)

where `q_I,q_J` include arbitrary within-block quadratic and induced linear terms.

The regularized-determinant argument already proves the exact Cauchy--Schwarz reduction

`|phi(t)|^2
 <= E_D prod_{i in I}|hat f_i(2t [B D]_i)|`,                          (3.2)

where `D=X_J-X_J'` is a coordinatewise difference of two independent copies. Its coordinates remain independent. Each difference density

`g_j=f_j * tilde f_j`

is a probability density and satisfies

`||g_j||_infinity<=||f_j||_infinity ||f_j||_1<=1`.                     (3.3)

Equation (3.2) is uniform in the initially conditioned outside coordinates. Thus it suffices to estimate its right side.

## 4. Right singular frame: bounded density of the difference projection

Write the thin SVD `B=L Sigma R^T` and set

`Z=R^T D in R^3`.

Apply (2.1) to the orthonormal-column frame `R` and the independent cap-one difference densities `g_j`. Fourier inversion gives a continuous density `h_Z` satisfying

`||h_Z||_infinity
 <= e^(3/2) exp(D_R/2).`                                                (4.1)

Indeed (2.1) bounds `||hat h_Z||_1` by `(2pi)^3` times the right side of (4.1).

Therefore, since `BD=L Sigma Z`, (3.2) yields

`|phi(t)|^2
 <= e^(3/2) exp(D_R/2)
    int_{R^3} prod_{i in I}|hat f_i(2t <l_i,Sigma z>)| dz`.              (4.2)

No independence between the three coordinates of `Z` is asserted or needed.

## 5. Left singular frame: determinant-weighted Fourier L1

For `t!=0`, make the invertible change of variables

`x=2t Sigma z`.

Then

`dz = [8 |t|^3 |det Sigma|]^(-1) dx`.                                  (5.1)

Apply (2.1) to the left frame `L` and the original cap-one densities `f_i`:

`int_{R^3} prod_{i in I}|hat f_i(<l_i,x>)| dx
 <=(2pi)^3 e^(3/2) exp(D_L/2).`                                        (5.2)

Substituting (5.1)--(5.2) into (4.2),

`|phi(t)|^2
 <= [e^3 pi^3 exp((D_L+D_R)/2)]
    /[|t|^3 |det Sigma|].`                                             (5.3)

Hence

`|phi(t)|
 <= K |t|^(-3/2),`                                                     (5.4)

where

`K=e^(3/2) pi^(3/2) |det Sigma|^(-1/2)
   exp((D_L+D_R)/4).`                                                  (5.5)

Together with `|phi(t)|<=1`, this is an integrable characteristic-function envelope.

## 6. Fourier inversion and exact constant

The crossover between `1` and `K t^(-3/2)` is

`t_0=K^(2/3)`.

Therefore

`int_R min(1,K|t|^(-3/2))dt
 =2[t_0+int_{t_0}^infinity K t^(-3/2)dt]
 =6 K^(2/3).`                                                          (6.1)

Fourier inversion gives

`||p_Q||_infinity <= (1/(2pi)) 6K^(2/3)
 =3 e |det Sigma|^(-1/3) exp((D_L+D_R)/6),`                            (6.2)

which is (1.1). Since `phi in L^1`, the inverse Fourier transform is a continuous density vanishing at infinity.

Conditioning outside `I union J` caused no dependence of the bound on the conditioned values, so averaging restores the same bound for the full `Q`.

For the disjoint-basis choice, insert

`D_L<=log(1/delta_L)`, `D_R<=log(1/delta_R)`

into (6.2) to obtain (1.2).

## 7. Exact minor interpretation

Because `rank(B)=3`,

`P_3(B):=e_3(BB^T)=|det Sigma|^2
       =sum_{|K|=|H|=3} det(B[K,H])^2`.                                (7.1)

Moreover every `3 x 3` cross minor factors exactly as

`det(B[K,H])^2
 =|det Sigma|^2 w^L_K w^R_H`.                                          (7.2)

Thus the theorem is genuinely determinant weighted. Equation (1.2) may be written

`||p_Q||_infinity
 <=3e [P_3(B) delta_L delta_R]^(-1/6).`                                 (7.3)

The quantity `P_3(B)` measures total third cross-minor mass, while `delta_L,delta_R` measure whether that mass is distributed across disjoint physical coordinate bases on both sides. A single large minor is neither assumed nor sufficient.

## 8. Relation to the previous leverage gate

The regularized-determinant theorem gives the same desired `|t|^(-3/2)` exponent from three cross singular directions when one physical side has projection leverage at most `1/2`. The six-row paired-frame control from account01/B07's preceding run shows a rank-three cross cut can have substantial aggregate determinant mass while every coordinate leverage is one, so a one-cut leverage criterion is not exhaustive.

The present theorem replaces pointwise leverage by a **two-sided determinant-distribution condition**. It is useful exactly when neither side is dominated by common-coordinate bases: disjoint Pluecker mass pays the Fourier exponents through entropy rather than through maximum leverage.

Unlike the earlier assigned-partner theorem, this proof permits arbitrary nonseparable quadratic self phases because the first Cauchy--Schwarz step removes them before the two entropy estimates are applied.

## 9. Remaining selection problem

The full QFORM conjecture would follow on any branch where the three-large-eigenvalue hypothesis can produce a physical rank-three cross block satisfying

`P_3(B) delta_L delta_R >= c>0`                                        (9.1)

for a universal `c`; then (7.3) gives a universal continuous-density bound.

That implication is false if interpreted as one universal fixed cross cut without an alternative branch: localized/near-coloop frames can have vanishing disjointness mass, and existing source-valid examples show that a single cross-rank-three selection need not exist. The correct next step is therefore an exhaustive determinant-weighted dichotomy:

* two-sided disjoint cross-minor mass satisfying (9.1), paid by this theorem; or
* a localized heavy physical row/triple, paid by the nonisotropic-pivot theorem unless its Rayleigh quotient is near zero; or
* the quantitatively strong hyperbolic-bank branch isolated in this run's `REPORT.md`.

This is a narrower structural obligation than the previous arbitrary nonseparable-residual debt: the nonseparable phase is now fully paid on the two-sided diffuse cross-block branch.

## 10. Classification

`NEW SUPPORTING THEOREM / FULL TARGET OPEN`.

The full arbitrary-matrix three-large-eigenvalue conjecture is not claimed. The theorem does prove both an essentially bounded density and continuity on its exact stated branch.
