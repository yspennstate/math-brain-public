SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T14:49:50Z.
attacking: optimize the fresh third-volume projection/tail certificate, then test it on a dense rotated indefinite matrix whose top singular subspace is maximally localized.

# fleet03/B04 r35 — optimized projection/tail product-Fourier certificate

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control consumed:** revision `2026-09-22.15`; QFORM only.  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.  
**Outcome:** `INDEPENDENT_REVIEW_PASS_ON_NEW_MATRIX/TAIL_CERTIFICATE + NEW_QUANTITATIVE_OPTIMIZATION + EXPLICIT_ROTATED_TARGET_BOUND / FULL_TARGET_OPEN`.  
**Continuity:** proved on every branch of the theorem below because the imported characteristic-function estimate is in `L^1`; full-target continuity remains open.

## 1. Exact sources and live corrections

The source specifically assigned for independent fleet03/B04 review is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`

and its

`PEER_TAIL_EXTENSION.md`.

The latter applies fleet01/B20's completed singular-value identity

`T2 E2 <= 3 E3`,

source

`yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B20/20260922T234545Z-fleet01-B20-QFORM-auto11/REPORT.md`.

A second completed same-role product-Fourier result is used at an actual inequality in Section 6: fleet01/B04's corrected global compatibility-Hellinger theorem

`QFORM-COMPATIBILITY-HELLINGER-COUPLING-v1`,

source

`yspennstate/math-open-problems@77053ce0593dd60c613220d313569cb3f48244bd:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T121357Z-fleet01-B04-QFORM-auto11/REPORT.md`.

I also consumed its correction `QFORM-SIXROW-HELLINGER-UNIVERSAL-EXTRACTION-FALSE-v1`: a single six-row Hellinger packet is not forced at universal scale. Nothing below assumes such an extraction.

The designated partner remains `fleet04/B04`. Fresh lookups found current QFORM login/start evidence but no completed current-QFORM report/handoff from that slot, so no designated-partner result is fabricated or waited for.

No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea estimate, positive conditional projection-density moment, naive fiber supremum, or uniformly good physical minor is used.

## 2. Independent review of the fresh matrix/tail certificate — PASS

Let `M` be an original-coordinate cross block of rank at least three. Write its squared singular values as

`lambda_1 >= lambda_2 >= ... >= 0`,

and put

`Z=E3=e3(lambda)`, `E2=e2(lambda)`, `T2=sum_{j>=3} lambda_j`.

For the canonical squared-3x3-minor volume law, let `alpha_i` be the physical row-inclusion marginals and `W` the row marginal matrix. The source gives

`W=U diag(p_j) U^T`,
`p_j=lambda_j e2(lambda without j)/Z`.

I checked the following steps independently.

1. `0<=W<=I`: since
   `Z=lambda_j e2(lambda without j)+e3(lambda without j)`, one has `0<=p_j<=1`.
2. `W <= (E2/Z) M M^T`: coefficientwise,
   `e2(lambda without j)<=E2`.
3. Fleet01/B20's identity gives
   `T2 E2<=3Z`. Indeed
   `3Z=sum_{p<q}lambda_p lambda_q sum_{r notin {p,q}}lambda_r`,
   and deleting any two coordinates leaves at least the tail mass `T2` because `lambda_1,lambda_2` are the largest two.
4. Consequently
   `W <= (3/T2) M M^T`. This remains valid when `s3` is arbitrarily small as long as collective tail energy survives.
5. For every orthogonal projection `P`, put `l_i=P_ii` and `eps=||(I-P)M||op`. Without assuming that `P` commutes with `MM^T`,

   `sqrt(alpha_i)=||W^(1/2)e_i||`
   ` <= ||W^(1/2)P e_i||+||W^(1/2)(I-P)e_i||`
   ` <= sqrt(l_i)+sqrt(3)*eps/sqrt(T2)*sqrt(1-l_i)`.

   The first term uses `W<=I`; the second uses `W<=(3/T2)MM^T`.

I also re-derived the source's q-dependent Fourier constant. If `alpha_i<=q/2` for all rows, `1<=q<3/2`, the sharp Hausdorff-Young/BL calculation yields

`E F_t^q <= e^3 q^(-3/2) (pi/|t|)^3 Z^(-1/2)`.

Thus

`|phi_Q(t)| <= min(1,K |t|^(-b))`,
`b=3/(2q)>1`,

and exact Fourier inversion gives

`boxed( ||p_Q||inf <= [3e/((3-2q)sqrt(q))] Z^(-1/6) ).`       (2.1)

The endpoint-column convention is safe for the same reason stated in the source: a column with volume marginal one belongs to every positive-weight minor and is removed with its density cap before the determinant expansion. I find no gap in the new matrix/tail certificate or its constants. **Independent review verdict: PASS for this supporting theorem and PEER_TAIL_EXTENSION, not for the full QFORM conjecture.**

## 3. New theorem — `QFORM-OPTIMIZED-PROJECTION-TAIL-CERTIFICATE-v1`

For an arbitrary orthogonal projection `P` on the physical row space define

`rho(P)=sqrt(3)*||(I-P)M||op/sqrt(T2)`,

`h(P)=max_i [sqrt(P_ii)+rho(P)sqrt(1-P_ii)]^2`.               (3.1)

Assume

`h(P)<3/4`.                                                    (3.2)

Set

`q(P)=max(1,2h(P))`.                                           (3.3)

Then `1<=q(P)<3/2`, and Section 2 gives `alpha_i<=h(P)<=q(P)/2`. Therefore, for every independent cap-one product input in the full arbitrary-self-block/outside-coupling/affine scope,

`boxed(
 ||p_Q||inf
 <= C(P) E3(M)^(-1/6),
 C(P)=3e/[(3-2q(P))sqrt(q(P))].
)`                                                               (3.4)

Since the positive terms in `E3` containing singular directions 1 and 2 give

`E3(M) >= s1(M)^2 s2(M)^2 T2`,                                (3.5)

also

`boxed(
 ||p_Q||inf
 <= C(P)[s1(M)^2 s2(M)^2 T2]^(-1/6).
)`                                                               (3.6)

The imported Fourier proof gives `phi_Q in L^1`, hence a density in `C_0(R)`.

For a fixed `h`, the choice (3.3) is optimal within this certificate: on `q>=1`,

`d/dq log[3e/((3-2q)sqrt(q))]
 =2/(3-2q)-1/(2q)
 =(6q-3)/[2q(3-2q)]>0`.

Thus there is no reason to pay the source's fixed `q=4/3` if the actual matrix gives a smaller volume-marginal cap.

## 4. Leverage-free collective-tail exit

Take `P=0`. Then

`h(0)=3 s1(M)^2/T2`.                                          (4.1)

Hence the projection/tail Fourier route works whenever

`boxed( T2>4 s1(M)^2 ).`                                      (4.2)

No leverage assumption is needed. If

`T2>=6 s1(M)^2`,                                               (4.3)

then `h(0)<=1/2`, so `q=1` and

`boxed(
 ||p_Q||inf <=3e E3(M)^(-1/6)
             <=3e[s1^2 s2^2 T2]^(-1/6).
)`                                                               (4.4)

For `r=T2/s1^2` in `(4,6)`, the explicit optimized value is `q=6/r`, giving

`C(r)=3e/[(3-12/r)sqrt(6/r)]`.                                (4.5)

This pays a regime in which the top singular directions can be completely localized, provided the remaining singular energy is sufficiently broad.

## 5. Sharpening the fixed top-two stable-tail threshold

Let `P=P2` be the projection onto the top two left singular directions, put

`ell=max_i(P2)_ii`, `r_tail=T2/s3(M)^2`.

Then

`h(P2)=[sqrt(ell)+sqrt(3/r_tail)sqrt(1-ell)]^2`.               (5.1)

For `ell<3/4`, condition `h(P2)<3/4` is equivalent to

`boxed(
 r_tail > R(ell)
 := 3(1-ell)/(sqrt(3)/2-sqrt(ell))^2.
)`                                                               (5.2)

In particular, if `ell<=1/2`, the right side is maximized at `ell=1/2`, where

`R(1/2)=30+12sqrt(6)=59.393876913398...`.                      (5.3)

Thus the fresh source's convenient sufficient stable-tail requirement `r_tail>=225` can be replaced, at the same `ell<=1/2` leverage level, by the sharp threshold furnished by its own matrix inequality:

`r_tail >30+12sqrt(6)`.                                        (5.4)

The density coefficient is then taken at the actual `q=max(1,2h(P2))`; it grows as the threshold is approached, as it must.

## 6. Explicit dense rotated indefinite target; two product-Fourier certificates

Let `H_32` be the Sylvester Hadamard matrix, `V=H_32/sqrt(32)`, and

`D=diag(2,2,1,...,1)` with thirty trailing ones.

Put

`M=D V`,
`A=[[0,M],[M^T,0]]`.                                           (6.1)

Every physical entry of `M` is nonzero. Since `V` is orthogonal, the singular values of `M` are

`2,2,1,...,1`,                                                  (6.2)

so

`spec(A)={+2,+2,+1^(30),-1^(30),-2,-2}`.                       (6.3)

This is a genuinely rotated indefinite original-coordinate target; all 64 eigenvalues have modulus at least one.

Here

`T2=30`, `h(0)=3*4/30=2/5<1/2`,                               (6.4)

so the new theorem applies at `q=1`. The exact third volume is

`E3 = C(30,3)+8 C(30,2)+16*30 =8020`.                         (6.5)

Therefore, for every admissible independent cap-one product law,

`boxed(
 ||p_(X^T A X)||inf
 <=3e * 8020^(-1/6)
 =1.822720208282299... .
)`                                                               (6.6)

The density is continuous and vanishes at infinity.

This example is outside the fixed sufficient tail gate in `PEER_TAIL_EXTENSION.md` for **every** projection. Indeed `sqrt(T2)/15=sqrt(30)/15<1=s_min(M)`. If `P!=I`, then `||(I-P)M||op>=s_min(M)=1`; if `P=I`, its maximum diagonal is one. Hence no `P` satisfies simultaneously `max P_ii<=1/2` and `||(I-P)M||op<=sqrt(T2)/15`. The optimized inequality therefore strictly enlarges the source's stated sufficient region.

### Equation-level application of a completed peer B04 theorem

Apply fleet01/B04's corrected global compatibility-Hellinger theorem to the same `M`, using the symmetric relation that two physical row triples are compatible exactly when they are disjoint. Because

`M M^T=D^2`,

every row triple `S` has aggregate column-lift volume

`a_S=prod_(i in S) d_i^2`, where `d=(2,2,1^30)`.

The compatibility overlap parameter is `beta_*=0`. Every row triple has at most

`D_deg=C(29,3)=3654`

disjoint partners. Moreover

`B_E=sum_(S cap T=empty) sqrt(a_S a_T)`
`   =20 e6(d)`
`   =20[C(30,6)+4C(30,5)+4C(30,4)]`
`   =25,468,380`.                                               (6.7)

The peer theorem's degree consequence therefore has exact effective currency

`B_E/D_deg =6970`,                                              (6.8)

and gives the actual independent inequality

`boxed(
 ||p_(X^T A X)||inf
 <=3e * 6970^(-1/6)
 =1.8658509168174702... .
)`                                                               (6.9)

Thus two separate product-space rearrangements control this matrix. The new projection/tail optimizer is slightly sharper, `1.82273` versus `1.86586`, because it spends the complete third-volume currency while the peer compatibility bound pays a conditional-entropy/degree loss.

The earlier six-row extraction correction is respected: (6.9) uses the replacement **global** compatibility theorem, not an assertion that one local six-row packet must be large.

## 7. Deterministic checks

`CHECKS.py` and its executed `CHECKS.json` in this run directory verify:

- normalized `H_32` orthogonality to numerical error `2.03e-16`;
- `MM^T=D^2` to operator error `4.72e-16`;
- singular values `2,2,1,...,1` and minimum absolute eigenvalue of `A` `0.9999999999999982`;
- all physical cross entries nonzero, with absolute values between `1/sqrt(32)` and `2/sqrt(32)`;
- `T2=30`, `h(0)=0.4`, `E3=8020`;
- the density constants in (6.6) and (6.9).

These finite checks support the arithmetic only; they are not substitutes for the analytic proof.

## 8. Remaining full-target implication

The full conjecture remains OPEN. The optimized certificate gives a clean quantitative split for any candidate physical cross block:

- if some projection has `h(P)<3/4`, the continuous-density Fourier exit (3.4) pays it;
- failure means every projection has large combined physical leverage/residual ratio. For `P2`, low leverage then forces bounded tail stable rank by (5.2); for `P=0`, failure forces `T2<=4s1^2`.

The next B04 obligation is therefore narrower:

`QFORM-LOW-STABLERANK-HIGHLEVERAGE-COMPILER-v1` — starting from the full no-pivot/N3 reduction, route the simultaneous survivor `T2<=4s1^2` plus failure of the top-two optimized gate into a completed compatibility-Hellinger, coloop/star, pair-log, rank-two half-Riesz, mixed-hub, or grouped-bank endpoint without selecting a vanishing local minor.

The designated `fleet04/B04` result remains unavailable as a completed artifact at this publication point; that is the only partner-specific requirement not satisfiable in this run without inventing evidence. Full-target continuity remains open separately.