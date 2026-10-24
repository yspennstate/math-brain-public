SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-24T00:42:17Z.
attacking: the majority-sign ultra-coloop discriminant endpoint; isolate whether the nonzero fresh-hub square itself is an obstruction once a genuine product-preserving transverse puncture is present.

# account01/B16 — hub-phase lift of the phase-weighted two-bank receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `account01-B16-20260924T004217Z-auto11`  
**Status:** `NEW SUPPORTING THEOREM + COMPLETED PARTNER APPLIED TO AN ACTUAL TARGET INEQUALITY / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the new punctured branch has a continuous density vanishing at infinity. Global continuity remains open.

## 1. Source boundary and corrections retained

Fresh controls still place every worker exclusively on the full quadratic-form density conjecture. The unrestricted theorem is **OPEN / NOT PROVED / NOT DISPROVED**.

The mathematical inputs actually used are:

1. the bounded-density projection theorem in the owner-pinned package `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`; in particular an orthonormal two-dimensional projection of a cap-one product law has density at most `2`;
2. the newest **completed** designated partner account02/B16 result, `QFORM-PHASEWEIGHTED-PUNCTURED-TWOBANK-v1`, at `yspennstate/math-open-problems@c9c865f02890e5fe7108c49759ee82b84f42ee38`;
3. the preceding account02/B16 zero-pivot result `QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1` at `@be8062b160868bcc71aff45a77c56ff2d0501a9a`, used only to locate the remaining interface, not as a premise in the proof below;
4. the preceding account01/B16 conditional discriminant theorem at `@407fb7555d24b85565afbce0caea98bdad914c08`, again used only to locate the majority-sign endpoint.

The live corrections are preserved. In particular, no independence is inferred after projection; no arbitrary-joint indefinite coarea estimate is used; no conditional projection cap is inferred from a marginal cap; and the proof never replaces a product bank by a bare bounded joint density inside an indefinite physical level-set integral.

## 2. New theorem: an arbitrary hub phase costs nothing in the completed punctured receiver

Use the notation of account02/B16 r37. Let `H`, source bank `A`, and source bank `B` be mutually independent. For `i=A,B`, let

`Y_i=(L_i,V_i,P_i)`

be a three-dimensional linear projection of bank `i`, with joint density `g_i` and `(L_i,V_i)` marginal density `m_i`. Assume

`||m_i||_infinity <= M_(2,i)`,
`||g_i||_infinity <= M_(3,i)`.

Set

`L=L_A+L_B`, `V=V_A+V_B`, `P=P_A+P_B`,
`K_2=(M_(2,A)M_(2,B))^(1/2)`,
`K_3=(M_(3,A)M_(3,B))^(1/2)`.

Let the fresh hub have density `f_H` satisfying

`||f_H||_infinity <= L_H`.

Let `R_H(H)`, `R_A(X^A)`, and `R_B(X^B)` be arbitrary real measurable functions of their respective original source blocks. For real `alpha,beta,delta,lambda,epsilon` with

`alpha epsilon lambda != 0`,                                      (2.1)

consider

`Q = R_H(H)
     +2 alpha H L + beta L^2 +2 delta L V +lambda V^2+2 epsilon L P
     +R_A+R_B+affine`.                                             (2.2)

### `QFORM-HUBPHASE-PUNCTURED-TWOBANK-v1`

The law of `Q` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= 3 [ L_H K_2 K_3 / |alpha epsilon lambda| ]^(1/3).
`                                                                    (2.3)

Thus the completed account02/B16 punctured theorem is stable not only under arbitrary phases on the two light banks, but also under an **arbitrary real phase on the fresh hub itself**. In particular, a nonzero quadratic hub term `theta H^2` has exactly zero cost in this branch.

### Proof

For each fixed outer Fourier time `t`, replace the positive hub density by the complex phase-weighted density

`h_(H,t)(x)=f_H(x) exp(i t R_H(x))`.                               (2.4)

Let

`Psi_(H,t)(xi)=integral exp(-i xi x) h_(H,t)(x) dx`.               (2.5)

The phase has modulus one, so Plancherel gives, for every `t`,

`integral_R |Psi_(H,t)(xi)|^2 dxi
 =2pi integral_R f_H(x)^2 dx
 <=2pi L_H integral_R f_H(x) dx
 =2pi L_H`.                                                        (2.6)

This is exactly the hub input used in account02/B16 r37. Indeed, r37 first phase-weights each light bank, proves

`||S_t||_infinity <=(2pi)^2 K_2`,                                  (2.7)
`integral S_t <=(2pi)^3 K_3`,                                     (2.8)

and hence

`||S_t||_2 <=(2pi)^(5/2)(K_2K_3)^(1/2)`.                          (2.9)

Its only hub estimate is its displayed Plancherel line

`||hat f_H||_2^2 <=2pi L_H`.                                      (2.10)

Replacing `hat f_H` by `Psi_(H,t)` therefore changes none of the inequalities: positivity of the hub measure is not used after this point, and (2.6) is uniform in the same outer time `t`. The exact `P` integration, the one-dimensional Fresnel integral in `V`, and the final Cauchy--Schwarz pairing consequently give the identical characteristic-function estimate

`|phi_Q(t)|
 <= pi^(3/2) sqrt(L_H K_2 K_3)
    |alpha epsilon lambda|^(-1/2) |t|^(-3/2)`                     (2.11)

for `t!=0`.

Write

`C_0=pi^(3/2)sqrt(L_HK_2K_3)|alpha epsilon lambda|^(-1/2)`.

Together with `|phi_Q(t)|<=1`,

`integral_R |phi_Q(t)|dt
 <= 2[ C_0^(2/3) + 2 C_0^(2/3)]
 =6 C_0^(2/3).`                                                   (2.12)

Fourier inversion gives

`||p_Q||_infinity
 <=(1/(2pi)) 6 C_0^(2/3)
 =3[L_HK_2K_3/|alpha epsilon lambda|]^(1/3)`,                     (2.13)

which is (2.3). Since `phi_Q in L^1`, the inverse Fourier transform is a continuous function vanishing at infinity. QED.

The dependence point is essential: no coordinate of `(L_i,V_i,P_i)` is declared independent of another. The product structure is retained at the level of the two disjoint **original source banks**, and the bounded-density projection theorem is used only to control the Hilbert energies that survive the nonlinear Fourier integration.

## 3. Insert the actual bounded-density projection theorem

Suppose now that each bank is an arbitrary cap-one product law and that the three coefficient rows producing `(L_i,V_i,P_i)` are orthonormal. The actual projection theorem gives

`M_(2,i)<=2`,
`M_(3,i)<=2^(3/2)`.                                                (3.1)

Hence

`K_2<=2`, `K_3<=2^(3/2)`,                                        (3.2)

and Theorem 2.1 yields

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/6)|alpha epsilon lambda|^(-1/3)
 =5.345392308842... |alpha epsilon lambda|^(-1/3).
`                                                                    (3.3)

More generally, the completed partner calculation already records that if each three-row coefficient Gram is at least `kappa I_3`, then

`M_(2,i)<=2/kappa`,
`M_(3,i)<=2^(3/2) kappa^(-3/2)`,                                  (3.4)

so the hub-phase lift gives, unchanged,

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/6) kappa^(-5/6)|alpha epsilon lambda|^(-1/3).
`                                                                    (3.5)

The hub phase is absent from the right side. Thus once a quantitative two-bank three-dimensional puncture is available, the nonzero physical hub square is not itself a singular parameter.

## 4. Completed account02/B16 result applied to an actual target family, then lifted through every hub square

Take one fresh physical coordinate `H` and two disjoint product banks

`X^A in R^(n_A)`, `X^B in R^(n_B)`,

all original coordinates mutually independent with densities bounded by one. In each bank choose a deterministic `3 x n_i` matrix `T_i` with orthonormal rows, and write

`(L_i,V_i,P_i)=T_i X^i`.

Let `E_A,E_B` be arbitrary real symmetric matrices with

`||E_A||_op, ||E_B||_op <=1/2`.                                   (4.1)

For arbitrary `theta in R`, define

`Q_theta
 = theta H^2
  +2H(L_A+L_B)
  +(V_A+V_B)^2
  +2(L_A+L_B)(P_A+P_B)
  +(X^A)^T E_A X^A +(X^B)^T E_B X^B`.                            (4.2)

### 4.1 The completed partner inequality at `theta=0`

At `theta=0`, this is a literal application of the completed account02/B16 r37 theorem with

`alpha=epsilon=lambda=1`, `beta=delta=0`,
`R_A=(X^A)^TE_A X^A`, `R_B=(X^B)^TE_B X^B`.                      (4.3)

The projection theorem gives (3.1), so r37 yields the actual inequality

`boxed:
 ||p_(Q_0)||_infinity <=3*2^(5/6)<5.346.
`                                                                    (4.4)

No projected coordinates are treated as independent.

### 4.2 The new hub-phase lift makes the same inequality uniform in `theta`

Apply Theorem 2.1 with

`R_H(H)=theta H^2`.                                                 (4.5)

The same computation now gives, for **every** real `theta`,

`boxed:
 ||p_(Q_theta)||_infinity <=3*2^(5/6)<5.346.
`                                                                    (4.6)

Moreover each `Q_theta` has a continuous `C_0` density.

### 4.3 Every member of (4.2) is genuinely in the owner target

Let `ell_i,v_i,p_i` denote the three orthonormal coefficient rows of `T_i`. On the combined two-bank physical space define normalized symmetric aggregate directions

`ell=(ell_A,ell_B)/sqrt(2)`,
`v=(v_A,v_B)/sqrt(2)`,
`p=(p_A,p_B)/sqrt(2)`.                                             (4.7)

They are orthonormal. Before adding the two `E`-perturbations, the coefficient matrix of (4.2) on the orthonormal carrier basis

`(H,ell,v,p)`

is

`A_theta^0 =
 [[theta, sqrt(2), 0, 0],
  [sqrt(2), 0,       0, 2],
  [0,       0,       2, 0],
  [0,       2,       0, 0]].`                                    (4.8)

The `ell,p` principal submatrix is

`[[0,2],[2,0]]`,                                                   (4.9)

with eigenvalues `+2,-2`. By Cauchy interlacing, the three-dimensional `(H,ell,p)` block has one eigenvalue at least `2` and one at most `-2`, independently of `theta`. The orthogonal `v` direction is an eigenvector with eigenvalue `2`. Therefore `A_theta^0` has at least two positive eigenvalues `>=2` and one negative eigenvalue `<=-2` for every real `theta`.

The full same-bank perturbation is block diagonal on the original source banks and has operator norm

`max(||E_A||_op,||E_B||_op)<=1/2`.                                (4.10)

Weyl's inequality consequently leaves at least two positive eigenvalues `>=3/2` and one negative eigenvalue `<=-3/2`. Thus every member of (4.2), in every ambient dimension and for every `theta`, has at least three eigenvalues of modulus at least one.

So (4.6) is an actual dimension-free owner-target inequality for a genuinely rotated, dependent-projection family carrying an arbitrary nonzero fresh physical hub square and arbitrary within-bank quadratic curvature of norm at most `1/2`.

If the two bank projections are literally the first three physical coordinates of each bank, then `M_(2,i),M_(3,i)<=1`; the same theorem sharpens (4.6) to

`||p_(Q_theta)||_infinity<=3`.                                    (4.11)

## 5. What this pays in the current near-coloop logic

The preceding B16 chain had isolated the nonzero fresh physical hub square as the new term absent from the zero-pivot theorem. The present result separates two issues that had been entangled:

* **hub-square stability is completely paid on every genuine punctured two-bank packet**: an arbitrary term `R_H(H)`, in particular `theta H^2` with no size or sign restriction, leaves the r37 bound unchanged;
* the bound still carries the puncture factor `|epsilon|^(-1/3)` and therefore says nothing at `epsilon=0`.

Hence the surviving structural implication is more precise:

`QFORM-EXTRACT-PRODUCT-PRESERVING-PUNCTURE-OR-INNOVATIONFREE-HUB-v1`.

In a general true-near-coloop survivor with small nonzero physical hub pivot, either extract two disjoint original-coordinate banks whose relevant three-dimensional coefficient Grams are quantitatively nondegenerate and whose reduced receiver has `|alpha epsilon lambda|` bounded below, in which case (3.5) closes the branch **uniformly in the hub pivot**, or treat the genuinely innovation-free endpoint where every such transverse puncture degenerates. The latter is the only place where a new source-preserving majority-sign/hyperbolic-discriminant mechanism is still needed from this B16 viewpoint.

This conclusion is consistent with the account02/B16 r37 obstruction: law-uniform perturbative comparison as `epsilon->0` is false, so the remaining `epsilon=0` bridge cannot be obtained by continuity in the coupling parameter.

## 6. Status

`QFORM-HUBPHASE-PUNCTURED-TWOBANK-v1`: **PROVED SUPPORTING THEOREM**.

Actual projection-product target family (4.2): **PROVED**, with continuous density and

`||p||_infinity <=3*2^(5/6)<5.346`

for arbitrary cap-one original laws and arbitrary `theta`, under (4.1).

Completed designated partner account02/B16 r37: **APPLIED at the actual inequality (4.4)**, then extended by a phase-invariant hub Plancherel argument to (4.6).

Full unrestricted QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains **OPEN**.
