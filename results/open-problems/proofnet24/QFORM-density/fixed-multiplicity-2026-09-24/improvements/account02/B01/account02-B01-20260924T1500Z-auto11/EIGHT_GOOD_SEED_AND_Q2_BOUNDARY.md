# Eight-direction good-seed refinement and a sharp q=2 density obstruction

Run: `account02-B01-20260924T1500Z-auto11`  
Source theorem consumed: spectral-tail/overlap theorem in the pinned nine-eigenvalue source `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`.

Status: **proved structural improvement + proved counterexample to a tempting analytic shortcut; NOT an eight-eigenvalue density theorem.**

## 1. A dimension-free good-seed inequality in the unresolved s8 chamber

Assume the normalized no-pivot chamber of the nine paper, with

`d=3/40`, `p=1/400`, `h=2/25`, `kappa=h^2=4/625`,

and assume `s_8(A)>=1`. If `V_3>=kappa^3`, the existing disjoint order-three receiver already pays the form. Thus consider the only unresolved branch

`V_3<kappa^3`.

The no-pivot spectral-to-volume proposition at order two gives `V_2>=kappa^2`, hence

`r:=V_3/V_2 < kappa`.

Sample each invertible disjoint two-seed `(S,T)` with probability `det(A_{S,T})^2/V_2`, and form the completion

`A=D+R+E`

used in the overlap theorem. The proof of that theorem gives the exact/one-sided expectations

`E_seed ||D||_F^2 = W^cross_{2,1}(A)/V_2`,

`E_seed ||E||_F^2 <= 9 V_3/V_2 = 9r`.

Since `s_8(A)>=1`, the overlap corollary gives

`W^cross_{2,1}(A)/V_2 >= 2-9r`.

Therefore, for every `c>=0`,

`E_seed[ ||D||_F^2 - c ||E||_F^2 ] >= 2-9(1+c)r`.      (1)

In particular, taking `c=30` and using `r<4/625`,

`E_seed[ ||D||_F^2 -30||E||_F^2 ]
 > 2-279*(4/625)
 = 134/625`.                                                   (2)

Hence there exists an invertible physical two-seed for which

`boxed: ||D||_F^2 -30||E||_F^2 > 134/625`.                    (3)

Consequences for that seed are

`||D||_F > sqrt(134/625)`,

and, since the left side of (3) is positive,

`||E||_F < ||D||_F/sqrt(30)`.

Thus the unresolved eight-direction branch contains a seed with a quantitatively nontrivial completed-diagonal vector and a **relative** Frobenius interpolation error below `1/sqrt(30)`. This is stronger than merely knowing total overlap mass `W>0`.

Equation (1) is exact except for the already-proved one-sided `E||E||^2` estimate; no dimension factor is introduced.

### What (3) does not permit

`E` is a coefficient error, not a bounded random perturbation. Under the theorem's arbitrary cap-one laws there are no moments or support bounds, so `||E||_F` small does not imply `X^TEX` small in probability or in any usable uniform norm. Any analytic receiver must keep that rough-law issue explicit.

## 2. Fixed rank-two crossing volume does not imply bounded density

A natural but false route below nine is to discard the shared overlap coordinate and try to upgrade the underlying order-two crossing seed to a direct bounded-density receiver.

Take four independent `Unif[-1/2,1/2]` variables `X_1,X_2,Y_1,Y_2` and

`Q=(X_1+Y_1)(X_2+Y_2)`.

For the literal cut `I={X_1,X_2}`, `J={Y_1,Y_2}`, the symmetric quadratic matrix has cross block

`M = [[0,1/2],[1/2,0]]`.

Therefore

`det M=-1/4`,  `Z_2(M)=det(M)^2=1/16`.

The full quadratic matrix is `(ab^T+ba^T)/2` with

`a=(1,0,1,0)`, `b=(0,1,0,1)`,

so its nonzero eigenvalues are exactly `1,-1`.

Now set

`U=X_1+Y_1`, `V=X_2+Y_2`.

The two sums use disjoint sets of original variables, so `U,V` are independent. Each has triangular density

`g(u)=1-|u|`, `|u|<=1`.

For `0<z<1`, the product-density formula gives

`p_Q(z)=2 int_z^1 (1-u)(1-z/u) du/u`

`       = -2(1+z) log z -4+4z`.                              (4)

Hence

`p_Q(z) ~ 2 log(1/z)` as `z downarrow0`,

and

`boxed: ||p_Q||_infinity = infinity`                          (5)

although the physical order-two crossing determinant is fixed away from zero.

This is a stronger obstruction than the one-edge `2XY` example: even an **invertible 2x2 physical crossing block** does not by itself yield a bounded density when arbitrary same-bank quadratic terms are allowed. It confirms that the manuscript's q=2 theorem is correctly formulated as a half-potential estimate, not a density estimate.

## 3. Consequence for the eight-eigenvalue programme

The overlap theorem supplies genuinely third-order information through the shared original index `h`. The counterexample above proves that an eight-direction proof cannot simply throw away `h` and pay the remaining invertible two-seed by a hypothetical q=2 density theorem.

The next analytic obligation can therefore be stated sharply:

> starting from a good seed satisfying (3), consume the shared-index bordered determinant / completed-diagonal resource while using the physical random coordinate `h` exactly once, and obtain an integrable output estimate without duplicating `h`, invoking pointwise scalar quadratic Fresnel decay, or treating `E` as a probabilistically small quadratic perturbation.

Until such a receiver is proved, the rigorously supported fixed multiplicity remains nine.
