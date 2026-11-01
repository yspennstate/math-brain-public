# Arbitrary-gate informative quotient with an owned control debit

Natural logarithms in this derivation. All functions are actual Boolean signs on finite uniform cubes. This is a narrow extension of the conditional-row interface, not a universal FEI payment. The fixed bent-core hypothesis is retained explicitly.

## 1. General Boolean gate and its actual signed row

Let d>=4 be even, delta=2^-d, t=sqrt(delta), and b(y)=(-1)^(sum_j y_(2j-1)y_(2j)) on d bits. Its Fourier coefficients are sigma_T t with sigma_T=+/-1 and sign counts N_+=(2^d+2^(d/2))/2, N_-=(2^d-2^(d/2))/2. Let q(z) be ANY Boolean sign on r>=1 fresh control bits. Set

F(z,y)=b(y)+1_{y=0}(q(z)-1).

This is Boolean, with arbitrary gate q at the distinguished bent-core vertex. Write a=hat q(empty), alpha=1-a in [0,2], beta_i=hat q({i}), e_i=Inf_i(q). Its Fourier amplitudes for control set U and core set T are

hat F(empty,T)=sigma_T t-delta alpha,
hat F(U,T)=delta hat q(U), U nonempty.                         (1)

For a relevant control i, Inf_i(F)=delta e_i by direct physical flips. For each residual control set U not containing i, the actual complete residual reference and derivative laws are r_i(U,T)=p_(U,T)+p_(U+i,T) and mu_i(U,T)=p_(U+i,T)/(delta e_i). They normalize to one; reference atoms outside derivative support are not removed.

Retain ALL residual control occupancies U and discard only the core Fourier set T. For U nonempty, the two core conditional laws are exactly uniform, so this cell loses zero KL even when both endpoints and erasure are positive. Only U=empty has a nonflat reference:

c_sigma=1-2alpha sigma t+delta(alpha^2+beta_i^2),
R_i=1+delta(a^2+beta_i^2-1),
r_i(empty,T)=delta c_sigma,
C mu_i(empty)=beta_i^2/e_i,
C r_i(empty)=R_i.                                               (2)

The remaining quotient cells have C mu_i(U)=hat q(U+i)^2/e_i and C r_i(U)=delta[hat q(U)^2+hat q(U+i)^2]. The reference still has total mass exactly one. Since |a|<=1 and a^2+beta_i^2<=1, 1-delta<=R_i<=1.

If beta_i=0, the exceptional cell has zero derivative probability and total loss is zero. Otherwise the conditional derivative core law in this cell is uniform (mass delta per set), while the reference is delta c_sigma/R_i. Define

D0_i=sum_sigma [(1+sigma t)/2] ln(R_i/c_sigma).

Exact KL chain rule gives the influence-weighted lost refund

L_i=delta beta_i^2 D0_i>=0.                                    (3)

No control cell is merged with another and no data-dependent likelihood ratio is discarded without this debit. This extends the A073/A100 two-control gate to arbitrary gate dimension and arbitrary gate spectrum, while retaining a flat signed bent core.

## 2. Uniform quadratic remainder paid by one physical control ledger

Let A_i=1+delta(alpha^2+beta_i^2). Jensen's inequality using the actual unequal sign weights gives

D0_i <= ln[ R_i sum_sigma (1+sigma t)/(2c_sigma)]
      = ln[1+4alpha^2 delta(1-delta)/(A_i^2-4alpha^2 delta)].      (4)

For delta<=1/16 and alpha<=2, the denominator is at least (1-alpha^2 delta)^2>0, hence at least 9/16. Using ln(1+x)<=x yields

0<=D0_i<=(256/9)delta,
L_i<=(256/9)delta^2 beta_i^2,
sum_i L_i<=(256/9)delta^2 W1(q)
          <=(256/9)delta^2 I(q)
          =(256/9)delta I_controls(F).                          (5)

Here W1(q)=sum_i beta_i^2<=I(q) by the actual spectral influence identity. This is one combined debit, not a separate core fraction reused for every control row. If another argument already assigns K I_controls to the rest of the ledger, its combined upper coefficient becomes K+(256/9)delta; the same influence is not declared fresh. At d=4 the extra rate is <=16/9, and it tends to zero as d grows, uniformly in r and q.

The d=2 regime is explicitly excluded from this proof; alpha may approach 2, making the denominator degenerate. The earlier specific A073/A100 gate theorem still covers its own d=2 case. No arbitrary-gate d=2 result is inferred here.

Every physical control restriction replaces q by its actual Boolean restriction and leaves the same bent core and delta. Thus the result is hereditary under control-only queries. At a node querying i, (5) gives L_i<=(256/9)delta Inf_i(F_node), since beta_i^2<=e_i. In every finite adaptive CONTROL-ONLY singleton stopping tree, including early stopping,

sum_nodes w_v L_(i_v)(F_v)
 <=(256/9)delta[I_controls(F_root)-E_leaf I_controls(F_leaf)]
 =(256/9)delta[I(F_root)-E_leaf I(F_leaf)].                       (5a)

The first equality is the ordinary physical influence telescope; the core influence has the same weighted average at every control restriction because it is affine in the actual gate mean. Every removed control influence is charged once. Leaves retain their full q_leaf, core entropy and K. This statement does NOT cover a data/core query that changes the flat signed core. Extending it to such a query requires a new retained reference and reserve, which is the next mechanism rather than an unstated hereditary assumption.

## 3. The retained row and terminal costs are still explicit

Let M_i(F)=sum_(U,T) p_(U+i,T)ln(r_i(U,T)/p_(U+i,T)). The quotient price satisfies exactly M_i^C=M_i(F)+L_i. From (2),

M_i^C=delta sum_(U nonempty) hat q(U+i)^2
                       ln[(hat q(U)^2+hat q(U+i)^2)/hat q(U+i)^2]
       +delta beta_i^2 ln[R_i/(delta beta_i^2)].                 (6)

The logarithmic root term and the full arbitrary gate's retained oriented bill have NOT been paid by (5). For q the two-bit negative-AND gate, (6) reduces to the already reviewed A073 growing selected-row price. A bounded discarded remainder is not a bounded complete entropy drop.

Physical influences are

I_controls(F)=delta I(q),
Inf_(y_j)(F)=1/2+delta(1-a),
I(F)=d/2+d delta(1-a)+delta I(q).                                (7)

The second formula follows because the bent sign and each of its neighbors are +1 at the edited vertex, and the gate differs there on fraction (1-a)/2 of control assignments. Revealing ALL controls stops at physical core leaves b or b-2 1_{y=0}, with weights (1+a)/2 and (1-a)/2. Their full heat functional K and entropy remain in any stopping ledger. Revealing the core instead leaves q at y=0 with weight delta, so that arbitrary terminal gate is not free either.

The previous exact heat telescope 2(K(root)-E K(leaf))=sum(M_i^++C_i^++ell_i) and singleton price beta=2+2/e^2 remain at their stated scope. The new debit (5) is only the KL information lost by the specified quotient; it is not substituted for heat erasure, the complete retained price (6), or leaf entropy. The FIRST UNSUPPORTED LINE for full FEI is a universal payment of those retained rows and actual terminal costs from one available signed child/influence reserve.

## 3a. First core exposure: retain the newly informative Fourier flag

For an original even d>=6, physically query the first core bit y1. On y1=1 the edit disappears and the child is the clean character y2 times a quadratic bent sign on d-2 bits. Its control influence is zero. On y1=0 the child is

G(z,w,Y)=b_(d-2)(Y)+1_{w=0,Y=0}(q(z)-1), w=y2.

Let delta0=2^(-(d-2)) and theta=1/2, so its point mass is delta_p=theta delta0. The base bent sign is independent of w. Retain residual control U AND Fourier occupancy W of w, discarding only the remaining bent Fourier index T. All cells except (U=empty,W=0) have uniform conditional core laws and lose zero KL. In that exceptional cell equations (2)-(4) apply with delta0 and scaled parameters alpha'=theta alpha, beta'=theta beta_i. Consequently

L_i(G)=delta0 theta^2 beta_i^2 D0_i',
D0_i'<=(256/9)theta^2 delta0,
sum_i L_i(G)<=(256/9)theta^4 delta0^2 W1(q)
 <=(256/9)theta^2 delta_p I_controls(G).                         (8)

This is a paid first-core-exposure extension with the SAME complete reference, refined by the explicit surviving flag. It is hereditary under further control-only restrictions, with cumulative loss bounded by (256/9)theta^2 delta_p times their removed physical influence. It does not cover further arbitrary core exposure, overlapping edits, or a free code for the retained flag. Full terminal/core and retained quotient-row prices remain explicit.

Keeping that flag is necessary for this small-loss conclusion. For q the two-bit negative-AND gate, condition the reference and derivative on residual U=empty. The derivative W law is (1/2,1/2), while the reference W=1 probability is epsilon=(delta0/8)/(1-delta0/4). Erasing W in addition to T loses an EXTRA weighted KL

Delta L=delta_p beta_i^2 D(Ber(1/2)||Ber(epsilon)),
Delta L/Inf_i(G)=(1/2)D(Ber(1/2)||Ber(epsilon))
 >=(1/4)ln[7/(4delta0)]                                         (9)

because epsilon<=delta0/7 when delta0<=1/16, and D(Ber(1/2)||Ber(epsilon))=(1/2)ln[1/(4epsilon(1-epsilon))]. Thus the old partition discarding every core bit has unbounded local loss after just ONE physical data query, despite (8) for the flag-retaining partition. This is a source/history correction, not a FEI counterexample. NEXT must preserve or explicitly pay these new informative flags and the terminal reference when departing from the control-only tree, rather than reuse the original partition unchanged.

## 4. Independent A100 Jensen review

Specialize to the gate negative only at (1,1): a=beta_u=beta_v=1/2, alpha=1/2, e_u=e_v=1/2. Equations (2)-(4) give the original family R_i=1-delta/2, D_full=D_binary+D0/2 and L_i=(delta/4)D0. The Jensen expression is exactly R(delta)=(1+delta-3delta^2/4)/(1+delta^2/4). Its derivative numerator 1-2delta-delta^2/4 is positive on (0,1/4], so R<=77/65. The integer inequality 77^4<2*65^4 gives log2(R)/2<1/8. Also R<1+delta, ln(1+delta)<delta, so the pair loss is <delta^2/(2 ln2) bits, and <delta/8<=Inf_(y1)/20. An independent spectator law multiplies both conditional laws by the same factor, canceling exactly. Thus A100-BINARY-REMAINDER-JENSEN-BOUND v1 HOLDS at full stated scope, without repair. Its dedicated fraction covers these two remainders only. The arbitrary-gate extension above is a separate author result, not a repair supplied to A100.
