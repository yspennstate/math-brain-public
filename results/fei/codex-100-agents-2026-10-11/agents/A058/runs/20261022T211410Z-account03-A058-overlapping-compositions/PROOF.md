# Common-phase collision transport

All entropies use bits. All cubes are finite and uniform. Set E(x)=x^2 log2(1/x^2), E(0)=0. Define
Psi(a,b)=E((a+b)/2)+E((a-b)/2)-(E(a)+E(b))/2
and rho(a,b)=Psi(a,b)-(a-b)^2.

## 1. Exact coherent identity

Let X,Y,S,z be disjoint physical coordinate sets, z a fair selector, and G(X,S), H(Y,S) Boolean. Let a_T and b_T be their shared-only Fourier coefficients (the Fourier coefficients of their conditional private means). The physical mux F=(G+H)/2+z(G-H)/2 has shared-only amplitudes (a_T+b_T)/2 and (a_T-b_T)/2; these are coherent sums, not an incoherent branch mixture. Every coefficient involving X or Y is exclusive to one branch and splits into two selector sectors of half amplitude.

If A=sum a_T^2 and B=sum b_T^2, the exclusive coefficients contribute entropy increment 2-A-B relative to (H(G)+H(H))/2. The shared coefficients contribute sum_T Psi(a_T,b_T). Conditional independence on disjoint private blocks gives E(GH)=sum_T a_T b_T, hence Inf_z(F)=(1-sum_T a_T b_T)/2. Therefore, exactly,
H(F)=(H(G)+H(H))/2+4 Inf_z(F)+R(F),
R(F)=sum_T rho(a_T,b_T).

The exclusive Fourier label has a fair sector posterior: splitting one exclusive atom into two selector sectors contributes the entropy of that posterior. The common sector instead retains the signed amplitudes above. This is the collision ledger; a disjoint-block chain rule is not being assumed on S.

If E_X G(S)=E_Y H(S) for every S, then a=b and rho(a,a)=0. Thus R=0 and the selector price is exactly 4 Inf_z, including Inf_z=0. Equality of global biases alone is insufficient: G(S)=S,H(S)=-S gives zero entropy increment and Inf_z=1. Disjointness of private blocks is also used: G(X)=X,H(X)=-X has the same failure with empty S.

## 2. Arbitrary common shared phase

Take any Boolean u(S), and independent point indicators a(X),b(Y) of probabilities p,q. Each probability is 0, 1, or 2^(-r) for a positive integer r. Zero denotes a point activation already killed by a restriction. Define G=1+a(u-1), H=1+b(u-1). Let t=Pr(u=-1).

For T nonempty the shared coefficients are p uhat(T), q uhat(T). The empty coefficients are 1-2pt,1-2qt. Conservation of the two squared Hadamard amplitudes makes rho homogeneous:
rho(ca,cb)=c^2 rho(a,b).
The logarithm of c^2 cancels because the two sides have equal total mass; at c=0 the identity follows directly from E(0)=0. Parseval now gives the exact mean-only formula
R(t,p,q)=rho(1-2pt,1-2qt)+4t(1-t)rho(p,q).
No norm or degree assumption on u is used. In particular, its Fourier entropy does not enter this correction.

## 3. Scalar estimates and side conditions

On [-1,1], E is continuously differentiable, including at zero, and |E'|<=2/ln 2<3. For x>=0 this follows by maximizing 2x|2 ln x+1|/ln 2: on the negative-log branch the maximum is 4e^(-3/2)/ln 2, and at x=1 it is 2/ln 2. The first is smaller. The elementary bounds e>2 and ln 2>2/3 justify the strict relaxation to 3.

For a,b in [-1,1], the arguments (a+b)/2,(a-b)/2 also lie in that interval. Differentiating Psi in either variable gives absolute derivative at most 9/2. The derivative of (a-b)^2 is at most 4. Consequently rho is separately 9-Lipschitz throughout this square. In particular rho(p,p)=0 and |rho(p,q)|<=9|p-q|<=9(p+q) for p,q in [0,1].

Holding p,q fixed, the first part of R is 18(p+q)-Lipschitz in t, and the second is 36(p+q)-Lipschitz, since 4t(1-t) is 4-Lipschitz on [0,1]. Thus R is 54(p+q)-Lipschitz in t. Also R(0,p,q)=0.

## 4. Every physical query before selector revelation

A surviving private point-control query in X has children p'=0,2p, with p<=1/2. The shared mean t and q stay fixed. Changing p by p changes each empty coefficient by at most 2pt, so its rho charge changes by at most 18pt. The nonempty contribution changes by at most 9p*4t(1-t)<=36pt. Therefore
|R_parent-E R_child|<=54pt=54 Inf_x(F).
The same argument applies in Y. Resolved or dummy controls have zero change and zero influence.

For a shared coordinate i, child minority probabilities t_+,t_- have mean t. The same remaining shared assignment couples u_+ and u_-, so |t_+-t_-|<=Inf_i(u). Thus E|t_child-t|<=Inf_i(u)/2. The Lipschitz bound gives
|R_parent-E R_child|<=27(p+q)Inf_i(u)=54 Inf_i(F).
Here Inf_i(F)=(p+q)Inf_i(u)/2 is an exact physical identity. Nothing is divided by t, p, q or Inf_i.

These statements survive every adaptive data history: shared restrictions replace u by an arbitrary Boolean restriction; private point restrictions update p,q within the specified set. No previous constant or reserve is restarted.

## 5. Selector revelation and root closure

The selector influence is exactly t(p+q-2pq). Since R(0,p,q)=0,
|R(t,p,q)|<=54(p+q)t.
If p=q=1, R=0 identically. Otherwise admissible point probabilities satisfy p+q-2pq>=(p+q)/3: when both are at most 1/2, the stronger factor 1/2 holds; when one is 1, the other is at most 1/2. The zero p+q case is direct. Hence
|R|<=162 Inf_z(F).
Together with section 1 this gives
H(F)<=(H(G)+H(H))/2+166 Inf_z(F).
If both complete branches satisfy H<=C I, then
H(F)<=max(C,166) I(F),
using I(F)=(I(G)+I(H))/2+Inf_z(F).
This is a transfer theorem, not a proof of the inherited branch FEI bounds.

## 6. Exact stopped-tree ledger

Before selector revelation define K_v=(H(G_v)+H(H_v))/2; after revelation define K_v=H(selected core). At a data query, selector influence is a martingale, so the exact entropy decrement is Delta H_v=Delta K_v+R_v-E R_child. After revelation its coherent correction is zero. At selector revelation Delta K_v=0 and Delta H_v=4Inf_z+R_v.

For any finite adaptive physical restriction tree (arbitrary stopping leaves), with true reach weights w_v, telescoping gives
H(F)-E H(F_leaf)-sum_data w_v Delta K_v
 =sum_live_data w_v(R_v-E R_child)+sum_selector w_v(4Inf_z+R_v).
Thus the right side is at most 54 P_live_data+166 P_selector. Every physical query is charged once on its reached path. The consumed influence identity is
sum_all_internal w_v Inf_queried(F_v)=I(F)-E I(F_leaf).
Both child branches and every actual stopped terminal remain in the identity. No terminal entropy or unused child surplus is erased or renewed. The inherited Delta K terms are signed and must not be discarded.

At matching probabilities p=q, the first private query has a sharper price 12. On each nonempty shared row the child ratios are (0,1),(2,1); homogeneity gives expected correction kappa p^2 Var(u), kappa=4-(9/4)log2 3 in [0,1/2] (2^14<=3^9<=2^16). This part is at most pt. On the empty row the amplitudes differ by w=2pt<=1. The Psi Lipschitz constant 9/2 and the square w^2<=w give absolute expected correction at most (11/2)w=11pt. Together |E R_child|<=12 Inf_x(F).

## 7. Boundary, novelty scope, and unpaid step

The common-phase hypothesis is substantive. The two shared-only coefficient vectors are collinear off the empty mode, so their scale logarithms cancel. For unrelated u,v this collinearity fails, and replacing the full spectral sum by the mean-only formula is the first unsupported line.

This class has rare phases of unbounded hereditary Fourier l1 norm. For example, activate a bent phase on 4ell bits behind an ell-bit shared point indicator. Its minority probability tends to zero while the l1 contribution of nonempty bent frequencies is 2^(2ell)-2^(-2ell). The result does not assume a quadratic or minority gap, but retains the arbitrary inherited core entropies. It also does not authorize charging the same physical influence separately at multiple nested mux levels.

The shortest next step is a one-row perturbation away from the common phase: retain this exact collinear contribution and price only the noncollinear spectral remainder from one named unused inherited source. Keep the same old debits and both complete terminals. Full FEI is OPEN.

