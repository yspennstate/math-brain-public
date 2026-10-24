SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-22T20:51:56Z.
attacking: a product-preserving one-zero-diagonal triple gate and its use in the heavy-null two-bank overlap branch; aggregate before reciprocal-minor payment and keep all outside couplings.

# account03/B04 r18 — one-zero-diagonal triple smoothing and a two-bank overlap gate

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15` at the final pre-publication refresh  
**Assignment:** Product Fourier rearrangement  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW TARGET-SUPPORTING THEOREMS / FULL TARGET OPEN`

## 0. Scope and correction boundary

The full target remains open: for independent real physical coordinates with probability densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential bound for the density of `Q=X^T A X`, or give a target-valid counterexample. No moment, support, log-concavity, Gaussian, diagonal-basis-independence, or post-rotation-independence hypothesis is added.

Fresh control and the correction inbox were reread immediately before publication. In particular this report does **not** use law-uniform pointwise van der Corput decay, the false arbitrary-joint rank-three coarea cap, positive conditional projected-density moments, a fixed-good-minor claim, or the false principle that a bounded conditional scalar cap can replace genuine independence.

The designated partner `account04/B04` still has no completed current-QFORM report or shared handoff in the source tree, so no partner result is fabricated. Compatible completed mathematics actually used below is:

1. account03/B11, `QFORM-HEAVY-NULL-SEPARATED-v1`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T182528Z-account03-B11-QFORM-r12/REPORT.md`, specifically its translation-stable hyperbolic-square rearrangement lemma;
2. account03/B19, `QFORM-DIFFUSE-2D-TWO-BANK-PARTITION-v1`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T203112Z-account03-B19-QFORM/REPORT.md`, which manufactures two disjoint original-coordinate transverse banks in the residual-diffuse heavy-null state;
3. account04/B16, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`, whose nested-heavy determinant-bank identity is used in Section 4 to sharpen its atom branch.

The local theorem below is reproved self-containedly, so the dependency on item 1 is a consistency/source pin rather than an omitted proof step.

## 1. The local rearrangement lemma

### Lemma 1.1 — translation-stable hyperbolic square

Let `S` be independent of a pair `(Y,Z)`. Assume `S` has a probability density bounded by `M`, and `(Y,Z)` has a joint probability density bounded by `H`. Let `a,b` be nonzero. For arbitrary measurable `F`,

`T=2a S Y+b Z^2+F(Y)`

has an essentially bounded density and

`||p_T||_infinity <= 3*2^(2/3) (MH)^(2/3)|a|^(-2/3)|b|^(-1/3).`    (1.1)

The same bound holds after an arbitrary determinant-one shear `Z -> Z+theta(Y)` and arbitrary translations of `(Y,Z)`.

#### Proof

Fix an output value `t`. For `r>0`, split according to `|Y|>=r` and `|Y|<r`.

On `|Y|>=r`, integrate in `S`; the affine Jacobian is `2|aY|`, so

`I_large <= M/(2|a|r).`                                            (1.2)

On `|Y|<r`, first use the pair cap `H`, then integrate the scalar density through the square-root kernel. The decreasing-rearrangement/bathtub estimate

`sup_A int_R f(A-z^2) dz <= 2 sqrt(M)`                              (1.3)

holds for every probability density `0<=f<=M`: after `u=z^2`, the kernel is `u^(-1/2)`, and the maximizing cap-`M` density fills the interval adjacent to the singularity. Scaling gives

`I_small <= 4 sqrt(2) H sqrt(M) sqrt(r)/sqrt(|ab|).`                (1.4)

Minimizing `A/r+B sqrt(r)` with `A=M/(2|a|)` and the displayed `B` yields exactly (1.1). This is the same rearrangement currency as the completed B11 lemma, and uses no pointwise Fourier decay. QED.

## 2. New full-matrix local theorem: only one diagonal entry must vanish

### Theorem 2.1 — `QFORM-ONE-ZERO-TRIPLE-v1`

Let `X_1,...,X_n` be independent real variables with probability densities at most one, and let `A` be any real symmetric `n x n` matrix; no rank assumption is imposed. Suppose there are distinct original-coordinate indices `i,j,k` such that

`A_ii=0`

and the physical principal block

`B=A_{ {i,j,k},{i,j,k} }`

is invertible. Then `Q=X^T A X` has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <= C_0 |det B|^(-1/3),`

where

`C_0=3*2^(2/3)=4.762203155904598... .`                              (2.1)

Arbitrary outside spectrum, arbitrary outside quadratic terms, and arbitrary couplings to the triple are allowed.

#### Proof

Condition on every original coordinate outside `{i,j,k}`. This preserves independence and the density caps of the three selected coordinates. All outside interactions become affine terms, so it suffices to prove a bound uniform over those affine coefficients.

Write `S=X_i` and `x=(X_j,X_k)^T`. The conditional polynomial has the form

`T=2S d^T x + x^T Cx + ell_0 S + ell^T x + r_0`,                    (2.2)

where `d=(A_ij,A_ik)^T` and `C` is the lower-right `2 x 2` block of `B`. Since `det B!=0`, necessarily `d!=0`. Put `a=||d||_2>0` and choose a `2 x 2` orthogonal matrix `O` whose first column is `d/a`. Define

`(y,z)^T=O^T x`.                                                     (2.3)

The original pair `(X_j,X_k)` has joint density at most one. Orthogonal transformation preserves Lebesgue measure, so `(y,z)` also has joint density at most one. It may be dependent; no independence is claimed or needed.

In the coordinates `(S,y,z)`, the quadratic block is

`B'=[[0,a,0],[a,alpha,beta],[0,beta,gamma]].`                       (2.4)

Hence

`det B=det B'=-a^2 gamma`.                                           (2.5)

In particular `gamma!=0`.

The affine term `ell_0 S` is absorbed by translating `y`:

`Y=y+ell_0/(2a)`.                                                    (2.6)

Translations preserve the joint density cap. After collecting the remaining affine terms, the conditional polynomial is

`T=2a S Y + alpha_1 Y^2+2 beta_1 Y z+gamma z^2+eta_1Y+eta_2 z+r_1`.

Complete the square in `z`:

`gamma z^2+2 beta_1Yz+eta_2z
 =gamma [z+(beta_1/gamma)Y+eta_2/(2gamma)]^2 + H_1(Y)`.             (2.7)

The map `(Y,z)->(Y,Z)` in (2.7) is a determinant-one shear plus translation, hence the joint density of `(Y,Z)` is still at most one. The scalar `S` remains independent of that pair and has density at most one. Lemma 1.1 with `M=H=1`, hyperbolic coefficient `a`, and square coefficient `gamma` gives

`||p_(T | X_{outside})||_infinity
 <=3*2^(2/3) a^(-2/3)|gamma|^(-1/3)`
` =3*2^(2/3)|det B|^(-1/3)`                                       (2.8)

by (2.5). The bound is uniform in every conditioned outside value. Mixing therefore gives (2.1), together with absolute continuity. QED.

### Why this is stronger than the existing zero-diagonal atom gate

The completed account04/B16 atom theorem required an invertible physical triple with **all three** selected diagonal entries zero. Theorem 2.1 requires only one zero diagonal entry and allows the other two diagonals and all outside couplings to be arbitrary. It also gives the slightly smaller determinant constant `3*2^(2/3)=4.76221...` on this one-zero branch.

This theorem is not a fixed-good-minor reduction: it says what is obtained **if** a determinant atom exists. It does not assert that the target hypotheses force one atom of universal size.

## 3. Exact-rank-three interpretation and Pluecker atom payment

Let

`A=R Lambda R^T`, `R^T R=I_3`,

have exact rank three. Suppose physical row `i` is an exact null pivot. After a spectral rotation write

`r_i=sqrt(h)e_1`, `h>0`,

and each complementary row as

`r_m=(alpha_m,beta_m,gamma_m)`.

For a pair `j,k`, define its transverse Pluecker weight

`w_jk=(beta_j gamma_k-beta_k gamma_j)^2`.                            (3.1)

Then

`det(R_{ {i,j,k} })^2=h w_jk`,

and exact rank three gives

`|det A_{ {i,j,k} }|=|det Lambda| h w_jk`.                          (3.2)

Theorem 2.1 therefore yields, for every pair with `w_jk>0`,

`boxed: ||p_Q||_infinity
 <=3*2^(2/3)(|det Lambda| h w_jk)^(-1/3).`                          (3.3)

If every nonzero eigenvalue of `Lambda` has modulus at least `s` and `h>1/2`, then `|det Lambda|>=s^3` and

`boxed: ||p_Q||_infinity < 6 s^(-1) w_jk^(-1/3).`                  (3.4)

No scalar curvature condition on rows `j,k` is needed. In particular the old requirement that the whole triple be zero-diagonal disappears.

### Consequence for a diffuse determinant bank

For a heavy exact-null row, the total exact-rank-three determinant mass is

`sum_{j<k, j,k!=i}|det A_{ {i,j,k} }|=|det Lambda| h`,              (3.5)

by Cauchy--Binet. Thus any atom carrying a fraction `tau` of this total immediately gives

`||p_Q||_infinity <=3*2^(2/3)(tau |det Lambda|h)^(-1/3).`           (3.6)

The unresolved state is therefore forced farther into a genuinely diffuse angular regime where every transverse Pluecker atom is small.

## 4. A completed account04 result applied to an actual inequality

The exact assigned `account04/B04` result is absent, but completed compatible account04/B16 proves that in its nested-heavy exact-rank-three state a fixed pair `(i,j)` carries a determinant bank

`sum_k |det A_{ {i,j,k} }|=|det Lambda| c h_res > |det Lambda|/4`.  (4.1)

Assume here that the distinguished heavy row `i` is also an exact null pivot, `A_ii=0`. If one normalized bank atom has weight at least `tau`, then

`|det A_{ {i,j,k} }| > tau |det Lambda|/4`.                         (4.2)

Applying Theorem 2.1 to this actual physical triple gives

`boxed: ||p_Q||_infinity
 <3*2^(2/3)(4/(tau |det Lambda|))^(1/3).`                           (4.3)

At target scale `|det Lambda|>=1` and `tau>=1/8`,

`||p_Q||_infinity <3*2^(2/3) 32^(1/3)
 =15.119052598738476... .`                                         (4.4)

Unlike the earlier account04/B16 atom gate, (4.4) needs **no assumptions at all on `A_jj` or `A_kk`**. Thus every heavy determinant atom in the heavy-null nested branch is now paid; the residual nested-heavy state must have all determinant-bank atoms diffuse.

## 5. Applying the new B19 two-bank theorem to genuine overlap

The newest completed account03/B19 result proves that in the residual-diffuse heavy-null state the transverse rows `v_m=(beta_m,gamma_m)` admit a partition into disjoint original-coordinate banks `J,K` such that

`det S_J>=1/640`, `det S_K>=1/640`,

where

`S_G=sum_{m in G} v_m v_m^T`.                                      (5.1)

The two banks are genuinely independent. The remaining difficulty identified there is longitudinal leakage `alpha_m` inside those same banks.

The following theorem pays a nontrivial overlap subbranch; it is not support separation.

### Theorem 5.1 — `QFORM-TWOBANK-TRANSVERSE-GENERATED-LEAKAGE-v1`

Use the exact heavy-null normal form

`M=[[0,kappa,0],[kappa,d,e],[0,e,c]],`

with heavy physical row `sqrt(h)e_1`, `h>1/2`, and write complementary rows as `(alpha_m,beta_m,gamma_m)`. Let `J,K` be any disjoint original-coordinate partition with `S_J` positive definite. Suppose the longitudinal leakage in bank `J` is generated by its two transverse coefficient vectors:

`(alpha_m)_{m in J}=p (beta_m)_{m in J}+q (gamma_m)_{m in J}`        (5.2)

for some real `p,q`. Then

`boxed: ||p_Q||_infinity
 <=3*2^(4/3)(det S_J)^(-1/3) h^(-1/3)|det M|^(-1/3).`               (5.3)

Consequently, in the B19 partition with `det S_J>=1/640`, if (5.2) holds for either bank and every nonzero eigenvalue of `M` has modulus at least `s`, then

`boxed: ||p_Q||_infinity
 <3*2^(5/3) 640^(1/3) s^(-1)
 =82.07884544048144... s^(-1).`                                    (5.4)

This permits complete original-coordinate overlap of the leakage and transverse forms inside bank `J`; only the coefficient-span relation (5.2) is required.

#### Proof

Write the spectral linear forms as

`T=sqrt(h)X_i+U_J+U_K`,
`W=W_J+W_K`,
`V=V_J+V_K`,

with the obvious bank sums. Condition on every coordinate in bank `K` (and on any additional outside coordinates, if present). The `K`-quantities are now constants, while `X_i` remains independent of the entire `J` bank.

By (5.2), after replacing `W_J,V_J` by their translated totals `Y=W_J+const`, `Z=V_J+const`,

`U_J=pY+qZ+const`.                                                   (5.5)

Hence the conditional quadratic form is

`2 kappa sqrt(h) X_i Y`

plus a general quadratic-affine polynomial in `(Y,Z)`. Crucially, because the first spectral coordinate is null, the coefficient of `Z^2` remains exactly `c`: the leakage term `2 kappa U_J Y` changes only the `Y^2`, `YZ`, and linear coefficients. Therefore a determinant-one shear in `(Y,Z)` rewrites the remainder as

`c Z_tilde^2+F(Y)`.                                                 (5.6)

The pair `(W_J,V_J)` has a quantitative joint-density cap. Let `C_J` be the matrix with rows `(beta_m,gamma_m)`, so `C_J^T C_J=S_J`. Whiten it: `R_J=C_J S_J^(-1/2)` has orthonormal columns. The completed two-dimensional product-projection theorem gives the normalized projection density a cap `2`; scaling back gives

`H_J<=2 (det S_J)^(-1/2).`                                         (5.7)

Apply Lemma 1.1 conditionally with scalar cap `M=1`, pair cap `H=H_J`, hyperbolic coefficient `a=kappa sqrt(h)`, and square coefficient `b=c`. Since

`det M=-kappa^2 c`,                                                 (5.8)

we obtain

`||p_(Q | K)||_infinity
 <=3*2^(2/3)[2(det S_J)^(-1/2)]^(2/3)
   h^(-1/3) kappa^(-2/3)|c|^(-1/3)`
` =3*2^(4/3)(det S_J)^(-1/3)h^(-1/3)|det M|^(-1/3).`                (5.9)

The bound is independent of the conditioned bank values, so mixing proves (5.3). If `h>1/2`, `det S_J>=1/640`, and `|det M|>=s^3`, then (5.4) follows. QED.

### Structural consequence

If one B19 bank consists of exactly two original coordinates, condition (5.2) is automatic because its two transverse coefficient vectors span `R^2`; equivalently Theorem 2.1 applies directly to that two-row bank. Thus any still-unpaid B19 two-bank state must either have both banks of cardinality at least three or have nonzero longitudinal leakage components orthogonal to each bank's transverse two-plane. The overlap obstruction is now localized to those orthogonal residual leakage components.

## 6. Explicit genuinely rotated indefinite target example

Take the `5 x 3` Parseval frame with rows

`r_0=(sqrt(3)/2,0,0),`
`r_1=(1/4,1/sqrt(2),0),`
`r_2=(1/4,0,1/sqrt(2)),`
`r_3=(-1/4,1/sqrt(2),0),`
`r_4=(-1/4,0,1/sqrt(2)).`                                           (6.1)

A direct calculation gives `R^T R=I_3`. Let

`M=[[0,1,0],[1,0,0],[0,0,1]],`                                     (6.2)

whose eigenvalues are `{1,1,-1}`, and set `A=RMR^T`. Then `A` is genuinely rotated and indefinite; explicitly

`A=[[0,sqrt(6)/4,0,sqrt(6)/4,0],`
`   [sqrt(6)/4,sqrt(2)/4,sqrt(2)/8,0,-sqrt(2)/8],`
`   [0,sqrt(2)/8,1/2,sqrt(2)/8,1/2],`
`   [sqrt(6)/4,0,sqrt(2)/8,-sqrt(2)/4,-sqrt(2)/8],`
`   [0,-sqrt(2)/8,1/2,-sqrt(2)/8,1/2]].`                            (6.3)

Its three nonzero eigenvalues are exactly `{1,1,-1}`. The first physical pivot is zero and has leverage `h=3/4`. Choose the original-coordinate pair `{1,2}`. Its transverse vectors are `(1/sqrt(2),0)` and `(0,1/sqrt(2))`, so

`w_12=1/4`,

and their longitudinal coefficients `(1/4,1/4)` overlap the same two physical variables. This is not the support-separated theorem.

Theorem 2.1 / (3.3) gives, for **every** admissible choice of the five independent input densities,

`boxed: ||p_(X^T A X)||_infinity
 <=3*2^(2/3)(3/16)^(-1/3)
 =4*3^(2/3)
 =8.320335292207616... .`                                          (6.4)

Thus the new estimate applies to a genuinely rotated indefinite rank-three target with explicit constant and genuine same-coordinate leakage overlap.

The argument proves absolute continuity and essential boundedness. It does **not** separately prove continuity of the density for this branch.

## 7. What remains unpaid

Theorem 2.1 removes a real artificial restriction: a determinant atom touching an exact-null pivot no longer needs the other two physical diagonals to vanish. Theorem 5.1 also pays a genuine overlap branch of the B19 two-bank state.

The first remaining B04 implication is now:

**`QFORM-TWOBANK-ORTHOGONAL-LEAKAGE-AGGREGATION-v1`.** In the B19 residual-diffuse heavy-null state, decompose each bank's longitudinal coefficient vector into its transverse span plus an orthogonal residual,

`alpha_G=p_G beta_G+q_G gamma_G+eta_G`, `eta_G perpendicular span{beta_G,gamma_G}`.

Theorem 5.1 closes the branch `eta_J=0` or `eta_K=0`. The unpaid case has **both** `eta_J!=0` and `eta_K!=0`. Prove a dimension-free product-space/rearrangement inequality that aggregates these two residual leakage forms before taking reciprocal local coefficients. One must use their original-coordinate product provenance; replacing them by conditional density caps is forbidden by the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`.

A promising exact representation is to keep the two banks independent and use the orthogonal decomposition inside each bank before integrating the hyperbolic singularity. The determinant cancellation `kappa^2|c|=|det M|` should remain untouched. If three successive substantive runs fail on that precise splice, change FEI/QFORM mechanism as required rather than repeating the same conditional-cap attempt.

## 8. Status

Proved this run:

- `QFORM-ONE-ZERO-TRIPLE-v1`, valid for arbitrary full matrices and arbitrary outside couplings;
- the exact Pluecker/determinant atom inequality (3.3), removing all-zero-diagonal eligibility from the heavy-null atom gate;
- the strengthened account04/B16 nested-heavy atom inequality (4.3)-(4.4);
- `QFORM-TWOBANK-TRANSVERSE-GENERATED-LEAKAGE-v1`, a genuine same-coordinate overlap branch with explicit universal constants;
- the explicit rotated indefinite example (6.3)-(6.4).

Not proved: diffuse determinant-bank aggregation when every atom is small, the two-bank case with nonzero orthogonal residual leakage in both banks, arbitrary exact-rank-three closure, the extension through every additional-spectrum configuration, or the full owner conjecture.

**Full QFORM conjecture: OPEN / NOT PROVED.**
