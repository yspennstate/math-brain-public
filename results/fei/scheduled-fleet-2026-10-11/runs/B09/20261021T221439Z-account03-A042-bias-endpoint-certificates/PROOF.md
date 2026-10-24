# Uniform zero and unit cofactor endpoints

All logarithms are natural. This is a local endpoint certificate, not a solution of FEI. Let Z be an integer-valued random variable, j an integer, a=E(Z-j), b=E((Z-j)^2), and V=Var(Z)=b-a^2. Assume 0<b<=1/4. Integer quantization gives |a|<=E|Z-j|<=b, hence b(1-b)<=V<=b. No bound on the support size, number of variables, or relative rates of rare outcomes is used.

Define h(x)=x^2 ln(1/x^2), h(0)=0.

## Zero endpoint

If j=0, then

    0 <= h(E Z)/V <= 2b ln(1/b)/(1-b).                 (1)

Indeed |E Z|<=b<=1/4, and t^2 ln(1/t^2) is increasing on [0,1/4] (its derivative is 4t ln(1/t)-2t>0). Thus h(E Z)<=2b^2 ln(1/b); divide by V>=b(1-b)>0. The right side tends to zero. The convergence is uniform over all distributions satisfying the displayed moment bound, including unrelated rates of input biases. If b=0, Z=0 almost surely and h(E Z)=V=0; no quotient is formed.

## Unit endpoints

If j=sigma in {-1,1}, then

    | h(E Z)/V + 2 sigma a/b | <= 8b.                 (2)

Write x=sigma+a. On the segment between sigma and x, |x|>=3/4. The derivatives of h away from zero are h'(x)=-2x(ln(x^2)+1), h''(x)=-2ln(x^2)-6, h'''(x)=-4/x. Taylor's theorem gives

    h(sigma+a)=-2sigma a-3a^2+r, |r|<= (4/3)|a|^3,

where the stated remainder uses the weaker bound |h'''|<=8 (valid even on |x|>=1/2). Since |a|<=b,

    |h/V+2sigma a/b|
      <= (3b^2+(4/3)b^3)/(b(1-b)) + 2b^3/(b^2(1-b))
      = (5b+(4/3)b^2)/(1-b) <= (64/9)b < 8b.

In particular every subsequential limit lies in [-2,2], because |a/b|<=1. The positive part is at most max(0,-2sigma a/b)+8b. Oscillating bias paths need not have a ratio limit. Bernoulli excursions Z=sigma+D with D=-sigma with probability epsilon attain the positive limit 2; D=sigma attains -2. Both are genuine integer profiles; actual AND cofactors realize the positive example. For |j|>=2, h(j)<0, so continuity makes the positive residual identically zero sufficiently close to that endpoint. This last statement is qualitative for fixed j.

## Exact physical Fourier scaling, including vanishing v_S

For an actual Boolean sign f under an interior independent product law, let S be nonempty, k=|S|, v_i=4p_i(1-p_i), v_S=product v_i, c_S=fhat(S)/sqrt(v_S), and P(T)=fhat(T)^2. Define the integer physical cofactor Z_S=(1/2)sum_{x_S}(-1)^(k-|x_S|)f(x_S,x_notS). Put W_S=sum_{T strictly containing S}P(T). Direct centered-product integration and Parseval give

    m=E Z_S=2^(k-1)c_S,
    V=(4^(k-1)/v_S)W_S,
    R_S=E_S-(k-1)ln4 P(S)=(v_S/4^(k-1))h(m),
    E_S=P(S)ln(v_S/P(S)).

Consequently R_S/W_S=h(m)/V EXACTLY whenever W_S>0. Equations (1)-(2) are thus endpoint certificates for the signed local entropy residual divided by its entire actual strict-superset mass. They remain uniform when biases within S degenerate as well: their potentially vanishing scale cancels before taking the limit. Deterministic inputs contract first; at W_S=0 the ratio is undefined. The moment condition is a condition on the physical profile, not on an arbitrarily selected spectral fragment. This proof independently reconstructs A044's mean/variance scaling; it does not infer bounded congestion by summing local limits.

For a finite physical complement whose law tends to a corner x*, take j=Z_S(x*). Then b=sum_x Pr(x)(Z_S(x)-j)^2 tends to zero. This is a finite sum for each fixed gate, so no limit exchange needs an infinite dominating bound. More generally the displayed moment condition itself suffices for varying dimensions.

## Actual AND endpoints and degree ownership

For AND_d, S_i=[d]\{i} has Z_Si=X_i, V_i=p_i(1-p_i), and W_Si=P([d])>0 at every interior product law. Thus

    R_Si/P([d]) = phi(p_i),
    phi(p)=2p ln(1/p)/(1-p), 0<phi(p)<2.

For 0<p<=1/2, phi(p)<=4p ln(1/p). For p=1-epsilon with 0<epsilon<=1/2,

    phi(1-epsilon)=2-epsilon-2sum_{k>=2}epsilon^k/[k(k+1)],
    |phi(1-epsilon)-(2-epsilon)|<=epsilon^2/[3(1-epsilon)].

The series follows by multiplying the absolutely convergent series for -ln(1-epsilon) by (1-epsilon)/epsilon; its tail uses k(k+1)>=6. Hence at any independent-rate corner with d1 coordinates tending to 1,

    sum_i R_Si/P([d]) -> 2d1,
    |sum_i phi(p_i)-2d1|
      <= sum_{p_i->0}4p_i ln(1/p_i)
         +sum_{p_i->1}[epsilon_i+epsilon_i^2/(3(1-epsilon_i))]

once all endpoint distances are <=1/2. For d>=3, the exact codimension-one residual total is <=2d P([d])<=3(d-1)P([d]); degree sharing, unlike exclusive profile allocation, survives. This is only the codimension-one ledger. All other coefficients and terminal entropy still require payment.

## Independent admission check and first unpaid line

A045's source objection remains valid: retaining an integer cofactor of mean p_i forces V_i>=p_i(1-p_i); fractional allocation lambda_i of its only top packet forces lambda_i>=1 at every interior p_i, however close to an endpoint. The exact entropy cost, however, tends to zero at the zero-profile end while this admission fraction stays 1. Taking a limit in the admission inequality therefore cannot justify discarding the actual profile or renewing an owner budget. At fair AND3, top-packet deletion and normalization gives empty mass 3/5, which is not a possible squared Boolean mean on that fair cube. This is a necessary-condition rejection for every phase choice.

The first unsupported universal line remains: integrate the zero-profile refunds and signed unit-profile charges into ONE complete conditional reference, with ordinary KL, normalizer, off-support mass and full terminal entropy, bounded by unused root deficit independently of dimension. These local endpoint certificates neither supply that assignment nor bound its congestion. A045's all-d obstruction and A044's local inequality are preserved.

Integer admission is essential, rather than decoration: a real profile taking 0 and delta with equal probabilities has a=delta/2, b=delta^2/2, V=delta^2/4, and h(a)/V=ln(4/delta^2), which diverges as delta tends to zero. It violates the integer increment bound |a|<=b. Also, approaching a mean of zero alone does not imply b tends to zero: a nonconstant symmetric integer profile has zero mean and positive variance. Equations (1)-(2) require the stated second-moment localization, not just convergence of the mean. At a unit mean with fixed positive variance they make no vanishing-error assertion.
