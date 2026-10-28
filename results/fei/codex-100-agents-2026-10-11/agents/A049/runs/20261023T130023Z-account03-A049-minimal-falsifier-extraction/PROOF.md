# The exact unpriced normalizer and an influence-priced residual

Finite uniform Boolean signs; all entropy/KL in bits. Full FEI remains OPEN. All physical children and reference-only rows are retained. This is a scoped reference-price lemma, not an initial universal supplier.

## 1. Fixed-mask statement

Let f on n>=2bits have all n coordinates essential, and query coordinate i. Require BOTH children to have all the remaining n-1coordinates essential. Thus the parent spike erases to the SAME full mask U used by both fresh child references. For0<alpha<1 put beta=1-alpha and define

    (R_alpha p)(0)=p(0),
    (R_alpha p)(T)=beta*p(T), T!=0,U,
    (R_alpha p)(U)=beta*p(U)+alpha*(1-p(0)).

Use this rule at parent and children, with the parent full mask before erasure. It agrees with exact constants/full characters when those are admissible. Reference mass on source-zero full atoms is allowed and retained. Transport by the actual coherent physical query kernel, fair on source-zero erased rows; normalize by the reference's OWN outcome law Z. Write sigma for average fresh-minus-inherited child KL, and O=D(fair||Z). Then

    sigma <= O + [2+alpha/(1-alpha)] Inf_i(f)/ln2.       (1)

No independence between the physical child and the Fourier sample is assumed. All physical outcome weights are1/2. Only the explicitly displayed O is left without an influence price.

The unmatched term also has the universal profile-size cap

    0<=O<=-(1/2)log2(1-alpha^2)
         <=alpha^2/[2(1-alpha^2)ln2].                    (1a)

Indeed the parent reference is beta*P+alpha*R with R a probability law (empty mass p0 and full mass1-p0). Its transported outcome masses lie in [beta/2,(1+alpha)/2], so Z0*Z1>=(1-alpha^2)/4. The natural-log bound -ln(1-x)<=x/(1-x) gives the second inequality. This cap is per query; multiplying it by unbounded depth is not a once-only influence payment.

## 2. Concavity of full-spike cross entropy

For a probability law p with empty mass p0, write v=1-p0 and y=p(nonempty)/v. On the nonempty simplex let t=y(U). Its cross entropy against the nonempty spike rule is

    C(y)=-sum_(T!=U) y(T)log2(beta*y(T))
         -t log2(alpha+beta*t).

Each nonfull summand is concave. The last summand has second derivative

    -beta*(2alpha+beta*t)/[ln2*(alpha+beta*t)^2] <=0.

Therefore C is concave. Complete cross entropy is h2(p0)+v*C(y), a concave entropy plus the perspective of C; it is concave, including v0 by continuity. Since the average child source law equals the erased law P_e, Jensen gives

    avg_b D(P_b||R_alpha P_b)
       <= D(P_e||R_alpha P_e) + JS(P_0,P_1).             (2)

This proves the residual estimate for arbitrary Boolean children, rather than extrapolating a rare-family sign.

## 3. Exact erasure-profile mismatch and influence price

Let p0=p_parent(0), p_i=p_parent({i}), and Q_e the erased actual parent reference. The empty/full masses satisfy

    Q_e(0)=(R_alpha P_e)(0)-alpha*p_i,
    Q_e(U)=(R_alpha P_e)(U)+alpha*p_i;

all other atoms agree. Consequently

    D(P_e||R_alpha P_e)-D(P_e||Q_e)
       =sum_T P_e(T)log2[Q_e(T)/(R_alpha P_e)(T)]
       <= alpha*p_i/(beta ln2).                         (3)

The empty term is nonpositive. For the full term use log(1+x)<=x/ln2 and (R_alpha P_e)(U)>=beta*P_e(U). Zero source weights contribute zero; if a denominator vanishes, the corresponding positive-weight case is absent. No actual reference row has been erased from its normalizer.

The exact query KL chain gives avg inherited-child KL =D(P_e||Q_e)-O. Combine with(2)-(3): sigma-O <=JS+alpha*p_i/(beta ln2).

For completeness, write each erased Fourier pair as real coefficients u,v, with v on the queried-coordinate atom. Its two child weights are (u+v)^2,(u-v)^2 and its erased weight is u^2+v^2. Put z=2uv/(u^2+v^2). The natural-log binary term F(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2 obeys F(z)<=1-sqrt(1-z^2). For z>=0 the derivative of the difference is z/sqrt(1-z^2)-atanh(z)>=0: the derivatives of these latter two terms are (1-z^2)^(-3/2)>=(1-z^2)^(-1), and both start at0. Extend evenly and continuously to endpoints. Thus the row JS is <=2min(u^2,v^2)/ln2. Summing gives JS<=2Inf_i/ln2; also p_i<=Inf_i. This proves(1).

## 4. Independent reconstruction of A047 and a sharper equal-mean sandwich

For A047's stable-mask input, E f_0=E f_1=mu, so p_i=0. Let u=mu^2, c=alpha(1-u), t_b=hat(f_b)(U)^2>0 and E=(t0+t1)/2. Direct full-row coherent transport gives

    Z_b=1/2+(c/2)(t_b/E-1),
    sigma=O+Gamma,
    Gamma=(1/2)sum_b t_b log2[(beta+c/E)/(beta+c/t_b)].

For F(t)=t log2[t/(beta*t+c)], Gamma is its Jensen gap and

    0<=F''(t)=c^2/[ln2*t*(beta*t+c)^2]<=1/(ln2*t).

Comparing Jensen gaps with tlog2(t), and then the single erased-full row of the preceding scalar bound, gives the new sharper certificate

    0 <= sigma-O = Gamma
      <= (1/2)sum_b t_b log2(t_b/E)
      <= 2min(p_parent(U),p_parent(U+i))/ln2
      <= 2Inf_i/ln2.                                   (4)

For the activation lift, whose actual two vacuum masses are copied, equal means keep those vacuum ratios unchanged through erasure. Its actual outcome law is Z_b^act=1/2+(c/4)(t_b/E-1), and its exact price is sigma_act=O_act+Gamma/2. Therefore

    0<=sigma_act-O_act<=Inf_i(core)/ln2
                             =2Inf_i(activation)/ln2.   (5)

The outcome term is not blindly halved. Equations(4)-(5) identify it as the ENTIRE nonvanishing charge in A047's rare-query limit. The other charge has an influence price for every equal-mean stable-mask Boolean pair.

We independently reconstruct A047's declared family: for r>=4, delta=2^-r, let h(z)=(-1)^z1 if z0=0 and (-1)^z2 otherwise. Let f0 flip h at integer1 and f1 flip h at integers1,4,5, little endian; f(a,z)=f_a(z). Both means are -2delta, full coefficients2delta and6delta, and Inf_a=2delta. Both children retain all coordinates and have full support: original mux coefficients have magnitude1/2 and edit corrections<=6delta<=3/8, while all other coefficients have nonzero odd edit sums. Parent full coefficient is -2delta and its reference support matches its source. Hence

    0<=Gamma<=8delta^2/ln2,
    sigma=O+O(delta^2), sigma_act=O_act+O(delta^2).

With eta=4alpha(1-4delta^2)/5, the actual core outcomes are (1+/-eta)/2 and activation outcomes(1+/-eta/2)/2. At alpha1/6, eta>=21/160; -ln(1-z)>=z and ln2<1 give sigma>1/128 and sigma_act>1/512 for every r>=4. This verifies A047's all-r/all-fixed-alpha obstruction, without claiming the new invoice bound prices O. Their elementary H<=8I guard also holds: parent differs from the mux on fraction2delta, giving H<=3+8(r+1)delta<=11/2, and I>=3/2-12delta>=3/4. Activation uses the exact two-vacuum entropy/influence formula or its upper bound2+H/2. This is not an FEI counterfamily.

## 5. Unpaid line and source ownership

The fixed-tilt coefficient in(1) is dimension independent (at alpha1/6 it is11/(5ln2)). Along a finite stable-mask physical tree, queried influences telescope to at most the root influence, so this residual component can be assigned a once-only original influence quota. The outcome invoices O still require payment from ACTUAL unused original source surplus, with all old reset debits, old quarter and both terminal laws retained. They are not free simply because outcome KL appears in the exact query chain. A047 proves that O cannot be bounded by a fixed multiplier of newly queried influence. Summing old held KL at every reset would renew a spent source and is not supplied here. The independent arbitrary-core initial supplier is also missing. Thus no universal FEI constant improvement is asserted.
