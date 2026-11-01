# Optimizing the single-edge spectral ledger

Date: 2026-08-16  
Status: exact parameter optimization and interpolation bound proved; the FPP inputs remain open  
Companion: `SINGLE_EDGE_WEIGHTED_ENGINE_20260816.md`, SHA-256
`006e1baea140b92672cae7336f174283162560464e37b0cddd11e436e88503d0`

The weighted single-edge ledger contains two free parameters: the noise split
`kappa` and the spectral cutoff `r`.  Their joint cost can be optimized
explicitly.  The outside-uncertainty coefficient falls like
`(log r)/r`, while the conditional-revealment coefficient grows like `r^2`.
Consequently the best error has the interpolation scale

`A^(2/3) B^(1/3) (log(A/B))^(2/3).`                         (1)

This is an algebraic reduction, not a variance theorem: it still requires
estimates for the squared edge influences, route uncertainty, and weighted
outside revealment.

## 1. Starting ledger

Use the notation of the companion and put

`I=sum_e p_e^2,       R=sum_e r_e,       B=D_z,`            (2)

where

`r_e=E[Var(1_(e in gamma)|w_e)].`                           (3)

Define the nonnegative scaled quantities

`T=I/(9 alpha^2),       A=64 R/(729 alpha^2).`              (4)

The independently audited weighted ledger is, for every integer `r>=2` and
`0<kappa<1`,

`Var(X_(Mn))
 <=T(1+kappa)+A[kappa+(1-kappa)^r]
   +[r(r-1)/2]B.`                                           (5)

Boundary choices of `kappa` below are understood by taking one-sided limits;
(5) is continuous in `kappa`.

## 2. Exact minimizer of the uncertainty coefficient

First ignore the small target inflation `T kappa` and set

`mu_r(kappa)=kappa+(1-kappa)^r.`                            (6)

This strictly convex function has the unique minimizer

`kappa_r=1-r^(-1/(r-1)),`                                  (7)

and

`mu_r^*=1-[(r-1)/r]r^(-1/(r-1)).`                          (8)

Indeed, `mu_r'=1-r(1-kappa)^(r-1)`.  With

`x=(log r)/(r-1)`                                           (9)

and `r^(-1/(r-1))=exp(-x)`, the elementary inequalities
`1-x<=exp(-x)<=1-x/2` for `0<=x<=1` give

`(log r)/(2(r-1)) <= kappa_r <= (log r)/(r-1),`             (10)

and

`mu_r^* <=(1+log r)/r.`                                    (11)

The last bound follows directly from

`1-[(r-1)/r]exp(-x)
 <=1/r+[(r-1)/r]x=(1+log r)/r.`                            (12)

Thus the uncertainty cost tends to zero, while the target coefficient
`1+kappa_r` tends to one.  Also `1+kappa_r<=3/2` for every `r>=2`, since
`r<=2^(r-1)`.

## 3. Exact fixed-r optimizer for the full non-revealment cost

For fixed `r`, the part of (5) above the baseline `T` and before revealment is

`F_r(kappa)=(T+A)kappa+A(1-kappa)^r.`                       (13)

If `Ar<=T+A`, its infimum is the boundary value `F_r(0)=A`.  If
`Ar>T+A`, its unique interior minimizer is

`kappa_(r,T,A)
 =1-[(T+A)/(Ar)]^(1/(r-1)),`                               (14)

and the exact minimum is

`F_r^*=(T+A){1-(1-1/r)[(T+A)/(Ar)]^(1/(r-1))}.`            (15)

To verify (15), write `q=[(T+A)/(Ar)]^(1/(r-1))`.  At the
critical point, `Aq^r=q(T+A)/r`, so

`(T+A)(1-q)+Aq^r
 =(T+A)[1-(1-1/r)q].`                                      (16)

This exact formula is useful when the relative sizes of `T` and `A` are
known.  It also shows why minimizing `mu_r` alone is not always the exact
choice: a large target term pushes `kappa` toward zero.

## 4. A parameter-free upper interpolation

For a uniform bound that needs no comparison between `T` and `A`, use the
choice (7) in (5).  Since `kappa_r<=mu_r^*`, equation (11) gives the sharper
one-line estimate

`T kappa_r+A mu_r^*
 <=(T+A)mu_r^*
 <=S(1+log r)/r,`                                          (17)

where

`S=T+A.`                                                    (18)

Therefore, for every integer `r>=2`,

`Var(X_(Mn))
 <=T+S(1+log r)/r+(r^2/2)B.`                               (19)

Suppose `0<B<<S`, put

`L=1+log(S/B),       R_0=[(S/B)L]^(1/3),`                  (20)

and choose

`r_0=max{2,ceil(R_0)}.`                                    (21)

For `S/B` sufficiently large, `R_0<=r_0<=2R_0` and
`1+log r_0<=2L`.  Substitution in (19) yields the explicit bound

`Var(X_(Mn))
 <=T+4 S^(2/3) B^(1/3) [1+log(S/B)]^(2/3).`                (22)

Both terms have the same scale because

`S L/R_0=B R_0^2
 =S^(2/3)B^(1/3)L^(2/3).`                                  (23)

When `B=0`, take `r->infinity` in (19) to obtain simply

`Var(X_(Mn))<=T.`                                           (24)

For the isolated uncertainty--revealment pair, the logarithmic scale is sharp
up to absolute constants:

`inf_(integer r>=2){A mu_r^*+[r(r-1)/2]B}
 asymp A^(2/3)B^(1/3)[log(A/B)]^(2/3)`                     (25)

as `A/B->infinity`.  The lower bound follows from
`mu_r^*>=(log r)/(2r)` and `r(r-1)/2>=r^2/4`, splitting at
`r` of order `[(A/B)log(A/B)]^(1/3)`.

## 5. Meaning for the FPP route

Equation (22) isolates the sufficient asymptotic obligation.  If the squared
edge-influence term `T` is already below the desired recurrence constant and

`B/S ->0`                                                   (26)

fast enough that the second term in (22) fits the remaining margin, then the
spectral parameters can be chosen without a further constant loss.  The best
cutoff grows at the audited scale

`r asymp[(S/B)log(S/B)]^(1/3),`                            (27)

and `kappa` is only of order `(log r)/r`.

No estimate of (26) follows from this optimization.  In particular, the
available deterministic path-length bound on `R` does not force `B/S` small,
and the straight-path control has maximal route stability.  The remaining
probabilistic problem is to construct conditional decision procedures whose
variance-weighted outside revealment is genuinely below the combined
single-edge mass.

## 6. Break checks

1. The baseline in (5) is `T`; only `T kappa` is optimized.  Absorbing all of
   `T(1+kappa)` into the interpolation term would lose the target scale.
2. The exact full optimizer has a boundary regime `Ar<=T+A`.  Formula (14)
   must not be used there.
3. The logarithm in (22) has exponent `2/3`, not `1/3`: the optimizer solves
   `r^3` of order `(S/B)log r`.
4. The integer ceiling changes only the displayed absolute constant when
   `S/B` is large.  For bounded `S/B`, use (19) directly, for example with
   `r=2`.
5. Equation (24) is a limiting statement over finite `r`; it does not assert
   the existence of an infinite-level decision algorithm.
6. This note optimizes a valid upper ledger.  It does not turn `R`, `B`, or
   `I` into known FPP estimates.

An independent referee should verify (14)--(16), both inequalities in (17),
the choice (20)--(23), and the boundary cases before this optimization is used
in a bootstrap argument.
