# Cancellation-aware repair of the single-event bank

All cubes are finite and uniform; shared x and private y are independent. Entropies are in bits, including the empty coefficient. This repairs the raw-mask majorant in A076 stage11, rather than supplying a new arbitrary-core source. Independent review is pending.

## 1. Exact bank and activation factor

Let a(x) be a zero-one indicator, p=E a, V(y) Boolean, mu=E V, q=1-mu, v=1-mu^2, and F=1+a(V-1). Write phi(t)=-t log2(t), phi(0)=0, even when t>1, and J(a)=sum_S phi(ahat(S)^2). Put D(a)=sum_S |S| ahat(S)^2, U=p H(V), N=H(F)-U.

The joint coefficients are ahat(S)Vhat(T) for T nonempty; for T empty they are 1-pq at S empty and -q ahat(S) otherwise. The private marginal is p Vhat(T)^2 for T nonempty and 1-pv at T empty. It is the mixture p Spec(V)+(1-p) delta_empty. Thus N>=0 by entropy concavity and the joint Shannon chain rule; the full inherited U is retained.

Directly summing the coefficients, using v+q^2=2q, gives

N=2q J(a)+phi((1-pq)^2)-q^2 phi(p^2)
  -p(1-p)q^2 log2(q^2)-p phi(mu^2).                 (1)

The expression q^2 log2(q^2) is zero at q=0. The actual shared and private influence are

I_x(F)=2q D(a),  I_y(F)=p I(V).                     (2)

These are original physical influences, not an ambient carrier allowance. In particular q=0 gives F=1 and N=I_x=0 for every mask, repairing the stage11 constant-output obstruction exactly. The formulas hold at p=0,1 and q=0,2; no division by p,q,D occurs in (1)-(2).

## 2. Uniform elementary remainder bound

For all 0<=p<=1 and 0<=q<=2,

0<=N<=2q J(a)+5pq.                                (3)

Proof: phi(t)<=(1-t)/ln2 for t>=0 (at zero by continuity). With t=(1-pq)^2 this gives phi(t)<=2pq/ln2<3pq. The subtracted terms q^2 phi(p^2), p phi(mu^2) are nonnegative. If q>=1 the log term in (1) is nonpositive. If 0<q<1, q log2(1/q)<=1/(e ln2)<1, and hence -q^2 log2(q^2)<=2q. Its contribution is at most 2pq. The elementary constants use ln2>2/3, e>2, so 1/(e ln2)<1. This proves (3), including endpoints by continuity.

If 0<p<=1/2, Parseval gives D(a)>=sum_(S nonempty) ahat(S)^2=p(1-p)>=p/2. Therefore I_x>=pq. For any event certificate J(a)<=K D(a),

H(F)<=p H(V)+(K+5) I_x(F).                        (4)

No entropy bound on V was used. If an original account has already spent L, (4) requires its actual unused balance to cover (K+5)I_x; it does not renew the old source240 or spend a frozen R/K balance. Equations (1)-(2) hold at every cofactor. The rare-event hypothesis in (4) need not survive shared restrictions, so (4) is a root admission theorem, NOT an automatically hereditary consumed-influence estimate. Complete terminal U and N remain in any telescoping identity.

## 3. Threshold controls and the exact unpaid universal source

Let g=1-2a. At nonempty frequencies ghat=-2ahat, so

J(a)=H(g)/4-phi((1-2p)^2)/4+2p(1-p)+phi(p^2).

For p<=1/2, phi(p)<=1 implies phi(p^2)=2p phi(p)<=2p. Consequently J(a)<=H(g)/4+4p. If H(g)<=C I(g), then J(a)<=(C+8)D(a), and (4) yields

H(F)<=p H(V)+(C+13)I_x(F).                        (5)

For supplied threshold Theorem A one may take C=9, so a rare threshold event gives coefficient22, weighted by ACTUAL activation even as V approaches +1. This statement is conditional on that supplied theorem; (1)-(4) are independent of it. Recursive disjoint wrappers obey the corresponding static FEI constant max(C_base,22) when every active wrapper satisfies the rare-threshold event premise; correlation between descendants is not licensed by a disjoint substitution claim.

The all-event version of (4), with one absolute coefficient, is FEI-strength. Set V=-1. Then U=0, F=1-2a=g, I_x=I(g), so such an admission yields H(g)<=K I(g). Every Boolean g is represented after replacing g by -g if needed to ensure p<=1/2, which preserves H and I. Conversely full FEI with constant C implies (5) with C+13. Thus the existence of a uniform constant for this cancellation-aware admission is equivalent to full FEI (the constants need not agree). No all-event source has been paid here.

## 4. Why two arbitrary profiles need a private account

The recalled bent-splice obstruction already rules out replacing (4) by a shared-only bill for arbitrary nonconstant profiles G,V. Here is an independent elementary lower bound, not a novelty claim.

For even k>=4, let G(y)=(-1)^(sum_j y_(2j-1)y_(2j)) on zero-one bits, V=G-2*1_{y=0}, delta=2^-k, r=sqrt(delta). Both are Boolean and nonconstant. Let F choose G,V with a fresh unbiased shared bit. Then I_shared(F)=delta. Ghat has amplitudes +/-r; Vhat=Ghat-2delta; Fhat at shared-empty is Ghat-delta and at shared-nonempty is delta, for every private frequency. Hence

N=H(F)-[H(G)+H(V)]/2
 =2k delta+sum_T [psi(Ghat(T)-delta)
                  -(psi(Ghat(T))+psi(Ghat(T)-2delta))/2],

where psi(u)=phi(u^2). On each interpolation interval, |u|>=r-2delta>0 and

psi''(u)=-4log2|u|-6/ln2
 <=2k-4log2(1-2r).

The midpoint second-difference bound is at least -delta^2/2 times this upper curvature. Summing 2^k terms gives

N>=delta[k+2log2(1-2r)] >=(k-2)delta.              (6)

The last step uses r<=1/4. Thus no dimension-independent N<=K I_shared can cover arbitrary two-profile selectors, even with both profiles nonconstant and exactly one disagreement point. This refutes only that specified shared-only payment. The private influences are retained: I_y(F)=[I(G)+I(V)]/2=k/2+k delta, which grows rather than disappearing. It does not refute FEI, a good-coordinate selection theorem, or payment that uses the actual unused private owner.

## 5. Review scope

This is a repair and a reconstruction of existing obstruction evidence. Analytic level: author proof, independently unreviewed. Exact finite checks verify (1)-(2), boundary cancellation, and (6); finite enumeration does not prove the all-dimensional inequalities. The first unsupported universal step is an arbitrary-event influence-priced source J(a), or a two-profile continuation funded jointly from unused original private/shared accounts. Neither raw mask entropy nor shared disagreement alone supplies it.
