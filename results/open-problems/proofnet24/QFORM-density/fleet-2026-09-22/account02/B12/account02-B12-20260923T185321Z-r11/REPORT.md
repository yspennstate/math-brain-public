SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T18:53:21Z.
attacking: six-mode destructive square-Gram stability, closing the intermediate self-block regime by an ORIGINAL-coordinate physical pair and the low-self regime by the source-pinned fifth-volume receiver.

# account02/B12 r11 — destructive-Gram six-mode pair hybrid

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Claim: `QFORM-DESTRUCTIVE-GRAM-SIX-MODE-PAIR-HYBRID-v1`  
Status: **PROVED SUPPORTING STABILITY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED.**  
Continuity: **not claimed for the theorem as a whole**. The D5 branch has a continuous `C_0` density; the projected-gradient and physical-pair branches used below establish absolute continuity and an essential `L^infinity` bound.

The exact owner target remains: independent real inputs with scalar densities bounded by one, arbitrary symmetric coefficient matrix with at least three eigenvalues of modulus at least one, no moments/support/log-concavity/iid/diagonal-basis assumption, and no independence after spectral rotation.

## 1. First unpaid implication

The first unpaid implication is structural, not probabilistic:

> Starting from bare `s_3(A)>=1`, force either a bounded ORIGINAL-coordinate carrier with six square-energy modes at a universal scale after hostile added spectrum is charged by its actual destructive carrier footprint, or route the failure into an already-paid projected-crossing / grouped-bank / hub / ridge / Schur exit.

This run does **not** prove that extraction. It proves the six-mode receiver and its stability under arbitrary signed additions plus an arbitrary small dense tail.

## 2. Source-valid premises actually consumed

### 2.1 Pinned newest-Claude fifth-volume theorem

From

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

and the companion `RESULTS.md`, for an ACTUAL original-coordinate cross block `M`,

`Z_5=e_5(M^T M)`,

one has

`||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10)`.                  (2.1)

There is **no row-marginal condition** in this `D_5` theorem. Same-bank quadratic terms, outside couplings and affine terms are retained. In particular, if `s_5(M)>=u>0`, then

`Z_5 >= u^10`

and hence

`boxed: ||p_Q||_infinity <= 5 sqrt(2e)/u.`                     (2.2)

This will be applied below to the actual final physical cross block, not to a rotated law.

### 2.2 Latest designated partner account03/B12

The latest compatible account03/B12 report read in this run is

`yspennstate/math-open-problems@b4745ece98fa3839cf7afe35d829d08384c815b4`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T184647Z-qform-eigenvalue-r39/REPORT.md`.

For a final physical split `H direct_sum H^c`, write

`A=[[C,B],[B^T,D]]`.

The partner proves the exact identity

`(A^2)[H,H]=C^2+B B^T`                                         (2.3)

and, by Weyl for positive semidefinite sums, for positive integers `p,q` with `p+q=k+1`,

`boxed: s_p(C)^2+s_q(B)^2 >= lambda_k((A^2)[H,H]).`            (2.4)

The run below uses the previously unused six-mode specialization

`boxed: s_2(C)^2+s_5(B)^2 >= lambda_6((A^2)[H,H]).`            (2.5)

This is the equation-level use of the designated partner result.

### 2.3 Destructive square-Gram stability

From the completed account04/B12 theorem

`yspennstate/math-open-problems@c307f81b3196820aa711a5c47f243feeeeb74781`,

let `A_0,S` be arbitrary symmetric matrices, let `H` be an actual original-coordinate carrier, and put

`G_0=(A_0^2)[H,H]`,
`G=((A_0+S)^2)[H,H]`,
`N_H=[G_0-G]_+`.

Let `nu_1>=nu_2>=...` be the eigenvalues of `N_H`. For `k+r<=|H|`, and after any further symmetric matrix `T` with `||T||_op<=delta`,

`sqrt(lambda_k(((A_0+S+T)^2)[H,H]))`
` >= [sqrt((lambda_(k+r)(G_0)-nu_(r+1))_+) - delta]_+`.        (2.6)

No rank, sign or norm restriction is imposed on `S`; only its **actual destructive square-Gram footprint** is charged. The dense `T` is paid only through the deterministic matrix norm in (2.6).

### 2.4 Physical receivers

The finite physical-core projected-gradient theorem at

`yspennstate/math-open-problems@7f2c9f4c2dfeb6134d9291eb7e83b62a9cb4b3b0`

gives, on an `m`-coordinate original block having three eigenvalues of modulus at least `a>0`, after arbitrary affine terms,

`||p||_infinity <= 2 sqrt(6 pi m)/a`.                          (2.7)

The arbitrary-rank indefinite physical-pair theorem at

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

gives, for an invertible indefinite original-coordinate pair `P`, with

`D_P=|det P|`, `kappa=sigma_min(P)`, and `s_3(A)>=s>0`,

`||p||_infinity <= 3*400^(1/3)*(D_P^2*kappa*s)^(-1/6)`.        (2.8)

It retains arbitrary remaining spectrum and all induced affine terms.

## 3. A top-two self block forces a physical pair

Let `C=C^T` be an `m x m` matrix and let

`N_2=binom(m,2)`.

### Lemma 3.1 — rank-two Pluecker extraction with an operator tail

If

`s_2(C)>=b`, `s_3(C)<a`,                                      (3.1)

then some ORIGINAL-coordinate pair `I={i,j}` obeys

`boxed: sigma_min(C[I,I]) >= b/N_2-a.`                         (3.2)

### Proof

Let `lambda_1,lambda_2` be the two eigenvalues of `C` having largest absolute values, with orthonormal eigenvectors `u,v`. Write

`C_2=lambda_1 uu^T+lambda_2 vv^T`, `E=C-C_2`.

Then

`||E||_op=s_3(C)<a`.                                           (3.3)

The Pluecker identity gives

`sum_(i<j) (u_i v_j-u_j v_i)^2=1`.                            (3.4)

Hence some pair `I={i,j}` satisfies

`w_I^2=(u_i v_j-u_j v_i)^2 >=1/N_2`.                          (3.5)

For `K=C_2[I,I]`, direct expansion gives

`det K=lambda_1 lambda_2 w_I^2`.                              (3.6)

Also `||K||_op<=||C_2||_op=s_1(C)`. Therefore

`sigma_min(K)=|det K|/sigma_max(K)`
` >= s_1(C)s_2(C)/(N_2 s_1(C))`
` >= b/N_2`.                                                   (3.7)

The principal compression of `E` has norm at most `a`, so Weyl gives

`sigma_min(C[I,I]) >= b/N_2-a`.                               (3.8)

QED.

This lemma is sign-free. The pair can be definite or indefinite, and no rotated random coordinate is introduced.

## 4. Six physical square-energy modes are enough

### Theorem 4.1 — `QFORM-SIX-SQUARE-MODE-PAIR-COMPILER-v2`

Let `H` consist of `m>=6` ORIGINAL coordinates. Suppose a real symmetric final matrix `A` satisfies

`lambda_6((A^2)[H,H]) >= g^2>0`.                              (4.1)

Let

`N_2=binom(m,2)`.

Then every independent cap-one product source has an essentially bounded quadratic-form density, with

`boxed:
 ||p_(X^T A X)||_infinity <= C_m/g`,                            (4.2)

where one explicit constant is

`C_m=max{`
`  8 N_2 sqrt(6 pi m),`
`  4 pi N_2,`
`  3*400^(1/3)*(4N_2)^(5/6),`
`  10 sqrt(2e/3)`
`}.`                                                           (4.3)

No condition is imposed on the number, signs, magnitudes or locations of any other eigenvalues.

### Proof

Write the final physical split as in (2.3), and set

`b=g/2`, `a=g/(4N_2)`, `kappa=g/(4N_2)`.                      (4.4)

By the designated partner profile (2.5),

`s_2(C)^2+s_5(B)^2>=g^2`.                                     (4.5)

There are two main cases.

#### Case A: `s_2(C)<b`

Then (4.5) gives

`s_5(B)>=sqrt(g^2-b^2)=sqrt(3)g/2`.                           (4.6)

Apply the source-pinned fifth-volume theorem (2.2) to the **actual final** original-coordinate cross block `B`:

`boxed:
 ||p_Q||_infinity
 <= 5sqrt(2e)/(sqrt(3)g/2)
 =10sqrt(2e/3)/g.`                                             (4.7)

This is a real inequality from the required `e5f71d79...` source, with no marginal/leverage hypothesis.

#### Case B: `s_2(C)>=b`

If `s_3(C)>=a`, condition on every coordinate outside the original set `H`. Inside `H` the inputs remain independent with density caps one, while the exterior contributes only affine and constant terms. The projected-gradient receiver (2.7) gives

`||p_Q||_infinity`
` <=2sqrt(6 pi m)/a`
` =8N_2 sqrt(6 pi m)/g`.                                      (4.8)

It remains to treat

`s_2(C)>=b`, `s_3(C)<a`.                                      (4.9)

Lemma 3.1 gives an ORIGINAL-coordinate pair `I` with

`sigma_min(C[I,I])>=b/N_2-a`
` =g/(4N_2)=kappa`.                                            (4.10)

If this pair is definite, condition on all other original coordinates and complete the square. Under the linear change `z=|C[I,I]|^(1/2)(x+x_0)`, the two-dimensional joint density is at most `|det C[I,I]|^(-1/2)`. Polar coarea for `|z|^2` gives

`||p_Q||_infinity <= pi/|det C[I,I]|^(1/2)`
` <=pi/kappa`
` =4 pi N_2/g`.                                                (4.11)

If the pair is indefinite, let `D_P=|det C[I,I]|`. From (4.10),

`D_P>=kappa^2`.                                                 (4.12)

Also

`lambda_6((A^2)[H,H])=s_6(A P_H)^2>=g^2`.

Since `(A^2)[H,H]` is a principal compression of `A^2`, Cauchy interlacing gives

`s_6(A)>=g`, hence `s_3(A)>=g`.                                (4.13)

Apply (2.8) with `s=g` and (4.12):

`||p_Q||_infinity`
` <=3*400^(1/3)*(kappa^5 g)^(-1/6)`
` =3*400^(1/3)*(4N_2)^(5/6)/g`.                               (4.14)

The cases are exhaustive, proving (4.2)-(4.3). QED.

### Why this matters

The latest partner's compact compiler uses seven square-energy modes so that either a three-mode self block or five cross singular directions survive directly. Theorem 4.1 closes the missing six-mode configuration: when two self singular directions survive but the third does not, the rank-two geometry itself forces a usable **physical pair**.

## 5. Stability under arbitrary signed spectral additions and a dense tail

### Theorem 5.1 — `QFORM-DESTRUCTIVE-GRAM-SIX-MODE-PAIR-HYBRID-v1`

Let `A_0,S,T` be arbitrary real symmetric `n x n` matrices and let `H` be `m` original coordinates. Define

`G_0=(A_0^2)[H,H]`,
`G=((A_0+S)^2)[H,H]`,
`N_H=[G_0-G]_+`,                                               (5.1)

and let `nu_1>=nu_2>=...>=0` be the eigenvalues of `N_H`. Suppose

`6+r<=m`, `||T||_op<=delta`,                                  (5.2)

and put

`g=[sqrt((lambda_(6+r)(G_0)-nu_(r+1))_+) - delta]_+`.         (5.3)

If `g>0`, then for every independent cap-one product input,

`boxed:
 ||p_(X^T(A_0+S+T)X)||_infinity <= C_m/g`,                    (5.4)

with `C_m` from (4.3).

If `rank N_H<=r`, this simplifies to

`g=[sqrt(lambda_(6+r)(G_0))-delta]_+`.                         (5.5)

### Proof

Apply the completed destructive square-Gram theorem (2.6) with `k=6`:

`sqrt(lambda_6(((A_0+S+T)^2)[H,H]))>=g`.                      (5.6)

Theorem 4.1 applies to the actual final matrix `A=A_0+S+T`. QED.

### Interpretation

`S` can be full rank, indefinite, arbitrarily large in operator norm and can add or replace arbitrarily many eigenvalues. Only its actual **destructive** effect on the carrier square Gram is charged. Positive or orthogonal-completion square energy is free. The final dense tail `T` may be fully nonseparable and full rank; it is charged only by `delta` in the deterministic matrix inequality (5.6).

No step claims that small `||T||_op` makes the random variable `X^T T X` small. That claim is false for unbounded cap-one sources.

## 6. Exact target-class stress family: six modes suffice where the seven-mode reserve is unavailable

Take eight original carrier coordinates

`H={h_1,...,h_8}`,

six outside partner coordinates

`J={j_3,j_4,j_5,j_6,k_1,k_2}`,

and an arbitrary spectator space `S_0` of dimension `d>=0`.

Define the baseline `A_0` by the mutually disjoint pieces

`A_0(h_1,h_1)=2`,
`A_0(h_2,h_2)=-2`,                                             (6.1)

`A_0(h_l,j_l)=A_0(j_l,h_l)=2`, `l=3,4,5,6`,                   (6.2)

`A_0(h_7,k_1)=A_0(k_1,h_7)=2`,
`A_0(h_8,k_2)=A_0(k_2,h_8)=2`,                                (6.3)

and put `A_0=2I` on the spectator space. All other baseline entries vanish.

The eight carrier columns of `A_0` are mutually orthogonal and have norm two, so

`G_0=(A_0^2)[H,H]=4I_8`.                                      (6.4)

Now choose arbitrary real `tau_1,tau_2` and an arbitrary real symmetric spectator matrix `Theta` of arbitrary dimension. Let the added spectrum `S` change only

`2 -> 2+tau_1` on the `(h_7,k_1)` hyperbolic coefficient,
`2 -> 2+tau_2` on the `(h_8,k_2)` hyperbolic coefficient,       (6.5)

and replace the spectator block `2I` by `Theta`.

Each hyperbolic block has the fixed eigenvectors `(h_q+k_q)/sqrt2`, `(h_q-k_q)/sqrt2`; its two eigenvalues are literally changed from `+2,-2` to `+(2+tau_q),-(2+tau_q)`. Because the spectator baseline is the degenerate `2I`, the `d` spectator eigenvalues `+2` are replaced by the arbitrary real spectrum of `Theta`, with arbitrary internal mixing.

For `B=A_0+S`,

`(B^2)[H,H]`
` =diag(4,4,4,4,4,4,(2+tau_1)^2,(2+tau_2)^2)`.                (6.6)

Hence

`rank [G_0-(B^2)[H,H]]_+ <=2`                                 (6.7)

for **every** `tau_1,tau_2,Theta`, irrespective of their signs or magnitudes.

Finally add any symmetric, genuinely dense, full-rank-allowed tail `T` satisfying

`||T||_op<=1/64`.                                              (6.8)

Apply Theorem 5.1 with `m=8,r=2`. Since `lambda_8(G_0)=4`,

`boxed:
 sqrt(lambda_6(((B+T)^2)[H,H])) >= 2-1/64=127/64.`            (6.9)

Thus this entire family has a finite density cap from the six-mode compiler, uniformly in `tau_1,tau_2`, in the spectator dimension, in every eigenvalue of `Theta`, and in every dense tail obeying (6.8).

It is also literally in the owner's exact target class. Before `T`, the protected pieces (6.1)-(6.2) alone already contribute ten eigenvalues of modulus two: `+2,-2` from the two self coordinates and four pairs `+2,-2` from the fixed hyperbolic blocks. Therefore Weyl gives

`boxed: s_3(B+T)>=2-1/64=127/64>1.`                            (6.10)

### A strict six-mode obstruction to the carrier D5 / seven-mode route

At the simultaneous cancellation endpoint

`tau_1=tau_2=-2`, `T=0`,                                      (6.11)

the physical carrier cross block `A[H,H^c]` has rank exactly four, from (6.2). Therefore

`e_5(A[H,H^c]^T A[H,H^c])=0`.                                (6.12)

So the fifth-volume branch on this carrier gives no finite certificate. Also the latest partner's destructive **seven-mode** theorem with the same two spent destructive directions would require

`7+2<=|H|=8`,

which is false. The six-mode pair hybrid does apply.

In fact this family has a much sharper direct pair bound. The physical pair `{h_1,h_2}` is `diag(2,-2)` before `T`. Under every dense tail (6.8), the pair remains indefinite and both singular values are at least `127/64`. Together with (6.10), the arbitrary-rank physical-pair theorem gives

`boxed:
 ||p_Q||_infinity
 <= 3*400^(1/3)/(127/64)
 = 11.139118862030774... .`                                   (6.13)

This bound is uniform in arbitrarily many arbitrary spectator eigenvalue replacements and the two arbitrary signed hyperbolic replacements.

## 7. Explicit D5 branch on an actual target matrix

The required `e5f71d79...` result is not merely cited in the abstract proof. Keep the stress family above but set `tau_1=0`; leave `tau_2`, `Theta` and the spectator dimension completely arbitrary. Before the dense tail, the carrier cross block has at least five singular values equal to two: the four fixed couplings (6.2) plus `(h_7,k_1)`.

After any `T` satisfying (6.8), its actual final cross block changes in operator norm by at most `1/64`, so

`s_5(A[H,H^c])>=2-1/64=127/64`.                               (7.1)

Consequently

`e_5(A[H,H^c]^T A[H,H^c]) >= (127/64)^10`.                   (7.2)

The pinned D5 theorem gives the concrete final-matrix inequality

`boxed:
 ||p_Q||_infinity
 <= 5sqrt(2e)/(127/64)
 = 5.875008457567557... .`                                    (7.3)

All same-side curvature, the arbitrary spectator spectrum, the arbitrary second hyperbolic replacement, and the dense tail remain in the matrix. This is a product-preserving original-coordinate application.

## 8. Why the dense tail must stay at matrix level

For completeness, let

`T=delta e_1 e_1^T`,

and take `X_1` uniform on `[R,R+1]`, which is an admissible cap-one density. Then

`X^T T X=delta X_1^2 >= delta R^2`

almost surely. Thus there is no law-uniform implication

`||T||_op small => X^T T X small`.

The proof above never uses such an implication. It controls singular values and square-Gram compressions of the **actual final coefficient matrix**, then invokes receivers by conditioning only on original coordinates.

Likewise, no spectral rotation is used to manufacture independent inputs. Rotations appear only in deterministic matrix proofs (eigenvectors, singular values, Pluecker identity).

## 9. Remaining gap

The new theorem does not solve the full QFORM conjecture. The remaining unpaid implication is:

> From only `s_3(A)>=1`, derive a bounded original-coordinate carrier carrying six square-energy modes at a universal scale after the relevant hostile directions are spent, or force a quantitatively compatible already-paid projected-crossing / grouped-bank / hub / ridge / physical-core / Schur certificate.

The live correction `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` rules out simply demanding a uniformly positive one-sided singleton star aggregate from the three-large-eigenvalue hypothesis. Diffuse exact-rank families likewise rule out a universally good fixed principal minor. The extraction must therefore aggregate physical product structure rather than pick one favorable rotated or bounded coordinate object without proof.

## 10. Source pins and scope

- Required pinned newest-Claude source: `e5f71d79eff325201dd0274053d20268ce65b837` (`RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`).
- Latest designated partner account03/B12 used at equation (2.5): report read through `b4745ece98fa3839cf7afe35d829d08384c815b4`, theorem commit `005c80f70952024e3460260cb12936870f26d70e`.
- Destructive square-Gram stability: `c307f81b3196820aa711a5c47f243feeeeb74781`.
- Finite physical-core projected-gradient theorem: `7f2c9f4c2dfeb6134d9291eb7e83b62a9cb4b3b0`.
- Arbitrary-rank physical-pair theorem: `742ac943440e41925fe09db9a8c02a96cbd83dbc`.
- Preceding account02/B12 six-mode Pluecker proof: `e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`.
- Execution label: `WITHOUT_VERIFIED_BRAIN`.

No continuity claim beyond the individual receivers' proved scopes is made. No counterexample to the full conjecture was found.
