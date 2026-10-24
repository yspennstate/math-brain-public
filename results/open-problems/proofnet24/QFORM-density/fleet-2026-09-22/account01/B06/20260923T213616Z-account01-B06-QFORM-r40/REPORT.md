SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T21:36:16Z.
attacking: the rank-two hub-to-bank crossing half-Riesz receiver — integrate the exact crossing Fourier envelope against the one-half Riesz kernel, then reduce r39's mixed diagonal packet to a true crossing-area branch plus a quantified near-collinear residue.

# account01/B06 r40 — rank-two crossing half-Riesz receiver and mixed-packet reduction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T213616Z-account01-B06-QFORM-r40`  
Role: curved fiber integration / analytic derivation and exact structural identities  
Status: **PROVED SUPPORTING ANALYTIC THEOREM / DESIGNATED PARTNER APPLIED / MIXED-PACKET CROSSING-AREA SUBBRANCH CLOSED / NEAR-COLLINEAR RESIDUE QUANTIFIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. This report proves a dimension-free half-Riesz estimate for an exact rank-two crossing between two genuine original coordinates and an arbitrary original-coordinate product bank, then spends it through an outer genuine physical square. Applied to the diagonal shared-index normal form from r38-r39, it closes the quantitatively non-collinear part of the previously unpaid mixed currency. It introduces no Gaussianity, moment, compact-support, connected-support, log-concavity, iid, diagonal-basis or post-rotation-independence assumption. Continuity of the final density is not claimed.

## 1. Fresh source boundary

Fresh `math-research-brain` control at the prepublication refresh is commit

`58a0cc3c21033d8b1d445194421ff978111020db`,

with OWNER CONTROL revision `2026-09-22.15`, programme `QFORM-DENSITY-3EIG-20260922`, no paused account and no paused B06 slot. The current owner continuation remains `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.

The live state continues to mark the full QFORM claim OPEN and the global continuous-density conclusion OPEN. I retain the required corrections: no law-uniform pointwise quadratic-phase decay, no unrestricted fiber supremum, no independence after rotating independent coordinates, no arbitrary-joint coarea cap, no positive moment of worst conditional projection-density caps, and no assertion that aggregate spectral mass forces one uniformly good physical minor.

The freshest directly relevant correction consumed is

`QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1`,

account03/B06 run `20260923T205344Z-account03-B06-qform-r44`, canonical report commit

`eb5cd7bd244d799988b7fa618280b46713bd13c8`.

It shows that an indefinite two-hub core plus a robust slope does not absorb an arbitrary completed same-bank remainder: a rank-two example remains logarithmically singular. The theorem below does not use that false interface. It requires a genuine rank-two crossing area and then spends an independent original physical square as the third smoothing resource.

Own predecessor:

`yspennstate/math-open-problems@aac76ab560be5a95b892a9668b075b1924d147a7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T203409Z-account01-B06-QFORM-r39/REPORT.md`.

The new independently checked crossing theorem used below is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its exact-rank crossing statement allows arbitrary internal functions on each bank. For an exact rank-r cross matrix with singular values `s_1,...,s_r`, projection-density caps `M_X,M_Y`, and arbitrary measurable internal phases, it gives

`|phi(t)| <= min(1,(pi/|t|)^(r/2)(M_X M_Y)^(1/2)(s_1...s_r)^(-1/2)).`   (1.1)

For r=2 this is the borderline `1/|t|` estimate: it does not itself imply a bounded density, but it is exactly integrable after multiplication by the one-half Riesz Fourier weight.

The designated partner is account02/B06. I use two of its completed results at actual equations:

1. Latest `QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1`, canonical mathematics
   `yspennstate/math-open-problems@b38a9627f059b13d532f5c208c30579ec2d2d362`, gives for a literal disjoint physical cross block `M`

   `H_(1/2)(S):=sup_a E|S-a|^(-1/2) <= 8 e^(1/4) e_2(M^T M)^(-1/8)`.   (1.2)

   No volume-row-marginal gate remains, and arbitrary same-bank quadratic curvature and affine terms are allowed.

2. `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical mathematics
   `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, gives for any k-dimensional orthonormal projection of a product cap-one law

   `||p_projection||_infinity <= exp(k/2)`.                            (1.3)

   In particular a scalar unit projection has density at most `sqrt(e)`, and a two-dimensional orthonormal projection has density at most `e`.

## 2. A Fourier-to-half-Riesz lemma

Write

`H_(1/2)(Y)=sup_a E |Y-a|^(-1/2)`.

### Lemma 2.1 — borderline `1/t` decay is exactly enough

Let Y be any real random variable whose characteristic function satisfies

`|phi_Y(t)| <= min(1,K/|t|)`                                         (2.1)

for some K>0. Then

`boxed: H_(1/2)(Y) <= (8/sqrt(2pi)) sqrt(K).`                        (2.2)

### Proof

With Fourier convention `hat f(t)=int exp(itx)f(x)dx`, the one-dimensional Riesz kernel satisfies in tempered distributions

`widehat{|x|^(-1/2)}(t)=sqrt(2pi)|t|^(-1/2).`                       (2.3)

For rigor without presupposing a density for Y, multiply the right side by the Gaussian cutoff `exp(-eps t^2)`. Its inverse transform is the positive heat regularization `k_eps=|.|^(-1/2)*g_eps`. Hence for every a,

`E k_eps(Y-a)
 = 1/sqrt(2pi) int_R |t|^(-1/2) exp(-eps t^2)
      exp(-ita) phi_Y(t) dt`.                                       (2.4)

The absolute integral is bounded uniformly in eps by (2.1). As eps decreases to zero along any sequence, `k_eps(x)->|x|^(-1/2)` for x!=0 and tends to +infinity at x=0. Fatou therefore gives

`E|Y-a|^(-1/2)
 <= 1/sqrt(2pi) int_R |t|^(-1/2)|phi_Y(t)|dt`.                       (2.5)

Now

`int_R |t|^(-1/2) min(1,K/|t|) dt
 =2[ int_0^K t^(-1/2)dt + K int_K^infinity t^(-3/2)dt ]
 =8 sqrt(K).`                                                        (2.6)

Insert (2.6) into (2.5) and take the supremum over a. QED.

The point of this lemma is structural: rank-two crossing is logarithmically insufficient for L-infinity, but it is exactly sufficient for the half-Riesz potential that an additional physical square asks us to control.

## 3. Main analytic theorem: rank-two crossing half-Riesz smoothing

Let `H=(H_1,H_2)` consist of two **original independent** real coordinates, each with density at most one. Let `Z=(Z_j)` be a disjoint bank of original independent coordinates, also with one-dimensional densities at most one, independent of H. Let `B` be a real `2 x m` matrix of rank two, with singular values `sigma_1>=sigma_2>0`, and put

`Delta=sigma_1 sigma_2
      =sqrt(e_2(B^T B))`.                                           (3.1)

Let F and G be arbitrary measurable real functions for which the displayed random variable is defined, and set

`S=F(H)+2 H^T B Z+G(Z).`                                            (3.2)

No separability is assumed inside F or G.

### Theorem 3.1 — `QFORM-RANK2-CROSS-HALFRIESZ-v1`

Under (3.1)-(3.2),

`boxed:
 H_(1/2)(S)
 <=4 sqrt(2) e^(1/4) Delta^(-1/4).`                                (3.3)

The numerical front constant is

`4 sqrt(2) e^(1/4)=7.263544634846...`.                              (3.4)

### Proof

Take an SVD `B=U diag(sigma_1,sigma_2)V^T`. The left frame U is a `2 x 2` orthogonal matrix. Since H consists of two original independent cap-one scalars, `U^T H` has joint density

`p_(U^T H)(u)=f_1((Uu)_1)f_2((Uu)_2)<=1`.                           (3.5)

No independence of the rotated coordinates is asserted or needed; only the two-dimensional joint density cap is used.

On the right, V has two orthonormal columns in the original Z-bank. Apply the designated account02/B06 weighted affine-fiber theorem (1.3) with k=2:

`boxed: ||p_(V^T Z)||_infinity <= e.`                               (3.6)

This is the actual partner-result application in the proof.

Now apply the independently checked exact-rank crossing theorem (1.1) with r=2, `M_X=1`, `M_Y=e`. Arbitrary F and G are allowed there, so we obtain

`|phi_S(t)|
 <=min(1, pi sqrt(e) Delta^(-1/2) |t|^(-1)).`                       (3.7)

Thus Lemma 2.1 applies with

`K=pi sqrt(e) Delta^(-1/2)`.                                        (3.8)

Since `sqrt(K)=sqrt(pi)e^(1/4)Delta^(-1/4)`, (2.2) becomes

`H_(1/2)(S)
 <=[8/sqrt(2pi)]sqrt(pi)e^(1/4)Delta^(-1/4)
 =4sqrt(2)e^(1/4)Delta^(-1/4)`.                                    (3.9)

QED.

### Direct check against the newest partner theorem

The same S has a literal disjoint original-coordinate cross block B. Since B has rank two,

`e_2(B^T B)=sigma_1^2 sigma_2^2=Delta^2`.                           (3.10)

Therefore the latest account02/B06 row-gate-free theorem (1.2) applies directly and gives the independent source-compatible estimate

`H_(1/2)(S)<=8 e^(1/4) Delta^(-1/4).`                               (3.11)

The new argument sharpens the constant in (3.11) from 8 to `4sqrt(2)` by exploiting that the left bank has exactly two original coordinates and hence its rotated two-dimensional density cap is exactly one. More importantly, (3.11) verifies that no hidden row-marginal or exact-rank-of-the-remainder assumption is being smuggled into the intended application.

## 4. Spend the half-Riesz credit through one genuine physical square

Let `X_0` be another original coordinate, independent of `(H,Z)`, with density at most one. Let `c!=0`, and allow an arbitrary measurable shift `Psi(H,Z)`. Consider

`Q=c(X_0+Psi(H,Z))^2+S`,                                            (4.1)

with S as in Theorem 3.1.

### Corollary 4.1 — `QFORM-SQUARE-PLUS-RANK2-CROSS-v1`

The law of Q is absolutely continuous and

`boxed:
 ||p_Q||_infinity
 <=4sqrt(2)e^(1/4)|c|^(-1/2)Delta^(-1/4).`                          (4.2)

### Proof

Condition on `(H,Z)`. For any fixed shift psi, the law of `c(X_0+psi)^2` has a one-sided density bounded by

`|c|^(-1/2)|u|^(-1/2)`                                              (4.3)

on the appropriate half-line. Therefore the mixture density of Q satisfies for a.e. q

`p_Q(q)
 <=|c|^(-1/2) E|q-S|^(-1/2)
 <=|c|^(-1/2)H_(1/2)(S)`.                                          (4.4)

Apply (3.3). QED.

This is the desired three-resource structure: two crossing directions provide the borderline Fourier factor `|t|^-1`; the outer **original-coordinate** square provides exactly the additional half-Riesz smoothing needed for bounded density. No post-rotation independence is used.

## 5. Application to the r38-r39 diagonal shared-index normal form

Recall the exact usable-pivot normal form from r38-r39. A genuine original-coordinate pivot has coefficient

`c=A_ii !=0`.                                                        (5.1)

After completing its square, the two-hub Schur block is rank one. A deterministic O(2) change of hub basis, used only for coefficient algebra, writes the residual as

`S=-rho U^2 +2U(m.Z)+2V(n.Z)+R(Z)`,                                 (5.2)

where `(U,V)=O(H_1,H_2)` for two original independent hub coordinates, `m,n` are real coefficient vectors on the original product bank Z, and R contains every remaining background quadratic/affine term. The variables U,V are generally dependent; no independence between them is used.

In the original hub basis the literal physical cross block is

`B=O^T [m^T; n^T]`.                                                  (5.3)

Orthogonal left multiplication does not change singular values, so its rank-two area is

`Delta^2
 =e_2(B^T B)
 =||m||^2||n||^2-(m.n)^2
 =sum_(j<k)(m_j n_k-m_k n_j)^2.`                                    (5.4)

Thus whenever `Delta>0`, Corollary 4.1 applies to the **actual original-coordinate** decomposition (the hub rotation in (5.2) is not being used to manufacture product independence):

`boxed:
 ||p_Q||_infinity
 <=4sqrt(2)e^(1/4)|c|^(-1/2)Delta^(-1/4).`                          (5.5)

This is the curved/grouped receiver that r39's mixed currency was missing.

## 6. Close the quantitatively transverse part of the mixed packet

Use r38 notation

`D0=sum_j delta_j^2`,
`D_i^diag=c^2 D0`,
`B_mix=sum_j m_j^2 n_j^2`,
`N4=sum_j n_j^4`,
`M4=sum_j m_j^4`.                                                    (6.1)

One of the r38 exact packet alternatives is

`B_mix >= D0/2`.                                                     (6.2)

Fix any `0<eta<=1`. On the quantitatively transverse subbranch

`Delta^2 >= eta B_mix`,                                              (6.3)

(6.2) gives

`Delta^2 >= eta D_i^diag/(2c^2)`.                                   (6.4)

Insert (6.4) into (5.5):

`boxed:
 ||p_Q||_infinity
 <=2^(21/8)e^(1/4) eta^(-1/8)
   |c|^(-1/4)(D_i^diag)^(-1/8).`                                    (6.5)

The front constant before `eta^(-1/8)` is

`2^(21/8)e^(1/4)=7.920951590859...`.                                (6.6)

### Concrete target-scale corollary

Let `s=s_3(A)>0`. In the live r30-r39 target-scale diagonal-packet chamber, suppose

`|c|>=s/16`,
`D_i^diag>=81 s^6/2^24`,
`B_mix>=D0/2`,
`Delta^2>=B_mix/16`.                                                 (6.7)

Then (6.5) with `eta=1/16` yields

`boxed: ||p_Q||_infinity <103.479/s.`                               (6.8)

Under the normalized conjecture `s>=1`, this is a universal `103.479` bound on that whole subbranch.

The scale is correct: c contributes one quadratic scale, `D_i^diag` is a squared third-minor packet with scale six, and (6.5) is homogeneous of degree `-1` in A.

## 7. Quantify the remaining mixed survivor: it is near-collinear

The point of (6.5) is not merely another branch constant; it gives a clean geometric meaning to failure. If (6.2) holds but the area exit with `eta=1/16` fails, then

`Delta^2 < B_mix/16
 <= ||m||^2||n||^2/16`.                                              (7.1)

Therefore the angle theta between m and n satisfies

`sin^2(theta)=Delta^2/(||m||^2||n||^2)<1/16`,
`boxed: sin(theta)<1/4.`                                             (7.2)

Equivalently, writing

`n=lambda m+r`, `r perpendicular m`,                                (7.3)

we have

`boxed: ||r||<||n||/4.`                                             (7.4)

So the unpaid part of the mixed currency is no longer a generic two-star configuration: its two hub-to-bank coefficient vectors are quantitatively nearly collinear.

## 8. If the transverse-fourth-power exit also fails, the longitudinal bank is large

R39's transverse-star theorem actually gives the more general implication

`N4>=theta D0
 => ||p_Q||_infinity
    <=2^(17/4)e^(1/4)theta^(-1/8)
       |c|^(-1/4)(D_i^diag)^(-1/8).`                                (8.1)

For the convenient threshold `theta=1/16`, this is

`||p_Q||_infinity
 <=2^(19/4)e^(1/4)|c|^(-1/4)(D_i^diag)^(-1/8).`                     (8.2)

Under the target-scale assumptions on c and `D_i^diag` in (6.7), (8.2) is

`||p_Q||_infinity<319.173/s`.                                       (8.3)

Hence the surviving mixed branch may additionally be assumed to satisfy

`N4<D0/16`.                                                         (8.4)

Now Cauchy-Schwarz gives

`B_mix^2
 =(sum_j m_j^2 n_j^2)^2
 <=(sum_j m_j^4)(sum_j n_j^4)
 =M4 N4`.                                                           (8.5)

Combining (6.2), (8.4), and (8.5),

`M4 > (D0/2)^2/(D0/16)=4D0.`                                       (8.6)

Thus

`boxed: sum_j m_j^4>4D0.`                                          (8.7)

In particular `||m||^4>=M4>4D0`, so

`||m||>sqrt(2) D0^(1/4)`.                                           (8.8)

Apply the designated account02/B06 scalar projection consequence of (1.3) to the genuine original bank Z:

`||p_((m/||m||).Z)||_infinity<=sqrt(e)`.                            (8.9)

Therefore the longitudinal projection obeys the actual inequality

`boxed:
 ||p_(m.Z)||_infinity
 < sqrt(e)/(sqrt(2)D0^(1/4))
 = [sqrt(e)/sqrt(2)] |c|^(1/2)(D_i^diag)^(-1/4).`                   (8.10)

This does not by itself finish the near-collinear survivor, but it shows that the large mixed packet leaves a quantitatively spread longitudinal product projection after both existing exits fail.

## 9. Add the longitudinal-square currency: a sign-coherent diagonal bank emerges

The remaining r38 currency is

`L=sum_j (rho d_j+m_j^2)^2`.                                        (9.1)

Suppose, in addition to the survivor assumptions above, that

`L<D0/2`.                                                           (9.2)

Set `A_j=rho d_j+m_j^2`, and define

`G={j: |A_j|<=m_j^2/2}`.                                            (9.3)

On the complement `G^c`,

`m_j^4<4A_j^2`,

so by (9.2)

`sum_(j in G^c)m_j^4<4L<2D0`.                                      (9.4)

Using (8.7),

`boxed: sum_(j in G)m_j^4>2D0.`                                    (9.5)

The case `rho=0` is impossible under (8.7),(9.2), because then `L=M4>4D0`. Thus `rho!=0`. For every j in G,

`|rho d_j+m_j^2|<=m_j^2/2`,                                        (9.6)

which forces `rho d_j` to have sign opposite to `rho` and magnitude at least `m_j^2/2`. Therefore all `d_j`, j in G, have one common sign and

`d_j^2>=m_j^4/(4rho^2)`.                                            (9.7)

Summing (9.7) and using (9.5),

`boxed:
 sum_(j in G)d_j^2>D0/(2rho^2).`                                    (9.8)

This is an exact deterministic structural consequence. It does **not** yet give a density bound, because arbitrary off-diagonal curvature within the background bank remains and one may not simply convolve the diagonal squares as if that bank were separable. What it does accomplish is to identify the last same-branch residue precisely:

> after the crossing-area receiver, the transverse-star receiver, and a small-longitudinal-currency assumption all fail to pay, the matrix has a near-collinear rank-one hub crossing, a low-density longitudinal product projection, and a quantitatively large **same-sign physical diagonal square bank**.

That is a substantially narrower product-preserving target than the original mixed packet.

## 10. What is closed and what remains

The new theorem closes the r39 mixed packet whenever its two hub-to-bank coefficient vectors have crossing area

`Delta^2 >= (1/16) sum_j m_j^2 n_j^2`.                               (10.1)

The r39 transverse-star theorem closes the complementary mixed branch whenever

`sum_j n_j^4 >= D0/16`.                                             (10.2)

If both fail, then the vectors are quantitatively near-collinear, `sum m_j^4>4D0`, and the longitudinal product projection has the density cap (8.10). If also the longitudinal-square currency is below `D0/2`, a same-sign background diagonal bank satisfying (9.8) is forced.

The first unpaid local implication is now

`QFORM-NEARCOLLINEAR-HUB-PLUS-SAMESIGN-DIAGONAL-BANK-v1`:

> In the usable-pivot diagonal shared-index branch, retain the near-collinear hub interaction and the sign-coherent physical diagonal bank jointly, with arbitrary same-bank off-diagonal curvature, and obtain the target-scale L-infinity bound; otherwise show that the large longitudinal-square currency itself enters an existing grouped/ridge/projected-crossing receiver. The separate small-pivot complement remains outside this argument.

The new account03/B06 correction is exactly why the words “jointly” and “genuine third curvature” matter here: a near-collinear/near-null hub slope cannot simply be declared smoothing against an arbitrary remainder.

## 11. Quantifier and regularity ledger

- Every probabilistic use of independence is between actual original-coordinate banks.
- The O(2) hub change in (5.2) is used only to express coefficient geometry; the crossing theorem is applied to the corresponding literal original-coordinate block (5.3).
- F and G in Theorem 3.1 are arbitrary measurable internal functions; therefore arbitrary same-bank quadratic curvature and affine terms in the intended application are retained.
- No moments, compact support, connected support, centering, identical distribution, log-concavity or Gaussianity are used.
- The full arbitrary-dimensional target remains **OPEN**.
- No target counterexample is produced.
- Corollary 4.1 proves **essential boundedness** in its stated branch. I do not claim a continuous representative there; global continuity remains **OPEN**.
- The new r40 theorem has not yet received an independent end-to-end review.

## 12. Numeric constants

The exact constants used above are

`4 sqrt(2)e^(1/4) = 7.263544634846...`,
`2^(21/8)e^(1/4) = 7.920951590859...`,

and with `|c|>=s/16`, `D_i^diag>=81s^6/2^24`, the common scaling multiplier is

`16^(1/4)(2^24/81)^(1/8)=9.237604307034...`.

Thus the `eta=1/16` crossing-area branch gives

`7.920951590859 * 9.237604307034 * 16^(1/8)
 =103.478878266...`,

while the `N4>=D0/16` transverse-star branch gives

`2^(19/4)e^(1/4)*9.237604307034
 =319.172492526...`.

These computations only verify arithmetic; the proof is analytic and structural.
