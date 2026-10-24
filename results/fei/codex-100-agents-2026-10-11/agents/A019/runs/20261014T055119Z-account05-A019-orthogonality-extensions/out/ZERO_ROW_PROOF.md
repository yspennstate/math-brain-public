Use the same supplied nonlinear-mask reference Q_s at parent and both children. For every Boolean core h_v let Q_v be its normalized complete core reference, c_v its cost, beta_v its mean. On F_v=1 at x0 and h_v*s at x1 the physical-label mixture reference has exactly CE_v=c_v/2+c_s/2+Psi(beta_v*sigma)-D_v, where sigma=E s and

D_v=(1+beta_v^2*sigma^2)/2 * KL_Ber(beta_v^2*sigma^2/(1+beta_v^2*sigma^2) || Q_v(empty)Q_s(empty)/(1+Q_v(empty)Q_s(empty))).

At a true core query, define Q_parent by the actual parent queried-frequency conditional times (Q_0+Q_1)/2 on the unqueried private data. This lift is normalized. On zero true data rows its conditional is arbitrary; choose the queried frequency ABSENT. If both children are balanced, their empty squared coefficients and the parent empty query-row mass are zero. The convention then gives Q_parent(empty)=[Q_0(empty)+Q_1(empty)]/2.

All three beta values are zero, so D_v=(1/2)log2(1+Q_v(empty)Q_s(empty)). Concavity of log(1+t) proves (D_0+D_1)/2<=D_parent. The core-query KL refund D_core=[KL(P_0||Q_0)+KL(P_1||Q_1)]/2-KL(P_parent||Q_parent) is nonnegative by log-sum. Thus the net activation debt Lambda=(D_0+D_1)/2-D_parent-D_core/2 is NONPOSITIVE. Both inherited children stay nonconstant whenever balanced. The complete costs satisfy

CE_parent - (CE_child0+CE_child1)/2 <= (H(h_parent)-(H(h_0)+H(h_1))/2)/2.

This uniform signed bound holds without any lower bound on query disagreement, with arbitrary supplied finite-cost references, and with a nonconstant fallback h_v*s. It is conditional on preserving two balanced child cores and on the zero-row convention. It does not certify their entropy decrement or terminal CE from influence.

The convention cannot be left unspecified. For every k>=1 let h0=chi_u, h1=chi_u*(-1)^1_(v=0) on one u bit and k v bits, and expose q selecting h0/h1. Both children are balanced and nonconstant, disagreement2^-k. Give both children Q_b=(P_b+delta_empty)/2. On positive true parent rows the conditional core lift gives Q_parent=P_parent/2. The sole unqueried-empty row has reference mass1/2 and zero true mass; splitting it equally over absent/present query gives Q_parent(empty)=1/4. Each core KL is1 bit, so D_core=0.

With a point-defect two-bit mask, true mask reference has Q_s(empty)=1/4. The child activation refunds are D_b=(1/2)log2(9/8), but parent D_parent=(1/2)log2(17/16). Hence Lambda=(1/2)log2(18/17)>0, independent of k. Lambda/disagreement tends to infinity. The supplied core references are rate4 eligible: the inherited character contributes I=1 and H=0, while the rare point phase has H<=4I, so H+1<=4I for parent and children, leaving at least3 bits core slack. This is a reference-transport obstruction, not an FEI disproof; its actual unused half-branch core reserve easily pays the constant debt.

Using the absent-query convention instead makes Q_parent(empty)=1/2, D_parent=D_children, and Lambda=0 for this same sparse family. Thus the repair acts on reference-only rows and retains every true terminal cost, rather than resetting to an unknown exact core reference.
