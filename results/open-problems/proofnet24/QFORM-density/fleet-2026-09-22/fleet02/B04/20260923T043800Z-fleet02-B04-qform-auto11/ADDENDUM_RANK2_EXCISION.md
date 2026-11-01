# B04 addendum — balanced weak direction forces physical rank-two excision before weak-scale payment

Programme `QFORM-DENSITY-3EIG-20260922`; run `20260923T043800Z-fleet02-B04-qform-auto11`. Status: **ESSENTIAL STEP / PROOF-MECHANISM OBSTRUCTION / EXPLICIT TARGET-VALID UNIFORM EXIT; FULL QFORM OPEN**.

This addendum preserves the immutable primary `REPORT.md` and adds a sharper same-matrix separation using the fresh designated-partner result fleet03/B04 r24. It proves that even when third-volume marginals are perfectly admissible and the direct ridge leverage gate is satisfied at every scale, both the optimized third-volume certificate and the unreduced one-scale ridge certificate may be forced to pay an arbitrarily weak third cross direction, while conditioning one ORIGINAL physical coordinate exposes a uniform rank-two product-Fourier exit.

## 1. Sources used at equations

1. Claude/e5 Theorem D: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. For a physical cross block with `Z=e_3(M^T M)` and determinant-squared row marginals at most `1/2`,

`||p_Q||_inf <= 6 sqrt(e) Z^(-1/6)`.

Its arbitrary-weight variant replaces `Z` by `G(w)=exp(E_w log det^2+H(w))`.

2. Fresh designated partner fleet03/B04 r24: `yspennstate/math-open-problems@a11e719b61c4be07fae4e2dcfa4d88d31812d0d9`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260923T034739Z-r24/REPORT.md`. It independently checked the completed ridge theorem: with

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`, `theta=tr K_gamma`,

if `max diag K_gamma<=1/2` and `theta>2`, then

`||p_Q||_inf <= sqrt(e)/(sqrt(2) gamma) * theta/(theta-2)`.          (1.1)

All self blocks and outside couplings remain unrestricted. Its spectral-window theorem also records that failure of diffuse high-spectrum leverage forces a genuine physical pivot/star.

3. Rank-two product-Fourier exit: `yspennstate/math-open-problems@36263ba314738468f934a5b3245130b6754e940f`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B09/B09-20260922T184627Z-r15/REPORT.md`, theorem `QFORM-ONE-SIDED-SEPARABLE-CROSS-DIFFUSE-v1`. For rank two with singular-value product `D_2`, left-frame leverage at most `1/2`, coordinate-separable left-bank phase/curvature and arbitrary right-bank term,

`||p_Q||_inf <= 2 sqrt(2e) D_2^(-1/2)`.                            (1.2)

No pointwise scalar decay, post-rotation independence, arbitrary-joint coarea, moment, support or log-concavity hypothesis is used below.

## 2. Target-valid balanced weak-direction family

Fix `m>=4` and `0<eps<=1/4`. On a left bank of `N=2m+2` original coordinates let `u1,u2,u3` be orthonormal with disjoint supports:

`u1=m^(-1/2) 1` on rows `1,...,m`,

`u2=m^(-1/2) 1` on rows `m+1,...,2m`,

`u3=(e_(2m+1)+e_(2m+2))/sqrt(2)`.

Put `U=[u1 u2 u3]`. On a three-coordinate right bank take the orthogonal all-nonzero Householder matrix

`V=I-(2/3)11^T`

` = [[ 1/3,-2/3,-2/3],[-2/3,1/3,-2/3],[-2/3,-2/3,1/3]]`.

Define

`M_eps=U diag(2,2,eps) V^T`.                                      (2.1)

Its singular values are exactly `2,2,eps`, and every physical cross entry is nonzero. Embed it in

`A_eps,m = [[(1/2)I_N, M_eps],[M_eps^T,(1/2)I_3]].`                 (2.2)

Because the diagonal blocks are scalar, each cross singular mode `s` contributes `1/2+s` and `1/2-s`. Hence

`spec(A_eps,m)={5/2,5/2,-3/2,-3/2,1/2+eps,1/2-eps, (1/2)^(2m-1)}`. (2.3)

Thus the matrix is full rank, indefinite, genuinely rotated in physical coordinates, and has four eigenvalues of modulus at least one for every allowed `eps`.

## 3. All admissible third-volume weights still pay `eps`

The right bank has exactly three columns. A nonzero `3x3` minor must choose one left row from each support of `u1,u2,u3`. For every such row triple `S`,

`det(U_S)^2=1/(2m^2)`, `det(diag(2,2,eps))^2=16eps^2`, `det(V)^2=1`,

so

`det(M_eps[S,:])^2=8eps^2/m^2`.                                   (3.1)

There are `2m^2` nonzero minors, whence

`Z=e_3(M_eps^T M_eps)=16eps^2`.                                    (3.2)

The determinant-squared volume law is uniform. Its physical row marginals are `1/m` on every strong-support row and exactly `1/2` on each weak-support row, so the e5 `q=1` gate is satisfied.

Moreover, all nonzero determinant squares in (3.1) are equal. Thus for every probability weight `w` on nonzero minors,

`G(w)=Z exp(-KL(w||w_vol)) <= Z`,                                  (3.3)

with equality at the already-admissible uniform volume law. Therefore the e5 arbitrary-weight mechanism is globally optimized by the raw volume law; no entropy/KL repair can remove the weak scale.

Applying the completed e5 theorem to the actual quadratic form (2.2) gives

`||p_(X^T A_eps,m X)||_inf`
` <= 6 sqrt(e)(16eps^2)^(-1/6)`
` = 6 sqrt(e) 2^(-2/3) eps^(-1/3)`
` = 6.231775903093545... eps^(-1/3).`                              (3.4)

## 4. Fresh partner r24 applied: direct unreduced ridge costs at least `eps^(-1)`

On the same physical cross block,

`K_gamma=U diag(k,k,h)U^T`,

`k=4/(4+gamma^2)`, `h=eps^2/(eps^2+gamma^2)`.                      (4.1)

Hence

`max diag K_gamma=max{k/m,h/2}<=1/2`                               (4.2)

for every `gamma>0`; physical ridge leverage is not the obstruction. The effective dimension is

`theta=2k+h`.                                                       (4.3)

Whenever `theta>2`, the partner r24 inequality (1.1) produces the certificate

`R_eps(gamma)=sqrt(e)/(sqrt(2)gamma) * theta/(theta-2)`.             (4.4)

Because `2k<=2`,

`theta-2=h-2(1-k)<=h`.                                              (4.5)

Thus every valid `gamma` obeys

`theta/(theta-2)>=2/h>=2gamma^2/eps^2`,

and therefore

`R_eps(gamma)>=sqrt(2e) gamma/eps^2`.                              (4.6)

Also `theta/(theta-2)>1`, so

`R_eps(gamma)>sqrt(e)/(sqrt(2)gamma)`.                              (4.7)

Minimizing the maximum of (4.6) and (4.7) over `gamma` yields the mechanism lower bound

`boxed: R_eps(gamma)>=sqrt(e) eps^(-1)`                             (4.8)

for every valid direct one-scale ridge choice. This is a lower bound on the **numerical certificate supplied by (1.1)**, not on the true output density.

The order is sharp within this simplified partner certificate. For `gamma=eps/sqrt(2)`,

`k=8/(8+eps^2)`, `h=2/3`,

`theta-2=4(4-eps^2)/[3(8+eps^2)]>0`,

and exactly

`R_eps(eps/sqrt(2)) = [sqrt(e)/eps] (32+eps^2)/[2(4-eps^2)]`.       (4.9)

For `eps<=1/4`,

`R_eps(eps/sqrt(2)) <= (57/14)sqrt(e) eps^(-1)`
`                    = 6.712650887850521... eps^(-1)`.              (4.10)

More precisely, setting `gamma=c eps` shows

`inf_gamma R_eps(gamma)=[2sqrt(3e)+o(1)]eps^(-1)`                  (4.11)

as `eps->0`, with `2sqrt(3e)=5.711338016744285...`.

So on this family the optimized third-volume certificate is `Theta(eps^(-1/3))` while the direct partner-ridge certificate is `Theta(eps^(-1))` even though its leverage gate is perfect at every scale.

## 5. The partner spectral-window gate sees a genuine physical hub

For the full matrix (2.2), the `|lambda|>=1` spectral subspace consists of the two strong singular modes. On the left its projection diagonal is `1/m` on strong-support rows and zero on the weak pair. On the three-coordinate right bank it is the projection onto the first two columns of `V`, so

`diag(P_1|_right)=(5/9,5/9,8/9)`.                                  (5.1)

Thus the partner r24 diffuse spectral-window hypothesis fails strongly, with `mu=8/9`. Its heavy-row consequence is real: at the right coordinate with leverage `8/9`, the scalar diagonal is only `1/2`, while the cross-column norm is

`||M_eps e_j||=sqrt(32+eps^2)/3 > 4sqrt(2)/3`.                     (5.2)

This is exactly an aggregate physical hub, not a rotated-coordinate artifact.

## 6. Condition one ORIGINAL hub coordinate: rank-two exit is uniform

Keep right physical coordinates `1` and `3` and condition only on right coordinate `2`. Let

`C_eps=M_eps[:,{1,3}]`.                                             (6.1)

Because `U` is an isometry, the two nonzero singular values of `C_eps` are those of `diag(2,2,eps)V^T[:,{1,3}]`. Exact multiplication gives

`C_eps^T C_eps =`

`[[20/9+4eps^2/9, 8/9-2eps^2/9],`
` [8/9-2eps^2/9, 32/9+eps^2/9]]`,                                 (6.2)

hence

`det(C_eps^T C_eps)=4(16+5eps^2)/9`.                               (6.3)

Therefore the product of the two positive singular values is

`D_2=sqrt(det(C_eps^T C_eps))=(2/3)sqrt(16+5eps^2)>=8/3`.           (6.4)

The left singular subspace of `C_eps` is contained in `range(U)`. Consequently its coordinate projection is dominated by `UU^T`, whose diagonal is `1/m` on strong-support rows and `1/2` on the weak pair. Thus the rank-two left-frame leverage is at most `1/2`.

After conditioning the discarded **original** right coordinate, the left quadratic block is still `(1/2)I_N`; the induced left linear term is coordinate-separable. The retained two-coordinate right side may have arbitrary same-bank curvature. The completed rank-two product-Fourier theorem (1.2) therefore applies conditionally, uniformly in the conditioned coordinate, and averaging preserves the bound:

`||p_(X^T A_eps,m X)||_inf`
` <=2sqrt(2e) D_2^(-1/2)`
` <=2sqrt(2e)(8/3)^(-1/2)`
` =sqrt(3e)`
` =2.855669008372142... .`                                         (6.5)

The theorem also supplies a continuous density. Crucially, **no `eps` remains**.

## 7. Consequence for the proof map

On one explicit target-valid genuinely rotated indefinite full-rank family:

`best admissible weighted e5 three-volume <= 6.2318 eps^(-1/3)`,

`every direct partner-r24 ridge certificate >= 1.6487 eps^(-1)` (and its optimized asymptotic is `5.7114 eps^(-1)`),

while an original-coordinate physical rank-two excision gives

`||p||_inf <= sqrt(3e)<2.856` uniformly.

Thus the weak third cross singular direction is not intrinsically required for target-level smoothing. A structural proof that first pays either full third-volume or `theta>2` on the unreduced block can lose arbitrarily much even when all relevant marginal/leverage gates are already satisfied.

The next unpaid implication is therefore

`QFORM-NEAR-COLOOP-PHYSICAL-RANK2-EXCISION-v1`:

from only `s_3(A)>=1`, show that a low-total-tail/high-leverage survivor either allows conditioning a bounded number of ORIGINAL physical hub coordinates while retaining a target-scale rank-two cross packet in a completed separable/half-Riesz/grouped branch, or necessarily enters another completed ridge/grouped-coordinate branch. The difficult survivor is genuine nonseparable self-curvature on both sides together with loss of every quantitative rank-two physical reduction.

This is a counterexample to an **exhaustive proof mechanism**, not to QFORM. The displayed family itself has a universal density bound (6.5).
