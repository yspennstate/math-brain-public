# One original influence reserve pays sparse inherited-reference resets

All entropies and KL divergences use base two. Every physical input is a fresh uniform bit. The result pays the ADDITIONAL reference-reset reserve; the original incoming KL and full terminal Fourier entropy remain in the account. It is not a proof of FEI.

## 1. Statement with the original owner

Let n>=2 and g_n=1-2*1[x=0]. Its squared Fourier law on subsets of [n] is

    d_n=2^(1-n),  p_n(empty)=(1-d_n)^2,
    p_n(S)=d_n^2 for S nonempty,
    Inf_j(g_n)=d_n,  I(g_n)=n*d_n.

Supply ONE normalized original spectral reference R_n supporting p_n. Its nonempty conditional law must be

    R_n(S | S nonempty)=delta^|S|(1-delta)^(n-|S|)
                         /[1-(1-delta)^n],
    0<delta<=d_n.

The empty mass may be ANY number strictly between zero and one. In particular the actual marginal product reference with parameter d_n qualifies, but R_n is not required to be a product. After every physical query transport this SAME reference with the actual normalized erasure/physical kernel; do not reset it. A policy may query any remaining coordinate adaptively, stop without conversion, or at its stopping cut convert ONCE to the product of the current actual spectral marginals. Conversion is terminal; no post-conversion continuation is included.

At a reached history rho write K=KL(p||R), TC=KL(p||product(actual marginals)), and I for actual current influence. Then

    [TC-K]_+ <= (5/3) I.                                  (1)

With E>=0 the erasure conditional KL and O=KL(fair physical outcomes || reference-predicted outcomes), define the least pending conversion reserve on the finite history tree by

    B_rho=max([TC-K]_+, max_i(mean B_child-E_i)).

Every admitted adaptive policy and stopping cut obeys

    0<=B_rho<=(5/3) I(g_rho),                             (2)
    E KL_terminal + E sum O + (5/3) E sum queried Inf
        <= K_initial+(5/3) I_initial.                    (3)

The terminal KL is to the actual inherited reference if there is no conversion, and to the actual product if there is conversion. Add E H(g_terminal) to both sides to retain the complete terminal cross entropy. No terminal H is removed.

The original additional owner is (5/3)I_initial, booked ONCE. At ordinary queries, influence conservation accounts for the same owner: current influence plus all prior queried influence is a martingale. Formula(3) prices both the prior physical debit and the terminal reset from that original owner. If the caller has an already paid unrelated omega, it stays spent. If an earlier theta is the pending booking for a nested subclass of these same policies, enlarge to the cap by topping up only (5/3)I_initial-theta. A previously consumed debit cannot be relabeled pending theta. Availability of the original owner is a hypothesis, not a consequence of computing a new current surplus.

## 2. Actual reference shape under any physical history

For remaining m>=2, let d=d_m. On nonempty spectator sets T after erasing a queried bit, both Fourier amplitudes equal -d. Thus the actual physical kernel is 1 on the active child (query outcome0, which retains the point defect), and0 on the constant child. At the empty spectator set its active probability is

    alpha_m=(1-2d)^2/[2((1-d)^2+d^2)],

and the other probability is1-alpha_m. The denominator is positive. For m=2 alpha=0 and the active child is a dictator, with zero empty Fourier mass; this endpoint is handled rather than divided away.

Write a current inherited reference as R(empty)=r and

    R(S)=c*delta^|S|(1-delta)^(m-|S|) for S nonempty,
    c=(1-r)/[1-(1-delta)^m]>0.

On erasing the queried bit, every nonempty spectator coefficient of R becomes c*delta^|T|(1-delta)^(m-1-|T|); the two erased possibilities sum exactly. The erased empty coefficient is r+c*delta*(1-delta)^(m-1). Multiply by the above physical kernel and normalize by the predicted active reach. Therefore the active child's nonempty conditional shape is the SAME parameter delta at dimension m-1. Only r and c change. The constant child reference is concentrated at empty, so its K, TC, I and B are zero.

The predicted active and constant reaches are strictly positive for m>=2: source support and the nonzero normalized physical child laws suffice; explicitly the erased empty reference is positive, and alpha<1. At m2 the positive active mass lies on nonempty spectators. At m1 the actual function is a dictator, both children are constants, and the normalized transport is again valid. There are no reference-only erased source rows for a nonconstant point function; if the core has become constant, the process stops. Thus no hidden zero-row convention is needed in this restricted theorem.

After r active reveals, m=n-r and delta<=d_n<=d_m. Every other physical history is an actual constant branch. Permuting remaining coordinates leaves both source and inherited reference unchanged, so this argument covers arbitrary choices depending on earlier outcomes, not only a fixed order. It does not assume reference transport factors over independent Boolean modules.

## 3. A reference-shape projection lemma

For m>=2, the nonempty conditional source is the uniform law U on the 2^m-1 nonempty subsets. Write Q_z for the product Bernoulli(z) law conditioned on being nonempty. For any source-supported normalized reference whose nonempty conditional law is Q_delta, KL chain gives

    K=KL(Bernoulli(p_empty)||Bernoulli(r))
          +(1-p_empty) KL(U||Q_delta)
      >=(1-p_empty) KL(U||Q_delta).                       (4)

The function KL(U||Q_z) decreases on 0<z<=1/2. To prove this, differentiate the finite positive exponential family:

    d/dz KL(U||Q_z)
       =[E_Qz |S|-E_U |S|]/[z(1-z) ln2] <=0.

For z<=1/2, Q_z/U is proportional to (z/(1-z))^|S|, a nonincreasing function of |S|. Its covariance with |S| under U is nonpositive: for independent X,X', (X-X')(a^X-a^X')<=0 when0<a<=1. This proves the expectation comparison, including equality at z=1/2. Every differentiation is of a finite sum; all canceled denominators are positive on 0<z<1. No limiting theorem is used.

As delta<=d_m<=1/2, (4) is at least (1-p_empty) KL(U||Q_d). Let q be the ACTUAL marginal product, q(empty)=(1-d)^m. A second KL chain then gives

    TC-K <= KL(Bernoulli((1-d)^2)
                  ||Bernoulli((1-d)^m)).                 (5)

The right side is an explicit binary normalization mismatch, rather than the entire divergent marginal-entropy sum. Arbitrary reference empty tilt has been retained by discarding only its NONNEGATIVE binary KL from (4).

For m>=3, q_empty<=p_empty<=1. Convexity of binary KL in its first argument and the endpoints KL(q||q)=0, KL(1||q)=-log2(q) give

    binaryKL <= -m log2(1-d).

The ratio -log2(1-d)/d increases in d on(0,1): it is the average over[0,d] of the increasing function1/[(1-x)ln2]. Since d_m<=1/4 for m>=3,

    binaryKL <=4 log2(4/3) * m*d
              < (5/3) I(g_m).                            (6)

The strict numerical constant is certified EXACTLY by 3^12>2^19, equivalent to 4log2(4/3)<5/3. For m2, p is uniform on all four spectral sets, TC=0, so (1) holds with zero reset reserve; for m1 the spectrum is a singleton and TC=0; for m0 the actual function is constant. These endpoints require no logarithm of zero. This proves (1) at every reachable history.

## 4. The complete finite-tree payment

### A general nonuniform version of the projection step

The projection mechanism above does not require a uniform nonempty source. Let p be ANY law on subsets of an m-element set, with actual marginals 0<d_j<1, product q and empty masses p0,q0. Suppose p0>=q0 and p0<1. Supply a normalized reference R with arbitrary supporting empty mass and conditional nonempty law

    R_lambda(S | S nonempty)
         =lambda^|S| q(S)/sum_(T nonempty)lambda^|T|q(T),
    0<lambda<=1.

Thus the original nonempty reference is a COMMON odds attenuation of the actual product, and need not itself be a product. The source may be nonuniform and the d_j unequal. The exact conclusion is

    TC(p)-KL(p||R) <= binaryKL(p0||q0)
                     <= -log2(q0)=sum_j -log2(1-d_j).      (7)

To prove it, condition source and reference on nonemptiness. For P=p(.|nonempty), its rank mean is I/(1-p0). For Q_lambda=R_lambda(.|nonempty), differentiation with respect to log(lambda) gives

    d KL(P||Q_lambda)/d log(lambda)
          =(E_Qlambda |S|-I/(1-p0))/ln2.

The rank mean E_Qlambda |S| increases with log(lambda), with derivative Var_Qlambda(|S|)>=0. At lambda1 it is I/(1-q0)<=I/(1-p0). Hence KL(P||Q_lambda)>=KL(P||Q_1) for every0<lambda<=1. Drop only the nonnegative binary KL of the supplied empty tilt, and compare to the exact product KL chain. This proves the first inequality in(7). The second is the same convexity argument as before. All sums are finite; q is strictly positive, the nonempty normalizer is positive, and no unproved limiting exchange occurs.

If every d_j<=1/4, (7) gives the strict influence-scale cap

    [TC(p)-KL(p||R)]_+ <=4log2(4/3) I <(5/3) I.           (8)

The all-history payment(3) therefore applies to ANY finite Boolean restriction tree at whose reached nonconstant nodes these actual-source/reference eligibility conditions hold; constant and explicit zero-TC terminal nodes can be treated separately. No assertion that arbitrary physical restrictions preserve these conditions is made. The point-function shape invariant in section2 supplies an actual closed all-dimensional application. For that application the attenuation parameter is lambda=[delta/(1-delta)]/[d_m/(1-d_m)]<=1 at each nonconstant m>=3.

This nonuniform projection lemma is the transferable result. Its extra assumptions are explicit: balanced sources with p0=0 and q0>0 are outside it, and an actual mixed query can destroy common attenuation even if the pointwise reference inequality held before the query. Products of unequal-width point cores provide actual nonuniform Boolean root fixtures, but are not claimed to retain common attenuation after arbitrary physical histories.

For the actual normalized reference transport, write q=p erased at the query and Rbar=R erased. On positive q rows use the same physical child kernel in source and reference. Applying the KL chain before and after this common kernel gives

    K_parent = E + O + mean K_child,
    E=K_parent-KL(q||Rbar)>=0.

The last inequality is the conditional KL chain for erasing the spectral indicator. This reconstructs the exact A061/A065 history interface at its required hypotheses, without using their field-family owner estimates.

Set P=K+(5/3)I on every unconverted history. Influence conservation gives

    P_parent-mean P_child = E+O+(5/3)Inf_query.

At a terminal, P>=K for the unchanged reference, and P>=TC for the converted product reference by (1). Summing these finite one-step inequalities to the declared stopping cut proves (3), with actual fair reaches and all terminal quantities. It simultaneously proves (2) by backward induction: the conversion obstacle is bounded by (5/3)I, and the continuation obstacle is bounded by (5/3)mean I_child-E <=(5/3)I_parent. Earlier influence expenditure is not restored.

Every tree has at most n physical reveals. Independent policy randomization is justified by conditioning on that randomness and averaging the finite inequalities. There is no unbounded-depth or varying-dimension passage, and no UI claim.

## 5. Essential hypothesis and exact universal gap

The nonempty reference-shape restriction is essential. If the incoming reference is instead R=p_n itself, then K=0 and its nonempty shape is Q_(1/2), which violates delta<=d_n for n>=3. At an immediate product reset the reserve is TC. For n>=2, M/I>=n-1 and

    H <= [4(n-1)+2log2(e)]d < (4n-1)d,

using -ln(1-d)<=d/(1-d) and log2(e)<3/2. Hence TC/I>n-5+1/n, already greater than5/3 at n8, and diverges. This refutes (1) without reference eligibility, not FEI. The executed n8 certificate must check this boundary before the theorem is marked checked.

The root marginal product is eligible but K_initial=TC(g_n) itself need NOT be O(I_initial). This theorem controls the extra reset reserve conditional on the originally booked incoming KL. It does not pay initial reference admission, arbitrary source terminal entropy, intermediate repeated resets, or non-point histories whose conditional reference shape changes. Those are the first unpaid universal lines. The new transferable mechanism is the projection bound (5), and the next target is one unequal/nonuniform nonempty spectral row with the SAME original reference, old debit and both terminal bills; no descendant may be assigned a fresh product prior.
