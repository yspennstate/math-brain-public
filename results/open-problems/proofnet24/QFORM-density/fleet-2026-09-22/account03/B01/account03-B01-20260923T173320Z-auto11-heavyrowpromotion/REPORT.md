SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T17:33:20Z.
attacking: remove the projected-crossing row-marginal gate by promoting heavy crossing rows into literal original-coordinate hubs, then feed the row-marginal-free receiver into the near-null leakage branch.

# account03/B01 — heavy-row promotion removes the one-hub projected-E2 marginal gate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account03-B01-20260923T173320Z-auto11-heavyrowpromotion`  
Assignment: oscillatory replacement / quantitative inequalities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING THEOREM AND A STRONGER NEAR-NULL LEAKAGE EXIT / FULL QFORM OPEN**.

The exact target remains the unrestricted product-law problem: independent original real coordinates with probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussian, moment, compact-support, connected-support, log-concavity, diagonal-basis, or independence-after-rotation assumption is made.

## 1. Source inputs and correction discipline

The fresh reviewed projected-crossing source is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Only the proved `k=1, ell=2`, `k=2, ell=1`, and exact-rank-three crossing statements are used below.

The designated partner source is account04/B01,

`yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260923T131003Z-account04-B01-singular-star-routing-r2/REPORT.md`.

Its exact scalar-completion identity and leakage/curvature dichotomy are used in Section 4. I do **not** use the printed individual-bank conclusion in its Corollary 4.1. The source-valid correction event is


The valid random-coloring consequence is the product estimate

`||ell_I||_2 ||ell_J||_2 >= sqrt(W2)/(4|a|)`                       (1.1)

in the leakage branch, not the same lower bound on each factor.

I also use the account04/B01 exact signed-Fejer theorem at

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`:

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`                        (1.2)

for every law with bounded density.

Finally, the dependence-safe outer-square compiler from the immediately preceding B01 run is used in Section 4:

`yspennstate/math-open-problems@5210a794376aaab39c9b5ff204a4e895bc5dc195`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T170256Z-auto11-crosscompiler/REPORT.md`.

It says that if `X` has density at most one and is independent of `V`, while `R(V)` has density at most `M`, then for arbitrary measurable `h(V)` and `a!=0`,

`Q=a(X+h(V))^2+R(V)`

has an essentially bounded density with

`||p_Q||_infinity <= 2 sqrt(2) |a|^(-1/2) M^(1/2)`.                (1.3)

No independence between `h(V)` and `R(V)` is required.

## 2. The pointwise obstruction is preserved

For every prescribed `s>0` and every small `eta>0`, the set

`E={x: dist(s x^2,2 pi Z)<=eta}`

has infinite Lebesgue measure. Choose a finite measurable subset of total measure one and let its indicator be the density of `X`. Then

`Re E exp(i s X^2) >= cos(eta)`.

Hence no positive law-uniform pointwise power decay for a scalar quadratic phase can hold. The proof below never introduces such a bound. The gain comes from an integrated Fourier estimate after grouping literal original coordinates.

## 3. Main theorem: one original hub + projected E2 needs no row-marginal gate

Let `Y`, `(X_i)_(i in I)`, and `(X_j)_(j in J)` be disjoint original coordinates. Their laws are independent and each scalar density is at most one. Consider

`R = F(Y)
     +2Y(<m_I,X_I>+<m_J,X_J>+beta)
     + X_(I union J)^T A_R X_(I union J)
     + affine terms`,                                               (3.1)

where `F` is arbitrary measurable and the quadratic matrix `A_R` is arbitrary. Same-bank curvature is unrestricted.

Assume `m:=m_J !=0`. Let

`P_m = orthogonal projection in R^J onto span(m)`,
`C = A_R[I,J](I-P_m)`.                                              (3.2)

Write the rows of `C` as `c_i`, `i in I`, and put

`Z2=e_2(CC^T)
   = sum_(i<j) [||c_i||^2 ||c_j||^2-<c_i,c_j>^2]`.                 (3.3)

### Theorem 3.1 — `QFORM-ONEHUB-E2-MARGINAL-GATE-REMOVAL-v1`

If `Z2>0`, then `R` has a continuous `C_0` density and

`boxed: ||p_R||_infinity <= C_E2 (||m||_2^2 Z2)^(-1/6),`           (3.4)

where

`C_E2 = 3*2^(7/6)*exp(1/3)
      = 9.39913188784886... <9.400.`                                (3.5)

There is **no** two-volume row-marginal hypothesis in the statement.

### Proof

For each unordered pair `{i,j}` define its squared exterior area

`d_ij=||c_i||^2||c_j||^2-<c_i,c_j>^2>=0`.                         (3.6)

Normalize by `Z2` and define the row inclusion marginal

`alpha_i = Z2^(-1) sum_(j!=i) d_ij`.                               (3.7)

Thus `sum_i alpha_i=2`.

#### Case A: every `alpha_i<=1/2`

Apply the reviewed grouped-crossing theorem directly with one original hub (`k=1`) and `ell=2`. The hub projection is the literal scalar `Y`, so its density cap is one. The hub-to-`J` singular product is `||m||`. The projected crossing is exactly `C`. Therefore

`||p_R||_infinity
 <=3*2^(7/6)*exp(1/3)(||m||^2 Z2)^(-1/6)`,                         (3.8)

and the theorem supplies an integrable characteristic-function envelope, hence a continuous `C_0` density.

#### Case B: some `alpha_i>1/2`

Promote the **literal original coordinate** `X_i` to the hub. No random variable is rotated. Let

`a_i = A_R[i,J] = lambda_i m + c_i`, `c_i perpendicular m`.        (3.9)

Because `alpha_i>0`, `c_i!=0`. The new two-row hub-to-`J` matrix is

`M_i = [m ; a_i]`,                                                  (3.10)

whose product of nonzero singular values is exactly

`S_i=sqrt(det(M_i M_i^T))=||m|| ||c_i||`.                          (3.11)

For every remaining row `j!=i`, projection away from the row span of `M_i`, namely `span(m,c_i)`, gives

`c'_j=c_j-(<c_j,c_i>/||c_i||^2)c_i`.                              (3.12)

Put

`Z1=sum_(j!=i)||c'_j||^2`.                                         (3.13)

The exterior identity is exact:

`sum_(j!=i)d_ij
 =||c_i||^2 Z1
 =alpha_i Z2`.                                                      (3.14)

Consequently

`boxed: S_i^2 Z1 = ||m||^2 alpha_i Z2.`                            (3.15)

Now normalize the one-volume marginals

`beta_j=||c'_j||^2/Z1`.                                             (3.16)

If every `beta_j<=1/2`, apply the reviewed `k=2, ell=1` grouped-crossing theorem. The two-dimensional hub `(Y,X_i)` consists of two independent original coordinates, so its joint density is bounded by one. The `ell=1` exponential entropy factor is absent. Hence

`||p_R||_infinity
 <=3*2^(5/6) S_i^(-1/3) Z1^(-1/6)
 =3*2^(5/6)(||m||^2 alpha_i Z2)^(-1/6)
 <6 (||m||^2 Z2)^(-1/6)`,                                          (3.17)

because `alpha_i>1/2`. This is already smaller than the constant in (3.5).

It remains only the subcase in which some `beta_j>1/2`. Promote that literal original coordinate `X_j` as well. Condition all remaining `I\{i,j}` original coordinates. Conditioning preserves independence between the three-coordinate hub `(Y,X_i,X_j)` and the untouched `J` bank, while all conditioned terms become arbitrary internal/affine terms, which the exact-crossing theorem allows.

The three-row hub-to-`J` matrix is

`M_ij=[m ; a_i ; a_j]`.                                             (3.18)

Its singular-value product is the three-row volume

`S_ij
 = ||m|| sqrt(d_ij)
 = ||m|| ||c_i|| ||c'_j||`.                                        (3.19)

Since `beta_j>1/2`,

`d_ij
 =||c_i||^2 ||c'_j||^2
 >(1/2)||c_i||^2 Z1
 =(1/2)alpha_i Z2
 >Z2/4`.                                                            (3.20)

Thus

`S_ij > (1/2)||m|| sqrt(Z2)`.                                      (3.21)

Apply the reviewed exact-rank-three crossing theorem. The hub side consists of exactly three original coordinates and therefore has projection-density cap one after a full three-dimensional orthogonal change of variables (Jacobian one; no independence claim is made after this change). The orthonormal three-dimensional projection of the product `J` bank has density cap `2^(3/2)`. Therefore

`||p_R||_infinity
 <=3 sqrt(2) S_ij^(-1/3)
 <3*2^(5/6)(||m||^2 Z2)^(-1/6)`,                                   (3.22)

again below (3.5). The characteristic-function envelope is integrable uniformly in the conditioned variables, so averaging preserves a continuous `C_0` density.

Cases A and B exhaust all possibilities. QED.

### What changed

The row-marginal gate in the preceding B01 theorem was not a fundamental analytic obstruction. Concentrated projected two-volume can be converted into one extra literal original hub; if the residual one-volume concentrates again, it produces a third literal hub and an exact rank-three crossing. This is the projected analogue of the physical-volume promotion cascade, but here the exterior identities (3.14) and (3.19) must be checked after projection away from the original hub row.

## 4. Designated partner result applied: stronger near-null leakage exit

Use the account04/B01 scalar-completion notation for a physical pair `S={x,y}`:

`B=[[a,b],[b,c]]`, `a!=0`,
`delta=c-b^2/a`,
`ell_k=A_yk-(b/a)A_xk`,
`M_kl=A_kl-a^(-1)A_xk A_xl`.                                       (4.1)

The partner proves

`W2(S)=a^2 sum_(k!=l)(delta M_kl-ell_k ell_l)^2`                    (4.2)

and in the leakage branch

`L(ell):=sum_(k!=l)ell_k^2 ell_l^2 >=W2(S)/(4a^2)`.                (4.3)

Its random two-coloring calculation gives

`E[||ell_I||^2 ||ell_J||^2]=L(ell)/4`.                             (4.4)

Therefore, for some literal original-coordinate split, the corrected source-valid conclusion is

`||ell_I|| ||ell_J|| >= sqrt(W2(S))/(4|a|)`.                       (4.5)

Orient the larger bank as `J`. Then

`||ell_J|| >= W2(S)^(1/4)/(2|a|^(1/2))`.                           (4.6)

Scalar completion of `x` writes the full form exactly as

`Q=a(X_x+h(Y,Z))^2+R(Y,Z)`,                                        (4.7)

where `Y=X_y`, the coordinates `Z` are the remaining original independent variables, and

`R(Y,Z)=F(Y)+2Y(ell dot Z+beta)+Z^T M Z+affine`.                    (4.8)

For the product-certified orientation from (4.5), define

`C=M[I,J](I-P_(ell_J))`,
`Z2=e_2(CC^T)`.                                                     (4.9)

### Corollary 4.1 — `QFORM-NEARNULL-LEAKAGE-E2-NOMARGINAL-v1`

If `Z2>0`, then **without any row-marginal gate** the residual `R` has a continuous `C_0` density and

`||p_R||_infinity
 <= C_E2 (||ell_J||^2 Z2)^(-1/6)`.                                (4.10)

Using the dependence-safe outer-square compiler (1.3), the full quadratic form has an essentially bounded density satisfying

`boxed:
||p_Q||_infinity
 <= 9.73330945413282
    |a|^(-5/12) W2(S)^(-1/24) Z2^(-1/12).`                         (4.11)

#### Proof

Equation (4.10) is Theorem 3.1 with `m=ell_J`. Applying (1.3) gives

`||p_Q||_infinity
 <=2sqrt(2 C_E2)|a|^(-1/2)(||ell_J||^2 Z2)^(-1/12)`.               (4.12)

From (4.6),

`||ell_J||^2 >= W2(S)^(1/2)/(4|a|)`.                               (4.13)

Substitution gives (4.11), because

`2sqrt(2 C_E2)*4^(1/12)=9.73330945413282...`.                       (4.14)

QED.

At the exact singular-pair endpoint, `L(ell)=W2/a^2`; the coloring product improves to `sqrt(W2)/(2|a|)`, hence the larger bank obeys

`||ell_J|| >= W2^(1/4)/(sqrt(2)|a|^(1/2))`,                        (4.15)

and (4.11) improves to

`||p_Q||_infinity
 <=9.18702077113785 |a|^(-5/12)W2^(-1/24)Z2^(-1/12)`.              (4.16)

The full exact-singular endpoint also has the different arbitrary-curvature random-slope receiver from the preceding B01 work, so (4.16) is mainly a consistency check rather than the best available exact-null theorem.

### Scope of the improvement

The preceding run left two projected-crossing failures: `Z2` tiny/zero and a two-volume row marginal above `1/2`. Theorem 3.1 removes the **entire heavy-row failure**. The only projected-crossing obstruction left in this branch is quantitative degeneracy of `Z2` itself. In particular, if `Z2>0`, no volume-concentration pattern can invalidate (4.10)-(4.11).

## 5. Averaged-in-frequency formulation

Apply the exact account04/B01 signed-Fejer equivalence (1.2). Theorem 3.1 gives

`boxed:
sup_(T>0,y) D_T law(R)(y)
 <= C_E2 (||m||^2 Z2)^(-1/6).`                                     (5.1)

The full near-null leakage corollary gives

`boxed:
sup_(T>0,y) D_T law(Q)(y)
 <=9.73330945413282
   |a|^(-5/12) W2(S)^(-1/24) Z2^(-1/12).`                          (5.2)

This is the requested averaged-frequency replacement. It does not require `hat mu` to belong to `L^1` in general and it does not restore the false pointwise Fresnel estimate.

## 6. Concrete heavy-row target instance

The heavy-row branch is not a formal edge case. Take eight independent cap-one coordinates

`x,y,u1,u2,u3,v0,v1,v2`

and

`Q=x^2+2 y v0+4 u1 v1+2 u2 v2-2 u3 v2`.                            (6.1)

For the residual after removing `x^2`, use one hub `Y=y`,

`I={u1,u2,u3}`, `J={v0,v1,v2}`, `m=(1,0,0)`,                       (6.2)

and projected crossing rows

`c1=(0,2,0)`, `c2=(0,0,1)`, `c3=(0,0,-1)`.                        (6.3)

Then

`Z2=8`,
`alpha_1=1`, `alpha_2=alpha_3=1/2`.                               (6.4)

So the old row-marginal gate fails maximally at row `u1`. Promote `u1`. The new hub-to-`J` singular product is `S=2`; the remaining one-volume is `Z1=2`, with both one-volume marginals exactly `1/2`. The `k=2, ell=1` stage therefore gives the sharper concrete bound

`||p_residual||_infinity
 <=3*2^(5/6)*(S^2 Z1)^(-1/6)
 =3.77976314968462...`.                                             (6.5)

Since `x^2` is independent, convolution cannot increase the density supremum, so the same bound holds for the full `Q`. The matrix spectrum is

`{-2,-sqrt(2),-1,0,1,1,sqrt(2),2}`,                                (6.6)

hence this is a genuine target-valid form with seven eigenvalues of modulus at least one. The residual is `C_0`; convolution with the independent square law preserves continuity.

## 7. Deterministic checks and homogeneity

The exterior identities were checked on 100 seeded random packets. The maximum floating-point discrepancy in

`sum_(j!=i)d_ij = ||c_i||^2 sum_(j!=i)||Proj_(c_i^perp)c_j||^2`

was `5.69e-14`. The maximum discrepancy in

`det([m;a_i;a_j][m;a_i;a_j]^T)=||m||^2 d_ij`

was `1.37e-12`. These are diagnostics only; the proof is the exact exterior algebra in Section 3.

The constants are

`C_E2=9.39913188784886...`,
`3*2^(5/6)=5.34539230884204...`,
`2sqrt(2 C_E2)=8.67139291595018...`,
`C_leak=9.73330945413282...`,
`C_exact=9.18702077113785...`.

Under `A -> lambda A`, `a`, `ell`, `M` scale by `lambda`, `W2` by `lambda^6`, and `Z2` by `lambda^4`; the right side of (4.11) scales by `|lambda|^(-1)` exactly.

## 8. Remaining implication

The row-marginal obstruction is closed. The first unpaid B01 implication in the near-null leakage route is now:

`QFORM-NEARNULL-PROJECTED-E2-DEGENERACY-v1`: handle the case in which every product-certified orientation has `Z2` quantitatively too small or exactly zero, while retaining arbitrary same-bank curvature and the nonzero near-null scalar Schur coefficient `delta`.

At `Z2=0`, every projected light-cross row lies in a one-dimensional subspace after removing `ell_J`; this is a genuine rank-two total-crossing endpoint. A further argument must use the remaining scalar curvature, a second original-product bank, or an already-paid hub/ridge/grouped-square receiver. The phase-aligned counterexample rules out repairing this by inserting a scalar pointwise quadratic-decay factor.

Full QFORM status: **OPEN**.  
Continuity: Theorem 3.1 proves a continuous `C_0` residual density. Corollary 4.1 proves only an essentially bounded full density because the outer completed-square translation may be correlated with the residual. Full-target continuity remains open.
