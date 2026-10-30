# Repeated-fallback controller payment and a global priority potential

All cubes are finite and uniform; outputs are signs, Fourier coefficients normalized, entropy in bits. Write phi(t)=t log2(1/t), Phi(a,b)=phi(a)+phi(b)-phi(a+b), with zero endpoints by continuity. All physical query probabilities are 1/2.

## 1. The actual repeated core, rather than an independent replacement

At an actual node let F=A u+(1-A)G, where A is a live point indicator on s>=1 fresh remaining controls, p=2^-s. The Boolean u uses a data block disjoint from the entire fallback G. G has any exclusive controller on independent data cores v_j and constant states, disjoint from A. Already exposed data are conditioned on; the remaining means may have any bias. Put y=Eu, x=EG, g(z)=E_data G(z,data), Vg=Var(g), W=sum_j b_j Var(v_j). Then W+Vg=1-x^2. This uses the actual same fallback on both query children. The queried A bit has d=p(1-xy); it is not p(1-x^2)/2 or a mismatch of independent fallback copies.

Merge duplicate descriptions of a physical core. For every live selector q_j define R=sum_j phi(q_j) Var(core_j). A controller query has kappa=R-average R_child>=0, by concavity of phi. Core means, variances and own-history reserves remain fixed at this query. The new core u has probability p before the query and 0,2p afterwards, hence its contribution to kappa is p Var(u).

## 2. Exact erasure decomposition

Let delta=g-y, with Fourier coefficients on the fallback controls. A nonempty u-data row has equal magnitude A-bit Fourier amplitudes, so its total erasure is exactly p Var(u), cancelling that part of kappa. A nonempty v_j-data row has selector C_j(1-A). Product homogeneity of Phi shows its erasure is

    b_j Var(v_j) c(p),
    c(p)=p-2p^2+Phi((1-p)^2,p^2).

Its kappa contribution is b_j Var(v_j) k(p), where

    k(p)=phi(1-p)-[phi(1)+phi(1-2p)]/2 >=0.

The factors log(1/b_j) cancel because probabilities have the same fair mean. This remains true for arbitrary spectra of C_j; only Parseval sum Chat_j^2=b_j is used. Constants have zero variance. The exact empty-data erasure is

    Bprofile=(p-2p^2) E(delta^2)
             + sum_T Phi((ghat(T)-p*deltahat(T))^2,p^2*deltahat(T)^2).

To check the coefficient p-2p^2, the remaining point block has 1/(2p) frequencies, each nonempty pair has magnitude p*|deltahat(T)|, and Phi(a^2,a^2)=2a^2. Thus the complete exact formula is

    B_A-kappa=Bprofile+[c(p)-k(p)]W.                 (E)

No sign is needed for c-k in the upper-bound argument. In particular this proof does not claim every signed residual is nonnegative.

## 3. Constant price independent of all point widths and fallback complexity

The independently reconstructed scalar bound b(t)=2t(1-t)+Phi((1-t)^2,t^2)<=3t implies c(p)=b(p)-p<=2p. Its proof: for 1/4<=t<=1/2 use Phi(a,b)<=2sqrt(ab); for 0<t<=1/4 use Phi(a,b)<=b log2(e(a+b)/b) with a+b<=1 and the increasing upper envelope 2(1-t)+t[2log2(1/t)+1/ln2], whose endpoint is 5/2+1/(4ln2)<3. For t>=1/2 use symmetry. The inequalities ln2>1/2 and endpoint cases close the numerical guard.

For real amplitudes Phi(a^2,b^2)<=2|ab|. One proof scales to amplitudes 1,z, 0<=z<=1: the derivative of [(1+z^2)ln(1+z^2)-z^2 ln(z^2)]/(2z) has nonnegative numerator (z^2-1)ln(1+z^2)-z^2 ln(z^2), by ln(1+w)<=w and -ln w>=1-w. Its maximum is ln2 at z=1; scale back. Consequently

    Bprofile <= p E(delta^2)+2p sum_T |ghat(T)deltahat(T)|
             = p[3Vg+(x-y)^2+2|x(x-y)|].

Since k(p)>=0, (E) gives

    B_A-kappa <= p[3Vg+2W+(x-y)^2+2|x(x-y)|]
               <= p[3(1-x^2)+(x-y)^2+2|x(x-y)|]
               <= 8p(1-xy)=8d.                   (B)

Here is the entire last scalar proof, including zero influence. Simultaneously flip both x,y so x>=0. If y<=x the bracket is 3+y^2-4xy<=4(1-xy). If y>=x it is 3-4x^2+y^2<=4(1-x^2)<=8(1-xy), because y<=1, xy<=x and 1-x^2<=2(1-x). If d=0, x=y=1 or x=y=-1 and every term vanishes.

For the normalized physical Boolean child spectra, J<=2d/ln2. This follows pairwise from natural binary divergence L(t)<=(1-sqrt(1-t^2)), since L'(t)=atanh(t)<=t/sqrt(1-t^2); differentiation proves the latter from t=0. Summing pairwise 2 min(a^2,b^2)/ln2<=2b^2/ln2 yields the full physical rate. Together with (B),

    D_A-kappa <= (8+2/ln2)d <11d.                  (P)

The strict rational guard ln2>2/3 follows from the first positive term of its atanh series, so 2/ln2<3. No floating constants or independence substitution occurs.

## 4. Complete global potential, initial condition and every boundary

Take an arbitrary finite ordered priority list of point events A_1,...,A_m on mutually disjoint fresh control blocks, each selecting a Boolean core u_j on its own independent data block, with a final constant sign. Controls are queried in priority order: continue the earliest unresolved live event until success or failure; on failure move to the next event; on success all lower events become irrelevant. Data queries can be adaptively interleaved at any time, while respecting prescribed own-history core trees. A seed, if used, is independent and fixed initially. Duplicate core labels must be merged; the theorem assumes distinct independent cores in the priority list.

For each current core let r_j>=0 satisfy D_j<=C d_j+r_j-average r_j,child on its prescribed tree, C>=0. No bound on its initial value is assumed. Define

    Q_t=sum_j q_j(t) r_j(t)+sum_j phi(q_j(t)) Var(u_j,t).

At data queries the already independently reviewed A064 additional-v2 lift applies conditionally to the current controller: D_F<=(C+11/2)d_F+Q_t-average Q_next. At a controller query the first sum has zero fair-average drift since each q_j is a martingale, and (P) applies with u the earliest event's core and G the actual fallback priority function, on disjoint physical blocks. Thus D_F<=11d_F+Q_t-average Q_next. The same potential works on every finite adaptive policy in this declared priority order; no core-history tree is reset or core resource renewed after a controller query.

Initial condition:

    Q_0 <= sum_j q_j(0) r_j(0)+2 I_ctrl(F_0).

The rarity estimate is the reviewed original-edge proof: indicator isoperimetry I(C_j)>=2q_j log2(1/q_j), and for each actual control edge switching independent cores j,k the inequality Var(u_j)+Var(u_k)<=2(1-m_j m_k) gives sum_j Var(u_j) I(C_j)<=4 I_ctrl. One edge is charged once.

At any finite adaptive stopping time tau,

    E Q_tau <= Q_0+C Pi_data,
    H(F_0) <= (C+11/2)Pi_data+11Pi_ctrl+Q_0+E[H(F_tau)-Q_tau].

For expected-terminal control, core entropy drops are nonnegative, so E r_child<=r+C d_core. Weighted core reserves grow by at most C*d_F at data queries; their mean is unchanged at controller queries. Variance-rarity decreases at both types. Finite conditional summation proves the displayed expectation without assuming nonnegative signed entropy debt. Pi_data and Pi_ctrl are physically reached queried-influence sums, each original influence unit used once.

At a controller-resolved frontier Q_tau is precisely the selected remaining core reserve (constant state zero), and the boundary is H(selected core)-r_selected, not zero. At a complete-data frontier r=Var=0 if core leaves have zero reserve, hence Q_tau=0, but the actual remaining controller entropy must still be included. At a complete controller-and-data frontier both H and Q are zero. No other frontier replacement is allowed. For a declared full completion, alpha=max(C+11/2,11), finite Bellman induction gives the least nonnegative alpha-priced reserve at every node at most Q_t, with terminal zero. This is a true growth-controlling nonnegative reserve, not just signed telescoping.

An optional explicit initial certificate sum_j q_j r_j(0)<=K I_data(F_0), K>=0, gives H(F_0)<=max(C+11/2+K,13) I(F_0) on completed trees. This is conditional on the actual inherited core certificates and is not universal FEI.

## 5. The source's shared-X priority geometry

If a shared bit X gates two priority events in the same orientation, query X first among controls (arbitrary data can precede it): one child is constant, paid by A087's reviewed one-sided rate 3+2/ln2<11. Its live child is the priority function above, of arbitrary private widths. In opposite orientation the X children are independent private activations, paid at 4+2/ln2<11, followed by ordinary point overrides. This closes X,A,data,A at r=2,s=1 and all larger private widths under the declared ordered control policy. It does not repeat the already-paid A028 fixed-data block suffix.

## 6. Exact remaining line

The theorem's first unsupported universal extension is: choose an ordered disjoint-point independent-core representation and inherited r_j for every Boolean function with sum_j q_j r_j(0)=O(I_data), using only unspent physical influence. Arbitrary overlapping controllers or shared physical data do not satisfy this geometry. No arbitrary controller boundary or arbitrary seed-core price is obtained. The next useful test is a single repeated-core reveal with an overlapping, non-point continuation, retaining the actual sector rows, inherited reserve and both physical child bills.
