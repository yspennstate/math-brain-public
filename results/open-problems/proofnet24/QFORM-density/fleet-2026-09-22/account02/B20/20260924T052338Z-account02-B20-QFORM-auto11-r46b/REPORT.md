SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-24T05:23:38Z.
attacking: the r49/r50 strong physical rank-two survivor by composing the newest account03/B20 indefinite-pair logarithmic envelope with curvature-robust physical-R2 quarter smoothing; then isolate the exact Schur-collapse endpoint that survives both receivers.

# account02/B20 r46b — indefinite pair + post-Schur physical R2 endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL STEP APPLIED / NEW TARGET-LEVEL BRANCH RECEIVER / SCHUR-R1-COLLAPSE ISOLATED / FULL QFORM OPEN**.

Execution memory: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval and publication are not native learned-memory receiver ingestion.

Full target: for every dimension, independent real coordinates with densities at most one, and every real symmetric A having at least three eigenvalues of modulus at least one, prove one universal essential-supremum bound for the density of X^T A X, or give a valid counterexample. No moment, support, iid, Gaussian, log-concave, spectral-coordinate independence or continuity assumption is added here. Continuity remains separate and open.

All coordinates used below are literal ORIGINAL coordinates. Every same-bank quadratic term, affine term, outside coupling, extra eigenvalue and nonzero coefficient tail is retained.

## 1. Sources actually used


Newest completed designated partner actually consumed:

- account03/B20 r47, `yspennstate/math-open-problems@fb3a649f17234d139f1731e78557d2e7b1cdd187`,
  `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T044648Z-account03-B20-QFORM-auto11-r47/REPORT.md`.

Its exact physical-pair envelope is, for an invertible indefinite original-coordinate principal pair B, with

`D=|det B|`, `kappa=sigma_min(B)`,

and exact Schur remainder R,

`p_Q(t) <= 2 sqrt(2)/r + D^(-1/2) E log_+(2r^2/(kappa |t-R|))`      (1.1)

for every `r>0`. The same report pins and applies the completed log-to-quarter transfer.

Curvature-robust rank-two fractional input:

- account02/B19, `yspennstate/math-open-problems@f4d95bc33caf8db11888cceb817c005484f67d31`,
  `proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260924T031336Z-account02-B19-QFORM-auto11/REPORT.md`.

For any literal disjoint physical cross block `M` of a quadratic-affine form on independent cap-one ORIGINAL coordinates, define

`Z2(M)=e2(M^T M)`.

If `Z2(M)>0`, then with no restriction on same-bank curvature or outside couplings,

`H_(1/4):=sup_s E|Q-s|^(-1/4) <= C_R2 Z2(M)^(-1/16)`,             (1.2)

where

`C_R2=3.929131770449763...`.                                      (1.3)

The log-to-quarter theorem underneath the partner composition is source-pinned at
`yspennstate/math-open-problems@25ad8faaac5064b6814d51ae63d894fe97c1eac4`, account04/B20 r3. If `H_(1/4)(W)<=L`, then for every `delta>0`,

`E Psi((W-s)/delta) <= 6 delta^(1/4) L`,                           (1.4)

uniformly in `s`, with the same `Psi` used in the translated pair/square kernel.

The owner-required pinned Claude source was reread at
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. Its unrestricted D5 receiver is used in Section 5 below at an actual live physical cut.

The freshest compatible assembly input used is account03/B19 r50,
`yspennstate/math-open-problems@f3a0b13c6d73bb3ec94be4ad5fc293c60ab7da3f`, whose robust branch supplies a literal light-light cross block with

`sigma_2(M)>mu := 255/65536`.                                     (1.5)

## 2. Abstract pair + quarter-potential endpoint

The first observation is the exact abstraction implicit in the newest designated-partner proof.

### Lemma 2.1 — `QFORM-INDEFINITE-PAIR-QUARTERPOTENTIAL-ENDPOINT-v1`

Let two ORIGINAL coordinates form an invertible indefinite principal pair B. Let

`D=|det B|>0`, `kappa=sigma_min(B)>0`,

and let R be the exact Schur remainder after completing that physical pair. If

`sup_s E|R-s|^(-1/4) <= L`,                                       (2.1)

then Q has an essentially bounded density and

`||p_Q||_infinity <= 3*6^(2/3) D^(-1/3) kappa^(-1/6) L^(2/3)`.   (2.2)

Arbitrary affine shifts depending on the remaining original variables are allowed.

#### Proof

Start from the partner envelope (1.1). Put

`delta=2r^2/kappa`.

Since `log_+(delta/|u|) <= Psi(u/delta)`, the completed transfer (1.4) and (2.1) give

`E log_+(2r^2/(kappa|t-R|))
 <= 6 (2r^2/kappa)^(1/4) L`.                                     (2.3)

Hence for every `r>0`,

`p_Q(t) <= A r^(-1) + C r^(1/2)`,                                (2.4)

with

`A=2sqrt(2)`,
`C=6*2^(1/4) D^(-1/2) kappa^(-1/4) L`.                           (2.5)

The exact minimizer satisfies `r^(3/2)=2A/C`, and

`min_{r>0}(A/r+C sqrt(r))
 =3*2^(-2/3) A^(1/3) C^(2/3)`.                                  (2.6)

The powers of two cancel exactly:

`2^(-2/3)*(2^(3/2))^(1/3)*(2^(1/4))^(2/3)=1`.                   (2.7)

This is (2.2). QED.

## 3. New composed receiver: indefinite physical pair + post-Schur physical rank two

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-SCHUR-R2-ENDPOINT-v1`

Under the hypotheses of Lemma 2.1, write S for the quadratic coefficient matrix of the exact Schur remainder R. Suppose there are disjoint ORIGINAL-coordinate sets `L,M`, disjoint from the selected pair, such that

`Z2 := e2(S[L,M]^T S[L,M]) > 0`.                                 (3.1)

Then the full ambient quadratic law has an essentially bounded density satisfying

`boxed:
||p_Q||_infinity
 <= C_pairR2 D^(-1/3) kappa^(-1/6) Z2^(-1/24),`                  (3.2)

where

`C_pairR2=3*(6*C_R2)^(2/3)
        =24.66530466603276... <24.666`.                           (3.3)

No rank-exactness, sign condition outside the selected pair, diagonal same-bank condition, moment hypothesis, or compact-support assumption is present.

#### Proof

After completing the physical pair, R is a quadratic-affine form in the remaining ORIGINAL coordinates. Their product independence and cap-one densities are unchanged. Its literal cross block on `L|M` is exactly `S[L,M]`. Therefore the curvature-robust physical-R2 theorem (1.2) applies directly to the Schur remainder:

`sup_s E|R-s|^(-1/4)
 <= C_R2 Z2^(-1/16)`.                                            (3.4)

Insert (3.4) into Lemma 2.1. Since `(Z2^(-1/16))^(2/3)=Z2^(-1/24)`, (3.2)-(3.3) follow. QED.

This receiver is complementary to designated-partner r47. Partner r47 survives an arbitrary rank-two Schur correction by spending a **third pre-Schur cross singular** and therefore obtains post-Schur rank one. Theorem 3.1 instead targets the current near-rank-two frontier directly: it requires no pre-Schur third singular, but asks that two-dimensional crossing volume survive in the exact Schur remainder.

## 4. Exact application to the fresh r50 robust light-light branch

Account03/B19 r50 supplies disjoint ORIGINAL-coordinate light banks `L_R,L_C` and the actual literal cross block

`M=A[L_R,L_C]`

with

`sigma_2(M)>mu=255/65536`.                                       (4.1)

Consider an invertible indefinite physical pair P whose two coordinates are disjoint from `L_R union L_C`, and complete that pair. Let S be the exact Schur coefficient matrix. If

`sigma_2(S[L_R,L_C]) >= mu/2 = 255/131072`,                      (4.2)

then

`Z2(S[L_R,L_C])
 >= sigma_1^2 sigma_2^2
 >= (mu/2)^4`.                                                    (4.3)

Thus Theorem 3.1 gives

`||p_Q||_infinity
 <= C_pairR2 D^(-1/3) kappa^(-1/6) (mu/2)^(-1/6)`.               (4.4)

In the all-small-diagonal heavy-edge collar used by designated-partner r47,

`|A_ii|,|A_jj|<=1/64`, `|A_ij|>=1/32`,                           (4.5)

one has exactly the partner lower bounds

`D>=3/4096`, `kappa>=1/64`.                                      (4.6)

Substitution into (4.4) gives the concrete full-law bound

`boxed: ||p_Q||_infinity <1548.904 <1549.`                       (4.7)

The deterministic check gives `1548.9034078724994`.

Therefore a still-unpaid r50 state containing such a disjoint heavy indefinite pair must lie in the new quantitative Schur-collapse collar

`boxed:
sigma_2(S[L_R,L_C]) < 255/131072.`                              (4.8)

Combined with designated-partner r47, any still-unpaid heavy-pair state must also have, after puncturing that pair,

`s_3(A[L,M])<2^-16`                                               (4.9)

for every disjoint remaining physical cross cut `L|M`, unless another paid branch applies. Equations (4.8)-(4.9) separate two different debts: no third pre-Schur crossing, and strong collapse of the surviving two-dimensional crossing after exact pair completion.

## 5. Required pinned D5 source applied at an actual live inequality

Apply the owner-pinned unrestricted fifth-volume theorem D5 to the same actual r50 light-light cut `M=A[L_R,L_C]`. It states

`||p_Q||_infinity <=5 sqrt(2e) e5(M^T M)^(-1/10)`                (5.1)

with no volume-marginal condition.

Therefore at the concrete gate

`e5(M^T M) >= 1/1024`,                                           (5.2)

the full ambient law is already paid by

`boxed:
||p_Q||_infinity <=10 sqrt(2e)
 =23.316439815971243... <23.317.`                                (5.3)

Hence every still-unpaid r50 robust-light state may additionally be assumed to satisfy

`e5(M^T M)<1/1024`.                                               (5.4)

This is an equation-level use of the required pinned `e5f71d79...` package on the current literal physical block, not a background citation.

## 6. The post-Schur rank-two lower bound cannot be forced: exact target-valid obstruction

The new condition (4.2) is not automatically implied by a robust pre-Schur rank-two crossing, even under the full three-large-eigenvalue target and a legal all-small-diagonal physical pair. The exact cancellation family from account02/B19 can be written in the present notation as follows.

Fix `epsilon>0`. Take orthonormal pairs `u,a` and `v,c` in two disjoint physical banks and set

`N=epsilon^(-1) u v^T + a c^T`,                                  (6.1)

and the bordered physical cross block

`Bcross=[[N,u],[v^T,epsilon]]`.                                  (6.2)

Let the full symmetric matrix be the bipartite form

`A=[[0,Bcross],[Bcross^T,0]]`.                                   (6.3)

Select as the physical pair the appended left/right coordinates. Its principal matrix is

`Bpair=[[0,epsilon],[epsilon,0]]`,                               (6.4)

so it is invertible indefinite with

`D=epsilon^2`, `kappa=epsilon`.                                  (6.5)

The exact Schur crossing on the remaining two banks is

`S_cross=N-epsilon^(-1)uv^T=ac^T`,                              (6.6)

which has rank one and therefore

`Z2(S_cross)=0`                                                   (6.7)

exactly, although the pre-Schur N has singular values `epsilon^(-1)` and `1`.

Moreover `Bcross` has nonzero singular values

`epsilon^(-1)+epsilon`, `1`,                                     (6.8)

so the full symmetric A has nonzero spectrum

`{+(epsilon^(-1)+epsilon), +1, -1, -(epsilon^(-1)+epsilon)}`.    (6.9)

Thus it is a genuine target matrix with four eigenvalues of modulus at least one. At the concrete value

`epsilon=1/32`,                                                   (6.10)

the selected pair has zero physical diagonals, edge exactly `1/32`, `D=1/1024`, `kappa=1/32`, while the post-Schur `Z2` still vanishes exactly. The deterministic check reproduces the spectrum

`{-32.03125,-1,0,0,1,32.03125}`.                                (6.11)

This is **not** a QFORM counterexample. In the pure-bilinear model the completed account02/B19 projection theorem pays the family. Its purpose here is structural: any proof claiming that a robust pre-Schur rank-two crossing plus a heavy indefinite physical pair must leave a uniformly positive post-Schur rank-two volume is false, even inside the full target.

The source-valid next problem is therefore exactly the same cancellation geometry **with arbitrary internal same-bank curvature and the remaining live couplings retained**.

## 7. Updated strongest conditional end-to-end proof graph

The compatible current graph on the strong-rank-two side is now:

1. The r49/r50 compiler produces a literal original-coordinate crossing within `2^-16` Frobenius distance of rank two and a robust light-light branch with `sigma_2>255/65536`, or a fixed-strength literal hub star.
2. Designated partner account03/B20 r47 pays every all-small-diagonal entry-heavy indefinite pair that coexists, after puncture, with a disjoint third cross singular `s_3>=2^-16`; the explicit bound there is `<5034`.
3. Theorem 3.1 of this run pays the complementary situation in which, after exact completion of an indefinite physical pair, a genuine two-dimensional Schur crossing remains. At the r50/all-small-diagonal thresholds, `s_2(S[L_R,L_C])>=255/131072` gives `<1549`.
4. The required pinned D5 theorem independently pays the same actual r50 light cut whenever `e5>=1/1024`, with `<23.317`.
5. The exact target-valid family in Section 6 proves that simultaneous failure of items 2 and 3 is real: a physical pair can cancel one entire crossing direction and leave a rank-one Schur crossing while the full target spectrum persists.

Thus the first source-complete unpaid implication on this branch is sharpened to

`QFORM-R50-PAIR-SCHUR-R1-COLLAPSE-WITH-INTERNAL-CURVATURE-PAYMENT-v1`:

> Under the full independent cap-one target, retain the r49/r50 literal physical banks, all same-bank curvature, outside couplings, affine terms, extra spectrum and the nonzero `2^-16` coefficient tail. In the all-small-diagonal branch, suppose an entry-heavy invertible indefinite physical pair is disjoint from the r50 light-light cut; suppose every disjoint post-puncture cross block has `s_3<2^-16`; suppose the exact Schur remainder on the robust light-light cut has `s_2<255/131072`; and suppose the actual r50 light cut has `e5<1/1024`. Prove a universal density bound, or route this near-rank-one Schur cancellation into an already-paid physical-pair, grouped-star/hub, ridge/window, Fresnel, or volume receiver.

The pure-bilinear exact-collapse subcase is already paid. The genuinely unpaid content is the same cancellation with internal curvature sharing the two product banks. This formulation avoids the false stronger implication refuted in Section 6 and retains product provenance through the third smoothing resource.

The entry-diffuse/no-qualified-pair branch and r50 fixed-hub-star endpoint remain parallel debts; they are not renamed as solved.

## 8. Verification and status

`CHECKS.py` and `CHECKS.txt` in this run directory verify:

- `C_pairR2=24.66530466603276...`;
- the r50 heavy-pair application `<1548.904`;
- the pinned D5 threshold bound `<23.317`;
- the exact epsilon=`1/32` Schur-cancellation spectrum and rank-one remainder.

Checker marker: `QFORM_B20_R46B_PAIR_R2_CHECK_PASS`.

Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

Full universal continuity: **OPEN**.

No full-solution claim is made and two independent end-to-end reviews do not exist.
