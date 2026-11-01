# A015 stage 2: after minterm erasure, physical set locations remain

## exact target, quantifiers, hypotheses and units

Advance the previously completed minterm barrier packet by consuming A012's exact posterior activation repair and quantifying the cost left after conditioned minterm erasure. All functions are genuine Boolean signs on finite uniform cubes. Entropies and all displayed logarithms are in bits; natural logarithms appear only in the imported rank mean. References are fixed, complete output subprobabilities, with ideal cross entropy `CE(P,Q)=sum P log2(1/Q)`. Failure mass is retained. Single-sample integer prefix rounding is not included in ideal CE.

Two source-bound deliverables are complete: an independent acceptance of `A012-CONTROL-FIRST-POSTERIOR-REPAIR@1`, and a scoped compression obstruction/repair for full-minterm output references. **Full FEI remains OPEN.** The new obstruction is for exchangeable (permutation-invariant) references, not arbitrary complete codes. Its test family has every coordinate relevant. This stage introduces no new broad universal candidate while the stream review queue is full.

## sources actually read, revisions and theorem locators

Read BOARD dated 2026-10-12 04:39 UTC, B03 STREAM_NOTES v2 (2026-10-11 23:2xZ), own rolling files, and execution protocol v2 in full. B02 STREAM_NOTES v2 and its single-gate/tribes obstruction were consumed as a duplication guard. A012's stage-2 DERIVATION.md Sections 1--5 and full CLAIMS.json are the original source under independent review. A013 stage-2 GENERAL_RESET.md and DERIVATION.md were read: this stage does not redo averaged rank-reset or bent reserve calculations.

A006 stage-2 REPORT.md and CLAIMS.json were read, especially its actual majority posterior construction and stated all-n cost bound. Its majority theorem is a pending source-complete dependency, not independently accepted here. The raw fixed-scale majority label obstruction proved in A015 stage 1 does not contradict that improved posterior bound. No majority PI-J enumeration is repeated.

Read `source_material/reductions/paper/forests.tex` in the report tree: root odds, conditioning, actual partition-forest probabilities, and thm:posteriorforest. It retains `v(Lambda+log Z)`, and it explicitly distinguishes a single chosen witness from summed actual runs. Read the supplemental current threshold source at `lem:ranktail`, `eq:normalizer`, `eq:rankcost`, and the single-regular-function rank mean: `E sum F_j <=(1+ln2)I`. Source paths/hashes and inspection scope are recorded in `out/SOURCES.json`. The four paper contexts and older campaign registries were already read/inspected in stage 1; no unrelated percolation result is invoked anew.

## complete derivation or exact first unsupported line

### 1. Independently accepted activation repair; complete core debt survives

`A012_REVIEW.md` gives a reconstruction of the entire A012 v1 claim without importing its code or repairing its proof. For balanced core g and a fixed nonempty spectral reference R_g of mass z<=1 and cost c_g, use

`Q_F(empty,empty)=(1-p)^2`,

`Q_F(U,empty)=p^2` for U nonempty,

`Q_F(U,T)=p^2 R_g(T)` for T nonempty and every U,

where p=2^-r and F=1+A_r(g-1) on fresh controls. Exact summation gives reference mass `1-p+pz` and

`CE(P_F,Q_F)=p c_g+A_r`,

`A_r=2rp(2-p)+(1-p)^2 log2(1/(1-p)^2)`,

`D(P_F||Q_F)=p D(P_g||R_g)`.

The true control-first witness satisfies the original posterior formula in A012. Its physical stopping label J has H(J)=2(1-p), and W is deterministically equivalent to (J,S). The posterior is independent of the balanced core and tends to two bits. Original scope, sharp selector coefficient, and disjoint-reference iteration all hold. The coefficient is uniquely maximized at r=3:

`C_act=15/4+(49/12)log2(8/7)`, with `4.536<C_act<4.537`.

The first unsupported universal line remains `c_g<=K I(g)` for one finite K for all balanced cores, or a genuinely new paid shared-control/colliding-child transfer. The activation theorem preserves arbitrary seed cost; it does not construct that missing core reference.

### 2. Exact full-minterm root cancellation, including conditioning

Let f be any nonconstant Boolean function on n>=1 declared physical coordinates. Its positive full-cell DNF has N>=1 distinct terms, all support [n], all density `pi=2^-n`. Choose the fixed admissible gate weights lambda_l=1/N, and the same rank order in every term. Its independent-root normalization is

`Lambda=N log2(1+pi/N)`, `Z=1-2^-Lambda`, `D=2^Lambda Z=(1+pi/N)^N-1`.

Condition on a nonempty initial root set. The probability of **exactly one** root in that conditioned experiment is

`eta=pi/D`.

Indeed each selected one-root set has unconditional probability `2^-Lambda pi/N`; summing the N distinct actual runs and dividing by Z gives pi/D. The non-root subset laws are identical for these full supports and common orders, regardless of the literal signs. Their probabilities may therefore be summed before taking a logarithm.

This is a stronger refund than stage 1's unconditioned root sum. In that sum the minterm name disappears but pi remains. Conditioning contributes `Lambda+log Z=log D`, canceling that root rarity as well, up to the exact factor eta. Binomial expansion gives `D>=pi`; also `D<=(exp(pi)-1)<=pi exp(pi)`, so

`exp(-pi)<=eta<=1`, `0<=-log2 eta<=pi log2 e`.

For the finite rational checks, the cruder elementary bound `D<=pi/(1-pi)` gives `eta>=1-pi`. The case N=1 gives eta=1 exactly. No sample-dependent scale is selected. No rank, subset or termination cost has been canceled by this root computation.

### 3. Explicit output references and the role of the order prior

To keep every finite reference probability rational, use rank exponent **two**, rather than the original forest exponent 6/5. This is an explicitly modified valid output reference, not a claim about the original PI-J infimum. For each size s, give coordinate j weight `theta_s(j)=min(1,(s/rank(j))^2)` and normalize s-subsets by their elementary symmetric polynomial `Z_s`. Choose s with probability `1/[s(s+1)]`; an invalid size fails. Require no children, an event of probability one half. Keep only the conditioned one-root/no-child finite runs; all other mass is discarded as failure. Their complete output reference is

`R_ord(A)=eta prod_{j in A} theta_s(j)/[2s(s+1)Z_s]`, `s=|A|>=1`.

Its mass is exactly `eta n/[2(n+1)]`. Thus even the surviving finite-run failure cost is present. Adding vacuum probability 1-v and multiplying nonempty output mass by v is a complete subprobability with explicit empty-sector CE; v=Var(f). The examples below are balanced, so v=1.

Alternatively choose the common order uniformly from all n! permutations **before sampling**. This is a fixed normalized order prior; its output probabilities average the complete references, and no order-selection cost is omitted from that average. For each size s the averaged local subset law is uniform, by permutation equivariance and normalization. Hence exactly

`R_sym(A)=eta/[2s(s+1)binom(n,s)]`,

`CE(P,R_sym)=-log2 eta+1+E log2[|S|(|S|+1)]+E log2 binom(n,|S|)`

for a balanced spectrum. This shows explicitly how root names and latent orders are erased, while the physical output subset still has to be named. The same symmetrization identity holds for any exponent alpha>1, including the original 6/5; exponent two is used for rational construction and the ordered-cost certificate below.

### 4. All exchangeable references: exact optimization and a stronger barrier

Let Q be any subprobability on subsets, invariant under all coordinate permutations. Write W_s=P(|S|=s), and let q_s be its total mass at size s. Then `Q(A)=q_s/binom(n,s)`. If it vanishes on actual support its CE is infinite. Otherwise

`CE(P,Q)=sum_s W_s log2(1/q_s)+sum_s W_s log2 binom(n,s)`.

Minimizing over all such subprobabilities gives the exact optimum at q_s=W_s:

`inf_exchangeable CE=H(W)+E log2 binom(n,|S|)`.

Proof: q_s sum to at most one, so subprobability Gibbs gives the first term >=H(W), with equality for q=W. The excess over actual entropy is precisely

`J_ex=sum_s W_s D(P(. | |S|=s) || Uniform_s)`

`=H(W)+E log2 binom(n,|S|)-H(P)`.

This is a location/conditional-shape cost, not the entropy of a gate name. It is nonnegative. The infimum already optimizes every possible size law, including empty mass. Optimizing a root scale, a size prior, or any posterior whose final output reference remains exchangeable cannot avoid it.

Take r>=1 fresh control bits, p=2^-r, and two data bits y,z. Define the genuine balanced rare-switch function

`M_r=y+A_r(z-y)`, on `n=r+2` coordinates.

Its Fourier coefficients are `1-p` on {y}, `-p epsilon_U` on {y}+U for U nonempty, and `p epsilon_U` on {z}+U for every U. Therefore all non-leading supported sets have mass p^2, and

`I(M_r)=1+rp`,

`Inf_y=1-p`, `Inf_z=p`, `Inf_control=p` for every control,

`H(M_r)=(1-p)^2 log2(1/(1-p)^2)+2r(2p-p^2) ->0`.

Every coordinate is relevant; there are no dummy variables in this obstruction. Singleton mass is

`W_1=(1-p)^2+p^2 ->1`.

Thus every exchangeable subprobability satisfies

`CE(P_Mr,Q)/I(M_r) >= W_1 log2(r+2)/(1+rp) ->infinity`.

More precisely the best exchangeable cost is `log2(r+2)+o(1)`. The tail degree mass is <=2p, its binomial cost is <=2pn, and `H(W)<=h2(2p)+2p log2 n` for r>=2; all tend to zero. The dominant singleton term differs from log2 n by o(1). Consequently `J_ex=log2(r+2)+o(1)`, although H/I->0. This refutes influence payment for the entire exchangeable-reference class, not FEI or a function-adapted reference.

### 5. A location-aware common order repairs the same family

For the rare switch use the fixed order y first, followed by z and all controls. This is decreasing influence; y has influence 1-p and every other coordinate has p. With exponent-two weights, elementary symmetric normalization obeys

`sum_j theta_s(j)<=2s`, `Z_s<=(2e)^s`.

For j in A, its occupied predecessor count is at most s-1, so

`-log2 theta_s(j)<=2 log2[rank(j)/(|A intersect predecessors_j|+1)]`.

Writing G_bits(A) for the sum of these logarithmic rank discrepancies, the complete ordered cost obeys

`CE(P,R_ord)<=-log2 eta+1+log2(6e) I+2 E G_bits`.

Discarding the nonnegative predecessor subtraction gives

`E G_bits<=sum_j Inf_j log2 rank(j)=p log2(n!)`.

The sequence `2^-r log2((r+2)!)` is nonincreasing for r>=1, because `(r+2)!>=r+3`. Thus `2p log2(n!)<=log2 6`. Since pi=2^-n<=1/8 and I>=1,

`CE(P_Mr,R_ord) <= [log2(6e)+log2 6+1+(1/8)log2 e] I(M_r)`

`< (639/80) I(M_r) <8 I(M_r)`.

The last strict certificate uses only e<3, ln2>2/3, `18^5<2^21` and `6^5<2^13`: the bracket is less than `21/5+13/5+1+3/16=639/80`. The pilot independently constructs the complete rational reference and verifies the cost bounds. This is a repair of the same output-location obstruction; it is not presented as a new class-FEI theorem. Actual H/I already tends to zero.

This order is not a universal remedy. B02's existing single-gate tribes obstruction shows a dimension-sized rank cost in every single-gate table of the specified model, even with its best orders. This stage consumes that obstruction rather than reproducing it. Majority needs symmetry or a paid regular rank law, rare switches need physical location awareness, and tribes needs block support information. Root cancellation alone supplies none of these choices universally.

### 6. Concrete grouped-majority transfer with failure mass and full core CE

Use a single regular majority gate with fixed physical desirability order. Define its nonempty core reference R_g by the exponent-two subset sampler above, with one mandatory root (so eta=1), and the no-child factor one half. Its mass is `z=n/[2(n+1)]`; it is **not** assumed to be a probability law or an exact spectral oracle.

The source-complete regular rank mean gives `E G_bits<=(1+log2 e)I(g)`. Therefore for a balanced regular core,

`c_g<=1+[log2(6e)+2(1+log2 e)] I(g)`

`<=[3+log2 6+3log2 e] I(g) = K_ord I(g)`.

The last step uses I(g)>=1 by Poincare for balanced Boolean g. This is an explicit complete core reference cost, not an inference from H<=C I to a free code. Its constant satisfies `K_ord<101/10`. Feed this R_g into the independently accepted A012 construction. The full new reference has mass `1-p+pz`, and

`CE_F=p c_g+A_r <=max(K_ord,C_act) p(I(g)+r)`.

Keeping the exact K_ord is valid; since K_ord> C_act, it yields CE_F<=K_ord I(F). Thus the promised stage-1 transfer to grouped activated majority is now concrete and source-bound. It does not use A006's pending PI-J majority theorem or establish anything about that separate infimum. The source rank law and the imported activation transfer are exactly the mathematical hypotheses paying the costs.

The check constructs core and activation output references for n=1,3,5,7,9 and r=1,2,3,4. It verifies actual parent Walsh spectra, failure masses, interval CE bounds, and the exact generalized-divergence identity by aggregating equal rational density ratios. The full core bill is multiplied by p, rather than discarded.

### 7. Exact remaining gap and nonduplication

The original raw-label majority barrier remains correct as a component of the fixed-scale unrefunded Theorem R estimate. It cannot be promoted to a no-go for the conditioned posterior infimum: A006 already provides a majority repair, and the full-minterm sum here cancels labels/root rarity explicitly. B03 v2's 'false for DNF of majority (labels)' should be read at that coarse-component scope.

The stronger universal temptation is now also ruled out: after summing all interchangeable minterm names, making the output law permutation-invariant does not produce a universal influence-paid representation. Its unpaid exact term is J_ex. Ordering by influence repairs the rare-switch example but is not a universal gate-cover or rank theorem. First unsupported line: for every Boolean f there is a fixed function-adapted support/order/reference mixture with complete posterior cost O(I), retaining terminal entropy and all normalization/model-selection charges. Neither exact activation transfer nor the current single-order/symmetric references prove that line.

## executed validation with domain, arithmetic, commands and outputs

Both specs were frozen before their corresponding jobs: out/FROZEN_SPEC.json and out/TRANSFER_SPEC.json. All jobs estimated 60 MB and ran below the 60-second pilot cap; no >300 MB or heavy job was started, so no memok threshold was triggered. No upstream executable/code import, automatic dimension increase, GPU, background process or external write occurred.

Commands from A015:

`python -X utf8 runs\20261012T044229Z-fleet05-A015-minterm-barrier-analysis\code\check.py`

`python -X utf8 runs\20261012T044229Z-fleet05-A015-minterm-barrier-analysis\code\transfer.py`

Final successful outputs: out/EXACT_RESULTS.json, **20,956 exact assertions PASS**, 312 balanced-core activation cases, seven full rare-switch truth tables, and 64 declared symbolic switch parameters; observed computation time 0.7232003 seconds. out/TRANSFER_RESULTS.json, **95 exact assertions PASS**, five explicit majority core references and twenty actual activated references, maximum dimension 13; observed computation time 0.2911084 seconds. Total: **21,051 exact assertions**.

The first pilot failed only while serializing huge exact rational interval endpoints, after no mathematical assertion failure. out/PILOT_FAILURE.json preserves it. The repair rounds log bounds outward to the rational 2^-64 grid (transfer helper uses 2^-48), which is proved to retain enclosure by integer floor/ceiling. Positive atanh series bounds include a geometric remainder; signed interval division handles negative numerators correctly. Rational root estimates avoid unnecessary high-bit logarithm evaluation. Exact formal-log entropy comparisons use prime factorization of small rational joint masses; they are identities, not floating sign evidence. Decimal diagnostics are not certificates.

## proof dependencies and changed downstream conclusions

Independent review: A012-CONTROL-FIRST-POSTERIOR-REPAIR@1 is accepted at its original exact scope with no contributor repair. This is a source-bound local review record, not supervisor/shared-registry adoption. New full-minterm cancellation and exchangeable-location formulas are elementary proofs in this report; their ordered sampler uses a declared exponent-two modification. Concrete grouped-majority cost uses the threshold source regular rank mean plus the independently reconstructed A012 transfer. A006 majority posterior and B02 single-gate tribes are consumed to avoid duplicate work; A006's pending bound is not a proof premise here.

Downstream: A011/A012 must distinguish latent gate/physical stopping labels from physical coordinate locations in their output transfer. A013's coarse reset can retain its original unconditioned root metadata; a change to conditioned one-root summation must record the exact eta and failure probability instead of pretending the normalization is unchanged. B03/A006 can use the exchangeability obstruction to reject cardinality-only posterior replacements. No refutation propagates to the original A012 or A015 stage-1 claims; their different scopes are preserved.

## one next mathematical action and independent reviewer

Next: consume A006's actual-forest/determinant construction and test whether its output quotient preserves the dominant physical-coordinate information on the same rare-switch family and its nonconstant-child generalization, while retaining conditional core CE. The question is whether a function-adapted prime-support/order posterior pays the exact J_ex lost by exchangeable averaging. Do not repeat majority, tribes, point activation, or the projective-plane baseline. Independent reviewers: A086 primary for full reference/debt projection, A094 adversarial for the order prior, root conditioning and output-location no-go. A012 can consume the accepted activation review and exact ratio transfer.

## actual persistence receipts or precise save blocker

All results were saved inside the assigned A015 stage directory: four protocol files, A012_REVIEW.md, this report, NOTES.md, both frozen specs, independent code and exact outputs. STATUS is two lines; WORKLOG is appended and LEARNED updated. out/RECEIPTS.json gives reread sizes and hashes, with exact claim/progress schema checks and byte equality of PROGRESS/PACKET_DELTA. No independent acceptance of the new A015 theorem, supervisor adoption, GitHub mirror verification, public release or downstream execution is claimed. There is no local save blocker.

## Universal bridge

This stage moves **C020 whole-set witness cost** by independently accepting the exact A012 posterior-erased activation repair, completing its transfer to an explicit grouped-majority reference with the core failure/CE bill retained, and replacing the coarse raw minterm barrier by a sharper statement: conditioned multiplicity can cancel minterm labels and root rarity, but every exchangeable complete output reference still has unbounded cost/influence on an all-relevant Boolean rare-switch family. Its exact unpaid term is the degree-conditioned location divergence J_ex, repaired on that same family by an explicit ordered reference with CE<(639/80)I. Full FEI still needs a function-adapted support/order/posterior selection paying that cost and all remaining core debt universally. NEXT is the shortest local route because it tests the actual-forest construction against the information destroyed by the failed quotient, preserving terminal/core CE, rather than proving another already solved class bound.
