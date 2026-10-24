SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T16:40:42Z.
attacking: the r33 global rank-one physical core — convert its remaining tail into aggregate literal E2 mass, or compile its dominant mode into an original-coordinate 12-star hub / 12-by-2 grid packet without deleting the nonzero tail.

# account03/B07 r34 — aggregate E2 or a many-bank physical rank-one packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260923T164042Z-account03-B07-qform-r34`  
Initial research-brain main: `9a205f80b614da5341fb2546fb7105a2d4a8f7e5`  
Owner continuation consumed: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Pre-publication owner revision: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW SUPPORTING COORDINATE-MINOR / MANY-BANK COMPILER; FULL QFORM OPEN; FULL CONTINUITY OPEN**.

The unrestricted conjecture is not proved or disproved here. No Gaussian, moment, compact-support, connected-support, log-concavity, diagonal-basis, or post-rotation independence assumption is used. Singular vectors below are used only as deterministic matrix geometry; they are never treated as independent random coordinates. Every bank selected below is a subset of the original independent coordinates. No individual tiny coordinate minor is inverted.

## 1. Fresh sources and exact incoming packet

The immediately preceding B07 result is

`yspennstate/math-open-problems@316522c99a92f168d0e0dcfe3be3aa032bdf53f9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T153842Z-account03-B07-qform-r33/REPORT.md`.

Its theorem `QFORM-BANKCYCLE-GLOBAL-LOWTAIL-v1` leaves, in the cancellation branch, one literal original-coordinate four-bank cross block `K` whose whole Frobenius mass is close to one rank-one matrix. The same strict-N3 state carries the concrete lower scale

`sigma_1(K) > 243.24294332152962 h`,                              (1.1)

where

`h=(2sqrt(2)-1)/1572864`.                                        (1.2)

The completed designated-partner result actually used quantitatively is account04/B07 r1,

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T091740Z-account04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

At its fixed `tau0=h^2/128`, it proves the actual physical coefficient cap

`|K_ij| <= h/8`                                                   (1.3)

for the relevant off-diagonal entries in this strict-N3 packet. Equation (1.3), together with (1.1), is applied below at concrete inequalities, not cited nominally.

A newer designated-partner report was also read before publication:

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

Its theorem `QFORM-DIAGONAL-RANK-TAIL-CORE-v1` is valid but requires `r+3` actual physical diagonals bounded below after a diagonal-plus-rank-r decomposition. The present strict-N3 packet has tiny physical diagonals instead, so that theorem is not silently substituted here.

The new interactive projected-crossing theorem was also read at

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its one-hub payment needs positive projected second-volume `Z_2` with all corresponding row marginals at most `1/2`. The rank-one endpoint isolated below can have `Z_2=0` exactly, so the theorem is not claimed to pay that endpoint.

## 2. First essential implication: E2 mass or a diffuse dominant physical mode

The following deterministic lemma is the main new result.

### Theorem 2.1 — `QFORM-ENTRYCAP-E2-OR-DIFFUSE-TOPMODE-v1`

Let `K` be any nonzero real matrix with singular values

`sigma=s_1 >= s_2 >= ...`,                                      (2.1)

and put

`T=sum_(j>=2) s_j^2`, `c=max_(i,j)|K_ij|`.                       (2.2)

For every `0<tau<1`, at least one of the following holds:

**(E2)**

`E_2(K) >= tau^2 sigma^4`,                                      (2.3)

where `E_2(K)` is the sum of squares of all literal physical `2x2` minors of `K`;

or **(D)** there are top unit left/right singular vectors `u,v` such that

`K=sigma u v^T+E`, `||E||_F<tau sigma`,                         (2.4)

and

`min{ ||u||_infinity^2, ||v||_infinity^2 }
 < tau + c/sigma`.                                               (2.5)

Thus failure of aggregate second-minor mass forces one side of the *dominant deterministic rank-one mode* to be diffuse in the original coordinate basis, while the nonzero matrix tail is retained exactly through the quantitative bound in (2.4).

#### Proof

The singular-value identity for the second compound is

`E_2(K)=sum_(p<q) s_p^2 s_q^2
       =sigma^2 T + sum_(2<=p<q) s_p^2 s_q^2`.                   (2.6)

It is also exactly the Cauchy--Binet identity

`E_2(K)=sum_(i<k,j<l)
          (K_ij K_kl-K_il K_kj)^2`,                              (2.7)

so (2.6) is aggregate weight over literal original-coordinate minors.

If `T>=tau^2 sigma^2`, (2.6) immediately gives (2.3). Assume otherwise. Eckart--Young/SVD gives (2.4), with `||E||_F=sqrt(T)<tau sigma`.

For every physical entry,

`sigma |u_i v_j|
 <= |K_ij|+|E_ij|
 <= c+||E||_F
 < c+tau sigma`.                                                 (2.8)

Taking maxima over `i,j`,

`||u||_infinity ||v||_infinity < tau+c/sigma`.                  (2.9)

Put `x=||u||_infinity^2`, `y=||v||_infinity^2`, and `z=tau+c/sigma`. Equation (2.9) says `sqrt(xy)<z`. If both `x>=z` and `y>=z`, then `sqrt(xy)>=z`, a contradiction. Hence `min(x,y)<z`, proving (2.5). QED.

No probability statement is made about `u^T X` or `v^T X`; (2.5) is only a deterministic coordinate-leverage certificate.

## 3. Applying the designated account04/B07 coefficient cap

Insert the actual packet (1.1)-(1.3) and take

`tau=1/64`.                                                       (3.1)

Then

`c/sigma < 1/[8(243.24294332152962)]
          =0.0005138895225205745`,                               (3.2)

and therefore

`zeta:=tau+c/sigma
 <0.016138889522520575 <1/32`.                                  (3.3)

Theorem 2.1 gives the concrete exhaustive alternative

### Aggregate physical-minor branch

`boxed: E_2(K) > 854675.100194511 h^4`.                          (3.4)

Because every physical entry has modulus at most `h/8`, each physical `2x2` determinant has modulus at most

`2(h/8)^2=h^2/32`.                                               (3.5)

Thus (3.4) forces at least

`boxed: 875187303`                                               (3.6)

nonzero literal physical `2x2` minors. This count is a deterministic diffusion certificate, not an analytic density bound.

### Diffuse dominant-mode branch

After possibly transposing `K`, there is a unit top left singular vector `u` satisfying

`boxed: max_i u_i^2 < zeta <0.016138890`,                        (3.7)

and

`boxed: K=sigma u v^T+E,  ||E||_F<sigma/64`.                    (3.8)

This is strictly sharper than retaining only r33's `2.262%` global rank-one tube: the intermediate tail `sigma/64 <= ||E||_F <0.02263 sigma` is now rerouted to the aggregate-E2 branch.

## 4. Twelve disjoint original-coordinate banks from the diffuse mode

### Lemma 4.1 — `QFORM-DIFFUSE-TOPMODE-12BANK-v1`

If `u` is a unit vector and `max_i u_i^2<=zeta` with the numerical `zeta` in (3.3), then there are twelve mutually disjoint coordinate banks `S_1,...,S_12` such that

`boxed: ||u_{S_r}||_2 >=1/4,  r=1,...,12`.                       (4.1)

#### Proof

Greedily accumulate coordinates until the squared mass of a bank first reaches `1/16`. Every completed bank then has squared mass less than `1/16+zeta`. After eleven completed banks, the consumed mass is less than

`11(1/16+zeta)=0.865027784747726 <15/16`.                        (4.2)

Therefore more than `1/16` remains and a twelfth bank can be completed. Taking square roots gives (4.1). QED.

From (3.8), for every one of these banks,

`||K[S_r,:]||_F
 >= sigma ||u_{S_r}||-||E[S_r,:]||_F
 > sigma/4-sigma/64
 =15 sigma/64`.                                                  (4.3)

At the partner scale (1.1),

`boxed: ||K[S_r,:]||_F >57.0100648409835 h`.                    (4.4)

Together with the physical coefficient cap `h/8`, each row-bank cross block in (4.4) contains at least `208010` nonzero physical entries. Again this is structural currency, not by itself a density receiver.

## 5. Exhaustive one-hub or 12-by-2 grid refinement

The opposite top singular vector `v` now has only two possibilities.

### Branch H: a physical hub

If some physical coordinate `j_*` satisfies

`|v_{j_*}|>=1/2`,                                                (5.1)

then every one of the twelve disjoint row banks satisfies

`||K[S_r,{j_*}]||_2
 >= sigma |v_{j_*}| ||u_{S_r}||-||E[S_r,{j_*}]||_2
 > sigma/8-sigma/64
 =7 sigma/64`.                                                   (5.2)

Hence one literal physical column hub sees twelve mutually disjoint original-coordinate star banks, each obeying

`boxed: ||K[S_r,{j_*}]||_2 >26.6046969257923 h`.                (5.3)

By the partner entry cap, each such star has at least `45300` nonzero physical coefficients.

### Branch G: a two-bank opposite side

If (5.1) fails, then every squared coordinate of `v` is below `1/4`. Greedily fill a column bank until its `v`-mass reaches `1/4`. Its overshoot is at most `1/4`, so at least `1/2` total mass remains and a second disjoint bank can also be filled. Therefore there exist disjoint original-coordinate banks `T_1,T_2` with

`||v_{T_s}||>=1/2`, `s=1,2`.                                    (5.4)

For every `r=1,...,12` and `s=1,2`,

`||K[S_r,T_s]||_F
 >= sigma ||u_{S_r}|| ||v_{T_s}||-||E[S_r,T_s]||_F
 > sigma/8-sigma/64
 =7 sigma/64`.                                                   (5.5)

Thus the low-tail branch contains a **12-by-2 grid of literal original-coordinate cross blocks** with

`boxed: ||K[S_r,T_s]||_F >26.6046969257923 h`                    (5.6)

for all 24 cells. Each cell contains at least `45300` nonzero physical coefficients under the partner cap.

Equations (5.2) and (5.5) retain the entire nonzero tail `E`; they do not replace `K` by its rank-one approximation.

Combining Sections 2--5 gives the new compiler

### Theorem 5.1 — `QFORM-BANKCYCLE-E2-OR-HUBGRID-v1`

For the actual r33 strict-N3 physical block `K`, one of the following must hold:

1. `E_2(K)>854675.100194511 h^4` as aggregate literal physical-minor currency;
2. one physical hub sees twelve disjoint original-coordinate stars, each of norm `>26.6046969257923 h`;
3. twelve row banks and two column banks form a 12-by-2 original-coordinate grid in which every cell has Frobenius norm `>26.6046969257923 h`.

No single coordinate minor is selected for reciprocal payment in any branch.

## 6. Interface with the newest projected-crossing theorem

The owner continuation supplied the completed grouped-projection theorem `GC`. It is important not to overstate what Theorem 5.1 buys.

In branch H, take the literal hub coordinate `j_*`. Its twelve stars give strong hub-row mass, but `GC` with one hub still needs a projected light crossing with positive second volume `Z_2` and row marginals at most `1/2`. The exact rank-one model `K=sigma u v^T` satisfies every inequality in branch H while its projected crossing after removing the hub-row direction is zero. Hence Theorem 5.1 does **not** by itself manufacture the missing `Z_2`; doing so would silently delete the genuine rank-one endpoint.

Likewise branch G supplies many large cells but they can all be almost parallel to the same `v` direction. Large Frobenius cell norms alone therefore do not imply the rank/volume gate of `GC`.

What the present theorem accomplishes is a clean product-preserving localization of the obstruction: the formerly amorphous global rank-one tube is now either paid into aggregate `E_2`, or has one of two explicit original-coordinate grouped geometries (H/G). The next receiver must combine that grouped geometry with an independent curvature/crossing resource from the ambient form, rather than pretending that the rank-one packet already contains three smoothing directions.

## 7. Precise remaining implication

The first B07 debt is now

`QFORM-HUBGRID-PLUS-THIRD-RESOURCE-RECEIVER-v1`:

* on the aggregate `E_2` branch, select/average the second-minor mass jointly with an ambient third resource while retaining arbitrary same-bank curvature and the true remainder;
* on branch H, combine the twelve-star physical hub with an actual projected `Z_2`, independent square, or paid physical-core resource, verifying all row-marginal gates of the new grouped-crossing theorem;
* on branch G, use the 12-by-2 aligned grid to extract either a genuine rank-two/two-hub packet plus one projected crossing direction, or prove that failure forces a bounded physical principal core.

The newest account04/B07 diagonal-rank-tail theorem is a valid candidate for the last exit only if the construction actually regenerates enough large physical diagonals; the current N3 packet does not yet supply them.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.** This run proves only the deterministic supporting geometry above; it does not produce a new full-ambient density bound in the remaining H/G branches.

## 8. Rigorous computation / regression

`CHECKS.py` verifies, using exact integer arithmetic on 625 finite matrices, that the physical `2x2`-minor sum equals the second-compound trace identity. It also verifies all numerical constants and the greedy twelve-bank inequalities, and performs 500 seeded capped-weight regression tests of the packing algorithm. Its captured output ends `STATUS=PASS`.

Those computations are sanity/regression evidence only; the proof of Theorems 2.1 and 5.1 is the algebra above.

## 9. Source/status integrity

- `QFORM-ENTRYCAP-E2-OR-DIFFUSE-TOPMODE-v1`: **proved supporting deterministic theorem**.
- `QFORM-DIFFUSE-TOPMODE-12BANK-v1`: **proved supporting deterministic theorem**.
- `QFORM-BANKCYCLE-E2-OR-HUBGRID-v1`: **proved supporting theorem on the source-pinned r33 strict-N3 packet**.
- account04/B07 r1 coefficient cap: **actually applied** at (3.2), (3.5), (4.4), (5.3), (5.6).
- account04/B07 r2 diagonal-rank-tail theorem: **read and scope-checked; not applicable to the current tiny-diagonal packet without a new diagonal-generation step**.
- interactive `GC` projected-crossing theorem: **read and scope-checked; its projected-volume gate is not automatically supplied by this rank-one endpoint**.
- Full QFORM: **OPEN**.
- Full continuity: **OPEN**.
- Repository access is not native learned-memory ingestion: **WITHOUT_VERIFIED_BRAIN**.
