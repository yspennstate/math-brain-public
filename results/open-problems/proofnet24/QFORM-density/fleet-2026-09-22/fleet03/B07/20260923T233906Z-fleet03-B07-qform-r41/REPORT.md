SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B07, 2026-09-23T23:39:06Z.
attacking: the r40 one-overlap diagonal/projected-volume packet — pay star-dominant mass by a literal physical Z3 crossing, then route the diagonal-dominant remainder through the marginal-free square+Z2 receiver and the fleet04/B07 coordinate-core theorem.

# fleet03/B07 r41 — one-overlap diagonal-volume four-way router

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260923T233906Z-fleet03-B07-qform-r41`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW SUPPORTING ROUTER FOR r40 PACKET 1 / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, bounded-support, connected-support, iid, diagonal-basis, or post-rotation independence assumption is used. All banks below consist of literal original coordinates. No individual small determinant is inverted.

## 1. Exact incoming packet and source audit

The immediate source is my r40 report

`yspennstate/math-open-problems@c21a61aa6390c0be6ed68027341207e44c1bbb07`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T224121Z-fleet03-B07-qform-r40/REPORT.md`.

In the one-overlap sector it produces pairwise-disjoint original-coordinate banks `H,I,J`. For each `h in H`, write

`a_h=A_hh`, `m_h=A[h,J]`, `K=A[I,J]`.

If `m_h!=0`, decompose every row `k_i` of `K` as

`k_i=alpha_i m_h+c_i`, `c_i perpendicular m_h`,

and define

`Z_h=e2(C_h C_h^T)=sum_{r<s} ||c_r wedge c_s||^2`,

where `C_h=K(I-P_{m_h})`. If `m_h=0`, put `C_h=K` and use the same definition. The r40 positive compiler proves that one branch has

`S:=sum_{h in H} a_h^2 Z_h > 2/3125`.                         (1.1)

The complementary one-overlap packet `sum_h ||m_h||^2 W(h)>2/3125` remains a separate branch and is **not** claimed solved here.

Two source-valid analytic theorems are used.

1. Marginal-free physical third-volume crossing: if a literal cross block `M` has `Z3=e3(MM^T)>0`, the full ambient form has a continuous density with

`||p_Q||_infinity <= C3 Z3^(-1/6)`,
`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`.

A completed source is fleet02/B03, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T184716Z-fleet02-B03-QFORM-auto11/REPORT.md`.

2. Marginal-free square plus Schur-two-volume: if a physical scalar pivot is `d!=0` and a literal physical cut of its exact Schur residual has two-volume `Z2>0`, then

`||p_Q||_infinity <= 8 e^(1/4)(|d|^4 Z2)^(-1/8)`.             (1.2)

This is `QFORM-SQUARE-PLUS-Z2-MARGINAL-FREE-v1`, source

`yspennstate/math-open-problems@68e6d8f52d904033878f6f55c376c38fd214684e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T211103Z-fleet02-B03-QFORM-auto11/REPORT.md`.

A source search also found the earlier fleet01/B09 scalar-Schur aggregation theorem. Therefore no duplicate credit is claimed for the bordered-determinant Schur identity itself. The new step below is the aggregate star-versus-diagonal routing of the **colored r40 packet**, followed by a concrete partner-core graph alternative.

## 2. Star-dominant anchors pay a genuine physical Z3 crossing

For each `h`, exterior algebra gives the exact identity

`boxed:
 ||m_h||^2 Z_h
 = sum_{r<s in I} ||m_h wedge k_r wedge k_s||^2. `             (2.1)

Proof: `m_h wedge k_r wedge k_s=m_h wedge c_r wedge c_s`, and `c_r,c_s` lie in `m_h^perp`, so the squared norm is `||m_h||^2||c_r wedge c_s||^2`. Summing over `r<s` gives (2.1).

Now form the literal physical cross block

`M=A[H union I,J]`.                                             (2.2)

Cauchy--Binet identifies every summand on the right of (2.1) with the sum of squared physical `3x3` minors whose row triple is `{h,r,s}` and whose column triple lies in `J`. Different `h` give disjoint row-triple classes. Hence

`boxed:
 e3(MM^T) >= sum_{h in H} ||m_h||^2 Z_h. `                     (2.3)

Define

`G={h: ||m_h|| >= |a_h|}`,
`B=H\G`.                                                        (2.4)

If

`sum_{h in G} a_h^2 Z_h >= S/2`,                               (2.5)

then (2.3) gives

`e3(MM^T) >= S/2`.                                             (2.6)

Therefore the completed marginal-free Z3 theorem pays the **full ambient law**, with a continuous density,

`boxed:
 ||p_Q||_infinity <= C3 (S/2)^(-1/6). `                        (2.7)

For the actual r40 scale `S>2/3125`, this is

`e3(MM^T)>1/3125`,

`boxed: ||p_Q||_infinity < C3*3125^(1/6)
                        =40.3398624643818... .`                 (2.8)

Thus half of the aggregate diagonal/projected-volume currency is now paid without choosing a hub or minor at all whenever its hub-to-`J` stars dominate the diagonals.

## 3. Diagonal-dominant anchors: exact Schur two-volume survives

Assume instead that (2.5) fails. Then

`sum_{h in B} a_h^2 Z_h > S/2`,                                (3.1)

and every contributing `h in B` has `|a_h|>||m_h||`, hence `a_h!=0`.

Fix such an `h`, write `u_h=A[I,h]`, and complete the original coordinate `h` exactly. The `I x J` cross block of the scalar Schur residual is

`R_h=K-a_h^(-1)u_h m_h`.                                       (3.2)

Because `m_h(I-P_{m_h})=0`,

`R_h(I-P_{m_h})=K(I-P_{m_h})=C_h`.                             (3.3)

Therefore

`C_h C_h^T <= R_h R_h^T`                                      (3.4)

in Loewner order. Eigenvalue monotonicity for positive semidefinite matrices gives

`boxed:
 e2(R_hR_h^T) >= e2(C_hC_h^T)=Z_h. `                           (3.5)

Equation (1.2) consequently pays every anchor satisfying

`|a_h|^4 Z_h >= eta`                                           (3.6)

by

`boxed:
 ||p_Q||_infinity <=8e^(1/4) eta^(-1/8). `                     (3.7)

No two-volume marginal/spread hypothesis remains.

## 4. Fixed-scale four-way compiler

The preceding facts become especially useful after separating physical diagonal scales. Fix any `d>0`, and put

`B_hi={h in B: |a_h|>=d}`,
`B_lo=B\B_hi`.                                                  (4.1)

Under (3.1), one of the following is exhaustive.

### A. Low-diagonal projected-volume bank

If

`sum_{h in B_hi} a_h^2Z_h < S/4`,                              (4.2)

then

`sum_{h in B_lo} a_h^2Z_h >S/4`.                               (4.3)

Since `|a_h|<d` on `B_lo`,

`boxed:
 sum_{h in B_lo} Z_h > S/(4d^2), `                             (4.4)

and because `B_lo subset B`, these anchors additionally satisfy

`||m_h||<|a_h|<d`.                                             (4.5)

This is a dimension-free aggregate projected-two-volume packet with both the physical diagonal and the associated hub star uniformly small. It is not yet a density theorem.

### B. At most two high-diagonal anchors

Suppose instead

`sum_{h in B_hi} a_h^2 Z_h >=S/4`                              (4.6)

and `|B_hi|<=2`. Then some `h in B_hi` obeys

`a_h^2 Z_h >=S/8`.                                             (4.7)

Consequently

`|a_h|^4 Z_h >=d^2 S/8`,                                      (4.8)

and (3.7) pays the full law:

`boxed:
 ||p_Q||_infinity <=8e^(1/4)(d^2S/8)^(-1/8). `                 (4.9)

### C/D. At least three high-diagonal anchors: partner core or dense internal-edge graph

Assume (4.6) and `N:=|B_hi|>=3`. Apply the designated completed partner `fleet04/B07` theorem

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T161510Z-fleet04-B07-coordinate-core-r2/REPORT.md`.

Its `r=0` coordinate-core case says that for any actual three-coordinate principal block written as `D+E`, with all three diagonal magnitudes at least `d` and `|E|_max<=epsilon`,

`s3 >= d-3epsilon`,                                             (4.10)

and the full ambient law obeys

`||p_Q||_infinity <=2sqrt(18pi)/(d-3epsilon)`.                 (4.11)

Take `epsilon=d/12`. If there exist three anchors in `B_hi` whose three mutual off-diagonal entries all have magnitude at most `d/12`, then

`s3 >=3d/4`                                                     (4.12)

and the partner gives the actual full-target inequality

`boxed:
 ||p_Q||_infinity <=(8/3)sqrt(18pi)/d
                   =20.0530261970480.../d. `                   (4.13)

This is essential boundedness; continuity is not claimed by the partner gate.

If no such triple exists, make a graph on `B_hi` by joining `h,k` when

`|A_hk|>d/12`.                                                  (4.14)

The graph has independence number at most two. Its complement is triangle-free, so Mantel's theorem gives at least

`boxed:
 E_N := binom(N,2)-floor(N^2/4) `                               (4.15)

large physical edges. Hence the literal unordered internal-edge energy satisfies

`boxed:
 sum_{h<k in B_hi} A_hk^2
 > E_N d^2/144. `                                              (4.16)

This is a new concrete dense-edge residual packet forced by failure of the fleet04/B07 physical-core exit.

## 5. Numerical specialization at the r40 scale

Take the actual lower bound `S>2/3125` and choose

`d=1/64`.                                                       (5.1)

The four-way compiler becomes:

1. **star-dominant Z3 exit:** full ambient continuous density
   `||p_Q||_infinity<40.339863`;
2. **at most two high-diagonal anchors:** since
   `d^2 S/8 >1.953125e-8`,
   the full ambient essential density obeys
   `||p_Q||_infinity<94.476187`;
3. **three or more high-diagonal anchors:** either the partner physical-core exit gives
   `||p_Q||_infinity<1283.393677`,
   or there are at least `E_N` physical internal edges larger than `1/768` in magnitude;
4. **low-diagonal survivor:**
   `boxed: sum_{h in B_lo} Z_h >0.65536`,
   while every such anchor satisfies
   `|A_hh|<1/64` and `||A[h,J]||<1/64`.

Thus the r40 packet-1 debt has been reduced to two genuinely aggregate survivors: a large low-diagonal projected-two-volume bank or a dense internal high-diagonal edge graph. The previous dimension-losing instruction “choose the best shared hub” is no longer needed for any of the paid branches.

## 6. Regression checks

I checked the algebra independently on random finite matrices and exact rational examples.

- 500 floating-point trials verified (2.1), (2.3), and (3.5); maximum relative error in (2.1) was `6.32e-14`, and no Loewner/e2 violation occurred.
- 50 exact rational/integer trials verified (2.1) and the Schur projected-two-volume inequality exactly.
- Constants in Section 5 were recomputed from their displayed formulas.

These finite checks are regression evidence only; Sections 2--4 are the proof.

## 7. Remaining first implication

The immediate B07 debt is now

`QFORM-ONEOVERLAP-LOWDIAG-Z2-OR-DENSEEDGE-RECEIVER-v1`:

consume either

- the low-diagonal bank `sum_h Z_h>0.65536` with simultaneously tiny physical diagonals and tiny `h-to-J` stars, or
- the high-diagonal dense internal-edge graph (4.16),

without deleting same-bank curvature or selecting a vanishing physical coefficient. The r40 skew-mismatch packet `sum_h ||m_h||^2 W(h)>2/3125` and the r40 overlap-2/principal residual packets remain separate debts.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**. The Z3 branch above proves continuity in its exact scope; the square+Z2 and fleet04/B07 physical-core branches prove essential boundedness only.
