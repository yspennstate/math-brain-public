# B15 — exact product-collision law for the arithmetic remainder; unrestricted subadditivity is false

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval/context was used in this mathematics.  
**Role:** FEI spectral remainder proof.  
**Run:** 2026-09-21T11:01:18Z, fleet02/B15.

## 0. What moved

The inherited packet decomposition groups each distinct nonzero Fourier magnitude `a` into a packet `A_a`, with spectral mass

`p_a=|A_a| a^2`, signed mask `V_a=sum_{S in A_a} sign(fhat(S)) chi_S`, valuation

`r_a=min_{x:V_a(x)!=0} nu_2(V_a(x))`, physical mesh `b_a=a 2^{r_a}<=1`, and arithmetic remainder

`D(f)=sum_a p_a log2(1/b_a)`.

The previous B15 run rewrote `2D` as a packet free energy with an essential negative KL credit. A concurrent fleet03/B15 run then rigorously refuted the raw residual-normalizer target even at fixed strong bias by punctured subcubes. This run changes method: instead of trying to pay `D` packetwise, it asks how `D` behaves under the most basic FEI stress operation, disjoint product.

The result is an **exact collision formula valid for arbitrary packets**, followed by a small exact Boolean counterexample showing that `D` is **not** subadditive under unrestricted disjoint products. The formula identifies the precise debit and the precise negative cancellation credit. This closes a false route and gives a sharper object for any composition-based arithmetic proof.

Creative moves used: **#25 count the same quantity twice** (compute product `D` before and after collision grouping), **#20 find why the algorithm fails** (locate the exact failure of unrestricted tensor subadditivity), and **#30 one scale/direction at a time** (isolate each product-magnitude collision class).

Tracked full target `sup_f D(f)/I(f)` remains **UNKNOWN** before and after. Full FEI remains OPEN.

## 1. Exact product-collision valuation law

Let `f` and `g` be Boolean functions on disjoint variable blocks. Use `a` for a nonzero magnitude of `f` and `c` for a nonzero magnitude of `g`. Write their packet data as

`(p_a,r_a,b_a)` and `(q_c,s_c,d_c)`, where `b_a=a 2^{r_a}` and `d_c=c 2^{s_c}`.

For a product magnitude `z`, define

`C_z={(a,c): ac=z}`.

The Fourier labels belonging to different pairs in `C_z` are disjoint Cartesian sets, so the squared mass of the output `z`-packet is exactly

`P_z=sum_{(a,c) in C_z} p_a q_c`.                                      (1)

Its signed mask is

`U_z(x,y)=sum_{ac=z} V_a(x) W_c(y)`,                                  (2)

and let

`R_z=min_{U_z(x,y)!=0} nu_2(U_z(x,y))`.                                (3)

Each summand in (2) is divisible by `2^{r_a+s_c}`, hence

`R_z >= m_z := min_{ac=z}(r_a+s_c)`.                                  (4)

### Theorem B15-PRODUCT-COLLISION-01

For every pair of Boolean functions on disjoint blocks,

`D(fg)-D(f)-D(g)`

`= sum_z sum_{ac=z} p_a q_c [(r_a+s_c)-R_z]`.                          (5)

Equivalently, if

`rbar_z=(1/P_z) sum_{ac=z} p_a q_c(r_a+s_c)`,

then

`D(fg)-D(f)-D(g)=sum_z P_z(rbar_z-R_z)`                               (6)

`=sum_z P_z[(rbar_z-m_z)-(R_z-m_z)].`                                 (7)

The first bracket in (7) is a nonnegative **valuation-spread debit** created when unequal packet valuations collide at the same product magnitude. The second is a nonnegative **2-adic cancellation credit** created when the collided signed mask gains extra pointwise divisibility.

#### Proof

The output remainder is

`D(fg)=sum_z P_z log2(1/(z 2^{R_z}))`.

Because the input packet masses productize,

`D(f)+D(g)`

`=sum_{a,c} p_a q_c [log2(1/(a2^{r_a}))+log2(1/(c2^{s_c}))]`

`=sum_z sum_{ac=z} p_a q_c log2(1/(z2^{r_a+s_c}))`.

Subtracting, the `log2(1/z)` terms cancel exactly, leaving (5). Equations (6)-(7) are regroupings, and (4) proves both credits in (7) have the stated signs. QED.

### Consequences

1. **No collisions:** if every product magnitude `z` has one representation `ac`, then `U_z=V_aW_c`, so `R_z=r_a+s_c`; hence `D(fg)=D(f)+D(g)`.

2. **Collision-isovaluative criterion:** if `r_a+s_c` is constant over every collision class `C_z`, then (4) gives `R_z` at least that common value, and therefore

`D(fg)<=D(f)+D(g)`.                                                    (8)

This strictly contains the previous B15 common-mesh sufficient condition: common packet mesh in each factor forces the sum valuation to be constant inside every product-magnitude collision class.

3. In general the sign of (5) is not fixed. Product collisions can increase `D` when the weighted valuation spread is larger than the cancellation lift. Therefore an unrestricted proof of FEI cannot silently tensorize the arithmetic remainder.

## 2. Exact Boolean counterexample to unrestricted subadditivity

Use the normalized Walsh convention on `F_2^n`, `chi_S(x)=(-1)^{S dot x}`. Define `f:F_2^3->{-1,1}` by the truth vector, in binary index order `000,001,...,111`,

`f=(-1,+1,-1,-1,+1,-1,-1,+1)`.

Its unnormalized Walsh vector is

`(-2,-2,+2,+2,-2,-2,+2,-6)`.

Thus it has exactly two magnitude packets:

| magnitude | packet mass | valuation r | physical mesh |
|---|---:|---:|---:|
| `1/4` | `7/16` | `0` | `1/4` |
| `3/4` | `9/16` | `0` | `3/4` |

Now define `g:F_2^4->{-1,1}` by

`g=(-1,-1,+1,+1,-1,+1,+1,+1,+1,-1,+1,+1,-1,+1,+1,+1)`.

Its unnormalized Walsh vector is

`(6,-2,-10,-2,-2,6,-2,6,-2,-2,-2,-2,-2,-2,-2,-2)`.

Its packets are

| magnitude | packet mass | valuation s | physical mesh |
|---|---:|---:|---:|
| `1/8` | `3/16` | `2` | `1/2` |
| `3/8` | `27/64` | `0` | `3/8` |
| `5/8` | `25/64` | `0` | `5/8` |

There is exactly one product-magnitude collision:

`(1/4)(3/8)=(3/4)(1/8)=3/32`.

The two tuple valuations and masses in that collision are

- valuation `0+0=0`, mass `(7/16)(27/64)=189/1024`;
- valuation `0+2=2`, mass `(9/16)(3/16)=27/256`.

The actual collided output packet has valuation

`R_{3/32}=0`.

Every other product magnitude has a unique representation and therefore contributes zero to (5). Consequently

`D(fg)-D(f)-D(g)=(27/256)*2=27/128>0`.                                (9)

So unrestricted product subadditivity is **false**, already for a 3-variable factor times a 4-variable factor.

Numerically,

`D(f)=1.1084585933443496`,

`D(g)=1.0493407829428862`,

`D(fg)=2.3687368762872363`,

and the difference is exactly `27/128=0.2109375`.

The finite checker beside this report reconstructs the integer Walsh transforms, packet masses and valuations and verifies the exact rational excess. The theorem itself is analytic and does not depend on the checker.

## 3. Why this matters for the full arithmetic route

The inherited equality is

`H(f)=2 sum_a p_a r_a + 2D(f)`.                                      (10)

For disjoint products, Fourier entropy and total influence tensorize exactly. Therefore any positive collision increment in `D` must be matched by an equal negative increment in the valuation contribution `sum p r`; this is also immediate by subtracting (10) for the two factors from (10) for their product.

Thus the previously convenient split

`H <= 4 Ifrak + 2D`

can lose a real negative credit when product collisions move mass from the valuation term into `D`. The exact law (5) says the relevant arithmetic object is not merely `D` in isolation: it is `D` together with the collision-induced valuation transfer. This is independent of the separate negative KL credit in the packet free-energy identity; both credits can be large and both must be preserved by a full-scope proof.

This also explains why the five-variable common-mesh obstruction from the previous run behaved well under tensor powers: its collision classes are isovaluative, so the spread debit vanishes. The present example shows that this favorable behavior is not universal.

## 4. Relation to the concurrent fleet and preserved dead routes

- B14 owns restriction-critical / erasure-heavy descendants; this report does not re-prove that route.
- B16 owns signed physical transport and oriented/cut payments; this report uses only packet valuations under disjoint products.
- B18 owns product-marginal total-correlation / phase stability; this report does not use the product-law approximation `Q` or its Hellinger/KL estimates.
- Concurrent fleet03/B15 has already refuted the previous raw `v log N_perp` target by punctured subcubes and shown that its negative KL term cancels the apparent linear divergence. That obstruction is preserved here.

The new exact obstruction is separate: even when no raw normalizer is dropped, the arithmetic remainder itself is not tensor-subadditive unless collision valuations line up or cancellation is strong enough.

## 5. Literature check and priority status

A current search rechecked the 2026 González--MacManus--Pereyra stopping-tree paper (arXiv:2606.00246), the 18 September 2026 Potapov plateaued-function paper (arXiv:2609.21563), Han's general influence-profile upper bound, and the O'Donnell--Tan composition theorem. Those sources concern FEI/restriction/composition at the Fourier-entropy level; this run makes **no novelty or publication-priority claim** for the packet-valuation identity (5), which is elementary once the project-specific remainder is defined. Potapov's plateaued result is retained as prior art for the structured class and is not being re-announced as unrestricted FEI.

Priority status: **UNVERIFIED / NO CLAIM**. Full FEI status: **OPEN**.

## 6. Before / after / next exact obligation

**Before:** B15 had an exact free-energy identity for `D`, a common-mesh product subadditivity theorem, and a now-refuted raw residual-normalizer shortcut. It was unknown whether the favorable product behavior reflected a general tensor principle.

**After:** arbitrary disjoint products satisfy the exact collision law (5)-(7), and unrestricted subadditivity is rigorously refuted by the exact 3-by-4-variable example (9). The only source of product nonadditivity is now localized to a signed integer quantity: **mass-weighted input valuation spread minus output cancellation lift inside equal-product-magnitude collision classes**.

**Remaining universal obligation:** control that collision debit together with the already-paid centroid/valuation term, rather than bounding `D` after discarding the transfer. A concrete next target is a dimension-free inequality that charges

`sum_z P_z (rbar_z-m_z)`

against either the output cancellation credit `sum_z P_z(R_z-m_z)` or the genuine influence/centroid slack lost when the valuation term drops. Proving such a charge for arbitrary Boolean product/composition steps would give a composition-stable arithmetic potential; a family with unbounded debit relative to all available influence slack would kill this refined route.
