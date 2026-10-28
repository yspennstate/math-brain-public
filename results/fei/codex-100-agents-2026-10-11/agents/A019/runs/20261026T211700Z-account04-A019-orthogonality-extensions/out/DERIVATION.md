# Unbounded adaptive mixed queries after compulsory source cleanup

This is the BALANCED hierarchy of A016 stage11, not the earlier A019 one-balanced hierarchy. Let k>=5,j>=5,rho=2^-k,E=g3(a,b,c)g3(a,d,e), G the product of j disjoint E blocks, mu=(5/8)^j<1/8. Put A=point_k(v)(1-G)/2, p=rho(1-mu)/2, h=chi_u off A and chi_q on A. Use exactly Qh=(Ph+delta_q)/2 and QF(e,T)=[Qh(Tcore)Pw(Tmask)+delta_empty(T)]/4 for each gate frequency, with the flat two-bit mask w of mean1/2. Keep original insertion debit U<5/8. Query q first. Any subsequent finite adaptive padding/source-coordinate tree is allowed, with all outcomes retained. At every admitted terminal erase all physically irrelevant remaining source coordinates; no padding/u/mask/gate query beyond the declared padding queries is required. References are literal marginals of the ORIGINAL QF throughout.

Use A016's finite block contract CE(Pg,R)<=4I(g) for EVERY cleaned restriction of E, where R is its ORIGINAL spectrum projected to essential coordinates. Tensor independence gives the same contract for every cleaned restricted G. This contract must be independently reproduced, not assumed from fixed-set averages.

At a terminal where the original padding point is still possible, write k' for remaining padding bits, r=2^-k', nu=E[g], a=r(1-nu)/2, P=Pg, R=the projected original G law. Let L replicate a source measure over all remaining padding/u frequencies. The ACTUAL and ORIGINAL core laws are

Pc=(1-2a)delta_u+(r^2/4)L[P+(1-2nu)delta_empty],
Qc=(1-2p)delta_u/2+delta_empty/2+(rho*r/8)L[R+(1-2mu)delta_empty].

The formula for Pc is an algebraic identity; when a>1/2 its principal coefficient is negative and must NOT be used as a latent mixture. Instead keep the actual principal/empty atoms together, whose total true mass is at most1. Their reference masses are at least(1-2p)/2>1/4 and1/2; their total CE is at most2.

At nonempty source frequency T, every padding/u row has true mass r^2 P(T)/4 and reference mass rho*r R(T)/8. Summing the 2/r replicas gives EXACT nonempty-source cost

(r/2)[(1-nu^2)(k+k'+3)+sum_(T nonempty)P(T)log2(1/R(T))].

At empty source frequency, every row except principal/empty has actual mass r^2(1-nu)^2/4 and reference mass at least rho*r*(1-2mu)/8>3rho*r/32. Its log cost is less than k+k'+4. The total mass of these rows and all nonempty-source rows is at most

(r/2)[(1-nu^2)+(1-nu)^2]=r(1-nu)<=2r.

Thus, with all coincident rows and reference-only rows retained,

CE(Pc,Qc)<=2+2r(k+k'+4)+(r/2)CE(P,R).

If a queried padding bit falsifies the point, put r=0 for the conditional probability of that ORIGINAL point; actual core is chi_u and its CE is at most2 by the same original principal reference floor. No original reference is replaced by a point mass.

The complete gate/data mixture bound gives CE_F<=CE_core/2+3. Physical edges give

4I_F=6+2(k'-1)a+r I(g)-sigma*a >=6-3r+r I(g)

for either q sign sigma, since0<=a<=r and k'>=0. Therefore every cleaned terminal satisfies

W=4I_F-CE_F-U >=2-U-r(k+k'+7)+r[I(g)-CE(P,R)/4] >=2-U-r(k+k'+7).

All adaptation is handled by the ORIGINAL padding event V: r=Pr(V|physical leaf), including0 on falsified leaves. The leaf cylinders partition the original uniform space, hence E r=rho and E(r k')<=k*rho. This remains true when source choices, queried coordinate sets, cleanup, and stopping depend on the full history. Consequently

E W >=2-U-(2k+7)rho > 11/8-(2k+7)2^-k >=27/32

for ALL k>=5, every j>=5, and EVERY such finite adaptive mixed tree. The final inequality follows since(2k+7)2^-k decreases for k>=5 and equals17/32 at k5.

This removes A016's fixed bound of nine further source queries. There is no bound on the number of source queries except the finite original dimension; it may grow with j. Cleanup is compulsory at admitted terminals; ghosts without cleanup are excluded by the independently established A019 counterexample. This is an expected frontier theorem, not pointwise terminal eligibility. It uses a specific influence-priced ORIGINAL source and does not supply arbitrary indecomposable cores or a universal C019 stopping rule. Independent review remains required.

## Original debit and source eligibility

For completeness retain the literal A016 insertion debit

U=Lq+Econv,
Lq=log2((9+p^2)/8)/2+(p^2/8)log2((9+p^2)/(1+p^2)),
Econv=(1+p^2/4)[1-h2((1+p/2)^2/(2(1+p^2/4)))]/2.

Writing z=p/[2(1+p^2/4)], the last entropy deficit is D(Bern(1/2+z)||Bern(1/2)). The elementary log inequality ln x<=x-1 gives D<=4z^2/ln2. Since ln2>1/2, Econv<=p^2/[2(1+p^2/4)ln2]<=p^2. Also Lq<1/2+p^2/2, as its first log ratio is<2 and its second<16. Thus0<=U<1/2+3p^2/2<5/8 for p<1/64. We use this as an upper bound on the SAME booked U, not a second debit or a reference reset.

The original root is actually eligible. The rare part of its balanced core law has total mass2p, seed distribution [PG+(1-2mu)delta]/[2(1-mu)], and k padding/u frequency labels. Latent coding gives H(h)<=h2(2p)+2p(k+2)+(rho/2)H(G). Since Qh>=Ph/2, CEh<=H(h)+1, and the complete outer code has CE_F<=CEh/2+3. Physical edges give4I_root=6+2kp+rho I(G). The original block certificate gives H(G)<=4I(G). Therefore

4I_root-CE_root >=5/2+(k-2)p-h2(2p)/2+rho[I(G)-H(G)/4]>19/8.

Here p<1/64, h2(1/32)<1/4 follows exactly from31^31>2^152, and k>=5. No ineligible root or newly supplied terminal is hidden in the theorem.

## Boundary and failure audit

The finite certificates use all243 partial physical assignments of the five-bit block, not sampled functions. Every cleaned constant state has R(empty)=1 and zero influence. If cleanup is omitted, fix the shared bit a=1 and leave b,c,d,e unqueried: actual E=1, while its projected ORIGINAL reference has R(empty)=(5/8)^2+(3/8)^2=17/32. Its CE=log2(32/17)>0 but influence0. Thus the required clean-source contract fails on an actual restriction if this hypothesis is removed. The old A019 ghost-prefix family supplies the stronger all-outcome unbounded-debt obstruction; it belongs to a different original hierarchy and no numerical reserve is transplanted here.

The mu<1/8 hypothesis supplies the strictly positive vacuum floor; normalization of the two core laws and all coincident atoms is essential. The k>=5 hypothesis is used in the uniform27/32 estimate and initial eligibility. The fresh u,gate,mask coordinates remain unqueried, as required by the physical influence identity. The posterior identity uses full finite cylinder partitions; no rare sibling is discarded and no exchange of an infinite limit is made. Individual cleaned mixed leaves may still have negative reserve. The theorem controls their complete expected account.

The exact inequality31^31>2^152 and block integer products are arithmetic certificates. The two independent implementations use direct characters and butterfly Walsh respectively; they are representations independent within one author session, not external peer review. No literature-priority claim or Lean certification is asserted.
