# One genuinely shared, leafless defect is paid on its original primes

For ALL integers2<=a<=b, remove the named edge(0,a) from K_(a,b). Let f' be the actual uniform Boolean edge DNF on the surviving ab-1 primes. Keep both endpoint orders and actual rarity1/4; fix lambda_e=1/b on EVERY surviving gate. All incidence constraints hold, since deleting an edge only lowers their sums. For a,b>=3 there are no degree-one vertices. Unlike the complete-table calibration, this edge DNF contains the induced P4 on the missing endpoints and one additional vertex in each part. The result below is a full coding certificate for this actual damaged table, not an FEI novelty claim.

Its SAME original normalizer is D'=(1+1/(4b))^(ab-1)-1. A family of distinct actual source-SCC-rooted queue runs, with all probabilities retained, has positive output subprobability Q' on every nonempty A and satisfies

    C'=sum_(A!=empty) f'hat(A)^2[-log2 Q'(A)]
       < (297/8) I(f') <38 I(f').                        (1)

No extra physical controller, added leaves, replaced function, changed prime table or sampled-set weight choice is used. The old complete bipartite function f is only an analytic comparison for its explicit coefficients. Its reference never replaces the actual Q'.

## Repair actual runs with at most one additional root

For a one-sided set, each selected vertex is an isolated singleton root, summing over its ACTUAL surviving neighbors. A special left endpoint has b-1 choices and a special right endpoint has a-1. Since a,b>=2, the exact one-sided numerators are at least64^-s and (a/(64b))^t, respectively. This is a sum of distinct actual labels, rather than permission to use the removed gate.

For a mixed set with a selected nonspecial endpoint on each side, choose those endpoints for the double-star root. Every other selected vertex is adjacent to both appropriate root endpoints; the old double-star is legal and all gates survive.

The only remaining mixed configurations have A_L={0}, or A_R={a}. Consider A_L={0}. If a is not selected, one ordinary double-star works. If a is selected together with another right vertex j, root the star on(0,j) and cover A without a by that star. Give a its own singleton root on(1,a); vertex1 lies outside A. This root is disjoint in OWNED coordinates and neither root support meets the other's owned set. Both are source SCCs. The original fixed initial root order is retained. The symmetric construction handles A_R={a}. The extra root contributes exactly lambda*pi*(1/4)*(1/2)=lambda/32 to the numerator, not a free gate name.

Finally A={0,a} has no available root pair. Use exactly the two isolated singleton roots(0,a+1) and(1,a). Their supports are disjoint and their exact numerator is(lambda/32)^2. The assumptions a,b>=2 make these gates available. No denominator is cancelled at an endpoint where it is zero.

For k=|A|, the mixed repaired numerator is either the old star W_k, W_(k-1)*(lambda/32), or(lambda/32)^2. Equation(3) of LEAFLESS_CERTIFICATE gives W_j>=(lambda/48)^(j-1). All three cases imply the uniform actual lower bound

    N'(A)>=(lambda/64)^k       for mixed A.             (2)

All unused surviving gates remain in D'. This proves a positive actual same-table subprobability on every nonempty set, including the formerly missing pair. It also gives the complete occupation estimate

    C' <= v_f' log2 D' +6I' +R'log2(b/a)+M'log2 b,     (3)

with the actual right-only and mixed spectral expected degrees R',M'. The extra rarity and child-count factors have already been paid in(2); no hidden overhead term is deferred.

## Pay the changed spectrum and changed physical influence

Deleting(0,a) changes the output at exactly ONE physical input: only the two missing endpoints positive and all other bits negative. Put u=2^-a,v=2^-b. Every Fourier coefficient of the difference has absolute value2uv. Every nonempty coefficient of f has absolute value at least2uv, by the exact three-sector formulas in LEAFLESS_CERTIFICATE. Thus

    f'hat(A)^2<=4 fhat(A)^2  (A!=empty),
    R'<=4R,  M'<=4M.                                    (4)

This bound is termwise and includes coefficients that cancel to zero; no phase realization is assumed. Equations(6),(7) of the complete-table certificate therefore yield

    R'log2(b/a)+M'log2 b <=20 I_L(f)<=20 I(f).          (5)

Flipping a single vertex changes each physical influence by at most2/2^(a+b)=2uv, because exactly one undirected edge in that direction changes its crossing status. Consequently |I'-I|<=2(a+b)uv. As u,v<=1/4,

    I=2a u(1-v)+2b v(1-u)>=6(a+b)uv,
    I'>=I-2(a+b)uv>=(2/3)I.                            (6)

No original influence is silently substituted for the changed one. Combining(3),(5),(6) bounds the full occupation bill by36I'. Apply A008's independently reconstructed universal width-two root payment to the actual f', surviving table and fixed lambda: v_f' log2 D'<9I'/8. This gives(1).

## Scope and first unsupported line

The proof pays a concrete shared/leafless incidence after a genuine missing edge, including its same-reference cost and all true spectral sectors. It does not claim a new general FEI class, globally optimal weights or arbitrary damaged-graph payment. With a growing set of deleted edges the coefficient comparison4 in(4) can grow, and the two-root repair need not exist with this constant. The next mathematical obligation is a bounded-cost actual forest repair for a growing deletion matching PLUS a spectral/influence payment that avoids a square of the number of missing edges. Replacing the graph by its completion would not meet that obligation.
