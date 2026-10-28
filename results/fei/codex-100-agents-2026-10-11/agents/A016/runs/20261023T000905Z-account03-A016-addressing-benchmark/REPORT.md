# A016 stage 8: the full signed reserve survives a tensor bit and a padding bit

Full FEI remains OPEN. A020's unbounded-width admission no-go holds: the original half-bank can fail even when the complete reference is eligible. On that SAME Boolean tensor family and SAME Q, the full signed physical reserve pays an actual tensor-bit query and then one actual padding-bit query, retaining the old insertion debit and all eight proper terminal references. No reference is reset. The first four terminals have reserve greater than15/8, and the eight terminals after the padding query have reserve greater than39/32. After the original insertion debit these margins remain greater than5/4 and19/32 respectively. Independent review is pending.

## exact target, quantifiers, hypotheses and units

All physical bits are uniform independent 0/1 bits, signs are Boolean, and all entropy, CE, KL, and reserve quantities are in bits. Let g on three bits equal-1 at000 and+1 elsewhere, G_m be the product of m disjoint copies, m>=4, and A=1_(v=0)(1-G_m)/2 with k>=5 padding bits. Write rho=2^-k, mu=(3/4)^m, beta=(1-mu)/2, p=rho beta. Set h=chi_u off A and chi_q on A, F=1 at x0 and hs at x1, where s=[-1,1,1,1] is the two-bit mask. The one supplied root reference is Q_h=(P_h+point_q)/2 and Q_F(e,T)=[Q_h(T_core)P_s(T_mask)+point_empty(T)]/4 at BOTH gate frequencies. Every later reference is its frequency marginal.

Expose q, one specified bit in one g block, then one padding bit. Both outcomes of every query remain. The old booked first insertion is U=J_first=L_q+E, including the exact fresh-to-inherited conversion, and is fixed throughout. No new child bank is admitted. We bound 4I-CE-U at each complete terminal. As a separate averaged statement, after q and ANY predetermined subset of tensor bits (padding unqueried), the expected signed reserve4I-CE exceeds19/8, and exceeds7/4 after retaining U. This subset statement is averaged over all physical histories; it does not assert that every adaptive stopping partition or every conditional history is locally eligible.

## sources actually read, revisions and theorem locators

Read BOARD snapshot2026-10-23 00:10UTC, B04 STREAM_NOTES v2, own STATUS and prior-stage artifacts. The original addressing baseline and bent-splice benchmark are complete and not repeated. Static execution protocol revision2026-10-11-execution-v2 is rechecked for exact output fields. The newer owner deadline2026-10-23 14:49UTC supersedes its historical endpoint. Prior baseline campaign/paper readings remain carried forward; no new literature or priority claim is made.

New main source, read in full: A020 run20261022T231605Z-account03-A020-selector-boundary-tests REPORT.md sections1--6, admission no-go and exact same-bank ledger. Read the recent A019 run20261022T221313Z REPORT prefix through the opposite-means paid source and A018 run20261022T202507Z REPORT through the equal-mean insertion proof. Their author claims are not premises here. The present inherited Q is not silently replaced by A018's actual conditional lift. A016 stage7 supplies the original general endpoint and bank identity, with its hypothesis retained. A020 independently accepted that interface, not the whole finite-width theorem. Source hashes are saved in out/SOURCE_RECEIPTS.json.

Read-only math recall returned only weak/general leads; no card supplies this payment. Brain wake reports stale owner-model/state notes and a self-care ledger lock timeout. Those affected notes are not proof inputs. The compute snapshot is ok with4708MB available physical RAM,21589MB available commit and23GB free disk; no running work is stopped. Shared campaign, context, brain and other-agent artifacts are read-only.

## complete derivation or exact first unsupported line

1. The no-go is real, but scoped. At q fixed the common squared core spectrum P has coefficients squared(1-p)^2 at{u}, p^2 atempty and two copies of Ahat(T)^2 for each nonempty activation T. Put c=CE(P,(P+point_empty)/2) and J_A=4 sum|T|Ahat(T)^2. Then I(h_q)=1-p+J_A/2, C_root=c/2+3 and I_root=3/2+J_A/4. The exact old insertion satisfies

L_q=(1/2)log((9+p^2)/8)+(p^2/8)log((9+p^2)/(1+p^2)),
U=L_q+E<5/8, 0<=E<p^2.

The nonnegative conversion E is the actual empty-data gate conditional KL. Its formula is in the checker; its denominator1+(p/2)^2 is positive. It is not set to zero or rebooked.

For the seed, H0=4-(9/8)log3 and I0=3/4. Since3^3<2^5, H0>17/8 and H0/2-I0>5/16. Tensor coefficients have multiplicity binomial(m,b)7^b and squared mass9^(m-b)/16^m. With L_B=sum Bhat^2 log(1/Bhat^2), exact Boolean coefficients give

L_B=eta(beta^2)+(mH0-eta(mu^2))/4+(1-mu^2)/2,
H(P)=eta((1-p)^2)-eta(p^2)+4kp+2rho L_B,
J_A=2kp+rho(3m/4),
c=H(P)+1-p^2 log((1+p^2)/p^2).

Here eta(t)=t log(1/t), eta(0)=0. For k>=5, p<1/64. The same bounds as the source give c-J_A>(5/16)rho m+123/128. In detail eta(p^2)<1/128, p^2 log(1+p^2)<1/128, the exact mixture KL is>63/64, and eta(mu^2)<=1; all omitted terms are nonnegative. Thus the remaining original half-bank

R_half=C_end-(c-J_A)-1-2p-E-D

is<-123/128 whenever rho m>=8, because C_end<7/2. Both signs of the constant endpoint and its weighted positive deficit D remain. At k5 this includes every m>=256. The claimed universal c<=J_A+O(1) is false. For any fixed Boolean seed f with |E f|<1, even tensor powers replace the growing term by rho r[H(f)/2-I(f)]; all eta/K remainder terms are bounded. Such an admission would force the false constant2 FEI inequality. This reconstructs A020's actual no-go, not a refutation of A016's conditional statement or of FEI. Eligibility also holds analytically: L_B<=mH0/4+3/2 and eta((1-p)^2)<3p give c<1+(4k+3)p+3rho+(rho mH0)/2<=93/64+(rho mH0)/2. Since H0<3, this yields source core/root/immediate-child rate4 eligibility and S>159/128 without an unproved core premise. These inequalities are independently checked on the frozen cases; the all-m proof is analytic.

2. Use the full physical signed reserve. For any supplied finite-cost Q, physical restriction gives average child squared law equal to the frequency marginal of the parent law. Let Q' be that same marginal. Then

CE_parent=average CE_child+L_i,
L_i=sum P_parent(e,T) log(Q'(T)/Q(e,T))>=0.

Support is preserved and every positive denominator is covered: positive child mass implies positive erased parent mass. For W=4I-CE-U, with the SAME fixed booked U, the exact transition is

average W_child=W_parent-4Inf_i+L_i.

This is the full physical influence decrease, not the erroneous requirement that every additional positive code charge be paid from a separately isolated half-bank. The code charge releases parent CE as it retains the complete child CE. No claim is made that R_half becomes positive. This identity is conditional on already having the supplied root Q; it does not construct universal inexpensive codes.

3. Four actual tensor-bit terminals. After q and one tensor-bit query, write b for that bit's outcome. At b=0 the queried seed becomes the two-bit point-defect sign with mean1/2, entropy2 and influence1. At b=1 it becomes the constant+1. Hence the actual remaining products have

mu_0=(1/2)(3/4)^(m-1), mu_1=(3/4)^(m-1),
I(G_0)=1+3(m-1)/4, I(G_1)=3(m-1)/4,
H(G_b)<=4I(G_b).

For m>=4, both0<mu_b<1/2, so beta_b=(1-mu_b)/2 and p_b=rho beta_b satisfy0<p_b<1/64. The inherited core reference at either terminal is Q_*=(Pbar+point_empty)/2, with Pbar=(P_0+P_1)/2 the EXACT marginal of the original q-child law. It follows atomwise that Q_*>=P_b/4. This is one fixed reference for the two unequal spectra, not a newly optimized child reference. Therefore CE(P_b,Q_*)<=H(P_b)+2.

For any positive-mean Boolean G with mean mu<=1/2, B=(1-G)/2 has squared Fourier law equal to P_G/4+(1-2mu)point_empty/4. The coefficients are nonnegative; this is where the mean side condition is used. Normalizing by beta=(1-mu)/2 gives a mixture with weight w=1/(4beta)<=1. Thus

H(Bhat^2/beta)<=h2(w)+w H(G).

The actual rare-activation core P_b is the mixture of a point at{u} of weight1-2p_b and a distribution of weight2p_b, consisting of a uniform u sector, uniform k-bit padding spectrum and normalized B spectrum. Its entropy therefore obeys

H(P_b)<=h2(2p_b)+2p_b(k+2)+(rho/2)H(G_b).

The outer reference keeps its uniform gate law and exact mask spectrum. Its data marginal is (Q_* tensor P_s+point_empty)/2. The complete latent-label mixture code gives

CE(F_terminal,Q_inherited)<=CE(P_b,Q_*)/2+3
 <=H(P_b)/2+4.

This bound retains all ghost atoms and the constant mixture branch. It holds for BOTH q signs; the full code cost is the same because the reference gate is uniform. Their influences differ and are separately retained:

4I(F_terminal)=6+2(k-1)p_b+rho I(G_b) minus/plus p_b.

Consequently the smaller signed reserve satisfies

4I-CE>=2+(k-5)p_b-(1/2)h2(2p_b)>15/8.

Indeed h2 is increasing on[0,1/2], 2p_b<1/32 and h2(1/32)<1/4, the last inequality certified by31^31>2^152. Subtracting the same U<5/8 leaves>5/4 at ALL four actual q/b terminals. Neither the whole old bank nor a new one is reinstated. The actual tensor query influence in F is rho/16; its physical rate4 decrease is rho/4, retained in the exact W transition above.

4. One further real padding query, eight full terminals. Query one of the original padding bits at each of those histories. Its inherited core reference is again the frequency marginal of Q_*, identical at both physical outcomes. The exact averaged-law identity now gives Q_**>=P_terminal/8 atomwise. Hence CE_core<=H_core+3, and the complete outer code satisfies CE_F<=H_core/2+9/2. This factor8 is a domination certificate for the ORIGINAL reference, not a reset.

At padding outcome1, A=0 and the actual core is chi_u. Its full activation has I=3/2 and H_core=0, so 4I-CE>=3/2; the offbranch and its ghost cost are explicitly retained. At padding outcome0, the remaining point padding has k'=k-1>=4, rho'=2rho and p'=2p_b<1/32, with the SAME G_b. Repeat the previous entropy mixture bound at k',rho',p'. Its complete signed reserve is

4I-CE>=3/2+(k'-5)p'-(1/2)h2(2p')>39/32.

For k'=4 the negative term is at worst-p'>-1/32; for k'>=5 it is nonnegative. Also2p'<1/16 and h2(1/16)<1/2, certified by15^15>2^56. This proves the uniform39/32 margin. After subtracting the SAME U<5/8, ALL eight terminal references retain>19/32. No old debit, erased edge, rare branch or terminal cost is dropped. Their weights are the actual1/8 reaches, not a new spectral prior.

5. Beyond one chosen tensor bit: every fixed tensor subset is averaged-paid. After q, erase ANY predetermined subset of tensor frequencies, leaving padding untouched. In a seed block with r remaining bits, the projected seed spectrum has empty mass1/2+2^(-r-1) and2^r-1 other atoms of mass2^(-r-1). Each remaining coordinate has inclusion probability1/4. Its entropy is at most r=4 times its expected remaining spectral degree (for r=0 both are zero). Products preserve this bound, so H(P_G,projected)<=4 I_G,remaining for any subset.

Let b be the projected squared coefficient law of B=(1-G_m)/2. Since mu=(3/4)^m<1/2, it is b=P_G,projected/4+(1-2mu)point_empty/4 with total beta. The q-erased projected core Pbar again has the point/uniform-padding/normalized-b mixture from section3. The SAME core reference is (Pbar+point_empty)/2, and the outer inherited code has mean cost<=H(Pbar)/2+7/2. Expected remaining full influence is

Ibar=3/2+(k-1)p/2+(rho/4)I_G,remaining.

Substituting the entropy mixture bound and h2(w)<=1 yields

E(4I-CE)>=5/2+(k-4)p-(1/2)h2(2p)>19/8.

The retained old U leaves>7/4. This covers every prefix of every FIXED tensor-coordinate order and all physical outcomes on average, in arbitrary dimensions. It does not permit replacing the chosen subset by one depending on the outcomes without further work. Conditional terminal costs can differ; they must not be replaced by unconditional averages. Sections3--4 separately prove the local four/eight-terminal statements at the specific actual interleaving.

First unsupported universal line: obtain a contracting signed likelihood/source potential under arbitrary mixed adaptive core/padding queries while retaining the booked U and the original Q. The present simple domination certificate loses one bit per query and does not pay arbitrary lengths. The product seed projection estimate supplies the fixed-subset result, not an arbitrary-core invariant or a universal good-query policy. Full FEI remains unproved.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json and the subsequent PADDING_EXTENSION_SPEC.json precede their respective tests. Independent checker v1 reconstructs exact joint true/reference histograms at k5,m4,8,16,64,256, with binomial multiplicities instead of exponential truth tables. It verifies the A020 admission/half-bank signs, complete inherited normalization/support, all four tensor terminals, all eight padding terminals, exact factor4/factor8 domination, physical pivotal mass and the signed physical transition. Two separate literal Boolean reconstructions at k1,m1 and k1,m2 (maximum dimension12) independently verify actual Walsh restriction identities, physical edge influence, unequal children and all complete references. Small-k tables validate the formulas only; they are not substituted into the theorem's k>=5,m>=4 hypotheses. No symmetry assumption beyond exact product multiplicities is used.

Arithmetic is integer Walsh and Fraction spectra, with outward90-bit dyadic logarithm intervals. After range reduction1<=x<2, z=(x-1)/(x+1), the40-term atanh tail is at most2 z^81/[81(1-z^2)]. Each positive multiplication is enclosed outward; negative log coefficients reverse endpoints. The same construction encloses ln2. Exact integer inequalities certify the two binary-entropy endpoints. Interval overlaps are redundant consistency checks, not equality proofs; exact Walsh/marginal identities and the algebra above establish the equalities. Every completed histogram case is checkpointed. Frozen memory estimate110MB; checker runtime cap60seconds; no dimension escalation, GPU, window, detached job, git, external message or other-agent mutation is used.

Commands from this run: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py. The padding-extension pilot passed1575 assertions in0.153611seconds. The final full run passed48565 exact assertions across5 histogram and2 literal-table cases in14.835817200015299seconds. Full-run results and arithmetic receipts are in out/CHECK.json. No failed assertion is accepted. Compiler admission was checked after the bounded exact run. At that later snapshot memok exited1: physical free2.8GB versus required4.0GB, commit free20.4GB versus required8.0GB. Physical availability had fallen from the initial4.7GB; these are different observation times. No Lean compiler was launched. code/Bank.lean records only the rational margin implications and remains UNCOMPILED. out/COMPUTE_ADMISSION.json records this exclusion. No Lean claim follows. Mathematical rung: analytic proof with exact finite verification, independent review pending.

## proof dependencies and changed downstream conclusions

A020's exact conditional endpoint and unbounded-admission/half-bank no-go are independently reconstructed, including its actual Boolean family, original Q and both terminal signs. Its lower bound, source eligibility and positive half-bank are preserved. This is scoped acceptance of the no-go/interface, not blanket acceptance of all prior source claims. A016's earlier c<=J_A+2 theorem remains correct at its stated hypothesis and its finite-width instance; its desired arbitrary-width admission is now closed negatively by A020. There is no reason to repeat wider finite admission searches.

The new replacement pays the actual full signed reserve, not the failed half-bank allocation. It retains U=L_q+E explicitly at every new terminal and uses the ORIGINAL reference marginals. A018's equal-mean reference theorem is not invoked: our two tensor-bit children generally have unequal means and spectra, and their incoming reference is not replaced. A019's supplied source/repair bounds are likewise not used as premises. No universal FEI inequality is assumed. The new four/eight-terminal and fixed-subset claims await independent reconstruction by A020/A019/A018/A090/A091/A094.

## one next mathematical action and independent reviewer

Replace factor2-per-query domination by the exact rowwise inherited likelihood on the next padding/core query, with U and the current signed profile carried forward and every complementary terminal retained. Seek an invariant contracting under outcome-dependent mixed queries; a fixed-subset average is insufficient. A020/A019 should reconstruct the factor4/factor8 terminal bounds and the original-U ledger; A018/A090/A091/A094 should challenge the unequal-mean and adaptive-subset boundaries. This addresses the precise missing conservation mechanism instead of retrying the refuted admission.

## actual persistence receipts or precise save blocker

The four protocol files, both frozen specs, independent checker, pilot/full outputs, source receipts and local persistence manifest are saved only in this A016 run. STATUS has exactly two lines and names the unpaid step; WORKLOG is appended and LEARNED records the invariant, constants and scope. Final validation checks exact protocol keys, claim hashes, identical PROGRESS/PACKET_DELTA, JSON parsing, size limits and local byte hashes. Independent review of the new theorem, supervisor adoption and mirror verification remain pending. No remote save or shared-registry update is claimed. Required wake bookkeeping is separate from research writes; stale personal notes and contract-lock warnings are not ignored or treated as mathematical evidence.

## Universal bridge

This stage moves C024 history transfer and B04's C019 stopping-tree payment by replacing a disproved half-bank admission with the full signed physical reserve on A020's same unbounded-width Boolean obstruction: after q and one actual tensor bit the four original-reference terminals retain>5/4 after the old debit, and after one further actual padding bit all eight retain>19/32. Every predetermined tensor-subset exposure also has expected signed reserve>7/4 after that same debit. A020's admission no-go is accepted, so c<=J_A+O(1) is retired as a universal route; full FEI is still OPEN. What remains is a source potential contracting under arbitrary mixed adaptive histories without multiplying the reference loss or discarding unequal terminal profiles. NEXT attacks that exact likelihood/ownership step, which is necessary for a universal paid stopping tree rather than another isolated spectral-class inequality.
