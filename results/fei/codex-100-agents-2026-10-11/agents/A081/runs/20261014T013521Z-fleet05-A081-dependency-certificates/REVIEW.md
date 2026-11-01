# Complete refunds, coarsening debt, and exact dependency scope

Uniform finite physical cubes, Boolean signs, normalized squared Fourier law p, ordinary pivotal influence e_i and I=sum e_i. Every entropy and KL is in bits. This stage independently reviews A090-DEGREE-COARSENED-REFUND-OBSTRUCTION v1, consumes existing full scoped reviews of A096 and A097, and supplies a narrow spectator-compatible information contract. No arbitrary terminal reference is assumed to have paid cross entropy.

## 1. Arbitrary partitions must retain their conditional refund

For a relevant coordinate, mu_i(T)=p_(T+i)/e_i and r_i(T)=p_T+p_(T+i) are complete probability laws. On true support r_i>=e_i mu_i>0. Expanding the logarithm gives

    L_i=e_i[log2(1/e_i)-D(mu_i||r_i)]
       =sum_T p_(T+i)log2((p_T+p_(T+i))/p_(T+i)).

Let C be ANY deterministic finite partition of the entire residual subset space. Zero true cells retain their reference mass; they must not be deleted or renormalized. Write mu_C,r_C for pushforwards. Factoring mu_i(T)/r_i(T) into its cell-marginal and within-cell factors yields the exact chain rule

    D(mu_i||r_i)=D(mu_C||r_C)+W_i(C),
    W_i(C)=sum_c mu_C(c)D(mu_i(.|c)||r_i(.|c))>=0.

Hence L_i^C=L_i+e_i W_i(C), with L_i^C=e_i[log2(1/e_i)-D(mu_C||r_C)]. Summing gives L^C-L=sum_i e_i W_i. A proof that substitutes the coarse divergence has to pay or retain this exact quantity; data processing alone has the opposite direction from a claimed recovery of discarded refund. No choice of coarse-law labels supplies an automatic budget for W.

The hybrid reference r_tilde(T)=r_C(c)mu_i(T)/mu_C(c) on positive true cells, using the original conditional r on zero true cells, is complete, normalized, and positive on true support. Its KL is precisely the coarse divergence. Thus the coarse retained price corresponds to an honest function-specific reference, not merely a malformed law. The missing conditional refund is nevertheless real.

There is a useful exact spectator contract. For f(x)g(y) on disjoint physical blocks and a relevant coordinate i of f,

    mu_i^(fg)=mu_i^f tensor p_g,
    r_i^(fg)=r_i^f tensor p_g,
    e_i(fg)=e_i(f).

Therefore full row KL equals D(mu_i^f||r_i^f), even when the active core row is not a product law. For ANY spectator partition C_g, keeping (full core residual subset,C_g(spectator subset)) also preserves this KL exactly, because both pushforwards share the same spectator factor. Its discarded W is zero. Keeping only (core degree,spectator degree) preserves only the original CORE-DEGREE KL, not the full core refund. Keeping the TOTAL degree can further mix these distinct factors. These are likelihood-ratio identities, not spectral-reference CE bounds and not permission to borrow spectator influence.

On the actual core that is negative only at zero on three bits, tensored with the four-bit quadratic bent spectator, coordinate i=0 has e_i=1/4. Its full row divergence is 1-(1/4)log2 5. The exact positive discarded total-degree refund is

    W=(3/32)log2 11+(15/64)log2 13-(65/64)log2 5
      +(19/64)log2 3+(15/64)log2 19.

The exact checker verifies the chain identity by cancellation of prime coefficients. W is nonzero by unique prime factorization and is nonnegative by the conditional KL representation, hence strictly positive. The protected full-core/spectator-degree partition has W=0. This core derivative/reference row is genuinely non-product: its vacuum residual probability differs from the equal probabilities of the other three residual atoms, and fails their two-bit product relation. No relaxed spectral vector is used.

## 2. Independent review of A090 degree obstruction v1: HOLDS

Take w>=4, m=2^w, p=1/m, beta=1-p, n=mw, and the actual OR sign f=1-2 product_b(1-A_w). A factor 1-A_w has Fourier coefficient beta at empty and -p elsewhere. After dividing its squared spectrum by its norm beta, a block is empty with probability beta and active with probability p, with a uniform nonempty subset when active. Let xi(t)=binomial(w,t)/(m-1) for 1<=t<=w. Under the resulting independent block law nu, the active count is Bin(m,p), mean one. The actual Boolean squared degree masses are

    W_0=(1-2beta^m)^2, W_t=4beta^m nu_t for t>=1.

Pivotal counting gives e=2p beta^(m-1), I=2w beta^(m-1). Coordinate transitivity suffices (full fixed-degree exchangeability is neither true nor assumed) for the exact degree-row laws

    mu_bar(t)=(t+1)W_(t+1)/I,
    r_bar(t)=(1-t/n)W_t+(t+1)W_(t+1)/n.

A different probabilistic representation of mu_bar is Bin(w-1,1/2) plus m-1 independent active-block degrees. Its mean is w-1/2, and mu_bar(0)=e. We check both representations independently by an occupancy-count mixture, not by copying A090's checker.

Here is the key all-width domination. For t>0 the selected block's Bin(w-1,1/2) mass divided by xi(t) is 2beta(w-t)/w<=2beta; its zero mass is 2p. For the latter component, Bin(m-1,p) has likelihood ratio (m-j)/(m beta)<=1/beta against Bin(m,p). For the former, forcing one active block gives ratio j/(mp)=j. On total degree t every active block contributes at least one, hence j<=t. Summing their positive kernels proves

    mu_bar(t)<=(2p/beta+2beta t)nu_t, t>=1.

For all w>=4, elementary logarithm inequalities and positive series prove 1/4<=beta^m<3/8 and e^-1<=beta^(m-1)<=1/2. Specifically ln(1-p)>=-p/(1-p) and <=-p, ln2>2/3 from the first positive atanh term, and 8/3<e<3 from its positive factorial series. The reciprocal binomial expansion gives beta^(m-1)<=1/2. These are proved scalar comparisons, not floating-point signs.

Thus r_bar(0)>=1/16 while mu_bar(0)=e<=p<=1/16, so the zero-degree KL term is nonpositive. On 1<=t<=n/2, r_bar(t)>=2beta^m nu_t and the preceding domination gives mu_bar/r_bar<=4(t+1). The head contribution is at most 2+E log2(T+1)<=2+log2(w+1/2). Markov gives tail probability at most 2/m, while the complete reference inequality r_bar>=e mu_bar bounds its log ratio by log2(1/e)<w+1/2. The tail is therefore at most 2(w+1/2)/2^w<=9/16<1. Consequently

    0<=D(mu_bar||r_bar)<=3+log2(w+1/2),
    L_degree/I>=w-4-log2(w+1/2).

For w>=32, log2(2w)<=w/4 by its value at 32 and monotone positive difference derivative 1/4-1/(w ln2). Also 4<=w/4, so L_degree/I>=w/2.

The full bill remains bounded; we reconstruct it rather than assume FEI for this class. A nonempty set meeting j blocks has mass 4p^(2j)beta^(2(m-j)). Under nu, E j=1. Directly summing its atom entropy yields

    H=h(W_0)+8w beta^m-8beta^m log2(beta)[m(1-beta^m)-1]
      -8beta^m(1-beta^m),
    h(t)=-t log2 t.

Since h(W_0)<=1 and m(-log2 beta)<=m/(m-1)/ln2<8/5 for m>=16, H<=8w beta^m+13beta^m+1. Divide by I, use beta<=1 and beta^(m-1)>1/3, to obtain H/I<=4+8/w<=6. Each oriented edge charge L_i is nonnegative, is at most its binary edge entropy B_i, and B<=H by conditioning and the entropy chain rule. Hence 0<=L<=B<=H<=6I. The exact partition identity from Section 1 implies (L_degree-L)/I>=w/2-6. This proves the entire original A090 statement, including the unbounded discarded refund on actual Boolean signs, without a repair contribution.

The named w=4 certificate checks all 64 degree packets, exact normalization, both degree-law representations, every likelihood domination, the true derivative mean, head/tail bounds and physical influence. It is a finite implementation check. The preceding derivation, not extrapolation, proves every width and the infinite mechanism obstruction.

## 3. Source-bound review intake and the universal unpaid leaf

The full A096-TERMINAL-KL-REFUND-AUDIT v1 has saved substantive independent reconstructions by A073, A001, A099 and A100. This stage binds the A001 record to the literal source statement/hypotheses and its normalized-law scope. It does not relabel those reviews as a new A081 reconstruction. A097-ONE-SHARED-DATA-COLLISION-TRANSFER v1 and A086's disjoint predecessor have saved full A094 reconstruction, read here together with their proof sources. Import them only with the one-shared-bit or explicit l1-admission/dimension-dependent clauses, full calibrated terminal CE and the averaged actual shared influence. A094's separate balanced-tensor extension is still an author claim, not part of that accepted source version. Its one-node A097 review does not supersede A081's earlier full finite-tree reconstruction or establish a second integrated graph review.

For clarity, a paid KL lower bound would need one finite K and every Boolean seed:

    D(P_joint||Q_joint)>=Gamma(f)-K,
    Gamma=sum_i(e_i/I)log2(1/e_i).

Then L<=KI. The elementary complementary charge x log2(1+y/x)<=y/ln2 gives L<=B<=L+I/ln2. The already reconstructed C018 implication would give FEI at K+3/ln2. Conversely FEI bounds L<=B<=H, so finiteness of such K is FEI-equivalent. No lower bound of this strength is proved. A090's accepted degree obstruction forbids replacing the full divergence by its degree marginal in this proposed shortcut. The general KL reference and the complete A096 audit are not refuted.

A001's fixed-low-degree/single-tail obstruction is recorded as a source-complete pending claim, with the full-support and I->0 hypotheses preserved. This stage does not independently accept that separate compound argument. It reinforces dispatch, not a hidden proof premise for the accepted A090 result.

The shortest next step is one named signed-Boolean payment of the retained conditional W, tested on a non-product active core with independent spectators and on actual tribes. A map that preserves the full seed divergence passes the information contract, but still has to pay Gamma-D from a single influence budget and retain complete terminal CE. Merely keeping additional labels is not a new payment theorem.
