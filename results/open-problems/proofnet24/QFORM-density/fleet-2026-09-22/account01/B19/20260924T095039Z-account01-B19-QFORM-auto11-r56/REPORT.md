SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B19, 2026-09-24T09:50:39Z.
attacking: the pair-free moderate-residual endpoint by retesting the actual light-bank self stars against the robust physical rank-two crossing at a much finer fixed E3 scale, then feeding the resulting repurified residual into the completed spectral-partition/E3 receiver; apply account02/B19's general-rank latent theorem at the exact purified endpoint.

# account01/B19 r56 — direct transverse repurification and sub-target residual tail

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING PAYMENT / MODERATE-RESIDUAL TAIL LOWERED BELOW TARGET SCALE ON THE ANCHORED BRANCH / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Authenticated repository transport is not native learned-memory receiver ingestion.

Regularity: both new payment branches below use the completed marginal-free physical-E3 theorem and therefore give continuous `C_0` densities on their exact scopes. The final retained-tail branch is structural only. Full-target continuity remains OPEN.

All coordinate sets below are literal ORIGINAL-coordinate sets. No random coordinate is rotated. Orthogonal singular-vector operations occur only in deterministic coefficient-space matrix inequalities. No Gaussian, log-concave, moment, compact-support, connected-support, iid, arbitrary-joint coarea, conditional-density-cap, worst-fibre, coefficient-continuity, post-rotation-independence, or law-uniform pointwise oscillatory-decay assumption is used. No nonzero coefficient tail is discarded.

## 1. Fresh source-pinned frontier

Fresh owner control on `math-research-brain/main` remained OWNER CONTROL revision `2026-09-22.15`, QFORM-only, with the unrestricted theorem OPEN.

The current pair-free moderate-residual endpoint is the account02/B20 r50/r51 normal form

`A_light = diag(q) + W H_L W^T + (E_R direct_sum E_C) + T_cross`,

with the genuine cross tail retained, `||T_cross||op<2^-16`, row-small residuals, and (after the latest r50 sharpening) only the coarse survivor information

`s_5(E_R), s_5(E_C) < 43/20`,

hence a rank-12 representation with retained operator tail `<2.1500152587890625`. The r51 strong-indefinite-pair branch is already terminal; the live synthesis debt is the quantitative pair-free moderate residual.

The earlier structural source actually used below is account03/B19 r49,

`yspennstate/math-open-problems@b3922fe080467f7f34a7dd248460fa2478bc03d2`,

which starts from disjoint physical banks `R,C` and

`N=A[R,C]`,

with top-two truncation

`N_2=U Sigma V^T`,

and

`||N-N_2||_F < tau`, `tau=2^-16`,

`sigma_2(N)>=1/64`.

On its anchored/no-large-light-star branch, if

`L={j in C: ell_j:=||V_{j,*}||^2<=1/2}`, 

then at most three coordinates lie outside `L`, every `j in L` obeys

`||A[j,C\{j}]||_2 <= R_0:=1/64`,

and there are anchors `a,b in L` with

`|det(v_a,v_b)|>=kappa_0:=1/64`.

The same source's common-plane rigidity lemma converts uniform row-deleted plane errors `<=epsilon` into

`A[C,C]=diag(q_C)+K_C+E_C`,

where `rank K_C<=8` (the extra rank is supported on at most three heavy physical coordinates) and

`max_j ||E_C e_j||_2 <= epsilon(1+5/kappa_0)`.

The transposed statement applies to `R`.

The analytic terminal below is the completed marginal-free physical-E3 theorem, source-pinned in

`yspennstate/math-open-problems@d0bda9f4e884eff19e5e7b0cf4cacab34d416c28`:

for every literal disjoint physical cross block `K`,

`Z_3=e_3(KK^T)>0`

implies a continuous `C_0` density for the FULL ambient law and

`||p_Q||infinity <= C_E3 Z_3^(-1/6)`,

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`.

Arbitrary same-bank curvature, outside couplings, affine terms, signs, degeneracies and extra spectrum remain in the law.

The designated partner result consumed at equation level in Section 5 is account02/B19 r14,

`yspennstate/math-open-problems@02a537de4788fa8821d7986ef53fc5ad0a311003`,

`QFORM-BL-RANKR-LATENT-PSEUDODET-ENDPOINT-v1`.

For an exact original-coordinate source block

`D+W H W^T`,

with `D` physical diagonal, `W^T W=I`, every physical row leverage `<=1/2`, and `rank H=k>=3`, it gives the FULL ambient law a continuous `C_0` density and

`||p_Q||infinity <= [4k/(k-2)] |pdet(H)|^(-1/k)`.

This theorem is valid for every signature and every exact rank drop down to rank three; it does not permit deletion of a small nonzero latent mode or a nonseparable coefficient tail.

## 2. Direct physical E3 retest at an arbitrarily finer fixed scale

The r49 residual bound `eta_0=0.0854...` came from first transporting an adaptive row plane with an error `2^-12` and only then applying common-plane rigidity. The key observation is that after the robust physical rank-two crossing is known, one can retest the ACTUAL self star directly by a literal E3 block at a much smaller fixed scale.

Fix `j in L`. Put

`M_j=N^T[C\{j},R]`,

`d_j=A[C\{j},j]`.

These are actual original-coordinate coefficients. Let `P_j` be the top-two left singular projection of `M_j`.

The deleted rank-two approximant is

`(N_2^T)[C\{j},R]=V^{(j)} Sigma U^T`,

where `V^{(j)}` is `V` with row `j` deleted. Since

`(V^{(j)})^T V^{(j)}=I-v_jv_j^T >=(1-ell_j)I >=(1/2)I`, 

its second singular value is at least

`b_0:=1/(64 sqrt(2))`.

The actual deletion differs by operator norm at most `tau`, so

`boxed: sigma_2(M_j) >= beta:=b_0-tau`

with

`beta=0.011033284666977304...`.

Let

`h_j=||(I-P_j)d_j||_2`.

### Theorem 2.1 — `QFORM-R49-DIRECT-TRANSVERSE-REPURIFICATION-v1`

Take the fixed scale

`delta_*:=2^-24`.

If for some light `j`,

`h_j>=delta_*`,

then the full ambient law has a continuous `C_0` density and

`boxed: ||p_Q||infinity <54496.`

If no such `j` exists, every light self star is within

`epsilon_*:=delta_*+theta_* R_0`

of the single fixed deleted plane `range(V^{(j)})`, where

`theta_*:=tau/(b_0-tau)=0.0013829779184588303...`.

Numerically,

`epsilon_*=2.1668634620694615e-5`.

Consequently the r49 common-plane rigidity theorem can be rerun with the SAME physical anchors and yields a new exact decomposition

`A[C,C]=diag(q_C')+K_C'+E_C'`,

`rank K_C'<=8`,

with

`boxed: max_j ||E_C'e_j||_2 <= eta_*:=321 epsilon_*`

`eta_*=0.006955631713242971... .`

The same dichotomy holds on the transposed `R` bank.

### Proof

Consider the literal physical cross block

`K_j=A[C\{j}, R union {j}]=[M_j,d_j]`.

The exterior-volume extension identity gives

`e_3(K_jK_j^T)
 >=sigma_1(M_j)^2 sigma_2(M_j)^2 h_j^2
 >=beta^4 h_j^2`.

Thus `h_j>=delta_*` gives

`e_3(K_jK_j^T)>=beta^4 delta_*^2`.

The marginal-free E3 theorem yields

`||p_Q||infinity
 <=C_E3 beta^(-2/3) delta_*^(-1/3)
 =54495.774088... <54496`.

This is a full-law statement: nothing else in `A` is deleted.

Assume now `h_j<delta_*` for every light `j`. Let

`S_j=range(V^{(j)})`.

The same exact subspace-transport proof used in r49 gives

`||P_{S_j^perp}P_j||op <=theta_*`.

Indeed the rank-two approximant has second singular value at least `b_0`, the perturbation has norm `<tau`, and the actual second singular value is at least `b_0-tau`.

Taking `w=P_jd_j`,

`||d_j-w||<delta_*`,

and the no-large-light-star gate gives `||w||<=||d_j||<=R_0`. Hence

`dist(d_j,S_j)
 <=||d_j-w||+dist(w,S_j)
 <delta_*+theta_*R_0
 =epsilon_*`.

Restricting this estimate to `L\{j}` only makes the Euclidean error smaller. The r49 common-plane rigidity lemma therefore applies with the already-existing physical anchors `a,b`, `kappa_0=1/64`, giving

`max_j||E_C'e_j||
 <=epsilon_*(1+5/kappa_0)
 =321epsilon_*
 =eta_*`.

The rank count is unchanged: the common-plane piece has rank at most two and the terms touching the at-most-three heavy physical coordinates have rank at most six. QED.

### Structural significance

The direct physical retest lowers the row-small residual constant from

`0.0854140220...`

to

`0.0069556317...`,

more than a factor twelve, without perturbatively deleting a single random quadratic coefficient. The lower floor is caused by the genuine `2^-16` crossing tail through the deterministic plane-transport term `theta_*R_0`; it is not treated as a small random error.

## 3. The improved row bound lowers the residual spectral threshold below one

Work on one repurified light residual `E=E'`. It is symmetric and

`max_j||Ee_j||<=eta_*`.

Set the spectral cutoff

`t_*=3/64`.

Let

`P=1_{|E|>=t_*}`.

Functional calculus gives the exact leverage estimate

`P_jj <=eta_*^2/t_*^2`.

Apply the same completed two-part MSS frame partition used in account02/B20 r50 to an orthonormal frame for `range(P)`. There is a literal partition

`L=I disjoint_union J`

such that both partial Gram matrices are bounded below by

`Delta_* I`,

where

`Delta_*:=1-(1/sqrt(2)+eta_*/t_*)^2`

`=0.26813071563975677...`.

### Theorem 3.1 — `QFORM-R49-REPURIFIED-S5-THREE-SIXTEENTHS-PAYMENT-v1`

If

`boxed: s_5(E)>=3/16,`

then the ACTUAL ambient physical cross block between the MSS parts satisfies

`boxed: s_3(A[I,J])>=m_*>0,`

where

`m_*:=Delta_*(3/16)-3/64`

`=0.003399509182454394...`.

Consequently the FULL ambient law has a continuous `C_0` density and

`boxed: ||p_Q||infinity <3104.`

### Proof

Write

`E_H=P E P`, `F=E-E_H`.

Then `||F||op<t_*`. On the high spectral subspace, thin QR on the two MSS restrictions gives

`s_5(E_H[I,J])>=Delta_* s_5(E_H)>=Delta_*(3/16)`.

Restriction does not increase operator norm, hence Weyl gives

`s_5(E[I,J])
 >=Delta_*(3/16)-t_*
 =m_*`.

Across the same literal within-bank cut, the coordinate diagonal contributes zero. The repurified common-plane piece has rank at most two, and all heavy-coordinate-supported terms vanish because `I,J` lie in the light bank. Therefore

`A[I,J]=E[I,J]+K[I,J]`, `rank K[I,J]<=2`.

The singular-value rank-shift inequality gives

`s_3(A[I,J])>=s_5(E[I,J])>=m_*`.

Hence

`e_3(A[I,J]A[I,J]^T)>=m_*^6`,

and the marginal-free E3 theorem gives

`||p_Q||infinity<=C_E3/m_*
 =3103.438839... <3104`.

All remaining coefficients stay in the ambient law. QED.

### Corollary 3.2 — sub-target retained tail

Every anchored/no-star state surviving Theorems 2.1 and 3.1 on both banks may be written, after the already-valid physical heavy-coordinate conditioning and r51 normalization, as

`A_light=diag(q)+K_12+F`,

with

`rank K_12<=12`,

and

`boxed: ||F||op<3/16+2^-16`

`=0.1875152587890625.`

On the existing four-latent determinant-collapse subbranch, the rank can be lowered to at most eleven and the retained tail obeys

`boxed: ||F_collapse||op<3/16+2^-16+112*2^-20`

`=0.1876220703125.`

This is a qualitative change from the previous `2.150...` tail ceiling: on this anchored branch the retained nonseparable operator tail is now strictly below one fifth and, in particular, far below the target spectral scale one. It is STILL RETAINED and is not treated as a negligible random perturbation.

## 4. Why the improvement is not a coefficient-continuity argument

The new conclusion is deterministic and branchwise:

- if a self star leaves the physical crossing plane at the fixed scale `2^-24`, a literal physical E3 block pays the full law;
- otherwise the ACTUAL self block is algebraically re-fit into the same physical two-plane plus a much smaller row residual;
- if that residual has five modes at scale `3/16`, another literal physical E3 cut pays the full law;
- otherwise the residual is decomposed exactly into its top-four finite-rank part plus the retained low operator tail.

At no point is `X^T F X` discarded because `||F||op` is small. This is crucial for arbitrary cap-one laws with unbounded support.

## 5. Designated account02/B19 theorem applied at the exact repurified endpoint

The common-plane correction from Theorem 2.1 is absorbed into the existing two-bank latent coefficient matrix. On the exact algebraic endpoint where the repurified residuals and the genuine crossing tail vanish, the active original-coordinate block is exactly

`A_light=diag(q)+W H_new W^T`,

where `W` is the r51 normalized four-column physical frame, `W^TW=I_4`, and every physical row leverage is at most one half.

This is an ACTUAL equation, not a rotated random-coordinate model. Apply the completed account02/B19 r14 theorem to `H_new`. If

`rank(H_new)=k>=3`,

then

`boxed: ||p_Q||infinity
 <=[4k/(k-2)] |pdet(H_new)|^(-1/k).`

For `k=4` this is

`||p_Q||infinity<=8|det(H_new)|^(-1/4)`,

while exact rank three gives

`||p_Q||infinity<=12|pdet(H_new)|^(-1/3)`.

Both branches have continuous `C_0` densities. All signs, repeated eigenvalues and exact rank drops are allowed. The theorem deliberately does NOT erase a small nonzero fourth latent coefficient; the pseudodeterminant is taken only after an exact rank drop.

Thus the exact endpoint remains completely paid after the new common-plane correction changes the latent self matrices. The only obstruction is genuinely the retained nonseparable tail, not the sign or degeneracy of the updated latent matrix.

## 6. Compact conditional proof assembly after the new inequality

A compact source-pinned route now reads as follows.

1. Same-constant principal-minimal descent and the completed diagonal, physical-pair, pair-log, physical-E3, D5, ridge/window, grouped-star, hub+square, null-coloop and fractional rank-two receivers pay their exact branches.
2. The r47-r52 robust-crossing compiler produces either already-paid physical exits or the BL-compatible rank-two light planes with the genuine cross tail retained.
3. Account02/B20 r51 closes every quantitative strong-indefinite-pair leaf. Hence a live moderate-residual survivor can be assumed pair-free at the recorded universal gate.
4. On the anchored/no-large-light-star common-plane branch, Theorem 2.1 above either pays by a literal E3 cut or repurifies the row-small residual from `0.0854...` to `0.006956...`.
5. Theorem 3.1 then pays every repurified residual with `s_5>=3/16`; otherwise the rank-12/rank-11 compiler has an exactly retained nonseparable tail `<0.187623` instead of `>2.15`.
6. If that tail vanishes exactly, the updated latent source is terminal by the designated account02/B19 r14 pseudodeterminant theorem.
7. What remains is to spend the NONZERO sub-target tail jointly with the latent/diagonal carrier, or to route it source-preservingly to an already-completed physical receiver. No continuity conclusion is claimed for that survivor.

The first sharpened local debt on this route is therefore

`QFORM-ANCHOR-REPURIFIED-R12/R11-SUBTARGET-TAIL-JOINT-ENDPOINT-v1`:

> In the pair-free anchored common-plane chamber, start from
>
> `A_light=diag(q)+K_12+F`, `rank K_12<=12`, `||F||op<0.187515259`,
>
> or the rank-11 determinant-collapse version with `||F||op<0.187622071`; retain every coefficient and arbitrary cap-one product law. Prove a universal density bound by spending the sub-target tail jointly with the finite latent/diagonal carrier, or force a completed physical E3/D5, ridge/window, hub+square, grouped-star, incident-volume, finite-core or pair receiver.

Parallel global branches remain: the no-fixed-Pluecker-anchor aggregate geometry, finite star/hub localizations, and other previously tracked near-rank-one/pair-free chambers. Therefore the unrestricted theorem is not claimed.

## 7. Correction audit

Preserved throughout:

- no arbitrary-joint rank-three coarea;
- no pointwise `|t|^-1/2` decay for arbitrary cap-one one-dimensional densities;
- no independence after spectral or singular-vector rotation;
- no worst conditional-fibre density cap;
- no generic fractional-small-ball-to-`L^infinity` interpolation;
- no reciprocal selection of one tiny physical minor;
- no deletion of a nonzero coefficient tail by coefficient continuity;
- no claim that a diffuse rank-two packet alone supplies the third target resource.

All new payments are literal original-coordinate full-law E3 applications, and the designated partner theorem is used only on an exact product-preserving latent source block.

Full QFORM: OPEN / NOT PROVED / NOT DISPROVED. Full continuity: OPEN.
