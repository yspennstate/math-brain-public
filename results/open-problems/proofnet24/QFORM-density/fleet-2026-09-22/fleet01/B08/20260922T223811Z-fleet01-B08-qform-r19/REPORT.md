SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-22T22:38:11Z.
attacking: compare volume-sampling and one-scale ridge certificates on the same surviving diffuse bicolop matrix, consume the fresh fractional-E2 theorem, and test whether ridge-or-volume can be exhaustive.

# fleet01/B08 QFORM r19 — volume marginals are forced heavy in the bicolop survivor, and ridge-or-volume is not exhaustive

**Outcome:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / REFUTED_INTERMEDIATE_EXHAUSTIVE_ALTERNATIVE / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  

The unrestricted target remains OPEN: for every finite `n`, every independent real product input with one-dimensional probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `X^TAX`, or give a target-valid counterexample. No Gaussian, moment, compact-support, connected-support, log-concavity, spectral-coordinate independence, or diagonal-basis assumption is added. Continuity remains a separate issue.

This run follows the newest proof-first B07/B08 request literally: compare the fresh volume-sampling and ridge certificates on the SAME original-coordinate matrix and prove or refute the needed exhaustive alternative. A source-matching rank-two fractional-volume theorem appeared during the run, so I do not duplicate it. Instead I apply its exact gate to the live B08 survivor and prove that the gate is quantitatively impossible there. I then give a target-valid family on which every one-scale ridge certificate and both current canonical volume-sampling gates fail, while the designated `fleet02/B08` grouped theorem still gives a uniform density bound. Thus the failure is in the proposed certificate dichotomy, not in QFORM.

## 1. Correction boundary and fresh source inputs

I do not use law-uniform pointwise quadratic-phase decay, independence after spectral rotation, an arbitrary-joint coarea inequality, a positive moment of a worst conditional projection density, a fiber supremum, a uniformly large single physical minor, or perturbative deletion of a small quadratic tail. All matrices below are physical original-coordinate blocks and every positive density conclusion keeps the cap-one product provenance.

### 1.1 Designated partner `fleet02/B08`

Completed theorem `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1`:

`yspennstate/math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T204103Z-1dd824/REPORT.md`.

For an exact-rank-two physical cross block `C`, fixed physical row `j` and column `r`, and

`Delta_jr(C)=sum_(k!=j,s!=r) det C[{j,k},{r,s}]^2`,

it proves

`||p_R||_3 <= 3^(2/3) 2^(1/3) Delta_jr(C)^(-1/6)`

with arbitrary same-side quadratic-affine phases and outside original-coordinate conditioning retained. With the completed dependence-safe genuine outer square of coefficient `a!=0`, it gives

`||p_Q||_infinity <= C_grp |a|^(-1/2) Delta_jr(C)^(-1/8)`,

where

`C_grp=(2^(4/3)+1)sqrt(3)2^(1/4)=7.250055108887958...`.

Section 5 applies this theorem to an actual target-valid family.

### 1.2 Source state of the live B08 bicolop survivor

The source-pinned structural state is in

`yspennstate/math-open-problems@5f28a8cad9d3e1c3fbf3f5ea859bc482de077c28`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260922T214214Z-fleet01-B08-qform-r18/REPORT.md`,

using the preceding fleet03/B08 spectral-gap report. There is an ACTUAL original-coordinate cross block

`H=sum_nu h_nu u_nu v_nu^T`, `h_1>=h_2>=...`,

a scale `gamma>0`, physical anchor row `j` and column `r`, and

`L_j:=u_1(j)^2+u_2(j)^2 > L0:=6221/6450`,

`R_r:=v_1(r)^2+v_2(r)^2 > L0`,

`h_2^2 > gamma^2/2`,

`S:=sum_(nu>=3) h_nu^2 < s0 gamma^2`,

`s0:=329/3218176 = 0.000102231823243974...`.

At the source ridge scale `g=gamma/16`, the same survivor has a left and right ridge leverage above `0.99` while the total ridge effective dimension is below `2.01`. The preceding B08 theorem also proves the full untruncated incident exterior bank `Delta_jr(H)>0.59 gamma^4`.

### 1.3 Fresh source-matching fractional `e_2` theorem — duplicate work stopped

During this run fleet03/B01 published `QFORM-FRACTIONAL-E2-BL-L3-v1` and its outer-square version:

`yspennstate/math-open-problems@3642c75fb0909326c54c407eff8362f124f6bed7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260922T223030Z-auto12/REPORT.md`.

For a physical cross block `M`, let

`E=e_2(M^TM)=sum_(|S|=|T|=2) det(M[S,T])^2`

and use the canonical squared-minor volume distribution `w_ST=det^2/E`, with row marginals `alpha_i=P(i in S)`. For any `2/3<theta<1`, if

`theta alpha_i <= 1/2` for every row,

then the residual has an `L^3` density with a dimension-free `E^(-1/6)` bound; a genuine outer original-coordinate square then yields an essential `L^infinity` bound. This strictly contains the nonfractional `e_2` argument I was deriving, so I stop that duplicate line and test its actual gate instead.

### 1.4 Fresh fleet03/B08 successor

The newest same-assignment result is

`yspennstate/math-open-problems@ce84072924669b04f77a5591b7920b99f8ca29ef`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T222318Z-fleet03-B08-qform-diffuse-r23/REPORT.md`.

It pays a localized physical-row branch without deleting the tail and leaves a much narrower compiler: one exact weighted bilinear channel plus one extremely diffuse ridge channel. The comparison below shows why the raw common-scale volume-sampling gate cannot simply replace that compiler in the earlier bicolop state.

## 2. New theorem: the live bicolop block is volume-sampling heavy at orders two and three

Put

`lambda_nu=h_nu^2`,

and keep the same `S=sum_(nu>=3)lambda_nu<s0 gamma^2`. Let `T_2=e_2(lambda_3,lambda_4,...)` and `T_3=e_3(lambda_3,lambda_4,...)`. Then

`T_2<=S^2/2`, `T_3<=S^3/6`.

### Theorem 2.1 — `QFORM-BICOLOOP-VOLUME-MARGINAL-HEAVY-v1`

For the ACTUAL cross block `H` in Section 1.2:

1. the canonical squared-`2 x 2`-minor volume-sampling row marginal at the physical anchor `j` satisfies

`alpha_j^(2) > 32207793530528803/33400218073497600`

`=0.964298899475900... >24/25`;

2. the canonical squared-`3 x 3`-minor volume-sampling row marginal, whenever `e_3(H^TH)>0`, satisfies

`alpha_j^(3) > 96633261942995107/100200654220492800`

`=0.964397515113548... >24/25`;

3. the same two statements hold for the physical anchor column `r` after transposing `H`.

Consequently:

- the reviewed rank-three Theorem D gate `alpha_i<=1/2` fails strongly;
- the fresh fractional rank-two gate `theta alpha_i<=1/2` fails for **every** permitted `theta>2/3`, because `alpha_j^(2)>24/25` forces `theta<25/48<2/3` if the gate were to hold;
- at the already source-certified ridge scale `g=gamma/16`, the one-scale ridge gate also fails: `max diag K_g>0.99` forces `q>1.98`, while `tr K_g<2.01` makes the required `tr K_g>2q>3.96` impossible.

Thus the current raw ridge certificate and both current canonical volume-sampling certificates fail simultaneously on the SAME source-valid physical cross block.

### Proof: order two

For squared-minor volume sampling of order two, the singular-direction inclusion probabilities are

`p_nu^(2)=lambda_nu (sum_(mu!=nu)lambda_mu) / e_2(lambda)`.

The physical row marginal is

`alpha_j^(2)=sum_nu p_nu^(2) u_nu(j)^2`.

Since `lambda_1>=lambda_2`,

`p_1^(2)-p_2^(2)=(lambda_1-lambda_2)S/e_2(lambda)>=0`.

Also

`e_2(lambda)=lambda_1 lambda_2 +(lambda_1+lambda_2)S+T_2`,

so

`1-p_2^(2)
 =(lambda_1 S+T_2)/e_2(lambda)`

`<= S/lambda_2 + T_2/(lambda_1 lambda_2)`

`< 2s0+2s0^2`.                                                    (2.1)

The last line uses `lambda_2>gamma^2/2`, `lambda_1>=lambda_2`, `S<s0 gamma^2`, and `T_2<=S^2/2`.

Therefore

`alpha_j^(2)
 >=p_2^(2)[u_1(j)^2+u_2(j)^2]`

`>L0(1-2s0-2s0^2)`

`=32207793530528803/33400218073497600`

`>24/25`.                                                         (2.2)

### Proof: order three

Assume `e_3(lambda)>0`; otherwise the rank-three volume theorem is unavailable anyway. For order-three volume sampling,

`p_nu^(3)=lambda_nu e_2(lambda_without_nu)/e_3(lambda)`.

Again `p_1^(3)>=p_2^(3)`, because their difference is `(lambda_1-lambda_2)T_2/e_3(lambda)>=0`. Expanding around the top two singular values gives

`e_3(lambda)=lambda_1 lambda_2 S +(lambda_1+lambda_2)T_2+T_3`,

while

`lambda_2 e_2(lambda_without_2)=lambda_1 lambda_2 S+lambda_2 T_2`.

Hence

`1-p_2^(3)
 = (lambda_1 T_2+T_3)/e_3(lambda)`

`<=T_2/(lambda_2 S)+T_3/(lambda_1 lambda_2 S)`

`<=S/(2lambda_2)+S^2/(6lambda_1lambda_2)`

`<s0+(2/3)s0^2`.                                                   (2.3)

Thus

`alpha_j^(3)
 >=p_2^(3)[u_1(j)^2+u_2(j)^2]`

`>L0(1-s0-(2/3)s0^2)`

`=96633261942995107/100200654220492800`

`>24/25`.                                                         (2.4)

The column statements are identical for `H^T`, using `R_r>L0`. QED.

### Interpretation

This is not a small numerical miss. The current fractional-`e_2` route needs a common interpolation exponent `theta>2/3` in order for the resulting characteristic function to lie in `L^(3/2)`. But the source geometry forces `theta<25/48` at the heavy anchor. The two requirements are separated by a fixed gap:

`25/48 =0.520833... < 2/3`.

Therefore no constant optimization inside that common-scale volume interpolation can close this survivor. A successful compiler must treat the exact/heavy anchor and the diffuse residual channel anisotropically.

## 3. Explicit target-valid family: ridge-or-volume is not exhaustive

The preceding theorem concerns a source-generated survivor. The next construction isolates the obstruction in a transparent target-valid family and shows it is structural rather than an artifact of the constants.

For `0<epsilon<=1/200`, define

`H_epsilon=diag(1,1,epsilon)`

and the real symmetric `7 x 7` matrix

`A_epsilon = [1] direct_sum [[0,H_epsilon],[H_epsilon,0]].`       (3.1)

With independent cap-one coordinates write the corresponding form as

`Q_epsilon=X_0^2+2U_1V_1+2U_2V_2+2epsilon U_3V_3`.              (3.2)

The spectrum is

`{1,+1,-1,+1,-1,+epsilon,-epsilon}`,

so every `A_epsilon` is a valid instance of the original target.

At the B08 normalization `gamma=1`, `g=1/16`, the singular values of the cross block are `1,1,epsilon`; the top physical row and column leverages are one, the tail square is `epsilon^2<=1/40000<s0`, and for `epsilon=1/200` the ridge data at `g` are

`mu_1=mu_2=256/257=0.9961089494...`,

`mu_3=0.00635930047...`,

`tr K_g=1.99857719931...<2.01`.

So this family sits squarely in the same near-rank-two/heavy-anchor geometry.

### Proposition 3.1 — `QFORM-RIDGE-VOLUME-NONEXHAUSTIVE-v1`

For every `0<epsilon<=1/200`:

**(a) No one-scale ridge certificate works at any regularization scale.**  
For an arbitrary ridge scale `rho>0`,

`K_rho=diag(k,k,k_epsilon)`,

`k=1/(rho^2+1)`,

`0<k_epsilon=epsilon^2/(rho^2+epsilon^2)<=k`.

If a regularized-determinant criterion had `max diag K_rho<=q/2`, then `q>=2k`. But

`tr K_rho=2k+k_epsilon<=3k<4k<=2q`,

contradicting its necessary `tr K_rho>2q`. Thus the failure is scale-independent.

**(b) Rank-three volume sampling fails maximally.**  
There is exactly one nonzero `3 x 3` minor of `H_epsilon`; every row inclusion marginal equals one, so Theorem D's `alpha_i<=1/2` gate fails.

**(c) The fresh fractional rank-two canonical volume gate also fails for every admissible theta.**  
The three squared `2 x 2` minors have weights proportional to

`1, epsilon^2, epsilon^2`.

Hence

`alpha_1^(2)=alpha_2^(2)=(1+epsilon^2)/(1+2epsilon^2)`.

For `epsilon<=1/200` this is at least `40001/40002=0.9999750012...>3/4`. Therefore every `theta>2/3` has

`theta alpha_1^(2)>1/2`,

so `QFORM-FRACTIONAL-E2-BL-L3-v1` is unavailable.

Thus the proposed exhaustive alternative

`one-scale ridge OR canonical e_3 volume sampling OR canonical fractional e_2 volume sampling`

is false even inside the exact owner target.

This is **not** a counterexample to QFORM. Section 5 gives a uniform bound for the same family.

## 4. What the fresh fleet03/B08 theorem changes

The immediately newer fleet03/B08 r23 result is important context: it does not rely on the failed raw ridge-or-volume alternative above. It first physicalizes a complete row of the Schur-minor channel. If the leading physical-left singular vector is localized, it pays the whole nonzero tail. If not, it obtains a DIFFERENT ridge certificate for the Schur-minor matrix itself, with physical-left ridge leverage below `0.092` and effective ridge dimension above `0.969`, while keeping one exact weighted bilinear channel separately.

Therefore the current first analytic gap is not "find a better common-scale volume exponent." It is the r23 compiler

`QFORM-WEIGHTED-EXACT1-PLUS-RIDGE1-L3-v1`:

combine one exact heavy bilinear channel with one diffuse ridge channel before conditioning destroys the right-bank product provenance. Theorem 2.1 explains quantitatively why simply folding those two channels back into the present canonical `e_2/e_3` volume-sampling scheme cannot be expected to work: the heavy anchor consumes essentially all of the canonical volume marginal.

A plausible next mechanism is an **anisotropic** Brascamp--Lieb/differencing inequality in which the exact anchor is paid by a hub/physical-coordinate integration and the diffuse Schur-minor rows use finite-`p` Hausdorff--Young weights. A common `theta` tied to the canonical volume marginals is structurally too rigid here.

## 5. The designated partner theorem controls the explicit family anyway

Set `epsilon=0` in (3.2). The cross block

`H_0=diag(1,1,0)`

has exact rank two. With physical anchors `j=r=1`,

`Delta_11(H_0)=1`.

The outer physical coordinate `X_0` is a genuine square with coefficient `a=1`. Applying the completed `fleet02/B08` grouped theorem from Section 1.1 gives the actual inequality

`boxed( ||p_(Q_0)||_infinity <= C_grp =7.250055108887958... . )`     (5.1)

Now restore `epsilon>0`. The tail variable

`T_epsilon=2epsilon U_3V_3`

uses coordinates disjoint from every variable in `Q_0`; hence `T_epsilon` is genuinely independent of `Q_0`. Therefore

`Law(Q_epsilon)=Law(Q_0)*Law(T_epsilon)`

and convolution with a probability measure cannot increase an `L^infinity` density norm. Consequently

`boxed( ||p_(Q_epsilon)||_infinity <=7.250055108887958... )`          (5.2)

for every `epsilon`, with no moment or support hypothesis.

This is the designated partner result applied to an actual target inequality during this run. It also provides a clean control: the raw ridge and volume gates can all fail while QFORM remains uniformly easy for a product-structural reason invisible to those certificates.

Continuity is **not claimed** from (5.1)-(5.2), because the partner route is `L^3` plus a dependence-safe square and supplies essential boundedness rather than a continuous representative.

## 6. Conditional end-to-end map after this run

The source-valid map is now:

1. keep the exact original-coordinate scalar/Schur reductions and the completed localized/diffuse branches;
2. use the fresh fractional-`e_2` theorem where its canonical marginal gate is genuinely satisfied;
3. do **not** declare ridge-or-volume exhaustive: Theorem 2.1 and Proposition 3.1 prove it is not;
4. in the live heavy-anchor bicolop state, consume fleet03/B08 r23: localized physical rows are paid with the entire tail retained; the remaining Schur-minor channel is extremely ridge-diffuse;
5. the first unpaid diffuse implication is the anisotropic `QFORM-WEIGHTED-EXACT1-PLUS-RIDGE1-L3-v1` compiler, which must retain the right preconditioner/product provenance. The common-volume interpolation cannot handle the heavy exact anchor because its required exponent inequalities are mutually incompatible.

A future proof should therefore spend the exact channel separately rather than force both channels through one canonical volume distribution. This is a genuine narrowing of the proof design, not a claim that the full conjecture is solved.

## 7. Honest status

- Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- New structural theorem `QFORM-BICOLOOP-VOLUME-MARGINAL-HEAVY-v1`: **PROVED**.
- Proposed exhaustive ridge-or-volume certificate alternative: **REFUTED** by the target-valid family (3.1).
- Fresh source-matching fractional-`e_2` theorem: **CONSUMED, NOT DUPLICATED**.
- Designated `fleet02/B08` result: **CONSUMED AND APPLIED** to (5.1)-(5.2).
- New density conclusion in the explicit family: **essentially bounded**, constant `<7.251`; continuity **not claimed**.
- Repository transport was used; no authenticated native brain receiver/ingestion was observed, so execution remains `WITHOUT_VERIFIED_BRAIN`.
