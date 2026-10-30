# exact target, quantifiers, hypotheses and units

A046/B10 current-candidate intake is complete locally, pending independent review. Full uniform-cube FEI remains OPEN.

Freeze B09-BIASED-BLOCK-UNCERTAINTY v1, an author-proved, independently unaccepted helper explicitly live in CURRENT_STATUS.md. For every finite n, actual Boolean sign f on {0,1}^n, independent interior biases p_i, and physical block A with complement B, let mu(S)=fhat_p(S)^2 in the orthonormal basis phi_i=(X_i-p_i)/sqrt(p_i(1-p_i)). Include the empty coefficient. Under S~mu define M_A=H(S_A|S_B). Draw physical Z with its actual product probabilities, then draw T from the normalized squared biased spectrum of the Boolean restriction f_Z. Define J_A=I(Z;T) and L_A=H(mu)-E_Z H(mu_Z).

The exact frozen potential is P_A=M_A+Delta_A, where Delta_A=sum_{i in A}[h2(p_i)+log2(max(p_i,1-p_i))]. The live assertion is 0<=J_A<=P_A, hence L_A<=2M_A+Delta_A. All entropies here are Shannon bits, not corrected biased FEI+ entropy. Zero masses contribute zero; deterministic input coordinates must be contracted before defining the basis. FROZEN_POTENTIAL.json contains the complete interface and source version.

The substantive endpoint target addressed here is a separate correction: prove necessity of a rare logarithm by an actual lower-bound family, rather than by the asymptotic of an available upper bound. We prove for g_p,q(x,y)=(-1)^(xy), A={X}, fixed 0<q<1/2, and p down to zero:

    J_X-M_X = 4q(1-2q) p log2(1/p) + O_q(p).

In particular q=1/4 forces leading coefficient 1/2. Consequently any universal scalar one-bit tax tau(p) in J_X<=M_X+tau(p), valid for all actual Boolean functions and all interior residual biases, must satisfy liminf_{p->0} tau(p)/(p log2(1/p)) >= 1/2. No tau(p)=O(p) can work. This is a helper obstruction on a product-biased two-bit family, not a uniform FEI counterfamily.

# sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2; README, CURRENT_STATUS (2026-10-11T20:06:24Z snapshot), claim and obstruction registries, packet status, stream next actions, A046 assignment and plan subsection B10 (lines 798-804). Board at stage start: supervisor snapshot 2026-10-11 21:38 UTC. Claude B10/STREAM_NOTES.md was absent; no contrary lead instruction was available.

Read original B09 REPORT.md sections 0-9 at commit adb671ffcda143fa68347806bb96e8c305621a7d, original report blob 71b68e4decf9658a42fef6bb2668e19f25bd214a. Candidate theorem is section 3; exact channel is section 2; two-bit spectrum is section 4; the unsupported endpoint inference is section 5(4). Read repaired interval REPORT.md and CHECK.py at verification/B09_interval_repair_20261011, source revision a1ff93577685acd461b154b04e0c1aa0c65645c8. The repaired certificate, not the original signed-division code, is authoritative for the existing finite sign.

Read B05 original report sections 1-7, commit 80cc2e5027efa56d79c4ecdf7d4949759ef2068b, and B19 independent reconstruction, commit 7955d427222392911dc6af2e4ee3aa8aab67ac8c. These retire the fixed-price all-coordinate local helper, not existential selection or all stopping trees.

Read supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING; the twelve-note source catalog was inspected. Especially relevant are BLOCK_RESTRICTION_IDENTITY equations (1)-(4), LOG_ALLOCATION rare-logarithm control, ROUTE_MAP correction ledger, and GAMMA_ENDPOINT_LEDGER distinction between signed lifetime and dissipation. Historical raw-L/fixed-reserve/weighted controls are recorded as source-reported scope guards, not independently recertified here.

Inspected both versions of both supplied paper texts. Threshold 38pp sections 6.1 and 7, Proposition 7.1 and Corollary 7.2 distinguish corrected entropy/deficit composition from the Shannon channel; earlier 29pp opening has older constants and must not replace the current baseline. Percolation 30pp introduction and Theorems 3.1-3.2 distinguish pivotal influence I from spectral influence J at nonuniform biases, and restrict geometric conclusions to the stated percolation class; the 31pp other version was inspected for scope. These papers are context, not dependencies of the elementary endpoint proof. No complete independent audit of all their proofs is claimed. SOURCE_MANIFEST.json binds locally available inputs by SHA256 and inspection scope.

# complete derivation or exact first unsupported line

1. Exact physical channel. Expanding f_Z in the A coordinates and using biased Parseval gives Pr(S_B=T)=sum_R fhat_p(R union T)^2=E_Z fhat_Z(T)^2. Each child is Boolean, so its squared spectrum has mass one. Thus the joint channel's marginal T is the parent B-marginal. The entropy chain rule yields L_A=M_A+J_A; mutual information gives J_A>=0. This argument is self-contained and handles zero fibers by omission.

2. Boolean source and spectrum. The AND sign has truth table (1,1,1,-1) and identity g=1-2XY. Independence, E phi_X=E phi_Y=0, E X phi_X=sqrt(p(1-p)), and E Y phi_Y=sqrt(q(1-q)) give

    fhat(empty)=1-2pq,
    fhat(X)=-2q sqrt(p(1-p)),
    fhat(Y)=-2p sqrt(q(1-q)),
    fhat(XY)=-2 sqrt(p(1-p)q(1-q)).

Their exact squared law, in that order, is

    a=(1-2pq)^2,
    b=4p(1-p)q^2,
    c=4p^2q(1-q),
    d=4p(1-p)q(1-q).

It sums to one and is an actual Boolean spectrum. Put u=4q(1-q), r=pu. Then Pr(S_Y=1)=c+d=r. The X=0 child is constant. The X=1 child is 1-2Y, with squared masses (1-u,u). Therefore

    M_X=H(a,b,c,d)-h2(pu),
    J_X=h2(pu)-p h2(u),
    E(p,q):=J_X-M_X=2h2(pu)-H(a,b,c,d)-p h2(u).

3. Controlled asymptotic. For a fixed alpha>0 and t(p)=alpha p+O(p^2),

    -t log2(t)=alpha p log2(1/p)+O_alpha(p).

This follows by t/p=alpha+O(p), whose logarithm is bounded, and p^2 log(1/p)=O(p). Also -(1-v)log2(1-v)=O(v) for v=O(p), and a mass O(p^2) contributes O(p^2 log(1/p))=O(p). These estimates follow from the mean value theorem on compact positive intervals and the boundedness of p log(1/p); no finite calculation is used to infer the limit.

For fixed q in (0,1/2), b=4q^2p+O_q(p^2), d=4q(1-q)p+O_q(p^2), c=O_q(p^2), and a=1-O_q(p). Hence

    H(a,b,c,d)=4q p log2(1/p)+O_q(p),
    h2(pu)=u p log2(1/p)+O_q(p).

Substitution proves

    E(p,q)=(2u-4q)p log2(1/p)+O_q(p)
          =4q(1-2q)p log2(1/p)+O_q(p).

At q=1/4, this coefficient is 1/2. Indeed 4q(1-2q)=1/2-8(q-1/4)^2, so 1/2 is the largest leading coefficient forced by this fixed-q AND subfamily. It is not proved to be the largest coefficient over all Boolean gates.

4. Quantifiers and correction. If a scalar tau(p) satisfies the universal one-bit inequality, the actual q=1/4 example gives tau(p)>=E(p,1/4). Divide by p log2(1/p)>0 and pass to liminf. It is at least 1/2. In particular, for every finite K there exists epsilon_K>0 such that E(p,1/4)>Kp for all 0<p<epsilon_K. Thus the universal O(p) tax is impossible. This supplies the missing lower-bound family in B09 section 5(4); that sentence's original reasoning remains invalid, while its endpoint conclusion now has an independent elementary proof.

For 0<p<=1/2 the existing tax simplifies exactly to

    Delta(p)=p log2((1-p)/p),
    Delta(p)/(p log2(1/p)) -> 1.

The actual excess/Delta ratio tends to 1/2. Therefore a replacement tau(p)=c p log2(1/p)+O(p) requires c>=1/2. The current coefficient 1 is not refuted. Sharp universal leading coefficient in [1/2,1] is unpaid, conditional on acceptance of the B09 core upper bound.

5. Aligned disjoint tensor scope guard. Products of Boolean signs on disjoint input blocks have product Fourier laws; their physical-child channels also factor for aligned reveals. Conditional entropy and mutual information add, so M,J and actual excess add. The fixed p=1/8,q=1/4 witness repeated m times forces block tax greater than m*(1195/10000) bits. A tax bounded independently of block size, or a fixed multiple of max_i Delta(p_i), cannot replace the sum universally. This is an elementary consequence of product distributions; no broader composition or shared-variable additivity is asserted.

First unsupported line for the main FEI route: a finite dimension-independent influence payment of the complete actual restriction/composition cost, including terminal entropy and nonreused taxes. Neither the present endpoint obstruction nor B09's candidate uncertainty bound proves that payment.

# executed validation with domain, arithmetic, commands and outputs

SEARCH_SPEC.json was written before executing any finite calculation. Domain: exactly four actual two-bit AND instances, p in {1/8,1/16,1/32,1/64}, q=1/4, block {X}; no symmetry reduction, no random search, no dimension increase. Estimated memory 20 MB, pilot cap 60 seconds; no >300 MB job and no heavy job.

Executed:

    python -X utf8 code/exact_check.py

from this run's directory (the actual invocation used its absolute path). Output out/EXACT_CHECK.json: PASS, four cases, arithmetic runtime approximately 0.0078 seconds. Each spectrum was independently reconstructed by exact truth-table centered-basis sums divided by rational squared basis norms. Parent and marginal laws and the p=1/8 masses were checked exactly. All four excesses were rigorously positive and less than the displayed Delta; the p=1/8 excess was certified >1195/10000 bits.

Logarithms: scale each positive rational x by powers of two to y in [1,2). Use z=(y-1)/(y+1), so 0<=z<=1/3, with 24 rational atanh terms and remainder bounded by 2z^(49)/(49(1-z^2)). This follows termwise from 1/(2j+1)<=1/49 in the positive tail. Divide the resulting ln(y) interval by the strictly positive ln(2) interval using all four endpoint quotients, then add the exact integer scale. Multiplication by a negative entropy weight reverses endpoints. Zero terms are omitted. The checker also enclosed the 17 known integer logarithms log2(2^k), k=-8,...,8. Displayed decimals are rounded outward by exact integer floor/ceiling. No floating point enters a mathematical certificate; runtime measurement is floating point only.

The four finite checks are source and sign verification, not a proof of an all-p statement. The analytic derivation above supplies that statement. The original 1200-term B09 checker was inspected but not replayed; the new checker uses an independent range-reduced implementation.

# proof dependencies and changed downstream conclusions

The new endpoint theorem uses only the displayed Boolean truth table, product expectations, elementary entropy chain rule and asymptotic estimates proved above. It has no unreviewed external mathematical dependency. The original B09 v1 core remains pending review; its Maassen-Uffink step is not accepted by this intake. The known repaired finite witness was independently recertified here.

KNOWN_FALSIFIERS.md preserves direct tax-free failure, signed interval correction, fixed-price rare-logarithm failure, raw-L tensor normalization, fixed-reserve source limitations, weighted physical-TC/pivotal controls, and fixed spectral Renyi obstruction. These have different scopes and do not refute the frozen live helper. Numerical changes alone cannot reopen a retired universal claim.

Changed downstream conclusion: B09 endpoint necessity can be justified by the actual AND family, with necessary leading coefficient at least 1/2. Replace the unsupported upper-bound-to-lower-bound inference by this proof after review. A047/A048/A071 should target genuine strengthened formulas; do not allocate another search to the unchanged tax-free or fixed-price statements. B20 can adopt the intake and source-bound correction; no shared index was edited.

# one next mathematical action and independent reviewer

Next action: determine whether the one-bit universal tax can have leading coefficient 1/2 by optimizing actual Boolean-realizable physical-child pairs; retain q=1/4 AND as the lower boundary and the exact nonasymptotic p=1/8 witness. Freeze the changed formula and bounded domain before computing. This is a fresh sharpness question; it does not ask for another replay of a refuted coefficient.

Independent reviewers: A092 primary, A087 alternate; consumers A038, A047, A048, A071, A076, B09/B19 and B20. Intake is retired locally until a substantive candidate revision or review objection arrives. One new mathematical claim awaits review; full FEI remains open.

# actual persistence receipts or precise save blocker

All artifacts are local under the assigned A046 run: REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json with packet_ids=[A046], FROZEN_POTENTIAL.json, KNOWN_FALSIFIERS.md, SEARCH_SPEC.json, SOURCE_MANIFEST.json, code/exact_check.py, code/finalize.py, and out/EXACT_CHECK.json plus artifact receipts. Rolling STATUS, WORKLOG and LEARNED are current. Schema keys, canonical claim hashes, file sizes and progress-copy identity are checked by code/finalize.py; output is out/VALIDATION.json.

No git, messages, brain writes, publication, other-agent mutations or shared-ledger mutations were performed. Supervisor copying, repository mirror verification, downstream use and independent acceptance have not occurred in this run and are not claimed. Missing B10 lead notes were an access-only limitation, not a mathematical blockage.
