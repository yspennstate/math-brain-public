# Independent reconstruction: A046 rare-row lemma only

Source: A046 run 20261014T041928Z, REPORT.md section "complete derivation", claim A046-SEPARATOR-LAYER-CUTOFF-RESERVE v2. Verdict HOLDS for its constant/nonconstant moment identities and all-width rare-row assertion B_i/d_i<1781/480 when e<=1/8. This is an independent proof reconstruction by A024, not acceptance of A046's entire reserve, prescribed-reference, or interleaved-history claims. No repair was supplied.

Let G=1-WUV(1-g), H=1-(U OR V)(1-g), with disjoint point events and balanced Boolean g. Put eta=E WUV, beta=E(U OR V), e=beta-eta, Delta=H-G. Since the events are nested and Pr[g=-1]=1/2, EG=1-eta, EH=1-beta, E GH=1-e. Thus E Delta=-e, E Delta^2=2e and E G Delta=-e. Removing only the full constant Fourier row gives

    sum_nonconstant Ghat^2=2eta-eta^2,
    sum_nonconstant Ghat Deltahat=-eta e,
    sum_nonconstant Deltahat^2=2e-e^2.

At residual point density rho the queried coefficients are u=Ghat+rho Deltahat/2, v=-rho Deltahat/2. Hence q_*=sum_nonconstant(u^2+v^2)=2eta-eta^2-rho eta e+rho^2 e(1-e/2), and b_*=sum_nonconstant v^2=rho^2 e(2-e)/4. These identities depend on actual Boolean product expectations, not on independence of Fourier probabilities.

The residual-selector nonempty rows have equal squared queried coefficients and contribute 2(1-rho)d, d=rho e/2. The full constant row is L(1-eta-d,d). Concavity of binary entropy and h2(x)<=x log2(euler/x) give the nonconstant contribution <=b_* log2(euler q_*/b_*). Since q_*<=2eta+rho^2 e, b_*/d<=rho, and q_*/b_*<=4(1+2theta/rho^2)/(2-e), theta=eta/e, division by d yields

    B/d <=2+rho log2(euler/(2-e))
             +rho log2(1+2theta/rho^2)+d log2(euler/d^2).

For point probabilities q,r<=1/2 and event W of probability <=1/2, put z=sqrt(qr)<=1/2. Then eta<=z^2/2 and e=q+r-qr-eta>=2z-(3/2)z^2>=(5/4)z; consequently theta<=8e/25. This is where the source's compatible-point geometry is essential; it fails for an arbitrary high-contrast controller.

For e<=1/8, Euler's number <11/4 and 1/ln2<3/2 suffice. The first variable term is <2/3 because (22/15)^3<4. The second is <=(6/5)sqrt(e)<9/20, using ln(1+x^2)<=x for x>=0 and (6/5)^2/8<(9/20)^2. The last is <19/32: d<=1/16, d log2(euler/d^2) increases on that interval, and 704^2<2^19. Their sum with 2 is exactly 1781/480<4. The elementary constants are justified without decimals: euler=sum 1/j! <8/3+5/96<11/4, and ln2=2sum_{j>=0}(1/3)^(2j+1)/(2j+1)>2/3.

This independently closes the claimed rare-row scope and explains why A046's paid compatible controller does not conflict with A024's lifted tensor-selector obstruction. Its other cutoff/owned-drift and general-controller conclusions are not accepted by this review. The true universal obstruction here is transfer of mixed bad pivot mass, not a contradiction of the rare-row calculation.
