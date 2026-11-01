# Source-bound Booleanity audit, stage 4

## A067-TWO-SUBCUBE-COMPLETE-CELL-REFERENCE v1: HOLDS

Source: A067 run 20261014T020120Z, CLAIMS.json and DERIVATION.md Sections 1-4. Review covers the complete reference, all finite controller widths, both edit operations, final influence payment, and the conditional terminal/degree-two corollaries. No statement or proof repair is supplied. The exact source hash is preserved in CLAIMS.json.

### Independent reconstruction of the common reference

Let P,Q be the fixed coordinate sets of the two controller subcubes, contract controls outside their union, and split into shared R, first-private U and second-private V. For XOR the function is g-2gAp-2gBq+4gABpq; for OR the last coefficient is 2gABpq. Thus each core Fourier row is a real linear combination c0+c1p+c2q+c12pq. This expansion explicitly retains signed interference; it is not a sum of squared edit spectra.

When assignments agree, a common assignment character removes every controller phase. Nonempty control subsets fall into four membership cells according to whether they meet U and V. Within each cell, the surviving summands are fixed: 00 has p,q,pq; 10 has p,pq; 01 has q,pq; 11 has pq. Excluding the empty subset from 00 isolates the c0 term. All row squared coefficients are constant on each cell.

When assignments conflict on D subset R, pq=0. In shared-only 00, the relative phase of p and q is (-1)^|S intersect D|. Split 00 by this parity; the other three cells need no split. Hence at most five cells suffice, with 11 unoccupied in the incompatible case. This establishes flatness for arbitrary real row amplitudes, not only Boolean core coefficients.

For every nonempty cell C, log2|C|<=2 average_C |S|. To prove this independently, start with uniform subsets on each unrestricted block: entropy equals block size and mean degree is half block size. Requiring a private block to be nonempty decreases its entropy and increases its mean degree; products preserve the inequality. A parity constraint on d>=2 shared bits leaves each marginal fair and removes one entropy bit. For d=1, that bit is fixed and contributes zero entropy but nonnegative degree. Removing the empty set from the even shared cell again decreases entropy and increases mean degree. Empty cells are omitted; singleton cells have zero cardinality charge.

Define R_tail(S)=1/(M|C(S)|) on EVERY nonempty subset, including zero-mass cells. Summing one cell at a time proves normalization. Use R_full(empty)=1-alpha and R_full(S)=alpha R_tail(S), the same law in every core row. For alpha=0 use the support-compatible limit; empty contracted blocks are trivial. Averaging its binary cross entropy over rows gives h2(alpha), because their tail probabilities average to alpha. Label payment is alpha log2 M. Actual conditional uniformity in each occupied cell and the proved cardinality inequality give total cardinality payment <=2I_Z. Gibbs' inequality therefore gives

    B_Z=H(S_Z|S_X)<=h2(alpha)+alpha log2 M+2I_Z.

There is no row-specific choice, renormalization, or discarded core entropy in this calculation. The label cost is bounded by log2 5, independent of both controller widths and fiber cardinality. This closes the explicit ambient-label loss audited last stage for this two-controller geometry.

### Final Boolean payment and terminal scope

Let a_x=P_Z(E_x), rho=P(E). Boolean g^2=1 and partial Parseval imply alpha=E_x[4a_x(1-a_x)]<=4rho. Indicator isoperimetry gives I_Z>=2E_x[a_x log2(1/a_x)]>=4rho because a_x<=1/4. Consequently alpha<=I_Z.

On a core edge the combined-mask mismatch probability p is at most a_x+a_x'<=1/2. The final sign is pivotal with probability p or 1-p, depending on the Boolean seed edge. Thus I_X(F)>=I_X(mask); control pivotal influence equals the mask control influence. Apply indicator isoperimetry to the whole final mask to get I_X+I_Z>=2rho log2(1/rho). For completeness, the isoperimetric inequality follows by splitting a set into densities a0,a1: the child-bound deficit is 2a[1-h2(t)] and the split edge pays at least |a0-a1|=2a|2t-1|; concavity h2(t)>=2min(t,1-t) completes induction.

Using alpha<=4rho<=1 and monotonicity of t log2(e/t),

    h2(alpha)<=4rho log2(e/(4rho))<=4rho log2(1/rho)
              <=2(I_X+I_Z).

Hence B_Z<=(4+log2 M)I_Z+2I_X. The previously accepted exact restriction identity Q_access=B_Z+J_Z and real-valued channel bound J_Z<=2I_Z/ln2 give K=4+log2 5+2/ln2, or 6+2/ln2 when compatible. The inequalities ln2>2/3 and log2 5<5/2 give K<19/2, and compatible K<9. All dimensions are proved analytically, not extrapolated from finite cases.

Every complete control reveal retains E_Z H(F_z), with E_Z I(F_z)=I_X. Previously independently accepted Boolean granularity gives H(F_z)<=2I(F_z)+2U(F_z). If each actual core satisfies U<=bI, the final coefficients are K on I_Z and 4+2b on I_X. If each actual core has Fourier degree <=2, every supported nonempty S has d(S)-|S|<=|S|, proving U<=I. Since K>6, this gives H<=KI. Original seed admission alone does not imply actual-leaf admission. No control-dependent seed is allowed.

Verdict HOLDS at the precise scope, no unsupported line within the theorem. The first unsupported universal line is payment of arbitrary retained core entropy by a complete reference, or a control-dependent source transfer retaining all banks. The theorem does not resolve either.

In particular, a bare induction hypothesis H(F_z)<=C I(F_z) gives only H(F)<=K I_Z+(C+2)I_X. It does not close the same C: the retained-core reserve 2I_X is added above the entire inherited C I_X terminal bill. A universal continuation needs an exclusive certified child surplus or a sharper access accounting that pays this reserve without renewing it. This is an unsupported universal extension, not a defect in the conditional U corollary.

### Minor prose inconsistency, not a theorem repair

Source Section 1 says the 11 cell has zero mass “for this family.” That is true for incompatible assignments; it is false generally for compatible assignments. The next source paragraph correctly includes pq in compatible 11, and its proof/reference already handles that occupied cell. For compatible p={z0=0,z1=0}, q={z0=0,z2=0}, A=B=g=1, XOR has final density 1/4 and nonzero 11 coefficients of magnitude 1/2. Our full domain contains this fixture. The erroneous explanatory sentence is not used for coverage, flatness, cardinality, or the theorem. No substantive repair is needed for the reviewed claim.

### Strong normalized-real diagnostics

Relax g to an arbitrary norm-one real seed, retain sign masks and all actual norm-one children, and use spectral Dirichlet energy. The signed row expansion, common flat-cell law, and row channel bound survive. The Boolean alpha specialization instead becomes E_x[g(x)^2*4a_x(1-a_x)]; final-edge pivot ownership also fails. Thus the flat-cell algebra is not by itself a use of full Boolean phase constraints. The genuine output-Boolean steps are g^2=1, the p versus 1-p pivotal comparison, and discrete leaf granularity.

For real core values (1,-1/3,5/3,1/3), all 1024 prescribed two-subcube flag/mode inputs yield 499 cap-admissible cases. Eight violate ownership. The first uses incompatible p=(0,0,*), q=(1,*,0), A=(0,1,0,0), B=(1,0,0,1), XOR, and gives final core energy 13/18<3/4 mask core influence. All 7984 checked real row-cell squares are flat. No bare access-bound violation was certified on this finite grid; the unrestricted real access extension remains undecided here.

The terminal and degree-two corollaries actually fail on the same norm-one real relaxation. Use g=(4095+128x)/4097, empty final edit, and any fixed compatible three-control subcubes with A=B=0. Its Fourier masses are 1-p,p, p=16384/16785409<1/1024. Its norm is one, degree one, U=0, and all actual children have norm one, but H/I=h2(p)/p>log2(1/p)>10>K. This refutes the real extensions, not the stated Boolean theorem or FEI.

## A070-MASK-REFUND-BOOLEANITY-AND-EDGE-CONVERSION-AUDIT v1: HOLDS

Source A070 run 20261014T005025Z, DERIVATION Sections 2-3 and exact original CLAIMS.json. Independently represent W_T(u) as sum of b_C times conditional variances. For Boolean signs, conditional independent copies disagree with half that variance, so W=2sum b_C P(D_C). Product disagreement is XOR, giving W(gq)=W(g)+W(q)-R_T. Ordinary physical edges similarly give I(gq)=I(g)+I(q)-R_I. Subtract the two exact identities to obtain the signed conversion equation for every real K. Neither refund can be omitted or converted into the other by positivity alone.

Direct independent resampling-pair enumeration under cells all,{c,u,v},{u,v} reconstructs q=(1-c)/2+(1+c)uv/2, g=q*y, f=y. It certifies Gamma(g)=11/2, Gamma(q)=5, Gamma(f)=3, R_T=13/2, R_I=3. The K=12 banks are 49/2,14,-59/2, totaling 9. The final nonconstant core is retained. This falsifies refund-alone conversion and illustrates why A067 requires g independent of controls; it is outside that theorem's hypothesis.

For the strong normalized-real product relaxation, u=(12+5x1)/13 has norm one and W=50/169. Its square renormalizes to (169+120x1)/sqrt(42961), with W=28800/42961>100/169. Exact positive integer gap 571100 proves failure of the real product subadditivity. The Boolean-specific variance/disagreement and XOR steps cannot follow from Parseval alone. The general real quadratic Gamma/projection identities themselves remain valid. Verdict HOLDS at all stated quantifiers, without repair; no acceptance of the full A069 decoder chain is newly asserted in this review.
