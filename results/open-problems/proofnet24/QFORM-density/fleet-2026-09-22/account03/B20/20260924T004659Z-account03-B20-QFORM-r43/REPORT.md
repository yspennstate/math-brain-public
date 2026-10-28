SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-24T00:46:59Z.
attacking: the fresh global disjoint-E2 packet from account03/B19 r45 after the account01/B02 E3 payment; prove that the entire remaining packet is an ultra-thin literal rank-two tube or a quantitative giant rank-one tube, and splice the designated account04/B20 one-anchor theorem into the same funnel.

# account03/B20 r43 — low-third-volume E2 packet collapses to an ultra-thin rank-two/rank-one tube

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Proof closure and keeper  
Status: **NEW STRUCTURAL CLOSURE / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.  
Full-target continuity: **OPEN**. Continuity is claimed below only on the already-paid physical-E3 branch.

## 1. Fresh proof graph and correction boundary


The live corrections were reread before publication. In particular this run does not use: law-uniform pointwise quadratic-phase decay; the refuted maximal weak-L2 chirp supremum; arbitrary-joint rank-three coarea; worst-fiber projected-density bounds; post-rotation independence; deletion of a small nonzero quadratic/cross tail on unbounded inputs; a one-good-minor inference; or Monte Carlo as proof.

The current synthesis input is account03/B19 r45,

`yspennstate/math-open-problems@cb2d1efbcba8c6977376e0ad3d15638a6df8ff58`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T000337Z-account03-B19-QFORM-r45/REPORT.md`.

After the paid diagonal/principal-triple/disjoint-E3 branches and its overlap-two funnel, every remaining state is routed into one of four literal original-coordinate packets, one of which is a disjoint physical cross block `M` satisfying

`E2(M)>4/9`.                                                        (1.1)

Here, if `sigma_1(M)>=sigma_2(M)>=...` and `x_i=sigma_i(M)^2`,

`E2(M)=e_2(x)=sum_(i<j) x_i x_j`,
`E3(M)=e_3(x)=sum_(i<j<k) x_i x_j x_k`.                           (1.2)

The fresh account01/B02 r41 theorem applies the completed marginal-free physical-E3 receiver at

`E3(M)>=2^(-18)`                                                   (1.3)

and gives a continuous `C_0` density with

`||p_Q||_infinity <=82.760672`.                                   (1.4)

Therefore the first still-unpaid E2 implication may assume

`E2(M)>4/9`, `E3(M)<2^(-18)`.                                    (1.5)

This run attacks (1.5) directly.

## 2. A sharp exterior-volume tail inequality

### Lemma 2.1 — `QFORM-E3-OVER-E2-RANK2-TAIL-v1`

For every finite or compact real matrix `M`, let

`x_1>=x_2>=...>=0`

be its squared singular values and define

`T_2:=sum_(k>=3) x_k
     =dist_F(M,{rank<=2})^2`.                                    (2.1)

Then

`boxed: T_2 E2(M) <= 3 E3(M).`                                   (2.2)

Equivalently, whenever `E2(M)>0`,

`boxed: dist_F(M,{rank<=2})^2 <= 3 E3(M)/E2(M).}`                 (2.3)

#### Proof

For every unordered pair `{i,j}`, the sum of the squared singular values outside that pair obeys

`sum_(k notin {i,j}) x_k
 >=sum_(k>=3)x_k=T_2`,                                            (2.4)

because `x_i+x_j<=x_1+x_2` by monotonicity. Multiply (2.4) by the nonnegative weight `x_i x_j` and sum over `i<j`. Every unordered triple `{i,j,k}` is counted exactly three times on the left, so

`sum_(i<j) x_i x_j sum_(k notin {i,j})x_k
 =3 sum_(i<j<k)x_i x_j x_k
 =3E3(M).`                                                        (2.5)

The right side of the summed inequalities is `T_2 E2(M)`. This proves (2.2)-(2.3). QED.

This is a deterministic singular-value identity/inequality. It uses no random-coordinate rotation at all.

## 3. Apply the lemma at the live E2/E3 thresholds

Under (1.5), Lemma 2.1 gives

`T_2
 <3*2^(-18)/(4/9)
 =27/2^20
 =27/1048576
 =2.574920654296875e-5`.                                         (3.1)

Hence every still-unpaid E2 packet satisfies

`boxed:
 dist_F(M,{rank<=2})
 <3sqrt(3)/1024
 =0.005074367600299445.}`                                        (3.2)

Thus the current global `E2>4/9` survivor is not merely qualitatively low-third-volume. It lies in a **dimension-free 0.005075 Frobenius tube around a literal rank-two original-coordinate cross block**, with the nonzero tail retained in the actual quadratic form.

No claim is made that the tail can be deleted probabilistically.

## 4. Robust rank-two versus giant rank-one split

Set

`tau:=27/2^20`.                                                    (4.1)

There are now two exhaustive possibilities.

### Branch R2: a robust second cross singular value

If

`sigma_2(M)>=1/8`,                                                 (4.2)

then (3.2) already yields the explicit surviving packet

`boxed:
 sigma_2(M)>=1/8,
 dist_F(M,{rank<=2})<3sqrt(3)/1024.}`                             (4.3)

This is an ultra-thin, genuinely rank-two physical cross tube. Arbitrary same-bank quadratic blocks and all outside couplings are still present.

### Branch R1: the second cross singular value is small

Suppose instead

`sigma_2(M)<1/8`, so `x_2<1/64`.                                  (4.4)

Put `T=sum_(k>=3)x_k`; by (3.1), `T<tau`. Then

`dist_F(M,{rank<=1})^2=x_2+T
 <1/64+tau
 =16411/1048576`.                                                 (4.5)

Therefore

`boxed:
 dist_F(M,{rank<=1})
 <sqrt(16411)/1024
 =0.12510295442771513.}`                                         (4.6)

The leading singular value is simultaneously forced to be large. Indeed, writing

`E2(M)=x_1(x_2+T)+x_2T+e_2(x_3,x_4,...)`,                         (4.7)

and using

`x_2<1/64`, `T<tau`,
`e_2(x_3,x_4,...)<=T^2/2`,                                       (4.8)

we obtain

`E2(M)
 <x_1(1/64+tau)+tau/64+tau^2/2`.                                 (4.9)

Since `E2(M)>4/9`, this forces

`x_1>
 [4/9-tau/64-tau^2/2]/[1/64+tau]
 =8796085053023/309747253248
 =28.3976208369486... .`                                         (4.10)

Consequently

`boxed: sigma_1(M)>5.328941812118856.}`                           (4.11)

So failure of the robust-rank-two gate turns the packet into a quantitative **giant near-rank-one literal crossing** rather than an amorphous low-volume state.

### Theorem 4.1 — `QFORM-LOCAL-E2-ULTRATHIN-R2-OR-GIANT-R1-v1`

Every literal original-coordinate cross block satisfying (1.5) obeys one of the mutually exhaustive structural alternatives (4.3) or (4.6),(4.11).

Combined with account01/B02 r41, every global r45 disjoint-`E2` packet is therefore either:

1. continuously paid by `E3>=2^-18`, with `||p_Q||_infinity<=82.760672`; or
2. an ultra-thin robust-rank-two tube (4.3); or
3. a giant near-rank-one tube (4.6),(4.11).

This is the first missing implication proved in this run.

## 5. Designated account04/B20 result applied at an actual live inequality

The completed designated partner result used is account04/B20 r12,

`yspennstate/math-open-problems@95d5c3b6e8a753f5da44f742f8449d51470f4a11`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T201641Z-account04-B20-QFORM-r12/REPORT.md`.

For an anchored literal block

`[[b,r^T],[c,N]]`,                                                 (5.1)

its corrected aggregate theorem states

`sqrt(J3_full)
 <=|b| sqrt(E2(N))+||r||_2||c||_2||N||_F`,                        (5.2)

and hence

`max{b^2 E2(N), ||r||_2^2||c||_2^2||N||_F^2}
 >=J3_full/4`.                                                     (5.3)

On the actual B20 overlap-one split already present in the current global compiler,

`J_sep>=1/2304`, `|b|<1/64`.                                     (5.4)

Applying the partner theorem to that live inequality gives exactly

`boxed: E2(N)>4/9`                                                (5.5)

or

`boxed: ||r||_2||c||_2||N||_F>=1/96.`                            (5.6)

The new Theorem 4.1 now immediately refines the partner's first branch: if additionally `E3(N)>=2^-18`, the account01/B02 physical-E3 receiver pays it continuously below `82.761`; otherwise the **same actual literal N** obeys either the ultra-thin robust-rank-two collar (4.3) or the giant near-rank-one collar (4.6),(4.11).

Thus the account04/B20 aggregate third-volume theorem is not merely cited: one of its actual current inequalities is fed into the new tail theorem.

I do not apply (5.2) to an arbitrary restricted third-minor sub-sum; r12 explicitly corrected that overreach.

## 6. Relation to the other current residual packets

The fresh r45 synthesis also retains:

- one-anchor/two-star product packets;
- a physical two-star packet;
- a separate giant near-rank-one cross packet with stronger leading size but a different tail constant.

Theorem 4.1 does not claim those are paid. It does, however, remove the previous broad `E2>4/9` chamber as an independent amorphous case. After the already-proved E3 payment, its entire debt is now concentrated on two explicit low-rank tubes.

The first next closure edge is therefore

`QFORM-E2-ULTRATHIN-R2-OR-GIANT-R1-PAYMENT-v1`:

> uniformly pay (a) a literal physical cross block with `sigma_2>=1/8` and Frobenius distance `<3sqrt(3)/1024` from rank two, retaining the full nonzero tail and arbitrary same-bank curvature; or (b) a literal crossing with `sigma_1>5.32894` and Frobenius distance `<0.125103` from rank one. Splice either payment with the existing two-star/one-anchor packets rather than deleting the tail or replacing physical product provenance by an arbitrary joint law.

The ultra-thin rank-two branch is especially compatible with the existing tail-retaining B06/B19 Schur and overlap-square machinery, but those theorems still require an additional physical pivot/cross-null curvature resource. I do not silently assume that resource here.

## 7. Quantitative checks

The constants were recomputed independently:

- `tau=27/2^20=2.574920654296875e-5`;
- `sqrt(tau)=3sqrt(3)/1024=0.005074367600299445`;
- `1/64+tau=16411/1048576=0.01565074920654297`;
- `sqrt(16411)/1024=0.12510295442771513`;
- the exact lower bound in (4.10) is `8796085053023/309747253248=28.3976208369486...`;
- its square root is `5.328941812118856...`.

A separate random singular-value regression over dimensions 3 through 29 found zero violations of `T_2 E2<=3E3`; the largest sampled ratio `(T_2E2)/(3E3)` was about `0.981`. This is diagnostic only; Lemma 2.1 is proved analytically by the exact triple-counting identity (2.5).

## 8. Status

`QFORM-E3-OVER-E2-RANK2-TAIL-v1`: **PROVED supporting lemma**.  
`QFORM-LOCAL-E2-ULTRATHIN-R2-OR-GIANT-R1-v1`: **PROVED structural closure**.  
Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**. The `E3>=2^-18` branch has a continuous `C_0` density by the cited physical-E3 theorem; the two surviving low-rank tubes are not claimed to have been paid in this run.

No scheduler, notification, email, permission, public-release, paid-model, installation, or cross-account-authentication change is part of this mathematical report.
