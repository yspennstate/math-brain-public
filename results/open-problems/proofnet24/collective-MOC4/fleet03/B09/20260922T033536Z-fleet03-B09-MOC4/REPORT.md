# MOC4 fleet03/B09 — exact complementary-minor/unitary compatibility

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Worker:** fleet03/B09  
**Assignment:** derive an inequality exploiting the special complementary 2-by-2 minors in dimension four, and actually apply it to the lead's determinant-support expression.  
**Named partner consumed:** fleet04/B07.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / AUXILIARY_ONLY`; MOC4 remains open.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and inherited gap

For normal 4-by-4 matrices, after unitary conjugation write

`A=diag(a_1,...,a_4)` and `B=U diag(b_1,...,b_4) U*`.

The target is

`det(A+B) in conv{ product_i(a_i+b_{pi(i)}): pi in S_4 }`.

The previous complementary-pair reduction separates the exterior-square layer into a symmetric quotient `R` and an oriented difference `D`. Previous relaxations that let those channels vary as arbitrary bistochastic/color data are too strong. This run therefore derives a compatibility identity satisfied by every genuine unitary `U`.

## 2. Complementary-pair coordinates

Use the three representative pairs

`S_1={1,2}, S_2={1,3}, S_3={1,4}`

and the analogous column pairs `T_beta`. Put

`P_ip=|u_ip|^2`,

`q_{S,T}=|det U[S,T]|^2`,

`R_{alpha beta}=q_{S_alpha,T_beta}+q_{S_alpha,T_beta^c}`,

`D_{alpha beta}=q_{S_alpha,T_beta}-q_{S_alpha,T_beta^c}`.

Jacobi complementarity for a unitary gives the required four-minor block pairing, and `R` is doubly stochastic with `R_{alpha beta} >= |D_{alpha beta}|`.

Introduce the tetrahedral sign matrix

```
E = [ 1  1  1
      1 -1 -1
     -1  1 -1
     -1 -1  1 ].
```

Column `alpha` is the sign vector of membership in `S_alpha`: `+1` on `S_alpha`, `-1` on its complement. Note `E^T E=4 I_3`.

## 3. New exact compatibility identity

### Proposition

For every complex 4-by-4 unitary `U`, the genuine minor data above satisfy

`D E^T = E^T P`,

and hence

`D = (1/4) E^T P E`.                                             (C)

Thus the oriented/difference channel of the entire 2-by-2-minor layer is not an independent transport variable: it is determined exactly by the same unistochastic matrix `P` appearing in the k=1 and k=3 layers.

### Proof

Fix a representative row pair `S={i,j}` and a column `p`. Row orthogonality gives

`sum_{q != p} |u_ip u_jq-u_iq u_jp|^2 = |u_ip|^2+|u_jp|^2`.

Indeed, including the zero `q=p` term and expanding gives

`|u_ip|^2 sum_q |u_jq|^2 + |u_jp|^2 sum_q |u_iq|^2
 -2 Re( u_ip conjugate(u_jp) sum_q u_jq conjugate(u_iq) )`,

which is `P_ip+P_jp` because the two rows are orthonormal.

The six 2-subsets of columns occur as the three complementary pairs `(T_beta,T_beta^c)`. Multiplication by the signs in row `p` of `E` subtracts the three minors not containing `p` from the three minors containing `p`. Therefore

`sum_beta E_{p beta} D_{alpha beta}
 = 2 sum_{r in S_alpha} P_{r p} - 1
 = sum_r E_{r alpha} P_{r p}`,

where the last equality uses `sum_r P_{rp}=1`. This is exactly `D E^T=E^T P`. Multiplying on the right by `E/4` and using `E^T E=4I` proves (C). QED.

No reality assumption on `U` was used.

## 4. Application to the full determinant-support expression

For each representative pair put

`x_alpha=product_{i in S_alpha} a_i`, `x'_alpha=product_{i in S_alpha^c} a_i`,

`y_beta=product_{j in T_beta} b_j`, `y'_beta=product_{j in T_beta^c} b_j`,

and

`A^+_alpha=x_alpha+x'_alpha`, `A^-_alpha=x'_alpha-x_alpha`,

`B^+_beta=y_beta+y'_beta`, `B^-_beta=y_beta-y'_beta`.

The four terms in one complementary 2-by-2 block give exactly

`L_2 = (1/2) (A^+)^T R B^+ + (1/2) (A^-)^T D B^-`.

Applying (C),

`L_2 = (1/2) (A^+)^T R B^+ + (1/8) (E A^-)^T P (E B^-)`.          (1)

Let `c_i=product_{r != i} a_r` and `d_p=product_{s != p} b_s`. The k=1 layer is `sum c_i b_p P_ip`; Jacobi complementarity identifies the k=3 layer with `sum a_i d_p P_ip`. Consequently the entire determinant is

`det(A+U diag(b) U*)
 = a_1a_2a_3a_4 + b_1b_2b_3b_4
 + sum_{i,p} H_ip P_ip
 + (1/2) (A^+)^T R B^+`,                                  (2)

where

`H_ip = c_i b_p + a_i d_p + (1/8)(E A^-)_i (E B^-)_p`.          (3)

This is an exact source-valid reduction. It collapses every antisymmetric/oriented 2-minor contribution into the same genuine unistochastic `P` already present at levels 1 and 3. The only remaining separate middle-layer object is `R`.

For a support direction `eta` on the unit circle, (2) reduces the first unpaid MOC4 implication to bounding

`Re[ eta_bar ( sum H_ip P_ip + (1/2)(A^+)^T R B^+ ) ]`

for the genuine linked pair `(P,R)` arising from one unitary. It is not legitimate to replace `(P,R)` by arbitrary independent bistochastic matrices.

## 5. Named-partner result consumed and sharpened into a P-R gate

I consumed fleet04/B07 run `20260922T021038Z-fleet04-B07-MOC4-r13`, handoff commit `63a7439240d9e98245277ac7ef03772949485b3b`, canonical scientific report commit `89fe5ebe78b671f1a7f46624ebcd385ceea91ddd`.

That result proves, for the genuine `SO(6)` exterior-square image and every `rho in S_3` and odd sign pattern `epsilon`, the odd-Weyl overlap inequality

`sum_alpha sqrt(q^{epsilon_alpha}_{alpha,rho(alpha)}) <= 2`,

where `q^+=(R+D)/2` and `q^-=(R-D)/2`. It also gives an exact structured witness refuting the orientation-forgetting 48-state Weyl/Birkhoff relaxation, so its effect on this run is substantive: the remaining support problem must retain true unitary compatibility instead of maximizing over arbitrary colored matchings.

Substituting (C) turns the partner theorem into the explicit genuine-unitary P-R compatibility inequality

`sum_alpha sqrt( ( R_{alpha,rho(alpha)}
                  + epsilon_alpha (E^T P E)_{alpha,rho(alpha)}/4 ) / 2 ) <= 2`       (4)

for every odd `epsilon` (with the sign convention matching `q^+`/`q^-`). Together with

`R >= |E^T P E|/4`, `R 1=1`, and `R^T 1=1`,

(4) is a nonlinear unitary-orbit gate directly in the variables of (2). It is strictly more faithful than the refuted arbitrary-bistochastic/common-lift mechanisms. I do not claim these displayed constraints are yet sufficient to characterize all genuine `(P,R)`.

## 6. Exact verifier, including singular and repeated spectra

The committed Fraction-only verifier uses the exact rational Householder matrix

`U=I-vv^T/15`, `v=(1,2,3,4)`,

and checks exactly:

- `U^T U=I`;
- `D E^T=E^T P` and `D=(1/4)E^T P E`;
- `R` is doubly stochastic and `R>=|D|`;
- the full determinant reconstruction (2) for `a=(0,2,2,7)`, `b=(3,0,5,5)`, which deliberately contains singular and repeated spectral entries.

The exact result is

`det(A+U diag(b)U^T)=148984/225`,

and the right side of (2) gives exactly the same rational number. No division by any spectral difference or eigenvalue occurs, so the identity itself covers singular and repeated spectra without a limiting argument.

A separate complex-unitary numerical sanity check performed during derivation gave errors below `6e-16` for (C) and about `1.2e-13` for the full complex determinant reconstruction; this is only a check, not part of the proof.

## 7. Status and exact next step

**Status: `ESSENTIAL_STEP_APPLIED / AUXILIARY_ONLY`.** MOC4 is neither proved nor disproved here.

The run removes one genuine compatibility degree of freedom: `D` is exactly determined by `P`. The first remaining implication is now sharply stated: prove the 24-vertex support bound for (2) over genuine unitary-linked `(P,R)`, using (4) and/or the full block-orthogonality relations to control the symmetric quotient `R`. A valid next move is to exploit the rank-one spectral coefficient `(A^+)(B^+)^T` in the remaining `R` term together with the odd-Weyl inequalities; returning to arbitrary independent bistochastic `P,R` would discard the information just proved and is not source-valid.

No counterexample to MOC4 was found in this run.
