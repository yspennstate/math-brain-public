# fleet04/B18 — visible/hidden mixed-curvature split for the adaptive FEI reduction

**Run:** `20260922T081002Z-b18-fei-r22`  
**Classification:** `ESSENTIAL_STEP_APPLIED / A-B_INTERFACE_INTEGRATION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim.

## 0. Exact scope and source compatibility

This report integrates the candidate-independent adaptive restriction theorem of fleet04/B14 with the exact mixed-curvature law previously proved by fleet04/B18.  The point is to identify exactly which part of the old derivative-depth bank is already paid by interface A's posterior-crossing refund and which part remains genuinely unpaid.

The universal inputs actually used are:

1. fleet01/B18, `20260921T1856Z-curvature-refunded-crossing/REPORT.md`: with folded influences `q_i<=1/2`, phase potential `P=sum_i j(q_i)`, corrected entropy `F=H-P`, singleton posterior crossings `c_j({i})`, and `W_i=sum_{j!=i} j'(q_j)c_j({i})`, a critical core of ratio `rho=F/J` obeys the all-block curvature/crossing inequalities and, in particular,
   
   `sum_i sum_{j!=i} (rho+j'(q_j)) c_j({i}) <= P-DTC(X)`.

2. fleet04/B14, `20260922T071120Z-criticality-matched-stopping/REPORT.md`: the realizable physical policy querying `i` when
   
   `h_2(q_i)-W_i < K(q_i+C_i)`
   
   satisfies `F(root)-E F(leaf) <= K[J(root)-E J(leaf)]`.  Every `F/J`-critical core of ratio `rho` is terminal at `K=rho`, and hence at every smaller `K`.

3. fleet04/B18, `20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`: for derivative rows `g_j=D_j f`, support-boundary probabilities `p_{ji}`, opposite-sign overlaps `o_{ji}`, mixed curvature `kappa_{ji}`, and row depth `d_j`,
   
   `kappa_{ji}=p_{ji}+4o_{ji}=kappa_{ij}` and `sum_{i!=j} kappa_{ji}=4d_j`.
   
   If every normalized depth defect is zero, Boolean integrability classifies `f` as a character times a signed one-point defect (irrelevant variables allowed), and then `H<4J`.

The newest fleet01/B18 `121` MUX boundary layer, fleet04/B12 Holevo/slack-starvation collar, and fleet04/B13 MUX center-crossing tube were also read source-exactly.  They are fixed-`Gamma^dagger` / prime-gate statements.  The current source correction says that fixed `Gamma^dagger` is globally refuted as a universal all-gate potential, so those results are retained as family-specific exclusions and are **not** spent as universal currency in the candidate-independent A/B argument below.

No `sum_j d_j=O(J)` assumption is made.

## 1. Ordered singleton crossing versus one mixed derivative

Median-center the current Boolean state, so every remaining folded influence satisfies

`q_j = Inf_j(f) <= 1/2`.

Let `eta_j` be the pivotality indicator of coordinate `j`.  For distinct `i,j`, write

`a = E[eta_j | x_i=0]`, `b = E[eta_j | x_i=1]`.

Then `(a+b)/2=q_j<=1/2`.  The singleton posterior crossing from revealing `i` into survivor `j` is

`c_{j<-i}:=c_j({i}) = (1/2)[(2a-1)_+ + (2b-1)_+]`.

### Lemma 1.1 — crossing is at most half the support boundary

For every ordered pair `i!=j`,

`2 c_{j<-i} <= |a-b| <= p_{ji} <= kappa_{ji}`.

#### Proof

Since `a+b<=1`, at most one of `a,b` can exceed `1/2`.  If neither does, `c_{j<-i}=0`.  If, say, `b>1/2`, then

`c_{j<-i}=b-1/2`.

The constraint `a+b<=1` gives `a<=1-b`, hence

`b-a >= 2b-1 = 2c_{j<-i}`.

This proves the first inequality.  For the second,

`|a-b| = |E[eta_j(0,x_-)-eta_j(1,x_-)]| <= E |eta_j(0,x_-)-eta_j(1,x_-)|`.

The last expectation is exactly the support-disagreement probability `p_{ji}` of the derivative row `g_j` in direction `i`.  Finally `p_{ji}<=p_{ji}+4o_{ji}=kappa_{ji}`.  QED.

This is the exact local bridge between interface A's posterior crossing and interface B's mixed derivative.

## 2. Exact visible/hidden decomposition of mixed curvature

Define the nonnegative **hidden mixed-curvature remainder**

`omega_{ji}:=p_{ji}-2c_{j<-i}+4o_{ji} >= 0`.

Lemma 1.1 and the mixed-curvature identity give the exact ordered-pair decomposition

`boxed(kappa_{ji} = 2c_{j<-i} + omega_{ji}).`

Thus mixed curvature has two source-exact parts:

* `2c_{j<-i}` — the part visible to the actual physical posterior-crossing refund;
* `omega_{ji}` — support boundary that does **not** force a posterior majority crossing, plus all opposite-sign overlap.

In particular, the parity/orientation obstruction is retained: if `p_{ji}=0` but `o_{ji}>0`, then the whole contribution is hidden rather than being silently dropped.

For each derivative row set

`C^in_j := sum_{i!=j} c_{j<-i}`,
`Omega_j := sum_{i!=j} omega_{ji}`.

Summing the ordered-pair identity over `i` and using `sum_i kappa_{ji}=4d_j` gives the exact row law

`boxed(4d_j = 2 C^in_j + Omega_j).`  (2.1)

This sharpens the one-sided estimate `C^in_j<=2d_j`: it tells us precisely what that estimate discards.

## 3. Critical cores: interface A already pays the visible part

For `K>2`, define

`S_K := sum_j (K+j'(q_j)) C^in_j`

and

`U_K := sum_j (K+j'(q_j)) Omega_j`.

Weighting (2.1) by `K+j'(q_j)` gives the exact identity

`boxed(4 sum_j (K+j'(q_j)) d_j = 2S_K + U_K).`  (3.1)

Now let the centered state be an `F/J`-critical core of ratio `rho>=K`.  The fleet01/B18 fixed-cardinality curvature theorem gives

`S_rho <= P-DTC(X)`.

Because every crossing is nonnegative and `rho>=K`,

`S_K <= S_rho <= P-DTC(X).`  (3.2)

Also `j'(q_j)>=0`, so the left side of (3.1) is at least `4K sum_j d_j`.  Combining (3.1)-(3.2) yields the new depth reduction

`boxed(sum_j d_j <= [P-DTC(X)]/(2K) + U_K/(4K).)`  (3.3)

This is the central integration statement.  The old unpaid bank `sum_j d_j` is **not** declared `O(J)`.  Instead it is split into:

1. a visible part already paid by the existing phase/crossing bank `P-DTC(X)`; and
2. one explicit nonnegative hidden-curvature remainder `U_K`.

Since the source proves `DTC(X)<=P` and `P<=(2/ln 2)J`, the first term in (3.3) is dimension-free and already paid.  No crossing credit is spent twice.

## 4. The natural FEI target K=4

The candidate-independent B14 compiler says that proving `F<=4J` on its `K=4` terminal class would yield

`H <= (4+2/ln 2) J <= (4+2/ln 2) I`.

Assume toward a contradiction that `F<=4J` fails, and choose a centered physical-restriction descendant maximizing `rho=F/J`.  Then `rho>4`; by fleet04/B14 it is automatically terminal for the `K=4` adaptive selector.

Apply (3.3) with `K=4`:

`boxed(sum_j d_j <= [P-DTC(X)]/8 + U_4/16).`  (4.1)

The exact all-row zero-depth endpoint cannot be this obstruction.  Indeed, if every normalized depth defect is zero, the fleet04/B18 rigidity theorem gives a character-twisted one-point defect with `H<4J`, hence `F<4J`, contradicting `rho>4`.

Therefore every genuine `K=4` critical obstruction lies in the positive-defect branch, while (4.1) says that its **crossing-visible** mixed-curvature depth is already paid.

## 5. Consequence for the existing robust near-subcube elimination theorem

The previous fleet04/B18 robust-row theorem proves, at relative near-subcube error at most `1/16`, that for any family `G` of such derivative rows at one Boolean state,

`sum_{j in G} R_j^ent < 13.348 sum_k d_k`,

where `R_j^ent` is the corresponding restriction-entropy decrement.  Combining with (4.1) gives

`boxed(sum_{j in G} R_j^ent
 < (13.348/8)[P-DTC(X)] + (13.348/16)U_4).`  (5.1)

Using `P<=(2/ln2)J`,

`boxed(sum_{j in G} R_j^ent < 4.814274 J + 0.83425 U_4).`  (5.2)

Thus the entire old second-factorial-moment obstruction has been reduced, on a `K=4` critical state, to one **explicit hidden-curvature** remainder.  The portion seen by actual singleton posterior crossings is already dimension-free.

For exact-subcube derivative rows, the sharper source estimate `sum R_j^ent <=8 sum d_k` gives

`boxed(sum_{j in G} R_j^ent <= P-DTC(X) + (1/2)U_4
 <= (2/ln2)J + (1/2)U_4).`  (5.3)

No finite check is needed for (5.1)-(5.3); they follow analytically from the exact ordered-pair decomposition and already-proved source inequalities.

## 6. Smallest honest universal chain after this run

A candidate-independent contradiction proof with the currently paid arrows can now be written compactly:

1. If `F<=4J` holds, B14 immediately gives FEI with constant `4+2/ln2`.
2. Otherwise choose a centered `F/J`-critical physical descendant with `rho>4`; it is a `K=4` terminal state.
3. The all-row zero-depth branch is already classified and has `F<4J`, so the obstruction must have positive depth defect somewhere.
4. For every ordered pair, mixed curvature splits exactly as
   
   `kappa_{ji}=2c_{j<-i}+omega_{ji}`.
5. The whole crossing-visible component is already paid by fleet01/B18's `P-DTC` bank; consequently (4.1) replaces the old raw `sum d_j` bank by the paid phase term plus `U_4`.
6. Robust near-subcube rows therefore cost only the already-paid dimension-free term plus `0.83425 U_4` as in (5.2).

### Unpaid arrows — kept explicit

**U1. Hidden-curvature payment.**  Prove a dimension-free payment for

`U_4 = sum_{i!=j} (4+j'(q_j))[p_{ji}-2c_j({i})+4o_{ji}]`

on positive-defect `K=4` terminal critical cores, or construct a realizable selector/classification that eliminates exactly the states where this bank is large.  The opposite-sign term must remain; the unsigned support bank is known to be insufficient.

**U2. Nonrobust positive-defect rows.**  The `13.348` theorem only covers derivative rows in its inherited relative-`1/16` near-subcube regime.  Rows outside that regime still need a source-valid entropy payment or a stability reduction into U1.  They are not silently absorbed into (5.2).

These are genuine remaining arrows.  In particular, this report does **not** claim `U_4=O(J)`, does not claim `sum d_j=O(J)`, and does not promote the fixed-`Gamma^dagger` MUX/collar results into a universal proof.

## 7. Relation to the freshest B12-B14 / fleet01-B18 results

* **fleet01/B18 newest MUX-121 result:** retained exactly at its fixed-candidate scope.  It enlarges a deterministic-data boundary layer but cannot be inserted into the universal candidate-independent chain after the fixed `Gamma^dagger` counterexample.
* **fleet04/B12 newest Holevo/slack-starvation result:** likewise retained at the fixed-candidate, balanced-child all-gate scope; its child-slack starvation is not identified with derivative depth `d_j` here.
* **fleet04/B13 newest completed MUX tube:** retained as a family-specific prime-gate exclusion; no ambient-dimension continuity factor is imported.
* **fleet04/B14 newest stopping theorem:** used directly and without modification.  It is the realizable adaptive A-interface step that makes `K=4` terminal cores the correct candidate-independent target.

This compatibility separation prevents a conditional or refuted fixed-potential input from being counted as unconditional FEI closure.

## 8. Preserved exclusions and status

Preserved exactly:

* prescribed-coordinate Shannon payment is false;
* fixed-relative near-subcube tolerance is false;
* `sum d_j=O(J)` is not assumed;
* the opposite-sign `4o_{ji}` curvature mode is retained;
* the fixed `Gamma^dagger` universal all-gate candidate is refuted and is not revived;
* the exact all-row zero-defect classification remains a character-twisted one-point defect with `H<4J`;
* no conditional input has been converted into unconditional full FEI.

**Full uniform-cube FEI remains OPEN / NOT PROVED.**
