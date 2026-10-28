SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-24T10:19:32Z.
attacking: the near-zero overlap-one survivor by removing the projected-E2 row-marginal gate through literal physical-row promotion, with no division by the small scalar pivot.

# account03/B04 r55 — marginal-free one-hub projected-E2 density receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM / NEAR-ZERO-PIVOT ANALYTIC ENDPOINT ENLARGED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity: every branch of the new theorem has an integrable characteristic-function majorant, hence a continuous density vanishing at infinity (`C_0`). The unrestricted continuity conclusion remains open because the theorem still has a structural currency hypothesis.

The owner target remains the unrestricted one: independent ORIGINAL real coordinates, each with density bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No Gaussianity, moments, support assumptions, log-concavity, connected support, iid hypothesis, diagonal-basis independence, pointwise scalar quadratic-phase decay, arbitrary-joint coarea, or worst-fiber supremum is used.


## 1. Source-valid inputs and the first missing implication

The analytic input is the grouped-projection / projected-crossing theorem read on fresh `math-open-problems` master at commit

`yspennstate/math-open-problems@35bc266eff789abbc87566751c074d636337489d`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For `k` original hub directions and projected crossing order `ell`, with `d=k+ell>2`, it gives

`||p_Q||_infinity
 <= d/(d-2) * 2^((k+3 ell)/(2d)) * exp(ell/(2d))
    * M_H^(1/d) * S^(-1/d) * Z_ell^(-1/(2d))`,                 (1.1)

provided every `ell`-volume row marginal is at most `1/2`. For `ell=1` the exponential factor is omitted. Here `S` is the product of singular values of the hub-to-light crossing, `Z_ell` is the projected `ell`-volume, and all same-bank quadratic terms and affine terms are retained. For an actual set of original hub coordinates, `M_H<=1`.

The same source gives the exact-rank crossing estimate: three ORIGINAL hub variables whose full crossing matrix has third-volume `Pi_3` give

`||p_Q||_infinity <= 3 sqrt(2) Pi_3^(-1/3)`,                    (1.2)

with a continuous `C_0` density. Both (1.1) and (1.2) are product-coordinate Fourier estimates; neither assumes independence after spectral rotation.

The preceding B04 run r54 reduced the overlap-one branch to

`J_1(h)>=1/144,  |A_hh|<2^(-16)`,                               (1.3)

including the exact-zero face, because its scalar-square completion still cost `|A_hh|^(-1/4)`. The immediate analytic debt was therefore to spend an inverse-free projected two-volume packet without dividing by `A_hh`.

## 2. New theorem — `QFORM-ONEHUB-PROJECTED-E2-MARGINALFREE-v1`

Fix one ORIGINAL coordinate `h` and disjoint ORIGINAL coordinate banks `I,J` not containing `h`. Put

`m=A[h,J]`,
`s=||m||_2`,
`B=A[I,J]`,
`C=B(I-P_m)`,                                                     (2.1)

where `P_m` is orthogonal projection in the physical `J`-coordinate coefficient space onto `span{m}`. Define

`Z=e_2(CC^T)
 =sum_(i<k, i,k in I) ||c_i wedge c_k||_2^2`,                    (2.2)

where `c_i` is row `i` of `C`.

### Theorem 2.1

If

`s>0,  Z>0`,                                                       (2.3)

then for every admissible independent cap-one product input and for the **full ambient quadratic form**, including arbitrary coefficients on every other entry of `A`, the law of `Q=X^T A X` has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_PF (s^2 Z)^(-1/6),
 C_PF=3*2^(7/6)*e^(1/3)
     =9.39913188784886... .`                                     (2.4)

There is **no row-marginal hypothesis** in (2.4), and there is **no dependence on the scalar pivot `A_hh`**. In particular, (2.4) applies unchanged at `A_hh=0` and uniformly as `A_hh ->0`.

### Proof

For each physical row `i in I` define its incident projected second-volume

`K_i=sum_(k!=i) ||c_i wedge c_k||^2`.                             (2.5)

The natural E2 row marginal is `alpha_i=K_i/Z`, and

`sum_i alpha_i=2`.                                                 (2.6)

There are two main cases.

#### Case A: all E2 marginals are at most one half

If every `alpha_i<=1/2`, apply the completed grouped theorem (1.1) with

`k=1, ell=2, d=3, M_H=1, S=s, Z_2=Z`.                            (2.7)

This gives directly

`||p_Q||_infinity
 <=3*2^(7/6)*e^(1/3) s^(-1/3) Z^(-1/6)
 =C_PF (s^2 Z)^(-1/6).`                                          (2.8)

This branch already has an `L^1` characteristic-function envelope.

#### Case B: one E2 row is heavy

Otherwise choose a literal physical row `i in I` with

`K_i>Z/2`.                                                        (2.9)

Promote the ORIGINAL coordinate `X_i` to a second hub. Write `b_i` for row `i` of `B` and let

`M_2=[m; b_i]`.                                                    (2.10)

Since `K_i>0`, `c_i!=0`, and Gram--Schmidt gives

`S_2^2:=det(M_2 M_2^T)=s^2 ||c_i||^2`.                           (2.11)

For each remaining row `k`, project `b_k` off the two-dimensional physical row span of `M_2`, and denote the residual row by `d_k`. Put

`Z_1=sum_(k!=i)||d_k||^2`.                                        (2.12)

Because `c_i,c_k` both lie in `m^perp`, another one-line Gram--Schmidt identity gives

`||c_i wedge c_k||^2
 =||c_i||^2 dist(c_k,span{c_i})^2
 =||c_i||^2 ||d_k||^2`.                                          (2.13)

Summing (2.13),

`boxed: K_i=||c_i||^2 Z_1,}`                                     (2.14)

and hence

`boxed: S_2^2 Z_1=s^2 K_i.}`                                     (2.15)

Now inspect the one-volume law on the rows `d_k`.

**B1. Diffuse residual one-volume.** If every row has `||d_k||^2/Z_1<=1/2`, apply (1.1) with `k=2,ell=1,d=3`. Because the two hubs are literal independent original coordinates, `M_H<=1`; because `ell=1`, there is no exponential loss. Thus

`||p_Q||_infinity
 <=3*2^(5/6) S_2^(-1/3) Z_1^(-1/6)
 =3*2^(5/6)(s^2K_i)^(-1/6)`                                     (2.16)

by (2.15). From (2.9),

`||p_Q||_infinity
 <3*2^(5/6)*2^(1/6)(s^2Z)^(-1/6)
 =6(s^2Z)^(-1/6).`                                               (2.17)

**B2. Heavy residual one-volume.** If instead some literal physical row `k` has

`||d_k||^2>Z_1/2`,                                                (2.18)

promote that ORIGINAL coordinate too. The three-row physical hub-to-`J` block

`M_3=[m;b_i;b_k]`                                                 (2.19)

has

`S_3^2:=det(M_3M_3^T)
 =s^2||c_i||^2||d_k||^2
 >(1/2)s^2K_i
 >(1/4)s^2Z.`                                                     (2.20)

The full crossing from these three physical hubs to their entire complement has third-volume at least `S_3`, since adding complement columns only increases the hub Gram matrix. Apply the exact three-hub theorem (1.2):

`||p_Q||_infinity
 <=3sqrt(2) S_3^(-1/3)
 <3*2^(5/6)(s^2Z)^(-1/6).`                                      (2.21)

The constants in (2.17) and (2.21) are both strictly below

`C_PF=9.3991318878...`.                                          (2.22)

This exhausts the heavy-row branch and proves (2.4). Every promotion is of a **literal original coordinate**. No random-variable rotation is made; the projections occur only in coefficient space. All terms internal to the promoted hubs, all terms internal to the remaining coordinates, all outside couplings, all diagonals and all affine terms are precisely the arbitrary `F`/`R` terms already permitted by the cited grouped and exact-crossing theorems. QED.

## 3. Why this is a real strengthening of the Fourier endpoint

The original grouped `k=1,ell=2` theorem had the gate

`max_i alpha_i<=1/2`.                                             (3.1)

Theorem 2.1 removes (3.1) completely. A failed E2 marginal gate does not create a new obstruction: it manufactures a second literal hub; if that new one-volume law is itself concentrated, it manufactures a third literal hub and reaches an exact rank-three crossing.

This is also the correct behavior at a zero or nearly zero scalar diagonal. The proof never completes the square in `X_h`, so `A_hh` is absorbed into the arbitrary internal hub phase. Thus the `|A_hh|^-1/4` divergence of r54 is not intrinsic whenever the inverse-free currency

`s^2 e_2(B(I-P_m)(I-P_m)^T)`                                     (3.2)

is available at target scale.

A direct consequence for the live overlap-one chamber is:

> if (1.3) holds and one can find a physical split `I,J` for which `s^2Z>=tau>0`, then
> `||p_Q||_infinity <=9.400 tau^(-1/6)` continuously, uniformly through `A_hh=0`.

The remaining structural issue is now sharper: prove that the overlap-one packet forces target-scale (3.2) on some physical split, **or** route its failure into the already-developed two-star/ridge/square-bank/low-rank mixed-hub endpoints. The scalar near-zero pivot itself is no longer an analytic obstruction on this branch.

## 4. Genuinely rotated indefinite stress test where the old row gate fails

The theorem is not merely the diffuse special case. Let the left physical bank have four coordinates `{h,i_1,i_2,i_3}` and the right bank have three coordinates `J`. Define the unscaled cross matrix

`M_0 = [[1, 1, 1],
        [6,-2, 2],
        [4, 4, 1],
        [5, 3, 1]]`,                                              (4.1)

and use the actual cross block `2M_0`. Let the left same-bank block have every entry `1/100` except

`A_hh=2^(-20)<2^(-16)`,                                          (4.2)

and let the right same-bank block have every entry `-1/100`. The resulting symmetric `7x7` matrix `A_*` is fully dense: every physical coefficient is nonzero.

For the hub `h`,

`m=(2,2,2),   s^2=12`,                                            (4.3)

and with `I={i_1,i_2,i_3}` the three rows of `B=A[I,J]` are

`(12,-4,4), (8,8,2), (10,6,2)`.                                  (4.4)

Projection off `m` gives exactly

`c_1=(8,-8,0),
 c_2=(2,2,-4),
 c_3=(4,0,-4)`.                                                   (4.5)

Their squared two-areas are

`||c_1 wedge c_2||^2=3072`,
`||c_1 wedge c_3||^2=3072`,
`||c_2 wedge c_3||^2=192`.                                       (4.6)

Hence

`Z=6336`,                                                         (4.7)

and the E2 row marginals are

`alpha=(32/33,17/33,17/33)`.                                     (4.8)

So the **old projected-crossing gate fails maximally** on row one. The new theorem nevertheless gives

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=9.39913188784886 * 76032^(-1/6)
 =1.4440703172492453... .`                                       (4.9)

In fact this example enters branch B1. Here

`K_1=6144`, `||c_1||^2=128`, `Z_1=48`,                            (4.10)

and the two remaining one-volume marginals are exactly `1/2,1/2`. Therefore the actual promoted-hub estimate sharpens (4.9) to

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=3*2^(5/6)*(12*6144)^(-1/6)
 =0.8254818122236568... .`                                       (4.11)

Both (4.9) and (4.11) give continuous `C_0` densities for every admissible independent cap-one product law.

### Rigorous spectral target check

For (4.1),

`M_0^T M_0 = [[78,20,22],[20,30,4],[22,4,7]].`                   (4.12)

The leading principal minors of

`M_0^T M_0-(5/8)I`                                                (4.13)

are exactly

`619/8, 119865/64, 2139/512`,                                    (4.14)

all positive. Sylvester therefore gives

`sigma_3(2M_0)>sqrt(5/2).`                                       (4.15)

The same-bank perturbation from the pure-cross matrix has operator norm below `1/25`: the left-block Frobenius square is

`15/10000+2^(-40)<1/625`,                                        (4.16)

and the right-block Frobenius norm is `3/100`. Weyl's inequality therefore leaves three positive and three negative eigenvalues of `A_*` with modulus at least

`sqrt(5/2)-1/25
 =1.5411388300841897...>1`.                                      (4.17)

Thus the example is genuinely rotated, fully dense, indefinite, strongly inside the owner spectral target, has a near-zero physical pivot, and genuinely violates the row-marginal hypothesis removed in this run.

`CHECKS.py`, `CHECKS.json` and `CHECKS_OUTPUT.txt` verify (4.3)--(4.17) with exact rational arithmetic where applicable. Marker:

`QFORM_B04_R55_MARGINALFREE_PROJECTED_E2_CHECK_PASS`.

No Monte Carlo evidence is used.

## 5. Designated partner account04/B04 applied at an actual inequality

The newest completed designated partner remains account04/B04 r2:

`yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B04/20260924T001353Z-account04-B04-QFORM-r2/REPORT.md`.

On its high-fourth-volume carrier branch, failure of its anchored entropy gate gives a literal physical pair `a,b` with canonical pair mass

`eta_ab>2/75`.                                                     (5.1)

For the pair-anchored fourth-volume mass `H_ab=eta_ab E_4(M)`, this is the actual inequality

`H_ab>(2/75)E_4(M)`.                                              (5.2)

Apply the completed B04 pair-anchored promotion theorem from r48,

`||p_Q||_infinity <=2^(17/8) H_ab^(-1/8)`.                       (5.3)

Combining (5.2)--(5.3) gives

`boxed:
 ||p_Q||_infinity
 <4*75^(1/8) E_4(M)^(-1/8)
 =6.861872579851902... E_4(M)^(-1/8).`                            (5.4)

That partner branch has a continuous `C_0` density. This is an actual quantitative use of the designated partner result, not a source-only citation.

## 6. Scope, status, and next exact debt

**What is proved in this run.** A single physical hub plus positive projected second-volume always gives a direct continuous density bound with no row-marginal hypothesis and no scalar-pivot denominator. The proof is exhaustive: diffuse E2 uses the existing grouped Fourier theorem; E2 concentration promotes one literal physical row; remaining E1 concentration promotes one more literal row and lands in an exact three-hub crossing.

**What is not proved.** The bare three-large-eigenvalue hypothesis has not yet been shown to force a universal lower bound on `s^2Z` for a suitable physical split. Therefore this is a supporting theorem, not a proof of the full conjecture. Independent end-to-end review of this new theorem is not claimed in this run.

The next B04 implication is

`QFORM-OVERLAP1-TO-PROJECTED-E2-OR-BISTAR-v1`:

inside the surviving global one-anchor packet `J_1(h)>=1/144` with `|A_hh|<2^-16`, aggregate before inversion and prove that either some physical split has target-scale

`||A[h,J]||^2 e_2(A[I,J](I-P_{A[h,J]})(...)^T)`,                 (6.1)

which is now completely paid by Theorem 2.1 even at exact zero pivot, or the failure of (6.1) quantitatively forces the inverse-free two-star / rank-one projected-cross / ridge / square-bank configurations already represented elsewhere in the proof graph. Arbitrary same-bank curvature and extra spectrum must be retained.

Full QFORM: **OPEN**. Full-target continuity: **OPEN** separately. Repository use occurred; authenticated native brain ingestion/receiver use did not, so status remains `WITHOUT_VERIFIED_BRAIN`.
