SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T05:22:28Z.
attacking: the distributed-star/two-child survivor by forcing a literal third-compound crossing whenever the physical star has transverse mass to a diffuse child two-frame, and using the designated deletion-child theorem when the child third spectrum is too large for that crossing perturbation.

# account03/B08 r51 — transverse distributed star + two-child compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING ANALYTIC ROUTER / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN, and full-target continuity remains OPEN. The paid branches proved here are continuous `C_0` branches. No moment, compact-support, connected-support, Gaussian, log-concavity, iid, post-rotation independence, arbitrary-joint coarea, conditional-density-cap, fiber-supremum, or law-uniform pointwise quadratic-phase-decay assumption is used.

## 1. Fresh source boundary and immediate predecessor


The immediate new predecessor is account01/B08 r43:

`yspennstate/math-open-problems@5eceb142f1c4ebaa8c6096d0333a9c1995f39c69`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260924T051232Z-account01-B08-qform-r43/REPORT.md`.

It consumes every fixed-scale physical diagonal or edge and reduces the genuinely diffuse r50 source branch to a physical deletion

`A = [[a,b^T],[b,C]]`,                                           (1.1)

with

`||b||_2 > rho_* L`, `rho_*=0.0006247538095703261`,             (1.2)

all individual surviving physical edges much smaller than that row norm, and

`s_2(C) >= m_0 L`, `m_0=sqrt(47/48)=0.9895285072531598...`.     (1.3)

In particular the remaining star is genuinely distributed. The r43 report records the two-bank partition of its squared edge mass. This run attacks the next issue: how to combine that distributed star with the two robust child spectral directions while retaining arbitrary child curvature.

The full-crossing receiver used below is the reviewed `QFORM-THIRDCOMPOUND-CROSS-PROMOTION-v1`, source-pinned in account03/B08 r50. For every ORIGINAL-coordinate crossing matrix `B_cross`,

`||p_Q||_infinity <= 6^(4/3) e_3(B_cross B_cross^T)^(-1/6)`,      (1.4)

with `p_Q in C_0(R)`, and with arbitrary same-bank quadratic/measurable phases retained.

The designated account04/B08 input is

`QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`,

`yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`.

If an ORIGINAL-coordinate deletion child has three eigenvalues of modulus at least `m` and its projection onto `|lambda|>=m/64` has every physical leverage at most `1/32`, then the full parent form has

`||p_Q||_infinity < 64/m`, `p_Q in C_0(R)`.                     (1.5)

## 2. A two-frame cut which also preserves an arbitrary orthogonal vector

The first new point is that the star-residual direction need NOT itself be diffuse.

### Lemma 2.1 — `QFORM-TWOFRAME-ORTHOGONAL-RESIDUAL-HALFCUT-v1`

Let `V in R^(N x 2)` have orthonormal columns and physical rows `v_i^T`, with

`max_i ||v_i||_2^2 <= 1/16`.                                    (2.1)

Let `u in R^N` be any unit vector satisfying `V^T u=0`; no coordinatewise bound on `u` is assumed. Then there is an ORIGINAL-coordinate partition `S disjoint T={1,...,N}` and a choice of orientation of the two sides such that

`V_S^T V_S >= (1/4) I_2`, `V_T^T V_T >= (1/4) I_2`,            (2.2)

and

`dist(u_T, range(V_T))^2 >= 3/8`.                               (2.3)

#### Proof

Choose independent Bernoulli `xi_i in {0,1}` with probability `1/2`, and put

`G=sum_i xi_i v_i v_i^T`,
`c=sum_i xi_i u_i v_i`.                                          (2.4)

Because `sum_i v_i v_i^T=I_2` and `sum_i u_i v_i=V^T u=0`,

`E G=I_2/2`, `E c=0`.                                            (2.5)

Independence and centering give

`E ||G-I_2/2||_F^2
 = (1/4) sum_i ||v_i||^4
 <= (1/32)`,                                                     (2.6)

while

`E ||c||_2^2
 = (1/4) sum_i u_i^2 ||v_i||^2
 <= 1/64`.                                                       (2.7)

Hence

`E[ ||G-I_2/2||_F^2 + 2||c||^2 ] <= 1/16`,                     (2.8)

so one physical cut has the bracket at most `1/16`. For this cut,

`||G-I_2/2||op <=1/4`, `||c||^2<=1/32`.                         (2.9)

The complementary side has Gram `I_2-G` and mixed vector `-c`, hence the same two bounds. Orient the cut so that `||u_T||^2>=1/2`. Then both restricted Grams are at least `I_2/4`, proving (2.2). Moreover, with `P_T` the projection onto `range(V_T)`,

`||(I-P_T)u_T||^2
 = ||u_T||^2-c^T G^(-1)c
 >= 1/2-(1/32)/(1/4)
 =3/8`.                                                          (2.10)

This is (2.3). QED.

The useful feature is that only the CHILD two-frame is assumed diffuse. A star residual concentrated on one or a few physical coordinates does not break the half-cut: the orientation step puts at least half of its mass on `T`, while orthogonality makes the mixed covariance small in expectation.

## 3. Transverse-star crossing theorem with arbitrary child tail

Return to (1.1). Let `V` be an orthonormal eigenframe for the two largest absolute eigenvalues of `C`, and write

`C=V Lambda V^T+E`,                                              (3.1)

where

`m:=s_2(C)=min(|lambda_1|,|lambda_2|)`,
`||E||op=s_3(C)`.                                                (3.2)

Decompose the physical star into its child-spectral and transverse parts:

`b=Vc+w`, `c=V^T b`, `w=(I-VV^T)b`, `beta=||w||_2`.             (3.3)

Fix `0<zeta<=1` and suppose

`max_i ||V_{i,*}||^2 <=1/16`,                                   (3.4)

`beta >= zeta ||b||_2`.                                         (3.5)

Set

`tau_0=sqrt(3/8)`,
`q_0=zeta tau_0/2`,
`theta(zeta)=q_0/[4(1+q_0)]`.                                   (3.6)

### Theorem 3.1 — `QFORM-DISTRIBUTED-STAR-TRANSVERSE-TWOCHILD-v1`

Under (3.1)-(3.6), one of the following holds.

**Crossing branch.** If

`s_3(C) <= theta(zeta) m`,                                      (3.7)

then the full form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 6^(4/3)
    [ beta m^2 tau_0 / (32(1+q_0)^2) ]^(-1/3).
`                                                                    (3.8)

**Large-third-child branch.** If (3.7) fails and the child spectral projection

`P=1_{|C|>=theta(zeta)m/64}`                                    (3.9)

has `max_i P_ii<=1/32`, then the designated account04/B08 theorem gives

`boxed:
 ||p_Q||_infinity
 < 64/[theta(zeta)m],
 p_Q in C_0(R).
}`                                                                    (3.10)

If (3.7) fails and the window (3.9) is not diffuse, there is an ACTUAL child coordinate `j` with

`boxed:
 max{|C_jj|,||C[j,-j]||_2}
 > theta(zeta)m/512.
}`                                                                    (3.11)

Thus arbitrary higher child curvature is not discarded: small `s_3(C)` is absorbed deterministically into the literal crossing; large `s_3(C)` is handed to the completed physical-deletion theorem at its actual scale.

#### Proof of the crossing branch

Apply Lemma 2.1 to `V` and `u=w/beta`. Let `S,T` be the resulting physical child partition. The ORIGINAL-coordinate crossing of the parent between `{hub} union S` and `T` is

`B_cross = [ b_T^T ; C[S,T] ]`.                                 (3.12)

Put `G_S=V_S^T V_S`. Since `G_S>=I/4`, the 2-by-|S| map

`R_S=(1/2) G_S^(-1) V_S^T`                                     (3.13)

has operator norm at most one and satisfies `R_S V_S=I_2/2`. Apply the row contraction `diag(1,R_S)` to (3.12). The resulting 3-by-|T| matrix is

`M=[b_T^T; L]`,
`L=L_0+F`,
`L_0=(1/2) Lambda V_T^T`,
`F=R_S E[S,T]`.                                                  (3.14)

By Lemma 2.1,

`s_2(L_0)>=m/4=:sigma`, `||F||op<=s_3(C)=:r`.                   (3.15)

The ideal lower-row space is exactly `range(V_T)^T`, hence

`dist(b_T,row(L_0))
 = beta dist(u_T,range(V_T))
 >= beta tau_0`.                                                 (3.16)

For `r<sigma`, a direct principal-angle estimate gives

`||P_row(L)-P_row(L_0)||op <= r/(sigma-r)`.                      (3.17)

For completeness: every unit `y` in `row(L)` can be represented as `y=z^T L` with `||z||<=1/s_2(L)<=1/(sigma-r)`, so its component perpendicular to `row(L_0)` is at most `r/(sigma-r)`; the two row spaces have equal dimension two, so this is the largest principal sine and equals the projector distance.

Under (3.7), using `sigma=m/4` and the definition (3.6),

`r/(sigma-r) <= q_0`.                                           (3.18)

Therefore, by (3.5),

`dist(b_T,row(L))
 >= beta tau_0-q_0||b||
 >= beta tau_0/2`.                                               (3.19)

Also

`s_2(L)>=sigma-r>=m/[4(1+q_0)]`,                                (3.20)

and the same lower bound holds for `s_1(L)`. The product of the three singular values of the 3-row matrix `M` is its lower-row area times the perpendicular distance of the first row. Hence

`s_1(M)s_2(M)s_3(M)
 >= [beta tau_0/2] [m/(4(1+q_0))]^2
 = beta m^2 tau_0/[32(1+q_0)^2].`                               (3.21)

Because `diag(1,R_S)` is a contraction, exterior-power monotonicity gives

`e_3(B_cross B_cross^T)^(1/2)
 >= s_1(M)s_2(M)s_3(M)`.                                        (3.22)

Insert (3.21) into the reviewed third-compound crossing theorem (1.4). Since `e_3^(-1/6)=[e_3^(1/2)]^(-1/3)`, (3.8) follows, including the `C_0` conclusion. No same-bank coefficient is removed. QED.

#### Proof of the large-third-child branch

If (3.7) fails, the literal deletion child `C` has three eigenvalues of modulus at least `theta(zeta)m`. Apply account04/B08 (1.5) at that actual scale. This is exactly (3.10) when (3.9) is diffuse. If a physical child coordinate has window leverage `>1/32`, spectral energy gives

`||Ce_j|| > [theta(zeta)m/64]/sqrt(32)`.                         (3.23)

Splitting this norm into diagonal and off-diagonal parts gives (3.11). QED.

## 4. Actual constants on the live distributed-star survivor

Apply Theorem 3.1 to the account01/B08 r43 state (1.2)-(1.3). Take

`zeta=1/4`.                                                       (4.1)

Then

`tau_0=sqrt(3/8)=0.6123724356957945...`,
`q_0=sqrt(3/8)/8=0.07654655446197431...`,
`theta=0.017775950827372714...`.                                 (4.2)

If, in addition to the r43 survivor,

`max_i ||V_{i,*}||^2<=1/16`,                                    (4.3)

and

`dist(b,range(V))>=||b||/4`,                                    (4.4)

then `beta>=rho_*L/4` and `m>=m_0L`. The low-`s_3(C)` crossing branch gives

`boxed: ||p_Q||_infinity <800.633/L, p_Q in C_0.`               (4.5)

If instead `s_3(C)>theta m`, applying the designated account04/B08 theorem to the ACTUAL deletion child at scale `theta m` gives

`boxed: ||p_Q||_infinity <3638.471/L, p_Q in C_0`               (4.6)

provided its `theta m/64` window is diffuse. If that window localizes, (3.11) yields an ORIGINAL child row witness

`boxed:
 max{|C_jj|,||C[j,-j]||_2}
 >3.435509782659315e-5 L.
}`                                                                    (4.7)

Thus the entire transverse/diffuse-two-child chamber of the new distributed-star survivor is now either paid or converted into another explicit physical localized row.

There are only two structural ways Theorem 3.1 can fail before that partner router:

1. **child two-frame localization:** `max_i ||V_i||^2>1/16`; then spectral energy already gives some child coordinate

`||Ce_i||>m/4`, hence
`max{|C_ii|,||C[i,-i]||}>m/(4sqrt2)>0.1749 L`;                  (4.8)

2. **star/child alignment:** `beta<||b||/4`, equivalently

`||P_V b|| > (sqrt(15)/4)||b|| =0.9682458...||b||`.             (4.9)

The latter is now the genuinely low-dimensional aligned carrier; it is much sharper than an unspecified failure of a transverse argument.

## 5. Why this does not invoke a forbidden shortcut

The proof never asks for pointwise van-der-Corput decay of a one-dimensional bounded density. It never treats a bounded projection density as sufficient for an indefinite quadratic pushforward. It does not rotate the independent coordinates. The only rotation is the deterministic spectral description `C=V Lambda V^T`, used to define coefficient-space quantities; all conditioning/crossing sets are subsets of ORIGINAL physical coordinates. The arbitrary tail `E` is either retained in the literal crossing and controlled in operator norm at coefficient level, or it is large enough that the designated deletion-child theorem is invoked. No random-tail smallness is asserted.

A tempting stronger statement — that the two-frame `V` alone forces a third crossing direction from any nonzero star residual without comparing `beta` to `||b||` — is not proved here. A tiny perturbation of the lower-row space can absorb a residual whose ratio `beta/||b||` is tiny. The ratio gate (3.5) is therefore explicit rather than silently suppressed.

## 6. Regression computation

The deterministic constants are

`rho_*=0.0006247538095703261`,
`m_0=sqrt(47/48)=0.9895285072531598`,
`theta(1/4)=0.017775950827372714`,
`c_volume=tau_0/[32(1+q_0)^2]=0.01651201311610402`,
`C_cross=800.6323698240689`,
`C_partner=3638.470209892449`,
`window scale/L=theta*m_0/64=0.0002748407826127452`,
`localized-row witness/L=theta*m_0/512=3.435509782659315e-5`.

A seeded numerical regression generated diffuse orthonormal child two-frames, orthogonal unit residuals with no residual-coordinate cap, exact top-two child spectra, and tails of operator norm `0.9 theta m`. Among 67 admissible tests, the smallest observed ratio

`(actual compressed three-singular-value product)/(analytic lower bound (3.21))`

was `8.906148086186887`; there were zero violations. This is regression evidence only; Sections 2-4 are analytic.

## 7. Remaining implication

The unrestricted theorem and global continuity remain OPEN. This run removes the transverse/diffuse-child-two-frame chamber of account01/B08 r43's distributed-star survivor.

The sharpened next B08 endpoint is

`QFORM-DISTRIBUTED-STAR-ALIGNED-TOP2-OR-SECOND-LOCALIZED-COMPILER-v1`:

starting from the same diffuse-top-three source branch and r43 global fixed-edge exclusions, consume either

- the quantitatively aligned state `dist(b,range(V_top2(C)))<||b||/4`, with arbitrary `s_3(C)` and all signs retained; or
- the new second localized/distributed child row returned by (4.7) or the much stronger child-two-frame localization (4.8).

The account02/B01 heavy-star edge/tail theorem and the account01/B08 all-scale physical-pair/fixed-edge compiler are natural complementary inputs, but an arbitrary cross-curvature between distributed leaf banks still prevents a naive factorization.

No full-solution claim is made, and the two independent end-to-end reviews required by owner control have not occurred for this r51 supporting theorem.