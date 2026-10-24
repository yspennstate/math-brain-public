SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T18:30:23Z.
attacking: turn partner r40's anchored cofactor bank into the exact projected-crossing currency of a product-weighted one-hub receiver, then classify failure of its row gate without taking any worst conditional fiber supremum.

# account02/B06 — anchored cofactor gives projected crossing: logarithmic receiver or two new physical wedge hubs

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `b06-20260923T183023Z-a02r11`  
**Status:** `NEW SUPPORTING STRUCTURAL/ANALYTIC LEMMA + ROUTE COUNTEREXAMPLE PAID AFTER THIRD DISJOINT SQUARE / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains OPEN: arbitrary independent ORIGINAL real coordinates with one-dimensional densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and a universal essential density bound for `X^T A X`.  No moment, support, iid, log-concavity, diagonal-basis, post-rotation independence, or continuity assumption is added.

## 1. Source-valid inputs actually used

Fresh owner control is revision `2026-09-22.15`; the current owner continuation is `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.  The newest compatible designated partner is account03/B06 r40,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T171937Z-account03-B06-qform-r40/REPORT.md`,

read on current `math-open-problems` master.  In its live low-disjointness / ultra-thin branch it produces ORIGINAL anchors `i in J`, `a in K` and, after writing the complete physical cross block as

`N = [[b, r^T], [c, D]]`,                                               (1.1)

it proves

`Z_ia := ||b D - c r^T||_F^2
      > z0 := 4395076119/2748779069440
      = 0.0015989193776476895...`,                                     (1.2)

while the small-mutual-edge survivor has `|b|<1/32` and

`||r||, ||c|| > 0.07593224`.                                           (1.3)

Every entry of `D`, both same-bank blocks, and all extra spectrum remain present.

The current completed analytic receiver used below is Proposition 6.6 of

`math-open-problems@c4c23b784395630c094ba299a50712209921d1ae:proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`.

For one physical hub `X_h`, light product variables `X'`, partner `L=<w,X'>`, a light split `I,J`, and arbitrary quadratic remainder `R`, put

`C=(A_R)_{I,J}(Id-Pi_{w_J})`, `F=||C||_F`.                              (1.4)

If `w_J != 0`, `F>0`, and every row `c_i` of `C` has `||c_i||^2 <= F^2/2`, Proposition 6.6 gives, for arbitrary hub diagonal and affine terms,

`|phi_Q(eta)| <= 2 pi (||w_J|| F)^(-1/2) |eta|^(-1)`,                  (1.5)

and for every `s` and `delta>0`,

`P(|Q-s|<=delta)
 <= pi^2 (||w_J|| F)^(-1/2) delta
    [1 + log_+((||w_J|| F)^(1/2)/(4 delta))].`                         (1.6)

This is a weighted product-structure statement: the quadratic remainder is arbitrary and the conditional fiber singularity is integrated rather than maximized.

The owner-required pinned package

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was re-read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.  Its completed localized three-coordinate Theorem A is applied in Section 6 to a genuine target repair of the obstruction found here.

## 2. Exact cofactor-to-projected-crossing identity

Use `i` as the physical hub.  The remaining ORIGINAL coordinates are

`I = J\{i}` and `J' = {a} union (K\{a})`.                              (2.1)

The restriction of the hub partner to `J'` is the literal vector

`w = (b,r)`,                                                           (2.2)

and the crossing block of the hub-free remainder from `I` to `J'` is

`A_0 = [c  D]`.                                                        (2.3)

Let `Pi_w` be orthogonal projection onto `span(w)`, and set

`C_L = A_0 (Id-Pi_w)`, `F_L=||C_L||_F`.                               (2.4)

For a row `a_j=(c_j,D_{j,*})`, Lagrange's identity gives

`||w||^2 ||a_j(Id-Pi_w)||^2
 = ||w||^2||a_j||^2-<w,a_j>^2
 = sum_{u<v}(w_u a_{jv}-w_v a_{ju})^2.`                               (2.5)

Summing in `j` and retaining only the coordinate pairs consisting of the distinguished `a`-coordinate and one `K\{a}` coordinate gives

`||w||^2 F_L^2
 >= sum_{j,beta} (b D_{j beta}-c_j r_beta)^2
 = Z_ia.`                                                             (2.6)

Thus

`boxed: ||w|| F_L >= sqrt(Z_ia).`                                     (2.7)

Nothing probabilistic and no truncation enters (2.7); it is an exact physical-coordinate exterior-product identity.

There is a symmetric orientation.  Use `a` as hub, split the remaining coordinates as `K\{a}` versus `{i} union (J\{i})`, put

`w'=(b,c)`, `A_0'=[r  D^T]`, `C_R=A_0'(Id-Pi_{w'})`, `F_R=||C_R||_F`. (2.8)

The same calculation yields

`boxed: ||w'|| F_R >= sqrt(Z_ia).`                                    (2.9)

This is the main new deterministic bridge: partner r40's anchored cofactor bank is *already* a lower bound for the product `hub partner norm x projected crossing norm` required by the current one-hub weighted receiver.

## 3. Balanced projected crossing gives a quantitative logarithmic small-ball receiver

### Theorem 3.1 — `QFORM-ANCHOR-COFACTOR-BALANCED-LOG-v1`

In the setup (1.1), suppose in at least one orientation, say (2.4), that

`max_j ||(C_L)_{j,*}||^2 <= F_L^2/2`.                                 (3.1)

Then, retaining arbitrary same-bank curvature, arbitrary affine terms, the complete cross tail `D`, and every extra eigenvalue,

`boxed: |phi_Q(eta)| <= 2 pi Z_ia^(-1/4) |eta|^(-1).`                  (3.2)

Moreover, for every `s` and `delta>0`,

`boxed:
P(|Q-s|<=delta)
 <= pi^2 Z_ia^(-1/4) delta
    [1+log_+(Z_ia^(1/4)/(4 delta))].`                                  (3.3)

#### Proof

Apply current Claude Proposition 6.6 with physical hub `i`, full partner `L` given by the entire `i`th row outside `i`, and the light split (2.1).  Its `w_J` is exactly (2.2), and its projected crossing is exactly (2.4).  Equations (1.5)-(1.6) apply.

By (2.7), `q:=||w||F_L >= sqrt(Z_ia)`.  Equation (3.2) is immediate.  For (3.3), for fixed `delta` the function

`g(q)=q^(-1/2)[1+log_+(q^(1/2)/(4delta))]`                             (3.4)

is nonincreasing on `(0,infinity)`: below the logarithmic threshold it is `q^(-1/2)`, and above it, after writing `y=sqrt(q)`, the derivative of `(1+log(y/(4delta)))/y` is `-log(y/(4delta))/y^2`.  Hence replacing `q` by its lower bound `sqrt(Z_ia)` is valid. QED.

The same conclusion holds if the symmetric orientation (2.8) satisfies its row gate.

### Partner r40 at an actual inequality

Using (1.2),

`z0^(1/4)=0.19996622199530173...`,
`z0^(-1/4)=5.000844592760748...`.                                     (3.5)

Therefore the balanced subbranch of the actual partner r40 packet satisfies

`boxed: |phi_Q(eta)| < 31.421234 |eta|^(-1)`,                         (3.6)

and

`boxed:
P(|Q-s|<=delta)
 < 49.356358 delta [1+log_+(0.04999156/delta)]`                        (3.7)

for every `s,delta>0`.

This does not yet imply a bounded density; the logarithm is recorded honestly.  It is nevertheless a dimension-free all-level estimate that consumes the *entire* anchored cofactor bank before any local reciprocal minor is selected.

## 4. Failure of the row gate creates a new literal physical wedge hub

The row gate itself has a source-valid interpretation.

### Theorem 4.1 — `QFORM-COFACTOR-LOG-OR-WEDGE-HUB-v1`

For either orientation in Section 2, either the balanced logarithmic receiver (3.2)-(3.3) applies, or there is one ORIGINAL coordinate on the opposite side whose coefficient row has exterior-product norm at least

`boxed: ||w wedge a_j|| > sqrt(Z_ia/2).`                               (4.1)

If both orientations fail their row gate, there exist one `j in J\{i}` and one `beta in K\{a}` such that

`||(b,r) wedge (c_j,D_{j,*})|| > sqrt(Z_ia/2)`,                        (4.2)

`||(b,c) wedge (r_beta,D_{*,beta})|| > sqrt(Z_ia/2)`.                  (4.3)

#### Proof

If (3.1) fails, some row obeys `||C_j||>F_L/sqrt(2)`.  Because `C_j` is the component of `a_j` orthogonal to `w`,

`||w wedge a_j||=||w|| ||C_j||
 > ||w||F_L/sqrt(2)
 >= sqrt(Z_ia/2)`                                                      (4.4)

by (2.7).  The right orientation is identical. QED.

On the live r40 packet, (1.2) turns (4.1) into the explicit dimension-free certificate

`boxed: ||w wedge a_j|| > 0.02827471819... .}`                         (4.5)

So the remaining failure is no longer “the projected crossing is too concentrated” in an abstract weighted law.  It is localized to at most one new physical row on each side, each carrying a fixed exterior-product currency with the corresponding anchor partner.

## 5. The row gate cannot simply be deleted: exact logarithmic obstruction

A natural stronger claim would be that the cofactor lower bound `Z_ia>=z>0` by itself forces bounded density.  This is false even with `z=1`.

Let `X,Y,U,V` be independent `Unif[-1/2,1/2]` and

`Q_0=(X+U)^2-(Y+V)^2`.                                                 (5.1)

Use the physical cut `J={X,Y}`, `K={V,U}` and anchors `i=X`, `a=V`.  Then

`N=[[0,1],[-1,0]]`,                                                    (5.2)

so `b=0`, `r=1`, `c=-1`, `D=0` and

`Z_ia=|bD-cr|^2=1`.                                                    (5.3)

In the left orientation `w=(0,1)` and the single projected row is `(-1,0)`, so its row share is exactly one; the right orientation is identical.  Thus both row gates fail maximally and (4.2)-(4.3) are sharp in their qualitative form.

The output density is unbounded.  Put `S=X+U`, `T=Y+V`.  They are independent with triangular density `g(t)=1-|t|` on `[-1,1]`.  Let

`P=S-T`, `R=S+T`; then `Q_0=PR`, and the joint density of `(P,R)` is

`h(p,r)=(1/2) g((p+r)/2) g((r-p)/2)`.                                 (5.4)

On `|p|,|r|<=1/2`, `h>=1/8`.  For `0<q<1/64`, the product-density formula therefore gives

`p_{Q_0}(q)
 >= (1/8) int_{2 sqrt(q)}^{1/2} dp/p
 = (1/8) log(1/(4 sqrt(q))) -> infinity.`                             (5.5)

The matrix of (5.1) has only the two nonzero eigenvalues `+2,-2`, so this is **not** a counterexample to QFORM.  It proves that the third spectral resource is genuinely necessary for upgrading the cofactor/logarithmic endpoint to bounded density.

## 6. The owner-required pinned result pays the obstruction after a genuine third disjoint square

Add a fifth independent cap-one coordinate `Z` and set

`Q_*=(X+U)^2-(Y+V)^2+Z^2`.                                            (6.1)

Its ORIGINAL matrix has nonzero spectrum

`{2,-2,1}`,                                                           (6.2)

so (6.1) is an exact QFORM-target family.

Now define the *disjoint-bank* grouped variables

`S=X+U`, `T=Y+V`.                                                      (6.3)

This is not a spectral rotation: `S,T,Z` are functions of disjoint sets of ORIGINAL independent coordinates, hence are genuinely independent.  Their densities remain bounded by one because convolution preserves the cap:

`||f_X*f_U||_inf <= ||f_X||_inf ||f_U||_1 <=1`,                       (6.4)

and likewise for `T`.

Therefore

`Q_*=S^2-T^2+Z^2`                                                      (6.5)

is a literal three-variable independent cap-one quadratic form with matrix `diag(1,-1,1)`.  Apply the completed **Theorem A** from the owner-required pinned

`e5f71d79eff325201dd0274053d20268ce65b837:.../COUNTEREXAMPLE_SEARCH.md`.

Its `n=3`, `sigma=1` bound gives the real all-level inequality

`boxed: ||p_{Q_*}||_infinity <= 6 sqrt(pi)
       =10.6347231054... .}`                                          (6.6)

Thus the exact heavy-row/cofactor obstruction is repaired once the third direction is supplied in a genuinely product-preserving way.  The unresolved issue in the live r40 branch is precisely that its third large spectral direction is generally coupled, not an independent square that can be grouped off as in (6.1).

## 7. What changed in the proof map

Partner r40's low-disjointness small-edge survivor previously ended with robust opposite stars and an anchored cofactor bank but no direct analytic receiver for that cofactor.  The new exact identity (2.7) shows that the cofactor is already the projected-crossing currency seen by the current one-hub decoupled-slice theorem.

The branch now has a deterministic source-valid split:

`anchored cofactor Z_ia > z0`

`=> at least one orientation has diffuse projected crossing`

`   => dimension-free delta log(1/delta) small-ball bound (3.7)`

`OR both orientations are concentrated`

`   => one new ORIGINAL wedge hub on each side, each >0.0282747`.

The example (5.1) proves that neither robust cofactor nor the resulting literal wedge hubs can by themselves replace the missing third smoothing resource.  The target repair (6.1)-(6.6) shows that a genuine product-preserving third square does exactly what is needed.

## 8. First unpaid implication

The first unpaid implication is now

`QFORM-R40-COFACTOR-THIRD-DIRECTION-UPGRADE-v1`:

> In partner r40's complete near-rank-two physical packet, retain the small nonzero mutual edge, arbitrary same-bank curvature, the full cross tail, and all extra spectrum.  On the balanced projected-crossing branch, use the actual third large spectral direction to upgrade the uniform `delta log(1/delta)` estimate (3.7) to `O(delta)` without invoking a worst conditional-density supremum.  On the doubly concentrated branch, consume the two physical wedge currencies (4.2)-(4.3) together with that same third direction via a product-preserving two-/three-hub or projected-crossing receiver.  The route may not assume that the third direction is an independent square; Section 5 shows why the logarithmic endpoint alone is insufficient.

This is strictly narrower than the preceding `QFORM-TRANSVERSE-CHAIN-HUB-RECEIVER-v1`: the partner cofactor is now quantitatively connected to a proved weighted analytic receiver, and failure of its only analytic gate is reduced to two fixed physical wedge hubs.

## 9. Verification and scope

The constants in (3.5)-(4.5) are direct evaluations of the exact rational `z0`.  The algebraic identities (2.5)-(2.9) are Lagrange/exterior-product identities.  The obstruction spectrum in Section 5 is exactly `{2,-2,0,0}` and in Section 6 exactly `{2,-2,1,0,0}`.

No claim of continuity is made beyond the scopes of the cited source theorems.  Full unrestricted QFORM status: **OPEN / NOT PROVED / NOT DISPROVED**.
