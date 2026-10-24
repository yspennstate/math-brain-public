# Root-law certificate obstruction and incidence-cap replacement

All Boolean inputs are uniform independent signs. Let f_m be positive exactly when x_0 and at least one of x_1,...,x_m are positive, m>=2. Its entire positive prime table consists of m width-two edges 0i, each with rarity pi_i=1/4. A globally fixed positive weight vector is feasible exactly when s=sum_i lambda_i<=1. Orders and a finite distinct once-per-gate partition-event family are fixed before sampling the Fourier set. Assume that family has positive output mass wherever the nonempty physical spectrum is positive. The maximal-matching star family satisfies this assumption. No assertion below minimizes over alternative gate tables or families.

## Reconstructed global joint certificate

For complete event coefficients k_AT, W_A=sum_T k_AT lambda_T, D=prod_i(1+pi_i lambda_i)-1, and Q_A=W_A/D. Each k includes actual root rarity, selected subset, child count, multiset and chronological label probabilities. Defining p_lambda(T)=pi_T lambda_T/D and K_AT=k_AT/pi_T gives Q_A=sum_T K_AT p_lambda(T), purely algebraically. A USED subset indexes k; an INITIAL ROOT subset indexes p. They need not coincide in any individual run.

For nonempty spectral P_A, v=sum P_A, let G(p)=-sum_A P_A ln(K_A dot p). At physical p0 set h_T=sum_A P_A K_AT/Q_A(p0). Then sum_T p0(T)h_T=v. For any p with finite cost, -ln x>=1-x gives G(p)>=G(p0)+v-sum_T p(T)h_T. The inequality is automatic when G(p)=infinity. Therefore Gamma=max_T h_T-v>=0 gives G(p0)-Gamma<=inf_simplex G<=inf_feasible_lambda G<=G(p0). This is exactly the source's theorem, including its joint posterior optimization and its restriction to the SAME event family. It does not require K to be stochastic or joint convexity in lambda. Its bit gap is at most 2Gamma since ln2>1/2. Independent reconstruction supplies no substantive repair to A006 ROOT_LAW_RELAXATION.md.

## All-weight obstruction, not an unbounded coding cost

Let A_all={0,...,m} and T_all be all m edges. Each leaf has only its own edge as eligible owner. Consequently EVERY partition event producing A_all visits all m gates, whatever the admissible fixed endpoint orders or chosen event family. Write W_Aall=c lambda_Tall with c>0. The physical Fourier coefficient at A_all has magnitude 2^-m, so P_Aall=4^-m. Thus its contribution to h_Tall is

    P_Aall K_Aall,Tall/Q_Aall = 4^-m * (c*4^m)/(c*lambda_Tall/D)
                                           = D/prod_i lambda_i.

Bernoulli gives D>=s/4. AM-GM gives prod_i lambda_i<=(s/m)^m. With 0<s<=1,

    Gamma >= D/prod_i lambda_i-v
          >= m^m/(4 s^(m-1))-v >= m^m/4-1+4^-m.

Physical pivotal counting gives I=1+(m-1)2^-m<=5/4. Hence Gamma/I>=(m^m-4+4^(1-m))/5, unbounded uniformly over EVERY feasible positive weight vector, even though the actual coding cost has a bounded choice. In particular the uniform lambda_i=1/m matching-star reference has C_MS<=11I by the complete star numerator argument independently accepted for the A010 previous-stage theorem by A008. Its root normalizer D<1/3 is retained and contributes a negative log term. Thus there is no variational-cost growth or FEI counterexample here. The failure is of this specific full-simplex tangent-gap certificate at every physical weight. It does not show that the optimized simplex lower bound itself is poor; the tangent bound may be loose.

For matching-star events the exact full-set coefficient is c=(m-1)!/[3*8^m*m*(m+1)]; its K column entry is (m-1)!/[3*2^m*m*(m+1)]. This exceeds one at m=10, demonstrating concretely why K cannot be treated as a stochastic channel. The all-weight obstruction does not depend on that formula: c cancels, so it also holds for larger actual partition-event families covering A_all.

## A packing-aware global lower certificate

For any nonempty root subset T of k star edges let s_T=sum_(i in T)lambda_i<=1. Then D>=s_T/4 and AM-GM imply

    p_lambda(T)=(prod_(i in T)lambda_i/4)/D
               <=4^(1-k) s_T^(k-1)/k^k <=u_T:=4^(1-k)/k^k.

Every physical root law therefore lies in the bounded simplex P_cap={p>=0,sum p=1,p_T<=u_T}. It is nonempty because it contains p_lambda. Set L=max_(p in P_cap) sum_T h_T p_T and Gamma_cap=L-v>=0. The same supporting inequality gives

    G(p0)-Gamma_cap <= inf_(feasible lambda) G(lambda) <=G(p0).

This minimizes lambda and its event posterior jointly, at the fixed table/orders/family. It is not a frozen-posterior bound. The LP is solved exactly by sorting h_T decreasingly and filling each cap until total mass one. For the last filled threshold t the dual value is t+sum_T u_T max(h_T-t,0). Equality of the greedy primal and this dual is an exact rational certificate of the GLOBAL LP optimum. The inequality h dot p<=that dual also follows directly from p_T<=u_T and sum p=1. Natural-unit gap Gamma_cap becomes bit gap at most 2Gamma_cap.

All seven physical stars m=2,...,8, both orders per edge, matching-star events and lambda_i=1/m have Gamma_cap<I/6, exactly verified by rational primal-dual values in out/caps.json. Consequently their complete reference bit cost is within I/3 of the joint ALL-positive-weight/all-posterior infimum for that FIXED event family. These are finite exact global certificates, not extrapolation to all m. The n=4 graph census independently reconstructs all used-subset coefficients and the unrestricted root-law certificate; it does not claim a n=4 optimum or a lower bound for all forests.

## First unsupported line

The first unsupported extension is Gamma_cap<=K I for every m, or a useful incidence-cap analogue on arbitrary shared/leafless graph spectra, after recomputing h for the whole event family. A lower bound proved for a selected matching-star family cannot lower-bound the larger full partition family or its surrogate residual. Additional joint packing constraints may be needed beyond individual caps. Neither convexity of the simplex nor this finite success proves convexity in all weights. NEXT: derive a cardinality formula for the capped star gradient LP with the full partition numerator, then transfer only the exact packing constraints to a shared/leafless graph. This targets the global variational falsifier's missing certificate directly.
