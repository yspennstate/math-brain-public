# Independent challenge of the A086 -> A006 chain and A007

Verdicts: **HOLDS at stated scope** for A006-SUNFLOWER-POSTERIOR-FOREST-PAYMENT v1 and A007-SHARED-CORE-ROOT-CANCELLATION v1. A086's acceptance of A006 survives this second independent challenge. This does not accept A086's other claims or any universal FEI conclusion. No repair of either reviewed version was supplied.

The independent mechanism is to reconstruct the generator, enumerate ownership graphs and source components, and multiply chronological queue events, rather than import either author's checker. An additional all-dimensional stress test transports the lead's XOR-of-conjunction rank obstruction into A007's exactly zero-root-cost class and proves divergence of the **actual complete partition-run cost**, as well as its rank surrogate.

## 1. Full dependency chain

The source is `source_material/reductions/paper/forests.tex`, read in full, especially `eq:forestpacking`, `eq:forestconditioning`, `eq:forestcost`, and `thm:posteriorforest`. This is the lambda-child generator, not the public paper's different uniform-neighbour generator.

Independent roots with odds x_l=lambda_l*pi_l give empty-root mass product(1+x_l)^(-1). Put D=product(1+x_l)-1. Conditional probability of a specified nonempty root set R is product_{l in R}x_l/D. Thus Lambda+log2 Z=log2 D, including the sign of the conditioning term. Failed and infinite queues contribute no successful output mass; nonempty finite output requires a nonempty root set. The conditioned output reference is therefore a subprobability even without almost-sure termination.

For a partition of A among gates, draw edges from each owner to every other used gate containing one of its owned coordinates. One root per source strongly connected component and an outgoing spanning forest prescribe a finite once-per-gate run. Roots are queued in a fixed order; connecting-variable occurrences and chronological child-label draws prescribe subsequent queue order. The decoder unions the selected subsets. Every such run has positive probability and outputs exactly A.

For an owned subset of size s, the source's subset weights have sum at most 6 M s and elementary symmetric normalizer at most (6eM)^s: bound the order-weight sum by s+s^(6/5) integral_s^infty t^(-6/5)dt=6s, then use e_s <= (sum weights)^s/s! and s! >= (s/e)^s. The subset surprisal is consequently bounded by s log2(6eM), plus congestion and rank terms in B. Selecting sizes costs <=|A|log2 3. Selecting child counts costs <=|A|(1+log2 3), because (c+1)(c+2)<=2*3^c and number of used gates plus number of edges <=2|A| in the required separate accounting. More precisely sum c=number used-number roots and number used<=|A|. Selecting attachment multisets costs <=2|A|. A used gate has precisely one incoming label, either initial-root or child; label cost is summed once, not per owned coordinate. Therefore

    -log2 q(r) <= Lambda+log2 Z+K_ref |A|+B(A;r),
    K_ref=3+2log2 3+log2(6e).

For any finite collection of distinct actual runs, W(A)=sum q(r). The exact variational identity is

    E_eta[-log2 q]-H(eta) = -log2 W(A)+KL(eta || q/W(A)).

For the surrogate B the same identity gives inf(E B-H)=-log2 sum 2^(-B). These are different optimizers. Since W(A)<=Q_*(A), Gibbs with the binary empty/nonempty split proves the forest entropy bound. It retains h2(v). A fixed mixture of complete subprobability references with normalized weights remains a subprobability by nonnegative summation and costs log2(1/w_j) for a chosen component. No selected scale can lose that charge.

No regularity, pivotal antichain, or fractional-rank estimate from the later subsection of forests.tex is needed for these two claims. They use the elementary queue interface only. This closes the full dependency chain actually used here, without importing the threshold paper's analytic Theorem A.

## 2. A006: spectrum, exhaustive runs, and all-m bounds

Let b=product_{i=1}^m (1-x_i)/2. Then f=x0-(1+x0)b. Orthogonality gives P(empty)=4^(-m), P({0})=(1-2^(-m))^2, and each nonempty private T and {0}+T has mass 4^(-m). Physical edges give I0=1-2^(-m), Ii=2^(-m), and I=1+(m-1)2^(-m)>=1.

Use supports {0,i}, order (0,i), lambda=1/m, pi=1/4, a=2^(-6/5), D=(1+1/(4m))^m-1. A private coordinate has a forced owner. If 0 is absent all used gates are separate source components, hence all roots: one run. If 0 is present, its owner reaches every other used gate, and every other gate owns only its private coordinate and has no outgoing edge. This forces a star. For t=|T|, an inside root has t choices and (t-1)! ordered child sequences; an outside root has m-t choices and t! sequences. Thus counts are t! and (m-t)t!, respectively. These are distinct events in the actual generator: repeated attachment variable 0 does not make differently ordered gate draws the same event.

Summing residual weights yields exactly

    S_B({0})=1/4;
    S_B(T)=(a/(4m))^t;
    S_B({0}+T)=t! a^(t-1)/(4m^t) * [1+(1-t/m)a].

Reconstructing actual probabilities gives

    W({0})=1/[16(1+a)D];
    W(T)=D^(-1)[a/(16m(1+a))]^t;
    W_in=t!/[24 D t^2(t+1)m^t] [a/(4(1+a))]^(t-1);
    W_out=(m-t)t!/[8 D m^(t+1)(1+a)(t+1)(t+2)]
                       * [a/(4(1+a))]^t.

To check the factors independently: a private singleton with zero children costs a/[4(1+a)]. Inside-root size-two probability is 1/6, child-count probability 1/[t(t+1)], attachment multiset probability 1/t. An outside-root common singleton costs 1/[2(1+a)], child count 1/[(t+1)(t+2)], and attachment probability 1. Child names each cost 1/m. Multiplying root odds and summing ordered events gives the four expressions above.

Here 1/4<=D<e^(1/4)-1<1/3; the last sign follows termwise from exp(x)<1/(1-x) at x=1/4. The exact residual expectation is

    v log2 D+2(1-2^-m)^2
    +4^-m sum_{t=1}^m binom(m,t)
       [2t log2 m+(22/5)t+4/5-log2(t!)
                             -log2(1+(1-t/m)a)].

For an upper bound, discard only the identified nonpositive terms. Use sum t binom(m,t)=m2^(m-1) and log2 m<=m. The rare contribution is <=2^-m[m^2+(11/5)m+4/5]<=23/10: initial values at m=1,2 are 2 and 23/10, and 2P(m)-P(m+1)=m^2+m/5-12/5>=0 for m>=2. The dominant contribution is <=2. Hence R<=43I/10.

For complete probabilities, dominant cost is <4. Since (1+a)/a<5, private cost <=t(m+7). W_in alone gives common cost <=5+3m+t(m+5). The two rare sectors together cost <=2^-m(m^2+9m+5)<=15/2: its recurrence difference is m^2+7m-5>=0 for m>=1. Therefore C_m<=23I/2. With w_k=1/[(k+1)(k+2)] and lambda^(k)=2^-k/m, choosing k=0 pays v<=I, proving 53I/10 and 25I/2 for residual and complete cost including the prior, respectively.

For point-mass posteriors, every common singleton costs log2 m+2 and every other B is nonnegative. Since v log2 D>=-2v, residual >=(1-2^-m)^2(log2 m+2)-2v, and its ratio to I diverges. This is a fixed-representation obstruction, not an FEI counterexample.

All reported quantities exclude h2(v) unless explicitly included. In particular the complete-reference inference is H<=h2(v)+C_m, not H<=C_m. A086 stated this distinction correctly.

## 3. A007: arbitrary overlaps, actual roots, and suppression

Write F=2 A_r B-1, p=2^-r, b=E B, g=2B-1. Gates have shared relevant core C and data supports, root rarity pi_l=p rho_l<=1/2, and positive lambda with sum<=1. A positive Fourier coordinate of F must belong to at least one support. For a spectral U+T with U nonempty, assign all of U to one gate l0, and each data coordinate to a containing gate. Gate l0 reaches every used gate through any u in U. Its strongly connected component is the unique source: an edge from another component into it would make that component reachable in both directions. A star from l0 is consequently an allowed one-root partition forest. With U empty take a source-component forest; each used gate owns a distinct data coordinate, so 1<=K<=|T|. This proves existence of finite runs, not just abstract covers.

For every nonempty U+T, Fhat(U,T)=2p Bhat(T). Hence v=4pb(1-pb), I=p I(g)+2rp b, and

    E K-v <=4p^2 sum_T |T| Bhat(T)^2 = p^2 I(g).

The expectation is weighted by the unconditioned nonempty spectral mass; confusing it with a probability-one conditional expectation would destroy this estimate. Because r p<=1/2, r(E K-v)<=p I(g)/2.

Set s=sum lambda rho<=1 and D=product(1+p lambda rho)-1. Product expansion and exp give ps<=D<=exp(ps)-1<=ps exp(ps). Therefore delta=log2(D/(ps)) lies in [0,ps log2 e]. Substitution gives exactly

    T_root=v log2 s+v delta+r(E K-v)+E sum_roots log2(1/rho_l).

Since v<=4pb and 2ps/r<=1, v delta<=log2(e)*2rp b. Dropping v log2 s only after identifying it gives the claimed root-component payment. No data rarity or other coding term has disappeared.

For disjoint conjunction petals, Q=product(1-rho_l), b=1-Q. The complementary factor for petal l has total squared norm 1-rho_l and nonempty mass rho_l(1-rho_l). Product Fourier laws give sum_{T!=empty} Bhat(T)^2=Qb and sum_T K(T)Bhat(T)^2=Q sum rho_l. Thus E K-v=4p^2 Q(sum rho_l-b) exactly. The fixed mixture prior is valid on complete references and costs v for j=0. These prove every part of the reviewed statement at its original scope.

For core-only spectra, choosing the same core-first order on all gates gives identical core rank terms. Distinct singleton-root runs weighted by eta_l=lambda_l rho_l/s give expected label-plus-rarity minus root entropy, together with log2 D, equal to log2[D/(ps)]=delta by the finite Gibbs identity. Their actual subset normalizers can vary with l and remain in the complete cost; no equality for those unpaid normalizers is inferred.

## 4. Arbitrary seeds survive exact root cancellation

Take any Boolean h, t disjoint copies, and an independent fair sign z. The balanced seed g_t=z product_{j=1}^t h_j has H(g_t)=t H(h), I(g_t)=1+t I(h). Set B_t=(1+g_t)/2 and F_{r,t}=2 A_r B_t-1. Represent F as **one actual gate**, lambda=1. Its root probability parameter is pi=p/2, D=pi, K=1 on every nonempty set, and T_root=v log2 pi+v log2(1/pi)=0 exactly. It meets A007 with rho=1/2.

Direct Fourier multiplication gives

    H(F)=p t H(h)+2rp(2-p)
             +(1-p)^2 log2(1/(1-p)^2),
    I(F)=p[t I(h)+1+r].

For fixed r and nonconstant h, H(F)/I(F) tends to H(h)/I(h) as t grows. Therefore the best entropy/influence constant even on this exactly zero-root-cost class is the unrestricted FEI constant. In particular a universal O(I) bound on its complete nonempty reference costs would imply full FEI by H(F)<=h2(v)+cost and division by pt. Conversely a global FEI theorem bounds the class's entropy; it does **not** automatically bound this particular queue's cross-entropy. No equivalence of optimal queue constants is asserted.

This is the precise first unpaid line after A007: a bound for root normalizers supplies no control of the reference's remaining rank/label/subset costs on arbitrary data gates. It does not invalidate A007, which explicitly leaves them unpaid.

## 5. XOR-of-AND stress: zero root bill, diverging actual partition cost

This section independently reconstructs the lead's rank obstruction through a cardinality-moment identity, then applies it to A007 and to actual complete queue probabilities. No priority claim is made for the original XOR rank obstruction.

Let d_L=1-2 A_L on L coordinates, q=2^-L, and g=product_{b=1}^m d_L^{(b)} on disjoint blocks; n=mL. Let S be its spectral sample, K=|S|, and

    R_pi(g)=E sum_{j=1}^{|S|} ln(i_j/j),

where i_j are the positions of its selected coordinates in any full physical order pi. Every coordinate has influence d=2q. Therefore for **every** order,

    R_pi=d ln(n!)-E ln(K!).

This is exact: the numerator sum is sum_i P(i in S)ln(position_i)=d ln(n!), while the denominator sum is ln(K!). No independence within a block and no averaging over coordinate orders are required.

For one block E K=2Lq and E K^2=q L(L+1). Product blocks imply

    I=2mLq,
    E K^2/I=I+(L+1)/2-2Lq.

Use ln(n!)>=n ln n-n, ln(K!)<=K ln K, and Jensen for the size-biased probability law k P(K=k)/I. It follows that

    R_pi/I >=ln n-1-ln(I+(L+1)/2).

With m=4^L, the last expression is >=(L-1)ln2-5/4. Indeed (L+1)/(4mLq)<=1/4 and ln(1+x)<=x. The elementary atanh expansion yields ln2=2 sum_{j>=0}(1/3)^(2j+1)/(2j+1)>=2/3, so also R_pi/I >=(8L-23)/12. The all-L divergence is proved analytically; no huge truth table is computed.

This family satisfies H(g)<=4I(g). For one block the empty-atom contribution is <=4q log2 e, by -x ln x<=1-x, and its other contribution is 8q(1-q)(L-1). Dividing by 2Lq gives at most 4-(4-2log2 e)/L<=4, since ln2>=2/3>1/2. Disjoint tensor additivity proves the claim. Thus a diverging rank surrogate here cannot be confused with a diverging FEI ratio.

Now fix r>=1, let B=(1+g)/2 and F=2 A_r B-1. Again a single gate and lambda=1 give **exactly zero root block**, even though rho need not be 1/2. All coordinates are relevant. For any order of the full activated cube, take its induced data order. At a selected data coordinate, its full position is at least its data position and its full predecessor denominator is at most j+r<=(r+1)j. Summing over all core subsets, the spectral mass at every nonempty data T is p P_g(T). Core contributions are nonnegative. Hence

    R_pi(F)>=p[R(g)-I(g)ln(r+1)],
    I(F)=p[I(g)+2r E B]<=p[I(g)+2r].

Since ln(r+1)<=r, whenever the numerator below is positive,

    R_pi(F)/I(F) >= [(8L-23)/12-r] I(g)/(I(g)+2r).

For m=4^L, I(g)=2L2^L; the lower bound diverges uniformly over **all** full orders for each fixed r. This directly obstructs A007 -> an absolute rank payment in the single-gate, single-full-order representation, even after perfect root cancellation.

There is also an obstruction to **actual complete partition-run cost**, not just B. A single gate has exactly one partition run for each A: select A once and zero children. Conditioning makes its root certain. For s=|A|, its actual probability is

    q(A)=[1/(2s(s+1))] * product_{i in A} min(1,(s/rank(i))^gamma)/Z_s.

The first s ranks all have weight one, so Z_s>=1. Thus

    -ln q(A)>=gamma sum_{j=1}^s ln^+(i_j/s)
              >=gamma[sum_j ln(i_j/j)-s].

The last inequality uses s ln s-ln(s!)<=s. Averaging gives complete all-partition cross-entropy C_F >=(gamma/ln2)[R_pi(F)-I(F)], which diverges relative to influence along the family. The residual itself equals (gamma/ln2)R_pi(F), because root rarity cancels, M=1, and congestion is zero. There is no latent partition-run entropy to subtract in a single-gate representation.

This refutes only the proposed **extension** that A007's root payment plus one full gate order suffices for absolute complete partition cost. It does not refute A006, A007, alternative representations, multiple covers, or the potentially greater output mass of successful repeat-visit queue runs. It is not a Boolean FEI counterexample. F is a conjunction of a core event with an XOR of disjoint conjunctions and is itself in the established read-once formula class.

A direct bound also shows the actual stress functions have bounded entropy/influence without importing a formula theorem. Partition their spectrum by whether the data set T is nonempty. That event has mass t=p Var(g). Given it, the core subset is uniform and the data spectrum is P_g conditioned on nonempty. Given its complement, only r core bits remain. Hence H(F)<=h2(t)+r+p Var(g)H(P_g | T!=empty)<=1+r+p H(g)<=1+r+4p I(g). Consequently H(F)/I(F)<=4+(1+r)/(p I(g)), tending to at most 4 for fixed r along m=4^L, despite divergence of its partition-reference cost.

## 6. Exact execution and independence

Before the pilot, FROZEN_SPEC.json fixed 10 sunflower/auxiliary-theta pairs with m<=5, all 810 activations of nonconstant truth tables on 1..3 bits at r=1..3, and nine XOR cases with physical dimension <=8. The independent checker uses integer FWHT, physical edge counts, Fraction probabilities, and formal coefficients of ln(k), with no author code import. Ownership graphs, reachability/source components, parents, child permutations, chronological traces and direct probabilities are generated independently. Rational theta values 2/5 and 1/2 check the algebraic probability formulas; the analytic proof above supplies the actual irrational 2^-6/5 and all-dimensional bounds.

Command: `python -X utf8 runs/20261011T224936Z-fleet05-A094-proof-chain-challenger/code/check.py --freeze`, then the same command without `--freeze`. Saved result: 42,168 assertions, 1,750 actual partition runs, 810 activations, nine XOR parameter pairs, zero failures, 26.5323294 seconds. Maximum estimated memory 40 MB; no heavy job, background service, GPU, or automatic dimension escalation. Activation checks certify the spectral suppression upper bound with K<=|T|; the analytic construction above, rather than that bound alone, certifies the actual allowable star forests. The heterogeneous-petal identity is independently proved by tensor factorization above; no finite logarithmic check stands in for it.

Original A006 and A007 versions retain their exact statement hashes. The local CLAIMS.json appends this independent acceptance only, with no shared registry mutation. The new combined zero-root-cost boundary claim is author-proved and awaits A085/A095 independent review.
