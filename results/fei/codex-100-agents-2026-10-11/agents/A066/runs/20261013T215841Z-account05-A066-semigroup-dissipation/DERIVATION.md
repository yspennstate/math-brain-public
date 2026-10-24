# Singleton scope repair, a joint budget, and block refinement

All entropies and row charges below use natural logarithms. A Boolean sign f is defined on a finite uniform cube, p_S=hat(f)(S)^2, I(f)=sum |S|p_S, b(f)=p_empty ln(1/p_empty), and K(f)=(H_nat(f)-b(f))/2=integral J_f. Zero-weight log terms vanish.

## 1. Source correction: identity for blocks, price for singleton queries

The previous stage correctly proved for every physical block B

2[K(f)-E_y K(f_y)]=M_B^+(f)+C_B^+(f)+ell_B(f),                 (1)

where plus omits the empty residual Fourier row and ell_B=sum_{nonempty U subset B}p_U ln(1/p_U). Equation (1) telescopes for all finite adaptive block-query trees, with terminal K retained.

The previous serialized claim v1 did not explicitly restrict its ensuing dimension-independent channel-plus-level budget to singleton-query trees. That unqualified clause is false for block-query trees. A088 identified an exact n=128 point-defect counterexample. This stage issues v2: retain the all-block identity, but state the influence price ONLY for singleton-query trees, unless an explicit block-refinement transfer is retained. The original run and claim v1 remain immutable provenance; no all-block reading is adopted downstream. The majority/addressing calibration needs only (1), so its independently reviewed v1 remains valid.

## 2. Pay the channel and level term jointly

For a singleton i, write d=Inf_i(f), x=|hat(f)({i})|, p=x^2. For the row indexed by T not containing i, put a=hat(f)(T), c=hat(f)(T+i). The previous scalar channel proof gives C_T<=2min(a^2,c^2). Here is the proof again to make the sharpened price self-contained. With q=a^2+c^2, r=2ac/q, the physical child masses are (a+c)^2 and (a-c)^2, so C_T=q g(r), where g(r)=((1+r)ln(1+r)+(1-r)ln(1-r))/2. For 0<=r<1, atanh(r)<=r/sqrt(1-r^2): their derivatives are respectively 1/(1-r^2) and 1/(1-r^2)^(3/2), with equal value zero at r=0. Integrating again gives g(r)<=1-sqrt(1-r^2). Evenness and continuity cover all |r|<=1; zero q contributes zero. Thus C_T<=q-|a^2-c^2|=2min(a^2,c^2). Summing only over T nonempty yields the improved use of the same influence account:

C_i^+ <= 2 sum_{T nonempty} hat(f)(T+i)^2 = 2(d-p).             (2)

The deleted empty row uses exactly p of that account; it must not be charged again. Since ell_i=p ln(1/p),

C_i^+ + ell_i <= 2d+p[ln(1/p)-2].                              (3)

Booleanity gives x<=d: hat(f)({i}) is the mean of D_i f, which is in {0,+1,-1}, while E|D_i f|=d. If x>=exp(-1), the bracket in (3) is nonpositive, so the sum is at most 2d. If 0<x<exp(-1), divide the extra term by d and use d>=x:

(p/d)[ln(1/p)-2] <= 2x[ln(1/x)-1] <= 2exp(-2).                 (4)

The last scalar function has derivative -2ln x-4 and its maximum at x=exp(-2). The x=0 case has zero extra term. Thus the universal JOINT singleton price is

C_i^+ + ell_i <= beta Inf_i(f), beta=2+2exp(-2).                (5)

This improves the earlier separate price beta_old=2+2/e by

beta_old-beta=2/e-2/e^2 = 2(e-1)/e^2 >0.                       (6)

No sharpness claim for actual Boolean functions is made. Equations (2)-(5) exploit a known exact row budget and Boolean x<=d, not a finite search or a new entropy integral. For adaptive finite SINGLETON-query trees T,

sum_v w_v(C_i^+(f_v)+ell_i(f_v))
 <= beta [I(f)-E_leaf I(leaf)],                                (7)

and the full exact stopping ledger is

2[K(f)-E_leaf K(leaf)]
 = sum_v w_v M_i^+(f_v)+sum_v w_v(C_i^+(f_v)+ell_i(f_v)).        (8)

The ordinary physical influence telescope proves nonreuse: each coordinate is charged through its current pivotal probability once along a path. Terminal K is not dropped. In entropy units, the exact reconstruction additionally retains b(f)-E b(leaf).

## 3. Refine a block without losing the transfer term

For a block B choose any finite adaptive ordering that queries exactly all B coordinates and then stops. This is a singleton refinement with the same actual physical children f_y, each weighted 2^(-|B|). Let

R_ref(B,f)=sum_internal w M_i^+(child),
P_ref(B,f)=sum_internal w(C_i^+(child)+ell_i(child)),
D_ref(B,f)=R_ref(B,f)-M_B^+(f).

Apply (1) to the block and (8) to its refinement. Exact equality gives

C_B^+(f)+ell_B(f)=P_ref(B,f)+D_ref(B,f),                       (9)
P_ref(B,f)<=beta I_B(f).                                     (10)

Here I_B=sum_{i in B}Inf_i(f)=I(f)-E_y I(f_y). D_ref is SIGNED. It cannot be deleted or assumed nonpositive; it represents the conditional-erasure charge into which a large block level bill is redistributed. Consequently the repaired block inequality is

C_B^+(f)+ell_B(f)<=beta I_B(f)+D_ref(B,f).                     (11)

For any finite block-query stopping tree, concatenate such refinements at its nodes, preserve its terminal partition, and sum (9)-(11). The exact retained transfer replaces the false all-block influence price. One may upper-bound D_ref by its positive part, but that positive part remains unpaid and no universal bound for it is asserted. Selecting a cheaper refinement order without pricing R_ref also does not pay it.

The FIRST UNSUPPORTED LINE for full FEI is still a dimension-independent payment of the retained sum of M_i^+ on a specified singleton tree, together with its actual terminal entropy; or equivalently a universal bound on R_nat(f)=sum_i M_i^+(f). The optimal uniform constant for R_nat/I is exactly C018's erasure constant, by the previously reviewed arbitrary-core character/tensor admission. The smaller beta prices a proved fragment, not this residual.

## 4. Exact all-n point-defect refinement and the n128 objection

Let f_n=1-2 indicator_{all-plus vertex}, n>=1. Write q=2^(-n). Its nonempty spectral probabilities are 4q^2 and I=n2^(1-n). A whole-cube block has C_B^+=M_B^+=0, constant leaves, and

ell_B/I = 4(1-1/n)(1-q)ln2.                                  (12)

For the canonical singleton refinement, a clean branch is constant; the surviving defect on k coordinates has weight 2^(-(n-k)). The query influence at dimension k is d_k=2^(1-k). Each step has weighted influence 2^(1-n), so the full refined cost spends exactly I.

For each defect node, every nonempty residual row has equal coefficient squares. Its channel and erasure charges coincide. Summing the geometric series gives the exact whole-refinement formulas

R_ref/I = [2-(4/n)(1-q)]ln2,
C_ref^+/I = [2-(4/n)(1-q)]ln2,
L_ref/I = (4/n)[1-(n+1)q]ln2,
P_ref/I = 2(1-2q)ln2,                                        (13)

where L_ref=sum weighted singleton level charges and P_ref=C_ref^++L_ref. These formulas hold also for n=1 with all charges zero. Their sum is (12), as required by (9). In particular, as n grows the original block level price approaches 4ln2, but the refined paid price approaches 2ln2 and the transfer D_ref/I approaches 2ln2. Roughly half the block bill has become retained conditional erasure, not vanished.

For the source n128 witness, the exact lower bound ln2>842/1215 follows from the first three positive terms of 2 sum_j (1/3)^(2j+1)/(2j+1). Hence

4(127/128)(1-2^-128)ln2 > 11/4.

The inequality is checked by rational arithmetic. Also e>8/3 from its first four Taylor terms plus the strictly positive tail, so 2+2/e<11/4. This reconstructs A088's original counterexample independently of its checker. It also defeats the new beta as an unqualified all-block price, since beta<beta_old.

The same certificate may be made a PROPER-block witness by adding one irrelevant coordinate, then querying exactly the 128 relevant coordinates. The residual Fourier support is still only the empty row, and the influence and charges are unchanged. Requiring only that B be a proper subset of ambient coordinates does not repair the price. This observation is a scope guard, not a new FEI counterfamily.

## 5. Paid fragment versus a universal conclusion

If a chosen singleton stopping tree satisfies sum_v w M_i^+<=A[I(root)-E I(leaf)] and terminal K(leaf)<=kappa I(leaf), (7)-(8) give

K(root)<=((A+beta)/2)[I(root)-E I(leaf)]+kappa E I(leaf).

For complete trees with constant leaves, H_nat(root)<= (1+A+beta)I(root), using b(root)<=I(root). This conditional direct heat-route coefficient improves by beta_old-beta from the previous separate payment. The stronger C018 implication via aggregate R_nat and character/tensor admission remains (A+2)/ln2 bits and is unchanged; the joint-budget improvement must not be reported as a lower proved universal FEI constant.

NEXT must therefore price the transferred/retained conditional-erasure bill with full Boolean structure and one owned influence account, while preserving arbitrary cores and leaf costs. Repeating a block identity, dropping D_ref, or adding another point-defect class bound cannot supply that bridge.
