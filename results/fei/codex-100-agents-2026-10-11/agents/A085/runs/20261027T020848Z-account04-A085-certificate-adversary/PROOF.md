# Signed admission: verdict and scope

A097-SIGNED-ARBITRARY-REFERENCE-FLOOR-OWNER@1 holds as stated. Its statement hash is `8e3a5074a89063d0bb52d1a8ac5d9e3743fbbd167e47b159b86e4b760171e170`. Two equalities in the proof text require the corrections already identified by A093, A098 and A099. Neither changes the displayed claim statement. Full FEI remains OPEN.

## Exact reconstruction

All logarithms are base 2. Let p be a finite probability law, p(0)=r, t=1-r>0, A a subset of its nonempty labels, a=p(A) with 0<a<t. The reference q has the same vacuum mass r, finite CE(p,q), and b=q(A) with 0<b<ell<t. A compatible target preserves BOTH q conditional profiles on A and C=nonempty minus A, including reference-only atoms. Its masses on the two cells are z and t-z; z>=ell. Thus

F(z)=CE(p,q_z)-CE(p,q)=a log(b/z)+(t-a)log((t-b)/(t-z)).

This expansion uses only positive-p atoms. Their reference masses are positive by finite CE. Zero-p atoms contribute zero, but remain in the normalized profiles. A zero vacuum r=0 contributes zero; it does not require evaluating log(0). Every finite candidate has ell<=z<t. At z=t, the positive true C mass makes CE infinite.

The derivative is

F'(z)=(-a/z+(t-a)/(t-z))/ln(2)=t(z-a)/(z(t-z)ln(2)).

The missing factor t in A097's proof is positive and therefore leaves the sign and the unique minimizer z*=max(a,ell) unchanged. Alternatively F''(z)=[a/z^2+(t-a)/(t-z)^2]/ln(2)>0. The price is exactly F(z*), equivalently t times the difference between the two Bernoulli KLs with parameters a/t against z*/t and b/t. Its sign is unrestricted. Evaluating at ell and applying ln(1+x)<=x gives the author's sufficient upper bound; that bound is not the sharp necessary price.

At a full physical terminal, suppose P and Q have the IDENTICAL disjoint controller component and seed weight beta, with seed laws p and q. The beta factors cancel inside the log ratio, so replacement changes the FULL cross entropy by beta F(z*). This conclusion includes beta=0 by zero contribution, without evaluating any seed log. Summing ALL terminal reaches rho gives S=sum rho beta F. If original capacity is B, current FULL CE is C, and U includes every still-charged old bill, then the new residual is exactly

B-(C+S)-U=(B-C-U)-S.

Consequently SAME-owner payment is equivalent to S<=B-C-U. Dropping negative terms is sufficient but can be wasteful. A release is prepaid mismatch removed from CURRENT C; it cannot also be booked as a separate new refund. No dimension, leaf-count multiplier, new influence account or fresh source is introduced here.

## Physical-query identity: corrected full bill

For a physical query j, let barP and barQ be parent spectral laws marginalized over spectral bit j. The average actual child law equals barP: averaging (u+v)^2 and (u-v)^2 gives u^2+v^2. If BOTH children inherit barQ, chain-rule expansion gives

CE(P,Q)=CE(barP,barQ)+B_j+D_occ,

where B_j=H_P(S_j|S_without_j) and D_occ=sum_T barP(T) KL(P(S_j|T)||Q(S_j|T)). Thus

B_j+average CE(child,barQ)-CE(P,Q)=-D_occ<=0.

The author's literal CE-only increment=-D_occ omits B_j. Its CE monotonicity conclusion still holds. A two-bit sign AND with table (-1,1,1,1), Q=P, has uniform parent spectrum, CE=2 and B_j=1. Each inherited child reference is uniform on two labels and each actual child is a point mass, so average child CE=1, D_occ=0. The CE-only equality reads -1=0 and fails. This is dimension minimal for a matched-reference positive-erasure example: on zero or one Boolean bit the spectrum is a point mass, so B_j=0. This control corroborates A093's erratum and is not a new refutation of the claim statement.

## Exact sign boundary on the smallest Boolean seed

Take the SAME two-bit sign AND, whose squared spectrum is p=(1/4,1/4,1/4,1/4), and let A be one nonempty atom. Set t=3/4, a=1/4, ell=1/3, and incoming calibrated references

q_b=(1/4,(3/4-b)/2,(3/4-b)/2,b), 0<b<1/3.

Every q_b is normalized and finite CE, with the same profiles on A and C. Every optimal target is the SAME q*=(1/4,5/24,5/24,1/3). The signed admission cost satisfies the exact identity

4 Delta(b)=log(432 b(3/4-b)^2/25).

Its zero in (0,1/4) is

bcrit=(7-2 sqrt(6))/12.

Indeed

432 b(3/4-b)^2-25=432(b-1/3)(b^2-7b/6+25/144).

The other roots are 1/3 and (7+2 sqrt(6))/12>3/4. The derivative of b(t-b)^2 is (t-b)(t-3b)>0 on (0,1/4). Thus Delta<0 for b<bcrit and Delta>0 for bcrit<b<1/3 (the sign persists on (1/4,1/3) by the factorization). In particular b=1/8 gives Delta=(1/4)log(27/32)<0; b=1/4 gives Delta=(1/4)log(27/25)>0. With the supplied disjoint weight beta=3/8 these reproduce A097's two prices.

For every m>=4, define b_m^- = floor(2^m bcrit)/2^m and b_m^+=b_m^-+2^-m. Irrationality of sqrt(6) means neither endpoint equals bcrit. Both references satisfy every hypothesis, their TV distance is exactly 2^-m, and their signed prices have opposite signs. Irrationality here follows, for example, from prime valuations in u^2=6v^2 for relatively prime integers: the exponent of 2 is even on the left and odd on the right. Hence NO fixed absolute error tolerance on incoming event mass, by itself, can certify this signed payment sign. This is an all-m analytic statement; the finite test is not its universal bridge.

The first collision in the FROZEN m=4,...,160 dyadic-bracket diagnostic is m=58:

b^- =50464827764806005/288230376151711744,

b^+ =50464827764806006/288230376151711744.

Their exact signs are negative and positive, but their Python binary64 conversions coincide. Earlier m in this particular bracket sequence do not coincide. This is a statement about that formula/platform/grid, not the smallest possible floating-point failure of any implementation. Precision here varies the incoming reference, not the Boolean dimension. There is no FEI counterexample: the actual two-bit seed has H=2, I=1, and H/I=2 throughout. The independent checker caught and corrected an earlier explanatory I=3/2, mistakenly copied from the three-bit seed; direct spectral degree weighting gives (0+1+1+2)/4=1.

The seed dimension 2 is minimal for this calibrated interior two-cell class. On 0 or 1 Boolean bits the squared spectrum is a point mass. Its nonempty mass is either 0 or 1, and no nonempty event can have 0<a<t. The checker enumerates every table and every nonempty-label event in these dimensions. The general law theorem does not assume Boolean realizability of q; references are arbitrary normalized laws, exactly as in the reviewed claim.

## Checks that could fail

The checks target an incorrect derivative factor, mismatched vacuum, unnormalized ghost profiles, omitted outcomes, nonpositive denominators, an endpoint with infinite CE, reused old margin, an unproved Boolean realization, and floating cancellation near a zero. The finite checker tests interior scalar optima, actual integer-Walsh spectra and both physical children, ghost-bearing profile identities, unchanged statement hash, exact owner algebra and all fixed dyadic brackets. An independent checker reconstructs the radical brackets by integer square roots without importing the first helper. The calculus, positivity, support argument and irrationality provide the continuum and all-m scope. A separate Lean check concerns the rational derivative algebra only, and does not formalize CE, convexity, the owner theorem or FEI.

## First unpaid universal step

A useful arbitrary-core mandatory compatible class and an original complete source with B<=K I(core), including sufficient unused B-C-U after every old charge, remain unconstructed. Arbitrary profile declarations establish neither necessity nor affordability. For numerical use of this admission oracle, certify the signed likelihood difference with intervals or exact products, and refine until its sign is resolved; zero must be allowed and no uniform precision cap is justified. The two-bit example is a concrete audit control for that exact liability, not an isolated FEI class result or an assertion of priority over the elementary likelihood calculation.
