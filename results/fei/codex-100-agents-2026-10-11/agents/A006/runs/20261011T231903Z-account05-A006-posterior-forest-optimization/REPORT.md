# A006 stage 2: dictionary review and majority prime-implicant forests

## exact target, quantifiers, hypotheses and units

Following the B02 lead, this stage independently reconstructs A008 v1, then addresses PI-J on every odd-dimensional majority function. Units are bits for H, posterior entropy and B; natural logarithms for rank F; I=E|A| on the uniform cube. Full FEI and the all-Boolean PI-J target remain open.

For every odd n>=1, let k=(n+1)/2 and f=Maj_n. Use **all prime positive implicants**, the conjunctions on the k-subsets R of [n]. Let N=binom(n,k), d=binom(n-1,k-1), lambda_R=1/d, pi_R=2^-k, and one ordered cover per gate, the restriction of the same physical order 1,...,n. These globally fixed weights satisfy every incidence constraint with equality. No function/set-dependent scale selector is used. Let

    D=(1+2^-k/d)^N-1=2^Lambda Z,
    G(A)=sum_{j in A} ln[j/(|A intersect [j-1]|+1)].

I prove the all-dimensional upper bound for the **optimized actual partition-forest residual**:

    R_PI(Maj_n) <= [49/5+(6/5)log2(e)] I(Maj_n)
                < (58/5) I(Maj_n) <= (58/5)sqrt(n).

The proof retains posterior entropy and root conditioning in one fixed reference. It bounds the true infimum above by explicit realizable posterior laws; it does not identify that infimum from finite experiments. Exact all-partition sums for n=1,3 and rigorous constructed upper bounds for n=5,7 are saved separately.

Majority was already an FEI class. This stage proves a cost theorem for its specified prime-implicant reference, not a new FEI class or full FEI. A008's distinct dictionary reference is independently accepted at its original scope, without repair.

## sources actually read, revisions and theorem locators

Read the 2026-10-11 23:19 UTC BOARD.md, current A006 STATUS.md, and B02 STREAM_NOTES.md v1 dated 22:45 UTC. The lead redirects A006 from shared-core sunflower extensions to A008 review and odd-majority PI-J. The lead's stale pending-candidate count is superseded by source-level reviews: A094 AUDIT.md independently accepts A006 and A007; this run supplies an independent reconstruction of A008. No inference of shared registry adoption is made.

Read EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2, and the complete conditioned forest source, source_material/reductions/paper/forests.tex: eq:forestpacking, eq:forestconditioning, eq:forestcost and thm:posteriorforest. Its child-gate probability is lambda_child with remaining failure mass. The proof of its coding theorem requires a support/order table, not a physical OR relation; its later activation/path and fractional derivative estimates have extra hypotheses. The present majority table really is the positive prime-implicant DNF, so no extension of that source scope is needed.

A008's complete REPORT.md, WHOLE_SET_CODEC.tex and CLAIMS.json v1 were read; AUDIT_A008.md gives the independent proof. A094's AUDIT.md supplies the exact previous-stage review and the single-gate rank/actual-cost warning. A086's file inventory was inspected, without reusing its checker. Baseline current-threshold-paper.tex lem:pivotal-antichain, lem:antichain-density, lem:antichain-noise, lem:ranktail, and the derivative-law rank expectation in Section 4 were read as a complete dependency chain. Source hashes and inspection scopes are in out/SOURCES.json. A009/A014 statuses and B03 lead notes were consulted to choose a nonduplicating next action.

## complete derivation or exact first unsupported line

### 1. Independent A008 acceptance

AUDIT_A008.md reconstructs normalized finite dictionary sampling, its output pushforward, finite prefix decoding, canonical root/attachment recovery, all sunflower output masses, the <25I/4 and <33I/4 bounds, and the latent-name lower bound. No author code was imported and no repair was contributed. Verdict: HOLDS at the exact original statement. In particular output-code credit is not a reduction in bits needed to reveal the latent record, and it is not a bound on the original B residual.

### 2. Why the majority gates are exactly the primes

A positive subcube certificate for majority must force at least k positive coordinates: if fewer are fixed positive, set every remaining free coordinate negative and the function is false. Fixed negative coordinates cannot aid a minimal positive certificate. A conjunction fixing exactly k coordinates positive is sufficient, and removal of any one literal makes it insufficient. Thus the prime positive implicants are precisely all k-subsets. Every coordinate lies in d such gates, hence lambda=1/d is admissible. All supports are ordered by the same physical order; the sampler is globally fixed.

Since majority is balanced, v=1 and the binary empty/nonempty term is zero. Put r=N lambda pi=(n/k)2^-k. Because n/k<=2 and k>=1, r<=1. We first retain the exact root block Lambda+log Z=log D. Then

    D <= exp(r)-1 <= r exp(r),
    log D+k <= log(n/k)+r log(e) <3.

The last bound uses log(n/k)<=1 and log2(e)<2, which follows from ln2>1/2. Failed and infinite runs supply no output mass and are never inserted into posterior entropy.

### 3. Small Fourier sets: posterior over all containing clauses

Fix any nonempty A with s=|A|<=k. Every gate R containing A yields a distinct actual run: R is the sole root, it selects B_R=A, chooses zero children, and terminates. There are C_s=binom(n-s,k-s) such runs. Their root names differ, so their uniform posterior has entropy log C_s. These are not alternative descriptions of a single event.

For each such run, M=1, kappa=s and the congestion term is zero. If j is the t-th selected coordinate, all A predecessors of j lie in R, and its gate rank is at most its physical rank j. Hence F_R^j(A)<=ln(j/t). Therefore

    log D+E B-H(posterior)
       <= log D+k+log d-log C_s+(6/5)/ln2 * G(A).

The full label/root block, rather than an independent per-coordinate label, is present before bounding it. The containment ratio satisfies

    log[N/C_s]=log[binom(n,s)/binom(k,s)] <=2s.

To prove this for every s<=k, write the logarithm as sum_{j=0}^{s-1} log[(n-j)/(k-j)]. Its increments are nondecreasing, so the average of its first s increments is at most the average of all k. The total at k is log binom(n,k)<=n<=2k. Also d/N=k/n<=1. Thus log d-log C_s<=2s and

    small-set cost <=3+2s+(6/5)/ln2 * G(A)
                   <=5s+(6/5)/ln2 * G(A).

There is no paid model switch here: the posterior selects different runs of the same fixed generator.

### 4. Large Fourier sets: two actual gates suffice

For s>k, split the selected coordinates alternately in their physical order into U and V, with |U|=ceil(s/2), |V|=floor(s/2), and choose j=min U. Choose a gate R containing U and a gate T containing V union {j}, with a fixed global lexicographic tie rule. They exist because |U|<=k and |V|+1<=k for s<=n=2k-1. They must differ: otherwise one k-set would contain A, impossible when s>k.

Assign U to R and V to T; root R, child T attached at j. The ownership graph contains R->T. If it also contains T->R, both are in one source SCC; otherwise R is the unique source. In either case root R is permitted. Thus this is a genuine once-per-gate finite partition run with one root. Prescribed size, child-count, multiset and label probabilities are positive; selected subsets are disjoint and decode exactly A. A point mass on this run has posterior entropy zero, stated explicitly rather than implicitly dropped.

Every gate has congestion kappa/s_l<=s/floor(s/2)<=3, since this regime has s>=3. Its total congestion cost is <(12/5)s because log3<2. The gate-name cost is 2 log d<=2(n-1)<4s. At the t-th selected coordinate, the assigned block has at least (t-1)/2 previous coordinates in the integer sense: previous block members plus one equal ceil(t/2), which is >=t/2. Full A predecessors within the gate may only increase this denominator. Its gate rank is <=j, so

    F_owner^j(A) <=ln(j/t)+ln2.

The rank increment costs at most (6/5)s. Root rarity and global root normalization together cost <3, as in Section 2. Thus

    large-set cost <=3+(38/5)s+(6/5)/ln2 * G(A)
                   <=(43/5)s+(6/5)/ln2 * G(A),

using 3<=s. The small-set bound is also <=this expression. All gate-label, congestion, rarity and rank charges remain in this derivation.

### 5. Spectral expectation and all-dimensional bridge

The construction proves the following pointwise-to-expectation statement for the fixed complete middle-layer table, even for an arbitrary spectral law supported on nonempty sets:

    constructed residual <=(43/5) E|A|+(6/5)/ln2 * E G(A)

when that law has v=1. With v<1 the same statement holds with the unconditioned nonempty expectation, since the bound is pointwise. This statement is about the coding table and does not assume that the input Boolean function is its OR; majority supplies exactly that OR and its prime interpretation.

For majority, every earlier coordinate is as desirable as every later coordinate. The j-pivotal derivative is the indicator of the middle Hamming slice on n-1 coordinates; its supports on predecessor fibers are antichains. The baseline signed relative-noise/rank proof therefore gives

    E_{nu_j} ln[j/(|T intersect [j-1]|+1)] <=1+ln2.

The exact derivative Fourier identity is P_f(T union {j})=I_j nu_j(T). Multiply by I_j and sum j to obtain

    E_{P_f} G(A) <=(1+ln2) I(f).

No estimate from the fractional-overlap theorem or unknown FEI conclusion is used here. Substitution gives the displayed residual constant 49/5+(6/5)log2(e). The elementary atanh series gives ln2=2 sum_{l>=0}(1/3)^(2l+1)/(2l+1)>2/3, so this constant is strictly less than 58/5.

Finally I(Maj_n)=n*2^{-(n-1)}*binom(n-1,(n-1)/2). The exact antichain-density recurrence bounds the factor by 1/sqrt(n), hence I<=sqrt(n). The claimed O(sqrt n) bound follows for all odd n, with no extrapolation from finite cases.

The constructed law is merely an upper certificate for the optimized residual over every actual partition forest. No claim that the large-set deterministic witness, or the small-set uniform posterior, is optimal is made. No prior term is missing: every witness used belongs to one fixed complete reference, and no sampled-output choice of a reference table or scale occurs.

### 6. Exact finite optimization and logarithmic certificates

For n=1,3 the checker exhausts all assignments to containing gates, computes source SCCs, chooses each permitted root set, checks parent reachability, enumerates attachments and child-label orders, and deduplicates by actual chronological queue trace. In an assigned forest let

    z=product_l (s_l/kappa_l)^(s_l)
         *product_{j in A}[(|A intersect U_j^owner|+1)/rank_owner(j)],
    c=lambda^(number used)*pi^(number roots).

Then 2^-B=c*z^(6/5), exactly. The full sum of these weights is stored as a finite algebraic expression; its optimum is -log of that sum. Exact trace identity, not abstract witness multiplicity, determines the count. Fifth roots are enclosed by integer comparisons on a 48-bit dyadic grid. Logarithms use the 18-term atanh expansion after dyadic range reduction, with remainder

    2*z^37/[37(1-z^2)]

for z=(y-1)/(y+1), 1<=y<=2. Interval division uses all endpoint quotients, including negative numerators. Summing signed bounds gives rigorous intervals for the residual. The files distinguish full optimization at n=1,3 from constructive upper bounds at n=5,7.

The exact n=1 residual is zero by root cancellation. At n=3 the rigorous full optimum interval is [1.302334214,1.302334215]. At n=5,7 the constructed residuals lie in [2.888679153,2.888679154] and [4.252815747,4.252815748], respectively. These latter intervals enclose costs of the selected construction, not the full infimum. The finite checker optimizes within each small-set one-root cohort by weights proportional to 2^-B; this can only improve on the uniform posterior used in the analytic proof. For large sets it uses the one prescribed two-gate run.

There is no first unsupported line in the stated all-odd-majority cost bound; it awaits independent review. The first unsupported universal line is an absolute expected bound on the analogous rank-weighted prime-cover/forest mass for **every** Boolean function. The global G(A) bound used here is a regular-function input and is false in general: A094's XOR-of-conjunction stress gives diverging single-order rank/I. It must not be promoted to a universal premise.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before execution. One bounded pilot ran with an estimated 70 MB allocation, below the 300 MB memok threshold; no larger job was started. It completed in 38.930 seconds, with 11,574 console assertions passing (saved summary has 11,573 before the last runtime check), below the 60-second pilot cap. No GPU, background process, heavy concurrent job or automatic dimension increase was used.

Command from A006: `python -X utf8 runs/20261011T231903Z-account05-A006-posterior-forest-optimization/code/check.py`.

Saved outputs: A008_REVIEW_CHECK.json (5,454 independent dictionary traces, exact mass 1 and all fibers for m=1,...,6); MAJORITY_EXACT.json (all partition weights for every nonempty set at n=1,3, plus fixed-construction bounds for every nonempty set at n=5,7); SYMMETRIC_SPECTRA.json (exact binomial character sums at every odd n through 31, checked normalization, influence, parity of spectral levels, and rational rank-mean enclosures); CHECK_SUMMARY.json. For n<=7, every Fourier coefficient was additionally checked against a direct truth-table character sum. Influence was checked against the exact physical pivotal probability. Finite rational checks verify I^2<=n; the all-n proof is the density recurrence above. No floating entropy or logarithmic sign is used to establish a result.

## proof dependencies and changed downstream conclusions

The new cost candidate depends on the source-complete conditioned posterior forest theorem and the baseline pivotal-antichain/rank-mean chain. It does not depend on A008's theorem; A008 was reviewed as a separate source-level action. That separation avoids turning an output-dictionary bound into a queue-residual bound. A006's first-stage theorem is already independently reconstructed by A086 and A094 at its stated scope; its run files remain unchanged.

Changed conclusion for B02/C020: the prime-implicant table for every odd majority passes PI-J with an absolute constant, despite exponentially many clauses and exponentially large read. Posterior containment multiplicity pays small sets' labels, while two actual gates suffice for large sets. No coordinatewise fractional pressure or latent-name surrogate is substituted. A008's dictionary candidate can be adopted as independently reviewed locally, subject to supervisor index reconciliation.

## one next mathematical action and independent reviewer

Next: derive a certified determinant lower bound for the **rank-weighted sum over actual forests for a fixed assignment in an arbitrary prime-support hypergraph**, with canonical child ordering and the correct source-SCC root constraints. This is a generic computable posterior bound, designed to replace B03 Theorem R's raw label count; consume A009's affine-plane obstruction and A014/B03's signed-L2 work as diagnostics/dependencies. B03 v2 says the complete projective-plane theorem is already proved locally: do not redo that class. The target is the unpaid counting mechanism beyond one-/two-gate coverage. Independent reviewers: A086 for the actual-run construction/full finite sums; A094 for the containing-clause count and all-n rank transfer. A007 can challenge this independent A008 reconstruction without changing A008's original version.

## actual persistence receipts or precise save blocker

The four protocol files, FROZEN_SPEC.json, AUDIT_A008.md, code/check.py and code/persist.py, and all exact outputs are saved in this stage's requested A006 run. out/SOURCES.json pins the inspected sources; out/RECEIPTS.json binds saved file sizes and hashes. STATUS.md, WORKLOG.md and LEARNED.md are current. Only A006 files were written; no Git, shared-index edit, Brain write or external messaging occurred. Supervisor adoption/upload and independent acceptance of the majority cost candidate are not claimed.

## Universal bridge

This stage moves C020 whole-set witness cost / PI-J by independently resolving A008's output-quotient claim at its exact scope and proving that all odd majorities' complete prime-implicant tables have optimized posterior residual <(58/5)I, with exact all-partition certificates at n=1,3. The mathematical mechanism is explicit: posterior containment multiplicity pays exponentially many clause names for small sets, and two realizable clause runs pay large sets without a dimension loss; the remaining rank expectation is charged by a proved regular-function input. Unrestricted PI-J still needs a rank-weighted multi-gate posterior mass payment for arbitrary Boolean prime-support hypergraphs, and the single-global-order substitute is already refuted. NEXT targets a generic determinant certificate for that actual-forest mass, using the affine-plane obstruction and already completed projective-plane/signed-L2 results to identify the missing terms. This is shorter than another isolated class calculation because it works directly on arbitrary prime-support tables and would make the unpaid universal expectation a checkable quantitative inequality; the expectation bound itself remains open.
