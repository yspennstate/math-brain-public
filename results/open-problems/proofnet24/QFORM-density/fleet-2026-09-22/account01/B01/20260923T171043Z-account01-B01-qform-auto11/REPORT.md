SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T17:10:43Z.
attacking: the critical two-physical-hub packet when the third smoothing coordinate is NOT an independent residual term but is entangled with the same leaf bank through an arbitrary linear coefficient; replace the failed factorization by an L4-in-frequency scalar square-phase budget coupled to two-dimensional hub Plancherel.

# Two hubs plus an entangled scalar square: an L4/L1 compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T171043Z-account01-B01-qform-auto11`  
Role: account01/B01, Oscillatory replacement  
Status: **PROVED SUPPORTING TARGET-LEVEL ANALYTIC THEOREM / FULL QFORM OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact correction boundary and source inputs

The unrestricted conjecture remains OPEN. We keep every original quantifier: independent real input coordinates with probability densities bounded by one; arbitrary symmetric matrix; at least three eigenvalues of modulus at least one; no moment, support, log-concavity, connected-support, Gaussian, or post-rotation independence assumption.

The phase-aligned fragmented-support counterexample remains fully in force. This report does **not** assert a law-uniform pointwise scalar estimate

`|E exp(it X^2)| <= C |t|^(-1/2)`.

The replacement below is genuinely averaged in frequency: one ORIGINAL scalar coordinate gives an `L^4(dt)` square-phase budget, while two ORIGINAL physical hubs give a critical `|t|^-1` Plancherel factor. The coefficient of the scalar linear phase is allowed to depend arbitrarily on the same leaf bank that creates the hub slopes, so the scalar residual is not independent as a random term.

Fresh control before publication: `math-research-brain` main, OWNER CONTROL revision `2026-09-22.15`, QFORM-only; current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`; full theorem still explicitly open. Current correction inbox was reread. No false arbitrary-joint coarea cap, conditional projection-density cap, post-rotation independence, or uniform scalar Fresnel decay is used.

Source inputs used at equations:

1. Designated partner account02/B01 scalar square-phase theorem: `yspennstate/math-open-problems@91dbcb0e8b3f6faa4af9629aaaff2f69d385695a`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T100534Z-account02-B01-qform/REPORT.md`. For a cap-one scalar density, `c!=0`, and arbitrary affine coefficient `ell`, it proves

   `int_R | E exp(it(c Z^2+ell Z)) |^4 dt <= 27 pi/(2|c|).`       (1.1)

   The estimate is uniform in `ell`; this uniformity is the essential partner input below.

2. Current projected-crossing theorem: `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. In particular it records the dimension-two product-projection cap used below: if `B` is a rank-two linear map from an independent cap-one product bank, then

   `||p_(BY)||_infinity <= 2 / sqrt(det(BB^T)).`                   (1.2)

   I also check its new weighted-subset row-marginal gate on the stress family in Section 6; that gate fails there because the projected crossing is concentrated on one physical row.

3. Latest completed designated-partner handoff before publication: account02/B01 r46, canonical mathematics `yspennstate/math-open-problems@a9cb334579e92753035a96d258fa94cac01cdbfc`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T160109Z-account02-B01-qform-r46/REPORT.md`. I apply its pair-Schur theorem at an actual equation in Section 7.

## 2. Main theorem

Let

- `H=(H1,H2)` be two ORIGINAL independent coordinates, each with density at most one;
- `Y` be a disjoint bank of ORIGINAL independent coordinates, all densities at most one;
- `Z` be one further disjoint ORIGINAL coordinate with density at most one.

All three groups are mutually independent. Let `B` be a real `2 x m` matrix of rank two and put

`D = det(BB^T) > 0.`                                                (2.1)

Let `c!=0`. Let `F:R^2->R`, `R:R^m->R`, and `q:R^m->R` be arbitrary measurable real functions, and let `d in R^2`. Consider

`Q = F(H) + 2 H^T(BY+d) + R(Y) + c Z^2 + q(Y) Z.`                 (2.2)

For an ambient quadratic form, after conditioning any remaining ORIGINAL coordinates, `F` is a quadratic-plus-linear hub polynomial, `R` is an arbitrary leaf quadratic-plus-linear polynomial, and `q` is affine in `Y`; the theorem deliberately allows more than that.

### Theorem 2.1 — `QFORM-TWOHUB-ENTANGLED-SCALAR-L4-v1`

Under (2.1)-(2.2), the law of `Q` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= C_* [ D |c| ]^(-1/5),
 C_* = (15/4) 12^(1/5)
     = 6.164069360689596... .`                                    (2.3)

The statement is uniform in `F,R,q,d` and in every admissible product input law.

The key point is that the third smoothing term

`c Z^2 + q(Y) Z`                                                    (2.4)

is generally **not independent** of the two-hub leaf slope `BY`: both depend on `Y`. Thus (2.3) is not a convolution or independent-residual theorem.

The theorem scales correctly. Under multiplication of the entire quadratic form by `s`, `D` scales as `s^4`, `|c|` as `|s|`, hence `(D|c|)^(-1/5)` scales as `|s|^-1`, exactly the density scale.

## 3. Frequency-averaged scalar budget with an entangled coefficient

For `t in R` and a fixed leaf value `y`, define

`G_t(y) = E_Z exp( it [ c Z^2 + q(y) Z ] ).`                       (3.1)

For each fixed `y`, the partner theorem (1.1), with affine coefficient `ell=q(y)`, gives

`int_R |G_t(y)|^4 dt <= 27 pi/(2|c|).`                             (3.2)

Define

`A(t) = ( E_Y |G_t(Y)|^2 )^(1/2).`                                (3.3)

By Jensen in the probability variable `Y`,

`A(t)^4 = (E_Y |G_t(Y)|^2)^2 <= E_Y |G_t(Y)|^4.`                  (3.4)

Tonelli and (3.2) therefore give the uniform averaged-frequency bound

`boxed:
 ||A||_4 <= [27 pi/(2|c|)]^(1/4).`                                (3.5)

This is the first essential step. It is valid even when `q(Y)` is wildly dependent on `BY`; no pointwise-in-`t` scalar decay is asserted.

## 4. Complex pushforward through the hub slope

Set

`L = BY+d in R^2`                                                   (4.1)

and let `p_L` be its density. Put

`M = ||p_L||_infinity.`                                            (4.2)

For each `t`, push the complex measure

`exp(it R(Y)) G_t(Y) dP_Y`                                        (4.3)

through the map `Y -> L`. It has a complex Lebesgue density `a_t(l)`. In disintegration notation,

`a_t(l) = p_L(l) E[ exp(itR(Y)) G_t(Y) | L=l ].`                  (4.4)

Conditional Cauchy-Schwarz gives

`|a_t(l)|^2
 <= p_L(l)^2 E[ |G_t(Y)|^2 | L=l ].`                              (4.5)

Using `p_L^2 <= M p_L` and integrating in `l`,

`||a_t||_2^2
 <= M E_Y |G_t(Y)|^2
 = M A(t)^2.`                                                       (4.6)

Hence

`boxed: ||a_t||_2 <= M^(1/2) A(t).`                                (4.7)

This is the dependence-safe replacement for the factorization used when the third residual is source-disjoint as a *random term*. The leaf curvature `R(Y)` disappears only through its unimodular phase, not by being discarded.

## 5. Two-dimensional original-hub Plancherel and L1 frequency closure

With Fourier convention

`hat a(xi)=int_R2 exp(i xi.l) a(l) dl`,                             (5.1)

the characteristic function of `Q` can be written

`phi_Q(t)
 = int_R2 f_H(h) exp(itF(h)) hat a_t(2t h) dh,`                    (5.2)

where `f_H(h)=f_1(h_1)f_2(h_2)`. Since each scalar density is at most one,

`0<=f_H<=1`, `int f_H=1`.                                          (5.3)

Cauchy-Schwarz against the probability measure `f_H(h)dh`, followed by `f_H<=1`, yields

`|phi_Q(t)|
 <= [ int_R2 |hat a_t(2t h)|^2 dh ]^(1/2).`                        (5.4)

For `t!=0`, change variables `xi=2t h` and use two-dimensional Plancherel,

`int |hat a_t(2t h)|^2 dh
 = (4t^2)^(-1) int |hat a_t(xi)|^2 dxi
 = pi^2 |t|^-2 ||a_t||_2^2.`                                      (5.5)

Combining (4.7),

`boxed:
 |phi_Q(t)|
 <= min{ 1, pi M^(1/2) |t|^-1 A(t) }.`                            (5.6)

This is a critical `|t|^-1` two-hub envelope multiplied by an `L^4(dt)` amplitude. The scalar phase itself need not decay pointwise at all.

For any `T>0`, Hölder with exponents `4` and `4/3` gives

`int_R |phi_Q(t)| dt
 <= 2T + pi M^(1/2)
      [int_(|t|>T) |t|^(-4/3) dt]^(3/4) ||A||_4`                  (5.7)

and

`[int_(|t|>T)|t|^(-4/3)dt]^(3/4)
 = 6^(3/4) T^(-1/4).`                                              (5.8)

Using (3.5),

`int |phi_Q|
 <= 2T + D_0 T^(-1/4),`                                           (5.9)

where

`D_0
 = pi M^(1/2) 6^(3/4) [27pi/(2|c|)]^(1/4)
 = 3 sqrt(6) pi^(5/4) M^(1/2) |c|^(-1/4).`                        (5.10)

The optimum occurs at

`T=(D_0/8)^(4/5),`                                                  (5.11)

and the minimum is

`10 (D_0/8)^(4/5).`                                                 (5.12)

Therefore Fourier inversion gives first the useful projection-density form

`boxed:
 ||p_Q||_infinity
 <= 5 (3 sqrt(6)/8)^(4/5)
       M^(2/5) |c|^(-1/5)
 = 4.67149102355819...
       M^(2/5)|c|^(-1/5).`                                        (5.13)

Because the proof actually shows `phi_Q in L^1(R)`, the inverse Fourier transform supplies a continuous `C_0` density. Thus continuity is proved for this scoped theorem, not merely essential boundedness.

Finally, apply (1.2). If `s_1,s_2` are the singular values of `B`, then the two-dimensional orthogonal projection of the product bank has density cap `2`, and the invertible singular-value map contributes `(s_1s_2)^(-1)`. Hence

`M <= 2/(s_1s_2) = 2 D^(-1/2).`                                   (5.14)

Substitution in (5.13) yields

`||p_Q||_infinity
 <= 5(3sqrt(6)/8)^(4/5) 2^(2/5)
      D^(-1/5)|c|^(-1/5).`                                        (5.15)

The constant simplifies exactly:

`5(3sqrt(6)/8)^(4/5)2^(2/5)
 = (15/4)12^(1/5),`                                                 (5.16)

which proves Theorem 2.1.

## 6. A strict no-pivot target family that the theorem pays

The new mechanism is not an easy localized-pivot restatement. Let `m` be a Walsh/Hadamard order and take three flat orthonormal vectors

`u,v,r in R^m`, `|u_j|=|v_j|=|r_j|=m^(-1/2).`                     (6.1)

Use original physical coordinates

`H_1,H_2,Z,Y_1,...,Y_m`.                                           (6.2)

For `k>=1`, define the symmetric matrix by

`A_(H1,Y)=k u^T`,
`A_(H2,Y)=k v^T`,
`A_(Z,Y)=r^T`,
`A_(Z,Z)=c=k^(-4),`                                                 (6.3)

and set every other coefficient to zero. The quadratic form is

`Q_k
 = 2k H_1 <u,Y>
 + 2k H_2 <v,Y>
 + 2 Z <r,Y>
 + k^(-4) Z^2.`                                                     (6.4)

Because `u,v,r` are orthonormal, the nonzero spectral blocks are exactly

`[[0,k],[k,0]], [[0,k],[k,0]], [[k^(-4),1],[1,0]].`               (6.5)

Hence the spectrum contains

`-k,-k,k,k`                                                        (6.6)

and the two additional roots

`lambda_+- = [k^(-4) +- sqrt(k^(-8)+4)]/2.`                        (6.7)

In particular every `k>=1` has at least four eigenvalues of modulus at least one, so this is a genuine target family.

It can simultaneously lie arbitrarily deep in the physical no-pivot regime. The only nonzero physical diagonal is `k^-4`. Every two-by-two principal determinant has magnitude at most

`max{k^2/m,1/m}.`                                                   (6.8)

Thus for any prescribed `tau>0`, first take `k>tau^(-1/4)` and then `m>k^2/tau`; every physical diagonal and every physical `2x2` principal determinant has magnitude `<tau`, while the four large eigenvalues persist.

For the theorem, take

`B=k [u^T;v^T]`, so `D=det(BB^T)=k^4`,                             (6.9)

and

`c=k^-4`, `q(Y)=2<r,Y>`.                                           (6.10)

Therefore

`D|c|=1`                                                           (6.11)

and Theorem 2.1 gives the completely uniform target-level estimate

`boxed: ||p_(Q_k)||_infinity <= 6.1640693607`                      (6.12)

for every admissible cap-one product law, every `k>=1`, and every allowed Hadamard order `m`. The density is continuous.

This family exposes exactly why the theorem is stronger than the previous independent-residual glue from this B01 slot: the third term is

`k^-4 Z^2 + 2Z<r,Y>`,                                               (6.13)

which shares the entire leaf bank `Y` with the two hub slopes. It cannot be factored as an independent scalar residual.

### Check against the newest projected-crossing theorem

Apply the new grouped-hub theorem `NEW_PROJECTED_CROSSING.md` to the actual physical split

`hubs={H1,H2}`, `I={Z}`, `J={Y_1,...,Y_m}`.                        (6.14)

Its hub-to-`J` matrix is `M_J=B`, of rank two, with singular-value product

`S=k^2`.                                                            (6.15)

The light crossing row is `r^T`. Since `r` is orthogonal to `row(B)=span{u,v}`,

`C=r^T(I-P_row(B))=r^T`, `Z_1=||r||^2=1`.                         (6.16)

However there is only one `I` row. The unique one-volume subset has weight one, so its row marginal is

`alpha_Z=1`,                                                       (6.17)

which violates the required gate `alpha_i<=1/2`. Thus the current weighted-subset crossing theorem is **not applicable** on this partition. This is not a contradiction or criticism of that theorem: it identifies a concentrated-one-row endpoint left outside its stated scope. The scalar square-phase `L^4` budget in Theorem 2.1 pays exactly this concentrated endpoint.

## 7. Required designated-partner application at an actual inequality

The latest completed account02/B01 r46 theorem states, for an invertible indefinite original-coordinate physical pair `P`,

`||p_Q||_infinity
 <= 22.385 D_P^(-1/6) kappa_P^(-1/6) W_2(P)^(-1/12),`             (7.1)

where `D_P=|det A[P,P]|`, `kappa_P=sigma_min(A[P,P])`, and `W_2` is the complete overlap-two pair-Schur currency.

On r46's strict-N3 stress family it proves

`D_P=epsilon^2`, `kappa_P=epsilon`, `W_2(P)>=4 epsilon^(-6).`       (7.2)

Substitution gives, with every epsilon power cancelling,

`||p_Q||_infinity
 <=22.385 epsilon^(-1/3) epsilon^(-1/6)
          (4epsilon^(-6))^(-1/12)`
` =22.385 * 2^(-1/6)`
` =19.9427678056... <19.943.`                                      (7.3)

This is a genuine equation-level use of the designated partner's completed result. It pays a complementary near-singular pair-Schur endpoint. The partner's first remaining issue is the residual `kappa_P` loss in more general near-null states; nothing in Theorem 2.1 claims to remove that structural problem.

## 8. Relation to the prior B01 result and exact advance

The preceding B01 run proved a two-hub theorem of the form

`Q=H^TCH+2H^T(BY+d)+R(Y)+Z_0`                                    (8.1)

when `Z_0` was a **source-disjoint independent residual random variable** with an `L^2` density. Then

`phi_Q(t)=phi_(two-hub packet)(t) phi_(Z_0)(t)`                    (8.2)

and one could spend the residual `L^2(dt)` budget only in the high-frequency tail.

That factorization fails for (2.2) because

`Z_0=cZ^2+q(Y)Z`                                                    (8.3)

depends on `Y`. Theorem 2.1 closes precisely this dependence gap: it pushes the complex, phase-weighted leaf measure through `BY` *after* integrating the original scalar `Z`, and conditional Cauchy-Schwarz converts the partner's scalar `L^4` estimate into an `L^4` budget for the two-hub amplitude. No conditional density cap is asserted.

This is the useful oscillatory replacement requested by the B01 assignment:

- scalar pointwise `|t|^-1/2` decay: false and still rejected;
- two-hub pointwise envelope: only critical `|t|^-1`;
- scalar square phase: uniform `L^4(dt)` rather than pointwise decay;
- product: `|t|^-1 * L^4` is integrable by `4`/`4/3` Holder in the tail.

## 9. Exact remaining implication

The full conjecture is still **OPEN**. The first unpaid implication for this branch is now

`QFORM-N3-TWOHUB-CONCENTRATED-THIRD-ROW-ROUTING-v2`:

starting from the remaining no-pivot / low-volume structural class, produce either

1. a rank-two original two-hub slope matrix `B` and a source-disjoint original scalar coordinate `Z` with nonzero self-curvature `c` after conditioning the remaining coordinates, while allowing arbitrary same-leaf coefficient `q(Y)` — paid by Theorem 2.1; or
2. a diffuse projected crossing satisfying the current `alpha_i<=1/2` volume gate — paid by the new projected-crossing theorem; or
3. an already-paid pair-Schur, rank-three-volume, grouped-square, ridge, hub-star, exact-null, or semidefinite receiver.

The hard survivor is when the third smoothing resource is concentrated but has zero/near-zero physical self-curvature, or is entangled through direct hub--third-coordinate couplings so that the scalar `L^4` amplitude itself depends on the Fourier hub variable. A new dependence-safe estimate is still required there.

No claim of a full proof, counterexample, or two independent end-to-end reviews is made. Full-target continuity remains OPEN; continuity is proved only for Theorem 2.1's scope.

## 10. Finite checks

A deterministic companion check records:

- the exact constants in (5.13)-(5.16);
- the partner cancellation in (7.3);
- the exact stress-family spectral formulas;
- the no-pivot inequalities for one concrete `tau=0.01`, `k=4`, `m=65536` instance;
- the projected-crossing row marginal `alpha_Z=1`.

These checks are diagnostics only; the proof above is analytic.
