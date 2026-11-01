# C0052: original-current overlap, its exact moment kernels, and the missing estimate

Author: w468. Referee: w470; adversary: w469. All new results are author proofs pending independent review. Current openness: UNKNOWN. Parent problem: NOT SOLVED.

## Exact target and assumptions

The source is Duminil-Copin, arXiv:1707.00520v1, Conjecture 6 and equations (7.1)-(7.2), printed p.94. The model is the zero-field nearest-neighbor ferromagnetic Ising model with unit couplings on Z^3. For 0<beta<beta_c use its infinite-volume free state and write G(x)=<sigma_0 sigma_x>, chi=sum_x G(x), and xi=[lim_n -(1/n)log G(n e1)]^(-1). Thus xi is exponential, not a second-moment length.

Let U4 be the fourth joint cumulant as defined explicitly in STATEMENT.md. The source's coupling is g=sum_(x,y,z)U4(0,x,y,z)/(chi^2 xi^3)<=0. The target is g NOT tending to zero as beta increases to beta_c. We attempt the stronger sufficient assertion liminf lambda>0, where lambda=-g. We assume neither existence of lim g nor uniqueness or conformal covariance of a continuum field.

The standard inputs used below are G>=0, translation invariance, chi<infinity below beta_c, independent sourced random-current laws and their switching identity, the augmented-current occupation identity, and the tree-diagram upper bound. They are described in the primary 2017 source, Exercise 61, and Aizenman arXiv:2112.04248v3, equations (5.9), (5.13), (8.2). Our formulas are first finite-volume identities; their infinite-volume version uses the standard sourced-current construction and its switching identity in the subcritical model. This construction is not a new theorem claimed here.

## Prior-attempt digest

The dated ranking has C0052 tier 5, attempted_un. The exact intake row is problems.jsonl:52 in probability_1000_intake_claude_20260907. Attempt C0052-A001 at attempts.jsonl:42 proposes a random-current second-moment route and leaves its variance estimate open. Its dimension calculation is a heuristic; it does not define and prove a random-current cluster dimension. Its sentence about independent fractals does not supply an occupation estimate for sourced current clusters. Separate currents ARE independent conditional on the endpoints; two hits within the same current cluster need not be independent.

The old attempt's claim that a two-point lower bound would yield a first intersection moment also needs the exact probability space. The readily available two-point occupation identity contains an extra sourceless current. Removing that current changes the law. The new calculations below make this missing step explicit instead of presuming that Lebowitz controls it. Targeted ID searches in the named H and I attempt directories and the Lean directory found no additional C0052 proof; this is not a claim about unnamed files elsewhere. Team O's board lists no C0052 holder.

The named memory scar perceptron_proof_open_gaps_fleet_2026_07_12 warns that a green pipeline or checked sublemma is not a full proof. Bounded brain recall timed out; the named scar was read directly. Its applicable lesson is enforced here by preserving the single unresolved uniform estimate below.

## L3: exact endpoint-average identity for the source coupling

Define mu(x)=G(x)/chi, a probability law. For fixed y, draw X,W independently from mu, then draw n1 with source set {0} symmetric-difference {X}, and n2 with source set {y} symmetric-difference {y+W}, independently conditional on X,W. Repeated endpoints cancel in the source set, but their tagged vertices remain in the connectivity event. Put

q(X,y,y+W)=P(0 connected to y in n1+n2),
Q_y=E_(X,W)[q(X,y,y+W)].

For distinct endpoints, each current connects its own two sources by the even-parity rule, so this is exactly the event that all four tagged endpoints are connected. The identity also holds with coincident endpoints, by the switching lemma with source sets taken modulo two; for example, if X=0 and W=0 it gives U4(0,0,y,y)=-2G(y)^2.

The switching identity gives -U4(0,x,y,z)=2G(x)G(z-y)q(x,y,z). Thus, by substituting z=y+w and summing nonnegative terms,

    lambda(beta) = 2 xi^(-3) sum_(y in Z^3) Q_y.                 (A)

The sums are finite: the tree-diagram bound gives sum_(x,y,z) -U4(0,x,y,z) <= 2 chi^4. Hence sum_y Q_y <= chi^2. This justifies the reindexing and shows that (A) is an equality, not just a scaling analogy.

Let R=floor(xi), assume xi>=1, and B={y: ||y||_infinity<=R}. Draw Y uniformly in B as well, independently of X,W. Write Q_B=E[q(X,Y,Y+W)]. Dropping y outside B in (A) gives

    lambda >= 2 |B| xi^(-3) Q_B >= 2 Q_B,                     (B)

because 2 floor(xi)+1>=xi for xi>=1. No critical exponent or comparability between correlation lengths is needed. The integer rounding and the volume factor have not been suppressed.

## L4: a precise sufficient hardest lemma

Under the same joint law, let A=C_0(n1), D=C_Y(n2) be the source-anchored components in the SINGLE currents, and define

    N = sum_(v in B) 1{v belongs to A and D},
    m1=E[N],  m2=E[N^2].

These components include their anchor vertices even when a source pair cancels. In particular m1>0: on Y=0, both components contain 0, and P(Y=0)=1/|B|.

If N>0, the two components meet, so 0 and Y are connected in n1+n2. The converse is not required and is not asserted: the union can connect through other current components. Cauchy-Schwarz gives

    m1^2 = E[N 1{N>0}]^2 <= m2 P(N>0).

Therefore Q_B>=P(N>0)>=m1^2/m2, and combining this with (B),

    lambda(beta) >= 2 |B| xi^(-3) m1^2/m2.                   (C)

**Single hardest unresolved input (UCM):** prove a constant C<infinity and beta_0<beta_c such that m2(beta)<=C m1(beta)^2 for every beta_0<beta<beta_c, with B=floor(xi_exp(beta)) as above, and with the ORIGINAL unaugmented current components.

If UCM is proved, (C) yields liminf_(beta->beta_c) lambda>=2/C>0, settling the source's first-clause non-triviality criterion. UCM is a sufficient input, not an equivalence, and may be stronger than necessary. It has NOT been proved here. If only a sequence beta_j has bounded m2/m1^2, the conclusion is limsup lambda>0, which is already sufficient for the source's weaker target. This distinction is explicit.

## L5: exact kernels and the direction of the two-point estimate

For a fixed pair (0,x), define h_x(v)=P^{0 triangle x}(v in C_0(n)), and h_x(u,v)=P^{0 triangle x}(u,v in C_0(n)), both for ONE current. Let

    k(v)=sum_x mu(x) h_x(v),
    k2(u,v)=sum_x mu(x) h_x(u,v).

Conditional independence of n1,n2 and independence of X,W, followed by translation invariance, yield the exact formulas

    m1 = (1/|B|) sum_(v in B) k(v) sum_(y in B) k(v-y),        (D)
    m2 = (1/|B|) sum_(u,v in B) k2(u,v)
                               sum_(y in B) k2(u-y,v-y).     (E)

Each factor in (E) is a JOINT two-hit probability within one current cluster. It is not replaced by a product of one-hit probabilities. The diagonal u=v is included. The finite box makes (D)-(E) finite; the endpoint sums are averages of probabilities and are absolutely convergent.

Add a sourceless current n0 to a current with endpoints 0,x. The primary identity says that its enlarged component hits v with probability G(v)G(x-v)/G(x). Averaging against mu(x) gives exactly

    k_aug(v) = G(v) [sum_x G(x-v)]/chi = G(v).                (F)

Since adding n0 can only enlarge a component, k(v)<=G(v). On the other hand the source endpoint X=v is always in C_0(n), so k(v)>=mu(v)=G(v)/chi. Thus

    G(v)/chi <= k(v) <= G(v),
    m1_aug/chi^2 <= m1 <= m1_aug,
    m1_aug=(1/|B|) sum_(v in B) G(v) sum_(y in B) G(v-y).     (G)

These are actual proved bounds on the first moment. They expose a factor chi^2 gap; they do NOT give UCM. A lower estimate for G controls m1_aug from below, but the exact available comparison to m1 loses chi^2. An asserted replacement k=G would silently change the current law.

For k2, the automatic bound k2(u,v)<=min(k(u),k(v)) only produces a crude volume-dependent bound for m2. It does not supply a uniform bound on m2/m1^2. No unsupported six-point-to-two-point factorization is used.

## Attempt at closing UCM and the precise stopping point

The natural strategy is to establish a scale-sized source-cluster occupation lower bound for k and a two-hit upper estimate for k2 whose convolution in (E) is at most a constant times the square of (D). The exact augmented occupation calculation (F) is attractive because it supplies a closed two-point expression. However it gives an upper estimate for k, and the deterministic-endpoint lower estimate in (G) loses susceptibility. The remaining joint two-hit control is not supplied by ordinary spin Lebowitz inequalities alone.

TREE_OBSTRUCTION.md proves that fixed-endpoint single-current and augmented occupations cannot be compared from below by a graph-uniform positive constant. It also refutes a graph-uniform linear reversal between the original two-current connection event and the four-current augmented-cluster meeting event. At t=log(3), the latter loses a factor exactly 37 at bridge length 100; the former loses the factor (8/5)^100. These counterexamples are finite trees, so they do not refute a critical Z^3 comparison or an improved endpoint-AVERAGED estimate for k. Such an estimate would need an actual dimension-specific proof.

The open step is UCM (or a weaker subsequence version), specifically deriving it for the original-current kernels in (D)-(E). The algebraic reduction, known switching identity, and finite-tree checks cannot be relabeled as this estimate. No contradiction, complete proof, asymptotic numerical result, or formal-check receipt is claimed.

## Verification and review boundary

Run `python -X utf8 verify_tree.py` under compute_gate.json. It enumerates both current trace supports and Ising spin configurations with exact integer/rational arithmetic on six small paths, rather than sampling. These checks validate the finite specializations and the distinction between the two measures. They do not establish UCM. Independent review is pending, and served-model identity is not visible from these tools.

NEXT: Obtain a dimension-specific lower estimate for the endpoint-averaged ORIGINAL-current k and a joint two-hit bound for k2 that make (E)/(D)^2 uniformly bounded; do not substitute k_aug=G for k.
