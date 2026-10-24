# P0110: dependence-safe cylinder reduction

Date: 2026-10-10. Author: w372. Independent referee: w374 (pending). No claim that P0110 is solved, currently open, or that the reductions below are new.

## Target and hardest remaining input

The exact primary question is Auffinger--Damron--Hanson, arXiv:1511.03262v2, Question 22: "Find a distribution of passage times where (4.19) holds." Equation (4.19) is chi = 2 xi - 1. The surrounding discussion distinguishes the known conditional KPZ theorem from the unproved existence of suitable exponents. STATEMENT.md gives Chatterjee's global definitions and the concrete candidate Uniform[1,2] on undirected nearest-neighbor Z^d, d >= 2.

The single hardest parent input H_GLOBAL is: for this ONE law prove chi_a = chi_b and xi_a = xi_b, with the upper exponential-moment and lower variance/mean bounds uniform over all sufficiently distant lattice endpoints. An axis-only variance power law, a strip CLT, a continuum theorem, or a numerical fit does not prove H_GLOBAL. The results here certify a decoupling step useful in the existing relation proof; they do not supply H_GLOBAL.

## Prior-attempt digest

The ranking row is attempted_un. The corresponding campaign bundle op-p0110 explicitly has source_says_open, current status unverified, and result status attempted_unsolved. Exact-ID searches of the named H/I attempt directories found no P0110 proof row; that is absence of a located record, not evidence that no attempt exists. The initial Claude problems/attempts ledgers did not contain this Codex-origin ID, but brain_bundle_C006p01.json contains its exact campaign statement. The Lean annotation repeats attempted_un and supplies no P0110 formal-check receipt.

The brain's August FPP campaign scars are directly relevant: a measured bounded block-influence/variance ratio was calibration, not a proof of the missing comparison; an attractive point-conditioned membership residual remained unresolved. The owner's solved width-3 directed-strip time constant concerns a different model and quantity. The perceptron scar warns that a finished pipeline is not a finished proof. The recent arXiv:2604.01214 result is a variance upper bound for rotationally invariant planar Riemannian FPP; it does not establish an iid lattice exponent pair. Present openness remains UNKNOWN.

## L1. Finite dependence and an unconditional variance floor

Assume iid Uniform[1,2] edge weights. For v != 0 put L = ||v||_1. A coordinate path costs at most 2L. Any minimizing path has at most 2L edges, since each edge costs at least one. It lies in the deterministic l1 ball of radius 2L about its starting point. There are finitely many candidate simple paths, so a minimum exists; continuity and a finite union of zero-probability ties give uniqueness almost surely. Also L <= T(0,v) <= 2L.

For every v != 0,

    Var T(0,v) >= c_d := 4^(-(4d+1)).

Proof. Condition on all edges except the k = 2d edges incident to 0. A simple path leaves 0 exactly once. Write its optimal cost as min_i(U_i + A_i), where A_i is the optimal passage time from neighbor i to v in the graph with vertex 0 removed; A_i = 0 if that neighbor equals v. All A_i are finite and measurable in the conditioned exterior. If all U_i <= 5/4, T <= min_i A_i + 5/4; if all U_i >= 7/4, T >= min_i A_i + 7/4. Each event has conditional probability p = 4^(-k), because these k coordinates remain independent uniforms after conditioning on their exterior. Take two independent conditional copies. Their squared difference is at least 1/4 on each of the two ordered low/high event pairs. The identity Var X = (1/2) E(X-X')^2 gives conditional variance at least p^2/4 = c_d. The law of total variance gives the assertion. No geodesic segments or conditioned membership events are multiplied as if independent.

In d = 2, c_d = 1/262144. In particular this proves chi_b >= 0 under the original large-endpoint definition, but does not prove chi_b > 0 or chi_a = chi_b.

Short-endpoint obstruction. For v = e_1, the direct edge has cost at most 2, whereas every other simple path has at least three edges and cost at least 3. Thus the geodesic is that edge for every environment and D(0,e_1) = 0. Likewise D(0,2e_1) = 0 almost surely, since the two-edge straight path costs strictly less than 4 almost surely while every alternative costs at least 4. Consequently a lower bound on ED over ALL nonzero endpoints, as literally displayed in Auffinger--Damron (2.2), fails for Uniform[1,2]. The original Chatterjee (A4) has a sufficiently-large-distance cutoff. This packet uses that original formulation; citing the later all-endpoint version for this candidate without resolving its short-endpoint assumption would be incorrect. This finite-distance issue neither disproves the original KPZ target nor proves the large-distance lower wandering bound.

## L2. Unconditional disjoint-cylinder variance transfer

First an abstract statement. Let F_1,F_2 be identically distributed square-integrable random variables with standard deviation s. Let G_1,G_2 be iid square-integrable random variables on the same probability space. Suppose Delta_i = G_i-F_i >= 0, the Delta_i have the same mean, and ||Delta_i||_2 <= delta. No independence of the F_i, the Delta_i, or any localization events is assumed. Then

    2 (s-2 delta)_+^2 <= Var(F_1-F_2) <= 2 (s+2 delta)^2.       (1)

Proof. Write r = sd G_i. Centering contracts the L2 norm, so |r-s| <= delta. Since Delta_i >= 0,

    E(Delta_1-Delta_2)^2 <= E Delta_1^2 + E Delta_2^2 <= 2 delta^2.

The differences F_1-F_2 and G_1-G_2 both have mean zero. Independence of G_1,G_2 gives ||G_1-G_2||_2 = sqrt(2) r. The forward and reverse L2 triangle inequalities now give

    sqrt(2) (s-2 delta)_+ <= ||F_1-F_2||_2 <= sqrt(2) (s+2 delta),

which proves (1). Independence is used only for variables measurable in disjoint deterministic edge sets, before conditioning on any event.

Application to iid Uniform[1,2] FPP. Fix positive integers n,w. Take the induced box

    C_1 = ([-w,n+w] x [-w,w]^(d-1)) intersect Z^d

with endpoints 0 and n e_1; let C_2 be its translate by (4w+2)e_2 and translate the endpoints likewise. The two boxes have disjoint edge sets. Let F_i be unrestricted passage times and G_i be passage times restricted to C_i. The straight n-edge route lies in each box, so n <= F_i <= G_i <= 2n. Thus 0 <= Delta_i <= n. If the unique unrestricted geodesic stays in C_i, Delta_i = 0. Consequently, with p bounding the departure probability in each box, delta = n sqrt(p) is valid in (1). The original geodesic deviation D <= w guarantees containment in this extended box, including its longitudinal ends.

The abstract statement also works for atomic weights if p bounds the event F_i != G_i; no uniqueness assertion is then needed.

## L3. The exact probability budget for this reduction

Suppose s_n >= c n^b and p_n <= C n^(-q). Equation (1) implies

    Var(F_1-F_2) / (2 Var F_1) -> 1

provided q > 2(1-b), because delta_n/s_n <= (sqrt(C)/c) n^(1-q/2-b) -> 0. If b = 1/3, this sufficient threshold is q > 4/3. With the unconditional variance floor L1, q > 2 suffices without presuming a positive fluctuation exponent. At equality of the exponents, constants or a little-o improvement matter. This is a sufficient and sharply obstructed L2-error criterion, not a necessary confinement exponent for actual lattice FPP.

Counterexample to dropping the probability budget. For any fixed 0 <= b < 1, take Z_n Bernoulli with p_n = n^(-2(1-b)); set F_1 = F_2 = n(1-Z_n) and G_1 = G_2 = n (independent constants). Then 0 <= G_i-F_i <= n, F_i = G_i except on an event of probability p_n -> 0, and Var F_i = n^(2b)(1-p_n). But Var(F_1-F_2) = 0. Thus small departure probability alone does not imply near independence or a lower bound on difference variance. This is an abstract counterexample to a proposed inference, not a counterexample to iid lattice FPP or KPZ.

## L4. A dependence-safe mean-gap localization reduction

Write m(x) = ET(0,x). Fix a >= 0, alpha > 0 and M < infinity and assume, for all nonzero lattice x,

    E exp(alpha |T(0,x)-m(x)| / |x|^a) <= M.                 (2)

Let v = n e_1, and assume that for every lattice z in the l1 ball of radius 2n but outside C_1,

    m(z)+m(v-z)-m(v) >= H_n > 0.                           (3)

Then the departure probability satisfies

    p_n <= 3 M (4n+1)^d exp(-alpha H_n / (3 (3n)^a)).       (4)

Proof. A departing geodesic has a vertex z in this deterministic finite set. Optimality gives T(0,v) = T(0,z)+T(z,v). Subtract the three means. Equation (3) forces at least one of the three absolute centered passage times to be >= H_n/3. Translation invariance and (2), together with |z| <= 2n and |v-z| <= 3n, bound each event by M exp(-alpha H_n/(3(3n)^a)). Union-bound over the three events and at most (4n+1)^d vertices. No independence is needed between these passage times or the random vertex z; the vertex search is replaced by a union over a deterministic set.

If w = ceil(n^zeta), H_n >= c w^2/n, and 2 zeta - 1 > a, (4) is smaller than every inverse power of n. L1--L3 therefore certify asymptotic variance transfer in those cylinders. For Uniform[1,2], Chatterjee's unconditional bound chi_a <= 1/2 supplies (2) for each a > 1/2; it does not supply (3). Neither L4 nor a one-direction confinement proof supplies H_GLOBAL.

## Attempt at the remaining local input, and where it stops

The narrow attempted input H_MEAN is (3) with H_n >= c w^2/n and some zeta < 1 for Uniform[1,2]. The elementary deterministic bounds give m(z) >= ||z||_1 and m(v) <= (3/2)n. At z = (floor(n/2),w+1,0,...,0), these certify only

    m(z)+m(v-z)-m(v) >= 2(w+1) - n/2.

For every fixed zeta < 1 this lower certificate is negative for sufficiently large n. It therefore cannot certify (3). This does not show that the actual mean gap is negative.

The fixed-path route has the same issue quantitatively. For a prescribed self-avoiding path of length ell = n+2(w+1), Hoeffding gives

    P(path cost <= 3n/2) <= exp(-4.5 (ell-n)^2/ell).

The elementary count is at most (2d)(2d-1)^(ell-1) such paths. The resulting union certificate has logarithm of order +n log(2d-1) - O(w^2/n), which is positive when w = n^zeta and zeta < 1. It gives no useful bound even for this restricted path family and favorable cost threshold; longer paths and the randomness of the competing passage time add obligations. There is no legitimate product of row-wise or segment-wise probabilities to remove that entropy term.

A uniform quadratic bend estimate for the unknown time-constant norm, with an appropriate control of the nonrandom passage-time error, could imply H_MEAN. Neither estimate is proved here. Even proving H_MEAN would establish only a localization input; matching the global upper and lower exponent definitions remains H_GLOBAL.

## Independent checks and exact next step

tests/verify_transfer.py exhaustively checks the unconditional variance-transfer inequalities on two small iid bounded-weight ladder graphs, using exact rational moments. It also evaluates the common-shock counterexample. The finite computations check algebra and dependence handling; they do not prove the continuum-law localization input, large-n exponents, or novelty.

NEXT: w374 should independently rederive (1) and (4), check the common-shock obstruction and original exponent cutoff, then keep only these partial reductions; the next proof step is a quantitative positive mean-gap bound (3) for one actual iid law.
