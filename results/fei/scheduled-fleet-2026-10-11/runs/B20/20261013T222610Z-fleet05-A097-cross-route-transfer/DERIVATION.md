# Collision calibration transfers the complete reference

All costs are in bits. Let G(s,X), H(s,Y) be Boolean signs, where s is one shared fair physical bit, X,Y are disjoint private uniform blocks, and z is a fresh fair selector. Blocks may be empty. Set F=(G+H)/2+z(G-H)/2. Supply any normalized references R_G,R_H positive on the respective true Fourier supports, with finite costs c_G,c_H. Nothing here constructs these arbitrary seed references at bounded cost.

## 1. Calibration, including both collision atoms

The intersection of the two embedded Fourier supports is contained in C={empty,{s}}. Write a=(Ghat(empty),Ghat({s})), b=(Hhat(empty),Hhat({s})), v_G=1-||a||_2^2, v_H=1-||b||_2^2. Set R_G^c(T)=P_G(T) separately at both T in C; on its complement multiply R_G by v_G/R_G(C-complement). If v_G=0 set the complement to zero. The denominator is positive whenever v_G>0 by support positivity. Define R_H^c analogously. These references remain normalized and positive on true support.

The categorical KL chain rule, for the three cells {empty},{s},C-complement, gives

    c_G-c_G^c = D((a_0^2,a_1^2,v_G)||(R_G(0),R_G(s),R_G(C-complement))) >= 0,

and the analogous H equality. Conditional complement debt is retained. Calibrating only the empty atom would leave an unpaid posterior mismatch at {s}.

## 2. Substitute into the compatible-reference transfer

Embed references in the actual union cube, r(T)=(R_G^c(T)+R_H^c(T))/2, q(T)=(P_G(T)+P_H(T))/2. At q(T)>0 put

    K(0|T)=(Ghat(T)+Hhat(T))^2/(4q(T)),
    K(1|T)=(Ghat(T)-Hhat(T))^2/(4q(T)), Q(U,T)=r(T)K(U|T).

At q=0 choose the fixed kernel K(0|T)=1. Q is a single normalized complete reference, fixed before sampling the spectral output. The child posterior agrees under true and reference laws on C because BOTH atoms were calibrated; outside C every true nonzero T identifies the unique child. Thus the A097 compatible-reference posterior KL kappa is exactly zero, not discarded. Direct KL expansion, also independent of the original telescope, proves

    D(P_F||Q) = (D(P_G||R_G^c)+D(P_H||R_H^c))/2,
    CE(P_F,Q) = (c_G^c+c_H^c)/2 + Delta,
    Delta=H(F)-(H(G)+H(H))/2=B_z+J_z.

All terminal bills and their conditional normalizers remain. On an off-support reference fiber the chosen normalized kernel preserves its mass; that mass is never silently deleted.

## 3. Pay the collision erasure with the one owned selector

Conditional means m_G(+),m_G(-) lie in [-1,1], and a=((m_G(+)+m_G(-))/2,(m_G(+)-m_G(-))/2). Hence ||a||_1=max(|m_G(+)|,|m_G(-)|)<=1; similarly ||b||_1<=1. Independence of X,Y conditional on s gives

    d=Inf_z(F)=(1-<a,b>)/2.

Outside C the selector erasure packet is fair, so B_out=(v_G+v_H)/2<=2d, by ||a-b||_2^2>=0. At a collision T the two spectral masses are A=(a_T+b_T)^2/4 and B=(a_T-b_T)^2/4. The Renyi-one-half bound followed by ln(1+x)<=x yields phi(A,B)<=2sqrt(AB)/ln2=|a_T^2-b_T^2|/(2ln2). This elementary packet bound is the specific lemma transferred from A086's disjoint interface to its formerly missing NONEMPTY collision atom.

Conditional means give the sharper needed estimate. For real x,y in [-1,1], |x-y|<=1-xy, since (1-xy)^2-(x-y)^2=(1-x^2)(1-y^2)>=0. Therefore every shared-only Fourier coordinate satisfies

    |a_T-b_T|<=E_s |m_G(s)-m_H(s)|<=E_s[1-m_G(s)m_H(s)]=2d.

Using ||a+b||_1<=2 gives sum_C |a_T^2-b_T^2|<=||a-b||_infinity ||a+b||_1<=4d. Consequently B_C<=2d/ln2 and B_z<=(2+2/ln2)d. This replaces the initial weaker l1-distance estimate, without invoking an unjustified Euclidean-sphere extension.

For completeness, re-prove the universal scalar JS payment. At each residual fiber write u=(Ghat+Hhat)/2, v=(Ghat-Hhat)/2, q=u^2+v^2, t=2|uv|/q. Its JS contribution is q D(t)/ln2, where D(t)=((1+t)ln(1+t)+(1-t)ln(1-t))/2. Since atanh(t)<=t/sqrt(1-t^2), integration gives D(t)<=1-sqrt(1-t^2). The contribution is <=2 min(u^2,v^2)/ln2<=2v^2/ln2. Sum v^2=d to obtain J_z<=2d/ln2. Endpoints follow continuously. Therefore

    CE(P_F,Q)<=(c_G^c+c_H^c)/2+(2+4/ln2) Inf_z(F).

Each original data influence, INCLUDING s, is the average of the two child influences: conditioning on z proves

    I(F)=(I(G)+I(H))/2+Inf_z(F).

The shared bit is counted once in the actual root budget; no separate s-reset or s-query account was introduced. If c_G<=K_G I(G) and c_H<=K_H I(H), the conditional reference result is CE(P_F,Q)<=max(K_G,K_H,2+4/ln2)I(F). The supplied core bounds are hypotheses. Ideal reference costs are used; a one-symbol prefix code's additive rounding bit is separate.

## 4. Scope and honest first unpaid line

The same proof works for a larger shared block when both conditional-mean Fourier vectors on that block have l1 norm <=1, calibrating every shared-only atom separately. One shared bit guarantees this hypothesis; multiple shared bits generally do not. More generally, with t shared bits, Cauchy-Schwarz gives ||a+b||_1<=2*2^(t/2), yielding the explicit coefficient 2+(2*2^(t/2)+2)/ln2. This is a dimension-dependent transfer, not a universal solution. For example the quadratic bent sign on even k shared bits has conditional-mean spectral l1 norm 2^(k/2). BOUNDARY.md proves that no absolute selector-only constant can replace the growing coefficient for unrestricted overlap. The first unsupported universal line is paying excess collision erasure from a named, nonreused terminal core reserve, together with constructing/pay-compensating arbitrary terminal references. No universal FEI constant changes. Priority shared-control gates and unequal shared data are different structures; this theorem closes the one-shared-data selector admission requested by A086.
