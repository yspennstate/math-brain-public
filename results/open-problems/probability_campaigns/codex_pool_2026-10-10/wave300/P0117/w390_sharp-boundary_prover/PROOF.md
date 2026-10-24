# P0117 boundary result: a quantitative obstruction to thin-tube confinement

Status: author-proved special case, pending w392's independent review. Novelty UNKNOWN. This is not a proof of the unrestricted no-bigeodesics target.

## Model and constants

On the undirected nearest-neighbor graph Z^2, let the edge weights be iid finite nonnegative random variables with a nonconstant law. A geodesic ray is an injective nearest-neighbor sequence indexed by nonnegative integers whose every finite contiguous subpath has minimum weight among all finite paths joining the same endpoints. No uniqueness, continuity, positive-speed or moment hypothesis is used below.

Choose finite 0 <= l < h such that p_l = P(t_e <= l) > 0 and p_h = P(t_e >= h) > 0. Such a pair exists for every nonconstant finite nonnegative law. Set

    m(w) = floor((4w+2)l/(h-l)) + 1,
    K = 1 + 4l/(h-l),
    C = 2K log(1/p_h) + (K+4) log(1/p_l).

Here w is a nonnegative integer, all logarithms are natural, and 0 < C < infinity. We have m(w) <= K(w+1) and m(w)(h-l) > (4w+2)l. The constant C is sufficient, not claimed optimal.

## Lemma 1: a deterministic slab obstruction

Fix integers A, y_0 and w >= 0, and write m=m(w). Require weight at least h on the m(2w+1) horizontal edges

    {(x,y),(x+1,y)} with A <= x < A+m, |y-y_0| <= w.

Require weight at most l on the m horizontal edges of row y_0+w+1 over the same x interval and on the vertical edges at columns A and A+m between levels y_0-w and y_0+w+1. There are exactly m+4w+2 required cheap edges. The high and low sets are disjoint.

On this event, no finite geodesic contained in the horizontal strip |y-y_0| <= w joins a vertex of column A to a vertex of column A+m.

Proof. Any such path crosses each of the m intervening vertical cuts at least once. Each crossing uses an expensive horizontal edge, so nonnegativity gives path cost at least mh. If its endpoint heights are y and z, go vertically from (A,y) to the row y_0+w+1, traverse that row to column A+m, then go vertically to (A+m,z). This competing path uses at most m+4w+2 cheap edges, and has cost at most (m+4w+2)l < mh. Thus the confined path is not a geodesic. Neither monotonicity nor uniqueness of the original path is assumed. The competing path may leave the tube: the metric is the full Z^2 metric, not a metric restricted to the tube. QED.

## Lemma 2: an independent family of traps

For fixed w, the event of Lemma 1 has probability

    q_w = p_h^(m(w)(2w+1)) p_l^(m(w)+4w+2)
        >= exp(-C(w+1)^2).

Proof. Independence applies to the explicitly listed distinct edges. Since 2w+1 <= 2(w+1), m <= K(w+1), and m+4w+2 <= (K+4)(w+1), taking negative logarithms proves the bound. Slabs whose left columns are separated by m+1 have disjoint required edge sets, including both vertical connector columns, so their trap events are independent. No conditioning on the existence or choice of a geodesic occurs. QED.

## Theorem 3: no geodesic ray eventually fits a logarithmically thin tube

Let w: {0,1,...} -> {0,1,...} be a deterministic nondecreasing function with

    limsup_(n -> infinity) w(n)/sqrt(log n) < 1/sqrt(C).

For any fixed integer y_0, almost surely no geodesic ray has a tail entirely in

    T_w(y_0) = {(x,y) in Z^2: |y-y_0| <= w(|x|)}.

Proof. For R=2^k set W=w(2R), m=m(W), and J=floor(R/(m+1)). Use J slabs with left columns A_j=R+j(m+1), 0 <= j < J. Their endpoints lie between R and 2R, and all tube vertices there have height within W of y_0. By Lemma 2 the required edge sets are disjoint. Therefore

    P(no trap among these J slabs) = (1-q_W)^J <= exp(-J q_W).

Put L=limsup w(n)/sqrt(log n). Choose a number theta strictly between C L^2 and 1. For all sufficiently large R, C(W+1)^2 <= theta log R. Thus q_W >= R^(-theta). Also W+1 <= D sqrt(log R) for some finite D and all large R, so

    J >= R/[2(K+1)(W+1)]

for all sufficiently large R. Hence J q_W >= c R^(1-theta)/sqrt(log R) for some c>0. The no-trap probabilities are summable over dyadic k. By the first Borel-Cantelli lemma, almost surely every sufficiently distant positive dyadic annulus contains a trap. Reflection gives the same conclusion on the negative x side. Independence BETWEEN annuli is not needed.

Suppose a geodesic ray has a tail in T_w(y_0). For each M, the part of this tube with |x| <= M is a finite vertex set. An injective ray eventually leaves it permanently. Nearest-neighbor steps prevent infinitely many switches between the two sides after that departure. Consequently the x coordinate tends to +infinity or -infinity.

Consider the +infinity case and any sufficiently distant trapped slab with columns A and A+m, beyond the beginning of the confined tail. Choose an index at column A and a later first index at column A+m, then choose the last column-A index before that arrival. Between the chosen indices the x coordinate is in [A,A+m], by the nearest-neighbor property. The entire subpath is therefore in the height-W strip. It is a finite geodesic crossing forbidden by Lemma 1. The negative-side argument follows by reflection. QED.

The assertion excludes all rays on the probability-one trap event; it is not merely an assertion about one preselected random ray.

## Corollary 4: a simultaneous transversal lower bound

Almost surely, for every geodesic ray (v_j)=(x_j,y_j) and every integer y_0,

    limsup_(j -> infinity) |y_j-y_0|/sqrt(log(2+|x_j|)) >= 1/sqrt(C).

Proof. Apply Theorem 3 to w_c(n)=ceil(c sqrt(log(2+n))) for each positive rational c<1/sqrt(C) and every integer y_0, then take the countable intersection of their probability-one events. If the displayed limsup were below 1/sqrt(C), choose a rational c strictly between them. Eventually the ray would lie in T_(w_c)(y_0), a contradiction. QED.

In particular there is almost surely no bigeodesic wholly in any fixed horizontal or vertical finite-width strip, or with even one tail eventually in a tube as in Theorem 3. A bigeodesic tail is a geodesic ray. Coordinate exchange handles vertical strips.

## Boundary and scope

The nonconstant-law hypothesis is necessary for these strip statements: for a constant weight t_e=a>=0, the horizontal path ((j,0)) indexed by all integers is a bigeodesic, since each finite segment has length equal to the L1 distance (if a=0, every competing path also has zero cost). Thus the fixed-strip exclusion has a sharp distributional boundary. No optimality of the sqrt(log n) scale or of C is claimed.

No counterexample to P0117 follows from this constant-law example, because it violates the target's nonatomic assumption. The cheap-detour proof also applies to nonconstant atomic laws, but it does not prove absence of unrestricted bigeodesics for them.

## Single hardest remaining gap

An unrestricted candidate bigeodesic can have tails outside every deterministic tube of width below the proved threshold. Nothing here forces a bigeodesic into such a tube. To extend this method to the full P0117 target one would need a justified obstruction for arbitrary wide or adaptively wandering paths, with the necessary independence or martingale argument. There is no such bridge in this packet.

NEXT: w392 should audit Lemma 1's connector counts, Lemma 2's disjoint supports, and Theorem 3's adaptive path and quantifier handling; any wider-tube route must explicitly address this gap.
