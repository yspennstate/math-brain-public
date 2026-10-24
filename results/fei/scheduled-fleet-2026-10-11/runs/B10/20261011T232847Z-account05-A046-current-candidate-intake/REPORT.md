# exact target, quantifiers, hypotheses and units

A046 stage 2 follows the B10 lead's instruction to retire intake and independently reconstruct the one-bit reduction in B10L-ONEBIT-HALF-TAX@1. The original stage-1 endpoint is not recomputed. Full uniform-cube FEI remains OPEN.

For every finite residual product cube, common real orthonormal Fourier basis, real children G,H of unit L2 norm, and independent physical selector X with Pr(X=1)=p in (0,1), let g_T,h_T be their coefficients. Boolean children are included. Define q_T=(1-p)g_T^2+p h_T^2, posterior u_T=p h_T^2/q_T, selector-present spectral mass b_T=p(1-p)(h_T-g_T)^2, and v_T=b_T/q_T, omitting q_T=0. Let M=H(S_X|S_residual), J=I(X;T) for the actual child-spectral experiment. Entropies are Shannon bits and 0 log 0=0.

The reconstructed exact identity is

    J-M = h2(p)-sum_T q_T [h2(u_T)+h2(v_T)].

Writing (sqrt(1-p)g_T,sqrt(p)h_T)=sqrt(q_T)(cos t_T,sin t_T) and beta=arcsin sqrt(p) gives u_T=sin^2 t_T and v_T=sin^2(t_T-beta). Therefore J-M<=tau(p), where tau(p)=h2(p)-min_t F_p(t), F_p(t)=h2(sin^2 t)+h2(sin^2(t-beta)). If beta uses r=min(p,1-p), swap child labels first when p>1/2. This correction is necessary in the literal all-p claim.

We also repair the source's rounded asymptotic, proving independently

    tau(p)=(p/2)log2(1/p)+(log2(e)/2-1)p+O(p^2 log(1/p))

as p decreases to zero. The source's exact coefficient -0.2787 in an o(p) expression must be replaced by log2(e)/2-1. The finite-p inequality tau<=Delta/2, its full scalar certificate, multi-bit additivity, and global influence payment are separate review obligations.

# sources actually read, revisions and theorem locators

Stage-start BOARD.md is supervisor snapshot 2026-10-11 23:29 UTC. Read B10/STREAM_NOTES.md v1, 23:00 UTC, in full, and own STATUS/LEARNED. The lead explicitly directs A046 to review the exact one-bit reduction and retires intake. Notes v2, 23:31 UTC, were consumed during work and add analytic lemma-A/B review and certificate replay; those were completed. Board reports A092's independent acceptance of A046's endpoint result; its source is read below rather than inferred from the label.

Main review source: claude/B10/runs/20261011T230400Z-claude-B10-onebit-half-tax/REPORT.md, CLAIMS.json, FROZEN_SPEC.json, code/certify_half_tax.py and out/certificate.json. Target is B10L-ONEBIT-HALF-TAX@1's exact reduction, bias convention and asymptotic, plus its boundary lemmas and source replay, not blanket acceptance of that combined claim. The 80-bit mpmath certificate was replayed faithfully with the reported 4,100 positive boxes and three lemma-B boxes. Its full middle-region interval/sign/partition proof has not been independently rationally recertified here; both analytic boundary lemmas were independently reconstructed with exact constants.

Read A096 REPORT/CLAIMS, run 20261011T215017Z-account05-A096-live-gap-ledger: uniform singleton projection bound and its fixed-pair scope. Its REPORT equation after (7) has a source-noted sign typo: J<=h2(r)-h2(delta)+M, not minus M. We do not independently accept A096's theorem or repeat its endpoint census here. Read A047 CLAIMS, run 20261011T220210Z-account05-A047-boundary-search, which retains a pair-dependent endpoint remainder; A047 is separately assigned the constrained finite-p envelope. Read A048 REPORT, run 20261011T221822Z-account05-A048-tensor-stress, which keeps arbitrary terminal entropy under common unrevealed factors and distinguishes physical influence from biased spectral energy. Read A092 stage-1 REPORT/CLAIMS at run 20261011T221121Z-account05-A092-counterexample-referee for prior review provenance.

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was reread in full. The prior intake already froze the B09 candidate and obstruction ledger; those records remain unchanged. Source byte hashes, scopes and missing-source facts are saved in out/SOURCE_MANIFEST.json. No new external literature theorem is a dependency; the lead's cited block-additivity theorem is left conditional and was not fetched.

# complete derivation or exact first unsupported line

1. Independent reconstruction without angles. Write F(X,y)=G(y)+X(H(y)-G(y)). Since phi_X=(X-p)/sqrt(p(1-p)), the two parent coefficients over residual label T are

    alpha_T=(1-p)g_T+p h_T,
    gamma_T=sqrt(p(1-p))(h_T-g_T).

Expanding the squares cancels the cross terms and gives alpha_T^2+gamma_T^2=q_T. Parseval on each child gives sum_T q_T=1. The joint physical-child/spectral probabilities are (1-p)g_T^2 and p h_T^2. Each child law is normalized by hypothesis, so the selector marginal is exactly Bernoulli(p), the spectral marginal is q, and the selector posterior given T is u_T. Thus J=h2(p)-sum q_T h2(u_T). The parent spectral label posterior is v_T, hence M=sum q_T h2(v_T). Subtraction proves the identity. Zero q implies g_T=h_T=0 and is omitted. No Booleanity or entropic uncertainty theorem enters this reconstruction beyond child normalization.

2. Angles and orientation. For q_T>0, the normalized two-vector is a real point on the unit circle. Taking beta in (0,pi/2), sin beta=sqrt(p), cos beta=sqrt(1-p), yields

    alpha_T/sqrt(q_T)=cos(t_T-beta),
    gamma_T/sqrt(q_T)=sin(t_T-beta).

The source's expression with sin^2 beta=min(p,1-p) is valid on p<=1/2 as written. On p>1/2 relabel X'=1-X, p'=1-p, G'=H,H'=G. Parent absent mass is unchanged and the present coefficient changes sign, so both spectral masses and M are unchanged. The channel merely relabels its physical input, leaving J unchanged. The posterior u changes to 1-u and binary entropy is invariant. Only after this relabeling may beta=arcsin sqrt(min(p,1-p)) be used in the stated vector. Alternatively keep beta=arcsin sqrt(p) for all p.

The literal unswapped claim is false: choose G=H=1, p=3/4. Actual M=J=0. Its claimed smaller beta gives sin(t-beta)=2p-1=1/2, so its right-hand side becomes -h2(1/4)<-1/2 bits. This is a Boolean source satisfying the source's hypotheses. It refutes that literal identity, not the scalar half-tax upper conclusion. The identity's derivation in the source REPORT already uses the correct beta; the repair belongs in its all-p statement.

3. Necessary moment and scope. Physical-child normalization also gives

    sum_T q_T u_T=p,  sum_T q_T(1-u_T)=1-p.

Therefore an arbitrary choice of angles and weights satisfying only sum q=1 is not necessarily realizable by two normalized children. The pointwise minimum of F nevertheless gives a valid universal upper bound, because every summand is at least min F. Attainment over normalized real children additionally requires the fixed moment, and attainment over Boolean children additionally requires Boolean inverse transforms. We do not assert that either condition blocks or proves attainment. A047 is already assigned that optimization; it must not be confused with the accepted identity.

4. Independent scalar endpoint repair. Let 0<p<=1/16 and beta=arcsin sqrt(p). F has period pi/2 and symmetry t->beta-t. These reduce every angle to t=beta/2+d with 0<=d<=pi/4. Let a=|sin t|, c=|sin(t-beta)|. The sine triangle identity gives a+c>=sin beta=sqrt(p): on 0<=t<=beta use sin t+sin(beta-t)>=sin beta; on t>=beta the sum is increasing up to the domain endpoint and has value sin beta at t=beta. Also a^2<= (1+sqrt(p))/2<=5/8 and c^2<=1/2.

Put s0=e^(-3/2). If max(a,c)>=s0, at least one squared amplitude belongs to [e^-3,5/8]. Binary entropy has a strictly positive minimum C0 on this fixed compact interval. The trial t=beta/2 has F=2h2((1-sqrt(1-p))/2), tending to zero. Consequently, for all sufficiently small p, a minimizing angle has a,c<s0. This is an existence argument for a neighborhood, not an assertion of an uncomputed explicit cutoff.

On [0,s0], k(s)=s^2 log2(1/s^2), extended by k(0)=0, is increasing and convex: its second derivative is (-4 ln s-6)/ln2>=0 and its first derivative is nonnegative. Jensen and a+c>=sqrt(p) give

    k(a)+k(c)>=2k((a+c)/2)>=2k(sqrt(p)/2)
             =(p/2)log2(4/p).

For 0<=x<1, -ln(1-x)>=x, hence h2(x)>=x log2(1/x)+x(1-x)/ln2. Put S=a^2+c^2. Then S>=p/2 and S<=2e^-3<1/2; a^4+c^4<=S^2 and S-S^2 is increasing up to 1/2. Therefore

    F(t)>= (p/2)log2(4/p)+(p/2-p^2/4)/ln2.

The symmetric trial has x=(1-sqrt(1-p))/2=p/4+O(p^2). Binary entropy expansion, with x of order p, gives

    2h2(x)=(p/2)log2(1/p)+p+(p/2)log2(e)
            +O(p^2 log(1/p)).

The lower bound and trial upper bound squeeze min F to this same expansion. Since h2(p)=p log2(1/p)+p log2(e)+O(p^2), subtracting proves the exact tax expansion stated above. This proves the intended linear coefficient without assuming an exactly symmetric minimizer. It also shows why substituting a rounded -0.2787 as an exact coefficient cannot be accompanied by an o(p) remainder.

5. Analytic half-tax boundary review. LEMMA_REVIEW.md gives the independent all-domain proofs: for p<=2/25 the large-amplitude branch has F>7/25>131/500>R(2/25)>=R(p), with the compact endpoints certified by rational entropy and exp(3) bounds; the small-amplitude branch has F-R>(27/100)p-(41/100)p^2>0. For p in [489/1000,1/2] and |theta-beta|<=301/1000, phi''=-4/ln2+2cos(2theta)log2(cot^2 theta)>=-4/ln2, because the final factors have the same sign. Integrating gives the source semiconcavity bound. A rational sine lower bound gives h2(sin^2 e)>=(97/100)e^2 log2[1/((97/100)e^2)]; the net quadratic bracket is >1/2 over this widened region. When e<0 the negative linear term is bounded by (13/200)*(301/1000-489/2000), smaller than (1/2)*(489/2000)^2; e>=0 is immediate. This discharges the source's lemma-B boxes with exact threshold slack. Full derivations and fourteen rational constant checks are in the accompanying file/output. These analytic regions are checked proofs; intermediate box signs are source-code replay, not a new independent rational certificate.

6. Universal bridge limitation. In actual physical restriction of a uniform cube, every unrevealed original coordinate remains fair conditional on previous coordinate values. Consequently p=1/2 at every such node. A rare biased selector arising from an effective event or a gate output is a different ledger and needs an explicit physical-budget conversion. The exact channel identity is valid for both, but a p log(1/p) tax cannot simply be inserted into a uniform physical-coordinate telescope as though the original coordinate had bias p. Existing A048 common-factor guards likewise leave arbitrary expected leaf entropy untouched.

First unsupported lines are separated: acceptance of tau(p)<=Delta(p)/2 over all p needs an independent reconstruction of the source scalar analytic/certificate chain; extension to a general block needs its additivity argument; a full-FEI consequence needs an actual hereditary nonreusing physical influence payment of conditional erasure plus terminal entropy. None follows from the exact one-bit identity. The corrected scalar endpoint expansion is proved here; the entire original combined claim is not independently accepted.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_REVIEW.json and SEARCH_SPEC.json were saved before the computation. Fixed domain: ten named ordered pairs of norm-one children, five selector biases {1/8,1/4,1/2,3/4,7/8}, 50 cases, at most two residual bits, no symmetry omission and no escalation. Eight pairs are actual Boolean spectra of explicitly given constant, literal and AND sign tables; two are explicitly labeled real norm-one vectors, matching the lead's broader hypothesis. No real vector is asserted to be Boolean.

Command executed:

    python -X utf8 code/reduction_check.py

The actual command used the absolute path in this run. Output out/REDUCTION_CHECK.json: PASS, 50 cases, about 0.0228 arithmetic seconds. Estimated memory 20 MB, runtime cap 60 seconds, no >300 MB job and no heavy job. Exact arithmetic reconstructs parent masses, physical channel, its marginal, posterior moment, both conditional entropies and relabeling invariance. Entropy identities are verified as matching rational coefficient dictionaries multiplying log2(prime), from exact factorization of each rational mass. Equal dictionaries establish exact equality; no logarithmic independence assumption or floating sign calculation is used. The orientation witness has exact wrong ledger -2+(3/4)log2(3), i.e. -h2(1/4), while the actual ledger is identically zero. Its strict sign follows from the two positive interior entropy summands; no numerical logarithm approximation is required.

The all-dimensional proof is analytic, not inferred from the 50 cases. After freezing CERTIFICATE_REPLAY_SPEC.json under the updated lead instruction, executed python -X utf8 code/replay_certificate.py with a 60-second cap: PASS, 4,100 positive boxes, three lemma-B boxes, seven splits, 3.02 seconds. It reads the source with runpy and writes only out/CERTIFICATE_REPLAY.json here, creating no source pycache or output. This is a source-code replay, not independent arithmetic implementation. After freezing LEMMA_CHECK_SPEC.json, executed python -X utf8 code/check_lemma_constants.py: fourteen exact rational constant comparisons PASS, saved to out/LEMMA_CONSTANT_CHECK.json. Estimated memory remained below 30 MB. No new independent continuum box certificate, external paper theorem or multi-bit search was performed.

# proof dependencies and changed downstream conclusions

The corrected reduction and scalar endpoint repair use product-basis coefficient expansion, normalized child laws, binary entropy, elementary trigonometry and calculus proved in this report. No pending FEI helper is assumed. Source B10L-ONEBIT-HALF-TAX@1 is the review target, not an accepted all-components premise.

Review verdict: HOLDS for the exact reduction with beta=arcsin sqrt(p), or with the explicitly relabeled minimum-bias convention. ERROR in the source's literal unswapped p>1/2 identity, with an exact Boolean witness. ERROR in presenting a rounded linear coefficient as exact in the source's o(p) expansion; corrected expansion proved here. HOLDS for the analytic lemma-A/B boundary regions with the displayed exact constants. The middle-region scalar certificate reproduces PASS but is not independently rationally recertified; the full finite-p statement is not blanket-accepted or declared false. The block statement remains CONDITIONAL and the global bridge OPEN.

The source dependency edge into A050's scoped repair must use the corrected orientation and exact coefficient. A047's envelope must include sum q sin^2 t=p and its separate Boolean inverse constraint. A048/A049 cannot import block additivity from this identity. B20 should route the source-bound corrections; no shared indices were edited and no messages were sent. Because A046 contributes repairs, A046 is a contributor to the corrected subclaim and cannot independently accept its own corrected version; A092/A087 must review it. Original reduction on p<=1/2 was independently reconstructed, but this is not blanket acceptance of the lead's combined claim.

# one next mathematical action and independent reviewer

NEXT: A050/A064 should specify the actual hereditary physical restriction/composition budget in which the corrected singleton channel is used, explicitly converting any effective rare-selector bias to original influence and retaining expected leaf entropy; then test the nonreuse identity on the existing sparse-bent control-first tree. A046 should audit that complete ledger when source-complete rather than start another scalar or small-function census. A092 primary and A087 alternate review the corrected reduction/endpoint subclaim; A047 handles the constrained finite-p envelope already assigned by the lead.

# actual persistence receipts or precise save blocker

Saved only inside A046's assigned stage-2 run: the four protocol files, frozen reduction/replay/lemma specifications, REVIEW_FINDINGS.md, REVIEW.json, LEMMA_REVIEW.md, scripts and exact/replay outputs, source manifest, validation and receipts. Rolling STATUS.md is two lines, WORKLOG is appended and LEARNED retains both stages' durable statements. The finalizer checks protocol keys, statement hashes, report headings including this stage's requested terminal bridge paragraph, copy identity and file-size caps.

Independent corrected-version review, supervisor publication/copy, mirror verification and downstream adoption are pending. No git, messages, brain writes, shared-tree changes or other-agent writes occurred. Failed guessed source paths were replaced by the actual discovered run paths and are not evidence that their reports were absent.

# Universal bridge

This stage moves the lead-named singleton-tax reduction underlying C019 by independently proving its all-dimensional channel identity, repairing its all-p orientation and exact endpoint expansion, reconstructing both analytic half-tax boundary lemmas, and reproducing the middle-region certificate; it removes two statement defects and resolves the analytic-boundary review, but does not improve a universal FEI constant or supply an independent rational certificate for every intermediate box. What remains is full scalar-certificate/block acceptance where needed and, decisively, a hereditary conserved physical influence payment of conditional erasure and expected terminal entropy; on a uniform physical-coordinate tree all node biases are already 1/2, so rare effective-selector taxes need an explicit budget conversion. NEXT targets that conversion and the complete stopping-tree residual on the existing sparse-bent obstruction, the shortest route toward C019/C018 rather than another isolated class theorem or repeated biased-gate census.
