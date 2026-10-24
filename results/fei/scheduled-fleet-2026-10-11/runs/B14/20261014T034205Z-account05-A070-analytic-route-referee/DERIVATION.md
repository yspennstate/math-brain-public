# Source transfer: independent referee and exact privacy boundary

## 1. Independent reconstruction of A069 stage 4

On each source-visible edge fix its Boolean source disagreement d in {0,1} before averaging private coordinates. If mask disagreement has probability p<=theta<=1/2, the final disagreement is t=p when d=0 and t=1-p when d=1. The ratio (Kd+Mp)/t is M for d=0 (zero t handled separately), and (K+Mp)/(1-p) for d=1. The latter increases with p for K,M>=0. Therefore A=max(M,(K+Mtheta)/(1-theta)) pays every visible edge; private edges only contribute M times their mask disagreement. Sum each physical influence coordinate once. This proves K I(g)+M I(q)<=A I(gq). The previously accepted Boolean product cost gives Gamma(gq)<=Gamma(g)+W(q), so paid source and mask codes imply the asserted final bound.

Compatible two-subcube masks on C,U,V,Y with source g(C,Y) have conditional common-edge mask disagreement p=2^-s+2^-t-2^(1-s-t)<=1/2 on boundary edges, zero elsewhere. Y edges have no mask change. Thus M=12 from the accepted A069 mask theorem applies directly; no universal source code is assumed.

For g(x,Y) with unequal h_+,h_- use the same Y tree for both. Let J average core influence, D=P(h_+!=h_-), B average complete Y cost. Conditional Parseval gives W_Y(g)=average W_Y(h). The source control spectrum consists only of sets containing x, with total mass D. Hence Gamma_T(g)=B+2Var(g)+2(d+1)D, where d is x's internal C depth. Poincare Var(g)<=J+D yields Gamma(g)<=B+2J+(2d+4)D. Each Y edge of gq differs precisely when g does, so J=I_Y(gq). The edge ratio just proved, applied only to control edges with K=2d+4,M=12, gives Gamma(gq)<=B+2I_Y(gq)+(4d+20)I_controls(gq). Every actual final core is a scalar sign times the selected h; B is exactly its actual average full reference cost. If BOTH cores satisfy Gamma_Y(h)<=K I(h), this gives max(K+2,4d+20)I. Constants remain in B and cannot satisfy that paid-code hypothesis.

Verdict: A069-SOURCE-BLIND-SHARED-EDGE-TRANSFER@1 HOLDS at its full stated scope, no repair. The same common hierarchy and complete root/terminal bits are essential.

## 2. Partial privacy extends the sufficient edge condition

Partition U=U0 disjoint-union U1 and V=V0 disjoint-union V1, with U1,V1 both nonempty. The source may depend arbitrarily on X=C,U0,V0,Y but not Z=U1,V1. Put a=2^-|U1|,b=2^-|V1| and theta=max(a,b,a+b-2ab)<=1/2. For each fixed X assignment, the two private event probabilities are either 0 or a, and either 0 or b, according to the exposed assignments in U0,V0.

On a C boundary edge, mask disagreement is the XOR of those private events; its probability is one of 0,a,b,a+b-2ab. On a U0 edge crossing its exposed event boundary, the V mask is identical on both endpoints and cancels out in the disagreement; the U mask changes with probability either 0 or a, multiplied by the fixed common-event indicator. V0 edges similarly cost 0 or b. Other visible edges cost zero. Thus the exact source-blind condition holds after moving exposed private coordinates into X, and the accepted transfer pays any source on X, with A=max(12,(K+12theta)/(1-theta))<=2K+12 if Gamma_T(g)<=K I(g). This is a conditional reference transfer, not construction of paid arbitrary source references.

For one private coordinate in U this applies whenever |U|>=2. The corresponding statement for V is identical. More generally both exclusive blocks must retain at least one unseen coordinate for this sufficient argument. It is not claimed necessary for each individual source.

## 3. Complete exposure can destroy a paid source budget

Let C={c}, U={u}, V contain t bits, Y contain t independent bits, t>=4. Set delta=2^-t. Let q1=1-2*1{c=+,u=+}, q2=1-2*1{c=+,V=all+}, q=q1*q2. Let h=1-2*1{Y=all+}, source g=q1*h and final f=gq=q2*h. The source sees only one private coordinate u (plus common c and Y), and the nonconstant terminal core h remains in the final function. Exact physical influences are

    I(g)=1+2t delta, I(q)=1+t delta,
    I(f)=(3t+1)delta, R_I(g,q)=2-delta.

The hierarchy is T=(T_Y,(c,(u,T_V))) with binary singleton trees within Y,V. If W_Y(h) denotes its Y mask cost, then

    Gamma_T(g)=11/2 - (1-2delta)^2/2 + W_Y(h),
    W_Y(h)<=8(t-1)delta,
    Gamma_T(g)<=5+8t delta<=7<=7I(g)  (t>=4).

Indeed source q1 has mean 1/2, control nonempty mass3/4 and u marginal1/2. The outer root adds2Var(g), control join adds3/2, u/V join adds1, and Y cells contribute W_Y(h). For a point mask Var(h)=4delta(1-delta); each of t-1 binary Y cells costs at most2Var(h). The displayed upper bound follows, and t2^-t decreases for t>=4.

The accepted mask cost W(q)<=12I(q) is still valid. Nevertheless

    [7I(g)+12I(q)] / I(f)
       = [19+26t delta]/[(3t+1)delta] -> infinity.

There is no finite source-budget-to-final-influence factor for this fully exposed block, even with an explicitly paid source reference and nonconstant actual final core. The specific suggested continuation factor 2K+12=26 already fails at t=5. This refutes only dropping the residual privacy assumption from the sufficient transfer, not A069's stated result.

Nor is this a Boolean FEI counterexample: f is a disjoint product of two point masks and H(f)<=4I(f). To prove the point-mask bound, for m>=2 let rho=2^-m and alpha=4rho(1-rho). Its spectral entropy is h2(alpha)+alpha log2(2^m-1). Using h2(alpha)<=alpha log2(e/alpha), obtain H<=4rho[2m-2+log2(e)-log2(1-rho)]<=8m rho=4I. Here e<11/4<sqrt(8) gives log2(e)<3/2 and 1-rho>=3/4 gives -log2(1-rho)<=log2(4/3)<1/2. The elementary exponential bound follows from sum_{j=0}^5 1/j!=163/60 and the remaining geometric majorant 7/4320, whose sum is11743/4320<11/4. For m=1 the mask is a character and H=0. Entropy and influence add for disjoint Boolean products. Thus the unbounded ratio concerns the ancestral transfer bill, not H(f)/I(f). Root-bit Gamma(f)>=1 also prevents this fixed code from paying very small final influence without a different reference; that separate root convention is not the physical-budget obstruction's cause.

The exact signed conversion retains K I(g)-Gamma(g), K I(q)-W(q), and R_T-K R_I. No bank is erased. Constant-width privacy alone cannot pay a fully exposed canceled event; the next step needs a selected final reference or a once-owned source slack covering its destroyed-edge debit.

## 4. Normalized-real source guard

On X={x}, Z={z1,z2}, take g=sqrt(2)*1{x=+}, q=1-2*1{x=-,z1=+,z2=+}. Then E g^2=1 and gq=g, so the final is also normalized. Spectral Dirichlet influences are I(g)=I(gq)=1/2, while Boolean I(q)=3/4. The source-visible mask flip probability is theta=1/4. For K=M=1 the claimed Boolean edge factor would be5/3, but I(g)+I(q)=5/4>5/6=(5/3)I(gq). Zero source amplitude makes the mask edit invisible. Thus norm-one source independence and the same edge probability do not extend the actual-pivot comparison to real functions; its indispensable first step is the Boolean d in {0,1} and the t=p or1-p dichotomy.

The original degree-one singleton diagnostic remains a guard against universal spectral-influence-only real payments. Historical cyclic-law individual certificates remain unrecovered, not replayed and not proof dependencies. The pad-and-flip test is already met by the accepted all-set hierarchy at its specified scopes; no support-zero argument is used here.

## 5. First unsupported line and next exact target

For a source fully seeing an exclusive event, show that the actual final normalized reference can refund its canceled ancestral event using one unused source/child slack while retaining the complete nonconstant core reference. The fixed ancestral influence sum cannot be bounded by final influence as Section3 shows. In the partial-privacy theorem arbitrary source admission is still conditional on its paid Gamma, so full FEI and C019 physical stopping-tree ownership remain open.
