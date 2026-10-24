# Non-flat point rows: a paid remainder and a sharp child-bank obstruction

All logarithms are base two. The cube is finite and uniform; all functions are actual Boolean signs and influence is the physical flip probability. Write delta=2^-d, d>=1. Let b be ANY Boolean core on d coordinates with b(0)=1, c=b-2 1_0 its actual one-vertex flip, and g an arbitrary Boolean gate on r>=1 disjoint coordinates. Define

    F(y,x)=b(y)+1_0(y)[g(x)-1].

Thus the core child is b with probability (1+a_0)/2 and c with probability (1-a_0)/2, where a_V=hat g(V). Let beta_T=hat b(T), E_i=Inf_i(g), e_i=Inf_i(F)=delta E_i, I_X=sum_i e_i, and I_Y the sum of actual core-coordinate influences of F. This construction includes destroyed point edges; no assumption on the signs of the d incident edges is made.

## 1. Exact non-flat conditional reference

Finite character expansion proves

    hat F(T,V)=beta_T 1_(V=empty)+delta[a_V-1_(V=empty)].

For a relevant gate query i, use the COMPLETE normalized row laws mu_i(T,V)=p_(T,V+i)/e_i and r_i(T,V)=p_(T,V)+p_(T,V+i). Retaining (V,beta_T) preserves their full KL: the likelihood ratio is constant on every such cell. This partition need not have bounded alphabet, and the retained gate/core terminal charge is not paid by this sufficiency assertion.

If only V is retained, conditional core distributions coincide for every nonempty V. For the exceptional cell V=empty put

    rho_i=1-delta+delta(a_0^2+a_i^2),
    q_i(T)=[(beta_T+delta(a_0-1))^2+delta^2 a_i^2]/rho_i,
    D0_i=D(Uniform_(2^d)||q_i).

Parseval and sum_T beta_T=b(0)=1 prove sum_T q_i(T)=1. For a_i!=0 it is strictly positive on the uniform law. The exact loss is

    L_i=e_i[D(mu_i||r_i)-D(mu_i^V||r_i^V)]
       =delta a_i^2 D0_i.                                      (1)

If a_i=0 the exceptional derivative cell has zero mass and L_i=0. This is the arbitrary-core version of A090's bent formula, rederived without assuming flat amplitudes or source acceptance.

Since rho_i<=1 and each q_i(T)>=delta^2 a_i^2/rho_i,

    0<=D0_i<=log2[1/(delta a_i^2)],
    sum_i L_i<=delta d W1(g)+delta Lambda1(g),                   (2)

where W1=sum_i a_i^2 and Lambda1=sum_i a_i^2 log2(1/a_i^2). This upper bound remains valid even if the non-flat amplitude beta_T nearly cancels the point edit. There is no minimum nonzero core Fourier coefficient hypothesis.

The genuine Boolean derivative of g takes values in {0,+1,-1}, so |a_i|<=E_i. The elementary maximum u ln(1/u)<=1/e on [0,1] gives

    Lambda1(g)<=kappa I(g), kappa=2/(e ln2)<9/8.                 (3)

This uses signed Booleanity at the physical derivative, not an arbitrary normalized spectral vector.

## 2. A single root influence partition pays all discarded KL

Any nonconstant sign h on d bits has I(h)>=2d delta. Here is an elementary proof: every nonempty proper vertex set of the d-cube has at least d boundary edges. Induct on d. If both (d-1)-dimensional fibers are nontrivial their internal boundaries total at least 2(d-1)>=d. If only one is nontrivial, its d-1 edges plus at least one crossing edge suffice. If both are trivial and unequal, all 2^(d-1)>=d crossing edges appear. The d=1 case is direct. Each undirected pivotal edge contributes 2delta to influence.

The actual weighted core influence is

    I_Y=[(1+a_0)I(b)+(1-a_0)I(c)]/2.                            (4)

If both b and c are nonconstant, I_Y>=2d delta and W1<=1, whence delta d W1<=I_Y/2. If b is constant, it is +1 and c is its point flip, so I_Y=d delta(1-a_0). If c is constant, it is -1 and I_Y=d delta(1+a_0). In these cases W1<=1-a_0^2 yields delta d W1<=2I_Y. Thus, for ALL cores and gates,

    sum_i L_i<=2I_Y+kappa I_X <= 2I_Y+(9/8)I_X;                (5)

and when both physical core children are nonconstant,

    sum_i L_i<=I_Y/2+kappa I_X.                                (6)

This is one partition of the ORIGINAL physical influence, summed over all gate queries without repeating a core owner. It pays only the discarded quotient remainder. It does not establish that these root quotas are still available after terminal entropy, retained quotient price or other history charges have been paid.

For the specified quadratic bent core of A090 with even d>=4, its independent two-bit factors each have four coefficient magnitudes 1/2, so beta_T=sigma_T sqrt(delta); evaluating b(0)=1 gives the stated sign counts (2^d +/-2^(d/2))/2. The exact (V,beta_T) partition is its (V,sigma_T) partition. Each exceptional likelihood ratio is <=4, because |a_0-1|<=2 and sqrt(delta)<=1/4, so D0_i<=2. At the marked point every neighbor also has value +1, so flipping it adds one undirected pivotal edge per direction: Inf_(y_j)(F)=1/2+delta(1-a_0). Hence sum_i L_i<=2delta W1<=2delta<=Inf_(y_1)(F)/4. This independently reconstructs A090's full stated lemma, including its isolated-reserve limitation, with no repair.

## 3. A genuine child surplus need not pay the same loss

Root influence capacity in (5) is not a certified terminal surplus. The distinction is sharp on a NON-FLAT actual core. Let d>=2 and

    b_d(y)=-1+2 1_0(y), c_d=-1, g(x)=x.

Then F=-1+1_0(y)(1+x) is a (d+1)-bit one-point sign. The gate query has e=delta, I_Y=d delta and I(F)=(d+1)delta. Both actual children, b_d and c_d, satisfy H<=4I; so does F. The core b_d is non-flat: its constant coefficient is -1+2delta and every other coefficient is 2delta (for d=2, magnitudes happen to be flat; the non-flat subfamily is d>=3).

The mask-only quotient retains no residual gate mask and its reference probability is one. Its exact lost KL is L=delta D0 with

    z=(1-delta)^2+delta^2,
    D0=(1-delta)(d-1)+delta log2(delta/z).

As z<=1 and (2d-1)delta<=1 for d>=2,

    d-2<=D0<=d, and L>=delta(d-2).                             (7)

The upper bound is also immediate from the complete row KL bound log2(1/e)=d.

Use the ACTUAL terminal child bank at rate C, not a hypothetical influence quota:

    S_C=[C I(b_d)-H(b_d)]/2+[C I(c_d)-H(c_d)]/2.

Let eta(u)=-u log2 u, p0=(1-2delta)^2. Exact Fourier expansion gives

    H(b_d)=eta(p0)+(4delta-4delta^2)(2d-2),
    I(b_d)=2d delta,
    0<=S_4<=4delta+4(d-1)delta^2<=5delta.                       (8)

For nonnegativity use eta(p0)<=(1-p0)/ln2<8delta and the remaining entropy <=8(d-1)delta. The upper bound in (8) drops nonnegative eta and uses (d-1)delta<=1/4. Therefore

    S_C=S_4+(C-4)d delta,
    (L-S_C)/e >= (5-C)d-7.                                    (9)

For every fixed C in [4,5) the children are legitimately C-certified but no finite universal K gives L<=S_C+K e on this family. At C=5, however, S_5>=d delta>=L, so C=5 pays this exact quotient loss with no query allowance. Thus five is the sharp asymptotic child-bank price threshold for this specified loss, although the complete actual family already obeys FEI at rate four. This refutes only the extra payment requirement for the lossy quotient; it refutes neither child certification nor FEI nor a larger-price policy.

The constant child is not essential to the obstruction. Tensor the ENTIRE physical fixture with an independent nonconstant point sign q on 2d coordinates, retaining its full terminal spectrum and cost. Then I(q)=4d delta^2, H(q)<=4I(q), both actual query children b_d q and -q are nonconstant, and Fq still has H/I<=4. The same independent spectator factor occurs in both complete gate row laws, so L and e are unchanged. Its actual averaged child bank is S'_C=S_C+C I(q)-H(q). Therefore

    (L-S'_C)/e >= (5-C)d-7-4C d delta -> infinity, C<5.

At C=5 the added bank is nonnegative, so S'_5>=S_5>=L. This tensor continuation is not claimed to be a one-vertex mutation on all 3d core coordinates; it is an actual non-flat point attachment with an independent, nonconstant terminal that is retained in full. It shows that merely requiring both terminal children nonconstant cannot repair the insufficient-bank substitution.

In particular, replacing the informative partition by a lossy one can demand a higher terminal bank price than the actual entropy problem. The full conditional reference or its sufficient (V,beta_T) partition avoids this injected cost. It still retains the original terminal charge, which is not automatically bounded by (5).

## 4. First unsupported universal implication

The non-flat quotient loss is now paid at the explicit root rates (5)-(6). A genuine child surplus can fail to cover it at rates [4,5), as (9) proves. What remains is to retain a sufficient signed/amplitude statistic or choose a reference whose ACTUAL joint retained cost and conditional remainder fit one unspent terminal surplus, including arbitrary core/gate entropy. No step here proves the universal inequality sum_i e_i D(mu_i||r_i)>=sum_i e_i log2(1/e_i)-K I. NEXT must use actual complete-reference price, not substitute a fresh root quota for unused certified child slack.
