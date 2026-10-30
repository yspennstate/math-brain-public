SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-23T22:39:46Z.
attacking: the exact-Schur-match diffuse third-curvature endpoint after the newest fleet03/B08 transverse compiler, with emphasis on the remaining aligned hybrid and an explicit actual spectral gate.

# fleet02/B08 r29 — the transverse endpoint is paid; diffuse alignment is a genuine remaining hybrid

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / complementary constructions and source-valid counterexamples  
Designated partner: `fleet03/B08`  
Owner control at startup and refresh: revision `2026-09-22.15`, QFORM only  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING CLOSURE + TARGET-VALID ALIGNED-HYBRID OBSTRUCTION + FIXED-SOURCE PAYMENT / FULL TARGET OPEN**.

The unrestricted QFORM conjecture remains OPEN. All coordinates below are ORIGINAL independent coordinates with one-dimensional densities bounded by one. No moment, support, log-concavity, Gaussianity, post-rotation independence, arbitrary-joint coarea inequality, or coefficient-small random-error deletion is used. Essential boundedness is the target; continuity is asserted only when the cited Fourier theorem supplies it.

## 1. First unpaid implication after this run

The first unpaid B08 implication is now

`QFORM-NEARSINGULAR-EXACTMATCH-ALIGNED-THIRDCURVATURE-COMPILER-v1`.

The previous r28 state had already paid every original-coordinate physical `2x2` principal block with least singular value at least `L/64` by `<619/L`, and in the common-plane branch it paid nonzero post-Schur crossing once the rank-free first-compound currency exceeded its explicit threshold. The exact endpoint was a near-singular hub pair, zero post-Schur crossing, and a diffuse same-bank third square.

The newest designated-partner result now pays the **diffuse transverse rank-one** part of that endpoint. What genuinely remains is a diffuse residual direction that lies close to the two-dimensional hub-arm row plane. The construction below shows that this aligned state is not an artifact: one can have simultaneously

- exactly three target eigenvalues of modulus at least one;
- arbitrarily diffuse physical coordinates;
- robust two-dimensional arm area;
- exact common-plane Schur match and zero post-Schur crossing;
- every physical `2x2` principal block below the r28 `1/64` gate; and
- alignment angle `tau=0` (or `tau ->0`).

Thus “diffuse” alone does not force the transverse currency. A successful next compiler has to aggregate aligned third curvature without paying a reciprocal angle or a reciprocal near-singular hub factor, and must remain valid under arbitrary complementary spectrum.

## 2. Fresh source boundary and the result actually consumed

The owner-required fixed source was reread at

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed result applied below is its Fresnel--Brascamp--Lieb Theorem F: an exact rank-three quadratic form whose orthonormal spectral range has physical leverage at most `1/2` has

`||p_Q||_infty <= 12 |lambda_1 lambda_2 lambda_3|^(-1/3)`,

and the proof gives an integrable characteristic function, hence a continuous `C_0` density. The same source also records why a mere bounded three-dimensional joint density is insufficient: shell counterexamples invalidate the earlier arbitrary-joint coarea shortcut.

The newest compatible designated-partner report read this run is

`fleet03/B08/20260923T222118Z-fleet03-B08-qform-diffuse-r44`,
with theorem commit `2dc8a71902532a4e28c15b86346d758f004bfab3`.

Its new theorem concerns the exact common-plane representation

`A_LL = M^T R M + diag(S_1,S_2)`

with two original physical hubs and two light banks. For a rank-one same-bank residual

`S_1=lambda q q^T`, `||q||=1`,

put

`S_M=s_1(M_1)s_2(M_1)`,
`mu=max_j q_j^2`,
`tau=dist(q,row(M_1))`.

If

`mu<=27/593`, `tau>0`,

then the full ambient form, retaining arbitrary hub self-curvature, arbitrary other same-bank curvature and affine terms, has a continuous `C_0` density and

`boxed:
 ||p_Q||_infty
 <=2^(13/6)sqrt(3)
   (|lambda| S_M tau)^(-1/3)
   (1-3mu)^(-1/6).`                                             (2.1)

The proof uses a physical Bernoulli cut and the independently reviewed grouped projected-crossing theorem; it never rotates the random coordinates.

## 3. The previous exact-match stress family is now paid by the partner

The r28 stress family used three orthonormal Hadamard rows `r_1,r_2,q`, with

`M=[r_1^T;r_2^T]`, `MM^T=I_2`, `Mq=0`,

and exact same-bank residual `q q^T`. Thus in the partner notation

`S_M=1`, `lambda=1`, `tau=1`, `mu=1/m`.

For every `m>=22`, `mu<=27/593`, so (2.1) gives directly

`boxed:
 ||p_Q||_infty
 <=2^(13/6)sqrt(3)(1-3/m)^(-1/6)
 <7.969.`                                                        (3.1)

This bound is independent of the arbitrarily ill-conditioned hub parameter `epsilon`. At `m=64` it is `7.839119913...`, and as `m -> infinity` it tends to `7.776645188...`.

This is a genuine completed implication: the diffuse/transverse exact-Schur-match family that motivated the r28 unpaid endpoint is no longer unpaid. It also supplies the requested actual use of the newest fleet03/B08 result at a real target-valid inequality.

In the inherited live common-plane state, the partner itself records the scaled consequence: if the retained rank-one third Schur curvature has `|lambda|>=L`, the arm area obeys

`S_M > L^2/(64 sqrt(896))`,

and

`mu<=1/48`, `tau>=1/2`,

then

`boxed: ||p_Q||_infty <123.01/L`,                               (3.2)

continuously. Therefore a rank-one diffuse survivor must be localized (`mu>1/48`) or aligned (`tau<1/2`). B08's diffuse debt is the latter.

## 4. New target-valid aligned continuum

### Construction — `QFORM-ALIGNED-DIFFUSE-EXACTMATCH-STRESS-v1`

Let `m=2^q` and choose three distinct normalized Sylvester--Hadamard rows

`r_1,r_2,r_3 in R^m`.

For `0<=tau<=1`, define

`q_tau = sqrt(1-tau^2) r_1 + tau r_3`.                           (4.1)

Then

`||q_tau||=1`,
`dist(q_tau,span(r_1,r_2))=tau`,
`max_j q_tau(j)^2 <=2/m`.                                       (4.2)

Set

`M=[r_1^T;r_2^T]`,
`B=diag(epsilon,-epsilon)`,
`K=M^T B^(-1)M=epsilon^(-1)(r_1r_1^T-r_2r_2^T)`.                (4.3)

On the ORIGINAL-coordinate split

`H (2 coordinates) direct_sum J_1 (m) direct_sum J_2 (m)`

define

`A_(m,epsilon,tau)=
 [[ B,    M,                         M ],
  [ M^T,  K+3 q_tau q_tau^T,         K ],
  [ M^T,  K,                         K ]].`                       (4.4)

Both physical arm areas equal one. The common-plane coefficient is exactly `R_c=B^(-1)`, and there is no cross tail. Completing the hub pair subtracts

`[[K,K],[K,K]]`,

so the Schur residual is exactly

`diag(3q_tau q_tau^T,0)`,                                       (4.5)

and the entire post-Schur physical crossing is zero.

### Theorem 4.1 — exact target spectrum

For every `epsilon>0` and every `tau in [0,1]`, (4.4) has exactly three nonzero eigenvalues, all of absolute value strictly greater than or equal to one.

Proof. The `r_2` sector is

`A_- = -(1/epsilon)cc^T`, `c=(epsilon,-1,-1)`,

hence contributes the single eigenvalue

`lambda_- = -(epsilon+2/epsilon)`.                               (4.6)

The positive sector is the sum of two rank-one positive matrices: the common-plane `r_1` vector and the bank-one `q_tau` square. Its two nonzero eigenvalues `theta_+>=theta_->0` obey

`theta_++theta_- = epsilon+2/epsilon+3`,                         (4.7)

`theta_+theta_- = 3(1+epsilon^2+tau^2)/epsilon`.                (4.8)

Equation (4.8) is the two-vector Gram determinant: the common-plane vector has squared norm `epsilon^2+2`, while its inner product with the unit bank-one `q_tau` vector is `sqrt(1-tau^2)`. Evaluating the positive-sector characteristic polynomial at one gives

`(1-theta_+)(1-theta_-)
 =1-(epsilon+2/epsilon+3)+3(1+epsilon^2+tau^2)/epsilon
 >=1/epsilon+2epsilon-2 >0`.                                    (4.9)

Since `theta_+>1`, (4.9) forces `theta_->1`. Together with (4.6), this proves the target spectral claim. QED.

The actual spectral gate is therefore explicit: at scale `L=1`, this is not merely a large-Frobenius or approximate-spectrum witness; the matrix itself has exactly three nonzero target eigenvalues.

## 5. Exact obstruction to a transversality-free projected receiver

At `tau=0`, `q_0=r_1` lies exactly in `row(M)`, while it is still coordinate-diffuse: `max_j q_0(j)^2=1/m ->0`.

Take any physical cut `K_0 subset J_1` for which `M[:,K_0]` has row rank two, and let `P_{K_0}` be projection onto its row space. Then `(q_0)_{K_0}` is literally the first row of `M[:,K_0]`, so

`(I-P_{K_0})(q_0)_{K_0}=0`.                                     (5.1)

The fleet03/B08 r44 projected same-bank currency therefore has

`F_{K_0}=0`                                                     (5.2)

for **every** admissible physical cut. For `tau>0`, theorem (2.1) becomes, using `lambda=3`, `S_M=1` and `mu<=2/m`,

`||p_Q||_infty
 <=2^(13/6)sqrt(3)(3tau)^(-1/3)(1-6/m)^(-1/6)`,                 (5.3)

so that proof route deteriorates like `tau^(-1/3)` as `tau->0`.

But Theorem 4.1 shows that the third target eigenvalue does **not** deteriorate. At `epsilon=1/128`, for example,

`theta_-(0)=1.491257279...`,
`theta_-(0.1)=1.506256675...`,
`theta_-(1)=3`.

Thus no structural lemma may infer a universal transverse angle from “three large eigenvalues + diffuse residual + robust arm area + exact match”. The aligned state is genuine.

## 6. The r28 physical-pair gate also cannot remove this state

Every entry of `M` has modulus `m^(-1/2)`. Since the Hadamard row squares agree coordinatewise, `diag K=0`, and every off-diagonal entry of `K` has modulus at most `2/(epsilon m)`. Equation (4.2) gives

`|3q_tau(i)q_tau(j)| <=6/m`.                                    (6.1)

Hence:

1. the physical hub pair has least singular value exactly `epsilon`;
2. any hub-light principal pair has

   `sigma_min <=sqrt(1/m+36/m^2)`;                              (6.2)

3. every light-light principal pair has operator norm at most

   `2/(epsilon m)+12/m`.                                        (6.3)

Therefore if

`0<epsilon<1/64`,
`m>max(8192,128/epsilon+768)`,                                  (6.4)

**every** original-coordinate `2x2` principal block lies below the r28 spectral gate `sigma_min=1/64`.

At the concrete point

`epsilon=1/128`, `m=65536`,                                    (6.5)

the three deterministic bounds are

`0.007812500000`,
`0.003907322736`,
`0.004089355469`,                                               (6.6)

all strictly below `1/64=0.015625`.

The early checkpoint contained a harmless decimal typo in the second number (`0.0039076...`); equation (6.6) is the checked value. The formula there was correct.

Thus the aligned continuum survives both currently explicit actual gates: it has no well-conditioned physical pair and no post-Schur crossing, while remaining genuinely target-valid.

## 7. Required fixed-source Theorem F pays the same obstruction uniformly

The family is a mechanism counterexample, not a QFORM counterexample.

Its full spectral range is exactly three-dimensional. The spectral projection leverage can be bounded without diagonalizing the random coordinates:

- hub 1 leverage is at most `epsilon^2/(1+epsilon^2)`;
- hub 2 leverage equals `epsilon^2/(epsilon^2+2)`;
- a bank-one physical coordinate has leverage at most

  `2/m + 1/[m(epsilon^2+2)] < 5/(2m)`;

- a bank-two coordinate has leverage at most

  `1/m + 1/[m(epsilon^2+2)] < 3/(2m)`.

For the first bound, any vector in the positive two-dimensional range carrying hub-1 coefficient `epsilon a` necessarily carries bank-two `r_1` component of norm `|a|`; the extra `q_tau` vector has no bank-two component, so it cannot cancel that denominator. The bank bounds use that the positive bank-one components lie in `span(r_1,r_3)` and the negative sector lies in `span(r_2)`.

Hence for `epsilon<1` and `m>=5`, every physical leverage is below `1/2`. The fixed-source Fresnel--Brascamp--Lieb Theorem F applies to the whole exact rank-three form. Using (4.6) and (4.8),

`|lambda_- theta_+ theta_-|
 =3(1+epsilon^2+tau^2)(epsilon^2+2)/epsilon^2`.                 (7.1)

Therefore, for every admissible independent cap-one product source,

`boxed:
 ||p_(X^T A_(m,epsilon,tau) X)||_infty
 <=12[3(1+epsilon^2+tau^2)(epsilon^2+2)/epsilon^2]^(-1/3).`      (7.2)

Moreover this density is continuous and vanishes at infinity.

At (6.5), (7.2) gives

`tau=0:   0.260002543314...`,
`tau=0.1: 0.259141653634...`,
`tau=1:   0.206366254545...`.                                   (7.3)

By contrast, the partner transverse estimate (5.3) at the same `m` is approximately

`25.0279` at `tau=0.01`,
`11.6169` at `tau=0.1`,
`8.05474` at `tau=0.3`,                                         (7.4)

and is unavailable at `tau=0`. The target density itself becomes no worse there; only the transverse currency disappears.

This is the required fixed `e5f71d79...` source result applied to a real target-valid obstruction. Whole-range aggregation succeeds exactly where bounded physical-pair and projected-transverse mechanisms both vanish.

## 8. What has actually been narrowed

For the rank-one exact-match descendant, the diffuse/localized split can now be refined into three explicit branches:

- **transverse diffuse:** `mu<=1/48`, `tau>=1/2`; partner r44 pays `<123.01/L` continuously;
- **localized:** `mu>1/48`; an actual physical coordinate carries a fixed fraction of the third direction;
- **aligned diffuse:** `mu<=1/48`, `tau<1/2`; genuinely nonempty even with all physical pairs below `L/64`, as Sections 4-6 prove.

The first branch is now closed. The construction rules out any attempt to close the third branch merely by proving a positive angle from the target spectrum. In exact rank three, fixed-source Theorem F closes it. The remaining debt is **stability under arbitrary complementary spectrum and arbitrary non-diagonal same-bank curvature**: recover a collective rank-three mechanism before extra curvature can cancel the useful physical crossings, without assuming independence after a spectral rotation.

A natural next target is an aligned compiler that reduces to (7.2) when the complement vanishes and to the partner projected-crossing theorem when transverse energy reappears. It must not delete small matrix tails as small random quadratic errors.

## 9. Deterministic verification

`CHECKS.py` and `CHECKS.txt` in this run folder verify:

- the exact three nonzero eigenvalues against direct matrices at `m=16`, `epsilon=1/128`, for `tau=0,0.1,0.3,1`, with maximum numerical error below `3e-13`;
- all computed small positive eigenvalues exceed one;
- full spectral leverage is below `1/2` in the test matrices;
- the concrete physical-pair bounds (6.6);
- the fixed-source bounds (7.3);
- the partner angle loss (7.4); and
- the partner payment of the previous perpendicular stress family.

The output terminates

`QFORM_B08_R29_CHECK_PASS`.

## 10. Status

This run proves no unrestricted universal constant and gives no QFORM counterexample. It closes the previous **transverse** exact-match stress family by a fresh partner theorem and isolates a sharper **aligned diffuse** survivor with an exact target-valid construction. The unrestricted theorem remains OPEN.
