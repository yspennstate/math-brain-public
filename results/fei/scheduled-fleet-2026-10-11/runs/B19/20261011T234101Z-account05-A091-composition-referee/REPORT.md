# exact target, quantifiers, hypotheses and units

For every Boolean sign f on a finite independent product cube, all interior coordinate probabilities p_i, and every physical block A with complement B, independently review B09-BIASED-BLOCK-UNCERTAINTY@1:

    L_A=M_A+J_A,
    0<=J_A<=M_A+Delta_A,
    Delta_A=sum_{i in A}[h2(p_i)+log2 max(p_i,1-p_i)].

Here S has the actual squared normalized product Fourier spectrum, M_A=H(S_A|S_B), and L_A=H(S)-E_z H(S(f_z)). The physical assignment z is sampled from its inherited product law; J_A is the mutual information between that assignment and a spectral sample of its Boolean restriction. Entropies are in bits. I_p is spectral expected cardinality, not unweighted pivotal influence under bias. Full FEI remains OPEN.

Verdict on the analytic core: ACCEPT_AT_STATED_SCOPE, without a substantive repair. A093 already independently accepted it; this is the second requested reconstruction, not a novel theorem. The B19 lead specifically assigned this review. Optimal tax, sharp singleton improvements, arbitrary composition additivity and global influence payment are separate claims and are not accepted by this verdict. To consume the core in C019, this run also derives and checks a terminal-inclusive corrected-entropy/deficit ledger, with no assertion of a universal payment.

# sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-11 23:39 UTC, B19 STREAM_NOTES.md v2 23:35 UTC and own STATUS.md at stage start. Read full execution protocol revision 2026-10-11-execution-v2 again. Source B09 run 20261011T195500Z-account01-B09-biased-restriction-uncertainty, original REPORT Sections 2-3, at open-problems commit adb671ffcda143fa68347806bb96e8c305621a7d, report blob 71b68e4decf9658a42fef6bb2668e19f25bd214a. Read the repaired interval report at verification/B09_interval_repair_20261011, pinned repair commit a1ff93577685acd461b154b04e0c1aa0c65645c8. Its code is not reused.

Primary uncertainty source: Maassen and Uffink, *Generalized Entropic Uncertainty Relations*, Phys. Rev. Lett. 60 (1988), 1103-1106, DOI 10.1103/PhysRevLett.60.1103. Visually inspected pages 1103-1104 of the final article: overlap definition (5), Shannon relation (6), norm interpolation (10)-(13). Primary [author-hosted PDF](https://www.math.ru.nl/~maassen/papers/EntrUncert.pdf) was accessed; the identical article preserved by A093 is copied into this run's out/maassen_uffink_1988.pdf and independently rendered/read. The article's logarithms are natural; division by ln2 is required for this application. Bibliographic metadata also verified at [APS](https://doi.org/10.1103/PhysRevLett.60.1103). No claim of priority, new literature theorem or new classical uncertainty proof is made.

A093 REPORT and CLAIMS were read before extending its completed baseline. A024 REPORT was read for its signed normalization credit: that claim concerns a queried uniform physical child inside a disjoint composition. The ledger here is for a fixed arbitrary product physical law and general adaptive block tree, and does not freeze an outer output law. Threshold 38-page Section 6.1 supplies the established corrected entropy definition. B09 lead notes v2 were read: sharper scalar taxes already have other reviewers; no fresh scalar optimization or blanket endorsement is made here. Source hashes and audit locators are in out/SOURCE_RECEIPTS.json. Byte receipts do not imply a review of every theorem in a file.

# complete derivation or exact first unsupported line

## Actual physical-child probability law

Use phi_i(x_i)=(x_i-p_i)/sqrt(p_i(1-p_i)) on {0,1}. Write c_{R,T}=fhat_p(R union T), R subset A, T subset B, and q_T=sum_R c_{R,T}^2. Expanding on A and using product Parseval gives

    fhat_{z,p_B}(T)=sum_R c_{R,T} phi_R(z),
    E_z fhat_z(T)^2=q_T.

Define the joint law P(Z=z,T)=P_A(z) fhat_z(T)^2. Booleanity is essential for its physical marginal: every child has squared norm one, so summing over T gives P(Z=z)=P_A(z). Its T marginal is q. Therefore

    J_A=H(q)-E_z H(fhat_z^2)=I(Z;T)>=0,
    L_A=H(fhat_p^2)-E_z H(fhat_z^2)=M_A+J_A.

Zero-q fibers are omitted; all other spectra are probability laws. For A empty the experiment is unchanged and L=M=J=Delta=0; for B empty T is deterministic, J=0 and M=L=H(fhat_p^2). A normalized real function with nonconstant child squared norms does not have the required physical marginal: for example sqrt(2)1_{x=1} at fair x has child norms zero and two. Normalizing its children independently changes the experiment. This is why a unit vector alone is not a substitute for the Boolean physical source.

## Primary uncertainty application

For q_T>0, normalize a_R=c_{R,T}/sqrt(q_T) and b_z=sqrt(P_A(z)) fhat_z(T)/sqrt(q_T). Both vectors have norm one, and b=U_A a, where

    U_A=tensor_{i in A} [[sqrt(1-p_i),-sqrt(p_i)],
                         [sqrt(p_i),sqrt(1-p_i)]].

Its maximum entry magnitude is c_A=prod_i sqrt(max(p_i,1-p_i)); both bases are orthonormal. The primary Shannon theorem yields H(a^2)+H(b^2)>=-2log2 c_A. Averaging in q gives M_A+H(Z|T)>=-sum_i log2 max(p_i,1-p_i). Since H(Z)=sum_i h2(p_i), subtraction proves J_A<=M_A+Delta_A. Together with the previous identity and J_A>=0, this proves the core for arbitrary finite blocks, not just singletons.

No Boolean constraint on the individual normalized spectral fiber is required by that theorem. Its use is valid for real amplitudes because they are a special case of complex vectors. Global Booleanity was used separately to identify the physical marginal. An empty block is treated directly rather than invoking the article's nontrivial-overlap wording.

## Exact bias endpoints and tax normalization

Put r=min(p,1-p). The one-coordinate tax is exactly

    Delta(p)=r log2((1-r)/r),       0<r<=1/2.

It is nonnegative, symmetric under p<->1-p, zero at p=1/2 and tends to zero at both deterministic endpoints. More precisely,

    Delta(p)-r log2(1/r)=r log2(1-r),
    -r^2/[(1-r)ln2] <= remainder <= -r^2/ln2.

The inequalities follow by integrating 1/(1-u) on [0,r]. Thus the available tax has leading coefficient one and a negative second-order correction. This is an upper-bound tax, not a necessity/optimality result; the newer sharp scalar tax is a separate claim. Deterministic coordinates are deleted before constructing a normalized basis, so no p=0 or p=1 division occurs. On a fixed finite truth table, coefficients whose sets contain a degenerating coordinate have vanishing squared mass, and all other masses converge to those of the supported restriction; finite Shannon entropy is continuous. The limiting inequality therefore agrees with coordinate contraction. The two endpoints cannot be handled by pretending the singular basis is already defined there.

## Corrected entropy and deficit transport into C019

Fix the original physical product probabilities, and let a node reveal a block A. Write sigma_i^2=4p_i(1-p_i), h0(f)=P_f(empty)log2(1/P_f(empty)), and

    Eplus_p(f)=H_p(f)-h0(f)+sum_i I_i^p(f)log2 sigma_i^2,
    delta_p(f)=I_p(f)-V_p(f).

Unrevealed-coordinate spectral influences average exactly to their parent values, by the q marginal identity. Let

    I_A=sum_S |S intersect A| P_f(S),
    K_A=sum_{nonempty S subset A} P_f(S).

Then I_parent-E I_child=I_A and V_parent-E V_child=K_A. Hence the deficit spent at this physical node is

    d_A=I_A-K_A>=0.

The inequality follows termwise: a nonempty set contained in A spends |S|-1; a set meeting B spends |S intersect A|. In particular a singleton reveal spends I_i-P_f({i}), not the entire I_i deficit budget.

The exact corrected-entropy decrement is

    Eplus_parent-E Eplus_child
      = M_A+J_A+sum_{i in A} I_i log2 sigma_i^2
        +E h0(child)-h0(parent).                         (1)

Now take any finite adaptive physical restriction tree. Each internal node's block is chosen from the already observed physical history; the leaf partition consists of product-law cylinders. Its probability w_v is the product of actual physical branch probabilities, not an artificial fair weight. At each node use (1), then sum with w_v. Every h0 term cancels except root and leaves. The resulting identities are

    Eplus_root=E Eplus_leaf
       +sum_v w_v[M_v+J_v+sum_{i in A_v}I_i(f_v)log2 sigma_i^2]
       +E h0(leaf)-h0(root),                             (2)
    delta_root=E delta_leaf+sum_v w_v d_v.               (3)

Substitute only the accepted core to obtain the valid sufficient upper ledger

    Eplus_root <= E Eplus_leaf
       +sum_v w_v[2M_v+Delta_v+sum_{i in A_v}I_i(f_v)log2 sigma_i^2]
       +E h0(leaf)-h0(root).                             (4)

For terminal inequalities Eplus_leaf<=C delta_leaf, the exact unproved condition for a C-deficit payment is that the complete nonterminal term in (2), including its terminal h0 reserve, is <=C sum_v w_v d_v. The stronger sufficient condition replaces M+J by 2M+Delta as in (4). These are explicit obligations, not established bounds. At uniform original inputs the sigma logs vanish and Delta=0; converting to full H gives the usual C019 terminal-inclusive entropy/influence telescope. The biased core is thus a valid dependency, but pays no unpaid M or terminal entropy by itself.

A biased literal demonstrates the required cancellation. For f=2x-1, v=4p(1-p), its spectrum is (1-v,v), Eplus=delta=0. A full physical reveal has M=h2(v), J=0 and I_A=v. Exactly

    h2(v)+v log2(v)-h0(f)=0.

Removing the negative sigma log or empty-atom reserve would turn a certified zero-deficit terminal into spurious rare-bias debt. Even if those terms are kept, the crude MU sufficient ledger pays an excess h2(v)+Delta(p)>0 at this zero-deficit node; one must stop at the already certified literal terminal or use the exact decrement. This illustrates insufficiency of the upper ledger, not failure of the core or corrected FEI. Likewise irrelevant inputs contribute no actual decrement but a positive raw coordinate tax at nonuniform bias; contracting them is necessary before treating tax as a payment budget.

**First unsupported universal line:** the expectation of the entire corrected nonterminal charge in (2), with terminal h0 reserve and no reuse of d_v, is bounded by an absolute multiple of the root deficit spent. Equivalently, in the original uniform formulation one still needs paid conditional spectral erasure plus certified terminal entropy. No gate primality, scalar sharpness or finite table check establishes that line.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs are out/FROZEN_SPEC.json, out/FROZEN_ENDPOINT_SPEC.json and the scheduling revision out/FROZEN_SHARD_SPEC.json. The block case count was corrected arithmetically before the pilot: 4*4*2+16*3*4+256*3*8=6,368. There is no symmetry reduction or dimension escalation. After the original law-0 watchdog stopped, the unchanged three-bit domain was partitioned into 48 disjoint 16-mask jobs, each with its own 58-second watchdog. Estimated memory is 60 MB; no job was expected to exceed 300 MB, so no memory-gated job was started.

Commands from this run directory:

    python -X utf8 code/check.py --pilot
    python -X utf8 code/check.py --law 0   # watchdog stopped this attempt
    python -X utf8 code/shards.py         # all 48 fixed slices completed
    python -X utf8 code/endpoints.py

The implementation computes independent unnormalized centered-bit moments and reconstructs each child's amplitude by rational polynomial evaluation on the revealed coordinates. No square-root matrix code from B09 or A093 is reused. Probability marginals and entropy/telescope identities are checked in Fraction arithmetic and rational coefficient vectors of prime logarithms. Nonnegative core margins on this finite domain use rational atanh-series log intervals; exact zero vectors are recognized algebraically. A finite pass corroborates the displayed all-dimensional proof; it does not prove a universal payment. Actual counts and runtimes are written in out/PILOT.json, out/SHARDS.json, each out/LAWk_a_b.json and out/ENDPOINTS.json. No full-law certificate is claimed for the stopped attempt.

The fixed AND witness independently reconstructs masses (225,7,3,21)/256 and certifies J-M>1195/10000 by a different range-reduced logarithm implementation. The retained repaired-source 18-decimal enclosures are compared with this new outward interval. Scalar endpoint remainder inequalities above are analytic; at k=40 the diagnostic uses overlap tolerance because a fixed 1e-30 mesh does not resolve a p^3-wide bound, and no stronger numerical certification is claimed. The decisive AND sign is rigorously certified without tolerance.

Final executed totals: 6,368 block experiments (224 pilot plus 6,144 sharded three-variable cases), 2,304 adaptive trees, 273,190 exact assertions including endpoint checks. The first unsharded law-0 job stopped at the frozen 58-second watchdog and produced no law certificate; it is superseded by 48 complete nonoverlapping 16-mask slices, with no domain or dimension increase. Commands: `python -X utf8 code/check.py --pilot`, `python -X utf8 code/endpoints.py`, and `python -X utf8 code/shards.py` (each child uses `--law k --start a --end a+16`). Passed summary: out/SHARDS.json; per-slice outputs out/LAWk_a_b.json. Endpoint certificate: out/ENDPOINTS.json. The repaired AND interval independently gives M in [0.227909707141212807,0.227909707141212808], J in [0.347454723165637765,0.347454723165637766] and J-M in [0.119545016024424957,0.119545016024424958] bits, strictly above 1195/10000. Small-bias remainder inequalities are analytic; at p=2^-40 the fixed numerical mesh does not resolve the p^3-wide remainder band, and the endpoint diagnostic explicitly allows enclosure overlap tolerance. This tolerance is not used as a proof of that band.

# proof dependencies and changed downstream conclusions

B09 core@1 is accepted from finite product Fourier expansion, Boolean child Parseval, Shannon chain rules and primary Maassen-Uffink (5)-(6). This is an independent review, so the original author remains the contributor; no material repair is supplied to the core. A093's earlier review remains separate and intact. The classical theorem is an external proved premise; the application is fully reconstructed here.

A041/A045/A050/A057/A064/A096/A097 may now consume the core with explicit physical branch probabilities. The corrected tree identity supplies the exact place for sigma and h0 credits and distinguishes a deficit payment from ordinary influence spending. It neither accepts the sharp one-bit tax nor the weighted-threshold FEI+ endpoint nor a global tax budget. B20 should retain the distinction between accepted core dependency, sufficient upper ledger and unpaid universal payment. No shared registry has been edited and downstream adoption is not inferred from local artifacts.

# one next mathematical action and independent reviewer

Next: evaluate the complete charge (2) on the actual overlapping-control stopping tree requested of A050/A057/A064, using only the prescribed single-use local deficit reserves and certified terminal children. The immediate question is whether the recentered signed outer residue fits that reserve after the inner KL credit, rather than whether another scalar tax is smaller. A090/A085 should independently review this tree-ledger application; the core already has separate A093 and A091 reconstructions.

# actual persistence receipts or precise save blocker

All four protocol files, report, frozen specs, source receipt list, independent checker, primary PDF/images and outputs are local under the assigned A091 stage directory. Rolling STATUS.md, WORKLOG.md and LEARNED.md are maintained only in A091. Final readback hashes and schema checks are in out/RECEIPTS.json. Supervisor copy, remote mirror verification and downstream adoption remain pending. No local save blocker or external write is claimed.

# Universal bridge

This stage moves C019 stopping-tree payment by closing the specifically assigned B09 core dependency with a second primary-source reconstruction and by writing its terminal-inclusive corrected-entropy/deficit consumption rule (2)-(4). It improves no universal FEI constant: the complete conditional spectral charge, single-use deficit payment and terminal reserve remain unpaid. NEXT tests the exact recentered outer residue against one local reserve on the live overlapping-control tree, because that is the missing universal payment interface; another isolated gate-class or scalar-tax result would leave the same bridge untouched.
