# Independent reconstruction of the small-padding source-first continuation

This is a scoped review of A094-SMALL-PADDING-POSITIVE-SOURCE-PATH-PAYMENT@1, statement SHA256 6f875d0de8dc2dbbdcda33d02c52f50ffaff391cfbde15e1f74919945ec520ec. No repair or new theorem version is supplied. Bits, physical uniform restrictions, and complete subprobability reference costs are used throughout. The standalone conversion/path theorem is reconstructed for every Boolean source. Owner corollaries remain conditional on their separately supplied original reserve. The special rate-four history is not independently reconstructed here from its original baseline.

## 1. Actual law and the complete target reference

Translate the edited point to zero and negate g if necessary, so g(0)=1. Let g have a source bits, m untouched dummy data bits, and one unqueried fair selector. Put epsilon=2^(-a-m), u=2^-m, and M=1/epsilon. Let A range over the N nonzero Walsh coefficients of g, embedded at dummy mask zero. Parseval and inversion give sum A^2=sum A=1; N<=2^a, and every nonzero |A|>=2^-a (a safe weaker lattice bound, including a=0).

The actual Boolean point edit F has selector-zero amplitudes A-epsilon on old masks and -epsilon elsewhere, and selector-one amplitude -epsilon everywhere. Its data law is q=A^2-2epsilon A+2epsilon^2 on old masks and 2epsilon^2 elsewhere. The prescribed normalized data reference is R=(P_g+3epsilon Uniform_M)/(1+3epsilon), hence R=(A^2+3epsilon^2)/(1+3epsilon) on old masks and 3epsilon^2/(1+3epsilon) elsewhere. Lift R by the TRUE conditional selector law. This is an actual complete reference, and its full divergence is Dfloor=D(q||R), with no missing selector term or normalizer. This argument includes constants and a=0.

## 2. A separate chi-square reconstruction

On an old mask,

 (q-R) = epsilon[3A^2-2A-6epsilon A-epsilon+6epsilon^2]/(1+3epsilon).

Let L=(sum A^-2)^(1/2)<=2^a sqrt(N). The triangle inequality in weighted Euclidean norm, using A^2+3epsilon^2>=A^2, yields

 sqrt(chi_old) <= epsilon/sqrt(1+3epsilon) [3+2sqrt(N)+6epsilon sqrt(N)+epsilon L+6epsilon^2 L]
 <= epsilon sqrt(N)/sqrt(1+3epsilon) [5+u+6(1+u)epsilon].

For 0<epsilon<=u<=1/8, write A0=5+u and B0=6(1+u). Direct polynomial subtraction gives

 3A0^2-2A0B0-B0^2u = 15-78u-81u^2-36u^3 >=501/128>0.

The polynomial decreases on this interval. It follows that (A0+B0 epsilon)^2<=A0^2(1+3epsilon), and chi_old<=(41/8)^2 N epsilon^2. On the complementary masks the exact chi-square contribution is

 chi_off=(M-N)epsilon^2(1-6epsilon)^2/[3(1+3epsilon)] <=epsilon/3.

Because N epsilon<=u, chi<=epsilon[(1681/64)u+1/3]. The identity ln2=2 sum_(j>=0) (1/3)^(2j+1)/(2j+1)>2/3 and Jensen/log(1+x)<x give, strictly,

 Dfloor < C(u)epsilon,   C(u)=1/2+(5043/128)u.                    (1)

The strict bound also follows when a model divergence vanishes; its right side is positive. No lower bound on a conversion from an arbitrary incoming reference is asserted.

## 3. Incoming mass penalties and every positive booking

For any actual finite-cost incoming subprobability Q of mass s in (0,1],

 CE(P,Q)=H(P)+D(P||Q/s)-log2(s)>=H(P).

Therefore its reached conversion to the normalized exact-source floor costs e=lambda[CE(P,Qfloor)-CE(P,Q)], with e^+<lambda C(u)epsilon. This pays the entire change, including any changed mass/vacuum and full selector distribution. Unlike the prior A001 quarter-tail mixture, this is an EXACT prescribed floor, not merely a target likelihood floor with the old vacuum fixed.

For a physical source query j, put p=erase_j P, r=erase_j Q, and P_b the two actual child spectra. The signed amplitude identity gives (P_0+P_1)/2=p. Define raw_b=r P_b/p when p>0 and raw_b=r when p=0. Then Z_0+Z_1=2s, and Q_b=s raw_b/Z_b retains mass s, including all reference-only atoms. Finite true-support coverage ensures Z_b>0. Direct likelihood disintegration gives

 D(P||Q)-average_b D(P_b||Q_b)
 =D(P||Q)-D(p||r)-average_b log2(Z_b/s)>=0.             (2)

The first difference is conditional KL and the last average is nonpositive by concavity. In particular normalization is paid, never free.

On the distinguished path after k source queries, reach is lambda*2^-k and epsilon_k=2^k epsilon. Entry and d matching-child resets therefore have total POSITIVE booking <(d+1)lambda C(u)epsilon. All nonmatching child references stop or continue with their actual inherited complete models. Constants at the end still retain their full CE; source influence is not renewed.

For nonconstant original g, cube edge connectivity gives I_g>=2a/2^a. For a>=1 and d<=a, (d+1)2^-a<=2a2^-a<=I_g. Thus all positive conversion costs together are <=lambda C(u)u I_g. Edge connectivity follows by induction on the two half cubes: if both restrictions are proper nonempty sets use their boundaries; if one is constant add at least one crossing edge; opposite constant halves have 2^(a-1)>=a crossings. The a=1 case is direct.

At every frontier the full signed ledger is H(F)+average_terminal D, equivalently accumulated FULL entropy decrement plus complete terminal CE. By (2), its change under queries is nonpositive; a reset adds its actual signed e. Discarding every negative reset credit only increases the ledger to a bill bounded by initial CE plus sum e^+. Every sibling, normalizer and old external liability remains. This is stronger accounting than a signed-only reset telescope, and does not identify erasure B with full decrement B+JS.

## 4. Conditional original-owner corollaries and their boundaries

Take as a separately reviewed input the A011 v2 actual original floor root, its supplied CE(P_g,R)<=C0 I_g, K=4C0+15 chosen once, and the A094/A086 reserve >=7I_g/8 after compatible old U<=(C0+37/8)I_g. This is a ROOT statement, not permission to undo an executed padding-first path. Since C(u)u increases with u,

 C(u)u<=5555/8192,  7/8-5555/8192=1613/8192.

The prospective source-first continuation above retains reserve >1613 I_g/8192 for m>=3. This reconstructs the general owner corollary CONDITIONAL on that original reserve. For the separately supplied rate-four two-reset baseline with remaining reserve >3/256 and actual child00 source -h4 at reach1/4, m>=5 gives C(u)<=7091/4096 and epsilon<=1/512. The entry plus four floors cost <35455/8388608 and leave >62849/8388608. That arithmetic and conversion implication are checked; the full preceding rate-four history has not received a second original-source reconstruction from A001 in this stage.

The exact checker independently uses integer FWHT, compressed complementary masks, rational log enclosures, and literal physical child truth tables. It checks BOTH the signed identity and the enlarged positive-booking bill, including incoming source masses 1 and 1/2 and all old U=69I_g/8. Finite certificates corroborate the implementation. Equations (1)-(2) and the reach/mincut argument prove the unbounded quantifiers; finite tables do not establish them.

## 5. Updated universal quantifier audit and first unsupported implication

The all-dimensional target remains: there exists a finite absolute C>=0 such that for every integer n>=0 and every f:{-1,1}^n->{-1,1}, sum_S fhat(S)^2 log2(1/fhat(S)^2)<=C sum_S |S| fhat(S)^2, with 0log(1/0)=0. Constants have H=I=0 and cannot be discarded from terminal references.

The earlier recovered 37-route manuscript inventory is retained byte-for-byte in out/RECOVERED_GAP_MAP.json. It separates genuine class theorems, equivalences, and one-way sufficient conditions. This stage adds an application audit, not another purported manuscript theorem or a regenerated route inventory.

Current source premise: ONE C0 must work for EVERY dimension and EVERY Boolean g, with some actual true-support-covering subprobability R_g whose COMPLETE CE is <=C0 I_g. Gibbs gives this premise => FEI(C0), and FEI(C0) supplies R_g=P_g. It is an exact equivalence at the same constant. A separate C_g for each seed, or a supplied source price for a threshold/product family, does not instantiate that universal premise.

A094 now supplies an actual compatible exact-floor source-first handoff for arbitrary SUPPLIED cores, improving the prior unresolved quarter-tail-floor compatibility question in that regime. A095's new nested-reset theorem, read as a source-specific conditional theorem, pays arbitrarily many resets along geometrically decreasing original reach. This does not price the original arbitrary source and does not cover many simultaneously active branches of comparable total reach. Neither theorem proves an initial capacity supplier.

The first unsupported universal line is therefore: 'For arbitrary g obtain the initial R_g at one absolute C0 without assuming FEI or an equivalent capacity bound.' Converting supplied C0 to an output rate 4C0+15 is a one-way preservation theorem, not a decreasing source-price recurrence. Reusing its output as its own source input neither provides a well-founded induction nor a contractive bound. Even the scalar attempted inequality C0>=4C0+15 has no nonnegative solution. This observation refutes that particular closure argument only; it does not rule out a new proof with a different potential or independently paid source.

Review disposition: HOLDS without repair for the standalone universal conversion/path bounds, and HOLDS conditional on the explicit original-reserve input for the source-first owner corollary. The special rate-four baseline is not independently accepted here as a full chain. Full FEI remains OPEN.
