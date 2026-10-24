# Reused fallback under interrupted priority tests

All entropy expressions in this file use bits. Let A be the indicator of one point on r>=1 still-unqueried fair controller coordinates, q=2^-r. Let u and G be Boolean functions on disjoint remaining physical blocks, also disjoint from A. Put F=A u+(1-A)G, m=Eu, n=EG, delta=m-n, M=n+q delta, and d=(1-m n)/2. The fallback G is the SAME function in both children of a query of A. No independence of the two children is assumed.

Suppose G has an exclusive representation with independent disjoint data cores v_j, label probabilities p_j and variances V_j. The fine reserve is R=eta(q) Var(u)+sum_j eta((1-q)p_j)V_j, eta(x)=x log_2(1/x). For any A coordinate, its actual physical influence is i=2q d=q(1-m n). Write D=H(F)-(H(F_+)+H(F_-))/2 and kappa=R-(R_++R_-)/2. Then

    D-kappa <= (8+2/ln 2) i.                         (1)

This holds after arbitrary previous data restrictions. Such restrictions leave the u and G physical blocks disjoint, though both means may have changed.

## Exact computation and payment

Let Phi(a,b)=eta(a)+eta(b)-eta(a+b), V=Var(G), Vbar=sum p_j V_j and k(q)=eta(1-q)-eta(1-2q)/2. Conservation of label probabilities gives

    kappa=q Var(u)+k(q) Vbar,   k(q)>=0.              (2)

Separate Fourier coefficients into nonempty u subsets, nonempty G subsets, and the empty subset. Pair coefficients differing in the queried A coordinate. Directly, their erasure entropy B is

    B=q Var(u)+(q-2q^2)[V+delta^2]
      +V Phi((1-q)^2,q^2)+Phi(M^2,q^2 delta^2).     (3)

For example the nonempty remaining A masks contribute (2^(r-1)-1)*2q^2=q-2q^2; the empty remaining A mask is the last Phi packet. Equations (2),(3) retain the shared fallback exactly.

The elementary binary entropy bound Phi(a,b)<=2 sqrt(ab) holds for nonnegative a,b in bits. Here is an analytic proof. Write p=(1-tanh x)/2, x>=0; h_2(p) cosh x = [cosh x ln(2 cosh x)-x sinh x]/ln 2. Its derivative is [sinh x ln(2 cosh x)-x cosh x]/ln 2. Put f(x)=x-tanh x ln(2 cosh x). Then f'(x)=sech^2 x [1-ln(2 cosh x)], so f increases and then decreases, with f(0)=0 and limit f(infinity)=0. Hence f>=0, the displayed entropy expression decreases, and it is at most its value 1 at zero. Endpoint values follow by continuity.

Also V+delta^2=1+m^2-2mn<=2(1-mn)=4d, V<=4d and |delta|<=1-mn=2d. The last inequality follows by squaring: (1-mn)^2-(m-n)^2=(1-m^2)(1-n^2)>=0. Since |M|<=1 and q<=1/2, (2),(3) imply

    B-kappa <=4qd+8qd+4qd=16qd=8i.

The exact restriction split is D=B+J, where J is the Jensen-Shannon term of the two squared child spectra. The physical Hellinger bound J<=2i/ln 2 proves (1). No positive lower bound on D-kappa is asserted here.

## Ordered priority stopping, with arbitrary data interruptions

Let A_1,...,A_k be point indicators on pairwise disjoint control blocks of arbitrary positive widths. Let u_1,...,u_k be Boolean cores on pairwise disjoint data blocks, disjoint from all controls. F returns the first u_j whose A_j succeeds, and +1 if no test succeeds. Use a physical restriction tree that queries controls in priority order: finish or fail the current point test before querying the next test. Data coordinates may be queried anywhere between these control queries, with adaptive choices. Skip irrelevant controller blocks after success. Stop as soon as the output core is identified, or earlier at an arbitrary finite frontier.

At every live controller node, the function is exactly the reused-fallback form above. Thus (1) prices every controller residual uniformly, independently of k, widths, number of data interruptions, or total tree depth. Earlier inactive labels have zero probability and cause no term. For the fine U=sum p_j[H(u_j)-eta((Eu_j)^2)] and R=sum eta(p_j) Var(u_j), the already established A059 signed data inequality is D<=drop(U+R)+(3/ln 2)p_j beta_j^2. Telescoping gives, for any frontier,

    H(F) <= U_root+R_root+(3/ln 2) T_data
            +(8+2/ln 2) Pi_ctrl+E[H_leaf-U_leaf-R_leaf]. (4)

T_data and Pi_ctrl are the expectations of the singleton-weighted data bill and actual controller influence spent on THIS SAME tree. Formula (4) follows by summing per-node inequalities with visitation probabilities; it pays no quantity twice. Once all relevant controllers are resolved, R_leaf=0 and the terminal term is eta((Eu_leaf)^2)<=Var(u_leaf)/ln 2<=I(u_leaf)/ln 2. The first inequality follows from -x ln x<=1-x; the second is Poincare. Inherited U_root is retained. This is a stopping payment theorem, not universal FEI.

An explicit growing-depth family covered by (4) is the priority function with k=d stages, each A_j the all-zero point on d private controller bits and each u_j a private balanced literal. Its prescribed ordered controller tree has worst-case control depth d^2. Insert a query of u_j after the first tested bit of A_j to obtain data interruptions; (4) has the same constant for every d. These are actual Boolean functions with d^2+d inputs.

## Provenance, limits, and next unsupported line

A087 already closes the killed-child and r=s=1 independent-child residuals; A028 already closes a control-only arbitrary-width priority schedule. These are not claimed as new here. The new use of (2),(3) is the interrupted r>=2 priority test with a repeated fallback, singled out by A087 as its next gap. The proof does not claim arbitrary controller order. The first unsupported extension is that an arbitrary exclusive controller admits a tree with all residuals bounded by a uniform multiple of same-tree influence. In particular, querying later priority tests before earlier ones are decided is outside (4).
