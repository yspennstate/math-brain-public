# Independent quadratic-certificate review and centered logarithms

All entropy and KL use bits, influence is ordinary physical flip probability, and all Boolean functions are on finite uniform cubes. The explicitly reviewed statement is A085-QUADRATIC-CONDITIONAL-REMAINDER-CERTIFICATE@1. Its source is not repaired. The stronger upper envelope below is a separate A073 refinement, pending independent review.

## 1. Complete laws reconstructed from signed amplitudes

For even d>=2 set delta=2^-d, t=sqrt(delta). Let b(y)=(-1)^(sum_j y_(2j-1)y_(2j)), q(u,v) negative only at the 0/1 input11, and F=b+1_(y=0)(q-1). Each quadratic two-bit factor has signed Fourier coefficients (1,1,1,-1)/2. Hence hat b(T)=sigma_T t, and the counts of the two signs are N_sigma=(2^d+sigma 2^(d/2))/2. Expanding the actual gate gives amplitudes over each core Fourier set

    sigma_T t-delta/2, delta/2, delta/2, -delta/2.

All are nonzero. For either queried pair coordinate, e=delta/2 and the complete row laws, with V the partner occupancy, are

    mu(T,0)=mu(T,1)=delta/2,
    r(T,0)=delta c_sigma, r(T,1)=delta^2/2,
    c_sigma=1-sigma_T t+delta/2.

Their full sums are one. The V quotient is mu_V=(1/2,1/2), r_V=(1-e,e). Core conditionals agree at V=1. At V=0 the derivative is uniform and the reference is delta c_sigma/(1-e). Therefore

    D_full=D_binary+D0/2,
    D0=sum_sigma ((1+sigma t)/2) log2[(1-delta/2)/c_sigma],
    L_i=e D0/2, L_u+L_v=delta D0/2.

This is complete-reference marginalization, not conditioning the reference on derivative support. Physical flips give each core influence a=(1+delta)/2. The retained M_i/e=1+(1/2)log2((1-e)/e)-D0/2 remains large; nothing below pays that charge.

## 2. Independent acceptance of A085's analytic scope

Let C=c_sigma under probabilities p_sigma=(1+sigma t)/2. Its mean is m=1-delta/2, its variance is delta(1-delta), and its largest value is at most13/8. Since -ln x has second derivative1/x^2, its Jensen gap is at least Var(C)/(2(13/8)^2). Dividing by ln2<1 and using1-delta>=3/4 proves

    D0>(24/169)delta>0.

For the original upper bound, set a0=1+delta/2 and z=t/a0. Elementary log algebra yields

    (ln2)D0=ln(1-delta/2)-(1/2)ln(1+delta^2/4)+t atanh(z).

The integral bound atanh(z)<z/(1-z^2), together with ln(1-delta/2)<-delta/2, gives

    (ln2)D0 < delta[(1+delta/2)/(1+delta^2/4)-1/2]
             <=(5/8)delta.

Because ln2>2/3, this gives D0<(15/16)delta. The pair loss is consequently less than (15/32)delta^2. The dedicated reserve inequality (15/32)delta^2<=(3/64)a is equivalent to20delta^2<=1+delta, which factors as (4delta-1)(5delta+1)<=0. Its endpoint equality at d=2 is harmless because the preceding analytic bound is strict. Every mathematical clause of A085@1 holds without a repair. The Taylor coefficient stated in its proof is also confirmed by section4 below.

The separate numerical clauses concern only the source's frozen binary64 expression and evaluation order. Reimplementing that exact expression over the ordered540 even dimensions2..1080 yields first zero d=104, no negative value, and first zero directly squared gate atom at d=538. Thus the original platform-scoped clauses hold on the current environment. The analytic theorem has no dimension cutoff or floating premise. A distinct rational certificate below proves positivity at104 and1076.

## 3. Cancellation-safe rational sign certificate

For any finite rational weights p_j summing to one, rational x_j with |x_j|<1, and exact centering sum_j p_j x_j=0, define

    J=-sum_j p_j ln(1+x_j).

The linear terms cancel EXACTLY, so

    J=sum_j p_j sum_(k=2..N) (-1)^k x_j^k/k + R,
    |R|<=sum_j p_j |x_j|^(N+1)/[(N+1)(1-|x_j|)].

This follows from the absolutely convergent logarithm series; bounding1/k by1/(N+1) in the tail proves the displayed error. It applies to complete finite conditional laws whose reference-to-derivative ratios equal1+x_j, provided the stated support, centering and range conditions are checked. It does not cover arbitrary discarded reference mass or ratios outside this range without a separate reduction.

Here take p_sigma=(1+sigma t)/2 and x_sigma=c_sigma/m-1=(delta-sigma t)/m. Their weighted mean is exactly zero and max|x_sigma|<=6/7<1. Then J=(ln2)D0. The implementation divides J's rational interval by delta BEFORE the positive ln2 interval. Thus it never subtracts separately rounded logarithms of near-one numbers to recover an exponentially small residual. Fixed N=24, frozen before execution, certifies all requested signs; it is not refined even when the d=2 display interval is relatively wide.

The natural ln2 interval uses its positive atanh expansion at1/3 with24 terms and tail at most2(1/3)^49/[49(1-1/9)]. Every numerator interval divided here is strictly positive; division uses the lower numerator over upper denominator and vice versa. The complete rational margins are saved per dimension. For d=104,538,1076 they give

    0.721347520 < D0/delta < 0.721347521.

Therefore every such D0 is strictly positive, including when binary64 represents delta itself as zero. No large truth table is implied: these are compressed certificates for the explicitly proved amplitude counts. The all-dimensional positivity proof is section2, not finite extrapolation.

## 4. Separate sharper upper envelope and reserve

For every t>0,

    (1+t^2/2)sinh(t)-t cosh(t)
       =sum_(k>=1) [k(2k-1)/(2k+1)!] t^(2k+1)>0.

The entire series converges and every displayed coefficient is positive. Dividing by positive cosh(t)(1+t^2/2) gives tanh(t)>t/(1+t^2/2). As atanh is increasing,

    atanh[t/(1+t^2/2)]<t.

Substitute into the exact identity of section2. Since ln(1-delta/2)<-delta/2 and ln(1+delta^2/4)>0,

    0<D0<delta/(2 ln2),
    L_u+L_v<delta^2/(4 ln2).

The coefficient1/(2ln2) is asymptotically sharp: divide the exact identity by delta=t^2 and let t tend to zero. The three terms tend to-1/2,0,1 respectively, giving D0/delta->1/(2ln2). The permitted even dimensions tend to infinity and give t->0. This establishes sharpness of this particular linear-in-delta envelope, not an optimal physical reserve.

The physical core influence a=(1+delta)/2 gives

    (L_u+L_v)/a < delta^2/[2(1+delta)ln2]
                  <=1/(40ln2)<3/80.

The rational step is20delta^2<=1+delta for delta<=1/4; the last strict inequality is ln2>2/3. Hence the dedicated remainder-only core fraction can drop from3/64 to3/80, a reduction of3/320. The fixed rational ln2 interval certifies a positive uniform margin of3/80-1/(40ln2)>0. This allocation pays these two losses only once. It neither pays retained M_i nor shows that the named reserve is genuinely unused in a descendant stopping-tree ledger.

## 5. Validation and surviving universal gap

The independent program uses own prior exact helpers, not upstream executable code. Physical d=2,4,6 truth tables are checked by integer Walsh transforms, signed inverses, Parseval and actual flips, then complete joint KL and every signed amplitude. Compressed certificates use d=2,4,6,8,32,104,538,1076. The source negative-control scan is separately labeled. The pilot and main outputs are saved immediately; no precision increase, domain escalation or failed mathematical assertion occurred.

The first unsupported line remains the existence of one absolute K satisfying

    sum_i e_i D(mu_i||r_i)>=sum_i e_i log2(1/e_i)-K I(f)

for all actual Boolean signs. A096's new non-flat result pays a quotient remainder from explicit root influence quotas, but its independently reviewed price-five obstruction shows why such quotas cannot silently become available child slack. NEXT should apply the centered certificate to the exact non-flat conditional law at an actual physical query, retaining its sufficient signed amplitude statistic and both terminal debts, then certify availability of the one claimed child bank. More display precision on this completed family cannot supply that missing payment.
