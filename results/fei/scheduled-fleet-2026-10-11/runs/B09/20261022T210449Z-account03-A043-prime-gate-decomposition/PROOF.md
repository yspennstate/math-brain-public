# A sharp polynomial hierarchy for the actual singleton reserve

The failed degree-three surrogate is the first term of an increasing hierarchy. The error after m terms is at most 4 Delta/(m+1), in natural entropy units, for every Boolean function and every interior product law. The coefficient 4/(m+1) is optimal for this hierarchy, already on binary AND gates. This repairs the approximation step; it does not prove the remaining higher-degree payment or full FEI.

Let f:{0,1}^n->{-1,1}, let the coordinates be independent with probabilities p_i in (0,1), and put v_i=4p_i(1-p_i). Use the orthonormal biased Fourier basis (2x_i-1-(2p_i-1))/sqrt(v_i). Write P(A)=hat f(A)^2,

    Delta = sum_{A nonempty} (|A|-1)P(A),
    R = sum_{|A|>=3} (|A|-2)P(A).

Set D_i=(f(x_i=1)-f(x_i=0))/2, c_i=E D_i, d_i=E D_i^2, t_i=|c_i|. Booleanity gives D_i in {-1,0,1}, hence 0<=t_i<=d_i<=1. Put h(t)=t^2 ln(1/t^2), continuously zero at t=0, and let E_1=sum_i v_i h(t_i). All entropies in this proof use natural logarithms. Define the actual reserve

    S = 4 Delta - 2R - E_1.

For every integer m>=0 define the rational polynomial reserve, separately on each sign cell of the c_i,

    S_m = sum_i v_i {2(d_i-t_i)
          + t_i(1-t_i) sum_{k=1}^m 2(1-t_i)^k/[k(k+1)]}.

Then

    0 <= S_m <= S_{m+1} <= S,
    0 <= S-S_m <= [2/(m+1)](2 Delta-R) <= 4 Delta/(m+1).       (1)

No division by Delta is used in (1). Thus constants, zero-deficit functions, and one-coordinate functions are included. At deterministic input endpoints, first contract those coordinates; no normalized basis with zero variance is asserted.

## Proof of the reserve identity

Expanding D_i on the other coordinates gives

    v_i Var(D_i) = sum_{A containing i, |A|>=2} P(A).

Summing, each non-singleton A is counted |A| times, so

    sum_i v_i(d_i-c_i^2) = sum_{|A|>=2}|A|P(A) = 2 Delta-R.   (2)

The identity uses the actual joint spectrum of f. It assigns no new reserve to a constituent representation. In particular 0<=R<=Delta and the singleton identity is

    S = sum_i v_i {2(d_i-t_i)+phi(t_i)},
    phi(t)=2t(1-t)-h(t).

For 0<t<1, put s=1-t. The convergent logarithm series gives

    -2t ln(t)/(1-t) = 2-sum_{k>=1} 2s^k/[k(k+1)],
    phi(t)=t(1-t) sum_{k>=1} 2(1-t)^k/[k(k+1)].             (3)

At t=1 the second identity holds directly. At t=0 both sides of that second identity are zero, since the coefficient series has total sum 2. Thus (3) is valid on the whole closed interval. The coefficients are nonnegative, and

    sum_{k=m+1}^N 2/[k(k+1)] = 2/(m+1)-2/(N+1).

Consequently the omitted tail in phi is between zero and 2t(1-t)/(m+1). This proves monotonicity and

    S-S_m <= [2/(m+1)] sum_i v_i t_i(1-t_i).

Since d_i>=t_i, t_i(1-t_i)<=d_i-t_i^2=Var(D_i). Now (2) proves (1). Every sum over i is finite. The only infinite series has nonnegative summable coefficients with total 2, so its endpoint limit and tail bound require no unstated interchange.

The exact increment is

    S_{m+1}-S_m = sum_i 2v_i t_i(1-t_i)^(m+2)/[(m+1)(m+2)].

For m=1, S_1 is exactly the previously refuted sufficient surrogate S_poly. Its status as a lower bound remains valid; the false statement was S_1>=4T for prime56067 at every law. The hierarchy does not reinstate that statement.

## Optimality of the approximation error

Take the actual binary prime f(x,y)=-1+2xy with independent equal probabilities p in (0,1). Then c_x=c_y=d_x=d_y=p, R=0, and Delta=4p^2(1-p)^2>0. Equation (3) yields the exact formula

    (S-S_m)/Delta = 2 sum_{k>m} 2(1-p)^k/[k(k+1)].          (4)

As p decreases to zero, each summand increases to its coefficient. The summable coefficient tail bounds all these sums, so monotone convergence (or a finite-head/tail estimate) gives the limit 4/(m+1). Thus no smaller universal coefficient replaces 4/(m+1) in (1) for this hierarchy. This is an approximation obstruction, not an unbounded FEI ratio.

## What this pays, and what remains unpaid

For the full natural corrected entropy E=sum_{A nonempty} P(A)ln(product_{i in A}v_i/P(A)), with zero-mass terms omitted, write E_ge2 for its non-singleton part. The identity above gives

    (4+ln4)Delta-E = S+2R-[E_ge2-ln4 Delta].                 (5)

If a family has a proved gap of at least gamma Delta in (5), with gamma>0 independent of dimension and input law, then any m with 4/(m+1)<=gamma gives the sufficient polynomial-reserve inequality

    E_ge2-ln4 Delta <= S_m+2R.

This is a conditional consequence, not an assertion that such a uniform gap exists. At sharp boundary limits gamma may vanish, so compact-domain convergence or a fixed finite m cannot be silently extended to all biases.

For reflected prime56067, stage five gives R=T and E_ge2-ln4 Delta=G. The unpaid line remains

    G <= S+2T

for every four-bias interior law. The hierarchy bounds the exact loss from replacing S by S_m. It does not pay G, identify an all-arity prime packet owner, or supply a finite universal FEI constant. The general deficit-controlled approximation is reusable for arbitrary cofactor profiles because it makes no assumption on the arity, monotonicity, cofactor shape, or representation of f.

## No fixed truncation proves the stronger 4T payment

The sufficient assertion S_m>=4T fails for every fixed m, on the same actual prime56067. Use its reflected Boolean polynomial from stage five,

    f=-1+2z+2xy-2z[ax+(1-a)y],

and set (alpha,e,d,q)=(t,t^2,t^4,t), with 0<t<1/2. Every bias is interior. The singletons, in order a,x,y,z, have absolute coefficients

    t^3(1-t^2), t^2(1-t^2), t(1-2t), 1-t^3-t^4+t^5.

Their squared-derivative means are respectively

    t^3+t^5-2t^7, t^2+t^4-2t^6,
    t-2t^3+2t^4, 1-t^3-t^4+t^5.

Directly from the two triple packets,

    T=4t^4(1-t)^2(1-t^6)>0.

For fixed m, let phi_m(u)=u(1-u)sum_{k=1}^m 2(1-u)^k/[k(k+1)]. The finite telescope gives phi_m(u)/u -> 2m/(m+1) as u->0. Also phi_m(u)=O((1-u)^2) as u->1 (including m=0, where it is zero). Substitution into S_m shows that only the a and x terms contribute at order t^4. Each contributes 8m/(m+1)t^4; all other terms are o(t^4). Therefore

    S_m/T -> 4m/(m+1),
    (S_m-4T)/T -> -4/(m+1).                                (6)

For each fixed m there is consequently an interior interval of actual Boolean laws with S_m<4T. The order of quantifiers matters: m is fixed before t tends to zero. This proves a failure for every fixed order, not a single witness that serves all unbounded orders at once.

This path does not obstruct the actual sharp payment. From (3), phi(u)/u->2 at zero, so S/T->4. In the exact stage-five formula for G, the terms 2T A(q) and 2Tx A(alpha) are o(T), because A(t)=t ln(1/t)/(1-t)->0; 2Ty A(1-alpha)=o(T), since Ty/T->0 and A<=1; and (uw/4)h(d-e)=o(T). Thus G/T->0 and

    (S+2T-G)/T -> 6>0.

Here u=4alpha(1-alpha), w=4q(1-q), Tx=u v_x w/16, and Ty=u v_y w/16, as in stage five. The no-fixed-order result rules out only the excessive sufficient charge S_m>=4T. A proof must retain the actual G, rather than replace it by 6T and demand a uniform extra 4T from a fixed truncation.

Booleanity is essential to the universal reserve theorem: the real-valued uniform one-bit function f(x)=x-1/2 on {0,1} has Delta=0 but E_1=(ln4)/4>0, so S<0. The proof explicitly uses d_i>=|c_i|, which this non-Boolean example violates. No unmentioned monotonicity assumption is needed.

## Verification scope

The analytic argument above is an author proof, pending independent reconstruction. The exact finite helper checks direct physical derivatives against biased Fourier moments, the reserve identity, all signs in (1), the scalar recurrence, boundary cases t=0,1 and Delta=0, the old rational witness, and rare-AND paths. Its output records actual completion and any failure. A requested Lean check concerns only the finite scalar tail-coefficient identity; it must not be described as a formalization of the logarithmic series, Boolean Fourier identity, or full FEI.
