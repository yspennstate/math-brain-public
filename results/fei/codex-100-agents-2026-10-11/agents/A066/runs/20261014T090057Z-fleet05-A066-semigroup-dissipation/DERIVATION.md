# A retained gate account and one variance reserve through mixed histories

Information quantities use bits; ln is natural logarithm. This stage changes from paying only lost quotient KL to paying the complete CONTROL-query row price. Arbitrary non-flat Boolean cores are allowed. Data-query entropy and actual terminal accounts are retained explicitly.

For clarity, for p_S=hat f(S)^2 define M_i(f)=sum_(T not containing i) p_(T+i) log2[(p_T+p_(T+i))/p_(T+i)], with zero summands interpreted continuously. The complete reference r_i(T)=p_T+p_(T+i) is normalized. If e_i>0, mu_i(T)=p_(T+i)/e_i and M_i=e_i[log2(1/e_i)-D(mu_i||r_i)]. If e_i=0 the price is zero. Ordinary influence is e_i=sum_T p_(T+i).

The physical restriction identity is Delta H=B_i+JS_i, where B_i=sum_T (p_T+p_(T+i)) h2(p_(T+i)/(p_T+p_(T+i))). Thus M_i<=B_i<=M_i+e_i/ln2, using -(1-x)ln(1-x)<=x. Also JS_i<=2e_i/ln2: the scalar natural-log Jensen-Shannon summand is at most (sqrt(x)-sqrt(y))^2/2; applied to the squared restriction Fourier amplitudes (u+v)^2,(u-v)^2, its sum is at most (1/2)sum_T(2v)^2=2e_i. These elementary bounds justify both the gate decrement in (3) and the complete entropy bound (6). Finally beta_i=E[q(z)z_i]=E[(q(z)-q(z^i))z_i/2] implies |beta_i|<=E_i; x ln(1/x)<=1/e for x in [0,1] proves the constant kappa used in (2).

## 1. Exact complete quotient price, without a flat-core hypothesis

Let b be any Boolean core on d>=0 data coordinates, s=b(0) in {-1,1}, and q any Boolean sign on a disjoint control cube. Put delta=2^-d and

F(y,z)=b(y)+1_{y=0}(q(z)-s).

For d=0 this is simply q. Write a=hat q(empty), beta_i=hat q({i}), E_i=Inf_i(q), e_i=Inf_i(F)=delta E_i. Control Fourier coefficients with nonempty control subset U are delta hat q(U); with U empty the coefficient is hat b(T)+delta(a-s). For control i, retain its complete residual control subset U while marginalizing the core index T. Parseval and sum_T hat b(T)=s give

C r_i(empty)=rho_i=1-delta+delta(a^2+beta_i^2),
C mu_i(empty)=beta_i^2/E_i,
C r_i(U)=delta[hat q(U)^2+hat q(U+i)^2], U nonempty,
C mu_i(U)=hat q(U+i)^2/E_i.

The quotient reference sums to one, including all derivative-free atoms. Its oriented price M_i^C satisfies

M_i(F)<=M_i^C
 =delta M_i(q)+delta beta_i^2 log2[rho_i/(delta(a^2+beta_i^2))]. (1)

The first inequality is exact KL data processing: M_i^C-M_i(F) is the lost influence-weighted conditional KL. If beta_i=0 the exceptional contribution is zero. Since rho_i<=1 and a^2+beta_i^2>=beta_i^2,

M_i(F)<=delta M_i(q)+delta d beta_i^2
                       +delta beta_i^2 log2(1/beta_i^2).       (2)

Booleanity supplies |beta_i|<=E_i, hence the last term is at most kappa e_i, kappa=2/(e ln2). No flatness, minimum coefficient or bounded quotient alphabet is assumed. Formula (1) is also valid at d=0; its surcharge then vanishes exactly.

## 2. One carried account for all physical mixed queries

At each actual reached node retain its representation with the surviving core, surviving gate and current delta. Define

G=delta H(q),
R=delta d Var(q)=delta d(1-a^2).

G is a retained, potentially unpaid gate-entropy account. R is a single variance reserve. It is not declared to be an unused certified child surplus merely because it has an influence upper bound.

A CONTROL query i has actual gate children q_+,q_-, with means a+beta_i and a-beta_i. Therefore

G-E G_child=delta[H(q)-E H(q_child)]>=delta M_i(q),
R-E R_child=delta d beta_i^2.                                  (3)

A DATA query j has one child continuing the point attachment with core b|y_j=0, same gate q, dimension d-1 and point mass 2delta. In the other child the edit disappears; represent its surviving core using a constant gate equal to its marked-point sign, so G=R=0 there. Consequently

G-E G_child=0,
R-E R_child=delta Var(q).                                      (4)

These identities hold for ANY physical ordering and adaptively chosen coordinate, including both nonconstant children, constant descendants and early stopping. No gate is reinitialized at a live-point child. Clean branches have no remaining gate debt. If d=0 no DATA query is possible.

Let a finite adaptive mixed stopping tree have reach weights w_v. Put

P_C=sum_(control nodes) w_v Inf_(i_v)(F_v),
D_R=sum_(data nodes) w_v delta_v Var(q_v).

Sum (2)-(4) with their actual physical weights. The full oriented control bill obeys

sum_C w_v M_i(F_v)
 <=G_root-E G_leaf + R_root-E R_leaf -D_R +kappa P_C.            (5)

Thus data-query reserve release D_R is NOT spent again on the control bill. It remains named capacity for the separate unpaid data-query/terminal obligation. Since B_i<=M_i+e_i/ln2 and channel JS_i<=2e_i/ln2,

sum_C w_v[H(F_v)-E H(F_child)]
 <=G_root-E G_leaf +R_root-E R_leaf-D_R
                    +[(3+2/e)/ln2]P_C.                        (6)

The left side contains only control nodes; no equality with the complete entropy drop is asserted. Actual data entropy drops and full leaf entropy remain. The same control-node heat bill is bounded after retaining its exact constant-Fourier boundary difference; the earlier K ledger is not substituted for full entropy without that boundary.

More explicitly, set B_C=sum_C w_v[b_empty(F_v)-E b_empty(F_child)] with b_empty=p_empty ln(1/p_empty) in nats, a signed boundary sum. Then 2sum_C w_v Delta K =ln2 sum_C w_v Delta H_bits-B_C. Multiplying (6) by ln2 and subtracting the SAME B_C gives the heat inequality. Finite endpoint integrability is unchanged. B_C is neither dropped nor counted as a newly paid positive cost.

Here K(f)=integral_0^infinity J_f(t)dt, J_f(t)=sum_(S nonempty)|S|p_S exp(-2t|S|)ln(1/p_S). For each finite cube J_f is bounded at zero by its finite value J_f(0) and decays at infinity at least as exp(-2t) times J_f(0). Termwise integration gives 2K=H_nat-b_empty exactly. This proves both endpoint integrability statements without suggesting a dimension-independent pointwise envelope for J_f/I(f).

This is a source/history payment of the COMPLETE control bill, rather than the smaller quotient remainder alone. A root-only renewal of R at every descendant would be false ownership. Equations (3)-(5) debit the same R once.

## 3. Actual availability, sharp obstruction, and first unsupported line

If a separately certified unused child/source account S has R_root<=S, one may book R_root ONCE, carrying the booked remainder as R_v rather than claiming a new S at descendants. G_root is still an explicit retained gate account. For a quadratic bent zero-point attachment, the actual rate-four averaged core-child surplus is at least d bits, so R_root<=delta times that same surplus; this special admission is valid but is not asserted for arbitrary cores.

A096's non-flat point fixture demonstrates why that admission is essential. For b_d=-1+2 1_0, c=-1 and q a one-bit character, R_root=d delta. The actual rate-four averaged child surplus S4<=5delta, so R_root>S4 for d>5, even though both children and the root satisfy FEI at rate four. At price five its actual child surplus S5>=d delta pays this specified loss/account. This is a scoped source-bound obstruction to availability, not an FEI counterexample. We do not repeat its search or count it as a newly discovered witness.

The FIRST UNSUPPORTED LINE is payment of the actual DATA-node entropy/heat/reference debit and complete physical leaf debt from D_R plus genuinely unused certified child surplus, together with admission of the root gate account G. Equations (5)-(6) supply a reusable control ledger, not this missing universal payment. NEXT must expose one actual non-flat data query with these same G,R and inherited terminal functions; renewing the bank or replacing available surplus by root influence capacity is ruled out.
