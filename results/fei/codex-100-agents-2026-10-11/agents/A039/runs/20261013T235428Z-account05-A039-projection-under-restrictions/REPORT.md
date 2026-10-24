# exact target, quantifiers, hypotheses and units

Complete the productive unfinished B08 packet: minimize actual physical-tree debt minus queried-spectral-bit posterior credit, retaining terminal entropy. For every finite Boolean sign, the objective is C(T;f)=sum_h w_h B_i(f_h)+E_leaf H(f_leaf), where B_i=H(S_i|S_-i)=h2(Inf_i)-I_P(S_i;S_-i). All information is in bits and physical histories have fair branches. Resolve the optimal tree for every m-bit point defect and the frozen actual B05 roots k=2,r=4 and k=4,r=8; test whether root-optimal control-first order survives descendants. Full FEI remains OPEN.

Closed locally: an exact optimum formula for all m>=1, with 2-4/m<=V_m/I_m<=2+log2(e)/m and limiting ratio 2; exact finite B05 optimality certificates; and an actual descendant obstruction to hereditary control-first ordering. These are scoped completions of the lead's existing assignment, not a new broad universal candidate.

# sources actually read, revisions and theorem locators

Read BOARD at stage start (supervisor snapshot 2026-10-13 23:49 UTC), own STATUS, B08 lead notes v2 (2026-10-11 23:35Z), and full execution protocol revision 2026-10-11-execution-v2. Read the unfinished 20261012 TREE_TARGET/code/certificate and resumed that productive work, preserving its original files. The latest run copies their bytes with hashes in RESUME_RECEIPTS. Read current A038 stage-3 REPORT (interleaved reserve and unpaid signed reset) and A097 stage-3 REPORT (single shared-data collision and seed debt); these are context, not new proof premises. Targeted CLAIM_REGISTRY/PACKET_STATUS/BOARD reads checked the current B08 interfaces. Prior required campaign and paper reading retains the completed first-stage scope; no new external paper theorem is used or claimed read this stage.

Proof locators: TREE_TARGET.md physical Bellman objective and exhaustive D/P state transitions; OPTIMUM_PROOF.md all-m recurrence, descendant witness and finite certificate induction; prior A039 DERIVATION/claim v1 for compensated physical transfer; prior locally reviewed A037 common-lift v1 only for the root-posterior interpretation. Source hashes are in out/SOURCE_RECEIPTS.json. The shared log helper is pinned to SHA256 d6bc7dd1abce58f20c9488cd692818b12a6861d82b0f3c512b391005ab4d2599.

# complete derivation or exact first unsupported line

The actual coherent split gives H(parent)-average H(child)=B_i+JS_i. Therefore C=H(root)-sum w JS, and completing a leaf decreases C by nonnegative JS. The minimum exists on complete trees and obeys V(g)=min_i[B_i(g)+average V(child)], constants zero. Coordinate choices and remaining terminal costs are retained in a single tree; randomization cannot improve the minimum.

For f_m=1-2*1_0, all queries are symmetric and the only nonconstant child is f_(m-1). With a=2^(1-m), B_m=phi((1-a)^2,a^2)+(2^(m-1)-1)*2a^2 and V_m=B_m+V_(m-1)/2, V_1=0. Every complete adaptive tree has this same optimum. The elementary bound 0<=phi((1-a)^2,a^2)<=a^2 log2(e/a^2) gives the stated all-m ratio bounds and limit. OPTIMUM_PROOF contains the complete derivation, including m=1.

For B05, exhaustive restrictions reduce to the proved D/P classes, with exact spectra and prime-log Bellman costs. The k=2 and k=4 roots uniquely favor the control orbit; complete control-first policies equal the optimum exactly. Certified V/I intervals are respectively [1.836014211380,1.836014211381] and [1.956704604624,1.956704604625]. The k=4 influence is 141/4096; V is in [0.067357263001,0.067357263002]. Selector-first and data-first costs are strictly larger. These are finite optimum results, not all-even-k extrapolations or new B05 class FEI proofs.

Root optimality is not hereditary: D(1,1,2,r) for each r=4,...,8 is an actual root descendant, and uniquely favors its quadratic pair orbit over all other coordinate types. In coordinates its active core is (-1)^(u v)-2*1_{u=v=w=0,y=1}. At r=4 the control-query Bellman gap is in [0.000187542886,0.000187542887] bits; exact positive gaps for all five r are recorded. Thus deleting data exposure from an ordering rule loses genuine information even in this frozen family.

First unsupported universal line: V(f)<=K I(f) for every Boolean sign with one absolute K, or a paid transfer of prescribed terminal references on the same history. The optimal erasure objective does not price a reset or arbitrary terminal core reference. A038's reserve release and A097's compatible-reference posterior KL are not the B08 queried-bit mutual information.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC was saved before the resumed k=4 job; out/SECOND_CHECK_SPEC before independent verification. Frozen k=2 pilot from the unfinished stage was adopted once: 35 canonical states, 605 assertions, 0.0288979s, independent uncompressed check of 48 truth-function states. No automatic parameter increase occurred. Main k=4: 162 states, 208 comparisons, 2480 assertions PASS in 0.7695279s. The complete tree ledger checks sum weighted B=V, V+sum weighted JS=H, the compensated TC credit/Gamma identity, sum removed influence=141/4096, and zero terminal entropy/TC.

Executed commands from A039:

    python -X utf8 -B runs/20261013T235428Z-account05-A039-projection-under-restrictions/code/optimal_tree.py 4
    python -X utf8 -B runs/20261013T235428Z-account05-A039-projection-under-restrictions/code/verify_tree.py 2
    python -X utf8 -B runs/20261013T235428Z-account05-A039-projection-under-restrictions/code/verify_tree.py 4
    python -X utf8 -B runs/20261013T235428Z-account05-A039-projection-under-restrictions/code/check_and.py

Independent reconstruction uses full Boolean truth tables, recursive even/odd Walsh and all actual coordinate alternatives, with no compressed transitions or activated-spectrum formula. Pilot PASS: 32 truth-function states, 115 alternatives, all 35 canonical values, 52 assertions, 0.0936578s. k=4 PASS: 165 truth-function states, 1167 alternatives, all 162 canonical values, 376 assertions, 44.3541508s. It recomputes the five strict descendant gaps and re-encloses all saved prime logs. This is an alternate internal implementation, not an external reviewer acceptance.

AND PASS: all 16 recurrence states, direct physical spectra/query debts for m<=6, 60 assertions, 0.0626542s. All-dimensional conclusions come from the proof. Probabilities, spectra and log vectors are exact integers/Fractions; signs use rational outward atanh enclosures with proved tails. Exact ties are coefficient-map zero. No floating sign is accepted. Memory estimates are 80 MB for compressed optimization and 200 MB for independent verification, below the 300 MB memok trigger; observed peak memory is unmeasured. No heavy/background/GPU job occurred. The verifier itself completed under 60s.

# proof dependencies and changed downstream conclusions

The prior A039 compensated-transfer v1 is the existing identity interface; the needed physical entropy decrement is re-derived in TREE_TARGET. A037 physical-common-lift v1, locally independently reviewed by A039 in the first stage, supports only the optional posterior interpretation. Finite spectra and optimality are independently reconstructed here and do not require A038/A097 new unreviewed claims. Earlier 20261012 partial work is preserved and adopted with explicit provenance, rather than retroactively declaring that interrupted stage complete.

A037/A040/A064/A091 can use the exact optimum benchmark and descendant order obstruction. A038's new interleaved reserve confirms that the next task is reset compatibility after data exposure, rather than another already-paid root activation. No universal FEI constant improves. The lead's best-tree assignment is resolved for all AND_m and the explicitly frozen B05 roots; arbitrary B05 parameters remain outside the optimum claim. New claim is author-proved/exactly validated, pending independent external review. Registry adoption and downstream use are unobserved.

# one next mathematical action and independent reviewer

Compare the signed common-kernel Bayes product/occupancy reset with A038's owned selector-reserve release at one controller query on the three-state priority gate after a nonconstant data prefix, retaining both child cores and terminal entropy. A088 primary and A094 alternate should independently reconstruct the present optimum/certificate proof; A038/A064/A091 are the next mathematical consumers. The descendant obstruction supplies a concrete reason to keep the data-exposed state in this compatibility check.

# actual persistence receipts or precise save blocker

The four protocol files, proof, frozen specs, code and exact outputs are saved in this run. STATUS is updated to two lines; WORKLOG and LEARNED append the result. code/finalize.py checks exact protocol key sets, claim hash, PACKET_DELTA equality, required report fields, and all file sizes; out/PERSISTENCE_RECEIPTS.json records observed hashes. No local save blocker. Source-complete internal validation is distinct from external review, supervisor copying, mirror verification and public release; those are not asserted.

Universal bridge: This stage moves C019 stopping-tree payment and its C024 history interface by completing the lead's best-tree objective, proving the all-m AND optimum with limiting cost/influence 2, certifying both frozen B05 root minima, and identifying five exact data-exposed descendants where the root-optimal control-first rule fails. It improves no universal FEI constant: V<=K I for arbitrary functions, prescribed-reference reset payment, and terminal core cost remain open. NEXT is the shortest identified route toward full FEI because it compares the actual signed reset with the newly conserved, singly owned selector reserve at the first data-dependent controller exposure; it targets the shared unpaid interface rather than adding an isolated class entropy bound.
