# account01/B19 — heavy-hub compound-energy routing

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Universal proof assembly  
**Run:** 20260923T035138Z-account01-B19-QFORM-r11  
**Control at start:** yspennstate/math-research-brain@d5ab6023976df874d785e6fd308424e1f696d35c, OWNER CONTROL revision 2026-09-22.15  
**Execution:** WITHOUT_VERIFIED_BRAIN  
**Status:** ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL ROUTING LEMMA / FULL TARGET OPEN.

The unrestricted theorem is **not** claimed. Continuity remains separate and open globally. The argument below uses only original-coordinate product structure and matrix identities. It does not rotate the independent law, use arbitrary-joint coarea, condition a projection and then treat it as independent, delete small coefficients, or select one local minor before aggregation.

## 1. Source-pinned inputs

1. **Designated partner account02/B19 r22.** Canonical source `yspennstate/math-open-problems@3a8e3494dac898f3b7180d5b80a8c5eb974a8412`, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T020950Z-account02-B19-QFORM-r22/REPORT.md`. In its two-rank-two-bank geometry, if a bank frame has least positive eigenvalue `g` and a row has normalized leverage `ell_i>1/2`, then the row carries fixed Euclidean spectral mass; its grouped determinant identity is `delta_i=pdet(S_H)(n_H.u_i)^2`, with aggregate lower bound `sum delta_i >= g^2 h eta`. This is used only for the co-heavy input and its exact leverage meaning.

2. **account03/B19 r23 arbitrary-hub theorem.** Canonical source `yspennstate/math-open-problems@80403bc0adff2c5e8278848674c81448e9782e44`, report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T030233Z-account03-B19-QFORM-r23/REPORT.md`. If one ORIGINAL coordinate has star row `m=A[i,-i]`, then for arbitrary diagonal coefficient and arbitrary residual curvature

`sup_z P(|Q-z|<=eps) <= 4*2^(1/4)||m||^(-1/2) sqrt(eps)`.

3. **account03/B06 r24 aggregate-E2 theorem.** Canonical source `yspennstate/math-open-problems@606257652f3c70e90c7b7f80ea7cb76c1abf689b`, report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T011959Z-account03-B06-qform-r24/REPORT.md`. For an original-coordinate cross block `B`, if one cross-range side has coordinate leverage at most `q/2`, `1<=q<3/2`, then the whole quadratic form has an `L^3` density obeying

`||p_Q||_3 <= C3(q) Delta2(B)^(-1/6)`,

where `Delta2(B)=e2(BB^T)` is the complete sum of squared physical `2x2` minors and

`C3(q)=3^(1/6)e^(2/3)/(4q^(1/3)) * Beta(1/4,3/(8q)-1/4)^(2/3)`.

4. **Current completed exact-rank-three pivot theorem.** The live `CURRENT_RESEARCH.md` at the control snapshot records `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`:

`||p_Q||_infinity <=128 [c_i |A_ii| |det M|]^(-1/4)`

for an exact rank-three representation `A=RMR^T`, `R^TR=I_3`, with `c_i=||u_i||^2` and `A_ii!=0`, including arbitrary outside curvature and affine terms.

## 2. New lemma: a small-diagonal heavy row has a fixed aggregate second-gradient packet

Work first with an arbitrary real symmetric matrix `A` satisfying

`s_3(A)>=1`.

Fix a physical coordinate `i`. After relabelling write

`A = [[a,m^T],[m,B]]`,

where `a=A_ii`, `m=A[i,-i]`, and `B=A[-i,-i]`.

Let

`C=A[:, -i]`.

The `i`-th row of `C` is `m^T`; the other rows are the rows `r_j^T` of `B`. If `m!=0`, put `v=m/||m||` and `P=vv^T`.

### Theorem 2.1 — QFORM-HEAVY-HUB-COMPOUND-ENERGY-v1

Define

`W_i := sum_(j!=i) ||m wedge r_j||_2^2`.

Then

`boxed: W_i >= ||m||_2^2.`

#### Proof

Deleting one column is a rank-one compression of `AA^T`, so singular-value interlacing gives

`s_2(C)>=s_3(A)>=1`.

Also

`||C(I-P)||_F^2 = sum_(j!=i) ||r_j(I-P)||_2^2`

because the `i`-th row `m^T` is killed by `I-P`. Since `CP` has rank at most one, Eckart--Young gives

`||C(I-P)||_F^2 = ||C-CP||_F^2 >= sum_(k>=2) s_k(C)^2 >=1`.

Finally

`||m wedge r_j||^2 = ||m||^2 ||r_j(I-P)||^2`.

Summing proves `W_i>=||m||^2`. QED.

This is dimension-free. It says a hub with a nontrivial star cannot have all other residual physical rows aligned with that star when `s_3(A)>=1`.

## 3. Exact overlap/disjoint decomposition and partition capture

Expand each wedge by physical columns. Define

`D_i := sum_(j!=i) sum_(k<l; k,l notin {i,j})
        det A[{i,j},{k,l}]^2`,

and

`O_i := sum_(j!=i) sum_(k notin {i,j})
        (A_ij A_jk - A_ik A_jj)^2`.

The first is the fully disjoint two-gradient packet; the second is the one-column-overlap packet. Every two-column term in `||m wedge r_j||^2` is in exactly one of these classes, hence

`boxed: W_i=D_i+O_i.`

Consequently

`boxed: max(D_i,O_i) >= ||m||^2/2.`

There is also a product-preserving aggregate compiler for the disjoint half. Randomly partition the residual physical indices into `J` and `K`, independently with probability `1/2`. For every term of `D_i` indexed by three distinct residual indices `(j,k,l)`, the event `j in J` and `k,l in K` has probability `1/8`. Therefore some deterministic partition satisfies

`sum_(j in J) sum_(k<l in K)
 det A[{i,j},{k,l}]^2 >= D_i/8`.

For the actual original-coordinate cross block

`B_JK := A[{i} union J, K]`,

Cauchy--Binet gives

`Delta2(B_JK)=e2(B_JK B_JK^T)`

as the sum of squares of all of its physical `2x2` minors. The displayed packet is a subset of that sum. Hence

`boxed: Delta2(B_JK) >= D_i/8.`

No single minor is selected.

## 4. Application to the designated partner's co-heavy state

Now enter the exact-rank-three core

`A=RMR^T`, `R^TR=I_3`, `s_min(M)>=1`.

Take a co-heavy row `u_i` from the partner's rank-two bank `G`, whose frame has least positive eigenvalue `g`. Its normalized leverage is

`ell_i=u_i^T S_G^+ u_i>1/2`.

Since `S_G` has nonzero spectrum at least `g`,

`ell_i <= ||u_i||^2/g`.

Thus, with `c_i=||u_i||^2`,

`boxed: c_i>g/2.`

In the quantitative partner chamber `g>=1/3`, this gives

`c_i>1/6`.

Put `a=A_ii=u_i^T M u_i` and `m=A[i,-i]`.

### 4.1 Large physical diagonal: already paid

If

`|a|>=1/8`,

then the completed exact-rank-three pivot theorem gives, using `|det M|>=1` and `c_i>1/6`,

`||p_Q||_infinity
 <=128(c_i |a| |det M|)^(-1/4)
 <128*48^(1/4)
 =336.914947... <337.`

So every unpaid co-heavy row may be assumed to satisfy `|A_ii|<1/8`.

### 4.2 Small physical diagonal: fixed star and compound energy

The full physical row norm obeys

`a^2+||m||^2
 = ||A[i,:]||^2
 = u_i^T M^2 u_i
 >= ||u_i||^2
 =c_i`,

because `s_min(M)>=1`. Hence in the surviving branch

`||m||^2 > 1/6-1/64 = 29/192`.

Therefore

`boxed: ||m|| > sqrt(29/192)=0.38864079...`.

Applying account03/B19 r23 at the actual inequality gives the uniform target-level small-ball estimate

`boxed:
 sup_z P(|Q-z|<=eps)
 < 4*2^(1/4)*(192/29)^(1/4) sqrt(eps)
 < 7.631 sqrt(eps).`

This uses the genuine original coordinate `X_i`; no effective conditional variable is substituted.

The new compound-energy theorem further gives

`W_i>=29/192`.

Hence either

`boxed: O_i>=29/384`,

or

`boxed: D_i>=29/384`.

In the disjoint alternative the partition compiler yields disjoint original-coordinate banks with

`boxed: Delta2(B_JK) >= 29/3072 = 0.00944010416...`.

This is a fixed aggregate second-gradient resource created before any reciprocal minor selection.

## 5. Actual splice to account03/B06 r24

Suppose the partitioned cross block from Section 4 has, on at least one side, maximum cross-range coordinate leverage at most `2/3`. Take `q=4/3` in `QFORM-CROSS-E2-FRACTIONAL-L3-v1`. Then

`C3(4/3)=5.7514292817...`,

and the preceding lower bound gives

`||p_Q||_3
 <= C3(4/3)*(29/3072)^(-1/6)
 <12.511.`

If one side is actually diffuse at leverage at most `1/2`, the sharper `q=1` value is

`boxed: ||p_Q||_3 <6.490.`

Thus the small-diagonal co-heavy state can no longer be treated as having only a single `sqrt(eps)` star resource: unless the one-overlap packet is already macroscopically large, it contains a constant aggregate E2 cross block, and unless both sides of every such captured block are themselves co-heavy beyond `2/3`, the whole target law already has a universal `L^3` density.

This is an actual application of the completed other-account B06 theorem to the new inequality; its conclusion is deliberately recorded as `L^3`, not enlarged to `L^infinity`.

## 6. Compact conditional end-to-end route

At the current proof frontier, the broad route can be stated as follows.

* Existing global reductions pay the low-offdiagonal, ridge-diffuse, quantitative physical-pivot, exact-null-coloop, rank-two cross plus genuine square, and several grouped-coordinate branches.
* account02/B19 r22 reduces its two-rank-two survivor to internally co-heavy rows or paid grouped exits.
* For any such co-heavy row, the present run pays `|A_ii|>=1/8` outright by `<337`.
* If `|A_ii|<1/8`, account03/B19 r23 gives `<7.631 sqrt(eps)` and the present theorem forces at least `29/384` of incident compound energy into either O1 overlap or fully disjoint O2 energy.
* In the disjoint half a deterministic physical partition captures `Delta2>=29/3072`; account03/B06 r24 then gives `L^3<12.511` whenever one side is not more than `2/3`-co-heavy.

Therefore the first essential missing implication on this route is now

`QFORM-HEAVY-HUB-INCIDENT-E2-TO-LINFINITY-v1`:

> In the small-diagonal heavy-hub state, convert either the fixed O1 packet `O_i>=29/384`, or the fixed disjoint aggregate `Delta2>=29/3072` together with the existing hub smoothing, into a universal `L^infinity` bound. In the latter branch the only unhandled localization case is that every usable aggregate-E2 partition is co-heavy above `2/3` on both cross-range sides. The transducer must remain in original coordinates and retain arbitrary same-bank curvature and extra spectrum.

This is strictly narrower than seeking a second fixed physical minor: the new theorem proves a constant aggregate packet and identifies precisely where localization, rather than absence of curvature, is the debt.

## 7. Continuity and correction boundary

No continuity statement is proved here. The new `sqrt(eps)` and `L^3` conclusions establish regularity weaker than a bounded continuous density. All signs of `M`, all degeneracies of physical subblocks, and arbitrary cap-one marginal laws are allowed within the stated exact-rank-three scope.

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.
