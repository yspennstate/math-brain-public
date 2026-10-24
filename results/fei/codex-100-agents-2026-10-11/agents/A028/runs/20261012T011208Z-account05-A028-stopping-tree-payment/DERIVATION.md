# Arbitrary control indicator checkpoint

Follow B06 v2: A027 owns partial-core exposure; this run replaces point controls by an arbitrary indicator on a disjoint physical control cube. Let a=1-2c, p=Pr(a=-1), delta=Pr(u=-1), V_a=4p(1-p), V_u=4delta(1-delta), and F=1+c(u-1). Use eta(t)=t log2(1/t) and phi(t)=eta((1-2t)^2).

The actual full control-first leaf partition has constant +1 leaves with probability 1-p and terminal u with probability p. Its queried influence is Q=delta I(a), reserved terminal influence pI(u), and Pi_H=H(F)-pH(u). Direct Fourier grouping gives

Hplus(F)=delta Hplus(a)+pHplus(u)+G(p,delta),
G=V_u eta(p^2)+(V_u V_a)/2+delta^2 V_a log2(1/delta^2),
Pi_H=delta Hplus(a)+G+phi(p delta)-p phi(delta).

The exceptional empty coefficient is fully retained. At p=1 the correction cancels exactly and Q=0.

Since phi''(t)=-16log2|1-2t|-24log2(e)>=-24log2(e), interpolation yields phi(p delta)-p phi(delta)<=3log2(e)delta^2 V_a. Also eta(p^2)<=log2(e)V_a/2. Therefore

Pi_H<=delta Hplus(a)+C0 delta V_a,
C0=2+2log2(e)+log2(e)/sqrt(e)<6.

To maximize the scalar remainder, use max_{0<=t<=1} t[log2(e)-2+2log2(1/t)]=log2(e)/sqrt(e).

If a has Hplus(a)<=T(I(a)-V_a), Pi_H<=max(T,C0)Q. If only ordinary H(a)<=K I(a) is known, Pi_H<=(K+C0)Q. With terminal H(u)<=L I(u), the full stopping ledger has constant max(T,C0,L), respectively max(K+C0,L). This is a leaf-partition payment, independent of the chosen complete exposure tree inside the control block.

For D=4p delta(1-p)(1-delta), G/D=2+2p log2(1/p)/(1-p)+2delta log2(1/delta)/(1-delta)<=2+4log2(e)<8. Moreover I(F)-Var(F)=delta[I(a)-V_a]+p[I(u)-V_u]+D. Thus the standard strengthened composition certificate is preserved under arbitrary finite disjoint-control conjunction nesting at constant max(T_a,T_u,2+4log2(e)). This connects controller certification to the terminal bill; it does not establish controller FEI universally.

Universal obstruction: taking u identically -1 makes F=a, Pi_H=H(a), Q=I(a). A fixed absolute control-only K for all controllers would prove full FEI. Taking p=1/2 and u to be a rare point defect makes Pi_H/(delta I(a)) tend to 4 even for a dictator controller, so a tax-free Pi_H<=delta H(a) claim is false. Exact all-dimensional certificates and source-bound metadata will be saved in REPORT.md.

Point-controller strengthening: Hplus(1-2A_r)<=6(I-Var) for every r>=1. For r>=2 this reduces to 2r-8+4p(r+2)>=0; r=2 is equality, r=3 positive, r>=4 immediate. Hence the NEW actual leaf-partition cost is Pi_H<=6Q for arbitrary unbalanced cores. This does not replace the old larger bound on the magnitude-mismatch PLUS linear upper bill.

Exact coefficient-four obstruction: dictator controller a on one bit, core u=D_2 on two bits gives p=1/2, delta=1/4, Pi_H=3-(9/8)log2(3), Q=1/4, and Pi_H/Q=12-(9/2)log2(3)>4 because 3^9<2^16. Both leaves are certified point defects or constants. No unbounded H/I family is claimed.
