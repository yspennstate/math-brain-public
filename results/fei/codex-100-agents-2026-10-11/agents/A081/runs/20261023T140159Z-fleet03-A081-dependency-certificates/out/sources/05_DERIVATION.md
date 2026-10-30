# Independent chain review and smaller-padding extension

## 1. Scope, actual owner, and dependencies

Information is in bits. All references are actual subprobabilities of mass at most one, positive on the actual true support. Physical reach is lambda. A reset from Q to R is charged lambda[CE(P,R)-CE(P,Q)]; positive-part booking uses its maximum with zero. Every complementary terminal reference and its full CE, every prior charge and every old external U remains in the ledger. References are never normalized for free.

Reviewed: A086 20261023T114749Z GENERAL_HANDOFF.md, SOURCE_PATH_PAYMENT.md, POSITIVE_HANDOFF.md and RECONSTRUCTION.md. The actual two-reset chain uses A095-TWO-NARROW-RESETS-SAME-RATE4-BANK@1, independently reconstructed in A094 stage18. The owner-bank interface uses the original A011 v2 prescribed floor, not arbitrary edits in A011 v4. Its source, padding and root chain and the larger allowance were reconstructed in A094 stage19. No source proof repair is used to accept the two named A086 claims. A094 authored the larger-allowance dependency; that dependence is disclosed. A086's current immutable claim record includes its independent full-scope review of that allowance in RECONSTRUCTION.md.

## 2. Full canonical-to-floor analytic chain

Let g have a source bits, m untouched dummy bits and one fair unqueried point selector. Translate the distinguished point to zero and negate globally so g(0)=1; this preserves squared laws and all costs. Put epsilon=2^(-a-m), u=2^-m, and let A range over the N nonzero signed Walsh coefficients of g. Then sum A=sum A^2=1, N<=2^a, |A|>=2^-a and N epsilon<=u. These include constant sources and a=0. Set M=1/epsilon and W=2epsilon-N epsilon^2.

The Boolean full-point edit has joint true weight (A-epsilon)^2 at old selector-zero masks and epsilon^2 at every remaining joint mask. Its canonical reference is (1-W)A^2 at old masks and epsilon^2 elsewhere. Thus its divergence Dcan is exactly the sum over old masks of (A-epsilon)^2 log2[(A-epsilon)^2/((1-W)A^2)]. Its true data marginal q is A^2-2epsilon A+2epsilon^2 on old masks and 2epsilon^2 elsewhere. The prescribed exact-source floor data is R=(P_g+3epsilon Uniform_M)/(1+3epsilon); lift by the TRUE conditional selector law. The full floor divergence Dfloor equals D(q||R), with no omitted selector or complementary cost.

Writing L=(sum A^-2)^(1/2)<=2^a sqrt N, the old-data chi-square square root is at most

epsilon[3+2sqrt N+epsilon(6sqrt N+L)+6epsilon^2 L]/sqrt(1+3epsilon)

and hence at most epsilon sqrt N[5+6epsilon+u+6epsilon u]/sqrt(1+3epsilon). This follows directly by expanding q-R and the weighted Euclidean triangle inequality; R>=A^2/(1+3epsilon). The exact off-support chi-square contribution is (M-N)epsilon^2(1-6epsilon)^2/[3(1+3epsilon)]. The bit divergence is at most chi-square/ln 2 <3 chi-square/2 whenever chi-square>0. The strict elementary bound ln 2>2/3 follows by integrating its positive atanh series, already used by the interval checker.

For m>=8 the old bracket is <6, so Dfloor<54N epsilon^2+epsilon/2<=91epsilon/128. The canonical chi-square triangle estimate is sqrt[(1-W)chi-square]<=epsilon sqrt N(4+u)<(33/8)epsilon sqrt N. Since 1-W>=127/128, Dcan<26N epsilon^2<=13epsilon/128.

For the off-source data event x=2epsilon(1-N epsilon), y=3epsilon(1-N epsilon)/(1+3epsilon). At m>=8, 0<x<y<=3epsilon and y-x>15epsilon/16. Binary KL curvature gives Dfloor>=d2(x||y)>75epsilon/512. Therefore 23epsilon/512<Dfloor-Dcan<epsilon. The conditional NONEMPTY shape genuinely changes: comparing selector-one old and off-source masks would force A(A-6epsilon)=0 if the reference ratios matched. Quantization |A|>=256epsilon excludes this, even for constant g.

For any finite-cost incoming subprobability Q, CE(P,Q)-H(P)=D(P||Q)>=0, including its mass penalty. Therefore its actual positive conversion debit is <lambda epsilon. No positive lower bound is claimed for arbitrary incoming Q. These inequalities verify the full scope of A086-UNIFORM-FLOOR-CONVERSION-SOURCE-PATH-PAYMENT@1, not just finite tested sources.

## 3. Source path and full ledger

On a path querying d<=a distinct source coordinates, lambda_k=lambda 2^-k and epsilon_k=2^k epsilon. Installing the exact-source floor on entry and after each query therefore has total positive booking <(d+1)lambda epsilon. For nonconstant original g, the cube's minimum nonzero boundary gives I_g>=2a 2^-a, so (d+1)epsilon<=(a+1)2^-a u<=u I_g. Descendants can be constant; no influence assumption about them is made. An unexecuted query needs no floor.

Each query retains both inherited references, the old reference mass, all sibling costs and the full signed release; release is nonnegative by the inherited-reference inequality. The actual original CE plus signed resets minus signed releases equals the complete current frontier CE plus the accumulated signed ledger. Replacing each new reset charge by its positive part increases this complete bill by no more than the sum just bounded. Thus this is a payment in the actual original account, not a new source bank.

At the actual A011 v2 R-based floor root, the stage19 all-frontier allowance leaves 7I_g/8 after retaining U<=(C0+37/8)I_g at the original K=4C0+15. Switching prospectively to this SOURCE-FIRST policy costs <I_g/256 for m>=8 and leaves >223I_g/256. It does not retroactively change an executed padding-first path. All untouched finite-cost compatible terminals stay fully retained.

## 4. Actual two-reset rate-four chain

The independently reconstructed A095 two-reset baseline starts with h4*h2, original rate four and canonical reference. For every dummy stock and eta in[0,1/4], its original slack exceeds 451/256, and the two executed positive narrow resets are respectively <5/4 and <1/2. Remaining slack therefore exceeds 3/256. On actual child 00 (reach1/4), the source is -h4 with its actual canonical reference, untouched dummy bits and fair selector.

Here the 16 coefficients are -7/8 once and 1/8 fifteen times. Direct substitution sharpens the old chi-square bound to (11epsilon+56epsilon^2+192epsilon^3)/sqrt(1+3epsilon)<12epsilon for epsilon<=1/4096. Thus Dfloor<216epsilon^2+epsilon/2<epsilon, Dcan<200epsilon^2, Dfloor>epsilon/8, and (Dfloor-Dcan)/4>epsilon/64; its upper bound is epsilon/4. The shape comparison has nonzero cross product -7epsilon/32-3epsilon^2/4-6epsilon^3. For m>=8, epsilon<=1/4096. Entry booking is <1/16384, leaving >191/16384. All five possible source-path floors together cost <5/16384, leaving >187/16384. Both previous resets, their original rate and every complementary terminal remain. This verifies the full named A086-ACTUAL-TWO-RESET-FLOOR-HANDOFF-SAME-RATE4@1. No selector query or padding reset has thereby been paid.

## 5. New extension: upper-cost payment for m>=3

This is a separate A094 claim, not a repair or silent widening of A086. For 0<epsilon<=u<=1/8, put A0=5+u and B0=6(1+u). Then

3A0^2-2A0 B0-B0^2 u=15-78u-81u^2-36u^3>=501/128>0.

Consequently (A0+B0 epsilon)^2<=A0^2(1+3epsilon). The old-data chi-square contribution in section2 is at most (41/8)^2 N epsilon^2. Its off-support contribution is at most epsilon/3, since |1-6epsilon|<=1. It follows that

Dfloor<C(u)epsilon, C(u)=1/2+(5043/128)u.

This upper bound holds for EVERY source, including constants/a0. Therefore every actual finite-cost incoming subprobability has positive debit <C(u)lambda epsilon, and an actual source path has total positive booking <(d+1)C(u)lambda epsilon. For a nonconstant original source this is at most C(u)lambda u I_g. No positivity or genuine shape change is asserted at m=3 by this extension.

At m>=3, C(u)u<=5555/8192<7/8. Thus the original A011 floor root, same supplied source price C0, same rate K=4C0+15 and same old booking U<=(C0+37/8)I_g can pay EVERY such source-path positive conversion while retaining a reserve >1613I_g/8192. This is a prospective source-first continuation of an ACTUAL prescribed root. It neither erases prior executed padding history nor identifies unrelated references.

In the ACTUAL rate-four two-reset history of section4, m>=5 gives u<=1/32, epsilon<=1/512, C(u)<=7091/4096 and reach1/4. All five source-path floors cost <35455/8388608. The same original slack >3/256 leaves >62849/8388608. This proves upper-cost continuation for five dummy bits; it does not claim that the entry reset is positive for all m in this extension. The eight-bit A086 conclusion has a stronger numerical reserve on its narrower domain, consistently with this extension.

## 6. First unsupported universal line and audit limits

No unsupported line remains in the two explicitly reviewed A086 claims under their exact hypotheses. The new A094 extension has an analytic proof and exact finite checks but awaits independent review. None supplies CE(P_g,R)<=C0 I_g for arbitrary unknown g at one universal C0, pays arbitrary selector collapse, or admits arbitrary interacting edits in a fixed ambient bank. That initial influence-priced supplier remains the first missing universal implication. Arbitrary initial suppliers and general selector exposure are not consequences of a smaller padding constant. Exact finite checks corroborate the implementation and full-ledger identities; they are not a census proving arbitrary g.
