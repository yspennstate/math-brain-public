# Exact flow form of signed variational cuts

Finite uniform cubes; Boolean signs; entropy bits; K>=0. Write N=2^n, kappa=2/ln2 and G_f(x)=sum_S fhat(S)log2(fhat(S)^2)chi_S(x), zero terms zero. Let p_f(x) count incident pivotal coordinates. For any lambda>=kappa define

    b_lambda(x)=f(x)G_f(x)-lambda+(K/2)p_f(x).

Let P_+,P_- be the two sign vertex sets, and let their induced cube graphs contain only agreeing edges. Empty sign sets require no certificate. The following equivalence is unconditional: it is a representation of cut inequalities, not a claim that arbitrary roots satisfy them.

## 1. Signed cuts reduce exactly to two sign graphs

For E contained in one sign set P, all boundary edges leaving P are pivotal and all edges between E and P minus E are agreeing. Thus

    sum_E fG <= (K/2)sum_boundary(E) f(x)f(y)+lambda |E|

is EXACTLY

    sum_E b_lambda <= (K/2)|boundary_P(E)|.        (1)

For arbitrary E, split E=E_+ union E_-. Define the signed cut excess

    W(E)=sum_E fG-lambda|E|-(K/2)sum_boundary(E)f(x)f(y).

A pivotal edge between E_+ and E_- was counted with sign -1 in both separate boundaries, but is absent from the union boundary. Therefore

    W(E)=W(E_+)+W(E_-)-K e(E_+,E_-).              (2)

Since K>=0, all cuts satisfy W<=0 if and only if every single-sign cut satisfies(1). The signed cross edges have not been discarded or replaced by absolute values: equation(2) keeps their exact favorable sign. The equivalence need not hold for negative K.

## 2. Exact bounded-flow certificate

On each sign graph there exists an antisymmetric edge flow F_xy=-F_yx such that

    |F_xy|<=K/2,
    div F(x)=sum_(y in P adjacent x) F_xy >= b_lambda(x)          (3)

if and only if every subset E of that graph satisfies(1). Necessity follows by summing divergence: internal flows cancel and each outward edge contributes at most K/2.

For sufficiency build a network with source arcs of capacity b(x)>0, sink arcs of capacity -b(x) for b(x)<0, and both directed versions of each sign edge with capacity K/2. The cut of vertices E has capacity

    sum_(b>0 outside E)b - sum_(b<0 inside E)b
           +(K/2)|boundary_P(E)|.

This is at least total positive charge exactly when(1) holds. A maximum flow therefore saturates all source arcs. Its net flow across each sign edge has absolute value at most K/2, and its divergence equals b on positive-charge nodes, lies between b and0 on negative-charge nodes, and is0 on zero-charge nodes. Thus(3) follows.

The finite max-flow assertion also permits real capacities: the bounded feasible-flow polytope is compact, so a maximum exists. If a source-to-sink residual path remained, its positive minimum residual capacity would augment that maximum. With none, source-reachable vertices define a cut whose capacity equals the flow value. This proves the required cut equality without a rational approximation premise. Rational capacities admit the usual finite augmenting construction; every saved rational flow can instead be checked directly by(3), independent of how it was found.

## 3. Admission by the actual finite critical selector

If a K-violation exists, choose its least essential dimension, then a maximal D_K truth table at that dimension, as in the independently reconstructed A051 selector. Every physical child and smaller Boolean phase is nonviolating, and every same-dimensional vertex edit is nonimproving. A051's entropy curvature proof supplies the cut inequality with lambda=kappa. Consequently the selected witness admits BOTH exact sign-graph flows at edge capacity K/2 and charge b_kappa. Every lambda>=kappa only reduces the charges, so the same flow remains feasible.

For rational certificates choose lambda=3>kappa, evaluate fG by proved logarithm intervals, and replace b_3 by a dyadic upper bound. A feasible flow for these larger rational charges proves feasibility for the actual b_3. It does not itself certify the sharper b_kappa; the latter has the analytic existence proof above. No arbitrary near-extremizer is silently admitted: finite epsilon selection has an additive N epsilon/4 cut error, which cannot be dropped or exactly merged as epsilon=0. This stage asserts the exact-selector equivalence only.

## 4. Exact curvature refund and mandatory cut slack

The flow inequalities retain A051's curvature lower bound, not the full edit value. Put h(t)=-t^2 log2(t^2), h(0)=0, and k(t)=h(t)+3t^2/ln2. The curvature proof shows k convex and differentiable through zero. For an edit E let a_S and a'_S be the old and new Fourier coefficients and define the nonnegative Bregman remainder

    R(E)=sum_S [k(a'_S)-k(a_S)-k'(a_S)(a'_S-a_S)] >=0.

The exact Parseval edit identities yield

    D_K(f^E)-D_K(f)=(4/N)W_kappa(E)+R(E).         (4)

This is an equality, not just the semiconvex estimate. A true maximal-deficit table therefore forces

    -W_kappa(E)>=N R(E)/4                         (5)

for every E. On a single-sign subset, -W_kappa is exactly the cut slack c|boundary_P(E)|-sum_E b_kappa. Any flow certificate rewrites this as unused outward edge capacity plus absorbing vertex slack:

    -W_kappa(E)=sum_outward_edges (K/2-F_xy)
                    +sum_(x in E)[div F(x)-b_kappa(x)].

Thus actual extremality requires the flow slack to cover a NONLOCAL Fourier curvature refund on every edit. No capacity is a free pivotal influence reserve. For mixed edits equation(2) also retains the exact positive slack K times the internal pivotal-edge count; R(E) cannot generally be split into independent sign-component refunds.

An actual Boolean guard shows the distinction. On the three-bit majority, H=2,I=3/2 and fG=-2 at every vertex. At K=6 each sign graph is a three-leaf star. For lambda=5/2 the leaf charges are3/2 and the center charge is-9/2, so three rational flows of3/2 toward each center satisfy capacity3 exactly. Since kappa>5/2 (for instance ln2<3/4), this also certifies every sharper W_kappa<=0. But D_6=-7 and the edit of the entire negative sign set produces a constant of deficit0. Its actual improvement is7. Here W_kappa=10-4kappa<0 and R(E)=2+4/ln2, with equation(4) giving7 exactly. The nonnegative-cut constraints alone do NOT characterize even finite maximal deficit. Dropping R(E) would admit this false critical model.

## 5. Structural implication and honest gap

The charge b includes the FULL entropy potential and the actual pivotal degree. Positive charge in any sign component must be transported through agreeing physical edges to negative-charge vertices; isolated vertices necessarily have nonpositive charge. For every physical block face, the same flow gives its exact signed-cut certificate by divergence and equation(2). A giant or connected sign component without these charge/flow constraints is not an admissible critical model.

This is not component pruning. A sign graph is used only as a graph inside the original Boolean parent; its raw indicator spectrum is never substituted for a physical child. Flow divergence uses G_f from the original complete Fourier spectrum, including all component cross terms. Criticality licenses the cuts through finite same-dimension deficit maximization, while actual lower-dimensional physical children still supply their separate D+S bank. The historical component-indicator counterexamples do not violate the derived graph equivalence.

There is no FEI influence payment yet: flow capacity is attached to AGREEING edges, whereas total influence counts pivotal edges. Flow transport or congestion across a selected physical pair has not been bounded by its queried influence or by its signed parity-minus-refund residual. A valid bridge must preserve this distinction, all physical children, and the same complete Gibbs/interaction bank. A005's Gibbs-exhaustion equivalence shows that merely rewriting the bank is not mathematical payment.

FIRST UNSUPPORTED LINE: compare the mandatory Bregman-refund cut slack and sign-flow transport crossing a selected physical pair/fiber with that pair's actual signed Fourier interaction and its positive D+S reserve, using one pivotal influence owner. The two-flow representation closes simultaneous signed-cut certification and equation(4) exposes the lost resource; neither supplies this comparison or full FEI. NEXT targets that exact physical/Fourier transfer rather than another qualitative connected-component class.
