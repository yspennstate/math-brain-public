# Stage 2: independently reconstructed coding interfaces

Verdicts: HOLDS at the original stated scope for A003-OPTIMIZED-FOREST-DEBT v1, A003-PARITY-DEFECT-COMPLETE-RESIDUAL v1, A007-SHARED-CORE-ROOT-CANCELLATION v1, B02-A008-DICTIONARY-QUOTIENT-CODE v1 and A012-HEREDITARY-ACTIVATION-ADMISSION v1. No original statement required repair. These local review records do not update shared registries. A006/A011 are not reopened: A012 contradicts a universal payment for the unchanged physical transcript, not A011's admitted theorem.

## A003: exact optimized-reference debt

For each spectral A, sum 2^-B(r) over a finite set of distinct actual runs. Its sum t_A is positive. Setting posterior pi_r=2^-B(r)/t_A gives E B-H=-log2 t_A+KL(posterior||pi), so -log2 t_A is the exact minimum. The prior-stage reconstruction of the original conditioned forest proves q(r)>=2^-c-Kref|A|-B(r), with c=Lambda+log2 Z. Summing distinct runs proves U(A)=2^-c-Kref|A| t_A<=Q_*(A). This remains valid if selected runs cover only spectral outputs; set U=0 elsewhere, or include further selected nonspectral runs. In either case sum U<=1, and U is positive wherever P^+ is positive.

Normalize U by its mass m>0. Generalized divergence is D(P^+||U)=D(P^+||U/m)-log2 m>=0. Directly expand log2 U=-c-Kref|A|+log2 t_A. Then

    vD(P^+||U)=-vH(P^+)+vc+Kref I-sum_A p_A log2 t_A.

Since H(f)=h2(v)+vH(P^+), this proves exactly

    h2(v)+Kref I+R_*=H(f)+vD(P^+||U).

The v=0 case is separate and never divides by v. The identity does not identify U with the true spectral law or assert a reverse FEI-to-forest implication. It isolates a shape debt in addition to a normalization debt. Distinct actual runs are essential for the subprobability step.

For the implication constants, a spectral binary edge with masses a=p_T,b=p_(T+i) contributes b log2(1+a/b) to L_i and a log2(1+b/a) to its nonnegative complement. The latter is <=b/ln2, with zero endpoints interpreted by continuity. Thus L<=B<=L+I/ln2. Chain rule gives B<=H. Aggregate B<=KI implies an available relevant i with B_i<=K I_i, and the actual restriction identity Delta_i=B_i+JS_i, JS_i<=2I_i/ln2, gives dimension induction to FEI(K+2/ln2). The signed L version gives FEI(K+3/ln2). The full signed convolution equations imply f^2=1 after inverse Fourier transform; no normalized non-Boolean vector enters these arrows. The converse arrows invoke FEI explicitly. Terminal H is retained in the stopping-tree arrow.

For the second A003 claim, the parity lift sends the point-defect spectrum to all even subsets of d=n+1 coordinates. Their nonempty masses are 4/N^2, N=2^n; the empty mass is (1-2/N)^2. Adjacent spectral atoms never both have positive mass, so B=L=0. Sum of cardinalities gives I=2d/N. Complement output and use the single actual gate -F with pi=1/N and lambda=1. Conditioning contributes log2 pi=-n and rarity contributes n for every nonempty set, cancelling exactly. There is only one partition run per A, with no child draws. Congestion is zero and the rank sum is log2[(product i_j)/|A|!]. For k=|A|,

    1<=(product i_j)/k!<=binom(d,k)<=2^d.

This gives R<=6vd/5<=12I/5. The first inequality uses actual sorted selected ranks, not a product of independently minimized coordinate witnesses. This pays the residual on that calibration only.

## A007: root law and Boolean suppression

Use x_l=p lambda_l rho_l, a=sum x_l=ps, D=product(1+x_l)-1. Every prescribed nonempty root set has mass product_{l in roots}x_l/D, so expansion proves normalization exactly. Lambda+log2 Z=log2 D. Expansion gives D>=a, while product(1+x_l)<=e^a and e^a-1<=ae^a give

    0<=delta=log2(D/a)<=a log2 e.

No success or almost-sure termination assumption enters this initial-root normalizer.

When the output spectrum meets the shared core U, assign all its core coordinates to one gate l0 and its data coordinates to any covering gate. Each other used gate can be reached from l0 through a fixed owned core coordinate. Since l0 reaches every vertex, its SCC is the unique source: an incoming different component would also be reachable from l0 and hence would be the same SCC. A star is therefore a valid one-root partition forest. Each gate owns a nonempty subset and is visited once. On U empty, source-SCC spanning forests have 1<=K<=|T|. All prescribed draws have positive mass under the one fixed feasible generator.

For F=2A_r B-1, nonconstant Fourier sectors have coefficient 2p Bhat(T). The empty coefficient is 2pb-1; v=4pb(1-pb), I_data=pI(g), I_core=2rpb. Extra roots occur only in empty-core, nonempty-data sectors. Consequently

    0<=EK-v<=4p^2 sum_T |T| Bhat(T)^2=p^2 I(g).

EK is the unconditioned weighted sum, not conditional expectation given a nonempty spectrum. Since rp<=1/2, r(EK-v)<=I_data/2. Substituting log2 pi_l=-r+log2 rho_l proves the exact root block

    T_root=v log2 s+v delta+r(EK-v)+E base_root_rarity.

Also v delta<=4pb ps log2 e<=(log2 e) I_core. With log2 s<=0, the remaining common-scale overhead is <=I_data/2+(log2 e)I_core<=log2(e) I. Nothing pays base rarity, gate labels, ranks or subsets here.

For disjoint petals, complementary factors have norm squared 1-rho_l and nonempty mass rho_l(1-rho_l). Their tensor product gives sum_{T nonempty}Bhat(T)^2=Q(1-Q) and sum_T K Bhat(T)^2=Q sum_l rho_l. Thus EK-v=4p^2 Q(sum rho_l-(1-Q)). Every extra-root pattern is genuinely weighted by p^2. The complete-reference prior w_j=1/[(j+1)(j+2)] sums to one; selecting j=0 pays v. The component's D_j and all subsequent queue costs must travel together.

## A008: finite dictionary, actual output quotient

For a fixed rational table, the probability of a record is

    kappa_|F| product_{l in F}eta_l / E_|F|(eta) * product_{l in F}q_l(B_l).

Sum local subset laws, then the weighted fixed-size name sets, then the size law. This gives exactly one. There is no queue, no possible infinite execution and no independent root draw. Union decoding terminates. Canonical owners, source SCC roots and breadth-first attachments are deterministic functions of a record. They incur no additional conditional fields in this generator, but this does not erase the different queue's normalizer.

For any finite rational record/output law q, exact integer comparisons compute ceil(-log2 q). Kraft holds because 2^-ceil(-log2 q)<=q. Canonical sorted prefix words decode records or outputs separately. There is one total rounding bit. The output mass Q(A) sums all records in its fiber once; the fixed order of name sets supplies no factorial credit. KL inside that fiber gives inf(E record_cost-H(posterior))=-log2 Q(A). This quotient cost is physically realized by the output prefix, which does not recover the random record. It cannot be subtracted from a transcript transmitting the record itself.

For sunflower m, sum_k (m+1)/[mk(k+1)]=1. Output {0} has mass sum_k kappa_k 3^-k>=1/6. For private T, t=|T|>=1, Q(T)=kappa_t/[binom(m,t)3^t]. For {0}+T, choose u extra common-only gates and retain 2^t-1 choices when u=0, or 2^t when u>0. This reconstructs exactly the source formula. Both rare output costs are <=3m+2t. Their spectral expectation is <=r_m=8m2^-m-6m4^-m, whose values at 1,2 are 5/2,13/4 and whose positive recurrence difference is 16(m-1)2^m-18m+6 after multiplying by 4^(m+1). The dominant cost is <3. Thus the nonempty ideal cost is <25I/4; h2(v)<=1<=I and one rounding bit give <33I/4.

Every raw {0} record has probability <=1/m, by binom(m,k)>=m for k<m and 3^m>=m for k=m. Its latent-name cost is therefore >=log2 m, and its actual spectral weight tends to one. The output quotient and raw transcript conclusions are consistent. A dedicated address table has exactly one a-bit name and one a-bit control subset, hence exact cost 2a. A mixture choosing that table adds its prior penalty.

## A012: admission reflection and the rare physical label

The membership reflection is exact and algebraic: closure produces the balanced disjoint tensor and its activation. Fixing the controls extracts the tensor, and fixing all other tensor blocks plus the balancing sign extracts the original seed. Both reverse steps are genuine physical restrictions and do not involve an entropy limit.

The globally read-once AND/OR/parity class R has all the stated closures. Activation is OR of the mismatching control literals and the original core; disjointness of labels is essential. Multiplexer exclusion is exhaustive analytically: a root on three essential inputs has either three singleton children or a singleton plus two-variable child after removing constant/unary gates. An AND/OR root with a fair singleton can be balanced only if the other child is constant; three-singleton AND/OR is unbalanced. Parity roots give the singleton influence one. The balanced multiplexer has all three influences 1/2, contradicting every possibility. Overlapping OR(AND(x,y),AND(-x,z)) realizes it, so overlap is not an R closure.

The corrected entropy composition law is independently reconstructed by expanding every nonempty child block: coefficients are outer coefficients times child coefficients divided by the square roots of child variances. Splitting their squared-coefficient logarithm gives E(F)=E(b)+sum I_i(b)E(f_i)/Var(f_i); the influence/variance identity gives the same nonnegative coefficients for deficit. Deterministic children are deleted before division.

For OR with a_i=Pr(input_i=-1), Z=product a_i, R0=sum(1-a_i)-1+Z and Theta=sum(a_i-Z)ln(1/a_i), appending b increases R0 by (1-b)(1-Z) and Theta by (1-b)Z ln(1/Z)+b(1-Z)ln(1/b)<=2(1-b)(1-Z). Thus Theta<=2R0. OR has deficit 4ZR0 and natural corrected entropy (ln4)deficit+8ZTheta; hence E<=C0 deficit, C0=2+4/ln2. Parity has deficit R0 and natural corrected entropy Theta, so it obeys the same constant. Composition telescopes on disjoint labels. At uniform original inputs, adding empty entropy <=log2(e)Var gives H<=C0 I. These are proper-class source results, not a new universal admission theorem.

For the control-first activation of y, p=2^-r, physical leaf entropy is H(J)=D=2(1-p). The two-bits-per-query transcript has length 2D=4(1-p), while I=p(r+1). This gives the claimed divergent cost/I. The balanced activation spectrum gives H(F)=2rp(2-p)+L((1-p)^2)<=4rp+2p log2 e. If W retains J with this physical leaf law and decodes S exactly, H(W|S)=H(W)-H(S)>=D-H(F). Its lower bound tends to two bits. This is not a lower bound against every possible output reference or policy, nor an error in A011's admission-conditional theorem.

## Independently executed validation

FROZEN_SPEC.json precedes the checker. The main checker imports no author implementation and uses integer Walsh transforms, Fraction arithmetic, exact log2-prime linear forms and rigorous rational natural-log intervals. The interval uses 48 atanh terms after power-of-two reduction; with z=(q-1)/(q+1), the remaining absolute error is <=2|z|^97/[97(1-z^2)]. The ln2 interval is bounded by the same method. No floating entropy comparison is a certificate.

The final main checker covers 270 nonconstant labelled functions through n=3, seven parity-defect dimensions n=2..8, 876 overlapping two-gate activation/weight cases, 24 heterogeneous-petal cases, 1,359 sunflower records through m=5, one nonuniform three-gate dictionary, all 768 activations of labelled three-bit cores, 117 product-biased gates and six disjoint compositions. It reconstructs the 152-member read-once class and its restrictions; literal activation bounds cover r=1..12. Exact checks verify root probabilities, source-SCC forests, root debt identities, prefix Kraft sums, coherent activation spectra, corrected composition and entropy bounds. The source domain is frozen; no symmetry reduction or escalation occurred.

V1 computed A008 code lengths under the structural reference. V2 corrected this check to the actual Boolean spectral law; V1 is preserved and no source claim was changed. The frozen count field's 1,365 sunflower records was an arithmetic typo; the unchanged m=1..5 domain has sum(4^m-1)=1,359. REFINEMENT_SPEC.json records both points before V2 execution. V2 passed 89,093 assertions in 2.695150 seconds. For m=1..5, actual spectral expected compiled output lengths are 2, 23/8, 227/64, 899/256 and 107/32 bits.

The new reference-debt projection is proved in ACTIVATION_DEBT_PROJECTION.md, with a separate frozen 468-case exact symbolic-log checker and saved output. It is a derived audit interface, not independent acceptance of this author's new statement. A094/A085 should review it. Remaining universal payment is stated in JOINT_CODE_GAPS.json.
