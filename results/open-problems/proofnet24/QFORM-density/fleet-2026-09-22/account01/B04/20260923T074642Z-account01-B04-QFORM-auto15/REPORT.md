SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T07:46:42Z.
attacking: single-heavy-row canonical E2 volume via an exact Bernoulli entropy tilt, then applying the partner rank-two half-Riesz compiler without selecting a local minor.

# account01/B04 — single-hub Bernoulli tilt for rank-two volume

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING THEOREM / PARTNER RESULT APPLIED / TARGET-VALID ROTATED FAMILY / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full conjecture remains open. The new square-peel branch below proves absolute continuity with an essentially bounded density in its stated scope; it does **not** prove continuity of the density.

## 1. Source-pinned completed input

The completed partner theorem actually used is account02/B04's
`QFORM-ENTROPY-WEIGHTED-RANK2-HALFRIESZ-v1`, read from

- repository `yspennstate/math-open-problems`,
- commit `04297a630381fcfcf429b4c5ec560886bebacb39`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260923T052139Z-account02-B04-qform-auto11/REPORT.md`.

Its exact scope is as follows. For disjoint ORIGINAL-coordinate banks `I,J`, after conditioning arbitrary other original coordinates write

`R=F(X_I)+2 X_I^T M X_J+G(X_J)`,

with arbitrary within-bank quadratic and affine terms. For any probability weight `w` on nonzero physical `2x2` minors, put

`G_2(w)=exp(E_w log det(M_ST)^2 + H(w))`.

If `1<=q<2` and every row inclusion marginal under `w` is at most `q/2`, then

`sup_s E|R-s|^(-1/2)
 <= C(q) G_2(w)^(-1/8)`,

where

`C(q)=4 sqrt(2e) q^(-1/4)/(2-q)`.

If one further untouched original coordinate `Z` appears as

`Q=a[Z+m]^2+R`, `a!=0`,

then

`||p_Q||_infinity <= |a|^(-1/2) C(q) G_2(w)^(-1/8)`.

No post-rotation independence is used in that theorem.

## 2. First essential missing implication attacked

The preceding B04 obstruction was a canonical two-volume law with one very heavy physical row. Keeping the canonical law forces `q` close to two, while selecting one small non-star minor pays a reciprocal local coefficient. The goal here is to repair a heavy canonical row **globally** by changing only its Bernoulli inclusion frequency and leaving all conditional minor proportions intact.

Let

`d_ST = det(M[S,T])^2`,
`Z_2 = sum_{|S|=|T|=2} d_ST = e_2(M^T M)>0`,

and let the canonical physical-minor law be

`pi(S,T)=d_ST/Z_2`.

Let `mu` be its row-pair marginal. Fix a physical row `h` and assume

`0<p:=P_mu(h in S)<1`.

For every `k!=h` define the two conditional inclusion frequencies

`u_k = P_mu(k in S | h in S)`,
`v_k = P_mu(k in S | h notin S)`.

Because `S` is a two-element set, the `u_k` sum to one, while the `v_k` sum to two.

## 3. New theorem: exact one-hub Bernoulli tilt

### Theorem `QFORM-SINGLE-HUB-BERNOULLI-TILT-v1`

For any `theta in (0,1)`, define a new row-pair law

`nu_theta = theta mu(. | h in S)
          +(1-theta) mu(. | h notin S)`.

Lift it to a law on full physical minors by retaining the canonical conditional column law:

`w_theta(S,T)=nu_theta(S) pi(T|S)`.

Its row marginals are exactly

`alpha_h(theta)=theta`,

and, for `k!=h`,

`alpha_k(theta)=theta u_k+(1-theta)v_k`.                  (3.1)

Set

`q_theta = max{1, 2 theta,
                  2 max_{k!=h}[theta u_k+(1-theta)v_k]}`.       (3.2)

Whenever `q_theta<2`, the partner theorem applies and gives

`boxed:
 sup_s E|R-s|^(-1/2)
 <= C(q_theta) Z_2^(-1/8)
    exp(D_Ber(theta||p)/8),`                                    (3.3)

where

`D_Ber(theta||p)
 = theta log(theta/p)
 +(1-theta) log((1-theta)/(1-p))`.

Consequently, for an untouched original-coordinate square

`Q=a[Z+m]^2+R`, `a!=0`,

`boxed:
 ||p_Q||_infinity
 <= |a|^(-1/2) C(q_theta) Z_2^(-1/8)
    exp(D_Ber(theta||p)/8).`                                    (3.4)

This allows arbitrary same-bank curvature and arbitrary conditioned affine terms inside the partner theorem's scope.

### Proof

The row marginal formula (3.1) is immediate from the definition of `nu_theta`.

Because `w_theta` preserves the canonical conditional distribution of `T` given `S`, the chain rule for relative entropy gives

`D_KL(w_theta || pi)=D_KL(nu_theta || mu)`.                      (3.5)

On the event `{h in S}`, the Radon--Nikodym ratio is exactly `theta/p`; on its complement it is `(1-theta)/(1-p)`. Therefore

`D_KL(w_theta || pi)=D_Ber(theta||p)`.                          (3.6)

For the canonical determinant law `pi=d/Z_2`, the entropy-adjusted volume satisfies the exact Gibbs identity

`log G_2(w)=log Z_2-D_KL(w||pi)`.                               (3.7)

Hence

`G_2(w_theta)=Z_2 exp[-D_Ber(theta||p)].`                       (3.8)

By (3.1)--(3.2), every row inclusion marginal is at most `q_theta/2`. If `q_theta<2`, the account02/B04 half-Riesz theorem gives

`sup_s E|R-s|^(-1/2)
 <= C(q_theta) G_2(w_theta)^(-1/8)`,

which becomes (3.3) after (3.8). The dependence-safe scalar-square peel in the same partner theorem gives (3.4). QED.

## 4. Symmetric half-tilt and an exact endpoint classification

The particularly useful choice is `theta=1/2`. Put

`eta_h=max_{k!=h}(u_k+v_k)`,
`q_h=max{1,eta_h}`.                                             (4.1)

Then

`alpha_h=1/2`,
`alpha_k=(u_k+v_k)/2`,

and

`D_Ber(1/2||p)
 =-(1/2) log[4p(1-p)]`.                                        (4.2)

Thus

`boxed:
 G_2(w_{1/2})=2 Z_2 sqrt[p(1-p)].`                              (4.3)

Whenever `q_h<2`,

`boxed:
 sup_s E|R-s|^(-1/2)
 <= [4 sqrt(2e) q_h^(-1/4)/(2-q_h)]
    [2 Z_2 sqrt(p(1-p))]^(-1/8).`                               (4.4)

The same right side times `|a|^(-1/2)` bounds an outer-square form.

There is also a precise support endpoint. Since `0<=u_k,v_k<=1`, one has `q_h=2` if and only if some `k!=h` satisfies

`u_k=v_k=1`.                                                    (4.5)

But (4.5) is equivalent to row `k` belonging to every row pair in the support of `mu`, i.e. to `k` being a second strict row coloop. Hence:

> **A single canonical heavy row is not by itself an endpoint obstruction.** After the half-tilt, the only support-level failure `q_h=2` is the presence of a second strict row coloop. Quantitative near-failure is measured explicitly by `2-q_h`.

A cleaner constant occurs under the balanced-neighborhood condition

`u_k+v_k<=1` for all `k!=h`.                                    (4.6)

Then `q_h=1`, so

`boxed:
 sup_s E|R-s|^(-1/2)
 <=4 sqrt(2e)[2 Z_2 sqrt(p(1-p))]^(-1/8),`                      (4.7)

and

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2e)|a|^(-1/2)
   [2 Z_2 sqrt(p(1-p))]^(-1/8).`                                (4.8)

This is the new practical heavy-row smoother.

## 5. What failure of the balanced condition actually says

For a row `k!=h`, write

`m_hk=mu({h,k})`,
`alpha_k=mu(k in S)`.

Then

`u_k=m_hk/p`,
`v_k=(alpha_k-m_hk)/(1-p)`.                                    (5.1)

Thus the failure `u_k+v_k>1` is exactly

`boxed:
 p alpha_k-(2p-1)m_hk > p(1-p).`                                (5.2)

For `p>1/2` this is a concrete two-center overlap certificate. I do **not** infer from it a large individual minor, a good local Schur packet, or a full-target bound. It is only the exact obstruction produced by this tilt.

## 6. Genuinely rotated indefinite target-valid family

Let `L>0`, `c=cos(pi/12)`, `s=sin(pi/12)`, and let `M_L` be the `5x2` physical cross block whose rows are

`r0 = L(c,s)`,
`r1 = (1/2, sqrt(3)/2)`,
`r2 = (-sqrt(3)/2, 1/2)`,
`r3 = (-1/2, -sqrt(3)/2)`,
`r4 = (sqrt(3)/2, -1/2)`.                                      (6.1)

This is obtained by applying one deterministic `15 degree` coefficient rotation to the rows

`L e1`, and the four unit directions at `45,135,225,315` degrees.

The rotation is part of the deterministic matrix; **no random coordinate is rotated**. Every one of the ten physical entries of `M_L` is nonzero.

Right orthogonal rotation preserves absolute `2x2` minors. The four hub--leaf squared minors are each

`L^2/2`,                                                       (6.2)

while among leaf--leaf pairs the four cycle edges have squared minor `1` and the two opposite pairs have minor zero. Therefore

`Z_2=4(L^2/2)+4=2L^2+4=2(L^2+2)`.                              (6.3)

For the hub `h=0`,

`p=L^2/(L^2+2)`.                                                (6.4)

Conditional on using the hub, the four leaves are uniform, so

`u_k=1/4`.                                                      (6.5)

Conditional on avoiding the hub, the canonical law is uniform on the four-cycle edges, so every leaf is incident to two of the four edges and

`v_k=1/2`.                                                      (6.6)

Hence

`u_k+v_k=3/4<1` for every leaf.                                 (6.7)

The half-tilt therefore has `q=1`. In fact it is simply uniform on the eight nonzero row-pair classes: each receives weight `1/8`. Its entropy-adjusted volume is exactly

`G_2=2 Z_2 sqrt[p(1-p)]
    =4 sqrt(2) L`.                                              (6.8)

Now take arbitrary independent cap-one variables

`Z, X_0,...,X_4, Y_1,Y_2`

and define

`Q_L=Z^2+2 X^T M_L Y`.                                          (6.9)

The symmetric matrix is

`A_L=[1] direct_sum [[0,M_L],[M_L^T,0]]`.

Before the coefficient rotation,

`M_L^T M_L=diag(L^2+2,2)`,                                     (6.10)

so the exact nonzero spectrum of `A_L` is

`{1, +sqrt(L^2+2), -sqrt(L^2+2), +sqrt(2), -sqrt(2)}`.         (6.11)

Thus `Q_L` satisfies the owner's full spectral hypothesis for every `L>0`: it has five eigenvalues of modulus at least one. It is indefinite and physically rotated/dense across the two coefficient columns.

Applying (4.8) with `a=1` gives, for **every** admissible product input law,

`boxed:
 ||p_(Q_L)||_infinity
 <=4 sqrt(2e) (4 sqrt(2)L)^(-1/8).`                             (6.12)

At `L=3`,

`p=9/11`, `Z_2=22`, `G_2=12sqrt(2)`,

and

`boxed:
 ||p_(Q_3)||_infinity <= 6.546515487110656.`                     (6.13)

The unmodified canonical law on the **same matrix** has first admissible exponent

`q_can=2p=18/11`

and gives

`15.409272446385636`.                                           (6.14)

Thus the new one-hub tilt improves this actual partner-theorem certificate by a factor `2.3538...` at `L=3`.

More importantly, as `L->infinity`, the canonical hub marginal tends to one, while the tilted law remains at `q=1` and (6.12) behaves like `O(L^(-1/8))`. Hence a canonical near-coloop caused by one very energetic row need not be a genuine Fourier endpoint obstruction when the off-star geometry redistributes over sufficiently many leaves.

The newest account02/B04 projected-rowstar theorem does not subsume this example: the coefficient space here is already two-dimensional, so a rank-two coefficient projection is the identity, while deleting the hub leaves four leaf rows spanning rank two rather than rank at most one. The present entropy tilt therefore pays a distinct non-star configuration.

## 7. Exact scope and continuity

The new theorem uses only:

1. the canonical physical `2x2` determinant law in original coordinates;
2. relative entropy / conditional probability identities;
3. account02/B04's completed arbitrary-weight rank-two half-Riesz theorem;
4. one untouched original-coordinate scalar square for the `L^infinity` splice.

It does **not** use pointwise van-der-Corput decay, post-rotation independence, arbitrary-joint coarea, positive moments of conditional projection caps, fiber suprema, a uniformly good local minor, or a local cross-rank-three deduction.

The partner theorem's square splice yields an essentially bounded density / absolute continuity. Continuity of this new branch is **not** claimed.

## 8. First remaining implication

The narrowed next debt is

`QFORM-HUB-BERNOULLI-TILT-OR-TWOCENTER-ROUTING-v1`:

> Starting from a full-target structural survivor with large canonical `E_2` but a heavy physical row, either show that some heavy row admits a tilt with `q_theta<=2-c` and `Z_2 exp[-D_Ber(theta||p)]` at target scale, or use the exact near-endpoint condition `u_k≈v_k≈1` to force a genuine two-center grouped/hub packet that can be paid without a reciprocal tiny local coefficient. The zero/near-zero outer-square branch remains separate debt.

This is stronger and more precise than treating every canonical near-coloop as a generic entropy failure.

## 9. Integrity / review status

- Full QFORM: **OPEN**.
- New theorem: supporting theorem, proof supplied here, independent review not yet recorded.
- Partner theorem: source-pinned completed worker result, applied directly to (3.8) and to the explicit family (6.12).
- Target-valid finite family check: exact algebra, not Monte Carlo.
- No public release, email, scheduler mutation, paid model/API call, remote workflow, permission change, or installation work.
- Changed-file privacy review: this report contains only mathematics, public/private repository coordinates already authorized by the owner, and nonsecret control identifiers. No credentials, signed URLs, client/company/trading data, personal archives, or unrelated private material are present. Repository-side secret scanners were not exposed to this worker; this is a narrowly scoped manual fallback review.
