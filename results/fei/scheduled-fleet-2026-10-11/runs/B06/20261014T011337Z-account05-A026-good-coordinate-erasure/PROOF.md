# Sharp signed-row transfer to an actual uniform Boolean shadow

All entropies are bits and Phi(s,t)=(s+t)log2(s+t)-s log2 s-t log2 t. All cubes are uniform physical cubes. Define kappa=log2(32/27)=5-3log2(3).

## 1. A sharp continuous scalar inequality

For all real a,b,c,

 Phi((a+b)^2,c^2)-Phi(a^2,c^2)-Phi(b^2,c^2)<=kappa c^2.       (1)

The constant is sharp, with equality when a=b=c/sqrt(8), including simultaneous sign reversal. If c=0 every term is zero. Otherwise scale by c^2 and use natural logarithms temporarily. Set L(x)=Phi_nat(x^2,1) for x>=0. Opposite signs of a,b give |a+b|<=max(|a|,|b|); monotonicity of L makes the excess nonpositive. It suffices to maximize K(x,y)=L(x+y)-L(x)-L(y) on x,y>=0.

L'(x)=2x ln(1+x^-2), L''(x)=2ln(1+x^-2)-4/(1+x^2), and L'(0)=0 by continuity. With v=1/(1+x^2), L''/2=-ln(1-v)-2v. This expression is decreasing on (0,1/2), increasing on (1/2,1), is negative at 1/2 and tends to infinity at 1. Thus L' strictly increases to one maximum and then strictly decreases.

K vanishes on the axes. Its limsup at infinity is at most zero: order x>=y, use L'(t)<=2/t to get L(x+y)-L(x)<=2ln(1+y/x)<=2ln2. If y tends to infinity this is dominated by L(y)->infinity. If y stays bounded the difference tends to zero; subsequences with y tending to zero also have nonpositive limiting excess. A positive maximum therefore occurs in the interior. At an interior stationary point L'(x+y)=L'(x)=L'(y). Neither x nor y can be at or beyond the turning point, because x+y is larger and the decreasing branch would contradict equality. On the increasing branch equality forces x=y.

Put u=x^2. Along the diagonal K=Phi_nat(4u,1)-2Phi_nat(u,1). Its derivative is 4ln(1+1/(4u))-2ln(1+1/u), positive for u<1/8 and negative for u>1/8: the ratio inside the logarithm differs from one with the sign of 1-8u. Hence the global maximum is at u=1/8, where its exact value is ln(32/27). Division by ln2 proves (1) and sharpness. No finite grid or floating optimizer establishes this continuum result.

## 2. General biased encoder, arbitrary actual Boolean rest

Let f(z,r) be an arbitrary Boolean sign, z a fresh uniform sign, r arbitrary other uniform physical inputs. Write f=A+zD, with AD=0 and A^2+D^2=1 pointwise. Let delta=E D^2=I_z(f). Substitute any Boolean encoder h(x) on a disjoint fresh physical block: F=A+hD. Put mu=E h, gamma=hhat({i}), d=I_i(h). The exact A056/A057/A026 interface gives

 I_i(F)=delta d,
 B_i(F)=delta[B_i(h)-Phi(mu^2,gamma^2)]
             +sum_T Phi((Ahat(T)+mu Dhat(T))^2,gamma^2 Dhat(T)^2). (2)

This existing identity is consumed, not advertised as new. Apply (1) separately with a=Ahat(T), b=mu Dhat(T), c=gamma Dhat(T). Homogeneity gives sum Phi(mu^2 Dhat(T)^2,gamma^2 Dhat(T)^2)=delta Phi(mu^2,gamma^2). Therefore the signed empty-row subtraction cancels exactly, and

 B_i(F)<=delta B_i(h)+sum_T Phi(Ahat(T)^2,gamma^2 Dhat(T)^2)
                         +kappa delta gamma^2.                 (3)

For mu=0 the signed correction is exactly zero, so the last term can be omitted. Formula (3) holds after arbitrary physical histories inside and outside the encoder, provided A,D,h denote their actual current restrictions. The shadow f(z,r) is Boolean because its two z slices are the actual outer functions A+/-D. Its fresh z is an auxiliary mathematical variable, not an unqueried physical bit of F.

For 0<=t<=1, concavity of binary entropy gives

 Phi(a,tb)<=t Phi(a,b)+t b log2(1/t).                           (4)

For a,b>0 and 0<t<=1, define the difference as the right side minus the left side, using natural units. Its derivative in a is t ln(1+b/a)-ln(1+tb/a)<=0 by concavity of ln, and the difference tends to zero as a tends to infinity. Thus it is nonnegative. Zero endpoints follow by continuity. This proves (4) without assuming an external entropy-splitting theorem.

Apply (4) with t=gamma^2 and sum to obtain the new uniform-shadow transfer

 B_i(F)<=delta B_i(h)+gamma^2 B_z(f)
                      +delta gamma^2[log2(1/gamma^2)+kappa].    (5)

Zero terms are interpreted continuously. If delta=0 or d=0 the queried coordinate is irrelevant and both actual erasure and these terms vanish. If gamma=0 then B_i(F)=delta B_i(h) exactly.

The coefficient domination |gamma|<=d follows by averaging the Boolean derivative D_i h in {-1,0,1}. For 0<=u<=1, u ln(1/u^2)<=2/e, and gamma^2<=d. Consequently the remainder in (5) is at most

 C0 I_i(F), C0=kappa+2/(e ln2).                               (6)

A sharper scalar bound is 2 sqrt(32/27)/(e ln2), obtained by maximizing u[log2(1/u^2)+kappa], but no optimal Boolean-transfer price is asserted. Formula (5), including its exact signed ancestry, is the primary result.

## 3. One physical influence account on a represented stopping tree

At every represented actual node v of any adaptive physical stopping tree, choose a fresh disjoint encoder representation F_v=A_v+h_v D_v, with its actual restricted Boolean shadow f_v(z,r)=A_v+zD_v. Define

 E_inner=sum_v w_v delta_v B_(i_v)(h_v),
 Q_shadow=sum_v w_v gamma_v^2 B_z(f_v),
 S=sum_v w_v I_(i_v)(F_v).

Over all represented nodes (or over the entire tree if every node is represented), (5)-(6) give

 sum_v w_v B_(i_v)(F_v)<=E_inner+Q_shadow+C0 S.                (7)

Each error term is charged to that node's physical query once. S<=I(root)-E I(leaf) when other nodes are omitted; equality holds when all queried nodes are represented. If every node is represented, the exact entropy decrement Delta_i H=B_i+J_i with J_i<=(2/ln2)I_i gives

 H(root)<=E H(leaf)+E_inner+Q_shadow+(C0+2/ln2)S.              (8)

No leaf entropy or inherited inner erasure is suppressed. A003's once-sliced-majority bound, independently accepted at abstract scope by A004, pays E_inner at once-sliced majority nodes by 2 times their physical influence. Thus arbitrary outer derivative rarity is now contained in the actual Boolean-shadow charges Q_shadow rather than a local log(1/delta) estimate. This does not yet pay Q_shadow.

## 4. Exact first unsupported line and a shadow ownership warning

The unsupported universal step is Q_shadow+E_inner+E H(leaf)<=K times one remaining physical influence budget for a universally valid policy. The shadow is an actual Boolean function but its z is fresh and auxiliary: a physical query inside h is not a physical query of shadow z. Along encoder-only queries, f(z,r) can stay unchanged, so its Fourier entropy cannot be treated as a decreasing reserve paying every Q_shadow charge.

An exact ownership control is f(z,r)=AND2(z,r) in sign form, h=AND2(x1,x2), F=AND3. A complete x1-then-x2 encoder tree has positive shadow charges despite the same f(z,r) at each nonconstant encoder node. Gamma^2 B_z(f) is 1/4 at the root and 1 at the active child reached with probability 1/2, for total Q_shadow=3/4. The uniform shadow entropy is constantly 2 bits at those nodes. Actual encoder output is + with probability 1/4, not the shadow's uniform 1/2. After resolving the encoder, actual terminal core entropy is zero; shadow entropy remains an auxiliary quantity and is not a physical entropy telescope. This control refutes only naive unchanged-shadow entropy-decrement ownership, not a possible source-owned reserve or FEI.

## 5. Exact variance ownership on encoder-only prefixes

Fix an arbitrary outer shadow f(z,r) and query only physical coordinates inside its encoder h. The shadow remains fixed, but the actual restricted encoder changes. At a query with current mean mu and singleton gamma, the two physical child means are mu+gamma and mu-gamma, possibly interchanged by the sign convention. Therefore

 Var(h)-[Var(h_+)+Var(h_-)]/2=gamma^2.

On any adaptive encoder-only prefix, with actual fair physical reach probabilities,

 Q_shadow=B_z(f)[Var(h_root)-E Var(h_leaf)].                  (9)

This is an exact ownership identity: each variance decrement is charged once. The actual spent influence is separately delta[I(h_root)-E I(h_leaf)]. For a complete encoder tree, Q_shadow=B_z(f)Var(h_root), independent of every query-order choice. This does not assert that shadow variance has a dimension-independent influence price weighted by B_z(f).

The no-go for paying this nonnegative bank from encoder influence alone is genuine and all-dimensional. For even k>=4 take the standard quadratic bent sign g_k on k bits, equal to +1 at the origin, and g'_k obtained by flipping that one value. Let f_k(z,r) have z slices g_k,g'_k. Put delta=2^-k,s=sqrt(delta). Then D is a signed origin indicator, I_z(f_k)=delta, and all A coefficients have the form +/-s-delta. Hence each packet in B_z(f_k) obeys

 Phi((+/-s-delta)^2,delta^2)>=delta^2 log2((s-delta)^2/delta^2)>=delta^2(k-1),

since (1-s)^2>=9/16>1/2. There are 2^k packets, so B_z(f_k)>=delta(k-1). The bent spectrum follows directly from tensoring the two-bit quadratic sign, whose four coefficients have magnitude 1/2; this is an explicit Boolean family, not a real coefficient relaxation.

Use a fixed balanced Maj3 encoder, Var(h)=1,I(h)=3/2. On EVERY complete encoder-only query policy,

 Q_shadow/[spent encoder influence]>=2(k-1)/3 -> infinity.   (10)

Thus no finite K pays this entire nonnegative uniform-shadow bank using encoder influence alone. This is a route/ownership obstruction, not an FEI counterexample: the many physical outer data inputs remain available and their influence budget is excluded by this false proposed payment. It also does not prove actual erasure equals Q_shadow, since the signed and inherited terms are retained in (2). Completing the same encoder in every block is not a universally justified good-coordinate selection rule.

NEXT is to couple the shadow charge to queries of actual outer data under one terminal-inclusive reserve, or use a normalized terminal reference owning that variance-weighted shadow bill. The scalar signed bias conversion is now paid and its encoder-only ownership has been identified exactly; reopening it or adding another majority slice would leave precisely the unpaid outer-data transfer unchanged.
