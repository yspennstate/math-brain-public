# A018 stage 4: actual Boolean failure of shared-row subadditivity

Run 20261014T022025Z-fleet05-A018-shared-data-collision-law, B04/A018. Full FEI remains OPEN. The optional paired-row entropy-subadditivity line from stage 3 is FALSE, even for two Boolean point-defect modules sharing one bit. The previous exact TC/reference interface remains valid. The new obstruction has a pure-integer certificate and an all-dimensional rare-event extension; its complete reference is nevertheless paid at rate4 from a single allocation of the module terminal slacks. A016's new two-weak-separator theorem independently HOLDS at its stated scope.

## exact target, quantifiers, hypotheses and units

All physical bits are independent fair bits. For two mutually disjoint private blocks y_1,y_2 of sizes n_1,n_2, and one common physical bit z, define f_j(z,y_j)=-1 exactly when z=0 and y_j=0, and +1 otherwise. Let F=f_1 f_2 and G=H(F)-H(f_1)-H(f_2). Entropies, KL and complete reference CE are in bits; G_nat=ln(2)G uses natural units. Physical influence is edge disagreement probability. No balance or orthogonality assumption is made.

We refute H(F)<=H(f_1)+H(f_2), equivalently the optional B_*<=B_1+B_2+TC in the previous report. We also refute any dimension-free G<=K L on these actual Boolean modules, where L=I(f_1)+I(f_2)-I(F) is the lost shared physical influence. This is not a refutation of the exact identity H(F)-sum H(f_j)=B_*-sum B_j-TC, of A019's ownership theorem, or of FEI.

For equal private sizes m and delta=2^-m, we prove

G_nat=delta^2[(4m-24)ln2+6]+R,
|R|<=delta^3[(16m+48)ln2+1000], for all m>=4.

Consequently G>0 for every m>=12 and

G/L=2m+3/ln2-12+O(m 2^-m) -> infinity.

Despite this loss-price obstruction, H(F)<=CE_Q(F)<=4I(F) for every m>=12, for the explicitly normalized conditional-product reference Q described below. Every module terminal cost and the joint-data TC bill are retained; the two module slacks are allocated once.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start, supervisor snapshot 2026-10-14 02:12 UTC; B04 STREAM_NOTES v2, still 2026-10-11 23:25 UTC; own STATUS.md and stage3 report/helper. Read EXECUTION_PROTOCOL.json completely, revision 2026-10-11-execution-v2. Required campaign/paper context was consumed in previous stages; no new external theorem or literature-priority claim is needed here.

New useful sources: A019 LEARNED.md, folded-separator ownership section and its pointwise paired-bias counterexample at u=v=7/25; A020 LEARNED.md, width-dependent owner-loss obstruction; A016 runs/20261014T011255Z-fleet05-A016-addressing-benchmark/REPORT.md sections1-7 and CLAIMS.json, A016-TWO-WEAK-SEPARATORS-OWNED-PAYMENT@1. A019's pointwise failure means that zero-mean laws must be tested directly. The Boolean witness below goes further and refutes even that averaged proposal. A016 supplies a new paid two-pivot reference and a precise half-private hypothesis to audit.

A018 stage3 REPORT sections2-5 supplies the exact TC/reference interface and explicitly unproved scalar proposal. That proposal was not registered as a proved claim. Stage2 code/check_lead.py supplies only the already proved Fraction logarithm definitions; its main/search body is excluded. A016's checker is not imported. Source hashes/read scopes are saved in out/SOURCE_RECEIPTS.json; mutable board hashes at close do not assert an unchanged stage-start snapshot.

## complete derivation or exact first unsupported line

### 1. Boolean realization and physical ownership

Write a=2^-n_1 and b=2^-n_2. At z=0 each module is a private one-point defect h_j; at z=1 it is constant1. Its branch spectra are h_jhat(empty)=1-2a_j and h_jhat(T)=-2a_j for all nonempty T. The module itself is a one-point defect on n_j+1 bits, with empty coefficient1-a_j and every nonempty coefficient -a_j.

Every private coordinate of f_j has influence a_j. Private influence is unchanged by multiplying the other sign module. The shared product changes on exactly one of the two private-origin events, so

Inf_z(F)=a+b-2ab,
I(F)=(n_1+1)a+(n_2+1)b-2ab,
L=2ab.

These are physical edge identities, independently checked against the actual Walsh spectrum.

The posterior-bias realization is especially simple. For equal m, let eta=(1-(1-2delta)^2)/2=2delta(1-delta). Under the module's data marginal, U=1 on a nonempty private Fourier set (total probability eta), and U=-eta/(1-eta) on the empty set (probability1-eta). Therefore E U=0 exactly. At m=5 this is U=1 with probability31/512 and U=-31/481 with probability481/512. Thus failure of the averaged scalar proposal is realized by Boolean functions, not just a normalized real relaxation.

### 2. Eleven-bit certificate with no logarithm approximation

Take n_1=n_2=5. Each module has 64 truth values, negative only at its all-zero physical point, and Fourier integer transform histogram {62:1,-2:63}. The shared parent has 2048 actual truth values and integer transform histogram

{1924:1,-124:1,-60:124,4:1922}.

The parent normalization is 1924^2+124^2+124*60^2+1922*4^2=2048^2. Expanding the entropy gives

G_nat=[491071 ln31-231361 ln481-27900 ln15-262144 ln2]/131072.

The exact integer comparison

31^491071 > 481^231361 * 15^27900 * 2^262144

proves G>0. code/verify_integer_witness.py executes it directly, writes the two integer byte hashes and bit lengths, and independently checks the displayed Parseval count and 961*511=491071. Actual truth tables, a recursive Walsh implementation, a separate iterative Walsh implementation, physical edges and every branch-product coefficient are checked by code/check_boolean.py. Thus the certificate is source-complete and does not depend on a floating entropy sign. The first discovered Boolean witness was the unequal (4,6) fixture, also eleven-dimensional; the equal (5,5) witness provides the simpler integer certificate.

### 3. Exact all-m spectrum and collision asymptotic

Now set both private sizes to m and N=1/delta. Shared parent coefficients have the following four classes, with their multiplicities:

empty: c_0=1-2delta+2delta^2, once;
shared-only: -2delta(1-delta), once;
exactly one private block nonempty: -delta(1-2delta), 4(N-1) times;
both private blocks nonempty: 2delta^2, 2(N-1)^2 times.

These follow by taking the half-sum/half-difference of the private branch-product spectrum and the constant branch spectrum. All multiplicities sum to2N^2, and the squared masses sum to1. Each module has empty squared mass (1-delta)^2 and2N-1 other squared masses delta^2.

Let x=delta. Collecting logarithms in H(parent)-2H(module) gives the exact natural-unit expression

G_nat=(-4x^2+16x^3-8x^4)ln x
       +(-24x^2+48x^3-24x^4)ln2+A(x),

A(x)=-2(1-2x+2x^2)^2 ln(1-2x+2x^2)
     +[4(1-x)^2-8x^2(1-x)^2]ln(1-x)
     -8x(1-x)(1-2x)^2 ln(1-2x).

For 0<x<=1/16 we show |A(x)-6x^2|<=1000x^3. The bound is deliberately loose and fully explicit. For 0<=t<1,

|ln(1-t)+t+t^2/2|<=t^3/[3(1-t)].

In the first term put t=2x-2x^2<=1/8. The log remainder is <=4x^3; multiplication by2(1-t)^2 contributes <=8x^3. The polynomial replacing that term has coefficients

[0,4,-16,24,4,-64,96,-64,16].

Beyond degree2 their absolute sum is268, giving a total residual <=276x^3. In the second term the polynomial multiplier is [4,-8,-4,16,-8]; the log remainder at t=x is <=x^3. Its absolute coefficient sum is40. Multiplying its quadratic log approximation gives coefficients [0,-4,6,8,-14,0,4], whose degree>=3 absolute sum is26. This contributes <=66x^3. In the third term the multiplier is [0,-8,40,-64,32]. The log remainder at t=2x is <=4x^3. The multiplier's absolute coefficient sum is <=144x, so its error is <=576x^4<=36x^3. Its quadratic log approximation has coefficients [0,0,16,-64,48,64,-64]; the degree>=3 absolute sum is240. This contributes <=276x^3. The sum618x^3 is below1000x^3; the degree<=2 terms sum to6x^2. These polynomial products and coefficient sums are independently checked with exact rationals.

The remaining logarithmic residuals are bounded by16x^3 ln(1/x) and48x^3 ln2, proving the announced R bound. For m>=12, ln2 lies in (2/3,1), so

G_nat/delta^2 >= 2m-6-2^-m(16m+1048) > 2m-7 >0.

The quantity2^-m(16m+1048) decreases with integer m>=12 and at12 equals1240/4096<1. This proves positivity for every m>=12 without large truth tables or precision extrapolation. Dividing by L=2delta^2 proves G/L=2m+3/ln2-12+O(m2^-m), hence no finite loss-only price is possible. The entropy-to-total-influence ratio stays bounded; this family is not an FEI counterexample.

### 4. Complete conditional-product reference and one-use slack payment

For each module use its explicitly known squared spectrum as a finite normalized reference Q_j; its CE equals H(f_j). Let R_j be its data marginal and nu_* the actual parent selector conditional. Define

Q_*(A,T_1,T_2)=nu_*(A|T_1,T_2) R_1(T_1)R_2(T_2).

All private rows have positive true mass in this family, so no unsupported atom is excluded. Summing conditionals gives normalization1. The exact stage3 identity, or direct entropy expansion, yields CE_*=H(F)+TC. This is an explicit reference for a specified family; it supplies no oracle reference for arbitrary Boolean terminals.

Within each private block the nonempty data Fourier label is uniform, in both the module marginal and the shared joint law. Dependence therefore reduces exactly to the binary markers X_j=1{T_j nonempty}. Their marginal probability is eta=2delta(1-delta), and their joint law satisfies P(X_1=X_2=1)=2eta^2. The joint Bernoulli table has covariance eta^2, so its chi-square divergence from the product marginals is eta^2/(1-eta)^2. Using ln t<=t-1 gives

TC_bits<=eta^2/[(1-eta)^2 ln2]
        <=4delta^2/[(1-2delta)^2 ln2]<8delta^2,

since delta<=1/16, ln2>2/3, and6*(64/49)<8. This retains, rather than discards, the joint-data reference debt.

For m>=12 the proven remainder gives G<=4m delta^2: the normalized residual is <1 in natural units, and (7/ln2)-24<0. Also

H(f_j)=-(1-delta)^2 log2((1-delta)^2)+(2delta-delta^2)2m
      <=4m delta+(2/ln2)delta<4m delta+3delta.

The empty-sector estimate uses -ln(1-delta)<=delta/(1-delta). Thus each module's rate4 slack S_j=4I(f_j)-H(f_j) is at least delta. For the compatible parent reference the exact required payment is

S_1+S_2 >= 4L+G+TC.

The right side is <=(4m+16)delta^2, while the left is >=2delta. At m=12, (4m+16)delta=64/4096<2, and this expression decreases for integer m>=12. Hence CE_*<=4I(F), with each module slack used once. This includes both terminal costs, the lost physical influence and the complete TC debt. The failure of G<=K L does not imply failure of this stronger signed-slack insertion.

### 5. Independent review of A016's two weak separators

A016-TWO-WEAK-SEPARATORS-OWNED-PAYMENT@1 HOLDS at its stated scope; no substantive repair is supplied. Reconstruct its arbitrary-mask modules c_j-2A_j(z,w)1{t_j=0} directly. For each physical shared edge, a changed module derivative is a signed point indicator with kappa_j=m delta/2; unchanged modules have kappa_j=0. Its edge-average private energy is J_j,edge=m/2+m delta(A_j(b)+A_j(b')). With Q_-j=(1-2delta) to the number of other changed masks, product expansion gives

t_j,edge=(1-Q_-j)J_j,edge/2+Q_-j kappa_j<=J_j,edge/2.

Averaging the two edges in each of two directions defines one account u_j<=J_j; it does not assign a new J_j for each direction. Parseval identifies T_private=2sum u_j and the extra root mixed energy2E_zw. Since2E_zw<=d, T<=2J+d<=2I. Filtering exact bad nodes decreases this nonnegative bill.

Retain terminal uniform code am. Allocating4J_j to module j pays m+2u_j and leaves at least2J_j-m=4m delta p_j. The reviewed one-node constant c=3/ln2<6 adds c d; the mixed term adds at most d. After shared allocation4d the remaining need is <3d<=12delta sum p_j, whereas the unused private reserve is >=16delta sum p_j for m>=4. This proves the full rate4 ledger without spending a private block twice. The explicit conditional shared reference with uniform private marginal costs am+B_block<=am+2<=3I; entropy concavity also bounds it by the same terminal-inclusive ledger.

For unequal AND/OR masks, expanding their four Walsh coefficients gives exactly the source's displayed four sign classes, E_zw=delta(1+delta)/2 and T=(4m+1)delta(1+delta). The distinct highest ANF monomials connect both private blocks to z,w and cannot cancel. Equal private-sign rows have root weight ratio >=1/(2delta) and total smaller-sector mass delta(1-delta)^2/2, proving B_root>=delta(1-delta)^2(m-1)/2. Each child is a private point splice with B_child>=delta(m-1). At m=12 both exceed4delta; the lower factors increase thereafter. Finally T/I->0 and the normalized reference squeeze2m<=CE<=2m+2 proves CE/I->2. These all-parameter reconstructions supplement the independent finite checks; they do not infer the theorem from fixtures.

### 6. Changed gap and exact first unsupported line

The optional stage3 averaged scalar line and Boolean shared-bit entropy subadditivity are now refuted. No proved A018/A019 dependency is refuted. The current exact interface survives and explains the sign of the excess. A universal G<=K L repair is also impossible.

For general supplied finite complete module references Q_j, define S_j(K)=K I(f_j)-CE_j and k_j=E_Rj KL(nu_j||tau_j). The exact parent lift obeys

CE_*-K I(F)=K L+B_*-sum B_j-sum k_j-sum S_j(K).

The first unsupported universal line is existence of an admissible module/pivot policy whose SAME owned slacks satisfy sum(S_j+k_j)>=K L+B_*-sum B_j, while retaining arbitrary terminal CE and avoiding repeated use of any private/core reserve. Neither a loss-only bound nor the false entropy-subadditivity line supplies it. NEXT targets this signed insertion with a non-flat arbitrary certified terminal core, using the eleven-bit point product as a mandatory positive-excess control and A016's weak-and-bad two-pivot family as the paid control. The new no-go has closed this mechanism; no larger blind bias or Boolean census is the next step.

## executed validation with domain, arithmetic, commands and outputs

All specifications were saved before their respective jobs. Memory estimate80MB for each job; no expected >300MB job, so memok was not required. Peak memory was not measured. Jobs were sequential, under the fixed60-second target, with no GPU, randomization, automatic domain growth, window or background worker.

Commands run in this run directory:

- `python -X utf8 code/discover_bias.py --pilot`:100 floating discovery pairs,0 candidate violations,0.002s. No proof inferred.
- `python -X utf8 code/discover_bias.py`:390625 fixed ordered zero-mean two-atom law pairs,1716 positive floating candidates,2.585s. These motivated actual Boolean verification; FIRST_REAL_DISCOVERY.json is not a Boolean or mathematical certificate.
- `python -X utf8 code/check_boolean.py --pilot`:one(4,4) fixture,543 exact checks,0.022s.
- `python -X utf8 code/check_boolean.py`:nine fixed pairs n_1,n_2 in{4,5,6},25403 checks,6 positive gaps certified,0.935s. Every parent coefficient, actual influence direction and module point spectrum is independently checked. Completed cases saved immediately.
- `python -X utf8 code/verify_integer_witness.py`:3 checks,0.665s, pure-integer positive-gap certificate for(5,5). Each compared integer has about2.43million bits, under the frozen memory estimate.
- `python -X utf8 code/check_formula.py`:ten frozen formula cases,83 checks,0.422s in the final amended helper. Direct rational-log signs and residual bounds through m=24; symbolic remainder/rational lower bounds for the remaining frozen m=32,64,128. Exact normalizations and TC chi-square/reference budgets also checked. No high-dimensional truth table is constructed.
- `python -X utf8 code/review_two_pivot.py --pilot`:AND/OR m4,31 checks,0.075s.
- `python -X utf8 code/review_two_pivot.py`:all16 one-module masks at m4 plus AND/OR at m4,m6,434 checks,1.658s. Own recursive Walsh, separate iterative Walsh, physical edges, every edge-owned account, mixed energy, complete row reference normalization, and terminal-inclusive rate4 bound.

Total in final certificate receipts:26497 exact checks, separate from floating discovery. Prior exploratory/amended formula runs are not added to that total. Entropy signs use exact rational prime-log forms or logs of positive rationals, with36-term Fraction atanh tails, range reduction and outward2^-80 rounding. The eleven-bit decisive sign also has a pure-integer certificate.

Two arithmetic limitations were preserved. An initial formula attempt stalled on unnecessary trial factorization of a huge rational coefficient and was manually interrupted; FORMULA_ARITHMETIC_AMENDMENT.json records the switch to intact rational log arguments. Original interrupted-helper bytes were not archived, and no exact runtime is claimed for that attempt. The next direct remainder check was inconclusive at m32 because the O(delta^3) target lies below its fixed-grid cancellation error. FORMULA_INTERVAL_FAILURE.json preserves the enclosure, and FORMULA_SIGN_AMENDMENT.json records use of the already proved symbolic remainder, without precision escalation or midpoint inference. These were certificate-method failures, not failed theorem statements.

## proof dependencies and changed downstream conclusions

A016-TWO-WEAK-SEPARATORS-OWNED-PAYMENT@1 receives independent A018 HOLDS with unchanged statement/hash and no repair. Its complete rate4 ledger retains B04-NODE-BOUNDARY@1, previously independently reconstructed by A018; exact accounts, normalized reference and limits are otherwise elementary. New A018-SHARED-POINT-COLLISION-EXCESS@1 has a self-contained Boolean construction, exact certificate and explicit asymptotic/error/reference proof; it needs independent review. Stage3 A018-SHARED-SEPARATOR-TC-REFERENCE@1 is used at its author-proved exact-interface scope and rederived for this explicit reference; its optional strengthening is explicitly rejected.

Source-bound correction for B04/A019/A020/A086/A090/A091/A095/A097/B20: retire the unproved paired-row inequality and any universal loss-only entropy excess price. Keep the exact TC identity, the folded ownership theorem, all terminal debts, and the newly demonstrated one-use signed-slack payment. No registry, another agent folder, prior immutable run, brain, mail or git operation was performed.

## one next mathematical action and independent reviewer

Prove or refute the displayed exact signed-slack insertion condition for one shared row with an arbitrary supplied certified terminal core, keeping the same module reference and one unused physical reserve throughout. Use the actual positive-excess point product and A016 weak/bad two-pivot control before any recursive reuse. A090/A091 review the Boolean integer/asymptotic certificate; A019/A095/A097 review the TC chi-square reduction and exclusive slack payment; A016 can challenge the independent theorem reconstruction. Local files are the handoff; no tools sent messages.

## actual persistence receipts or precise save blocker

The four protocol files, code/, out/ frozen specifications, actual Boolean and pure-integer certificates, asymptotic/reference checks, method-failure records, independent review and source receipts are saved in this assigned run. STATUS.md is two lines; WORKLOG.md is appended and LEARNED.md updated. out/PERSISTENCE_RECEIPTS.json checks exact claim/progress key sets, declared hash recipes, equal packet delta, report fields, final Universal bridge paragraph, JSON parsing and20MB file limits. New obstruction review, supervisor adoption, copying and remote mirror verification remain distinct and pending.

## Universal bridge

This stage advances C019/C020 by closing the shared-row subadditivity escape route with an actual eleven-bit Boolean certificate and proving that even the exact entropy excess cannot be priced by the lost shared influence with a universal constant: G/L grows as2m. It independently confirms A016's complete two-weak-pivot ledger and supplies a positive-excess stress family whose compatible normalized parent reference is paid at4I using both terminal slacks exactly once, including TC. No universal payment is obtained; arbitrary-core signed-slack availability, consistent ownership through later pivots, and arbitrary terminal CE remain open. NEXT replaces the point-terminal proof by one arbitrary certified core in the exact insertion inequality, because that tests the reserve doing the payment after the false scalar shortcut has been eliminated, rather than extending another isolated census.
