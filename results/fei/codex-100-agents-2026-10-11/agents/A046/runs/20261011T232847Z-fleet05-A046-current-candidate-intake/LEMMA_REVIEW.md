# Analytic lemma review requested by B10 notes v2

The source scalar certificate was replayed read-only: PASS, 4,100 strictly positive boxes, three boxes discharged by lemma B, seven splits, minimum displayed lower bound about 0.0002353687, 3.02 seconds. This is a faithful replay of the source interval implementation, not an independent rational implementation of all continuum boxes. Below the analytic regions are independently reconstructed with rationally certified constants; the near-fair region is widened to make source decimal threshold roundoff immaterial there.

Write p<=1/2, beta=arcsin sqrt(p), theta=beta/2+d, 0<=d<=pi/4, F=phi(theta)+phi(theta-beta), phi(t)=h2(sin^2 t), and R(p)=h2(p)-Delta(p)/2. The fundamental domain follows from period pi/2 and reflection theta->beta-theta. R'(p)=log2((1-p)/p)/2+1/[2(1-p)ln2]>0 on (0,1/2].

Lemma A HOLDS for 0<p<=2/25. Let a=|sin theta|, c=|sin(theta-beta)|. As proved in REPORT step 4, a+c>=sqrt(p), a^2<=321/500 and c^2<=1/2. Rational exp(3) bounds certify 49/1000<e^-3<1/20. If max(a,c)>e^-3/2, at least one squared amplitude belongs to [e^-3,321/500]. By concavity, h2 there is at least the minimum of its endpoint entropies. Monotonicity below 1/2 and rational log intervals give h2(e^-3)>h2(49/1000)>7/25, while h2(321/500)>7/25. Thus F>7/25>131/500>R(2/25)>=R(p).

If both amplitudes are at most e^-3/2, convexity/increase of k(s)=s^2 log2(1/s^2) gives F>=(p/2)log2(4/p)+(p/2-p^2/4)/ln2. To bound R, use the positive series

    -ln(1-p)<=p+p^2/2+p^3/[3(1-p)].

Multiplying by 1-p/2 and discarding negative terms gives (1-p/2)(-ln(1-p))<=p+p^3/[3(1-p)]<=p+(2/69)p^2. Consequently

    F-R >= [1-1/(2ln2)]p-[(1/4+2/69)/ln2]p^2
         > (27/100)p-(41/100)p^2 >0.

The constants are exact rational comparisons checked in out/LEMMA_CONSTANT_CHECK.json. This supplies the complete source lemma-A case split with comfortable margins and no decimal-log claim as proof.

Lemma B HOLDS on the widened region 489/1000<=p<=1/2, |e|<=301/1000, where theta=beta+e. At regular points,

    phi''(t)=-4/ln2+2cos(2t)log2(cot^2 t)>=-4/ln2,

because cos(2t) and log(cot^2 t) have the same sign. phi is C1 at its entropy cusps; the displayed second derivative is locally integrable, so integrating the lower derivative bound gives phi(beta+e)>=h2(p)+2sqrt(p(1-p))*ell*e-2e^2/ln2, ell=log2((1-p)/p). The region used here contains no cusp of phi(beta+e), and phi(e) is handled directly, so no unjustified Taylor series across a cusp is needed.

For d=|e|<=301/1000, the sine Taylor lower bound sin(d)/d>=1-d^2/6 implies sin^2(d)>= (97/100)d^2; also sin^2(d)<=d^2<1/3<1/e. Since x log2(1/x) increases on [0,1/e],

    h2(sin^2 e)>= (97/100)d^2 log2[1/((97/100)d^2)].

Put A(d)=d^2[(97/100)log2(1/((97/100)d^2))-2/ln2]. Its bracket decreases with d, and rational intervals at d=301/1000 certify A(d)>d^2/2 for d>0. Thus

    F-R >= (p/2)ell+2sqrt(p(1-p))*ell*e+A(d).

For e>=0 this is nonnegative and strict unless p=1/2,e=0. For e<0, 2sqrt(p(1-p))<=1 gives lower bound ell*(p/2-d)+A(d). If d<=p/2 it is again nonnegative, with the same equality case. Otherwise d>=489/2000, ell<=log2(511/489)<13/200, and the negative part is at most (13/200)*(301/1000-489/2000), whereas A(d)> (1/2)*(489/2000)^2. The latter is strictly larger by exact rational comparison. This proves the source lemma-B semiconcavity argument with widened exact thresholds.

The fourteen constant checks use only Fraction arithmetic, a positive rational exp(3) series with geometric tail bound, a sine Taylor lower bound, and the earlier independently derived rational atanh logarithm remainder. The source-replay output is stored separately. Middle-region box signs still use the lead's interval implementation; independent rational recertification of those signs and partition coverage is not claimed here. The full finite-p theorem remains awaiting a complete certificate reviewer, while its exact reduction, both analytic boundary lemmas and corrected scalar asymptotic have been reconstructed.
