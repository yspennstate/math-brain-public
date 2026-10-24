# Independent reconstruction of the outer private-query interfaces

Verdict: HOLDS at the stated scopes of A091 stage17 first-private query and A057 stage17 later-private query. These are scoped reviews, not acceptance of a universal controller bound. Sources are the PROOF.md files in A091/runs/20261021T203312Z-account03-A091-composition-referee and A057/runs/20261021T223314Z-account03-A057-coherent-restriction-remainder. Both sources are read-only.

For A091, independently separate Fourier frequencies according to the nonempty core data block u, v or G, the nonempty B control block, and the completely empty row. Orthogonality of the DISJOINT core cubes eliminates mixed data rows, but the repeated G contributions must be added before squaring. With the source notation, these sectors give exactly

 B=(q-2q^2)(1-mh)+q^2 Var(u)
     +(Var(H)-(1-p)^2 Var(G)) Phi((1-q)^2,q^2)/2
     +Var(G) RG+R0.

This is the complete erasure, not an estimate. The four grouped bounds are respectively 2d,4d,4d,2d: Var(u)<=2(1-mh), Var(H)<=2(1-mh), (1-p)Var(G)<=Var(H), |m-h|<=1-mh. For R0 and RG the exact identity |a+b|+|a-b|=2max(|a|,|b|) must be used before estimating the pair. Phi(s^2,t^2)<=2|st| then gives the claimed12d. All inequalities remain valid at p=0, p=1, q=1/2 and d=0. No part of the argument depends on the shape of B or the dimension of G. The same fine reserve release is nonnegative by concavity; it need not be spent to obtain this erasure estimate.

For A057's later point coordinate, write B=P(1+x)/2, K=G+YA(u-G), D=Y(1-A)(v-G), b=PD/2 and L=K+b. The exact two Fourier amplitudes are Lhat and bhat. Since P is on a private block, summing its empty and nonempty frequencies gives sum |Lhat bhat|<=q sum |Khat Dhat|+d. Nonempty u-only and v-only rows do not overlap. Separating the G-nonempty and empty-data rows yields the source's overlap expression (1). Parseval for an arbitrary indicator A gives sum_nonempty Ahat^2=a(1-a); keeping the two Y coefficients paired gives max(|m|,|(1-a)m+a ell|), not a sum of two separate estimates. Thus S<= (1-a)(3/2+2a)(1-mn), and B<=2qS+2d<=(8+8a)d. A residual private point A has a<=1/2 or is certain; the latter makes the query irrelevant. Hence B<=12d at every applicable residual point node. B's arbitrary non-point current queries are NOT accepted in arbitrary dimension by this argument.

The scalar packet inequality is independently checked by considering the ratio z of the absolute amplitudes on [0,1] and differentiating 2z ln2-(1+z^2)ln(1+z^2)+z^2 ln(z^2). Its derivative changes sign once before1, and the expression vanishes at0 and1; inversion handles z>1. The physical JS term has the independently established bound2d/ln2. Neither source changes the old bank or removes either terminal.

code/review.py is a separate direct Fourier implementation. Its finite domain is intentionally wider than the later-point theorem at two B bits: all16 event tables, not a claimed arbitrary-dimensional non-point extension. The frozen review census checks the A091 identity and the claimed12d bound on every such small coordinate. These finite checks supplement the above reconstruction. This reviewer contributes no repair to either source version and does not independently review its own new wrapper extension.
