# Flat-carrier point edits: a carried bank through private collisions

Uniform independent physical bits; all entropy is in bits. This extends the existing A076 bundles, not a third general FEI candidate. Full FEI is OPEN.

## 1. Actual Boolean family and exact spectrum

Let k>=4 be even, epsilon=2^-k, b=2^(-k/2), and
H(s)=(-1)^(s_1 s_2+...+s_(k-1)s_k). For ANY Boolean V(x) on a disjoint cube, put

    F(s,x)=H(s)[1+1{s=0}(V(x)-1)], mu=E V.

H(0)=H(e_i)=1, every H Fourier coefficient h_S is +/-b, and the numbers of positive/negative coefficients are n_+=(2^k+2^(k/2))/2 and n_-=(2^k-2^(k/2))/2. The last count follows from sum_S h_S=H(0)=1. Direct transformation gives

    Fhat(S,empty)=h_S-epsilon(1-mu),
    Fhat(S,T)=epsilon Vhat(T), T nonempty.                  (1)

No input entropy certificate is assumed here. Parseval is exact. Private influences are epsilon Inf_i(V). Shared coordinate influences are 1/2+epsilon(1-mu): only the edge incident to zero changes, and it was originally nonpivotal. Thus

    I(F)=k/2+k epsilon(1-mu)+epsilon I(V).                  (2)

With phi(u)=u log2(1/u), define ell(v)=v^2 log2(v^2), t=b(1-mu),

    L_k(mu)=[(1+b)ell(1-t)+(1-b)ell(1+t)]/2,
    J_k(mu)=-L_k(mu)-epsilon phi(mu^2),
    R_k(mu)=k epsilon(1-mu^2).

Separating the T=empty rows of (1) from ALL nonempty T gives

    H(F)=epsilon H(V)+k+R_k(mu)+J_k(mu).                   (3)

In detail the empty rows have total mass 1-epsilon(1-mu^2) and entropy k[1-epsilon(1-mu^2)]-L_k(mu); nonempty rows have entropy epsilon[H(V)-phi(mu^2)]+2k epsilon(1-mu^2). This verifies both the factor 2k and its partial cancellation. Constants V=+/-1 are included. Every F is nonconstant for k>=4: changing at most one s vertex cannot turn a bent H into a constant.

## 2. A dimension independent signed profile estimate

For mu in [-1,1], 0<=t<=1/2 and 1/2<=1+/-t<=3/2. Since 2/3<=ln2<=1 and ln(3/2)<=1/2,

    0<ell''(v)=(4 ln v+6)/ln2<=12,
    |ell'(1)|=2/ln2<=3.

Write L'_k=b[(ell'(1-t)-ell'(1+t))/2+b(ell'(1-t)+ell'(1+t))/2]. The mean value theorem bounds its absolute value by

    12bt+b^2(3+12t)<=33 epsilon.

Also |d phi(mu^2)/dmu|<= (2/ln2)(|mu|+2|mu ln|mu||)<=6, using |mu ln|mu||<=1/e<=1/2. The derivative at mu=0 is its continuous limit. Therefore

    |J'_k(mu)|<=39 epsilon<=40 epsilon,
    J_k(1)=0, |J_k(mu)|<=80 epsilon.                     (4)

These are analytic inequalities for every real mu in [-1,1]; the finite checker is supplementary, not a continuum extrapolation.

## 3. Actual private-query transaction and one original bank

At any physical x-query i let a=Vhat({i}), d=Inf_i(V), mu_0=mu+a, mu_1=mu-a. Equation (3) yields the EXACT signed transaction

    Delta_i H(F)=epsilon Delta_i H(V)
                 +k epsilon a^2
                 +J_k(mu)-[J_k(mu_0)+J_k(mu_1)]/2.       (5)

The final signed term has absolute value <=40 epsilon |a|<=40 epsilon d. The middle term is EXACTLY the released part of the ONE bank R:

    R(parent)-average R(children)=k epsilon a^2>=0.       (6)

This bank is the specialization of A028 stage5's boundary reserve, not a newly independent reserve: take data branches H and H[1-2*1{s=0}], controller c=(1-V)/2. Their product is the k-bit point defect of influence 2k epsilon, so A028's 2p(1-p)I(product) is precisely R_k(mu). The local signed entropy price (5), beyond bank conservation alone, is the new flat-carrier calculation here.

For ANY adaptive stopping tree querying only x-coordinates (including an original mux selector if it belongs to x), let P be actual consumed private influence, Pi_H(V)=H(V)-E H(V_leaf), and w the physical reach probabilities. Then

    H(F)-E H(F_leaf)
      =epsilon Pi_H(V)+R(root)-E R(leaf)
                         +J_k(mu_root)-E J_k(mu_leaf),
    |J_k(mu_root)-E J_k(mu_leaf)|<=40 P,
    sum_v w_v k epsilon a_v^2+E R(leaf)=R(root).          (7)

Every terminal F and V spectrum remains. Influence satisfies P=epsilon[I(V)-E I(V_leaf)], and shared influence is harmonic because (2) is affine in mu. If erasures rather than full entropy decrements are desired, B_T(F)<=epsilon B_T(V)+43 P+R(root)-E R(leaf), using JS_T(V)<=(2/ln2)Pi_I(V)<3Pi_I(V) and JS_T(F)>=0. This retains the inherited input erasure; it does not bound it for arbitrary V.

For a supplied input certificate H(V)<=C0 I(V), C=max(C0,5) gives H(F)<=C I(F). Indeed (3)-(4) give H(F)<=epsilon C I(V)+k+epsilon(k+80), while epsilon(k+80)<=21k/16<3k/2 for k>=4. Thus the existing flat-carrier surplus (C/2-1)k pays the profile once. No independent copy of the carrier slack is assigned at descendants.

An exact SIGNED surplus formula, useful with supplied child certificates, is

    C I(F)-H(F)=epsilon[C I(V)-H(V)]+U_C(mu),
    U_C(mu)=(C/2-1)k+Ck epsilon(1-mu)-R_k(mu)-J_k(mu).
                                                               (8)

For C>=5, U_C>=3k/16. Negative input child surplus is never clipped. Under a stopped tree use the SAME incoming formula (8) with the signed inherited input costs in (7), rather than renewing U_C or R at each node. The literal child-deficit identity remains S_C(F)=E S_C(F_child)+C Inf_i(F)-Delta_i H(F).

## 4. Second private collision with both cores nonconstant

Let m>=2, G(s,x)=H(s)[1-2*1{s=0,x=0}], and select G if z=0 and H if z=1. This is (1) with V(x,z)=1-2*1{x=0,z=0}. Query x_1,x_2,...,x_m, stopping a branch as soon as x_j=1, and leave z AND all s unqueried. Every actual terminal mux and each of its two branch cores is nonconstant. In particular the first zero child contains a genuine second private collision, not the point-defect-to-constant exit paid by A077's geometric mark.

At reached depth j, mu_j=1-2^{-(m-j)}, d_j=2^{-(m-j)}, reach weight 2^-j, and the two private means are mu_j+/-d_j. Put delta=Inf_z(F)=epsilon 2^-m. The mismatch is supported only on the surviving child, hence its expected mass is UNCHANGED at every private query. A selector-disagreement reserve has zero release here.

Nevertheless the same R pays the signed residual (5) at every query, with

    P_private=m epsilon 2^-m,
    R_root=k epsilon(2^(1-m)-2^(-2m)),
    E R_leaf=k epsilon 2^-m,
    total R_release=k epsilon(2^-m-2^(-2m)).              (9)

At m=2, the first release is k epsilon/16, the SECOND weighted release k epsilon/8, total 3k epsilon/16, and P_private=epsilon/2. Both complete terminal spectra and the actual inherited quarter-core B_i(G)/4 are recorded by the checker. That quarter is an unpaid inherited cost in the general admission formulation; the present proof transports its information via the exact V entropy term, not by declaring it zero. The original selector remains unqueried and no bank is renewed.

Two literal private queries can also have zero first release and nonzero second release (V=x_1 x_2): first conditional means stay zero, second means become +/-1. This proves why retaining unused R matters. With V a single literal, R_release/Inf_private(F)=k; both F children are nonconstant. Hence a dimension independent price for the residual of (5) CANNOT simply discard R: |Jdrop|<=40 epsilon implies (Delta H(F)-epsilon Delta H(V))/Inf_private(F)>=k-40. These functions have a supplied trivial input certificate and bounded full H/I; this is an ownership obstruction, not an FEI disproof.

## 5. Extension through a shared query: flat nonzero rows with zeros

The next physical query can be handled without opening a new root bank. More generally let H on d shared bits have exactly M=2^q nonzero Fourier coefficients, each of magnitude b=2^(-q/2), with 0<=q<=d even, H(0)=1, epsilon=2^-d. Assume alpha=epsilon/b<=1/4. Its nonzero support need not be an affine subspace. Form the SAME phase-point F with arbitrary private V. Set w=M epsilon and rho=1-mu. The spectrum (1) still holds; outside the old H support, the private-empty coefficient is -epsilon rho. There are (M+sqrt(M))/2 positive old coefficients. With t=alpha rho, define L by the same weighted ell expression as above, now with this b,t, and

    K(mu)=epsilon[2(d-q)rho+(d-(2d-q)w)rho^2],
    J(mu)=-L+epsilon(1-w)phi(rho^2)-epsilon phi(mu^2),
    R(mu)=d epsilon(1-mu^2).

Counting ALL zero and nonzero old rows gives the exact formula

    H(F)=epsilon H(V)+q+R(mu)+K(mu)+J(mu).                (10)

For verification, the non-profile polynomial before extracting R,K is epsilon(2d-q)[2rho-w rho^2]. The coefficient d-(2d-q)w is nonnegative: for c=d-q, (d+c)2^-c<=d, using 2^c>=1+c>=1+c/d. Hence K is convex in mu and

    K(mu)-average K(mu+/-a)
       =-epsilon[d-(2d-q)w]a^2<=0.                     (11)

The previous derivative estimate for L still gives 33epsilon: now alpha^2=epsilon w<=epsilon and alpha b=epsilon. On rho in[0,2], |d phi(rho^2)/drho|<=18, since ln2>=2/3 and |rho ln rho|<=2. Thus |J'|<=57epsilon<60epsilon, J(1)=0, and |J|<=120epsilon. Consequently at every physical private query

    Delta H(F)<=epsilon Delta H(V)+release_R
                                      +60 Inf_private(F).     (12)

The SAME R is A028's original boundary reserve. Formula(10) and the signed negative drift(11) preserve the old zero rows rather than deleting them. The stopped-tree form retains epsilon Pi_H(V), E H(F_leaf), E R_leaf and the summed SIGNED K,J changes. For B_T the safe corresponding price is63. These are local signed prices in addition to A028's previously proved reserve conservation.

Here is an actual mixed history inside section4, not an independent new source. Start at k=6 and m=3. Query x_1, then x_2 on the surviving zero history; query s_1 next with ALL siblings retained, then query x_3 wherever still relevant, leaving z unqueried. Before s_1 the original carrier has all flat rows. On s_1=0 the carrier on the remaining five coordinates has q=4 flat nonzero rows and a dummy partner s_2; M epsilon=1/2 and alpha=1/8, so (10)-(12) apply. On s_1=1 the phase point has died, so the actual child is the unedited quadratic carrier times the literal s_2. Both children and both original mux branch cores remain nonconstant. The relevant shared query has Inf>=1/2-2epsilon>=3/8. Since B<=1 and JS<=3Inf, its full entropy bill is at most6Inf. Its boundary-bank release, NOT automatically spent on this physical price, is

    R_parent-E R_children=2p(1-p)Inf_(s_1)(D_6)
                             =epsilon(1-mu^2).          (13)

This is A028's data release for the same point-product bank; the zero child has conditional R=5*(2epsilon)*(1-mu^2), the other child R=0. Taking physical probabilities, the old bank plus releases and terminal bank telescope exactly through private/shared/private exposure. There is no second selector account.

Certified signed surplus is also explicit after the zero shared answer. Its base carrier has H=4,I=2, and all five H(e_i)=1. Thus I(F)=2+5epsilon(1-mu)+epsilon I(V). At d=5,q=4, R<=5epsilon, K<=12epsilon and |J|<=120epsilon. For C>=5,

    C I(F)-H(F)=epsilon[C I(V)-H(V)]
        +(2C-4)+5Cepsilon(1-mu)-R-K-J,

whose final carrier allowance is >=6-137/32=55/32. It is the physically restricted original child surplus with all previous releases booked, not a new source. The unchanged other shared answer has its complete quadratic/literal entropy and influence retained. Point inputs V have the supplied certificate H(V)<=4I(V): for a point defect on n>=2 bits put a=2^(1-n), use phi((1-a)^2)<=2a/ln2 and H=phi((1-a)^2)+2(n-1)(2a-a^2)<=4na. Characters/constants cover n<=1.

## 6. First unsupported universal line

This stage therefore reaches one actual shared query followed by another private collision with the SAME original bank and nonconstant terminals, including the new Fourier-zero rows. The unsupported line is extending (12) to arbitrary UNEQUAL nonzero carrier row heights after further general core restrictions, with the complete inherited input entropy and signed source surplus kept. Arbitrary V still retains its entire epsilon H(V) bill: a certificate for every V would itself resolve FEI. A028 bank conservation alone does not pay that bill or the actual signed mixed-query excess. NEXT is the first unequal-height carrier, using the already booked private/shared/private ledger rather than a new root certificate. No dimension independent arbitrary-core induction is claimed.
