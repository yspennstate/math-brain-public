# Boolean code-packet repair has linear entropy continuity with an explicit error budget

2026-09-30 UTC. Status: proved continuity and conditional paid-induction criterion. The remaining universal influence payment is not proved. Full FEI remains open.

## Continuity lemma for a quantized Boolean comparison

Let f,f_0 be Boolean on n bits, let epsilon=Pr(f!=f_0), and assume every nonzero coefficient of f_0 has magnitude at least

    lambda=2^(1−k),             k>=1 an integer.

If epsilon<=min(1/8,2^(−k−1)), then

    H(f)<=H(f_0)+4n epsilon+h_2(4epsilon)+L_k epsilon,
    L_k=2^(k+1)[2k+log2(e)].                             (1)

In particular,

    H(f)<=H(f_0)+epsilon[8n+L_k+4log2(e)].               (2)

Also

    |I(f)−I(f_0)|<=2n epsilon.                           (3)

The n dependence is retained. This is not a universal bound by tail influence.

### Proof

Write a=f_0hat and b=fhat. Boolean disagreement gives the coefficientwise estimate |a_S−b_S|<=E|f_0−f|=2epsilon. Let A=supp(a), of size M. Parseval and the minimum coefficient bound give M<=lambda^(−2).

For S in A, the small-error assumption implies |b_S|>=lambda/2=2^(−k). On [2^(−2k),1], the absolute derivative of phi(p)=p log2(1/p) is at most 2k+log2(e). Moreover

    sum_(S in A)|b_S^2−a_S^2|
      <=2epsilon sum_(S in A)(|a_S|+|b_S|)
      <=4epsilon sqrt(M)<=4epsilon/lambda.

The entropy change on A is therefore at most L_k epsilon.

Outside A, the squared mass tau is at most ||f−f_0||_2^2=4epsilon. Conditional entropy on at most 2^n labels gives

    sum_(S outside A)phi(b_S^2)<=h_2(tau)+n tau
                               <=h_2(4epsilon)+4n epsilon,

using 4epsilon<=1/2. This proves (1). If epsilon>0, Boolean truth tables give epsilon>=2^(−n), and h_2(4epsilon)<=4epsilon[log2(1/(4epsilon))+log2(e)]<=4epsilon[n+log2(e)]. This gives (2); epsilon=0 is immediate.

An edge's pivotal status can change only when f and f_0 disagree at one of its endpoints. Each coordinate influence therefore changes by at most 2epsilon. Summing proves (3).

## Application to the linear L2 code-ball repair

In LINEAR_L2_REPAIR.md, each repaired degree-d Boolean child k_z has Fourier coefficients in 2^(1−d)Z for d>=1. Walsh averaging over r syndrome bits gives coefficients of f_0 in 2^(1−d−r)Z. The same assertion holds for d=0,r>=1 by ordinary r-bit Boolean granularity. Thus (1)–(3) apply with k=d+r whenever k>=1. The fully constant d=r=0 case can be handled directly and is not needed below.

The repair theorem gives epsilon<=K_d delta/4, with K_d=2^(O(d)), independently of n and r. Therefore its entropy loss is linear in delta up to the explicit n and radius/rank dependent factors. A generic n sqrt(delta) entropy-continuity loss is not necessary for this quantized Boolean comparison.

## A conditional approximate degree-induction step

Use the exact code-packet theorem with r>=1 and the following notation for f_0:

    Ibar=E_z I(k_z),
    G_0=I(f_0)−Ibar,
    K=2[d+2r−1+log2(e)]/(D−2d).

Assume deg(f)>d, so these are strictly lower-degree children, and assume all the Boolean children satisfy H(k_z)<=C I(k_z), with C>K. The exact packet theorem yields

    H(f_0)<=C I(f_0)−(C−K)G_0.

Combining with (2)–(3) proves

    H(f)<=C I(f)−(C−K)G_0
       +epsilon[(2C+8)n+L_(d+r)+4log2(e)].              (4)

Thus the sufficient error-payment criterion

    epsilon[(2C+8)n+L_(d+r)+4log2(e)]
        <=(C−K)G_0                                     (5)

carries the same FEI constant from the children to f. One may use

    G_0>=(D−2d)m_0,

where m_0 is the repaired nonzero-code spectral mass. Let m be the original retained mass in balls with nonzero code center. If epsilon<=m/16, Cauchy–Schwarz gives sqrt(m_0)>=sqrt(m)−2sqrt(epsilon)>=sqrt(m)/2, so m_0>=m/4.

Every hypothesis is essential to the scope: the small coefficientwise error condition, the code geometry, the child inequalities, and the explicit reserve (5) are all retained. If m_0=0 there is no such positive code reserve; closeness to a constant does not pay arbitrary Boolean errors.

## Remaining gap

This proves a linear continuity estimate and a checkable sufficient approximate induction budget. It does not show that (5) holds for every high-ratio or critical Boolean function. In particular the n epsilon term and the potentially large L_(d+r) factor still need to be paid by genuine original influence. The existence of a universally useful packet decomposition remains open.

The report uses standard coefficient granularity, elementary entropy continuity on a fixed support, and exact Boolean disagreement. No general overlapping-product entropy triangle inequality is assumed. The parent independently checked the continuity constants and the inclusion of the 2C n epsilon influence-transfer cost in (4). Novelty is unverified. No executable code or numerical certificate is included.
