# B07 r13 — three-bank compiler for the threshold-eight two-sided collar

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T140521Z-fleet01-B07-fixedmult-audit-r13`  
Baseline manuscript pin: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **new supporting structural theorem; generic branch paid; threshold eight still OPEN**.

## 1. Input collar

Use the already checked threshold-eight terminal collar. Normalize `K=s=1`, keep

`eta=1/100`, `kappa=1/80^2=1/6400`.

Assume `A=A^T` has no `eta`-pivot and `s_8(A)>=1`. If `V_3(A)>=kappa^3`, the marginal-free physical `E_3` density receiver already pays the form. Thus consider the complementary branch. The collar theorem gives

`Xi_2(A) >= xi_* := (delta_*^2/2) kappa^2`,

where

`delta_*=(1-sqrt(18kappa)-eta)^2-(sqrt(eta^2+eta)+sqrt(18kappa))^2`

`=97/100-(297 sqrt(2)+3 sqrt(202))/4000`

`=0.85433514019113377...`,

and

`Xi_2(A)=sum det A[S,H]^2 det A[H,T]^2`,

summed over ordered pairwise-disjoint two-sets `S,H,T`.

Numerically

`xi_*=8.909772116276906e-9`.

The purpose here is to aggregate this repeated-middle-pair currency into one literal original-coordinate three-bank configuration before any small local minor is selected.

## 2. Three-bank random-color identity

Color every original coordinate independently and uniformly with one of three colors, giving a literal partition

`[n]=L disjoint_union M disjoint_union R`.

For each physical two-set `H subset M`, define

`b_H(L)=sum_{S subset L, |S|=2} det A[S,H]^2`,

`c_H(R)=sum_{T subset R, |T|=2} det A[H,T]^2`,

and

`Psi(L,M,R)=sum_{H subset M, |H|=2} b_H(L)c_H(R)`.

Expanding the product shows

`Psi=sum_{S subset L, H subset M, T subset R} det A[S,H]^2 det A[H,T]^2`,

where every displayed set has size two. For each ordered pairwise-disjoint triple `(S,H,T)` from `Xi_2`, the event `S subset L, H subset M, T subset R` has probability exactly

`3^(-6)=1/729`.

Therefore

`E Psi = Xi_2/729`.

Hence there exists one literal physical three-bank partition with

`boxed: Psi >= Xi_2/729 >= delta_*^2 kappa^2/1458.`                (2.1)

No dimension factor appears.

## 3. Exact second-compound interpretation

Put

`B=A[L,M]`,  `C=A[M,R]`.

For `H subset M`, `|H|=2`, Cauchy--Binet gives exactly

`b_H=det((B^T B)[H,H])`,

`c_H=det((C C^T)[H,H])`.

Consequently

`sum_H b_H = E_2(B):=e_2(BB^T)=e_2(B^TB)`,

`sum_H c_H = E_2(C):=e_2(CC^T)`.

Since `b_H,c_H>=0`,

`E_2(B) E_2(C)=(sum_H b_H)(sum_K c_K) >= sum_H b_H c_H=Psi`.       (3.1)

Thus the collar forces a common-middle second-compound overlap, not merely two unrelated volume statements.

Now form the actual physical cross block between the middle bank and the two outer banks,

`N=A[L union R,M]=[ B ; C^T ]`.

The complete order-two exterior volume of `N` contains, as nonnegative subfamilies, all two-row minors wholly in `L` and wholly in `R`. Hence

`E_2(N)>=E_2(B)+E_2(C)>=2 sqrt(E_2(B)E_2(C))>=2 sqrt(Psi)`.        (3.2)

Combining (2.1) and (3.2) gives the explicit dimension-free lower bound

`boxed: E_2(N) >= e_* := (sqrt(2) delta_* kappa)/27`               (3.3)

with

`e_*=6.99196957216563e-6`.

This is a literal original-coordinate cross block; no singular-vector random coordinates are introduced.

## 4. Generic third-volume branch is already paid

Let

`rho(N)=E_3(N)/E_2(N)^(3/2)`.

This quantity is scale-free. The independently reviewed marginal-free physical third-volume receiver says that every literal cross block with `E_3(N)>0` gives a continuous full-ambient density satisfying

`||p_Q||_infinity <= C_3 E_3(N)^(-1/6)`,

where

`C_3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`.

Therefore, if

`rho(N)>=1/64`,

then

`E_3(N)>=E_2(N)^(3/2)/64`

and

`||p_Q||_infinity
 <=2 C_3 E_2(N)^(-1/4)
 <=2 C_3 e_*^(-1/4)
 <576.342.`                                                       (4.1)

This branch has a continuous `C_0` density, and all same-bank quadratic terms, affine terms, outside couplings and additional spectrum remain present because the `E_3` receiver is a full-ambient physical-crossing theorem.

## 5. Sharpened threshold-eight frontier

Thus the no-pivot threshold-eight collar admits the following exhaustive funnel:

1. `V_3(A)>=kappa^3`: already paid by the standard order-three cut;
2. otherwise, there exists a literal three-bank partition `L,M,R` obeying the shared-middle packet (2.1) and the actual physical crossing lower bound (3.3); and then either
   - `rho(N)>=1/64`, in which case (4.1) pays the form with continuous density `<576.342`; or
   - `rho(N)<1/64`, while still
     `E_2(N)>=6.99196957216563e-6`
     and
     `Psi>=delta_*^2 kappa^2/1458`.

At the exact endpoint `E_3(N)=0`, the physical cross block `N` has rank at most two. For small but nonzero `rho`, this report deliberately calls the state **third-exterior-poor / second-exterior-rich**, not “near rank two” in operator or Frobenius norm; such a norm conclusion would require an additional argument and is not claimed.

The new remaining interface is therefore narrower than the raw repeated-anchor collar:

`QFORM-S8-E2-RICH-E3-POOR-SHARED-MIDDLE-RECEIVER-v1`:

> Pay a literal original-coordinate crossing `N=A[L union R,M]` with `E_2(N)>=e_*`, normalized third volume `E_3(N)/E_2(N)^(3/2)<1/64`, and the simultaneous common-middle compound overlap `Psi>=delta_*^2 kappa^2/1458`, while retaining arbitrary quadratic curvature in all three banks and arbitrary cap-one product laws.

This is not yet an eight-eigenvalue theorem. In particular, the existing one-linear-bank rank-two receiver cannot be invoked unless one physical source bank has exactly zero self-curvature; that hypothesis is not forced here. The result is a product-coordinate-safe aggregation/selection advance only.

## 6. Scope

- Arbitrary symmetric `A`: retained.
- Arbitrary dimension and spectrum outside the `s_8` assumption: retained.
- Arbitrary affine terms: retained by the full-ambient crossing receiver.
- Independent rough coordinate densities bounded by one: retained; general `K,s` follows by the standard scaling only after a complete threshold-eight receiver exists.
- No Gaussianity, log-concavity, moments, bounded support, diagonal basis, or post-rotation independence.
- Threshold 8: **OPEN**.
- Threshold 9: remains the lowest complete fixed-multiplicity theorem currently supported by two full reviews.
