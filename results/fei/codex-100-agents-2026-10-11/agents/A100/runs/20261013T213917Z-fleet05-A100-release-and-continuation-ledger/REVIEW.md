# Source-bound independent reviews and correction decisions

Reviewer: A100, fleet05, stream B20. No repair was supplied to the statements accepted below; this is independent reconstruction of source-complete claims, not a new universal theorem. Full FEI is OPEN.

## A051-PROPER-BLOCK-DESCENT-SQUEEZE v1: HOLDS at stated scope

Source: A051 run 20261011T233123Z, UNIVERSAL_DESCENT_SQUEEZE.md and original claim. Let phi(f) be the least actual entropy decrement per removed influence over nonempty proper physical blocks. Let M_n be the maximum H/I of actual nonconstant n-bit signs, and K_desc(n) the maximum phi, n>=2.

Independent reconstruction starts from a maximizing actual truth table, which exists because the domain is finite. Its root has H=M_n I; every restriction, padded back to n bits, has H(child)<=M_n I(child). For any proper block, the exact physical influence decomposition then gives Delta_A H>=M_n I_A. Therefore phi of this maximizer is >=M_n and K_desc(n)>=M_n. This uses M_n as the exact finite maximum, not an unproved dimension-independent FEI hypothesis.

For arbitrary f, leave unrevealed a coordinate with minimum influence and reveal its complement. The resulting leaves have at most one physical bit and hence spectral entropy zero: a one-bit sign is a constant or a signed character. Thus this block has Delta_A H=H(f), I_A=I(f)-min_i Inf_i(f)>0, and phi(f)<=H(f)/(I-min Inf_i)<=n(H/I)/(n-1). Maximizing proves the upper squeeze. Dummy coordinates cause no difficulty: leaving a dummy coordinate gives I_A=I. As M_n increases by dummy padding, M_n<=K_desc(n)<=n M_n/(n-1) implies lim K_desc(n)=sup M_n in the extended reals. This proves the source's universal analytic claim in full without relying on its finite NAND census.

Decision: independently ACCEPT_AT_STATED_SCOPE for the squeeze only. A051-NAND-SEED-DESCENT-CERTIFICATES is not accepted by this review. B11's open uniform proper-block target is FEI-equivalent in finiteness. The finite proper-block optimum need not equal the coordinate erasure optimum or the FEI optimum at the same constant. B06 R1 remains the source for the conditional-erasure-to-singleton implication; the sharper A051 squeeze concerns actual entropy decrement and is kept under its original ID.

## A097-B05-COMPATIBLE-REFERENCE-CERTIFICATE v1: partial acceptance

Sources: A097 run 20261012T005449Z DERIVATION.md and claim; earlier compatible-transfer version and A098's independently reconstructed terminal-KL ceiling subclaim. The tree and reference laws remain exactly those of the source. We accept the all-even-k erasure bound, physical budget, seed-reference costs, and uniform-leaf chi-square/credit ceiling subclaims. The full A097 compatible-transfer theorem, including its general block-information bound and all listed dependencies, is not independently accepted here.

Use 0/1 labels for fair physical inputs. Write delta=2^-k, eta=2^(-k/2), r=2k, p=2^-r, c=1-eta+delta. Direct quadratic Walsh factorization gives each coefficient of b_k magnitude eta, with sign imbalance eta under uniform frequency index. The zero-point flip subtracts 2delta from every coefficient. Physical edges give I(b)=k/2 and I(b')=k/2+2kdelta. The selector between them disagrees on precisely one core input, hence selector influence delta. At a suffix with s controls, control influence is u_s c with u_s=2^-s; its physical reach is p/u_s. Therefore I_removed=p(rc+delta), I_terminal=p(k/2+kdelta). No seed influence enters the removed budget.

The residual-empty control packet has masses (1-u_s c)^2 and u_s^2 c^2; all other packets have equal membership masses and combined mass 2u_s c-2u_s^2 c^2. Its conditional erasure is consequently B_s=phi((1-u_s c)^2,u_s^2 c^2)+2u_s c-2u_s^2 c^2. The actual selector erasure B_sel is computed from its signed core spectrum, and B_sel<=h2(delta)<=delta[k+1/ln2]. Hence B_tree/p=B_sel+sum_s B_s/u_s.

For a+b<=1, phi(a,b)<=b log2(1/b)+b/ln2: bound a log2(1+b/a)<=b/ln2 and the other contribution by b log2(1/b), since a+b<=1. It follows that B_s/u_s<=2c+u_s c^2[1/ln2+2s-2log2 c]. Summing u_s<=1 and s u_s<=2, and using c>=3/4 and c<1, gives

    B_tree/p<=2rc+C0+delta[k+1/ln2],
    C0=1/ln2+4+2log2(4/3)<13/2.

The last inequality has a rational proof: ln2>56/81>2/3, and (4/3)^12<2^5, so C0<3/2+4+5/6=19/3<13/2. For even k>=6, rc>=3k/2>=9, and delta(k+3/2)<=15/128; the latter expression decreases with k>=6. Therefore B_tree/I_removed<2+(13/2+15/128)/9<3. The fresh exact rational-logarithmic certificates at k=2,4 prove the two remaining cases. The lower estimate B_s/u_s>=2c-2u_s c^2 yields B_tree/p>=2rc-2, so B_tree/I_removed tends to 2.

Both uniform seed references have complete cost k. This is <=2I(b) and <=2I(b'), and constant leaves have zero cost. The perturbed bent law satisfies P_b'(T)=delta[1-4 sigma_T eta+4delta]. Since E_uniform sigma_T=eta, expanding the square gives exactly chi-square(P_b',uniform)=16delta(1-delta). Gibbs with ln t<=t-1 yields D_2(P_b'||uniform)<=16delta(1-delta)/ln2. The already reviewed A098 terminal-slack ceiling gives

    0<=K_tree<=p D_2(P_b'||uniform)/2,
    K_tree/I_removed<=8delta(1-delta)/[(rc+delta)ln2].

Thus the prescribed cheap uniform references have asymptotically negligible credit and the corrected ratio also tends to 2. Exact leaf references induce the exact compatible root law and zero credit; this follows from linearity of the compatible averaging and shared true spectral kernel, not from a numerical equality test.

The independent implementation uses integer Walsh spectra for the cores at k=2,4,6,8 and the full roots at k=2,4, direct physical edge influence, independently grouped complete root references, and rigorously enclosed rational logarithms. All 8,544 completed assertions pass. Its eight erasure/credit/residual intervals intersect the upstream certified enclosures. The KL identity discrepancy enclosing zero is only a finite consistency check; the terminal-slack ceiling used above has its own accepted analytic source. We do not turn interval overlap into an equality proof.

Decision: ACCEPT_ERASURE_AND_TERMINAL_SLACK_SUBCLAIMS_ONLY. The complete-reference FEI corollary remains conditional on the full A097 transfer version. The already-known B05 bounded-ratio family is a closed calibration; repeating its k-grid cannot establish the arbitrary-seed or overlapping-control payment.

## A021-UNIFORM-RARE-CORE-EXPANSION v1: ERROR in its remainder component

Actual Boolean witness: activate a balanced dictator by one fair control, equivalently the two-bit sign with values (1,1,1,-1). Its four squared coefficients are 1/4, so H=2 exactly and I=1. Here q=1/2, t=k=1, H(seed)=0. The claimed expansion polynomial gives 3/2+1/(4ln2), so the actual remainder is

    R(1/2)=1/2-1/(4ln2)>31/224>0,

because ln2>56/81. This directly refutes the exact v1 assertion R<=0 with no floating entropy evaluation. Coefficientwise multiplication of -2(1-q)^2 log2(1-q) gives the positive tail 4/(ln2) sum_{j>=3}q^j/[j(j-1)(j-2)], as recorded in A021 v2. Consequently the decrement remainder R(u)-R(2u)/2 is negative, not positive. The old claim cannot remain fully accepted. A023's and A087's old sign approvals are retracted/narrowed; A087 independently accepts corrected v2. The separate exact spectrum, limiting-ratio arguments and control-first KL ledger survive. A100's previous accepted list must replace the v1 sign package with this source-bound correction; preserve the old run unchanged.

## A096 sign and minimum-coordinate interpretation

A096's formal singleton tax has always been J-M<=tau. Its report inference is repaired by the saved corrigendum: M+H(X|T)>=h2(delta) implies J<=tau+M. A090 accepted only this singleton theorem, with its endpoint lower witness reconstructed directly; the general fixed-pair theorem is not accepted through that review.

For any nonconstant actual f, over relevant coordinates, min_i B_i/Inf_i<=sum_i B_i/sum_i Inf_i=B/I<=H/I. Hence on a family with H/I<=C, the minimum cannot diverge. This class check calibrates a chosen rule and does not test a universal unbounded-ratio counterfamily. The applicable implication uses the same actual function and ordinary physical influence; it says nothing about a fixed chosen coordinate, which may have a large ratio. Finite f5/f6 violations of the old Kstar constant remain genuine scoped certificates, not an FEI disproof.
# Additional release objection: A066 block-tree scope

A088's stage2 audit distinguishes the valid finite block heat identity from the paid singleton-query telescope. The serialized A066-POSITIVE-RESTRICTION-HEAT-LEDGER v1 does not retain that qualifier. An unrestricted physical stopping-tree reading is false.

Independently take the Boolean point defect f=1-2*indicator(all plus) on n=128 coordinates and query the entire block once. Each nonempty Fourier mass is 4/2^(2n); there are 2^n-1 such atoms. All leaves are constants, no nonempty residual context remains, and C_B^+=0. Its physical influence is n*2^(1-n). Thus (C_B^++ell_B)/I=4*(n-1)/n*(1-2^-n)*ln2. The first three positive terms of ln2=2*sum_{j>=0}(1/3)^(2j+1)/(2j+1) give a rational lower bound for this ratio exceeding 11/4. Since e>1+1+1/2+1/6=8/3, the alleged coefficient 2+2/e is strictly below 11/4. This exact Boolean countercertificate is saved in out/A066_BLOCK_SCOPE_INDEPENDENT.json; no 128-bit truth table is enumerated.

Full acceptance of the unqualified bundle is withheld. Retain the valid block identity, singleton inequalities and singleton-query tree telescope, together with A088's separately reviewed constant reduction. No corrected source version is supplied here, and this scope diagnostic is not an independent review of every bundled subclaim. The separately accepted heat-entropy identity, no-envelope result and family calibration do not use the false broad block-tree clause.
