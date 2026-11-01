# exact target, quantifiers, hypotheses and units

The full target is: there exists one finite absolute C such that for every finite n>=0 and every actual Boolean sign f:{-1,1}^n->{-1,1}, on the uniform cube, H_2(f)=sum_S p_S log2(1/p_S)<=C I(f), where p_S=hat f(S)^2 and I=sum_S |S|p_S=sum_i epsilon_i. Zero masses contribute zero; constants have H=I=0. Natural logarithms are explicitly ln. Full FEI remains OPEN.

This packet consumes the new A098 assignment: audit the quantifiers, global normalizer and conserved influence budget of the higher-level reference after A096's reviewed T12 payment. It resolves a narrower mechanism question, not FEI: a complete spectral reference determined only by the influence vector cannot have universal cross entropy <=K I. Explicit exact obstructions also invalidate the all-degree product-influence reference and two entropy-majorant extensions of the fixed-layer proof. The references here are ideal subprobabilities; failure mass is retained and no integer prefix rounding is claimed.

# sources actually read, revisions and theorem locators

Read BOARD.md at stage start (supervisor snapshot 2026-10-13 21:34 UTC), B01 STREAM_NOTES.md v1, and own STATUS.md. B01's assigned X009/B05 minima were completed last stage. A098's CHECKPOINT_ALLOCATION.json, A001 delta, explicitly assigns the new all-degree quantifier/budget audit, with A086 reviewer; its REPORT.md supplies the reviewed A096 frontier. No productive child-deficit derivation had started. Consuming this new dependency follows protocol dispatch; it does not contradict B01's completed assignment. No shared assignment deployment is presumed.

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2; A096 stage2 REPORT.md equations (1)-(7), remainder definition and CLAIMS.json; A098 stage2 REPORT.md including the independent ordered-pair reconstruction; B20 SYNTHESIS.md sections 1,3,4; B12 STREAM_NOTES.md v2 for its no-reuse guard; A015 LEARNED.md, stage2 REPORT.md sections 3-5 and CLAIMS.json. A015's exchangeable-location identity is independently reconstructed below, accepted only at that slice; its complete bundled conditioning/ordered/regular-core theorem is not accepted by association. A045/A073/A096 durable notes were searched for duplicate influence-only reference work. Previous recovered manuscript inventories remain archived and are not rebuilt. Byte receipts for the critical sources are saved in out/SOURCE_MANIFEST.json.

# complete derivation or exact first unsupported line

## 1. The complete row, its normalizer, and the one original budget

For a relevant coordinate i, let h_i=(f(+1,x_-i)-f(-1,x_-i))/2. Actual Booleanity gives h_i in {0,+1,-1}, support probability and Fourier energy epsilon_i. Its complete row law is mu_i(T)=p_(T+i)/epsilon_i, T excluding i. Put q_i(T)=p_T+p_(T+i). Both mu_i and q_i are probability laws; q_i is the actual residual spectral marginal, not an unnormalized product prior. It is positive on the support of mu_i. With phi(x,y)=(x+y)h2(y/(x+y)), define

    B=sum_i sum_{T excluding i} phi(p_T,p_(T+i)),
    M_i=sum_T p_(T+i) log2((p_T+p_(T+i))/p_(T+i)).

Then exactly

    M_i=epsilon_i[log2(1/epsilon_i)-D(mu_i||q_i)],
    M<=B<=M+I/ln2,  M=sum_i M_i.                 (1)

The other half of phi is bounded by p_(T+i)/ln2, using ln(1+u)<=u. Terms with p_T=0 or p_(T+i)=0 are handled directly. For I>0, the global joint laws

    P(i,T)=p_(T+i)/I,
    Q(i,T)=(epsilon_i/I)q_i(T)

both have total mass one, and share the coordinate marginal epsilon_i/I. Consequently

    M/I=sum_i (epsilon_i/I)log2(1/epsilon_i)-D(P||Q). (2)

There is exactly one original influence budget I in (2). These are the previously known retained-KL/C018 identities, reconstructed as the audit's acceptance interface, not renamed as new progress. A new reference must specify its complete normalizer and any cost of replacing actual Q. Erasing the divergence, changing Q, or assigning a fresh whole I to every degree is not a paid reduction.

A096 proves T12<=16700/2187 I, supported by a special degree-one row suppression. With the lead's paid root term B_root, the remaining line is

    R_ge2=sum_{|S|>=2} sum_{i notin S} phi(p_S,p_(S+i))<=K I

for one K independent of dimension. One valid sufficient interface would assign nonnegative layer budgets J_m with sum_{m>=2} J_m<=I and prove the level-m bill <=K J_m with one K. Bounds <=K_m I separately at each m do not supply that interface. Equation (2)'s universal lower bound on retained KL is FEI-equivalent up to constants, not a weaker solved lemma.

## 2. Actual Boolean failure of an all-degree sparse-row extension

Let r>=4, delta=2^-r, A_r be the indicator of one control point, and

    F_r=1+A_r(chi_{123}-1)

on r controls and three fresh data coordinates. Every physical influence is delta: data flips change the parity only on activation, and control flips cross the activation point and change the output on half of data inputs. Hence I=(r+3)delta.

The constant coefficient is 1-delta. Other nonzero coefficients have absolute value delta, exactly on nonempty control subsets and on all control subsets united with all three data coordinates. Therefore nonconstant mass W=2delta-delta^2 and

    H=eta((1-delta)^2)+2rW<4I, eta(u)=-u log2 u.   (3)

Indeed eta(u)<= (1-u)/ln2, giving H<=delta(4r+2/ln2)<4(r+3)delta, since ln2>1/2. In particular B<=H<4I; this is no FEI counterfamily.

For a data coordinate h_i=A_r times the parity of the other two data bits. All of its Fourier energy delta is at residual row degrees >=2. Extending A096's degree-one suppression to the whole higher-degree row would assert

    delta<=2delta^2 ln(2/delta).

This fails for every r>=4: the right side is less than 2delta^2(r+1), and 2delta(r+1)<1, starting at 10/16 and decreasing. This is the first invalid inference when linear-form concentration is silently applied to an arbitrary-degree row. Ternary derivative support alone does not produce quadratic suppression of its complete row energy.

## 3. A fully normalized product-influence reference still overcharges

On nonempty subsets consider the natural all-degree extension

    Q_prod(S)=prod_{i in S}epsilon_i/Z,
    Z=prod_i(1+epsilon_i)-1.

It has total mass exactly one. On F_r, Q_prod(S)=delta^|S|/Z and Z=(1+delta)^(r+3)-1>=delta. Its nonempty cross-entropy bill is exactly

    X=sum_{S nonempty}p_S log2(1/Q_prod(S))
      =rI+W log2 Z,
    X/I>=r-2r/(r+3)->infinity.                    (4)

Thus restoring the normalizer does not make this extension influence-paid. For the normalized actual nonempty law p_S/W, Gibbs gives H_nonempty<=X-W log2 W; adding the vacuum entropy still leaves an unpaid divergent reference bill. The complete probability reference with vacuum weight 1/2 and nonempty weights Q_prod/2 has CE=1+X, so adding a vacuum sector does not repair it. A retained KL refund could cancel the excess, but that refund requires proof. Equation (4) refutes this specific reference, not every reference.

## 4. All-degree upper-atom entropy and row-entropy majorants fail

For even n>=2 let b_n=(-1)^(sum_j x_(2j)x_(2j+1)), using physical bits 0,1. Each two-bit block has Fourier coefficients of magnitude 1/2; tensorization proves every full squared coefficient is 2^-n. Consequently

    I=n/2, B=n, H=n,
    sum_S |S|p_S log2(1/p_S)=nI,
    sum_i epsilon_i H(mu_i)=(n-1)I.              (5)

Moreover R_ge2=n-n^2*2^(1-n). Replacing every edge by its upper-atom entropy, as in a layerwise application of phi(x,y)<=y log2(1/y)+y/ln2, leads to the weighted entropy in (5), not H. Neither that term nor the summed complete-row entropies is O(I), even on actual Boolean functions with B/I=2. Fixed-layer conversion is valid, but this all-degree surrogate has destroyed the equal-mass pair cancellation. This diagnostic is distinct from the known fixed-Renyi obstruction.

## 5. Influence-vector-only complete spectral references are impossible

Consider any rule Q_n(epsilon_1,...,epsilon_n) returning a subprobability on all subsets. It may use physical labels and need not be permutation-equivariant. It may also know any permutation-invariant metadata. It may not depend on which Boolean function realizes those same inputs. There is no absolute K making CE(p_f,Q_n(epsilon(f)))<=K I(f) for every actual Boolean sign.

For every integer w>=2, take k=2^w disjoint width-w point conjunctions A_j, n=kw, delta=1/k, and

    f_w=1-2 prod_{j=1}^k(1-A_j).

Every influence equals epsilon=2delta(1-delta)^(k-1), and I=2w(1-delta)^(k-1)<=2w. These equal labeled vectors remain exactly the same under every permutation of the n coordinates. Thus the reference Q is the same for the entire permutation orbit, even for a label-dependent rule.

Average the actual spectral laws over that finite orbit, obtaining bar p. It is uniform conditional on spectral degree m. If Q vanishes on its support, some orbit member has infinite CE. Otherwise linearity and subprobability Gibbs imply

    average_pi CE(p_(f_w o pi),Q)=CE(bar p,Q)
      >=H(bar p)=H(|S|)+E log2 binom(n,|S|).       (6)

This reconstructs A015's exchangeable-location optimum: an exchangeable reference has q_m/binom(n,m), and its infimum is attained at q_m=Pr(|S|=m). Here the orbit/Gibbs argument additionally covers arbitrary nonexchangeable Q that must remain the same for all equal-influence realizations.

The one-block function 1-A_j has constant coefficient 1-delta and every nonempty coefficient of magnitude delta. Therefore the total squared spectral mass of f_w on sets touching exactly one block and having m elements is

    4k delta^2(1-delta)^(2(k-1)) binom(w,m).       (7)

Let a=(1-1/k)^(2(k-1)). Integrating 1/(1-t)<=1/(1-1/k) on [0,1/k] gives ln(1-1/k)>=-1/(k-1), hence a>=e^-2>1/9. The elementary exponential series gives e<3. At least 2^(w-1) subsets of a block have m>=ceil(w/2), so (7) gives at least 2/9 spectral mass with m in [ceil(w/2),w]. On these degrees

    binom(n,m)=prod_{j=0}^{m-1}(n-j)/(m-j)
      >=(n/m)^m>=k^m,
    log2 binom(n,m)>=wm>=w^2/2.

Consequently H(bar p)>=w^2/9. Some coordinate permutation pi therefore satisfies

    CE(p_(f_w o pi),Q)/I(f_w)>=w/18.             (8)

This proves the all-parameter no-go, with no asymptotic extrapolation from a census and no hypothesis of exchangeability imposed on Q itself. It strengthens A015's obstruction by allowing influence-aware rules: all influences here are equal, so their vector provides no block-location information. It is a coding-cost obstruction, not a lower bound on the original H(f_w) and not a disproof of FEI. It does not exclude function-adapted references, signed-coefficient information, adaptive histories, references with a paid KL correction, or references directly coding conditional edges instead of the entire spectrum.

## 6. Honest first unsupported universal line

The complete row normalizer and joint influence budget are known, but the needed all-degree retained-KL payment in (2), equivalently R_ge2<=K I after paid layers, is unproved. Sparse support alone, a product-influence prior, atom entropy majorization and any complete spectral prior depending only on the influence vector are now ruled out as sufficient payments. The next construction must retain function-specific spectral/support information and cancellation between the two endpoint masses. Nothing here proves that such a construction cannot exist.

# executed validation with domain, arithmetic, commands and outputs

Both specs were saved before their respective jobs. Run commands from A001:

    python -X utf8 runs\20261013T213937Z-fleet05-A001-quantifier-audit\code\check_reference.py
    python -X utf8 runs\20261013T213937Z-fleet05-A001-quantifier-audit\code\check_orbit.py

The first checks eight actual Boolean tables: activated parity3 at r=4,6,8,10 and quadratic bent signs at n=2,4,6,8. Integer Walsh transforms are independently matched to physical flip counts and signed ternary derivative transforms, every coordinate and coefficient. Exact spectrum multiplicities, normalizers, row tails, rational CE lower bounds and interval H/I,B/I bounds all pass: 79,672 assertions, 2.321 seconds, out/CHECK.json.

The orbit job checks w=2,3,4,6,8,10,12 (seven declared symbolic cases) via exact one-block Walsh transforms and factorized actual Boolean spectra, rational one-block high-degree masses and integer binomial comparisons. The w=2 case also checks the complete n=8 physical truth table, every coefficient and influence. It passes 378 assertions in 0.066 seconds, out/ORBIT_CHECK.json. No permutation orbit or large truth table was enumerated. The analytic proof establishes all w>=2. An initial signed-mean check failed because the helper constructed the global negative of the declared sign; it was corrected, and the failure/repair is preserved in out/ORBIT_PILOT_FAILURE.json. No squared-spectrum assertion was used to conceal that discrepancy.

Total: 80,050 exact assertions, zero failures in final jobs. Logarithms use 24 positive atanh terms after range reduction to [1,2), geometric remainder 2z^49/[49(1-z^2)], all four signed division endpoints for ln2, and outward floor/ceiling rounding to denominator 2^70. Floating time measurements are diagnostic only. Both jobs estimated 30 MB and ran below 60 seconds; no job exceeded the 300 MB memok trigger. No dimension escalation, heavy search, GPU or background process occurred.

# proof dependencies and changed downstream conclusions

The new scoped mechanism diagnostic is self-contained. A096-UNIVERSAL-LEVEL12-ERASURE@1 is consumed as independently accepted by A098; it is not re-proved or used to extrapolate all-degree suppression. Known C018/KL and elementary Fourier identities supply the interface but are not claimed as new. A015-CONDITIONED-MINTERM-LOCATION-BARRIER@1 receives an independent local acceptance only of its exchangeable-reference optimum identity in section 4. Its conditioning, ordered repair and regular-core transfer remain outside this review. No substantive repair was supplied to that identity. A015's author hash covers the statement alone; the copied review record preserves it while the local claim hash covers statement plus hypotheses. out/SOURCE_HASH_SCHEME.json records both verified conventions; neither statement nor hypotheses changed.

Downstream A045/A073/A096 should reject an influence-vector-only complete spectral prior as a universal cost proof even if its normalizer is exact. They may still use such a prior with a proved function-specific KL refund. A099/B20 can record three distinct failure lines: linear concentration extended to arbitrary degree; fresh I reused across layers or upper-atom surrogate; influence-only global reference. The finite non-Boolean control from A096 remains useful but is no longer the only guard: all witnesses here are actual Boolean signs.

The B01 pending-claim queue is already over its broad-candidate cap in A098's intake. This run therefore adds a scoped mechanism obstruction and independent source-slice review, not a new proposed universal sufficient theorem. Shared ledgers, other-agent files and schedules are unchanged; adoption is pending.

# one next mathematical action and independent reviewer

Next: test a function-adapted conditional-edge reference against the signed Boolean convolution identities, keeping the exact joint normalizer in (2) and one cross-degree influence budget; require the proposed refund to survive the activated parity row tail and permuted equal-influence tribes, with bent equal-mass pairs charging only 2I. A096 owns the universal row construction, A045 its Boolean admissibility, A073 its exact normalizer; A001 audits the first proposed all-degree refund. A086 is the allocated independent reviewer, A094 alternate. A015 can consume the strengthened influence-only obstruction and scoped review. This is a source-bound handoff, not a sent message or an assertion that recipients have acted.

# actual persistence receipts or precise save blocker

The assigned immutable run contains REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, immediate DERIVATION.md, two frozen specs, independent scripts and exact outputs. STATUS.md has two lines; WORKLOG.md is appended and LEARNED.md updated. out/PERSISTENCE_RECEIPT.json records sizes, SHA256 and protocol-schema checks. Every artifact is below 20 MB. No shared-tree/other-agent write, git, brain write, mail, mirror verification, independent acceptance of the new diagnostic or downstream adoption is claimed. There is no local save blocker.

**Universal bridge:** This stage moves C018 by resolving A098's all-degree quantifier/budget audit: the complete joint reference is normalized with exactly one I, and three tempting extensions are rigorously excluded, including every influence-vector-only complete spectral reference with a w/18 divergent cost ratio on permuted Boolean tribes. It pays no new universal erasure layer; the reviewed frontier remains B_root+T12 with R_ge2<=K I unproved. NEXT asks for a function-specific conditional-edge refund constrained by these exact guards, because influence-only normalizers and fresh per-layer budgets cannot reach full FEI; retaining signed/support information and pair cancellation attacks the precise missing universal bridge instead of adding an isolated class bound.
