# Loss-free low-total-influence erasure completeness

This strengthens B20-ERASURE-LOW-INFLUENCE-COMPLETE v1 in its existing mechanism, rather than adding another universal-payment conjecture. Uniform Boolean signs; bits; ordinary physical influence. Let s:N->[0,infinity) have finite values and s(N)=o(N), and let K_E(s) be the supremum B(F)/I(F) over all N-bit Boolean F with 0<I(F)<=2^(-s(N)). Then **K_E(s)=K_E** in the extended reals.

For a nonconstant seed f on n>=1 bits, take m disjoint copies and an independent fresh sign z, and set h_m=z product_{j=1}^m f(x^(j)). Its squared Fourier law is the tensor law of the copies and the deterministic singleton law of z. Consequently B(h_m)=mB(f), I(h_m)=mI(f)+1, and E h_m=0. This uses aggregate B, not a selected-coordinate assertion.

Activate h_m at one point of k controls: F=1+A_k(h_m-1), delta=2^-k. Its constant coefficient is 1-delta; every nonempty core coefficient is delta times its h_m coefficient in all control-frequency slices; an empty core index with nonempty control index has coefficient magnitude delta. At a core coordinate i the original root packet has cost phi(0,ahat_i^2)=0. Direct edge partition therefore gives

    B_data(F)=delta B(h_m)
       +delta(1-delta) sum_i phi(1,ahat_i^2)
       +sum_i phi((1-delta)^2,delta^2 ahat_i^2)
       >=delta mB(f).

All control erasures are nonnegative, so B(F)>=delta mB(f). Physical edge counts give exactly I(F)=delta[mI(f)+1+k], since the balanced core has minority probability 1/2. Every extra root term is retained as a nonnegative remainder, not discarded with an unpriced sign.

Let sbar(N)=max_{1<=M<=N}s(M). It is nondecreasing and o(N): for any epsilon>0, the finite initial maximum contributes o(N), while later terms are <=epsilon N. The class for sbar is a subset of that for s. Put

    k_m=ceil(sbar(2mn)+log2(3mn))+1,
    N_m=mn+1+k_m.

For all sufficiently large m, k_m<=mn-1, N_m<=2mn, and

    0<I(F_m)<=2^(-k_m)3mn
        <=2^(-sbar(2mn))<=2^(-sbar(N_m)).

If K=K_E(sbar)<infinity, admissibility and the exact lower bound give

    mB(f)<=K[mI(f)+1+k_m].

Since k_m/m->0, B(f)<=K I(f). Supremizing implies K_E<=K_E(sbar)<=K_E(s)<=K_E. If K_E is infinite, the same argument rules out finite K_E(s), proving the extended-real equality. Constant seeds have I=B=0 and do not require a ratio. No finiteness of FEI is assumed in this implication.

The C018 consequence improves B20's available C_FEI<=K_E(s)+2/(sqrt(e)ln2)+2/ln2 to C_FEI<=K_E(s)+2/ln2. It does not prove K_E(s) finite. It does not transfer a chosen coordinate's B_i/Inf_i: auxiliary controls can still be the cheapest witnesses, precisely as A005's reviewed-scope guard explains.

Exact validation: the frozen 80 labelled seeds/tensor counts/control counts passed 4,945 assertions, with integer Walsh transforms, Fraction influence and prime-log coefficient cancellation; pilot 16 cases passed 433 assertions. These checks support implementation identities; the analytic proof supplies the arbitrary-dimensional and s=o(N) conclusions. Independent refinement reviews A090/A094 remain pending.
