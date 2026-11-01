# P0004: a nonstationary bounded-degree obstruction and the p=1 boundary

Label: proofs of a refuted generic route and a boundary case, pending w347. The random-cluster limit for p in (p_c,1) is not proved or disproved.

Let c_n(o) count length-n self-avoiding walks from the root of an infinite spherically symmetric tree. At level l, all vertices have b_l children. Partition the levels into successive blocks of lengths L_j=2^(2^j), j=0,1,... . Give one child at every level in even blocks and two children in odd blocks. This is an infinite connected tree with maximum degree three.

Every self-avoiding root walk moves outward, so c_n(o)=product_{l<n} b_l. At the end N_j=sum_{h<=j} L_h, write B_j for the number of two-child levels among those N_j. Then log(c_{N_j}(o))/(N_j*log 2)=B_j/N_j. The earlier blocks have total at most j*L_{j-1}=j*sqrt(L_j), negligible relative to L_j. Along odd block ends this ratio tends to one; along even block ends it tends to zero. Since every ratio lies in [0,1],

    liminf c_n(o)^(1/n)=1,  limsup c_n(o)^(1/n)=2.

The exponential limit therefore does not exist even on an infinite connected bounded-degree graph. On the first three levels, c_1=c_2=1 but c_3=2, directly refuting scalar rooted submultiplicativity c_{n+m}(o)<=c_n(o)*c_m(o). This tree lacks the translation-stationary percolation structure of P0004 and is not a counterexample to that problem.

At the p=1 boundary on Z^2, translation invariance does supply scalar submultiplicativity: split a length-(n+m) walk after n steps. There are c_n prefixes; after translating the endpoint to zero there are at most c_m suffixes, since prefix avoidance only removes possible suffixes. Thus c_{n+m}<=c_n*c_m. Fekete's lemma gives lim_n log(c_n)/n=inf_n log(c_n)/n and existence of the connective constant. Monotone northeast walks give c_n>=2^n and no immediate backtracking gives c_n<=4*3^(n-1), so the constant lies in [2,3]. Translating the initial vertex preserves every c_n exactly.

The earlier attempt established root-independent limsup but did not obtain a stationary scalar subadditive process or a liminf bound. The tree explains why connectedness and bounded degree alone cannot fill that gap; the p=1 case isolates the translational mechanism that must be replaced in a percolation environment.

Checks: exact early-level tree counts; super-dominant block-end ratios without materializing gigantic trees; direct enumeration of short lattice walks and their submultiplicative inequalities. No tree counterexample is transferred into the iid lattice model.
