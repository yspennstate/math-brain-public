# Independent review of A057-CAPPED-RECENTERED-ACTIVATION-TREE-BANK@1

Verdict: ACCEPT_AT_STATED_SCOPE without substantive repair. Original contributor remains A057. This is a second independent physical-coefficient reconstruction after A058's accepted review, with a separate implementation, not a rerun of A057's code. A058's review was consumed at final board reconciliation; it supplied no repair. The theorem pays the capped positive outer erasure bank on fresh point activation trees. It does not pay arbitrary inner entropy, terminal entropy, or overlapping-control charges.

Let u be any Boolean sign on a finite uniform cube. Controls are r>=1 independent fresh uniform bits, p=2^-r, and F=1+A_r(u-1). A core-first physical tree may adapt its coordinate choice and stop early at constants. For a partial tree keep its actual activated terminal children. At a core node put m=E u, v=1-m^2, beta=hat u({i}), t=beta^2, d=Inf_i(u). Entropies are bits. The zero-variance and zero-t caps are zero.

The point indicator's control Fourier coefficients all have magnitude p. In the outer affine expansion 1-A_r+A_r y, the empty row's recentered amplitude is C=1-p+pm; each nonempty row is -p(1-m). Summing their exact multiplicities 2^r-1 independently reconstructs

    M(s)=Phi(C^2,p^2 s)+p(1-p)Phi((1-m)^2,s),
    Phi(a,b)=(a+b)h2(b/(a+b)).

The actual core coordinate erasure is p[B_i(u)-Phi(m^2,t)]+M(t). The removed empty pair is essential and can carry a negative recentered correction. The checker independently computes the parent spectrum and verifies this equality at reached core nodes. Child product Parseval gives t<=v; Boolean derivatives give |beta|<=d and t<=d. The positive-sector concavity bound gives M(t)<=min{M(v),(t/v)M(v)+pt log2(v/t)}, defining the source cap.

For amplitudes a,b>=0, Phi(a^2,b^2)<=2ab in bits. By homogeneity assume z=b/a<=1. The derivative of [(1+z^2)ln(1+z^2)-z^2 ln z^2]/(2z) has sign (z^2-1)ln(1+z^2)-z^2 ln z^2>=0: use ln(1+x)<=x and -ln x>=1-x. Its maximum is ln2 at z=1; divide by ln2. Also Phi(A,B)<=B log2(e(A+B)/B). These handle all zero endpoints by continuity.

Now C^2+p^2v=1-2p(1-p)(1-m)<=1. Apply the logarithmic inequality to the first term of M(v), and the amplitude inequality to its second term, then multiply by t/v and retain the cap's logarithm. This gives

    cap <= p^2 t[2r+1/ln2+log2(1/v)]
           +2p(1-p)(1-m)t/sqrt(v)+pt log2(v/t).

The middle term is <=4p(1-p)d since t/sqrt(v)<=|beta|. The variance logs combine exactly into pt log2(1/t)+p(1-p)t log2(v); the latter is nonpositive. The rarity estimate t log2(1/t)<=2|beta|/(e ln2)<=2d/(e ln2) follows by maximizing x ln(1/x). Hence

    cap <=4p(1-p)d+p^2(2r+1/ln2)t+[2/(e ln2)]pd.

Under a fair core reveal, m_plus=m+beta and m_minus=m-beta, so v-E v_child=t. On the same actual finite tree sum w t=V_drop and sum w d=Pi_I; no alternate tree or fair weight is introduced. Using t<=d yields exactly the source partial-prefix bound

    prefix <=[4p(1-p)+p^2/ln2+2p/(e ln2)]Pi_I+2rp^2 V_drop.

For complete constant-core leaves Pi_I=I(u), V_drop=Var(u), and Var(u)=(1-m)(1+m)<=2(1-m). Since p<=1/2 and 1/ln2<4, the prefix is <=K pI(u)+2rp(1-m), K=4+2/(e ln2). The variance account is conserved over the prefix; the declared control reserve is not reopened at each depth.

At a negative constant-core leaf the control suffix is an r-bit point defect; positive leaves are constant. For a point defect on s bits, let delta=2^(1-s). Its query influence is delta and erasure is Phi((1-delta)^2,delta^2)+2delta(1-delta). It is zero for s=1. For s>=2, set l=s-1 and use delta=2^-l to bound the erasure/influence ratio by 2+delta(2l+1/ln2-2)<=3, since 2l/2^l<=1 and 1/ln2<2. Thus the suffix costs <=3 times its own consumed influence. Negative leaves have total probability (1-m)/2, so expected suffix influence is rp(1-m). The combined price is

    prefix+suffix <=K p I(u)+5rp(1-m)<=K I(F),
    I(F)=pI(u)+rp(1-m).

The last comparison needs K>=5. Independently certified e and ln2 intervals give K in [5.061475690846085977066754714467,5.061475690846085977066754714470]. The certificate uses a factorial sum through 32 with explicit geometric tail for e, and the copied A091 rational atanh-series interval for ln2; no floating sign. Constants and exact rational endpoints are in out/CHECK.json.

The finite checker uses A091's prior direct centered-moment primitives, whose provenance is recorded, plus a new cached physical-tree/cap implementation. It verifies direct parent erasure splits, exact variance/influence telescopes, both interval cap branches, partial-prefix bounds, complete suffix prices and complete budgets on all frozen roots. It does not depend on A057's compressed sparse-bent helper or formulas for selected numerical examples. General quantifiers are covered by the analytic argument above; finite cases corroborate them. No repair is necessary, so the reviewer remains independent.

The first unsupported universal line is unchanged: payment of nonempty inner-decrement sums and actual terminal entropy for a universally admissible physical tree. An overlapping priority gate has different control coefficients and a single common reserve; applying this fresh activation theorem twice is not justified. OVERLAP_INTERFACE.md and out/OWNERSHIP.json expose that next ownership obligation rather than claiming its payment.
