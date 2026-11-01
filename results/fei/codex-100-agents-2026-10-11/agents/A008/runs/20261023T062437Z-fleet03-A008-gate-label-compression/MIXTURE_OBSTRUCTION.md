# A fixed pair of polarity queues still repeats a shared clause label

All logarithms are in bits. This is an obstruction to the ORIGINAL queue reference, not to FEI or to arbitrary codes. It extends A007's obstruction from choosing one polarity globally to ANY fixed normalized mixture of one positive-prime queue and one negative-prime queue, with independently arbitrary positive packing-feasible weights and arbitrary ordered covers. All finite runs, including repeated gates, overlapping subsets and every output ambiguity, are included in the upper mass bounds.

## Finite-tree exponential moment: the missing occupation bound

The original offspring law is p_c=1/[(c+1)(c+2)], c>=0. Its probability generating function is Phi(t)=sum_c p_c t^c. An entirely rational certificate gives

    Phi(17/20) <= sum_{c=0}^{16} p_c(17/20)^c
                         +(17/20)^17/18 < 4/5.                 (1)

The tail uses sum_{c>=17}p_c=1/18. No finite offspring mean is assumed; in fact that mean is infinite.

Consider ANY original finite gate table, activities x_e=lambda_e*pi_e, A0=sum_e x_e, D=prod_e(1+x_e)-1. Let G be a collection of marked gate names of total packing weight t=sum_{e in G}lambda_e. For z>=1 suppose zt<=1/16 and zA0<=1/16. Count M=the number of CHILD visits whose gate name lies in G, with repetitions, and R=the number of initial roots. Then the full original conditioned queue satisfies

    E[1_{finite successful run} z^(R-1+M)] <=16/19<1.          (2)

Proof: let F_e,h(z) be the weighted mass of successful descendant trees at gate e of height at most h, weighting marked child names by z. Begin with F_e,0=0. If all previous F are <=4/5, then for each specified attachment coordinate j the weighted sum over allowed child names is at most

    (4/5)[sum_{e:j in R_e}lambda_e
                +(z-1)sum_{e in G:j in R_e}lambda_e]
          <=(4/5)(1+zt)<=17/20.

For every selected subset and attachment multiset the child-tree contributions multiply according to the actual independent queue choices. Sum over normalized multiset choices, then over c with its EXACT law, then over valid sizes/subsets of total mass <=1. Equation (1) bounds the next F by4/5. Induct on height and take the monotone limit: this includes all finite successful trees and excludes failed/infinite runs without renormalizing them.

For exactly a nonempty root set S, conditioned original mass is prod_{e in S}x_e/D. Multiply by z^(|S|-1), and sum the descendant masses and the actual root sets. The resulting moment is at most

    [prod_e(1+(4/5)z x_e)-1]/(zD).

The sum of the positive factors (4/5)z x_e is <=1/20. Finite product expansion gives prod(1+u_e)-1<=sum u_e/(1-sum u_e). Also D>=A0. Hence this last display is at most (4/5)/(1-1/20)=16/19. This proves (2), retaining absent roots and the exact nonempty normalizer. It is a sum of joint run probabilities, not an unsupported product of marginal success bounds.

## Actual Boolean family and complete prime classification

Fix w>=32, r=2^w, epsilon=1/r, p=1-epsilon. Let X and Y each consist of r disjoint clauses of w bits, and define

    U(X)=prod_{C=1}^r OR_w(X_C),
    V(Y)=1-U(-Y)=OR_{D=1}^r AND_w(Y_D),
    F=2U(X)V(Y)-1.

These are actual uniform-cube Boolean functions on 2rw bits. Positive primes of F are exactly a positive X-transversal (one variable per X clause) together with one whole positive Y clause D; their width is r+w. Negative primes are exactly a whole negative X clause C, or a negative Y-transversal; their widths are w and r, respectively. For disjoint blocks, a positive certificate of an AND must certify both factors, while a certificate of an OR must certify at least one factor (otherwise independent false completions falsify the OR). Minimality gives the stated complete tables; no mixed primes are omitted.

Fix ANY positive feasible weights for the positive table. For each Y clause D put t_D=sum of lambda over prime names using D. Since every positive prime contains exactly one coordinate in a fixed X clause, its packing rows give

    sum_D t_D=sum_e lambda_e<=w.

Therefore at least r/2 clauses D have t_D<=2w/r. Call them good. Every positive root has rarity pi=2^-(r+w), so A0=pi sum lambda<=w/r. For a good D choose z=1/[16(t_D+A0)]. Then zt_D,zA0<=1/16 and

    z>=r/(48w)>=2^(w/2)>=1.                            (3)

The middle inequality follows from (48w)^2<=2^w for w>=32; its base case and increasing adjacent ratio prove it for every integer w.

## One-clause joint targets force repeated rare child names

Let A=A_X union A_Y, where A_X is a nonempty subset of ONE X clause C of size k_X, and A_Y is a nonempty subset of one good Y clause D of size k_Y. In every successful positive-table run producing exactly A, each visited prime contains one X_C coordinate. A parent-child edge can change that coordinate only if its attachment is in Y_D, because every selected attachment lies in A and an X_C attachment forces both gates to contain the same X_C coordinate. Such a child MUST have gate name using D. Along each initial root tree, every newly encountered X_C coordinate therefore requires a marked D-child visit. Consequently

    k_X <= R+M_D.

All repetitions, unused X coordinates in visited primes and overlapping selected subsets only increase the available count, so they cannot defeat this necessary inequality. Equations (2),(3) give the FULL output bound

    Q_+(A) <= (16/19) z^-(k_X-1) <= z^-(k_X-1).        (4)

This is the once-per-needed-transition clause-name charge after summing EVERY finite run, not a lower bound on a single selected forest cost.

In the negative table, the A_X component is supported only by the X clause C; the k_Y distinct Y_D coordinates belong to k_Y distinct components, because a Y-transversal contains only one variable from D. No gate joins X to Y. The exact necessary-root event has mass D_X prod_i D_i /D_-. Here D_- >=D_X, and by packing each Y component activity is <=2^-r. Finite product expansion gives D_i<=2^-r/(1-2^-r)<=2^(1-r). Hence, independently of all negative-table weights and orders,

    Q_-(A)<=2^(-(r-1)k_Y).                             (5)

For k_X>=ceil(w/2), (3),(4) imply -log Q_+(A)>=w^2/8, since k_X-1>=w/4. Equation (5) implies the same lower bound for Q_-(A), since r-1>=w^2/8. Thus for ANY alpha in [0,1], fixed before sampling,

    Q_mix(A)=alpha Q_+(A)+(1-alpha)Q_-(A)<=2^(-w^2/8).

In particular, selecting polarity per set within this fixed mixture does not repair the cost. A007's universal one-root structural witness remains valid; its child labels are expensive here.

## Actual spectral mass and divergent complete queue cost

For a nonempty subset supported within ONE clause, |hat U(A_X)|=epsilon p^(r-1), and |hat V(A_Y)| is the same. Thus every joint target above has actual squared Fourier mass

    P_F(A)=4 epsilon^4 p^(4(r-1)).

There are r choices of C, at least r/2 good choices of D, at least r/2 X-subsets of size>=ceil(w/2), and r-1>=r/2 nonempty Y-subsets. These are distinct actual spectral sets, not duplicate descriptions. Their total mass is at least (1/2)p^(4(r-1))>1/162, using p^(r-1)>1/e>1/3. The latter follows from (1+1/(r-1))^(r-1)<e<3.

Physical pivotal counting gives I(2U-1)=2rw epsilon p^(r-1)=2w p^(r-1). The complementary clone has identical influence and mean probabilities a=p^r, b=1-a. Therefore I(F)=b I(2U-1)+a I(2U-1)=2w p^(r-1)<2w. The COMPLETE nonempty original mixed-reference cross entropy satisfies

    C_mix(F)>w^2/1296,
    C_mix(F)/I(F)>w/2592 -> infinity.                  (6)

The lower bound is uniform over BOTH independently chosen packing vectors, all their ordered covers, and alpha. Positive weights may be arbitrarily tiny: the A0 term in the choice of z handles this explicitly. Each summand retains its own D; no normalizers are pooled.

## Bounded entropy: this is not an FEI counterexample

For completeness, normalize the squared Fourier coefficients of indicator U by its total squared mass a=p^r. The resulting product measure has per-clause empty probability p and uniform nonempty mass epsilon. Its entropy is r[h2(epsilon)+epsilon log(r-1)]<=2w+log(e)<2w+3/2. The normalized nonempty spectrum of g=2U-1 is the nonempty part of this product law. Exact empty/nonempty decomposition gives

    H(g)<=1+4a(2w+3/2),
    H(g)/I(g)<4+9/(2w)<6.

For F, the four empty/left/right/joint sector masses are (2ab-1)^2, b^2 v0, a^2 v0, v0^2/4, v0=4ab. Their total coefficient for normalized nonempty-block entropy is v0(a^2+b^2+v0/2)=v0. Hence H(F)<=2+H(g)<8I(F), since I(F)>2w/3>1. No threshold theorem or FEI conjecture is used.

## Consequence and honest remaining line

The universal fixed-positive-prime PI-J route was already obstructed by A007. Even the proposed fixed TWO-polarity queue mixture fails for the full actual output law, despite universal one-root forests. Any posterior over actual partition forests is a subcollection of these runs and cannot create additional output mass. What remains viable is a genuinely different code: communicate a shared subdictionary/clause choice once for the WHOLE spectral set, instead of drawing that clause name again at many child visits; or use nonprime representations/a broader paid reference mixture. A dimension-free universal payment for that richer joint code is unproved. Equation (6) concerns reference cross entropy, while H(F)/I(F)<8, so it is NOT a disproof of FEI.
