SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-24T10:51:01Z.
attacking: cross-sign/transverse five-mode fusion, then square-order spectral inflation and a literal pinned-D5 stress inequality under arbitrary dense coefficient tails.

# fleet02/B12 — cross-sign/transverse fusion and finite-spectrum survivor obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T105101Z-fleet02-B12-QFORM-auto11`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING HYBRID STABILITY THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The full conjecture is not proved or disproved here. During this run the compatible partner advanced to fleet03/B12 r55, `9bcbbbdb12483a06b15d7923ec4324422924d781`. That theorem proves the full target whenever the final symmetric matrix has at least **189** eigenvalues of modulus at least one, with arbitrary remaining signed spectrum. Hence the global unresolved spectral-count window is now finite:

```text
3 <= #{j: |lambda_j(A)|>=1} <= 188.
```

The first unpaid implication is therefore sharper than in earlier B12 runs: in this finite window one must force an ORIGINAL-coordinate paid receiver, or show that every candidate carrier has a sufficiently severe resonance/transverse defect. The local theorem below makes the latter defect quantitative. No universal carrier scale is inferred from bare `s_3(A)>=1`.

For the partner r55 heavy/light parameters `alpha=213/2500`, `tau=1/512`, let `h` be the number of coordinates whose `|A|>=tau` spectral-projector leverage exceeds `alpha`. Reading the r55 proof parametrically gives an additional survivor constraint: if `h>=47`, its heavy 47-coordinate branch closes; if `h<=46` and

```text
r_1 := #{j: |lambda_j(A)|>=1} >= 5+4h,
```

its light MSS/ridge branch closes. Thus every r55-survivor in the finite window must satisfy

```text
h <= 46,
r_1 < 5+4h,
```

or equivalently `h > (r_1-5)/4`. This is not a full solution, but it converts the remaining large-spectrum obstruction into a finite spectral-count plus many-heavy-coordinate geometry.

## 2. Source-pinned analytic input

The required source is `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its proved fifth-volume theorem `D_5` states that for a literal disjoint ORIGINAL-coordinate cross block `C=A[I,J]`,

```text
||p_(X^T A X)||_infinity
 <= 5 sqrt(2e) e_5(C^T C)^(-1/10),
```

with **no fifth-volume marginal condition**. Same-bank quadratic terms, outside couplings and affine terms remain present. Hence

```text
s_5(C)>=h>0
  ==> e_5(C^T C)>=h^10
  ==> ||p_(X^T A X)||_infinity <= 5 sqrt(2e)/h.          (2.1)
```

The same pinned folder explicitly records that an arbitrary three-dimensional joint-density coarea shortcut is false, and its counterexample search found no full-QFORM counterexample. I therefore use `D_5` only on literal original-coordinate product banks.

## 3. Exact orthogonal-channel decomposition

Let `M in R^(p x m)` have full column rank and let `N in R^(p x m)` be arbitrary. Put

```text
G=M^T M,
g=s_m(M)>0,
U=M G^(-1/2),
Pi=UU^T,
K=G^(-1/2) M^T N G^(-1/2),
Z=(I-Pi)N.
```

Then `U^T U=I`, `U^T Z=0`, and

```text
M+N = U(I+K)G^(1/2)+Z.
```

The two displayed output channels are orthogonal. Therefore

```text
(M+N)^T(M+N)
 = G^(1/2)(I+K)^T(I+K)G^(1/2) + Z^T Z.              (3.1)
```

For descending singular values and integers `a,b` with `a+b>m`, PSD Weyl gives

```text
s_(a+b-m)(M+N)^2
 >= g^2 s_a(I+K)^2 + s_b(Z)^2.                       (3.2)
```

Indeed the first PSD summand in (3.1) has its `a`th eigenvalue at least `g^2 s_a(I+K)^2`, the second has its `b`th eigenvalue `s_b(Z)^2`, and Weyl's lower inequality adds them at index `a+b-m`.

This identity is deterministic matrix algebra. No random coordinate is whitened or rotated.

## 4. Cross-sign in-range shield

Write

```text
K=H+Omega,
H=(K+K^T)/2,
Omega=(K-K^T)/2,
D=I+H.
```

Fix `rho>0` and split the relative domain into spectral sectors

```text
E_+ = 1_[rho,infinity)(D) R^m,
E_0 = 1_(-rho,rho)(D) R^m,
E_- = 1_(-infinity,-rho](D) R^m.
```

Let `q=dim E_0`, and let

```text
Omega_+- = P_+ Omega P_- : E_- -> E_+.
```

For `r>=0`, set

```text
kappa_r = s_(r+1)(Omega_+-),
```

with `kappa_r=0` after its singular directions are exhausted.

The preceding fleet02/B12 theorem `QFORM-CROSS-SIGN-SKEW-RANK-SHIELD-v1` proved

```text
s_(m-q-2r)(I+K) >= (rho-kappa_r)_+                 (4.1)
```

whenever `m-q-2r>=1`. The mechanism is exact: within-sign skew blocks are free; a best rank-`r` approximation to the opposite-sign skew block spends at most `2r` modes; only its remaining operator tail `kappa_r` subtracts from the bipolar gap `rho`.

## 5. New theorem: cross-sign/transverse fusion

### Theorem — `QFORM-CROSS-SIGN-TRANSVERSE-FUSION-v1`

Under the definitions above, let `r,s>=0` satisfy

```text
q+2r+s <= m-1.
```

Then

```text
boxed:
s_(m-q-2r-s)(M+N)^2
 >= g^2 (rho-kappa_r)_+^2 + s_(m-s)(Z)^2.            (5.1)
```

If an arbitrary further matrix tail `T` satisfies

```text
||T||_op <= delta,
```

then

```text
boxed:
s_(m-q-2r-s)(M+N+T)
 >= [ sqrt(g^2 (rho-kappa_r)_+^2 + s_(m-s)(Z)^2)
      - delta ]_+.                                   (5.2)
```

### Proof

Take

```text
a=m-q-2r,
b=m-s.
```

The dimension hypothesis says `a+b>m`. By (4.1),

```text
s_a(I+K) >= (rho-kappa_r)_+.
```

Substitute this into the exact orthogonal-channel estimate (3.2):

```text
s_(a+b-m)(M+N)^2
 >= g^2 (rho-kappa_r)_+^2 + s_b(Z)^2.
```

Since `a+b-m=m-q-2r-s`, this is (5.1). Ordinary singular-value Weyl under the coefficient perturbation `T` proves (5.2). QED.

The important point is that the two resources add in **square energy**. A mode can be partly weak in the old carrier image and partly supplied by the transverse action; it need not be paid entirely by one channel.

For a five-mode target define the fusion envelope

```text
R_5(M,N)^2 =
 sup over rho>0 and r,s>=0 with q_rho+2r+s<=m-5 of
 [ g^2 (rho-kappa_r(rho))_+^2 + s_(m-s)(Z)^2 ].      (5.3)
```

Then every dense coefficient tail with norm at most `delta` obeys

```text
boxed:
s_5(M+N+T) >= [R_5(M,N)-delta]_+.                  (5.4)
```

This is strictly stronger than treating the in-range and transverse channels separately.

## 6. Literal ORIGINAL-coordinate compiler

Let `I,J` be disjoint original-coordinate banks, `|J|=m`, and let

```text
M=A_*[I,J],
N=S[I,J]
```

for symmetric coefficient matrices `A_*` and `S`. Form the fusion envelope from these literal physical blocks. Add any globally dense symmetric tail

```text
T_dense=T_dense^T,
||T_dense||_op <= delta.
```

Physical compression gives

```text
||T_dense[I,J]||_op <= delta.
```

Hence the actual final cross block `C=A[I,J]` satisfies (5.4). Whenever `R_5>delta`, the pinned completed `D_5` theorem gives

```text
boxed:
||p_(X^TAX)||_infinity
 <= 5 sqrt(2e)/(R_5(M,N)-delta).                    (6.1)
```

All same-bank quadratic terms and outside couplings remain present.

## 7. Exact stress family and real pinned-D5 inequality

Take `m=7`, `p=14`, and literal original-coordinate banks `I` of size 14 and `J` of size 7. Put

```text
M = [ 2 I_7 ]
    [   0   ],
```

and let

```text
E11 = diag(1,0,0,0,0,0,0),
D6  = diag(1,1,1,1,1,1,0),
N   = [ -2 E11 ]
      [  2 D6  ].
```

Then `G=4I_7`, `g=2`, and direct calculation gives

```text
K = -E11,
D=I+K=diag(0,1,1,1,1,1,1).
```

Choose `rho=1`. There is exactly one resonant direction, so `q=1`; there is no negative sector, hence `kappa_0=0`. The transverse action is

```text
Z = [ 0    ]
    [ 2 D6 ],
```

with

```text
s_6(Z)=2.
```

Take `r=0`, `s=1`. The new theorem yields

```text
s_5(M+N)^2 >= 2^2 + 2^2 = 8,
so s_5(M+N)>=2 sqrt(2).                            (7.1)
```

Here the estimate is exact. Indeed

```text
M+N = [ 2 diag(0,1,1,1,1,1,1) ]
      [ 2 diag(1,1,1,1,1,1,0) ],
```

whose column norms are `2, 2sqrt(2),...,2sqrt(2), 2`, with five copies of `2sqrt(2)`, and the columns are mutually orthogonal.

The in-range cross-sign theorem alone gives only `s_6>=2` and hence the weaker `s_5>=2`; the transverse channel alone also supplies only scale 2. Their square-energy fusion gives the strict factor `sqrt(2)` improvement.

Realise this as a symmetric coefficient core

```text
B_* = [[0, M+N],[(M+N)^T,0]]
```

on the 21 original coordinates `I union J`. Append any direct-sum symmetric spectator block `Theta`, with arbitrary signs, multiplicities, magnitudes, and internal mixing, and then any globally dense symmetric tail with

```text
||T_dense||_op <= 1/64.
```

For the literal final physical cross block,

```text
s_5(A[I,J])
 >= 2sqrt(2)-1/64
 = 2.8128021247461903....                            (7.2)
```

Applying the required pinned `D_5` theorem gives the real final-matrix inequality

```text
boxed:
||p_(X^TAX)||_infinity
 <= 5 sqrt(2e)/(2sqrt(2)-1/64)
 = 4.144699623702675....                             (7.3)
```

This is source-valid: the fifth-volume is that of the actual final original-coordinate cross block. No common-spectral-mode-to-cross-volume inference is made.

The exact-target condition is also literal. Before the dense tail the off-diagonal core has 14 nonzero eigenvalues, occurring as `+s_j(M+N)` and `-s_j(M+N)`, all of modulus at least 2. Therefore after the dense tail

```text
s_14(A) >= 2-1/64 = 127/64 >1,
```

so in particular at least three final eigenvalues have modulus at least one.

## 8. Arbitrary signed spectral inflation: use the newest partner mechanism

The newest partner r55 includes the r54 square-order monotonicity theorem: if symmetric `A_spec,B_*` satisfy

```text
A_spec^2 >= B_*^2,
```

then on every literal original-coordinate carrier `H`,

```text
s_k(A_spec P_H) >= s_k(B_* P_H).                    (8.1)
```

Thus start from the 21-coordinate proxy `B_*` above and keep its eigenvectors fixed while replacing every eigenvalue `mu_j` by an arbitrary signed `lambda_j` satisfying

```text
|lambda_j| >= |mu_j|.
```

Zero proxy modes may also receive arbitrary signed magnitudes. Then `A_spec^2>=B_*^2`, and for the literal seven-coordinate bank `J`,

```text
s_5(A_spec P_J)
 >= s_5(B_* P_J)
 >= s_5(B_*[I,J])
 =2sqrt(2).                                          (8.2)
```

Now add any noncommuting globally dense symmetric tail `T` with `||T||<=1/64`. Deterministic Weyl gives

```text
s_5((A_spec+T)P_J)
 >=2sqrt(2)-1/64.                                    (8.3)
```

The completed five-square-mode physical compiler quoted in partner r55 therefore yields, with `|J|=7` and `K3=3*2^(4/3)*e^(1/3)`,

```text
boxed:
||p_(X^TAX)||_infinity
 <= sqrt(24*pi*7+K3^2)/(2sqrt(2)-1/64)
 = 8.987586067946978....                             (8.4)
```

and a continuous `C_0` density on this entire spectrally inflated family.

This is the stronger additional-spectrum statement: arbitrarily many eigenvalue magnitudes may be increased without cost, with arbitrary signs, and a later dense noncommuting tail is paid only by its coefficient norm. I do **not** apply `D_5` after such a general spectral inflation, because square-order monotonicity controls physical column energy, not literal cross-block fifth volume. The pinned `D_5` inequality (7.3) is reserved for the actual-cross-block subfamily where its hypothesis is verified directly.

## 9. Interaction with partner r55 and the remaining survivor geometry

Partner r55 proves that `r_1>=189` closes the full target. Therefore any global counterexample must have `3<=r_1<=188`. Within that window, its own heavy/light proof further forces a survivor to have at most 46 heavy coordinates and `r_1<5+4h` for the specified projector scale.

On any candidate physical cross carrier inside such a survivor, the present theorem gives an independent necessary obstruction. For every usable `rho,r,s` with

```text
q_rho+2r+s <= m-5,
```

a failure of the fifth-mode receiver requires

```text
sqrt(g^2(rho-kappa_r)_+^2+s_(m-s)(Z)^2) <= delta_local             (9.1)
```

at the tail scale being paid. In words: a survivor must simultaneously have many relative cancellation directions, enough opposite-sign skew transport to consume the in-range reserve, **and** insufficient transverse singular energy to repair the missing modes. Large packet norm or large added eigenvalues alone are not an obstruction.

The next useful task is to turn the combined finite-count/heavy-coordinate condition from r55 and the local failure normal form (9.1) into a literal physical pair, projected crossing, grouped hub, ridge, Schur/common-plane, or Pluecker-volume certificate. That implication remains open.

## 10. Dense-tail and independence discipline

The dense tail is used only through deterministic coefficient inequalities such as

```text
||T[I,J]||_op <= ||T||_op,
s_k(C+T[I,J]) >= s_k(C)-||T||_op.
```

No statement treats `X^T T X` as uniformly small for unbounded inputs. The matrices `G^(-1/2)`, `U`, `Pi`, and the relative spectral sectors are proof devices only. Every probabilistic density theorem is applied on literal original-coordinate banks; no post-rotation independence is assumed.

No valid full-QFORM counterexample was found in the pinned search or in this run.