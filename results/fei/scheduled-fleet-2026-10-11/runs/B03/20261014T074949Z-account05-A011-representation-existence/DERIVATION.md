# Weak query, unequal amplitudes, one incoming reference bank

Bits throughout; ideal complete-reference costs, separate single-word rounding. This is a narrow continuation of the point-edit transfer interface. No universal FEI theorem is claimed.

## 1. Actual family and paid incoming model

For even k>=2 let b_k(z)=(-1)^(sum paired binary products), on k active bits. On three additional bits let a_3(y)=1-2*1_{y=000}. Put g(z,y)=b_k(z)a_3(y). Add one dummy data bit d and one fresh selector bit x. Pick z* of Hamming weight k/2, y*=000, d*=0, x*=0, and flip g at this full point only on the selector event:

    F=g-2g(z*,000)1_{z=z*}1_{y=000}1_{d=0}1_{x=0}.

The number of data bits is n=k+4, t=2^-n, selector probability p=1/2. The source's Fourier amplitudes have two nonzero magnitudes: (3/4)2^-k/2 on 2^k frequencies and (1/4)2^-k/2 on 7*2^k frequencies. It is a genuinely unequal-amplitude source. Its original pivotal degree at the selected point is k/2+3, because the quadratic bent degree is the point weight and all three conjunction edges are pivotal. Thus

    I_g=k/2+3/4; C=t(k/2+1); E=t(k/2+3); I_x=t;
    I_F=I_g+C-E+I_x=I_g-t.

Use the full uniform data reference R(T)=2^-n=t, cost c=n on both the original and point-edited data functions. For the actual data-frequency marginal q(T), let K(U|T) be the true selector-frequency kernel and set Q(U,T)=t K(U|T). Every coefficient is nonzero in this family, so Q is a positive normalized complete reference. Its entire cost is exactly

    CE_F=n+B, B=H(S_x | S_data).

The same coefficient calculation as the previous point-edit interface gives nonempty-selector mass V=t. Therefore B<=nt+4t=(k+8)t (also directly from h2(t)). The source reserve S4=4I_g-c=k-1 is an actual supplied-reference reserve, not a renewed child assumption. The original complete root bank is

    4I_F-CE_F=S4-B-4t >= k-1-(k+12)2^(-k-4)>0.

For k=2 the lower margin is 25/32; the term (k+12)2^(-k-4) decreases as k increases, while k-1 increases. Thus every even k>=2 root is paid at rate four with erased edges and source cost retained. This does not assert novelty for its entropy bound.

## 2. A weak physical query with two nonconstant children

Expose the dummy DATA bit d, not the fresh control. One child is the original g (with an unused x), the other is g with one point edit under x, with the dummy removed. Both are nonconstant. The query influence is I_d=t, which tends to zero. The children have influences I_g and I_g-4t, respectively, and I_F=average child influence+t.

Define L(v)=-v log2 v for v>=0, L(0)=0. Index the remaining frequencies by W (the k+3 core bits and x). Let a_W be the old source coefficient, zero when W contains x. The two parent coefficients with queried membership absent/present are a_W+z_W and z_W, where |z_W|=t. The physical child coefficients are a_W and a_W+2z_W. Their squared masses have the same fair average total as the paired parent masses. Consequently the true entropy decrement is exactly

    Delta_d=sum_W [L((a_W+z_W)^2)+L(z_W^2)
                  -L(a_W^2)/2-L((a_W+2z_W)^2)/2].

Let w=a_W/z_W and G(w)=L((w+1)^2)+L(1)-L(w^2)/2-L((w+2)^2)/2. Scale cancellation gives each term t^2 G(w). When a_W=0, G(0)=4. For nonzero a_W the two possible absolute ratios are 12*2^(k/2) and 4*2^(k/2), both at least eight.

For phi(u)=L(u^2), phi''(u)=-4log2|u|-6log2 e away from zero. The exact second-difference integral gives

    G(w)=integral_{-1}^1 (1-|s|)[2log2|w+1+s|+3log2 e] ds.

For |w|>=4 the interval stays away from zero, |w+1+s|>=|w|-2>=|w|/2. Since ln2<3/4 (the strict trapezoid upper bound on the integral of 1/x from1 to2), 3log2 e>4. Thus in the first query, where |w|>=8, G(w)>2log2|w|+2>=k+6. There are 2^(k+3) nonzero a_W and equally many zero a_W. The remaining cube has 2^(k+4) frequencies, and 2^(k+4)t^2=t. Therefore

    Delta_d > t[(k+6)/2+2]=(k/2+5) I_d.

This all-k estimate proves an unbounded local entropy-decrement price for the weak nonflat query, even though both children are nonconstant and the prescribed parent reference is already paid at rate four. It refutes a prospective dimension-independent local-query rule; it does not refute existence of a different query, stopping policy, or FEI.

## 3. Carry the SAME incoming reference and both terminal costs

Let P_0,P_1 be the actual child spectra, m(W)=(P_0(W)+P_1(W))/2. Delete queried membership from the incoming Q to get r(W)=Q(0,W)+Q(1,W). For every W, m(W)>0. Define the actual fair-child posterior pi_b(W)=P_b(W)/(2m(W)), unnormalized inherited reference Rtilde_b(W)=2r(W)pi_b(W), Z_b=sum_W Rtilde_b(W), and R_b=Rtilde_b/Z_b. Then Z_b>0 and Z_0+Z_1=2. Zero child probabilities are retained as zero inherited probabilities, not replaced with a fresh floor. For true child atoms,

    P_b(W)/R_b(W)=[m(W)/r(W)] Z_b.

The conditional incoming divergence L_d=sum_W m(W)KL(P(S_d|W)||Q(S_d|W)) is measured against this same Q. Disintegration yields

    T_d:=CE_F-average_b CE(P_b,R_b)
        =Delta_d+L_d-average_b log2 Z_b >=Delta_d.

Hence the FULL local incoming-reference ledger also has T_d/I_d>k/2+5. A favorable KL remainder cannot erase the true entropy obstruction. Both whole child costs are retained, and no influence price for each normalized child reference is assumed.

The one-use paid ledger is nonetheless exactly

    average child CE + T_d = c+B,
    4I_F-[average child CE+T_d]=S4-B-4t
                                  >=k-1-(k+12)t>0.

This spends at most (k+12)t from the original source reserve once, while retaining the entire prescribed child terminal bill. It does NOT assign that amount separately to each descendant. It pays the weak-query fixture from a single known bank and does not attempt the false local bound T_d<=K I_d. An arbitrary independent Boolean terminal h with normalized complete prescribed reference R_h is preserved exactly by product-compatible inheritance: each child reference is R_h tensor R_b, every cost has the full c_h added, and every divergence has the full D_h added. No independent terminal influence pays this query account.

## 4. Two actual weak queries, either order, without a new floor

Query both d and x, in either physical order. F is invariant under swapping these two input bits, while its incoming reference need not be. Both reference histories use the exact normalized inheritance above. On zero true/reference fibers choose any normalized child posterior; for independent terminals use the product-compatible core posterior, retaining off-true-support terminal reference mass. The four equiprobable physical leaves are three copies of g and one whole-point flip gstar on the k+3 active data bits. Every leaf is nonconstant. The final average influence is I_g-3t; the original I_F=I_g-t, so the total physical pivotal query mass is exactly2t. The second query has influence0 on the untouched child and2t on the edited child.

On the untouched child its entropy decrement is0. On the edited child the scalar calculation uses |z|=2t, all 2^(k+3) source coefficients nonzero, and minimum |a/z|=2*2^(k/2)>=4. Hence its entropy decrement is strictly greater than2t(k+4). Combined with the first query,

    Pi_H=H(F)-(3H(g)+H(gstar))/4 > t(3k/2+9),
    Pi_H/Pi_I >3k/4+9/2, with Pi_I=2t.

For each actual node define T as its whole incoming reference cost minus fair average inherited child cost. Its signed entropy/conditional-KL/normalizer ledger is exact. Summing with ORIGINAL physical reaches (1 at the root and1/2 at its two children) gives

    average_four_leaf_CE + T_root + (T_child0+T_child1)/2
        = CE_F = c+B.

The reference costs and normalizers are allowed to differ between query orders; no model symmetry or fresh descendant floor is assumed. Each divergence release is nonnegative, so the total whole-query ledger is at least Pi_H and has the same unbounded lower price. The total cost including EVERY inherited leaf remains paid by the SAME margin S4-B-4t>=k-1-(k+12)t>0. This is one source-bank payment, not two independent grants of it. Independent normalized terminal cost and debt remain outside that account at every node and leaf by the exact product-compatible inheritance rule.

## 5. Exact first unsupported line

The payment uses the explicit seed reserve k-1 and a single uniform incoming data model whose whole cost is n+B. For an arbitrary unequal-amplitude core with prescribed low-cost reference, that reserve need not exist, and a uniform reset can cost its entire data dimension. The first universal missing line is a selected physical query/history whose complete reference change and inherited terminal costs are paid by the SAME unused arbitrary-core reserve, without a fresh descendant floor or a local entropy-decrement price. The exhibited weak query rules out the latter shortcut; it does not rule out adaptive strong pivots or a global one-use ledger.
