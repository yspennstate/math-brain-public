# The logarithmic reserve is the physical terminal-curvature density

All entropy is in bits. Physical cubes are finite and uniform. Let h be the six-bit sign negative on {0,1,2,4,8,16,32,6,17,40}, a one bit denoting a negative input, and J(x)=-h(x xor1).

## Theorem: a paid local correction for every rare core dimension

Let g be any nonconstant Boolean core with minority probability 0<p<=1/16, oriented so P(g=-1)=p. Form F=k(g_1,...,g_6), k in {h,J}, on six identical disjoint copies. Query any physical coordinate i in any block j. Write d=Inf_i(g), beta=ghat({i}), and q_j for the outer pivotal probability under five independent outputs of bias p. Retain the FULL heterogeneous terminal correction

    C(p_1,...,p_6)=H_p(k)-sum_l q_l h2(4p_l(1-p_l)).

For the actual queried-core children, with their true weights 1/2, put Delta C=C_parent-(C_child+ +C_child-)/2. Then

    Delta C <= (5/4) q_j d = (5/4) Inf_(j,i)(F).        (T)

For h the stronger coefficient 1/2 holds. For J directions pivotal at the all-positive assignment of the other inputs, coefficient 1/8 holds. For irrelevant physical i the correction is zero. No dimension cutoff or lower singleton coefficient is assumed. Both nonconstant children and a constant child are allowed. Negative corrections remain signed credits; they are not replaced by their absolute values.

This pays the additive physical terminal curvature from the influence of the actual queried coordinate. It does not pay the inherited decrement of the arbitrary core or assert that a child has unused slack. It is a first-query statement with identical starting biases, not a blanket price for an arbitrary later heterogeneous history.

## 1. Preserve complete terminals through the physical query

For arbitrary independent Boolean cores and the normalized biased spectrum of a fixed outer gate,

    H(F)=sum_l q_l H(g_l)+C(p), I(F)=sum_l q_l I(g_l).

The physical spectral set specifies its occupied blocks and each occupied child's nonempty spectral set. Shannon chain rule gives the entropy identity, including every constant spectral mass. Pivotal edges give the influence identity. Neither statement uses the child's FEI inequality.

On querying i in block j, core means become m_j^+=m+beta and m_j^-=m-beta, where m=1-2p. The pivot q_j is independent of that selected bias. Every other q_l is affine in it, so its average over the two actual children equals its parent value. Therefore

    Delta H(F)=q_j Delta H(g)+Delta C,
    Inf_(j,i)(F)=q_j d.                               (1)

All five other complete core entropies cancel only through this affine average, not by being dropped. A constant child has H=I=0 and is included exactly by continuity.

## 2. An exact directional curvature identity

Fix the other five output laws. Write k(y)=A(y_-j)+y_j D(y_-j), and let a_T,d_T be the normalized biased coefficients on those other inputs. Put D_T=d_T^2, q=sum_T D_T, and for a varying selected mean x,

    U_T(x)=(a_T+x d_T)^2, v(x)=1-x^2.

The full outer spectrum consists of U_T and vD_T. Parseval gives sum U_T+v q=1. Other directions' q_l terms in C are affine in x, hence their central second difference is zero. The non-affine part of C is

    F_j(x)=sum_T ell(U_T(x))+v(x)sum_T ell(D_T)
                                             +q x^2 log2(x^2),
    ell(z)=-z log2(z), ell(0)=0.                       (2)

This follows by expanding sum ell(vD_T) and subtracting q h2(v), cancelling its v log(v) exactly before differentiating. Where x!=0 and U_T>0 for active D_T, elementary differentiation yields

    F_j''(x)=-2 L_j(x),
    L_j(x)=sum_(D_T>0) D_T log2(U_T(x)/(x^2 D_T)).      (3)

Indeed (ell((a+xd)^2))''=-2d^2 log2((a+xd)^2)-6d^2/ln2; the last term of (2) contributes 2q log2(x^2)+6q/ln2, and the middle term contributes 2sum D log2 D. All constant derivative terms cancel. L_j is exactly the logarithmic boundary slope used for signed erasure admission, now with the OTHER five laws held fixed as a physical query requires. Simultaneously changing all six biases would differentiate a different function and is not permitted here.

At an isolated coefficient zero, ell((a+xd)^2) is continuously differentiable and its second derivative has only a locally integrable logarithmic singularity. Its limiting curvature is positive infinity, which produces negative Delta C credit. Formula (3) and the integral below therefore remain valid as improper integrals; no finite positive boundary charge is lost. Terms with D_T=0 are independent of x and omitted.

## 3. A generic continuum curvature envelope

For q>0 and |x|>=ell>0, concavity of log with weights D_T/q gives

    L_j(x) <= q log2[sum_(D_T>0) U_T(x)/(x^2 q)]
           <= q log2[1+(1-q)/(x^2 q)]
           <= q log2[1+(1-q)/(ell^2 q)].              (4)

The second inequality keeps possible D=0 packets correctly: their nonnegative U masses can only increase the full Parseval sum 1-(1-x^2)q. Also 0<q<=1 because D is the half-difference of a Boolean gate's two sections. A vanishing active U is treated by its negative infinite L limit, which helps the upper bound.

Let b=|beta|. The exact central-difference Green kernel gives

    Delta C = integral_(-b)^b (b-|u|) L_j(m+u) du.

The kernel is nonnegative and has total mass b^2. Hence whenever the child-mean interval avoids zero,

    Delta C <= q beta^2 log2[1+(1-q)/(ell^2 q)].       (5)

For beta=0 the correction is exactly zero. This is an integral inequality covering EVERY real singleton shift, not a finite grid. It also explains the source's opposite curvature signs: positive logarithmic admission slope means negative second derivative of F_j and therefore positive physical curvature debt.

Actual Boolean constraints are |beta|<=d and |beta|<=2p. The first follows by averaging the signed physical derivative; the second from beta=-2 E[1_(g=-1)chi_i]. Thus beta^2/d<=2p for d>0. On the entire rare domain, m-b>=1-4p>=3/4; use ell=3/4 in (5):

    Delta C/(q d)<=2p log2[1+16(1-q)/(9q)].            (6)

This is a sharper bias-dependent envelope than the uniform constants of (T).

## 4. Gate-specific analytic endpoint reductions

For h, direct actual pivotal counting gives q=2p(1-p)^3(2-p)>=3p for 0<p<=1/16. Consequently

    1+16(1-q)/(9q)<=1+16/(27p)<=1/p,

since p<=1/16<11/27. The function p log2(1/p) increases on (0,1/16], so (6) is at most2p log2(1/p)<=1/2.

For J, every direction has a frozen all-zero pivotal status. If it is pivotal there, q>=(1-p)^5>=1-5p>=11/16. Then

    1+16(1-q)/(9q)<=1+80p/[9(1-5p)]
                                  <=1+80/99<2.

Thus (6)<2p<=1/8. There are four such directions; all are checked independently without assuming J is transitive.

J direction0 has a single-negative pivotal witness, while direction4 has its first pivotal witnesses at weight TWO. The initial proposal that both had a weight-one witness is false and is preserved in out/FAILED_SINGLE_NEGATIVE_WITNESS.json. The actual fixed-table certificate records both weights. If r is that minimum weight (1 or2),

    q>=p^r(1-p)^(5-r)>=(3/4)p^r.

The endpoint inequality (15/16)^4>3/4 is exact. Consequently

    1+16(1-q)/(9q)<=1+64/(27p^r)<=4/p^r,

and (6)<=2p[r log2(1/p)+2], which increases on (0,1/16]. Its endpoint is3/4 for r=1 and5/4 for r=2. This proves the corrected uniform5/4 theorem, with the finer3/4 price for direction0. These analytic bounds hold at every real p in the domain; the envelopes tend to zero as p->0.

At beta=2p one child can be constant, with selected mean x=1. Formula (2) has a continuous finite endpoint because the v log(v) term was cancelled first. The integral reaches x=1 without an uncancelled endpoint singularity. At d=0, beta=0 and the parent and child laws coincide. These reductions cover the entire compact closure and all omitted boundaries.

## 5. Exact downstream statement and the unpaid inherited bill

For any proposed rate K, (1) and (T) imply

    Delta H(F)-K Inf_(j,i)(F)
      <=q_j[Delta H(g)-(K-5/4)d].                     (7)

With k=h replace5/4 by1/2; for a dominant J direction replace it by1/8. Thus if an actual core query is already certified at rate K0, the same first query in the rare composition is certified at rate K0+5/4. If a child/core surplus is supplied, the exact inherited term remains visible and is not charged twice.

The source's eight non-flat queries have Delta H(F)>4 Inf even when Delta C is negative. This does not conflict with (T): the unknown inherited core decrement can itself exceed the proposed rate. Our bound pays the additional curvature only. The first unsupported universal line is a noncircular choice/payment of that inherited arbitrary-core decrement from an unused actual child surplus, followed by transport after another query when the blocks no longer have identical bias p. Neither an absolute FEI bound nor an unlimited heterogeneous history price follows here.
