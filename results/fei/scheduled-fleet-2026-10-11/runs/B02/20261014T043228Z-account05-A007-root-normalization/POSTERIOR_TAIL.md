# Uniform ownership-entropy tail under the original full-cell posterior

All entropy is in bits. Gamma=6/5 and delta=gamma-1=1/5. For integers s,N>=1, consider exactly A015's retained base surrogate posterior on k used gates and ordered positive sizes v=(v_1,...,v_k), where 1<=k<=min(N,s), sum v_i=s:

    W_(k,v)=binom(N,k) N^(-k) (s)_(k-1)
                    [s!/prod_i v_i!] prod_i (v_i/s)^(gamma v_i).

The sizes are ordered by increasing chosen gate ID. No k! is inserted. Let Z=sum W and normalize to probability W/Z. Write H(v/s)=-sum_i(v_i/s)log(v_i/s). Then, for EVERY s,N and every real h>=0,

    Pr_W[H>=h] <= min{1, C_s 2^(-s h/5)}
                <= min{1, 6^(s-1) 2^(-s h/5)},
    C_s=sum_(k=1)^s binom(s-1,k-1)(s)_(k-1)/k!.

Consequently

    E_W H <= 5 log(6)(1-1/s)+5 log(e)/s <=5 log(6)<13.

For s=1, H=0 exactly; the displayed bound remains valid. This controls the SAME old posterior: root choices, actual chronological multiplicities, finite N label factors and old congestion are already in W. It is not a replacement uniform ownership law, not an actual-queue posterior, and not a universal FEI theorem.

## Recordwise entropy damping

Put A(v)=prod_i(v_i/s)^(v_i)=2^(-s H). The multinomial probability of exactly these counts under independent categorical sampling with probabilities v_i/s is [s!/prod v_i!] A(v)<=1. Thus

    W_(k,v)<=binom(N,k)N^(-k)(s)_(k-1) A(v)^delta
            <= [(s)_(k-1)/k!] 2^(-delta s H).

Here binom(N,k)N^-k<=1/k!, since (N)_k<=N^k. The k=1 record has weight EXACTLY one, so Z>=1. There are binom(s-1,k-1) positive ordered compositions of s of length k. Summing the recordwise bound over the tail proves the first inequality. This sums finite-N labels and factorial tree credit before paying entropy; bounding those pieces separately by powers of s would lose the dimension-independent result.

## A rational combinatorial growth bound

Put n=s-1 and j=k-1. Since (s)_j/(j+1)!=binom(n+j,j)/(j+1),

    C_s=sum_(j=0)^n binom(n,j)binom(n+j,j)/(j+1)
         <=D_n:=sum_(j=0)^n binom(n,j)binom(n+j,j).

Derive the identity D_n=sum_(j=0)^n binom(n,j)^2 2^j directly by Vandermonde: binom(n+j,j)=sum_l binom(n,l)binom(j,l); interchange the sums and use binom(n,j)binom(j,l)=binom(n,l)binom(n-l,j-l), then sum j. This yields sum_l binom(n,l)^2 2^(n-l), and reindexing gives the displayed identity.

All terms are nonnegative, so

    D_n <= [sum_(j=0)^n binom(n,j)2^(j/2)]^2
          =(1+sqrt(2))^(2n)=(3+2sqrt(2))^n<=6^n.

For n>0 the last inequality is strict because 2sqrt(2)<3, proved by squaring positive quantities (8<9). For n=0 it is equality. The proof uses no asymptotic coefficient estimate. C_s is handled exactly as a rational sum; only its upper bound is used.

## Tail integration and the universal constant

Let h0=5(s-1)log(6)/s. Integrating Pr(H>h) over h>=0 gives

    E H <=h0+integral_(h0)^infinity 6^(s-1)2^(-s h/5)dh
         =5(s-1)log(6)/s+5/(s ln 2).

Because e<3<6, log(e)<log(6), this is <=5 log(6). The elementary bound e<3 follows, for example, from sum_(m>=0)1/m!<1+1+sum_(m>=2)2^(-(m-1))=3. Finally 5 log2(6)<13 is exactly 6^5=7776<8192=2^13. These constants are certified without a floating logarithm.

## Verify the retained W law and A015's scope

For N full-cell AND gates on m data coordinates with common full orders, lambda=1/N and rarity pi=2^-m, every nonempty selected T of size s has complete ownership-incidence graph on its used gates. If a used gate owns v_i selected coordinates, put q_i=sum_(j owned by i)x_j and X=sum_(j in T)x_j. The root-i incoming minor is q_i X^(k-2) for k>=2, and the k=1 minor is one. Sum root rarities to get pi X^(k-1), whose factorial moment is pi(s)_(k-1). This follows by direct determinant column expansion and multinomial composition counting, not an independent-root prior. The common rank factor depends on T but not on the assignment; keep it in S(T) and cancel it ONLY in the conditional posterior law.

Choose k IDs in binom(N,k) ways and partition the s LABELLED coordinates among them in s!/prod v_i! ways. Their labels contribute N^-k and congestion contributes prod(v_i/s)^(gamma v_i). Multiplication proves W exactly. Every assignment/root/attachment/local child sequence represents a distinct actual base partition event; actual probabilities still contain separate size/count/subset/multiset factors. Thus the theorem applies to the exact surrogate posterior used in the distributed-core lift, with no missing tree factor or free witness name.

The full-cell cover of a general B need not be its full prime table. This scoped extension is a valid fixed cover, because none of the trace, mass or rank proofs require primeness. It is PI-J literally for parity's positive full cells, where every implicant must fix every coordinate. Arbitrary-support prime tables can have kappa_l<s and are not covered by this conditional entropy theorem.

## Root normalization and paid controller correction

For the same full-cell cover, c=1 in every assignment, beta=1 and L_0=1. A015's fixed-assignment envelope Z_tau(u)>=2^(-u H(v/s)/5), proved independently in REVIEW_A015.md, yields with the unchanged posterior

    J_dist,U(T)>=E_eta_T 2^(-u H/5)>=2^(-u E_eta_T H/5).

Write the SIGNED exact debt before bounding its normalizer:

    Psi_dist=p Var(g)log[D'/(pD)]
               -p sum_(T nonempty)P_g(T) E_(U uniform)log J_dist,U(T).

The empty U contribution is zero. Our tail theorem and E|U|=r/2 therefore give

    Psi_dist <=p Var(g)log[D'/(pD)]+(pr/2)Var(g)log(6)
              <=(1-b)log(6) I_core(F)<=log(6) I_core(F),
    b=E B, I_core(F)=2rp b, Var(g)=4b(1-b).

The normalizer inequality D'<=pD is applied only AFTER the signed expression: prod(1+t lambda pi)-1 has nonnegative coefficients of positive degree and t=p<=1. No negative log Z is dropped in obtaining or testing its role. Core-only root/name cancellation and the inherited whole-set cost remain as in the actual-trace lift. For every nonconstant B under this fixed full-cell cover, the resulting scoped transfer is

    R_F <=p R_g+(7/2)p I(g)
            +[6/5+log(e)/4+(1-b)log(6)] I_core(F).

Here R_g is the COMPLETE original surrogate residual, including its signed normalizer and physical rank/location cost. It is not replaced by H(g), not set to zero, and not universally paid by this theorem. h2(Var F)+K_ref I(F) also remain outside the residual. This closes A015's proposed posterior-tail step and its controller correction, not the conjecture.

## Exact first unsupported line

Full FEI still requires a dimension-independent influence payment for the inherited full-cell base reference R_g, or a transfer of this posterior-tail argument to efficient arbitrary-support prime tables under the SAME complete posterior. For the live PI-J packet, the first unpaid general line remains Psi_dist<=K I(F) when selected gate intersections differ, with feasible global scale labels and unequal-width component rarities retained. The full-support tail is now closed; another full-support concentration search would repeat a settled interface.
