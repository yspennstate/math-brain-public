# A supplied core source pays sparse edits and every projection history

All quantities are in bits. Let g be ANY Boolean function on d coordinates, with a supplied normalized full reference Q_g covering its squared spectrum, and let C_g=CE(P_g,Q_g)<=c I(g), c>=0. Pad with m fresh physical coordinates. At an arbitrary set E of k distinct physical points flip the value of the padded core, obtaining F. Assume

    m>=max(4d,6),  1<=k,  k^4<=2^m.

There is no quadratic, flatness, disjoint-edit, or sign-coherence hypothesis on the core or on E. Set N=d+m, theta=k/2^N, eta=4theta, and define ONE ORIGINAL normalized reference

    R=(1-eta)(Q_g x delta_empty_padding)+eta U_N.       (1)

Here U_N is uniform on all 2^N Fourier labels. Thus R covers every actual Fourier atom, including vacuum. The clean supplier Q_g is scaled once and retained; there is no fresh descendant source.

The source theorem is

    I(F)>=I(g)+m theta,
    CE(P_F,R)<=2 C_g+24[I(F)-I(g)]
               <=max(2c,24) I(F).                     (2)

Consequently let C0=max(2c,24) and K=C0+4. A SINGLE ORIGINAL owner K I(F), with an eligible OLD booking U<=I(F), pays EVERY finite adaptive physical-query tree using projection inheritance and the paid profile/affine calibrations described below, including every actual query contraction and fee and ALL full terminal reference costs. Its remaining balance exceeds (3/28)I(F). This is conditional on the supplied core source. It gives no universal arbitrary-core supplier and no improvement in a universal FEI constant.

## 1. Actual edit influence, including cancellation

For any Boolean sign function, influence is the number of unordered bichromatic edges divided by2^(N-1). On a core-coordinate edge, flipping exactly one endpoint may remove a previous bichromatic edge. There are at most k such edges in each of the d core directions. Hence core influence decreases by at most2d theta.

On a padding-coordinate edge the clean core has equal endpoint values. That edge is bichromatic for F exactly when it crosses E. In each fixed-core fiber E_x, of size k_x, the m-cube edge-isoperimetric bound gives padding boundary >=k_x(m-log2 k_x). Empty fibers contribute0. As k_x<=k, summing gives padding boundary >=k(m-log2 k). Therefore

    I(F)-I(g)>=2theta(m-log2 k-d)>=m theta.            (3)

The last step uses log2 k<=m/4 and d<=m/4. No positive error influence is silently assigned to an independent payer; the actual increase (3), AFTER possible cancellation of core edges, is the payer used in (2).

For completeness the finite-cube edge-isoperimetric inequality follows by induction on m. If section sizes are a<=b, the two internal boundaries have the inductive bounds and the crossing boundary is at least b-a. The remaining scalar inequality is h2(t)>=2t on0<=t<=1/2, t=a/(a+b). It follows from concavity of h2 and its values0 at0,1 at1/2. Thus boundary >=(a+b)(m-log2(a+b)). Zero section sizes are handled directly, not by log0. This proves the bound for arbitrary E_x, not only subcubes.

## 2. A full reference from the supplied core and a fixed uniform error source

Write fhat=ghat+ehat, where e=F-g is zero off E and has magnitude2 on E. Parseval gives sum_s ehat(s)^2=4theta. Pointwise

    P_F(s)<=2 P_g_padded(s)+2 ehat(s)^2.              (4)

The reference (1) is normalized and positive. Its code costs are nonnegative. Wherever the clean spectrum is positive,

    log2(1/R)<=log2(1/Q_g)+log2(1/(1-eta)),

and everywhere log2(1/R)<=N+log2(1/eta). Multiplying (4) by this NONNEGATIVE cost and summing yields

    CE(P_F,R)<=2C_g+2log2(1/(1-eta))
                         +8theta[N+log2(1/eta)].     (5)

The assumptions imply eta<=1/2: eta<=4*2^(-3m/4)<=2^(-5/2) for m>=6. Also0<=log2(1/eta)<=N. The elementary logarithmic bound -ln(1-eta)<=eta/(1-eta), together with ln2>2/3, gives log2(1/(1-eta))<3eta. Hence

    CE(P_F,R)<=2C_g+(16N+24)theta
              <=2C_g+24m theta
              <=2C_g+24[I(F)-I(g)].                 (6)

Indeed N<=5m/4, and24<=4m. The final max(2c,24) bound follows by separating the NONNEGATIVE original influence I(g) and increase I(F)-I(g). No assumption I(g)>=1 is used. If g is constant, a source satisfying C_g<=c I(g)=0 is necessarily delta_empty; all displayed estimates still hold. The theorem does not require Q_g to have full support away from P_g because eta>0 covers every F atom.

The reference (1) is already constant outside the clean core frequency subspace V, and hence inside every finer outside-core phase-signature cell in A066's finite-edit construction. It is an explicit price for one source in that compatible class. Its physical projections retain the full old uniform mass landing inside projected V/vacuum, as in the exact fiber-count formula of A068 stage21; none is discarded.

## 3. Full query accounting from the SAME ORIGINAL owner

This section reconstructs A012 stage22 DERIVATION sections1--4 and A097 stage22 PROOF section2. It fixes the inheritance convention; it is NOT free substitution for prescribed true-kernel references.

At a physical query i, BOTH children inherit Q'=pi_i Q, where pi_i deletes spectral coordinate i. The actual average child law is P'=pi_i P, by signed Fourier restriction. Put

    L_i=D(P||Q)-D(P'||Q')>=0,
    J_i=average_b D(P_b||P').

The finite mixture/chain rules give exactly

    average_b D(P_b||Q')-D(P||Q)=J_i-L_i.             (7)

Moreover J_i<=(2/ln2) Inf_i. Here is a direct scalar derivation, included to identify the imported constant. In nats put

    e(a,b)=[a^2 ln(2a^2/(a^2+b^2))+b^2 ln(2b^2/(a^2+b^2))]/2.

Replace a,b by their absolute values; e is unchanged and (a-b)^2 can only decrease. For a+b>0 write a=s(1+t), b=s(1-t), |t|<=1. The function j(t)=e(1+t,1-t) has j(0)=j'(0)=0 and

    j''(t)=2 ln((1-t^2)/(1+t^2))+4/(1+t^2)<=4.

Twice integrating gives j(t)<=2t^2, with endpoints by continuity. Thus e(a,b)<=(a-b)^2/2. Summing over the two child amplitudes and using Inf_i=sum_T(a_T-b_T)^2/4 proves the stated J bound. All sums are finite.

Permitted reference updates have FULL fee F_v and satisfy

    D(P_v||Q_after)-D(P_v||Q_before)+F_v<=0.          (8)

This includes paid partition-profile mixtures from A012, and finite affine information projections from A097 with F_v=D(Q_after||Q_before). Their hypotheses are stated explicitly: the true law is feasible for the selected affine constraints, support is covered and the total reference mass remains unchanged. For affine projection, minimizing D(q||Q_before) over the feasible simplex gives stationarity in the feasible direction P-q, hence D(P||Q_before)-D(P||q)=D(q||Q_before). Boundary support is justified by mixing with P: a missing feasible positive atom would decrease the objective by a t log t term. Nothing here permits an arbitrary reset or unspecified fee. A066's free finite-edit returns are also allowed with F_v=0: their signed change is tracked ONLY through the current divergence/full CE. It must NOT also be entered as a negative fee, which would collect the same release twice.

For explicit partition-profile mixtures, let p,q be the actual/current cell masses and r=(1-t)q+t p, retaining the old conditional reference within each cell. For0<t<1 the left side of (8), with fee D(r||q), is exactly minus ((1-t)/t)[D(r||q)+D(q||r)]: expand it as minus sum_cells(p-r)log2(r/q) and use p-r=((1-t)/t)(r-q). The endpoint t=0 is the identity update and t=1 has exact equality. Cover handles zero q-cell masses; cells with zero actual mass need no division by that mass. Thus this update class is reconstructed without importing an unchecked sign or discarding its full fee.

For actual reaches w_v and terminal laws, define the COMPLETE bill

    Bill=U+sum_queries w_v[H(P_v)-avg_b H(P_b)+L_v]
             +sum_updates w_v F_v
             +E_terminal CE(P_terminal,Q_terminal).

Telescoping (7)--(8), and I(parent)=Inf_i+avg I(children), gives

    Bill<=U+CE(P_F,R)+(2/ln2)I(F).                    (9)

It retains all signed entropy decrements, positive query contractions, old U, updates, reference-only mass and ALL terminal costs. It applies to arbitrary data/padding query interleavings and optional finite stopping, not merely padding-first policies. For U<=I(F), (2) and (9) yield

    K I(F)-Bill >=[3-2/ln2]I(F)>(3/28)I(F).          (10)

The rational lower bound ln2>2/3+2/81=56/81 follows from the first two terms of its positive atanh series. Hence2/ln2<81/28. No positive unused balance is renewed at a descendant. If an actual prefix is run, its booked charges stay in the SAME full policy telescope; treating U as a new independent descendant allowance is forbidden. U<=I(F) is an explicit original encumbrance hypothesis, not evidence that any unspecified prior policy has that price.

## 4. Scope guards and the first unsupported line

Without the padding condition the actual influence increase can be negative: flip the unique negative point of a sign function that is negative at just one point, leaving a constant. The original core had positive influence and the final function has zero. Thus replacing (3) by I(F)>=I(g) for arbitrary edits is false. The code tests that exact negative control.

Projection inheritance cannot be silently replaced by true-kernel inheritance: for AND2 with Q=P, projection after one query gives the constant branch reference(1/2,1/2), whereas true-kernel inheritance gives delta_empty; their reverse divergence is infinite. This guard is retained from A012 rather than suppressed by the new supplier.

This is a conditional clean-core-to-edited-source compiler plus a FULL history interface. It pays arbitrary sparse finite edits of NONQUADRATIC cores from an explicit ORIGINAL source and actual influence increase, rather than simply regularizing shape. The original clean-core supplier remains given. Supplying an O(I(g)) complete source for EVERY Boolean g is still FEI-equivalent; setting Q_g=P_g without pricing its CE would be circular. Neither an interface mandated by another route nor a universal productive stopping certificate is proved. The first unpaid universal line is the original arbitrary-core source or a REQUIRED interface conversion with its actual query bill inside the same unused balance.
