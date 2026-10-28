SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-24T06:52:38Z.
attacking: the r51 BL-compatible robust-rank-two survivor; deepen the physical leverage peel to the 1/16 gate, then force either a partner-compatible target-scale hub star or a balanced 2x2 grid of four literal rank-two crossings.

# account03/B20 r49 — deep leverage peel to a balanced physical rank-two grid or a beta-scale hub

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW TARGET-RELEVANT STRUCTURAL COMPILER / PARTNER RESULT APPLIED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository access/writeback is not native learned-memory receiver ingestion.

Regularity: this report proves deterministic coefficient structure and a fractional small-ball consequence. It does **not** prove a new endpoint `L^infinity` density theorem on its surviving grid branch. Full-target continuity remains **OPEN**.

All sets below are literal ORIGINAL-coordinate sets. No random variable is rotated. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, arbitrary-joint coarea, fiber-supremum, or law-uniform pointwise oscillatory-decay hypothesis is added. The nonzero coefficient tail is retained throughout.

## 1. Source-pinned frontier


Immediate same-account frontier:

`yspennstate/math-open-problems@bcb36a7573a7e9f23f1ea78792e0b72bc8bb0d9c`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T060028Z-account03-B19-QFORM-r51/REPORT.md`.

It supplies disjoint physical banks `R,C`, their actual crossing

`N=A[R,C]`,

and the top-two SVD truncation

`N_2=U Sigma V^T`,

with

`||N-N_2||_F < tau`, `tau=2^-16`,                                (1.1)

`sigma_2(N)>=s0`, `s0=1/64`.                                     (1.2)

The r51 peel used the threshold `2/7` and obtained normalized light-plane leverage at most `1/2`. The first endpoint debt there is to make the product-coordinate geometry sufficiently diffuse to use the fleet's strongest physical balanced-cut and BL/Fresnel tools while retaining the genuine nonzero tail.

Two completed supporting results are used at their proved scopes.

1. account03/B08, `QFORM-TWOFRAME-BERNOULLI-BALANCE-v1`, canonical source
   `yspennstate/math-open-problems@19c12072f7e67266ce894042034bcabb9c376bea`,
   proves that an orthonormal two-frame `W` with maximum row leverage `mu` has a literal physical bipartition with both restricted Gram matrices at least

   `1/2-sqrt(mu/2)` times the identity.                           (1.3)

2. account04/B20 r13, canonical source
   `yspennstate/math-open-problems@d2560a041fd91c05d7fddf50f5b5414ecd2680a2`,
   proves the localized child-window pivot/star and exact double-anchor refinement. Its anchor-star threshold is

   `beta0=sqrt(3)/(128 sqrt(96))=1/(512 sqrt(2))`
   `=0.0013810679320049757...`.                                  (1.4)

The completed account02/B19 full-ambient rank-two fractional theorem is also used only for the optional quantitative corollary in Section 6.

## 2. Deep physical leverage peel

Set

`eta=2/63`, `g=32/63`.                                            (2.1)

For the left singular frame `U`, define

`H_R={i in R: ||U_{i,*}||_2^2>eta}`, `L_R=R\H_R`,                 (2.2)

and analogously

`H_C={j in C: ||V_{j,*}||_2^2>eta}`, `L_C=C\H_C`.                 (2.3)

Because each two-frame has total leverage two,

`|H_R|,|H_C|<=62`.                                                (2.4)

Indeed 63 rows each strictly larger than `2/63` would have total leverage strictly larger than two.

Put

`G_R=U[L_R]^T U[L_R]`, `G_C=V[L_C]^T V[L_C]`.                    (2.5)

The constants in (2.1) are chosen so that two useful identities hold simultaneously:

`eta/g=1/16`,                                                     (2.6)

and

`(1-g)/62=(31/63)/62=1/126`.                                     (2.7)

The second identity is the reason the failure branch lands just above the account04/B20 anchor threshold after the retained tail is paid *aggregately* rather than once per selected row.

## 3. Main theorem

### Theorem 3.1 — `QFORM-DEEPPEEL-R2-GRID-OR-BETASTAR-v1`

Under (1.1)-(1.2), at least one of the following alternatives holds.

### A. beta-scale literal physical hub star

There is an original coordinate `i in R` or `j in C` such that respectively

`||A[i,C]||_2 > beta_*`,

or

`||A[R,j]||_2 > beta_*`,                                         (3.1)

where

`beta_* := (s0 sqrt(31/63)-tau)/sqrt(62)`
`        = 1/(64 sqrt(126))-1/(65536 sqrt(62))`
`        = 0.001390047766811737...`.                              (3.2)

In particular

`boxed: beta_*>beta0=1/(512 sqrt(2))`                             (3.3)

with margin

`beta_*-beta0=8.97983480676e-6`.                                 (3.4)

### B. 1/16-diffuse light planes and a balanced 2x2 rank-two grid

Both light Grams obey

`G_R>=g I_2`, `G_C>=g I_2`.                                      (3.5)

Define normalized restricted frames

`U~=U[L_R] G_R^(-1/2)`, `V~=V[L_C] G_C^(-1/2)`.                  (3.6)

Then

`U~^T U~=V~^T V~=I_2`,                                           (3.7)

and every physical row has leverage at most

`boxed: max_i ||U~_{i,*}||^2 <=1/16, max_j ||V~_{j,*}||^2<=1/16.` (3.8)

The actual light-light crossing first satisfies

`boxed: sigma_2(N[L_R,L_C]) > g s0-tau`
` =1/126-2^-16`
` =0.007921249147445436... .                                     (3.9)

Moreover there are literal original-coordinate partitions

`L_R=R_1 disjoint_union R_2`,
`L_C=C_1 disjoint_union C_2`                                     (3.10)

such that **all four** actual physical crossing cells obey

`boxed: sigma_2(A[R_a,C_b]) > s_grid` for every a,b in {1,2},    (3.11)

where

`h:=1/2-1/(4 sqrt(2))=0.32322330470336313...`,                   (3.12)

`s_grid:=h g s0-tau`
`       =h/126-2^-16`
`       =0.002550005533980064... .`                              (3.13)

Thus an unpaid robust-rank-two survivor cannot remain merely a single diffuse two-plane crossing: after this compiler it either exposes a finite physical hub whose star already clears the account04/B20 anchor scale, or it contains four simultaneous target-independent rank-two crossings between four disjoint original-coordinate subbanks.

### Proof

Suppose first that `lambda_min(G_R)<g`. Since `U^T U=I_2`,

`U[H_R]^T U[H_R]=I_2-G_R`,                                      (3.14)

so its largest eigenvalue is `>1-g=31/63`, hence

`tr(U[H_R]^T U[H_R])>31/63`.                                    (3.15)

Using `Sigma^2>=s0^2 I_2` and `V^T V=I_2`,

`||N_2[H_R,C]||_F^2`
` =tr(Sigma^2 U[H_R]^T U[H_R])`
` >s0^2 (31/63).`                                                 (3.16)

Here is the quantitative improvement over the earlier rowwise star extraction: restore the **whole heavy block first**. By the reverse triangle inequality in Frobenius norm and (1.1),

`||N[H_R,C]||_F`
` >s0 sqrt(31/63)-tau.`                                          (3.17)

There are at most 62 rows in `H_R`, so one actual physical row satisfies

`||N[i,C]||_2`
` >(s0 sqrt(31/63)-tau)/sqrt(62)=beta_*.`                         (3.18)

Because `N=A[R,C]`, this is exactly the first alternative in (3.1). The column-side proof is identical. Direct arithmetic gives (3.3)-(3.4).

It remains to consider the case (3.5). For a light row `u_i`,

`||U~_{i,*}||^2=u_i^T G_R^(-1)u_i`
` <=||u_i||^2/g`
` <=eta/g=1/16`,                                                  (3.19)

and similarly on the right, proving (3.8).

Write

`B=G_R^(1/2) Sigma G_C^(1/2)`.                                   (3.20)

Then the rank-two light restriction is

`N_2[L_R,L_C]=U~ B V~^T`,                                       (3.21)

and

`sigma_2(B)>=sqrt(g) s0 sqrt(g)=g s0`.                           (3.22)

Restriction does not increase the Frobenius or operator norm of the retained tail `F=N-N_2`, so Weyl proves (3.9).

Now apply the completed physical two-frame balance lemma (1.3) separately to `U~` and `V~`, using the actual row-leverage bound `mu<=1/16`. This yields the literal physical partitions (3.10) and

`U~[R_a]^T U~[R_a]>=h I_2`,
`V~[C_b]^T V~[C_b]>=h I_2`                                      (3.23)

for all `a,b`. Consequently the rank-two approximant in every cell,

`U~[R_a] B V~[C_b]^T`,                                           (3.24)

has smaller nonzero singular value at least

`sqrt(h) sigma_2(B) sqrt(h)>=h g s0`.                            (3.25)

Restoring the actual tail in that same physical cell costs at most `tau` in operator norm. Weyl gives (3.11)-(3.13) simultaneously for all four cells. QED.

## 4. Why the aggregate-tail step matters

If one first chose a heavy approximant row and then restored the tail rowwise, the lower bound would lose the full `tau=2^-16`, giving only

`1/(64 sqrt(126))-2^-16=0.001376726845898...`,                   (4.1)

which falls *below* the account04/B20 anchor scale `beta0`.

Equation (3.17) restores the tail before pigeonholing the at-most-62 physical rows and therefore loses only `tau/sqrt(62)` after the final averaging. This raises the actual guaranteed star to `beta_*=0.0013900477668...`, strictly above `beta0`. The order of the inequalities is essential.

## 5. Designated account04/B20 result applied at the actual new inequality

The completed designated partner source is account04/B20 r13:

`yspennstate/math-open-problems@d2560a041fd91c05d7fddf50f5b5414ecd2680a2`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260924T051424Z-account04-B20-QFORM-r13/REPORT.md`.

Its exact localized child-window/double-anchor compiler assumes an original anchor star `b` with

`||b||_2>beta0=1/(512 sqrt(2))`.                                 (5.1)

The new star branch verifies this premise quantitatively by (3.3): take the row hub `i` from (3.18); its full physical star in the ambient matrix has norm at least `||A[i,C]||>beta_*>beta0` (and likewise after transposition for a column hub).

Therefore, **inside the partner's localized child-window leaf**, if its child window fails and the scalar-pivot alternative does not already pay, the partner supplies a second child star `v` with

`||v||>a0`, `a0=4.2146684313588616e-8`,                          (5.2)

and its exact double-anchor refinement applies with this actual new hub. At `epsilon=1/64` the resulting exhaustive alternatives are:

1. a literal strong anchor edge

   `boxed: |b_j|>=beta0/sqrt(2)=1/1024;`                         (5.3)

2. a literal transverse double-anchor crossing

   `boxed: s_2(A[K,{i,j}]) >= a0/(64 sqrt(2))`
   ` =4.6565947316667495e-10;`                                  (5.4)

3. the explicit alignment collar

   `boxed: dist(v,span u)<||v||/64.`                             (5.5)

This is an equation-level application of the designated partner theorem at the newly proved inequality `beta_*>beta0`; it is not a claim that every beta-star state automatically lies in the partner's child-window scope. The scalar-pivot branch remains paid exactly as in the source theorem.

## 6. Product-safe fractional consequence on the grid branch

For any one of the four literal cells `M=A[R_a,C_b]`, (3.11) gives

`Z_2(M)=e_2(M^T M)>=sigma_2(M)^4>s_grid^4`.                      (6.1)

The completed full-ambient account02/B19 theorem
`QFORM-PHYSICAL-R2-FRACTIONAL-SMOOTHING-v1` therefore gives, without deleting any same-bank term or the nonzero tail,

`H_(1/4)(Q):=sup_s E|Q-s|^(-1/4)`
` <3.929131770449763 s_grid^(-1/4)`
` <17.484826.`                                                    (6.2)

Hence every interval `I` of length `delta` satisfies

`P(Q in I)<14.702928 delta^(1/4).`                               (6.3)

This is deliberately recorded as fractional smoothing, not promoted by interpolation to an endpoint density bound.

## 7. What changed and what remains

The first structural mismatch in the r51 endpoint route is now removed:

- the robust branch no longer stops at physical plane leverage `<=1/2`; it reaches the much stronger `<=1/16` interface and a literal balanced `2 x 2` grid of four simultaneous rank-two crossings, with every cell satisfying `sigma_2>0.0025500`;
- failure no longer gives merely an arbitrary finite star: the aggregate-tail argument gives a star strictly above the exact account04/B20 anchor threshold, so the partner double-anchor trichotomy is immediately available whenever its localized child-window leaf is encountered.

The first remaining endpoint implication on this route is now

`QFORM-FOURCELL-R2-GRID-PLUS-DIFFUSE-THIRD-SOURCE-ENDPOINT-v1`:

> spend the four product-provenance rank-two cells together with the r49 diffuse third/high-spectrum residual, or show that failure to align that third resource with the two latent planes produces physical `E_3` and returns to the completed continuous third-compound receiver. The genuine `2^-16` coefficient tail and arbitrary same-bank quadratic curvature must remain in the law.

Parallel global debts (giant near-rank-one, small-Pluecker aggregation, and extra-spectrum/low-rank-carrier glue) remain open. No easy subclass is substituted for the full theorem.

Full QFORM target: **OPEN / NOT PROVED / NOT DISPROVED**.

Full universal continuity target: **OPEN**.
