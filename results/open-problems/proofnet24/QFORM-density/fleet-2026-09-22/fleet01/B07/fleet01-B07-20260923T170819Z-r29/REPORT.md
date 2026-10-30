SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-23T17:08:19Z.
attacking: `QFORM-PLUCKER-ONEHUB-OR-MACROEDGE-RANK2-STABILITY-v1` — close the near-product rank-two determinant-law one-hub face by conditioning the Plucker law itself, then spend the anchored E2 bank through the proved E2-to-E1 mixed half-Riesz receiver before any reciprocal pivot.

# fleet01/B07 r29 — near-rank-two Plucker law: macro-minor or half-Riesz

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / GEOMETRY  
Run: `fleet01-B07-20260923T170819Z-r29`  
Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.  
Status: **NEW PLUCKER ONE-HUB COMPILER / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN / CONTINUITY OPEN**.

The full theorem is not claimed. All random variables remain in ORIGINAL independent coordinates. Singular vectors below are deterministic coefficient devices only; no input law is rotated. No Gaussianity, moments, bounded or connected support, log-concavity, iid hypothesis, diagonal-basis assumption, fiber-density supremum, law-uniform pointwise quadratic-phase decay, or one-good-minor reciprocal estimate is used.

## 1. Source dependencies actually checked

1. Own r28 exterior-square theorem: `yspennstate/math-open-problems@45934a636682207f422de4ab3f94c658030ba1ac`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260923T160359Z-r28/REPORT.md`. It proves the dimension-free TV comparison between the full E2 determinant law and the product Plucker law of the best rank-two truncation.
2. Own r25 E2 half-Riesz theorem: `yspennstate/math-open-problems@fa0ddeb784bad52ae142e49e7c9448d4772decf8`, `.../fleet01-B07-20260923T130435Z-r25/REPORT.md`.
3. Own r26 anchored E2-to-E1 shadow and mixed order-2/order-1 half-Riesz theorem: `yspennstate/math-open-problems@dfb5c8b66cb2f60c1bd3dd202c609902cd5208b2`, `.../fleet01-B07-20260923T140342Z-r26/REPORT.md`.
4. Completed designated partner fleet02/B07 theorem: `yspennstate/math-open-problems@5ff9d960bffec400a9d6db422401e4c4df98ce6d`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T150720Z-fleet02-B07-qform/REPORT.md`. It proves the star-supported E3-to-rank-two-tube inequality used in Section 5.
5. Current grouped projected-crossing theorem: `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. This was checked for scope. It supplies a separate one-hub+crossing analytic receiver, but does not subsume the determinant-law structural compiler below.
6. Current Claude-attributed continuation at `c4c23b784395630c094ba299a50712209921d1ae`, including `single_hub_core/REPORT.md`, was checked. Its conditional-adaptation proposal `(SP)` remains open and is not used here.
7. The newer fleet02/B01 one-hub/one-cross half-Riesz peel at math-open-problems commit `d6e918e3fff5fa26336653cd309bb11bb5313635` was read before publication. It confirms the scalar-square/half-Riesz endpoint for an actual projected crossing; the result below is complementary because it constructs the needed fractional currency from a near-rank-two determinant law rather than assuming a projected-crossing gate.

## 2. Exact Plucker marginal identities

Let `K` be a physical cross block between disjoint ORIGINAL-coordinate banks. Assume

`Omega := E2(K) = sum_(|R|=|C|=2) det K[R,C]^2 > 0`.

Let `W` be the complete physical E2 determinant law

`W(R,C)=det K[R,C]^2/Omega`.

Let the best rank-two truncation be

`K2 = sigma1 u1 v1^T + sigma2 u2 v2^T`,

with two-column orthonormal frames `U=[u1,u2]`, `V=[v1,v2]`. Define the left and right Plucker pair laws

`mu({i,j}) = det U[{i,j},:]^2`,
`nu({k,l}) = det V[{k,l},:]^2`.

Cauchy--Binet gives `sum mu=sum nu=1`. The rank-one second compound of `K2` gives the exact product determinant law

`W0 = mu x nu`.

For every physical left coordinate `i`, let

`ell_i = ||U[i,:]||_2^2`.

Then the Plucker inclusion marginal is exactly

`boxed: sum_(j!=i) mu({i,j}) = ell_i.`                                      (2.1)

Indeed, if the two columns of `U` are `a,b`, orthonormality gives

`sum_j (a_i b_j-b_i a_j)^2 = a_i^2+b_i^2`.

The analogous right inclusion marginal is `m_k=||V[k,:]||_2^2`. In particular

`sum_i ell_i=sum_k m_k=2`.

### Unique-hub conditional law

Fix `h=3/4`. Suppose a left coordinate `s` is the unique coordinate with `ell_s>h`. Conditional on `s` appearing in the Plucker pair, the residual-coordinate law is

`mu_s(i)=mu({s,i})/ell_s`.

The 2x2 Gram determinant inequality gives

`mu({s,i}) = det(U_s,U_i)^2 <= ell_s ell_i`.

Therefore

`boxed: mu_s(i) <= ell_i <= 3/4 for every i!=s.`                         (2.2)

This is the key exact fact: a one-hub two-plane becomes diffuse after conditioning on its physical hub, without rotating the input variables.

## 3. Main theorem — `QFORM-NEARRANK2-PLUCKER-MACROORRIESZ-v1`

Assume

`dTV(W,W0) <= 1/64`.                                                      (3.1)

Then at least one of the following holds.

### (A) Macroscopic actual coordinate minor

There are physical row coordinates `i1,i2` and physical column coordinates `j1,j2` such that

`boxed: det K[{i1,i2},{j1,j2}]^2 >= (15/64) Omega.`                       (3.2)

### (B) Full-ambient half-Riesz payment

For every ambient quadratic-plus-affine form `R` containing this physical cross block, with arbitrary same-bank curvature, outside couplings, affine terms, signs and additional spectrum retained,

`boxed:
 H_(1/2)(R):=sup_t E|R-t|^(-1/2)
 <=39.379 Omega^(-35/253) E^(27/1012),
}`                                                                            (3.3)

where

`E=||K||_F^2`.

Equivalently,

`H_(1/2)(R)
 <=39.379 Omega^(-1/8) (E^2/Omega)^(27/2024).`                          (3.4)

No density conclusion for `R` itself is asserted merely from (3.3).

### Proof

Classify the top-two singular planes by the number of physical coordinates whose leverage exceeds `3/4`.

#### Case 1: one side has no leverage hub

Suppose `ell_i<=3/4` for every left coordinate. Since event probabilities move by at most total variation, the actual determinant-law row inclusion marginals `alpha_i` satisfy

`alpha_i <= ell_i +1/64 <=49/64`.

Apply r25 `QFORM-E2-FRACTIONAL-TRACE-v1` with

`q=2(49/64)=49/32<2`.

It gives

`H_(1/2)(R)
 <= [8 sqrt(e/2)/(2-q)] q^(-1/4) Omega^(-1/8)
 <17.887 Omega^(-1/8).`                                                (3.5)

The right-side no-hub case is identical by transposition. Since `Omega<=E^2/2`, (3.5) is stronger than (3.3).

#### Case 2: each side has at least one hub, and one side has a unique hub

Suppose the left side has a unique hub `s` with `ell_s>3/4`; choose any right hub `t` with `m_t>3/4`. Let

`A={s belongs to R and t belongs to C}`.

Under the product law,

`W0(A)=ell_s m_t>9/16`.

By (3.1),

`p:=W(A) >= 9/16-1/64 =35/64`.                                      (3.6)

For any two probability laws `P,Q` and event `A` with `P(A)=p>0`,

`dTV(P(.|A),Q(.|A)) <= 2 dTV(P,Q)/p`.                               (3.7)

Indeed, for every `B subset A`,

`|P(B)/p-Q(B)/q_A|
 <= |P(B)-Q(B)|/p + Q(B)|p-q_A|/(p q_A)
 <= 2 dTV(P,Q)/p`.

Thus here

`dTV(W(.|A),W0(.|A)) <= 2/35`.                                     (3.8)

Now `W0(.|A)=mu_s x nu_t`. By (2.2), every residual left-coordinate inclusion marginal of `mu_s` is at most `3/4`. Therefore every residual left marginal `gamma_i` of the actual anchored E2 law `W(.|A)` obeys

`gamma_i <=3/4+2/35 =113/140 =: eta <1`.                            (3.9)

The actual physical anchored E2 determinant mass is

`G = p Omega >= (35/64)Omega`.                                     (3.10)

Apply r26 `QFORM-ANCHORED-E2-EXACT-E1-SHADOW-v1` to this doubly anchored physical packet. It produces a fractional physical E1 packet of mass

`Z1=G/R_s^2`,

where `R_s=||K[s,*]||_2`, whose normalized residual row law is exactly `gamma_i`. The E2 packet itself has row marginals `1` at `s` and `gamma_i` elsewhere.

Apply r26 `QFORM-MIXED21-FRACTIONAL-HALFRIESZ-v1` with

`w=eta=113/140`,
`q=2 eta=113/70`,
`r=1+w=253/140`.

At the anchor, the mixed marginal is `w=q/2`; at every residual row it is `gamma_i<=eta=q/2`. Since `q<r`, the theorem applies and gives

`H_(1/2)(R)
 <=36.2238134022 G^(-35/253) R_s^(27/506).`                         (3.11)

Using (3.10) and `R_s<=sqrt(E)`,

`boxed:
H_(1/2)(R)
 <=39.37809584 Omega^(-35/253) E^(27/1012).
}`                                                                         (3.12)

The case where the right side is the unique-hub side is identical by transposition.

#### Case 3: both sides have at least two hubs

Choose distinct left hubs `i1,i2` and distinct right hubs `j1,j2`. Since a Plucker sample is a two-element set, Bonferroni gives

`mu({i1,i2}) >= ell_i1+ell_i2-1 >1/2`,
`nu({j1,j2}) >1/2`.

Hence the single product-law atom corresponding to the literal physical minor has

`W0({i1,i2},{j1,j2})>1/4`.

Total variation (3.1) gives

`W({i1,i2},{j1,j2}) >=1/4-1/64=15/64`.

Multiplying by `Omega` proves (3.2). QED.

### Remarks on the theorem

1. The theorem averages the entire E2 determinant law before any coordinate localization. The only selected minor is selected after it is proved to carry at least `15/64` of the entire determinant currency.
2. Repeated singular values are harmless: choose any orthonormal top-two singular frame; the exterior-square and Plucker identities are exact for that choice.
3. No independence of singular coordinates is used. `U,V` enter only into deterministic weights.
4. (3.3) is a half-Riesz statement. It becomes a full density bound when an independent original scalar square sits outside the residual, as in Section 4.

## 4. Scalar-square corollary

Suppose an ORIGINAL coordinate has been exactly completed as

`Q = a (X+h(Y))^2 + R(Y)`, `a!=0`,

where `X` is independent of the remaining original coordinates and the residual `R` contains the physical cross block `K` above. The cap-one law of `X` gives the standard exact square peel

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`.

Therefore, under (3.1), either the macroscopic physical minor (3.2) exists or

`boxed:
 ||p_Q||_infinity
 <=39.379 |a|^(-1/2)
          Omega^(-35/253) E^(27/1012).
}`                                                                         (4.1)

This proves absolute continuity and essential boundedness on this scalar-square branch. Continuity is **not** claimed.

The newly read fleet02/B01 theorem at commit `d6e918e...` proves another scalar-square half-Riesz payment from a one-hub/one-projected-crossing geometry. It is not a duplicate of (4.1): that theorem assumes a transverse projected crossing with row-volume marginals <=1/2; (4.1) instead derives usable fractional currency solely from near-product E2 determinant geometry.

## 5. Required actual application of the completed fleet02/B07 partner theorem

The completed designated-partner theorem at `5ff9d960...` gives, for its physical star/E2 state,

`dist_F(K,rank<=2) <= (2G_*/S^2)^(1/4)`,                              (5.1)

where `S` is the physical star norm and `G_*` is the complete star-supported anchored third-compound packet.

From r28, with

`delta=Omega-sigma1^2 sigma2^2`,
`rho=delta/Omega`,

we have the exact dimension-free inequalities

`delta <= E T2(K)`,

and hence, by (5.1),

`boxed:
 rho <= (E/Omega) sqrt(2G_*/S^2).
}`                                                                         (5.2)

Also r28 proves

`dTV(W,W0) <= sqrt(rho)+rho/2`.                                      (5.3)

Define

`rho_* := (sqrt(33/32)-1)^2
        =0.0002403988410099117...`.

It is chosen exactly so that

`sqrt(rho_*)+rho_*/2=1/64`.

Therefore the actual partner inequality

`boxed:
 G_* <= c_* S^2 Omega^2/E^2,
 c_*:=rho_*^2/2
     =2.88958013795e-8
}`                                                                         (5.4)

forces `dTV(W,W0)<=1/64`, and Theorem 3 applies.

Thus the designated partner's rank-two-tube branch is now sharpened to the following exhaustive conclusion:

* either

  `G_*>2.88958013795e-8 S^2 Omega^2/E^2`,

  so explicit physical third-volume currency is regenerated;
* or one actual physical `2x2` minor carries at least `15/64` of the complete E2 determinant mass;
* or the full ambient residual carries the half-Riesz estimate (3.3), and any enclosing original scalar-square branch is paid by (4.1).

This is an actual use of the partner theorem at a numerical inequality, not merely a citation.

## 6. What remains open

The previous r28 one-hub Plucker debt is closed **at the half-Riesz level**. The first B07 debt is now narrower:

`QFORM-PLUCKER-MACROMINOR-THIRD-SMOOTHING-OR-NOSCALAR-RECEIVER-v1`.

Two situations remain:

1. the `15/64` macroscopic physical `2x2` minor must be combined with a third independent/product-provenance smoothing resource while retaining arbitrary same-bank curvature and nonzero tails; a rank-two crossing alone is the logarithmic endpoint and is not enough;
2. when no enclosing scalar square is available, the half-Riesz currency (3.3) is not by itself a bounded-density theorem. It must be paired with a genuine additional original-coordinate smoothing direction. The new projected-crossing theorem is a plausible receiver when its exact `M_J`, projected-volume, and <=1/2 marginal gates can be verified, but those gates are not automatic from the present theorem.

The current Claude `(SP)` proposal remains open and is not used to bridge either debt.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Global continuity remains `OPEN`.

## 7. Constants/checks

The exact constants used above are:

`eps=1/64`,
`p=9/16-eps=35/64`,
`2eps/p=2/35`,
`eta=3/4+2/35=113/140`,
`r=253/140`, `q=113/70`, `r-q=27/140`,
`C_mixed=36.223813402128734`,
`C_after_G=39.37809583990397`,
`C_nohub=17.886255241223758`,
`rho_*=0.0002403988410099117`,
`c_*=2.8895801379454404e-8`.

These numerical evaluations only check the displayed arithmetic; the proof is analytic.
