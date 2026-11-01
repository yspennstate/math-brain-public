# A040 stage 2: odd-face debit versus posterior credit on one overlapping-control tree

## exact target, quantifiers, hypotheses and units

Bits throughout. For a Boolean sign f on a uniform physical cube let P(S)=fhat(S)^2, d_i=Inf_i, H=-sum P log2 P, I=sum d_i, B_i=H(S_i|S_-i), J_i=h2(d_i)-B_i, TC=sum h2(d_i)-H. J_i is the spectral-coordinate posterior mutual information; it is NOT the physical-child JS information, an occupancy KL, or a leaf-reference KL. At a physical split with children f0,f1 the odd-face debit is Q_i=I(f0*f1)/2. The strict K=4 bad set is B_i>4d_i; equality is good.

This stage consumes A098's source-bound reallocation: audit localized odd-face versus posterior credit on a prescribed overlapping-control tree, retaining terminal CE. B08 v2's minimum-ratio census/calibration direction is stale in that scope: A071/A082 have completed the five-bit census, and A001/A040/A089 already solved B05 best-coordinate calibration. No fresh random census or duplicate B05 calculation was run. This departure is recorded in STATUS.md. A098's dispatch delta is a saved mathematical direction, not evidence that a schedule or shared index was changed.

The fixed overlap mask is C(z)=1[z0=0]*(1[z1=0] OR 1[z2=0]). It represents two events sharing their physical common control z0 and the same data core. Put alpha=EC=3/8, L=I(C)/2=5/8. For even k>=4 use b_k(x)=(-1)^(x1*x2+...+x_(k-1)*x_k), b'_k=b_k-2*1[x=0], and define

    F_k(x,z,y)=1+C(z)*(b_k(x)-1-2*y*1[x=0]).

The adaptive tree queries selector y first, then the common control, then z1, and z2 only if z1 fails. It stops at a constant or at b_k/b'_k; no data coordinate is queried and no irrelevant resolved control is queried. Let delta=2^-k and s=sqrt(delta). We prove:

    B_root=alpha*delta*(k+log2 e+o(1)),
    J_root=alpha*delta*log2(8/3)+o(delta)>0,
    Q_root=alpha*delta*(k+5/3),
    J_root/B_root~log2(8/3)/k ->0,
    Q_root/J_root~k/log2(8/3) ->infinity.

All control descendants are strictly good at K=4. The selector is bad for every even k>=4, so Q_bad=Q_root. Moreover

    Q_bad/I(F_k)<=17/176, with equality at k=4,
    Q_bad/I(F_k)~2delta ->0.

Native terminal references are uniform on the k data spectral bits and deterministic on any irrelevant unqueried controls. They give CE_leaf=alpha*k, retained exactly, with CE_leaf<=2 I_leaf. These are explicitly native leaf references; this stage does not identify their average CE with a cross entropy against an unspecified root reference.

Independent review target: A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER@1, accepted at its stated scope by the reconstruction below. The new root-credit comparison completes A040's existing insufficiency packet under the review-cap guard; it is a scoped test, not a new broad universal payment candidate.

## sources actually read, revisions and theorem locators

Stage-start BOARD.md, supervisor snapshot 2026-10-13 21:14 UTC; B08 STREAM_NOTES v2, 2026-10-11 23:35Z; own STATUS and LEARNED; EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2. Read A098 run 20261012T024601Z REPORT, especially its retirement rationale and route-2 reallocation, and CHECKPOINT_ALLOCATION.json's A040 acceptance test. Read A071 run 20261011T233808Z REPORT for the full five-bit constant and duplicate-search guard; A089 run 20261012T044049Z REPORT was loaded for its completed calibration/descendant frontier. These are navigation sources, not assumed universal proof premises.

Critical originals: A023 run 20261012T010933Z REPORT sections 2-5, OVERLAP_GOOD_NODE_PROOF.md and CLAIMS.json; B05 lead run 20261011T225000Z REPORT sections 2 and 5, and B05 STREAM_NOTES v2; A039 run 20261011T223903Z DERIVATION.md/CLAIMS.json for the compensated TC identity; A064 run 20261011T224431Z REPORT for the terminal-corrected budget boundary. Prior A040 REPORT sections 2-3 supplies the bent surgery conventions and preserved tiny-credit mechanism. Earlier paper/context files remain prior-stage context; no new external theorem or Internet source is used here. Whole-file loads do not constitute review of unrelated claims. out/SOURCE_RECEIPTS.json records exact local bytes read and hashes; live board/status files may change after intake.

## complete derivation or exact first unsupported line

### 1. Independent reconstruction of A023's all-width control result

Take any independent Boolean core g, a=1-Eg>=11/16, compatible common point controls of width s0>=0, and two exclusive point blocks of widths r,t>=1. Write u=2^-s0, p=2^-r, q=2^-t, beta=p+q-pq. The physical event union is A_s0*(A_r OR A_t). A common-control edge is pivotal exactly when its other common controls match, the union occurs, and g=-1. An exclusive edge also needs the other exclusive event to fail. Direct edge counting therefore gives

    I_ctrl=u*a*[s0*beta+r*p*(1-q)+t*q*(1-p)],
    I_leaf=u*beta*I(g), H_leaf=u*beta*H(g).

The terminal probability is u*beta, not u*(p+q); the intersection and the shared core are counted once. All paths query each physical control at most once.

At a first-exclusive split with l controls remaining, set rho=2^-(l-1). With C0 the independent competing event, the two children are

    f0=1+C0*(g-1),
    f1=1+[C0+(1-C0)*A_(l-1)]*(g-1),
    d=a*rho*(1-q)/2.

In every Fourier packet with a nonempty label among the l-1 remaining fresh controls, f0 has coefficient zero. The parent pair then has equal squared masses, so its erasure is twice its mismatch mass. The point indicator has empty-label squared-mass fraction rho. Exactly 2(1-rho)d of erasure is thus already accounted for; the remaining packets have total mismatch rho*d and total packet mass at most one. Concavity of binary entropy and monotonicity of m*h2(e/m) in m give

    B/d<=2(1-rho)+rho*log2(e/(rho*d)).

If a(1-q)>e/8, this is strictly less than 2+2rho*(1+log2(1/rho))<=4, since rho=2^-j and (j+1)2^-j<=1 for every integer j>=0. Here q<=1/2 and a>=11/16, hence a(1-q)>=11/32>e/8. The condition depends on the actual node, not an assumed unsigned mismatch channel.

For a constant-child split, independently write its nonconstant child mean as 1-2d. The nonempty residual Fourier packets have equal parent pair masses, while the empty packet masses are (1-d)^2,d^2. Thus, with E(v,w)=(v+w)h2(w/(v+w)),

    B=2d(1-d)+E((1-d)^2,d^2).

Define the signed scalar A(d)=d-d^2+d^2 log2(((1-d)^2+d^2)/d^2), continuously at endpoints. The difference B-A is d-d^2+(1-d)^2 log2(1+d^2/(1-d)^2), at most d-d^2+(log2 e)d^2<=d*log2 e. Since the packet sum is at most one and d log2(1/d)<=1/(e ln2),

    B/d<=1+log2 e+2/(e ln2)<4.

This includes negative child means and d=1; d=0 has zero bill. This derivation uses the actual parent spectrum and does not identify signed mismatch with the magnitude minority. For genuine magnitude-minority debt lambda, lambda<=B follows directly by dropping the positive companion entropy term, so A023's stated lambda bounds also follow.

Exact analytic constants are ln2>56/81 and 65/24<e<65/24+1/100<11/4. They follow respectively from two positive atanh terms and the exponential series through degree four with the remainder bounded by a geometric tail from 1/5!. These imply the strict threshold and the stated constants 4+2/ln2<7 and 4+3/ln2<9. With JS<=2d/ln2 and the exact entropy/influence telescopes, all A023 preterminal cost bounds follow. For its fair bent-surgery terminal class, H(g)<=k+1 and I(g)>=k/2-(k-1)delta>=7k/16, so H(g)/I(g)<=20/7<3; its mean gives a>=1-s-delta>=11/16. This reconstructs the full stated scoped class result without repairing it. Verdict: HOLDS_AT_STATED_SCOPE, locally independent acceptance. The source contributor remains A023; A040 is a reviewer, not a repairing contributor.

### 2. Exact overlap selector packets and the positive but insufficient KL

The two-bit bent Walsh spectrum is (+,+,+,-)/2. Tensoring gives b_hat(T)=s*sigma_T and sum_T sigma_T=2^(k/2). At the selector split the two actual child coefficients are those of 1+C(b-1) and 1+C(b'-1). Their difference is 2delta*C_hat(U) for every data label T. For T nonempty the midpoint is (s*sigma_T-delta)*C_hat(U). Thus

    e_(T,U)=delta^2*C_hat(U)^2,
    q_(T,U)=C_hat(U)^2*((s*sigma_T-delta)^2+delta^2).

Summing over U multiplies the nonempty-data erasure by sum C_hat(U)^2=alpha. There are (2^k+2^(k/2))/2-1 positive nonempty data signs and (2^k-2^(k/2))/2 negative ones. For empty data, nonempty controls contribute with total squared-mask mass alpha-alpha^2, midpoint factor s-1-delta, and mismatch delta^2; the all-empty packet has midpoint 1+alpha*(s-1-delta) and mismatch alpha^2 delta^2. These four packet classes are explicit, normalized and used by the grouped exact checker.

In the nonempty-data packets theta=e/q=delta*(1+O(s)) uniformly. Their mismatch total is alpha*delta*(1-delta). Applying h2(theta)=theta*(log2(1/theta)+log2 e+O(theta)) gives their erasure alpha*delta*(k+log2 e+o(1)). The empty-data control packets have mismatch O(delta^2), so their entropy is O(kdelta^2)=o(delta); the all-empty packet obeys the same bound. Consequently

    B_root=alpha*delta*(k+log2 e+o(1)).

Since d=alpha*delta, h2(d)=alpha*delta*(k+log2(1/alpha)+log2 e+o(1)), proving J_root=alpha*delta*log2(8/3)+o(delta). Strict positivity for every k>=4 also follows without asymptotics: both nonempty-data sign classes have positive mass, and their conditional selector probabilities delta^2/((s-delta)^2+delta^2) and delta^2/((s+delta)^2+delta^2) differ. A zero posterior MI would require equality on every positive packet.

For k>=8, q/e>=1/(4delta) on all nonempty-data packets gives B_root/d>=(1-delta)(k-2)>4. The finite k=4,6 rational sign certificates close the remaining two even endpoints. Thus the selector root is bad for all even k>=4. Positivity alone pays no fixed fraction of its bill: J_root/B_root~log2(8/3)/k.

### 3. Root face ownership, exact budget and retained terminal CE

The root child product is 1-2*C*1[x=0]. Its data edge contribution to influence is 2alpha*kdelta and its control contribution is delta*I(C). Direct enumeration of the eight control assignments gives EC=3/8 and I(C)=5/4. Therefore

    Q_root=I(child product)/2=alpha*delta*(k+5/3).

After the selector is revealed, each terminal core is b or b'. Their deficits are 1-s and 1-s+2delta, both at least 3/4 for k>=4. The independent A023 reconstruction applies; every control descendant is good. The only bad debit is therefore Q_root. This debit is a set of actual odd faces charged at their first revealed direction, not a posterior KL and not a second claim on a control influence account.

The one-flip physical edge count gives I(b)=k/2, I(b')=k/2+2kdelta, and selector-core influence delta. Setting a=1-s+delta yields the exact resources

    I(F_k)=alpha*(k/2+(k+1)delta)+a*L,
    I_removed=alpha*delta+a*L,
    I_leaf=alpha*(k/2+kdelta),
    I(F_k)=I_removed+I_leaf.

These are the same physical tree's accounts. In particular the common control is not assigned once to each event; L=5/8 is the actual union's single account. Since I(F_k)>=alpha*k/2,

    Q_bad/I(F_k)<=2delta*(1+5/(3k)).

For k>=6 this is at most 23/576<17/176. At k=4, the exact values are I=11/8, Q_bad=17/128, hence ratio 17/176. This proves the stated all-k maximum; as k->infinity I(F_k)~alpha*k/2, so Q_bad/I(F_k)~2delta. Q_bad/J_root~k/log2(8/3) diverges despite this vanishing global price. This is insufficiency of the named KL credit, not a disproof of FEI or of ordinary influence payment.

At every active leaf choose Q_leaf uniform on the data subsets and put probability one on absence of any irrelevant control labels. It is a normalized reference on the leaf's full positive support. CE_leaf_node=k for both b and b'; constants use their deterministic exact reference. The total active leaf probability is alpha, so

    CE_terminal=alpha*k,
    H_terminal=alpha*(H(b)+H(b'))/2,
    KL_terminal=CE_terminal-H_terminal>=0,
    CE_terminal<=2 I_leaf.

For example k=4 retains CE_terminal=3/2 and I_leaf=27/32. No terminal entropy is deleted because the activation is rare. The root payment can be verified directly without importing an isoperimetric premise: B_root<=h2(d)<=d*(k+log2(8/3)+log2 e)<=Q_root+(log2 e)d, since log2(8/3)<5/3, equivalently (8/3)^3<2^5. Controls satisfy B<4d by the independent exposure proof. The exact physical entropy telescope then gives the complete native-leaf certificate

    H(F_k)<= (4+2/ln2)*I_removed+Q_bad+CE_terminal
           <= (4+2/ln2+17/176)*I(F_k)<7I(F_k).

The scalar last sign follows from 1/ln2<81/56. The useful delta is the explicit localized face/credit distinction and single-use stopping ledger, not a novelty claim for FEI on this easy terminal class.

### 4. Compensated posterior ledger and the first unsupported line

At each actual split, define Gamma_i=sum_(j!=i)[h2(d_j(parent))-(h2(d_j(child0))+h2(d_j(child1)))/2]. Marginal influence averages exactly for j!=i. Combining TC=M-H, H-parent-minus-average-H=B+JS, and h2(d_i)-B=J_i gives

The universal scalar JS allowance used above is independently justified as follows. Put D(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2. On [0,1], D(z)<=1-sqrt(1-z^2), because atanh(z)<=z/sqrt(1-z^2), with the latter comparison following by differentiating their difference. For a parent amplitude pair u,v the packet JS is (u^2+v^2)D(2uv/(u^2+v^2))/ln2, so it is at most 2min(u^2,v^2)/ln2. Summation gives JS<=2d_i/ln2. Endpoints follow by continuity. The exact compensated identity is

    TC(parent)=J_i-JS_i+Gamma_i+average TC(child).

This is a new-family use of A039's identity, not a repeated universal census. The checker retains and compares exact prime-log vectors for

    sum w J_i + sum w Gamma_i + E TC_leaf = TC_root + sum w JS_i,
    sum w B_i + sum w JS_i + E H_leaf = H_root,
    sum w d_i + E I_leaf = I_root,
    sum w Q_i + E Q_leaf = Q_root_function.

Here Q_root_function is the full root odd-face potential, distinct from the selector node debit Q_root. Native terminal reference KL is CE-H, while terminal TC uses the product of its marginals; they are NOT identical on b'. Neither is pooled with the root posterior. No conclusion about the signed Bayes/occupancy reset portions of the entire A039 claim is inferred merely from these equalities.

First unsupported universal line: arbitrary overlapping controls with arbitrary cores admit a history-measurable stopping order whose K=4 localized face debit is O(I), whose required source-compatible reference reset is paid once, and whose actual terminal CE is uniformly certified. This stage proves that statement only for the declared two-event mask and the explicitly certified bent-surgery terminals. It neither builds a universal compatible root witness from the native leaf laws nor pays arbitrary terminal cores. A failure of the sufficient exposure criterion a(1-q)>e/8 is not itself a bad-node certificate.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was written before computation. Physical roots k=4,6,8,10, at dimensions k+4; grouped roots k=4,6,8,12,16,32,64. No randomness, omitted orbit, full-function census, automatic dimension escalation, GPU or >300 MB job was used. Memory estimate 90 MB; no memok gate required. Exact integer Walsh transforms, Fraction squared spectra and independent physical edge counts check Parseval and influences. Physical odd-face enumeration independently checks the total face telescope. Every K=4 badness sign and root positive-credit sign is decided with outward rational intervals; every entropy/TC telescope is checked by exact rational prime-log vector cancellation.

Command from this run directory:

    python -X utf8 -c "import subprocess; subprocess.run(['python','-X','utf8','code/audit.py'],check=True,timeout=60)"

Final result: 427 assertions passed, 4 physical roots and 7 grouped roots, script runtime 5.77254 seconds, plus six exact rational constant checks: 433 total. The first implementation made two harmless zero-influence queries after an event was already resolved; inspection caught this discrepancy with the prescribed stopping rule. It was corrected to stop as soon as remaining controls are irrelevant, and all final certificates were regenerated. The earlier run's 523 assertions are not reported as the final adaptive-tree certificate. An initial constant certificate also caught equality in a loose rational substitute for a strict bound; the stronger proved rational upper bound on e resolved it. Both corrections are preserved in out/CODE_CORRECTIONS.md.

Log bounds use range reduction to [1,2), 24 positive atanh terms and the tail 2*t^49/[49*(1-t^2)]. For arguments within 2^-40 of one, u-u^2/2<=ln(1+u)<=u is applied to the original exact rational. Signed vectors use the proper lower/upper endpoints. Compact saved endpoints are rounded outward to rational multiples of 10^-30; the exact vector and code regenerate the unrounded bounds. At k=64, B/d has interval width below 4*10^-20; midpoint displays are illustrative. Each root is flushed to out/RESULTS.json immediately.

Exact finite localized face ratios are 17/176, 23/882, 29/4304, 35/20358 for k=4,6,8,10. At k=64, J_root/B_root is approximately 0.02162 and Q_root/J_root approximately 46.41. The all-k conclusions are supplied by the analytic argument, not extrapolated from those displays. out/ANALYTIC_CONSTANTS.json separately checks the rational threshold and all-k max comparisons.

## proof dependencies and changed downstream conclusions

A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER@1 is independently reconstructed and locally accepted at its exact stated scope, with no author repair. The review record preserves the source claim and author attribution. B05 localization and A039 compensated TC are rederived for the exact use here; neither an unreviewed universal premise nor the full occupancy/reset theorem is imported. New scoped comparison proof dependencies are the reconstructed A023 v1 and the direct algebra in this run. The proof-dependency graph is acyclic.

A037/A039/A064 receive an exact overlapping-control tree where a positive root posterior is asymptotically negligible but the localized face debit is correctly single-use and globally affordable. A023/A046/A089 receive an audit separating exposure goodness, face reserve and terminal CE. B20/A098 may adopt the local review and note that the stale minimum census was consumed rather than repeated. No shared claim status is changed by this saved review; supervisor adoption remains separate. Source-compatible reference reset and arbitrary-core terminal payment remain open.

## one next mathematical action and independent reviewer

Next: replace the two exclusive events by three overlapping compatible masks and freeze one history where the residual competing-event probability exceeds the exposed range. Compute the actual B-4d sign, odd-face boundary and compensated Gamma/JS terms there, using one shared-coordinate account and retaining the core's native CE. A failed exposure bound alone must not be called a counterexample. This probes the first surviving overlap gap, not another minimum-ratio calibration. A088 is the assigned independent reviewer; A087 should challenge the exposure reconstruction and A094 the native-leaf versus compatible-root distinction.

## actual persistence receipts or precise save blocker

The four protocol files, this report, DERIVATION.md checkpoint, code, frozen specification, per-root results, analytic constant certificate, scoped review record and source receipts are saved in the assigned A040 run. STATUS.md has exactly two lines; WORKLOG.md is appended and LEARNED.md preserves stage-1 facts and the new overlap lesson. out/PERSISTENCE_RECEIPTS.json holds file hashes and byte sizes. No local persistence blocker exists. No git, other-agent/shared write, brain-store write, message or external publication occurred. Independent review of the new comparison, supervisor copying, mirror verification and downstream adoption have not been observed.

**Universal bridge:** This stage moves C019 stopping-tree payment and the B08 posterior-credit target by independently accepting the existing two-event control-exposure lemma and paying a prescribed overlapping-control tree with exact terminal CE, maximum localized face debit 17/176 of source influence, and a root face/posterior ratio growing as k/log2(8/3). It shows quantitatively why positive KL is insufficient locally while the odd-face reserve is still affordable, with all compensated TC and physical ownership terms retained. The universal localized-face bound, source-compatible reference resets and arbitrary terminal cores remain unpaid. NEXT is the shortest route because it tests the first unresolved multi-event exposure/ownership node, rather than repeating a completed census or adding a detached class FEI result.
