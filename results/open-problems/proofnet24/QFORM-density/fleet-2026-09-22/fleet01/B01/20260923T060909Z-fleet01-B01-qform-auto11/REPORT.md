SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-23T06:09:09Z.
attacking: singular/near-singular overlap-two pair bases via an adjugate compound-Schur identity and a one-hub half-Riesz compiler.

# Exact rank-one pair-base compiler and compound-Schur identity

Run: `20260923T060909Z-fleet01-B01-qform-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: fleet01/B01, Oscillatory replacement  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction boundary

The unrestricted target remains OPEN: for every dimension, independent real physical coordinates with densities bounded by one, and every real symmetric A with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of Q=X^TAX, or give a target-valid counterexample. Full continuity remains separately OPEN.


Source control state refreshed during the run: `yspennstate/math-research-brain@5e2c719118284e6c535165f6172ec4737f7385a8` (the control file itself still states revision 2026-09-22.15).

## 2. Source-valid dependencies

### 2.1 One-dimensional product projection / random-slope source

The completed fleet01/B01 source

`yspennstate/math-open-problems@e398e885cc1902a2484e86973dd016a68721ec5c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260922T183610Z-b01-qform-auto11/REPORT.md`

records the product-projection bound

`||p_(b dot Y)||_infinity <= C1/||b||_2`, with `C1<=sqrt(2)`,

for every linear image of independent cap-one physical coordinates, and proves the associated aggregate random-slope Plancherel estimate. Only the projection-density statement is needed for the new endpoint lemma below.

### 2.2 Previous B01 overlap-two compiler

The completed source

`yspennstate/math-open-problems@21cf221fb1e8b99c99298fb11a0d5a41a8382aba`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T054511Z-fleet01-B01-qform-auto11b/REPORT.md`

proved an aggregate overlap-two compiler when the physical 2x2 pair base is invertible indefinite. It used the exact Schur identity `W2=det(B)^2 F(C)` and an aggregate quarter-Riesz theorem. That argument degenerates at `det B=0`; the present run treats that singular endpoint directly instead of dividing by a tiny determinant.

### 2.3 Latest designated partner fleet02/B01

The latest completed designated partner is

`yspennstate/math-open-problems@5a4923fcec8db7b5f5b7a14e5762c3291b02d299`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260923T060557Z-fleet02-B01-qform-auto11/REPORT.md`.

For `R=X^T C X+b^T X+c`, `F(C)=sum_(i!=j) C_ij^2`, it proves for every `0<beta<1/2`

`H_beta(R):=sup_s E|R-s|^{-beta} <= C_beta F(C)^(-beta/2)`,       (2.1)

with

`C_beta=e^(beta/2)(4pi)^beta/[beta(1-2beta)Gamma(beta)cos(pi beta/2)]`.

Section 6 applies this theorem to the exact residual produced by the new singular-pair reduction.

## 3. New endpoint lemma: one physical hub plus an aggregate random slope

### Theorem 3.1 — `QFORM-ONE-HUB-HALF-RIESZ-v1`

Let X be one physical coordinate and Y a disjoint bank of original coordinates. All coordinates are independent and have densities bounded by one. Let `b!=0`, `beta0` be real, and let R(Y) be arbitrary measurable. Put

`T=2 X (b dot Y + beta0)+R(Y)`.

Then

`boxed: sup_s E|T-s|^(-1/2) <= 2^(11/4) ||b||_2^(-1/2).`          (3.1)

No quadratic, moment, support, sign or regularity assumption is imposed on R.

### Proof

For every cap-one scalar density f and every shift a, the bathtub inequality gives

`int |x-a|^(-1/2) f(x) dx <= int_(-1/2)^(1/2)|u|^(-1/2)du=2sqrt(2).` (3.2)

Set `Z=b dot Y+beta0`. Since `b!=0`, Z has a density, and the product-projection bound gives

`||p_Z||_infinity <= M:=sqrt(2)/||b||_2`.                         (3.3)

Condition on Y. Outside the null event Z=0,

`E_X |2ZX+R(Y)-s|^(-1/2)
 = |2Z|^(-1/2) int |x-a(Y,s)|^(-1/2) f_X(x)dx
 <=2 |Z|^(-1/2).`                                                 (3.4)

A second bathtub bound, now for a probability density bounded by M, gives

`E|Z|^(-1/2) <=2sqrt(2M)`.                                       (3.5)

Combining (3.3)-(3.5),

`sup_s E|T-s|^(-1/2)
 <=4sqrt(2) M^(1/2)
 <=2^(11/4)||b||_2^(-1/2).`

This proves (3.1). QED.

This is an endpoint `beta=1/2` estimate, but only because the residual is exactly linear in one physical hub. It does not contradict the partner theorem's `(1-2beta)^(-1)` blow-up for a general quadratic form. A nonzero hub-square term can be completed against the random slope and may create a perfect square after adversarial coupling to R, so the exact zero-square structure below is essential.

## 4. New exact identity: compound-Schur overlap-two matrix without invertibility

Fix any physical pair `S={i,j}`. Write

`B=A[S,S]`, `K=S^c`, `M=A[S,K]`, `C0=A[K,K]`.

Define the compound-Schur matrix

`K_S := det(B) C0 - M^T adj(B) M`.                                (4.1)

For every k,l in K, direct bordered-determinant expansion gives the exact identity

`boxed: (K_S)_(kl)=det A[S union {k}, S union {l}].`              (4.2)

No invertibility is assumed. If B is invertible, (4.1) is `det(B)` times the ordinary Schur complement, recovering the preceding run.

Now assume B has rank one and is nonzero. Choose a coordinate ordering with

`B=[[a,b0],[b0,c]]`, `a!=0`.

Since `det B=0`, `c=b0^2/a`. Write the two rows of M as u and v and put

`z=v-(b0/a)u`.                                                     (4.3)

Then an exact rank-one factorisation holds:

`M^T adj(B) M = a z z^T`,                                         (4.4)

hence

`boxed: det A[S union {k},S union {l}] = -a z_k z_l.`             (4.5)

For the ordered off-diagonal overlap-two star

`W2(S)=sum_(k!=l) det A[S union {k},S union {l}]^2`,

(4.5) yields

`boxed: W2(S)=a^2( ||z||_2^4-||z||_4^4 ).`                        (4.6)

If B is the zero matrix, every overlap-two minor around S vanishes identically. Thus the singular pair-base geometry is completely explicit.

## 5. New theorem: exact rank-one physical pair compiler

### Theorem 5.1 — `QFORM-RANKONE-PAIR-OVERLAP2-v1`

Suppose the physical pair block B above has rank one and is nonzero, and `W2(S)>0`. Choose a nonzero diagonal pivot a in B and define z by (4.3). Then the full quadratic form, including arbitrary outside curvature and affine leakage, has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <=2^(11/4)|a|^(-1/2)||z||_2^(-1/2).`      (5.1)

Consequently,

`boxed: ||p_Q||_infinity <=2^(11/4)|a|^(-1/4)W2(S)^(-1/8).`       (5.2)

Choosing the larger-magnitude physical diagonal in the rank-one pair gives the coordinate-free pair-base form

`boxed: ||p_Q||_infinity <=8 ||B||_op^(-1/4) W2(S)^(-1/8).`       (5.3)

Continuity is not claimed.

### Proof

Let the two physical variables be x=X_i and y=X_j, and write the remaining variables as Y. Completing the square only in the original coordinate x gives exactly

`Q=a(x+(b0/a)y+a^(-1)u dot Y+gamma)^2 + T(y,Y)`,                  (5.4)

where all induced affine constants are absorbed into gamma and

`T(y,Y)=2y(z dot Y+beta0)+R(Y)`.                                  (5.5)

The y^2 coefficient cancels exactly because `det B=0`. The conditional density of the shifted square in (5.4) is bounded by

`|a|^(-1/2)|r|^(-1/2)`                                            (5.6)

at signed displacement r. Therefore

`p_Q(s)<=|a|^(-1/2) E|T-s|^(-1/2)`.                              (5.7)

Apply Theorem 3.1 to (5.5) to get (5.1).

From (4.6), `W2(S)<=a^2||z||_2^4`, which inserted into (5.1) gives (5.2). Finally a nonzero symmetric rank-one 2x2 matrix has one eigenvalue lambda with `||B||_op=|lambda|` and at least one diagonal entry of magnitude at least `|lambda|/2`. Selecting that pivot in (5.2) contributes only `2^(1/4)` and gives `2^(11/4+1/4)=8`, proving (5.3). QED.

The scaling is correct: `||B||_op` has matrix scale one and W2 has scale six, so the right side of (5.3) has density scale minus one.

This closes the exact singular endpoint left by the preceding invertible-pair overlap-two theorem. It does **not** by itself close arbitrarily near-singular invertible pairs; those remain assigned to the already-proved definite/indefinite pair receivers plus structural routing.

## 6. Latest designated partner applied to the new residual

The partner theorem (2.1) applies directly to the residual T in (5.5). Its symmetric quadratic matrix contains the hub-bank entries z, so

`F(T)>=2||z||_2^2`.                                                (6.1)

Hence for every `0<beta<1/2`, the completed fleet02/B01 theorem gives the actual inequality

`boxed: H_beta(T)<=C_beta 2^(-beta/2)||z||_2^(-beta).`             (6.2)

At beta=1/4,

`H_(1/4)(T)<=4.6725514573 ||z||_2^(-1/4).`                        (6.3)

Theorem 3.1 upgrades precisely this same residual to the endpoint

`H_(1/2)(T)<=2^(11/4)||z||_2^(-1/2)`                              (6.4)

because the hub square is exactly zero after the rank-one pair completion. Thus the newest partner result is used quantitatively, and the new theorem identifies a concrete structural condition under which its sub-half family can be spent at the missing endpoint.

## 7. Target-valid stress family: every individual overlap-two minor vanishes, aggregate compiler stays uniform

For m>=2 take three disjoint physical banks U,V,W with sizes

`|U|=|V|=m`, `|W|=N=m^3`,

and let u,v,w be their normalized all-ones vectors. Set

`L=m^(3/2)`,
`A_m= u u^T + L(v w^T+w v^T)`.                                   (7.1)

The nonzero spectrum is exactly

`{1,L,-L}`,                                                       (7.2)

so every A_m lies in the exact QFORM target.

Choose S={one U-coordinate, one V-coordinate}. Then

`B=diag(1/m,0)`, `a=1/m`,

and z is the V-to-W row, whose N entries all equal `m^(-1/2)`. Therefore

`||z||_2=m`.                                                       (7.3)

The direct singular-pair compiler gives, for **every** admissible cap-one product law,

`boxed: ||p_(X^T A_m X)||_infinity <=2^(11/4)=6.7271713221...`    (7.4)

uniformly in m.

For distinct k,l in W, however,

`det A_m[S union {k},S union {l}] = -1/m^2 ->0`.                  (7.5)

There are N(N-1) ordered such pairs, and their exact aggregate star is

`W2(S)=N(N-1)/m^4=m^2-1/m`.                                      (7.6)

Thus (5.3) also gives

`||p_Q||_infinity <=8 [m^3/(m^3-1)]^(1/8)`,                       (7.7)

uniformly as every individual overlap-two minor tends to zero. This is exactly the desired aggregate-before-reciprocal-payment behavior.

On the same residual, the latest partner theorem gives from `F(T)>=2m^2`

`H_beta(T)<=C_beta 2^(-beta/2)m^(-beta)`,                          (7.8)

while the new endpoint theorem gives `H_(1/2)(T)<=2^(11/4)m^(-1/2)`.

As an additional independent control, the joint Fresnel--Brascamp--Lieb Theorem F from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` applies to (7.1): use eigenvectors u,(v+w)/sqrt(2),(v-w)/sqrt(2), eigenvalues 1,L,-L, and all physical coordinates as the active set. The Gram matrix is I_3 and the row leverages are 1/m on U,V and 1/N on W, all <=1/2. It gives the stronger family-specific estimate

`||p_Q||_infinity <=12(L^2)^(-1/3)=12/m`.                         (7.9)

The point of (7.4)-(7.7), however, is that they use only the singular pair and its aggregate overlap-two star and remain valid with arbitrary additional outside curvature not covered by this special rank-three diagonalisation.

## 8. Verification and status

`CHECK.py` and the executed `CHECK.txt` beside this report verify symbolically the bordered-determinant identity and the rank-one adjugate factorisation, and verify the stress-family formulas for m=2,3,4,10. The output ends `STATUS=PASS`. These checks are regression evidence only; Sections 3-7 contain the proofs.

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This run proves a supporting endpoint theorem and closes the exact rank-one physical-pair overlap-two receiver. Essential boundedness is established in that scope; continuity is not claimed.

The first unpaid implication is now `QFORM-OVERLAP2-PAIRBASE-ROUTING-v2`: from global overlap-two exterior mass, route quantitatively to one of (i) a definite invertible pair, (ii) an indefinite invertible pair with the existing pair-log/quarter-Riesz payment, (iii) the exact rank-one compiler proved here, or (iv) an already-paid diffuse rank-three/ridge/grouped/hub/null branch, without requiring a single large physical minor. In particular, the remaining structural issue is quantitative control through *near*-singular invertible pair bases; exact singularity is no longer an analytic obstruction.
