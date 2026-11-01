# Arbitrary-height point carriers use the original boundary bank

All cubes are uniform, all logarithms in entropy are base 2, and all inputs mentioned as private are physically disjoint from the carrier. Full FEI remains open. This extends the stage-6 point-carrier payment; no certificate for arbitrary input entropy is assumed.

## 1. Exact statement

Let h be ANY Boolean function on d shared bits, with h(0)=1, including constant carriers and d=0. Put N=2^d, e=1/N, and let V be ANY Boolean function on private bits. Define

    F(s,x)=h(s)[1+1{s=0}(V(x)-1)], mu=E V,
    R(mu)=d e(1-mu^2), g(t)=-t^2 log2(t^2), g(0)=0.

At any private query i, write a=Vhat({i}), D=Inf_i(V), and Delta_i for parent entropy minus average child entropy. Then

    Delta_i H(F) <= e Delta_i H(V) + d e a^2 + 11 Inf_i(F).       (1)

There is no equal-height, nonzero-support, derivative-gap or balance hypothesis. Inf_i(F)=eD. The term d e a^2 is precisely R(parent)-average R(children); it is not a fresh reserve. For every finite adaptive tree of private queries,

    H(F)-E H(F_leaf) <= e[H(V)-E H(V_leaf)]
                        + R(root)-E R(leaf)+11 P,               (2)

where P is consumed actual private influence. The corresponding erasure bound retains e B_T(V) and has coefficient 14, using the existing JS bound 2/ln(2)<3. Both full terminal entropy spectra remain in (2).

## 2. Spectrum and exact profile

Write b_S=hhat(S). Parseval and inversion give sum b_S^2=1 and sum b_S=1. Direct transformation gives

    Fhat(S,empty)=b_S-e(1-mu),
    Fhat(S,T)=e Vhat(T), T nonempty.

Set

    J(mu)=sum_S g(b_S-e(1-mu))-H(h)+d e(1-mu^2)-e g(mu).

Counting every row, including all original zero rows, gives exactly

    H(F)=e H(V)+H(h)+R(mu)+J(mu).                         (3)

Indeed the nonempty-private rows contribute e[H(V)-g(mu)]+2d e(1-mu^2). This proves (3) at mu=0 and mu=+/-1 by continuity as well. No Fourier row is discarded.

## 3. The curvature estimate

Let A(mu)=sum_S g(b_S-e(1-mu))+d e(1-mu^2). Away from the finitely many zeros of the shifted coefficients,

    g''(t)=-4 log2|t|-6/ln(2),
    A''(mu)=e[-4e sum_S log2|b_S-e(1-mu)|-2d-6/ln(2)].

Their total squared mass is

    M(mu)=sum_S (b_S-e(1-mu))^2=1-e(1-mu^2)<=1.

If all shifted coefficients are nonzero, the concavity of ln applied to their squares gives

    e sum_S log2|b_S-e(1-mu)| <= (1/2)log2(M(mu)/N)
                                             <= -d/2.

Consequently A''>=-6e/ln(2), and A(mu)+(3e/ln(2))mu^2 is convex. This remains true across every zero: g is continuously differentiable at zero, so the corrected derivative is continuous and nondecreasing on each intervening interval, hence nondecreasing on their union. At d=0 and mu=0 all shifted rows vanish together; this is still one isolated zero and the same argument applies. There is no interchange of an infinite sum or limit.

Since mu+/-a are means of Boolean restrictions they lie in [-1,1]. The midpoint inequality yields

    A(mu)-[A(mu+a)+A(mu-a)]/2 <= (3e/ln(2))a^2.          (4)

Also |g'|<=6 on [-1,1]: writing t=|mu|, use t|ln t|<=1/euler<=1/2, t<=1 and ln(2)>=2/3 in |g'|<=(2/ln(2))(2t|ln t|+t). Thus the absolute midpoint gap of g is at most 6|a|. Because J=A-H(h)-e g, (4) gives

    Delta J <= e[(3/ln(2))a^2+6|a|] <= 11e D.           (5)

The last step uses |a|<=D<=1 and 3/ln(2)<=9/2. For completeness, Vhat(i)=E[chi_i partial_i V] with partial_i V in {-1,0,1}, hence |a|<=Pr(partial_i V!=0)=D. Inserting (5) into the exact decrement of (3) proves (1). Summing by reach probability proves (2), with the old terminal reserve retained. This is a one-sided signed estimate; no absolute bound on Delta J is asserted.

## 4. Physical shared queries and signed surplus

A shared query j has one surviving phase-point child h_0 and one unedited child h_1. Its child boundary banks are (d-1)2e(1-mu^2) and zero, so the weighted release is e(1-mu^2). Thus the SAME bank telescopes through any interleaving; equation (1) pays private nodes only. An actual shared-node entropy bill must still be charged separately.

For arbitrary h the exact influence is

    I(F)=I(h)+e I(V)+e(1-mu) L_h,
    L_h=sum_j h(e_j).

Only edges incident to the edited vertex change, with signed change determined by their former pivotal status. For ANY fixed target constant C the exact signed source surplus is

    C I(F)-H(F)=e[C I(V)-H(V)]
       +C I(h)-H(h)+C e(1-mu)L_h-R(mu)-J(mu).            (6)

Negative terms are retained. Formula (6) is an accounting identity, not a claim that its carrier remainder is nonnegative for every h. Restricting and telescoping it carries the existing bank and all old debits without renewing a root certificate.

## 5. Maj5 on the saved private/private/shared/private history

Use h=Maj5, with signs + at bit zero. Its nonzero coefficients are 3/8 on the five singleton sets and the full set, and -1/8 on the ten triples; all sixteen even rows vanish. Thus this is an unequal-height control. I(h)=15/8 and L_h=5.

Take V(x1,x2,x3,z)=1-2*1{x1=x2=x3=z=0}, leaving z unqueried. Query x1, x2 along their zero branch, then the first shared bit, then x3 along the surviving shared-zero branch; retain every other sibling and both last children. The shared-zero carrier is the four-bit threshold positive on Hamming weights <=2. Its first-coordinate influence is 3/8; editing the zero vertex can only add influence there, so Inf_shared(F)>=3/8. The universal coordinate bound B<=1 and JS<=3 Inf therefore give Delta H_shared<=6 Inf_shared. Each private node is paid by (1). The total signed bill is at most inherited private-input entropy cost + the SAME R release +11 P_private+6 P_shared. The checker records every inherited quarter-core erasure, both nonconstant mux branch cores, every complete terminal spectrum, and the exact C=5 signed source-surplus identity. No supplied child bank is renewed.

## 6. First unsupported universal line

Unequal nonzero carrier heights no longer obstruct the point-edit private payment. General edits supported at more than one shared vertex can have different private functions at different vertices; their Fourier rows are no longer a single common translation, and the mass/curvature argument above does not provide their inherited conditional entropy payment. Even for one vertex, arbitrary e H(V) is retained in full and a universal certificate for V is still FEI-strength. Paying arbitrary shared-node bills and these inherited inputs from one prescribed unused ancestor surplus remains open. Independent review of this analytic argument is pending.

## 7. Extension: arbitrary two shared branches, one disjoint controller

The point restriction can also be removed when all edited vertices use the SAME V. Let h and D be arbitrary Boolean functions on the same shared cube, let A={D=-1}, p=Pr(A), and let V be any Boolean function on a disjoint private cube. Set F=h[1+1_A(V-1)]; its two shared branches are h and hD. If p=0, F=h and all private costs vanish. Otherwise define

    b_S=hhat(S), c_S=(h 1_A)hat(S), w_S=c_S^2/p,
    kappa=I(D)/2, R(mu)=kappa(1-mu^2).

Then, for EVERY private query,

    Delta_i H(F) <= p Delta_i H(V)+kappa a^2+11 Inf_i(F),
    Inf_i(F)=p Inf_i(V).                                      (7)

This is the SAME product-boundary reserve as before: D is the product of the two shared branches, and kappa(1-mu^2)=2q(1-q)I(D) for q=(1-mu)/2. The two shared branches may have arbitrary overlapping Fourier spectra. They do not depend on the private coordinates of V.

Here is a complete derivation. Parseval gives sum c^2=p and sum bc=p. Consequently y_S(mu)=b_S+(mu-1)c_S has total squared mass M=1-p(1-mu^2)<=1. All nonempty private rows equal c_S Vhat(T), whence

    H(F)=p H(V)+E(mu)+p(1-mu^2)[H(w)+log2(1/p)]-p g(mu),
    E(mu)=sum_S g(y_S(mu)).

Put L=H(w)+log2(1/p),

    J(mu)=E(mu)-H(h)+(pL-kappa)(1-mu^2)-p g(mu).

Thus H(F)=p H(V)+H(h)+R+J exactly. Wherever the shifted coefficients with c_S!=0 do not vanish, let q_S=y_S^2/M. Then

    E''=2p[H(w)+D_2(w||q)-log2 M]-6p/ln(2).

This identity follows by expanding -2 sum c_S^2 log2(y_S^2)-6p/ln(2); it retains the COMPLETE relative entropy D_2(w||q), including terms on all w-positive rows. Define A_*(mu)=E(mu)+(pL-kappa)(1-mu^2). Its curvature satisfies

    A_*''=2p D_2(w||q)-2p log2 M
             +2kappa-2p log2(1/p)-6p/ln(2) >= -6p/ln(2).    (8)

The nonnegative terms are not replaced by a new entropy certificate. Gibbs' inequality gives D_2>=0 (apply ln u<=u-1 to q/w on the w-positive support). The boundary estimate kappa>=p log2(1/p) is proved below. The C1 gluing argument of section3 handles every shifted-row zero; M=0 is possible only for p=1, mu=0 and is an isolated point. Therefore A_*+3p mu^2/ln(2) is convex. The same midpoint argument and |g'|<=6 prove Delta J<=11p Inf_i(V), hence (7).

The needed boundary estimate is elementary. A subset of m cube vertices spans at most (m log2 m)/2 internal edges. Induct on cube dimension, splitting into sizes m0,m1. The two halves contribute at most (m0 log2 m0+m1 log2 m1)/2 and the matching between them at most min(m0,m1). The induction closes because h2(t)>=2 min(t,1-t), the chord bound from binary-entropy concavity. Use 0 log 0=0. Thus the edge boundary is at least dm-m log2 m=Np log2(1/p), and I(D)=2|boundary A|/N proves kappa>=p log2(1/p). All endpoints, including p=1, are covered.

Any adaptive PRIVATE stopping tree now satisfies (2) with e replaced by p and the SAME R, since shared h,D are unchanged and private means are a martingale. The inherited input term is still p[H(V)-E H(V_leaf)], not zero. At an actual shared query, kappa-average kappa_child=Inf_j(D)/2 and the corresponding original-bank release is (1-mu^2)Inf_j(D)/2. This proves conservation, not a bound for the actual shared-node entropy bill. Full signed child surpluses and both complete terminals remain necessary. If different activated vertices carry different private functions, the tensor factor c_S Vhat(T) disappears and (8) no longer supplies the payment. That multi-profile conditional problem, rather than unequal carrier heights or a common arbitrary event, is the next unsupported line.
