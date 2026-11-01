SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T14:28:46Z.
attacking: the nonzero-edge heavy E3 anchor with rank(S)>=3: convert a^2 E2(S) mass into an integrated-Fourier exit or a strictly deeper physical packet, then apply fleet04/B02's zero-diagonal L2 theorem to an actual hybrid inequality.

# fleet03/B02 r32 — heavy E3 anchor second descent through residual E2

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Owner control at start:** revision `2026-09-22.15`; QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport only  
**Full QFORM target:** **OPEN**  
**Target-wide universal unweighted Fourier L1 criterion:** **OPEN / not refuted**  
**Continuity:** proved on the new Fourier exit below; not proved on the structural packet alternatives and not proved for the full target.

## 1. Purpose and exact live branch

The preceding B02 run `QFORM-E3-MARGINAL-OVERLOAD-ANCHOR-COMPILER-v1` says that, for a physical cross block `B=A[I,J]` with `Z=E3(B)>0`, either a fractional third-volume Fourier gate pays the full law, or there are actual original-coordinate anchors `x in I`, `y in J` whose joint incident third-volume `J` is large. At the working choice `q=4/3`,

`J > Z/3`.

Writing the physical cross block around these anchors as

`B = [[a, r^T], [c, N]]`,                                       (1.1)

when `a!=0` the exact anchored identity is

`J = a^2 E2(S),       S=N-c r^T/a`.                              (1.2)

The exact-rank-two `S` branch is already paid by the grouped Schur `L1` theorem. The live B02 residue was therefore `a!=0`, `rank(S)>=3`.

This run does **not** try to delete the third and later singular directions of `S`. That would be invalid under arbitrary unbounded cap-one input laws. Instead it compares the cross-Schur second volume with the literal residual block `N`. Either a genuine two-star/transverse packet is already large, or enough literal residual `E2(N)` survives to invoke the completed weighted mixed-(3+2) Fourier theorem. Failure of that Fourier gate is then compiled into one more actual row and column.

The resulting theorem is correction-safe and, in fact, does not require `rank(S)>=3`; it is applied here specifically to that live branch because rank two already has a sharper payment.

## 2. Source-pinned inputs actually used

1. **B02 r30 heavy-anchor compiler**, canonical source
   `yspennstate/math-open-problems@cb55a355bc5c623eb5a98c1db8a0ebaa58ff1027`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T125927Z-fleet03-B02-qform-r30/REPORT.md`.
   It supplies the live alternative `J>Z/3`, the exact identity (1.2), and the already-paid exact-rank-two branch.

2. **Weighted mixed-(3+2) Fourier theorem**, B02 r25, canonical source
   `yspennstate/math-open-problems@ff8ec2ee90d4846f39e728e1ca20d50c717cc894`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T085705Z-fleet03-B02-qform-r25/REPORT.md`.
   If `J3` is third-volume incident to one physical row/column anchor and `E2` is the residual second volume after deleting those anchors, then at `theta=1/2` and `1<q<5/4`, a mixed marginal gate gives an `L1` characteristic function. Simultaneous row/column gate failure forces a common-anchor packet of relative mass `>q-1` in either the third-volume family or the residual second-volume family.

3. **Designated partner fleet04/B02**, canonical source
   `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.
   If a nonsingular physical zero-diagonal principal triple `H0` exists, then

   `int_R |phi_Q(t)|^2 dt <= 6 pi 2^(2/3) |det H0|^(-1/3)`.       (2.1)

No law-uniform pointwise van-der-Corput bound, post-rotation independence, arbitrary-joint coarea bound, positive conditional projection-height moment, fiber supremum, or coefficient-perturbation continuity is used.

## 3. Exterior-square survival lemma

### Lemma 3.1 — literal residual E2 or two-star/transverse mass

In (1.1), assume `a!=0`, set

`S=N-c r^T/a`,
`F=||P_(c^perp) N P_(r^perp)||_F`,                              (3.1)

with the evident convention when `c=0` or `r=0`. Then

`boxed:
 sqrt(J) <= |a| sqrt(E2(N)) + ||c||_2 ||r||_2 F.
`                                                                     (3.2)

Consequently at least one of

`boxed: a^2 E2(N) >= J/4`                                       (3.3)

or

`boxed: ||c||_2^2 ||r||_2^2 F^2 >= J/4`                         (3.4)

holds.

#### Proof

For a matrix `M`, `E2(M)=||wedge^2 M||_HS^2`. For a rank-one update `M+p q^T`, the exterior-square difference is supported only on wedges containing the `q` direction, and an orthonormal-coordinate calculation gives

`|| wedge^2(M+p q^T)-wedge^2 M ||_HS
 = ||p|| ||q|| ||P_(p^perp) M P_(q^perp)||_F`.                  (3.5)

Apply (3.5) to `S=N-c r^T/a`. The transverse block is unchanged by the update, so

`sqrt(E2(S))
 <= sqrt(E2(N)) + (||c|| ||r||/|a|)F`.                          (3.6)

Multiply by `|a|` and use the exact incident-minor identity `sqrt(J)=|a|sqrt(E2(S))`. This proves (3.2). If both terms on the right of (3.2) were `<sqrt(J)/2`, their sum would be `<sqrt(J)`, impossible. Squaring gives (3.3)-(3.4). QED.

This is an aggregate-before-inversion statement. No individual residual minor is selected.

## 4. Main theorem — `QFORM-HEAVY-E3-ANCHOR-SECOND-DESCENT-v1`

Assume the setup (1.1)-(1.2) with `J>0`. Put

`E=E2(N)`.

Then at least one of the following four alternatives holds.

### (S) Immediate two-star/transverse packet

`boxed:
 ||c||^2 ||r||^2
 ||P_(c^perp) N P_(r^perp)||_F^2 >= J/4.
`                                                                     (4.1)

### (F) Mixed-volume integrated-Fourier exit

The full ambient law has `phi_Q in L1`, hence a continuous density vanishing at infinity, and

`boxed:
 ||p_Q||_infinity
 <= (20 sqrt(2) e/3) |a|^(1/5) J^(-1/5)
 =25.6282068544... |a|^(1/5)J^(-1/5).
`                                                                     (4.2)

### (H3) Deeper double-anchor third-volume packet

There are non-anchor physical row/column coordinates `i,j` such that

`boxed: G3^(x,i;y,j)(B) > J/8.`                                  (4.3)

### (H2) Deeper residual second-volume packet

There are non-anchor physical row/column coordinates `i,j` such that

`boxed:
 H2^(i,j)(N) > E/8 >= J/(32 a^2).
`                                                                     (4.4)

Here `G3` is the sum of squared physical `3x3` minors containing both indicated row anchors and both indicated column anchors, and `H2` is the sum of squared residual `2x2` minors containing the indicated residual row and column.

#### Proof

By Lemma 3.1, either (S) holds or

`a^2 E >= J/4`.                                                   (4.5)

Assume (4.5). In particular `E>0`. Apply `QFORM-WEIGHTED-MIXED32-FOURIER-L1-v1` to the **same physical anchor** `(x,y)`, with incident third-volume `J3=J`, literal residual block `N`, and residual second-volume `E2=E`. Take

`theta=1/2`, `q=9/8`.                                            (4.6)

The mixed row and column inclusion marginals each have total mass `5/2`, while the two original anchors themselves have mixed marginal exactly `1/2`, below the gate `q/2=9/16`.

If either the row or column mixed marginal gate passes, the cited theorem gives

`||p_Q||_infinity
 <= C_(9/8) (J E)^(-1/10)`,                                     (4.7)

where

`C_(9/8)
 =5e/[2^(1/5)(5-4(9/8))sqrt(9/8)]
 =(20 e/3) 2^(3/10)
 =22.3106499134...`.                                             (4.8)

Use (4.5):

`(J E)^(-1/10)
 <= (J^2/(4a^2))^(-1/10)
 =2^(1/5)|a|^(1/5)J^(-1/5).`                                    (4.9)

The factor `2^(1/5)` cancels the corresponding factor in (4.8), yielding exactly (4.2). The cited Fourier proof has exponent

`b=(2+theta)/(2q)=(5/2)/(9/4)=10/9>1`,                           (4.10)

so this is a genuine `L1` characteristic-function conclusion, not merely an essential-density transfer.

It remains to handle simultaneous row and column gate failure. Because the anchor marginals equal `1/2<9/16`, the heavy coordinates are nonanchors. Choose a heavy row `i` and heavy column `j`. Under the equal mixture of the incident-third-minor and residual-second-minor determinant laws,

`P(i included and j included)
 >=P(i included)+P(j included)-1
 >9/16+9/16-1=1/8.`                                             (4.11)

If `p3` and `p2` denote this joint-incidence probability under the third- and second-volume constituent laws, respectively, then

`(p3+p2)/2>1/8`,                                                 (4.12)

so `max(p3,p2)>1/8`. If `p3>1/8`, (4.3) follows. If `p2>1/8`, then `H2^(i,j)(N)>E/8`; combine with (4.5) to obtain (4.4). QED.

### Exact normal forms of the two deeper packets

The alternatives (H3)-(H2) are not labels for unspecified concentration. They are exact finite physical packets.

For (H2), reorder the selected residual row and column first:

`N=[[b,rho^T],[gamma,M]]`.

Then

`boxed: H2^(i,j)(N)=||bM-gamma rho^T||_F^2.`                     (4.13)

Thus `b!=0` gives a scalar-edge times cross-Schur Frobenius bank; `b=0` gives the exact two-star product `||gamma||^2||rho||^2`.

For (H3), reorder the two selected row anchors and two selected column anchors first:

`B=[[P,R],[C,M]]`, with physical `2x2` `P`.

Then

`boxed:
 G3^(x,i;y,j)(B)
 =||det(P)M-C adj(P)R||_F^2.
`                                                                     (4.14)

If `det P!=0`, this is `det(P)^2||M-CP^(-1)R||_F^2`; if `det P=0`, positivity forces the corresponding inverse-free rank-one/two-star packet. These exact identities connect the present descent directly to the already-developed double-anchor and grouped-hub receivers.

## 5. Specialization to the live r30 heavy branch

On the r30 `q=4/3` heavy branch,

`J>Z/3`.                                                         (5.1)

Therefore alternative (F) sharpens to the explicit continuous-density bound

`boxed:
 ||p_Q||_infinity
 < C_Z |a|^(1/5) Z^(-1/5),
 C_Z=(20 sqrt(2)e/3)3^(1/5)
    =31.9258502054....
`                                                                     (5.2)

The three failure alternatives become respectively

`||c||^2||r||^2F^2>Z/12`,                                       (5.3)

`G3^(x,i;y,j)>Z/24`,                                             (5.4)

or

`H2^(i,j)(N)>Z/(96a^2)`.                                        (5.5)

Thus the previous unresolved phrase “`a!=0, rank(S)>=3`” is no longer a single analytic obstruction. It is reduced to a genuine `L1` Fourier exit or one of three explicit physical concentration packets already compatible with the fleet's star/double-anchor machinery. The theorem does not claim those three packets are all fully paid at universal scale.

## 6. Designated fleet04/B02 result applied to an actual new inequality

Assume the Fourier exit (F) and, additionally, that the full physical matrix contains a nonsingular zero-diagonal principal triple `H0`. Let

`R=J E`.                                                         (6.1)

The `theta=1/2,q=9/8` proof used above gives the explicit high-frequency envelope

`|phi_Q(t)|
 <=min{1,K0 R^(-1/9)|t|^(-10/9)},`                              (6.2)

with

`K0=2^(-2/9)e^(10/9)(9/8)^(-5/9)pi^(10/9)
   =8.70210960761....`                                           (6.3)

The designated fleet04/B02 theorem gives

`L:=int_R |phi_Q(t)|^2dt
 <=6pi 2^(2/3)|det H0|^(-1/3).`                                 (6.4)

For every `T>0`, Cauchy--Schwarz on `[-T,T]` and (6.2) outside give

`||phi_Q||_1
 <=sqrt(2LT)+18K0 R^(-1/9)T^(-1/9).`                           (6.5)

Write `A=sqrt(2L)` and `K=K0R^(-1/9)`. The exact optimizer satisfies

`T^(11/18)=4K/A`.                                                (6.6)

At this optimizer the second term in (6.5) is `(9/2)` times the first, hence

`||phi_Q||_1
 <=(11/2) A^(2/11)(4K)^(9/11).`                                (6.7)

Fourier inversion and (6.3)-(6.4) yield the new hybrid inequality

`boxed:
 ||p_Q||_infinity
 <= C_H |det H0|^(-1/33)(J E)^(-1/11),
`                                                                     (6.8)

where the pi factors cancel and

`C_H
 =11*2^(35/33)*3^(-9/11)*e^(10/11)
 =23.1797182431....`                                             (6.9)

Using (4.5),

`boxed:
 ||p_Q||_infinity
 <=26.2930446641
 |det H0|^(-1/33)|a|^(2/11)J^(-2/11).
`                                                                     (6.10)

On the live `J>Z/3` branch,

`boxed:
 ||p_Q||_infinity
 <32.1062954747
 |det H0|^(-1/33)|a|^(2/11)Z^(-2/11).
`                                                                     (6.11)

This is an equation-level use of the designated partner theorem, not a citation-only mention. Continuity on this overlap is already guaranteed by the mixed-volume `L1` branch.

## 7. Deterministic numerical regression

A seeded finite regression (`seed=20260923`) was used only to catch indexing and constant errors; it is not part of the proof.

For 1,000 random real `6x6` cross blocks, with anchor `(0,0)`, the checker enumerated every physical `3x3` minor containing the anchor row and column. It verified

`J=a^2 E2(N-cr^T/a)`                                             (7.1)

and the survival inequality (3.2). Results:

- maximum relative error in (7.1): `2.58386474356e-14`;
- minimum numerical slack in (3.2): `0.0158090862610`;
- violations: `0`.

The constants in (4.8), (4.2), (5.2), (6.9), (6.10), and (6.11) were recomputed independently in the same run. The symbolic arguments above are the proof.

## 8. What remains

The **full conjecture remains open**. This run neither proves nor refutes a target-wide universal unweighted `int |phi_Q|` bound.

For B02 the immediate residue after this run is no longer generic high-rank `S`. It is the explicit packet compiler problem:

`QFORM-HEAVY-ANCHOR-PACKET-PAYMENT-v1` — pay, at target scale and without selecting a reciprocal tiny minor, one of

1. `||c||^2||r||^2F^2 >= J/4`;
2. `G3^(x,i;y,j)>J/8`;
3. `H2^(i,j)(N)>J/(32a^2)`;

using the existing two-star, double-anchor stable-rank/low-rank, pair-log, grouped-bank, or fractional-volume receivers. The exact-rank-two cross-Schur branch remains already closed by r30.

No continuity conclusion is claimed on these three unpaid packet alternatives.
