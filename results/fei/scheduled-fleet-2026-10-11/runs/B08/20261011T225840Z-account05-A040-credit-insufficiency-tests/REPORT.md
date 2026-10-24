# A040 / B08: quantitative insufficiency and a best-coordinate guard

## exact target, quantifiers, hypotheses and units

All functions below are actual Boolean signs on uniform physical cubes. Logs are base two, except ln. Write P(S)=fhat(S)^2, d_i=P(i in S), I=sum d_i, M=sum h2(d_i), B_i=H(S_i|S_-i), J_i=I(S_i;S_-i)=h2(d_i)-B_i, and TC=M-H. The campaign B is sum B_i, not M. Q is the product of the spectral marginals, A=supp P, K_supp=-log Q(A), K_shape=D(P||Q(.|A)), so TC=K_supp+K_shape.

The collision convention tested is exactly A036 v1: b_S=sign(fhat(S))*sqrt(Q(S)) on A and zero off A, C_b(U)=sum b_S b_(S xor U), v_U=C_b(U)^2, Z=sum v_U, R=v/Z, T=sum v_U log(1/v_U)/Z=H(R)-log Z. When Q(A)<1 this b is subnormalized; its support conditioning must be stated separately. No unspecified completion at spectral zeros is being tested.

We prove three controls. First, addressing tensored with a fixed three-bit point defect has strictly positive TC, K_supp, K_shape and T, each Theta(1), while H=Theta(a); every one of these credit/entropy ratios is Theta(1/a). Second, a quadratic bent function with one flipped vertex has strictly positive J_i at every coordinate, J_i/B_i~4*2^-k/ln2, and TC/H~8*2^-k/(k ln2). Thus every physical-coordinate posterior KL can be positive and asymptotically negligible even at the best coordinate. Third, the specified B05 family does NOT have this defect at the best coordinate: min_i B_i/d_i ->2 and best-coordinate J_i/h2(d_i)->1. Sparse tribes also do not falsify the normalized collision mechanism: T/(4I)=w-3+o(1), (M-T/4)/I ->2+log2 e, and (TC-T/4)/I ->log2 e-2.

These refute any universal positive-fraction extraction of entropy by the specified credits alone. They do not refute payment with additional ordinary influence, FEI, the full-support collision-admission premise, or arbitrary references/completions.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full (fei-execution-protocol/2, 2026-10-11-execution-v2), campaign README and CURRENT_STATUS, the four registries/next-action files and the .tex plan. BOARD.md was read at stage start (snapshot 2026-10-11 22:57 UTC). B08 STREAM_NOTES.md v1, 2026-10-11 22:45Z supplied the live target and notation guard. Read A036 runs/20261011T214139Z-account05-A036-reference-law-divergence/REPORT.md, especially Sections 1,2,7; the exact signed support convention comes from that source. Read the earlier canonical B05 run 20261011T193057Z-account01-B05-rare-restrictions/REPORT.md, Sections 2-7, and the supplementary CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING. Source sections consumed: ERASURE_REDUCTION Sections 1-5; BLOCK_RESTRICTION_IDENTITY Sections 1-3; ROUTE_MAP_CURATED Sections 2,4,9.1; GAMMA_ENDPOINT_LEDGER was inspected for separation of occurrence credits from the present reference.

The four provided paper texts were loaded and searched; relevant entropy/reference/restriction passages were inspected. Threshold 38-page and earlier 29-page versions: reference normalization, composition and Theorem 6.6. Percolation 30-page and earlier 31-page versions: Section 11.2, Corollary 11.3, support-sensitive divergence. They are context, not proof premises; no whole-paper audit is claimed. These texts use a legacy cp1252-compatible encoding; an initial utf-8 read failed and was corrected without changing them. Local source hashes and locators are saved in out/source_receipts.json. No brain query or web source was needed for the self-contained derivations.

## complete derivation or exact first unsupported line

### 1. Addressing: keep the entire support loss

Let m=2^a and F_a(x,y)=y_x, with a address bits and m fresh data bits. Its coefficients are m^-1*(-1)^(V dot j) at (V,{j}), for every V,j, and zero otherwise. Consequently P is uniform on m^2 atoms, H=2a, d_address=1/2, d_data=1/m, I=1+a/2. Every support atom has product-reference mass Q(S)=w_a/m^2, where w_a=(1-1/m)^(m-1). Therefore Q(A)=w_a, Q(.|A)=P, TC=K_supp=-log w_a, K_shape=0, and b=sqrt(w_a)*fhat.

Booleanity gives sum fhat(S)fhat(S xor U)=1[U=0], so C_b(U)=w_a*1[U=0], Z=w_a^2, H(R)=0 and T=-2log w_a. This explicitly keeps the -log Z term: discarding it would incorrectly declare T=0 under the subnormalized convention. If instead b is conditioned by dividing by sqrt(w_a), Z=1 and T=0 exactly. A completion outside A changes the problem; no completed-reference conclusion follows here.

Let h be the three-bit sign equal to -1 at one vertex and +1 elsewhere. Its spectrum is (9/16,1/16,...,1/16), its marginals are 1/4, H_h=4-(9/16)log 9, I_h=3/4, and K_h=3h2(1/4)-H_h>0. The strict KL sign follows because this full-support spectrum is not product. A036's direct formula, also rechecked here, gives v_0=1, v_1=3/256 per singleton, v_2=9/256 per pair, v_3=27/256, Z_h=319/256 and T_h>0. All nonzero v_U<1 except v_0, so T_h is strictly positive without a numerical sign assumption.

For G_a=F_a*h on disjoint variables, actual phases and b tensorize. Hence

    H(G_a)=2a+H_h, I(G_a)=a/2+7/4,
    K_supp=-log w_a, K_shape=K_h, TC=-log w_a+K_h,
    Z=w_a^2*(319/256), T=-2log w_a+T_h.

Because -log w_a ->log2 e, the four strictly positive credit ratios to H satisfy

    a*K_supp/H ->(log2 e)/2,
    a*K_shape/H ->K_h/2,
    a*TC/H ->(log2 e+K_h)/2,
    a*T/H ->(2log2 e+T_h)/2.

Likewise T/(M-T/4)=Theta(1/a), since M=H+TC=2a+O(1). This supplies positive, quantitative credit-insufficiency witnesses with both support and normalization retained. However H/I ->4; finite-price influence can pay the growing residual. In particular this example is NOT a refutation of M<=T/4+cI for sufficiently large c.

### 2. A best-coordinate obstruction with every posterior KL positive

For even k>=4 let b_k(x)=(-1)^(x1*x2+...+x_(k-1)*x_k) in 0/1 coordinates, delta=2^-k and s=sqrt(delta). Flip its value at x=0: g_k=b_k-2*1[x=0]. The two-bit Walsh transform is (1,1,1,-1)/2; tensorizing shows c_T=s*sigma_T, sigma_T in {+1,-1}, with sigma_T=(-1)^(T1*T2+...). Point surgery subtracts 2delta from every coefficient. Thus

    P_T=delta*(sigma_T-2s)^2,
    count(sigma=+)=(2^k+2^(k/2))/2,
    count(sigma=-)=(2^k-2^(k/2))/2.

This is full support for k>=4. Flipping the central value toggles exactly one edge in each direction, giving d_i=1/2+2delta. Pair permutations and swaps within a pair act transitively on all physical coordinates and fix x=0; all B_i and J_i are equal. With the partner bit absent, sigma is unchanged on toggling i, hence the conditional spectral bit is exactly fair. With the partner present the signs are opposite. The latter pairs have total probability (1+4delta)/2 and conditional probability

    q=(1-2s)^2/[2(1+4delta)]=1/2-2s/(1+4delta).

The same-sign pairs have total probability (1-4delta)/2. Therefore the exact formula is

    B_i=(1-4delta)/2 +(1+4delta)/2*h2(q),
    J_i=h2(1/2+2delta)-B_i.

J_i>0 follows directly: same-sign pairs have positive mass and conditional probability 1/2, different from the unconditional d_i. Zero mutual information would require equality on every positive-mass packet. This proves strict positivity at every coordinate, not just nonnegativity.

The Taylor expansion h2(1/2+t)=1-2t^2/ln2+O(t^4), with its bounded fourth derivative on |t|<=1/3, gives

    B_i=1-4delta/ln2+O(delta^2),
    J_i=4delta/ln2+O(delta^2),
    J_i/B_i~4*2^-k/ln2 ->0,
    B_i/d_i ->2.

In particular every minimizer of B_i/d_i has the same vanishing credit fraction. To check global TC, write P_T=2^-k*(1+u_T), u_T=-4s*sigma_T+4delta. Under uniform spectral indices E u=0, E u^2=16delta(1-delta). For sufficiently large k, |u|<=1/2, and (1+u)ln(1+u)=u+u^2/2+O(|u|^3) with uniform remainder. It follows that D(P||Unif)=8delta/ln2+O(delta^(3/2)). Also D(Q||Unif)=k*(1-h2(d_i))=O(kdelta^2). Hence TC=8delta/ln2+o(delta), H=k-8delta/ln2+o(delta), and TC/H~8*2^-k/(k ln2). TC=K_shape>0; K_supp=0 exactly because support is full, and is not described as a positive credit.

This controls the erasure residual itself, rather than a merely large unrelated marginal entropy. It refutes J_i>=c*B_i at some coordinate for a fixed c>0, even allowing best-coordinate selection. It does not refute B_i<=K*d_i, which holds asymptotically here with K just above 2. Posterior extraction and influence payment are different tests.

The normalized collision term is also positive and insufficient on this SAME full-support family. Since s>2delta, surgery preserves every Fourier sign; these signs are the tensor products of the two-bit phase (+,+,+,-). With d=1/2+2delta the signed reference on each pair is ((1-d),sqrt(d(1-d)),sqrt(d(1-d)),-d). Its autocorrelations are C_0=1, C_10=C_01=2(1-2d)sqrt(d(1-d)), C_11=0. Put v=4(1-2d)^2*d*(1-d)=16delta^2-256delta^4. Then 0<v<1, Z=(1+2v)^(k/2), and

    T=k*v*log2(1/v)/(1+2v) ~32*k^2*delta^2,
    T/(sum_i B_i) ~32*k*delta^2 ->0.

Thus all k posterior KLs, TC=K_shape, and normalized T are strictly positive yet negligible compared with their specified unpaid erasure/entropy bills. K_supp is correctly zero because there is no support loss; the addressing tensor supplies the separate witness with strictly positive support loss as well. This does not falsify a collision lower-payment inequality TC>=T/4-kappa I: here TC is much larger than T and that lower payment is easy. The missing recovery of entropy is the relevant insufficiency.

### 3. Why B05 is not the best-coordinate insufficiency witness

Use the specified B05 construction with even k, r=2k, p=2^-2k, delta=2^-k, s=sqrt(delta), selector disagreement d=pdelta and A=1-s+delta. The exact parent Fourier coefficients, indexed by data T, control U and selector Y, are

    Y=0: 1[T=U=empty]+p*(c_T-1[T=empty]-delta),
    Y=1: d at every (T,U).

They come directly from 1+A(z)*(b(x)-1)-2*y*A(z)*1[x=0], with y=(1-chi_selector)/2. The coordinate influences are

    data: p/2+d; control: p*A; selector: d.

B05's explicit selector packets give B_selector=d*(k+log2 e+o(1)); expanding h2(d)=d*(3k+log2 e+o(1)) yields

    J_selector/h2(d) ->2/3, J_selector/B_selector ->2.

For a control coordinate, all Y=0 pairs have equal masses except the pair consisting of the all-empty coefficient and a control singleton. Write E(u,v)=(u+v)h2(v/(u+v)). The exact formula is

    B_control=2p*A-2p^2*A^2 + E((1-p*A)^2,p^2*A^2).

The Y=1 contribution d cancels the -d in the nonexceptional Y=0 mass. The exceptional term is O(kp^2). Thus B_control=2p*(1+o(1)).

For a data coordinate, restrict to Y=0 pairs with nonempty residual data index. Both coefficients have magnitude p*s*(1+O(s)); their pair entropy is their pair mass times (1+O(delta)). Their total mass is p*(1+O(s)). The omitted pairs have residual data index empty. For U nonempty their large/small masses are p^2*A^2 and p^2*(s-delta)^2; summed over fewer than 1/p controls their entropy is O(kpdelta). For U empty, their entropy is O(kp^2delta). These bounds follow from E(u,v)<=v*log2((u+v)/v)+v/ln2 when 0<v<=u. The Y=1 contribution is d. Consequently B_data=p*(1+o(1)). All bounds are uniform over the coordinates in their class.

Therefore B_data/d_data ->2, B_control/d_control ->2, whereas B_selector/d_selector~k. For all sufficiently large k a best coordinate is data or control, and

    min_i B_i/d_i ->2,
    J_best/h2(d_best) ->1.

This is the requested best-coordinate test with the opposite outcome from insufficiency. The exact k=2,4 computations are consistency checks, not a claim about all-k minimizer classification at finite k.

### 4. Sparse tribes: normalized credit remains large enough

Let there be t=w disjoint blocks of width w, p=2^-w, b=(1-p)^t and f=2*prod_j(1-1[block_j=0])-1. For w>=3, b>1/2. A nonempty Fourier set hitting j blocks has coefficient 2*(1-p)^(t-j)*(-p)^j. The empty coefficient is 2b-1>0, so the sign pattern is exactly the product of the point-defect block phases. All coefficients are nonzero; Q(A)=1, K_supp=0. Every marginal is d=2p*(1-p)^(t-1), I=t*w*d, M=t*w*h2(d).

The same signed-reference block calculation as A036, now with this d rather than d=2^(1-w), gives for a difference set of size j within one block

    v_0=1,
    v_j=[4d(1-d)]^j*[1-2^(2-j)*(1-d)^(w-j)]^2,
    Z_block=sum_j binom(w,j)*v_j,
    T=t*sum_j binom(w,j)*v_j*log2(1/v_j)/Z_block.

This keeps Z exactly and uses actual product-compatible phases. Since w^2*d ->0, the singleton mass is v_1=4d*(1+O(wd)), Z_block=1+O(wd), and its raw entropy is 4*w*d*(log2(1/d)-2+o(1)). The j>=2 terms have total entropy O(w^3*d^2): for large w, j=2 has the extra vanishing bracket, while j>=3 has bracket bounded away from zero and at most one; summing binom(w,j)*(4d)^j*j*O(w) gives the asserted upper bound. Dividing by w*d makes that remainder o(1). Thus

    T/(4I)=log2(1/d)-2+o(1)=w-3+o(1),
    M/I=log2(1/d)+log2 e+o(1),
    (M-T/4)/I ->2+log2 e.

The exact entropy formula, with v=4b(1-b) and e=(2b-1)^2, is

    H=e*log2(1/e)-v*log2(4b^2)+8*b*t*p*log2((1-p)/p).

Here tp->0, so H/I->4 and (TC-T/4)/I ->log2 e-2. Thus TC is asymptotically T/4 up to an ordinary influence-sized adjustment. This family does not furnish tiny collision credit; it supplies a surviving calibration. No conclusion about balanced/dense tribes is inferred.

### 5. First unsupported universal line

None of these calculations bounds sum B_i for arbitrary Boolean f by O(I), or constructs a nonreusing tree payment after reference resets. The first unsupported universal step would be to infer that the tiny-credit bent example cannot be paid by influence, or that sparse-tribes calibration implies a universal collision theorem. Both inferences are unjustified. Conversely one cannot infer small posterior credit at the best B05 coordinate from its bad selector split.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs are out/FROZEN_SPEC.json and out/FROZEN_SPEC_BENT_REPAIR.json. The latter was saved before testing the replacement family. Commands, from this run: `python -X utf8 -c "import subprocess; subprocess.run(['python','-X','utf8','code/check.py'],check=True,timeout=60)"` and the same wrapper with code/bent_repair.py. Exact checks use integer Walsh transforms, Fraction probabilities, Parseval, physical edge counts, complete signed coefficient comparison for B05 k=2,4, addressing character orthogonality a=1..4, grouped B05 selector k=4..32, sparse-tribes widths 2,3,4,6,8,12,16,24,32 (width 2 is explicitly excluded by the positive-empty-phase hypothesis), and bent packet multiplicities k=4..32.

Log intervals use range reduction to [1,2), outward dyadic argument brackets with denominator 2^96, 18 terms of ln x=2*sum t^(2j+1)/(2j+1), t=(x-1)/(x+1), and remainder <=2*t^37/[37*(1-t^2)]. When the main checker's reduced argument x satisfies 0<=x-1<2^-80, it uses the exact elementary enclosure u-u^2/2<=ln(1+u)<=u with u=x-1 instead; this preserves relative accuracy without long rational series. Division by positive ln2 bounds and signed endpoint handling are exact. Assertions of strict KL/collision signs use these intervals or the analytic proofs above. A relative-width check requires every grouped selector B/d interval to have width below 10^-8; this prevents a valid but too-wide absolute interval from producing a misleading midpoint at d=2^-96. Exported floating ratios are explicitly illustrative and are not serialized certified endpoints. Code outputs out/verification.json and out/bent_repair.json record checks and observed runtimes. The slow pilots, termination, premature output read, and relative-resolution refinement are documented in out/PILOT_CORRECTION.md; no failed pilot output is accepted.

Final executions passed 8,461 assertions in code/check.py (6.158 seconds inside the script) and 49 in code/bent_repair.py (0.497 seconds): 8,510 total. At k=32 the B05 selector B/d midpoint is 33.4426950475 with certified width below 1.3*10^-17, consistent with k+log2 e. On the bare bent surgery at k=32, J_i/B_i is about 1.344*10^-9 and T/(sum B_i) about 5.204*10^-17. These decimal displays illustrate the separately proved asymptotic statements.

## proof dependencies and changed downstream conclusions

Proofs use direct Walsh expansions, Booleanity autocorrelation, entropy/KL identities, elementary Taylor remainder bounds and explicitly derived packet multiplicities. A036 supplies the definition under test and B05 supplies the named family, not an unreviewed universal premise. One bundled candidate is saved; independent review is pending. The existing B08 review backlog prevents treating this as a new accepted broad theorem.

A036/A038 must keep support loss and distinguish completed from restricted b before using the addressing test. A037/A039/A064 receive a warning that mere positive posterior KL does not guarantee a fixed positive fraction of erasure payment, together with the explicit best-coordinate bent control. A089/A087 receive the B05 coordinate distinction. B20 should preserve both the insufficiency statement and its influence-payment scope. No FEI disproof is claimed.

## one next mathematical action and independent reviewer

Next: in A037's physical lift, evaluate the complete node debt B_i minus a single-use posterior rebate on the bent point-surgery control, using a data-coordinate-first stopping tree and retaining terminal entropy. Compare the resulting nonlocal bill with the actual queried influence; do not require any positive fraction of the bill to come from KL. A088 should independently reconstruct the exact bent pair formula and transitive coordinate symmetry. A094 should check addressing support conditioning, Z and the distinction between entropy-fraction insufficiency and failure of an influence payment.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code, frozen specs and outputs are saved solely under the assigned A040 run. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/save_receipts.json records file sizes and SHA256 after finalization. Supervisor copying, mirror verification, adoption and independent review are not observed. No shared file, other agent folder, brain store or repository was modified; no messages were sent.

**Universal bridge:** This stage moves the B08 posterior-credit target feeding C018 erasure and C019 stopping-tree payment by excluding fixed positive-fraction KL extraction even at the best physical coordinate, with the exact rate 4*2^-k/ln2. It also gives support-exact positive global credit ratios Theta(1/a), preserves sparse-tribes collision calibration, and prevents a false best-coordinate obstruction from B05. The remaining universal obligation is a nonreusing influence payment of the residual erasure after reference resets, with terminal entropy retained. The next action is the shortest route because it tests the live full ledger precisely where the proposed credit is negligible, rather than proving another isolated class FEI bound.
