SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-24T07:03:28Z.
attacking: coordinate-minor selection in the exact-singular physical-shear branch, and pair-preserving rainbow extraction from the current global rank-two separator.

# account01/B07 r43 — anchored fourth-compound Schur shadow and pair-deleted rainbow E2 packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection  
Status: **NEW EXACT COMPOUND IDENTITY + NEW ACTUAL FOUR-BANK DETERMINANT PACKET / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**

The unrestricted conjecture remains open. No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis or post-rotation independence assumption is used. No pointwise law-uniform van-der-Corput estimate, arbitrary-joint coarea bound, fiber supremum, or deletion of a nonzero coefficient tail is used.

## 1. Sources and incoming exact-singular branch

Fresh owner control was read from `yspennstate/math-research-brain` main at startup commit

`26c1c354fa0bafe8de3d1c5f73317182121fbbd7`.

OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no account01/B07 stop or reassignment. The programme claim ledger still marks the full bounded-density conjecture and the full-target continuity conclusion OPEN.

The exact-singular incoming geometry is the completed account01/B07 r42 result

`yspennstate/math-open-problems@75c225389c931a99c6fc9004fccc432cbb2d5215`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/20260924T050626Z-account01-B07-qform-auto11-r42/PHYSICAL_SHEAR_ADDENDUM.md`.

There is an actual physical pair `H={h,h'}` with rank-one principal block. Order its endpoints so that the larger physical diagonal is first and write

`A[H,H]=[[a,c],[c,b]]`, `a!=0`, `kappa=c/a`,

`u=A[O,h]`, `v=A[O,h']`, `w=v-kappa u`, `O=H^c`.

Since the pair has rank one, `b=a kappa^2`. The literal unit-Jacobian shear `(x,y)->(x+kappa y,y)` converts the coefficient matrix, only for deterministic algebra and source-level bookkeeping, to

`A' = [[a,0,u^T],[0,0,w^T],[u,w,C]]`,                            (1.1)

where `C=A[O,O]`. Any minor containing the entire pair `H` in both its row and column sets is unchanged because the pair shear has determinant one on both sides.

The completed r42 exact-singular star estimate supplies

`gamma:=|a| ||w||_2^2 >=7/96`,                                  (1.2)

and the transverse direction is diffuse in original residual coordinates:

`max_r w_r^2/||w||_2^2 <1/7`.                                   (1.3)

The new identity below does not require (1.3); only (1.2) is used in its quantitative corollaries.

## 2. Exact anchored fourth-compound shadow

Define the scalar Schur residual

`S=C-u u^T/a`.                                                    (2.1)

For each oriented physical residual pair `R={r<s}` define

`q_R=w_s e_r-w_r e_s in R^O`.                                   (2.2)

Let `E_w` be the matrix whose column indexed by `R` is `q_R`. Let `F_H^(4)` be the matrix indexed by residual physical pairs in rows and columns,

`F_H^(4)[R,T] := det A[H union R, H union T]`,                    (2.3)

using one fixed increasing orientation for `H,R,T`.

### Theorem 2.1 — `QFORM-EXACTSINGULAR-ANCHORED-C4-SCHUR-SHADOW-v1`

One has the exact matrix identity

`boxed: F_H^(4) = -a E_w^T S E_w.`                               (2.4)

Moreover

`boxed: E_w E_w^T = ||w||_2^2 P_(w^perp).`                       (2.5)

Consequently the nonzero singular values obey

`boxed:
 s_j(F_H^(4))
 = |a| ||w||_2^2 s_j(P_(w^perp) S P_(w^perp)|_(w^perp)).
}`                                                                 (2.6)

In particular,

`boxed: ||F_H^(4)||op = gamma ||P S P||op`,                       (2.7)

`boxed: ||F_H^(4)||F  = gamma ||P S P||F`,                        (2.8)

where `P=P_(w^perp)`. More generally, for every `k`, the complete `k`th exterior singular packet of the anchored fourth-minor matrix is exactly `gamma^(2k)` times that of the transverse Schur compression.

#### Proof

Take residual row pair `R={r,s}` and column pair `T={c,d}`. Since `a!=0`, scalar Schur elimination in the first sheared pair coordinate gives

`det A'[H union R,H union T]`
` = a det [[0,w_c,w_d],[w_r,S_rc,S_rd],[w_s,S_sc,S_sd]].`         (2.9)

Expanding the `3x3` determinant,

`det [[0,w_c,w_d],[w_r,S_rc,S_rd],[w_s,S_sc,S_sd]]`
` = -w_c w_r S_sd+w_c w_s S_rd+w_d w_r S_sc-w_d w_s S_rc`
` = -q_R^T S q_T`.                                               (2.10)

The pair shear has determinant one, so the anchored minors of `A'` equal those of the original physical matrix `A`. This proves (2.4).

For (2.5), the diagonal `(i,i)` entry of `E_wE_w^T` is

`sum_{j!=i} w_j^2=||w||^2-w_i^2`,

while its `(i,j)` entry for `i!=j` is `-w_i w_j`. Hence

`E_wE_w^T=||w||^2 I-w w^T=||w||^2P`.                             (2.11)

Thus `E_w/||w||` is a coisometry onto `w^perp`. Since `PSP` acts on that range, `E_w^T S E_w` has exactly the nonzero singular values `||w||^2 s_j(PSP|w^perp)`. Multiplying by `|a|` gives (2.6)-(2.8). QED.

### Quantitative consequence on the live exact-singular branch

By (1.2),

`boxed:
 ||F_H^(4)||F >= (7/96)||P S P||F,
 ||F_H^(4)||op >= (7/96)||P S P||op.
}`                                                                 (2.12)

Equivalently,

`boxed:
 ||P S P||F <=(96/7)||F_H^(4)||F,
 ||P S P||op<=(96/7)||F_H^(4)||op.
}`                                                                 (2.13)

This is dimension-free. No single `4x4` minor is selected or inverted: the whole anchored fourth-compound packet is the exact physical image of the transverse Schur curvature.

## 3. Exact rank-three fallback when the anchored shadow vanishes

Put `e=w/||w||`, `P=I-ee^T`,

`alpha=e^T S e`, `b=P S e`, `T=P S P`.                            (3.1)

Then

`S=alpha e e^T+e b^T+b e^T+T`.                                  (3.2)

After the scalar Schur elimination in the first pair coordinate, the residual coefficient matrix on the second pair coordinate and `O` is

`R = [[0,w^T],[w,S]].`                                            (3.3)

Define

`R0=[[0,w^T],[w,alpha e e^T+e b^T+b e^T]].`                       (3.4)

The range of `R0` is contained in the span of the physical second-pair coordinate together with `e` and `b`, so

`rank(R0)<=3`.                                                     (3.5)

The exact remainder is

`R-R0 = diag(0,T)`.                                               (3.6)

Therefore Theorem 2.1 yields the coefficient-level identities

`boxed:
 dist_op(R,rank<=3) <= ||F_H^(4)||op/gamma,
}`                                                                 (3.7)

`boxed:
 dist_F(R,rank<=3) <= ||F_H^(4)||F/gamma.
}`                                                                 (3.8)

In particular,

`boxed: F_H^(4)=0  =>  rank(R)<=3.`                               (3.9)

On the live branch `gamma>=7/96`, the right sides in (3.7)-(3.8) are at most `(96/7)` times the corresponding anchored-compound norms.

This does **not** authorize deletion of a nonzero `T`: arbitrary cap-one laws have no moment hypothesis. The structural gain is that the exact-singular low-pivot branch now has an exhaustive coefficient description: anchored fourth-compound currency, or a physical scalar-Schur residual lying in a quantitatively controlled rank-three tube.

## 4. Latest designated partner: actual pair-deleted rainbow E2 extraction

The latest completed designated account02/B07 result used here is

`yspennstate/math-open-problems@014a9c68675c6bc40377244dd28a128fa01d3efb`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260924T060205Z-account02-B07-qform/REPORT.md`.

Its unpaid global-separator branch has the literal physical cross block

`M=A[H_M^c,H_M]`,                                                 (4.1)

with

`s1(M)s2(M)>p_*:=1.19876993884320...`,                            (4.2)

and, after its E3-paid branch is removed, the normalized actual squared-`2x2`-minor law `p` satisfies

`d_TV(p,q)<1/12`,                                                  (4.3)

where `q=rho tensor kappa` is the leading rank-two product Pluecker law. For every determinant-stable matched physical column pair `K`,

`q{column pair avoids K}>1/4`.                                   (4.4)

The partner already pays `e3(MM^T)>=delta_*` continuously by

`||p_Q||infinity<=54.220600709697784...`; the argument below concerns only its unpaid branch.

### Theorem 4.1 — `QFORM-R48-PAIR-DELETED-ACTUAL-RAINBOW-E2-v1`

For every determinant-stable matched physical pair `K`, there exist literal original-coordinate partitions

`H_M^c=R disjoint_union S`,

`H_M\K=C disjoint_union D`,                                      (4.5)

such that the **actual** coefficient matrix, including its retained nonzero tail, satisfies

`boxed:
 Omega_K(R,S;C,D)
 :=sum_{r in R,s in S,c in C,d in D}
   det M[{r,s},{c,d}]^2
 >p_*^2/48
 =0.0299385284640443... .
}`                                                                 (4.6)

All four banks `R,S,C,D` are pairwise disjoint original-coordinate banks, and the preserved matched pair `K` is disjoint from all four. No individual minor is selected.

#### Proof

Under the product Pluecker law `q=rho tensor kappa`, fair independent two-coloring of the **row** physical coordinates splits a sampled row pair with probability `1/2`. Therefore some row partition `R,S` obeys

`q{row pair is R-S split AND column pair avoids K}`
` >(1/2)(1/4)=1/8`.                                               (4.7)

Total variation transfer (4.3) gives for the same event under the actual determinant law

`p{row split AND column pair avoids K}`
` >1/8-1/12=1/24`.                                                (4.8)

Since the total actual squared-minor mass is

`Z2=e2(MM^T)>p_*^2`,                                              (4.9)

the corresponding unnormalized actual minor packet has mass `>p_*^2/24`.

Now fair-color only the remaining physical columns `H_M\K`. Every actual column pair in (4.8) avoids `K`, hence is split by the new column coloring with probability exactly `1/2`. Averaging over that coloring produces some literal partition `C,D` for which the actual four-bank rainbow packet is larger than

`(1/2)(p_*^2/24)=p_*^2/48`.                                      (4.10)

This is (4.6). QED.

The sequential coloring is deliberate. Coloring rows and columns simultaneously at the `q` stage would leave only `q`-mass `>1/16`, smaller than the `1/12` TV error. Paying the TV transfer **before** the second coloring is what preserves a positive universal actual-coefficient packet.

### Interpretation

The partner's previous conclusion was that a leading rank-two carrier survives deletion of every stable matched pair. Theorem 4.1 upgrades this to a literal original-coordinate statement about the full matrix `M`: after preserving `K`, the actual determinant mass can be routed into four source-disjoint role banks with no reciprocal minor cost and with a numerical packet exceeding `0.0299`.

Thus the partner's remaining “third smoothing resource” problem may now be stated with a much cleaner physical carrier: one preserved matched pair `K` plus a genuinely rainbow actual `E2` packet on four banks disjoint from `K`.

## 5. What this run closes and what remains

Two coordinate-selection debts are reduced.

1. **Exact-singular low-pivot branch.** The arbitrary transverse same-bank curvature is no longer an opaque remainder. Its complete anchored mixed `4x4`-minor matrix is exactly a scaled partial-isometric copy of the transverse scalar-Schur compression. Large transverse curvature therefore creates anchored fourth-compound currency without selecting a tiny principal minor; vanishing currency forces an exact rank-`<=3` residual after scalar Schur elimination. A nonzero small packet yields a rank-three tube but may not be deleted.

2. **Current global rank-two separator.** The latest account02/B07 exterior-Pluecker theorem now yields, after every stable matched-pair deletion, an actual `>0.0299` four-bank determinant packet on original coordinates. The nonzero coefficient tail is retained because the TV transfer is made directly to the actual squared-minor law before the second coloring.

The sharpened next B07 obligations are therefore:

`QFORM-ANCHORED-C4-OR-RANK3-TAIL-RECEIVER-v1`: spend the exact-singular anchored fourth-compound packet, or consume the resulting rank-three-plus-nonzero-tail residual without moment assumptions; and

`QFORM-STABLE-PAIR-PLUS-RAINBOW-E2-THIRD-RESOURCE-v1`: combine one retained matched physical pair with the actual four-bank packet (4.6), retaining arbitrary same-bank curvature and all outside couplings, to produce the missing third smoothing direction or a previously paid physical E3/principal-core exit.

A clean rank-three cross-volume theorem cannot yet be invoked solely from (4.6): the preserved pair and the rainbow `E2` packet still have to be synchronized without assuming a block-diagonal form or deleting their cross couplings.

Full unrestricted QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**. Continuity is inherited only on the partner's already-paid physical-E3 branch, not on the new structural branches above.
