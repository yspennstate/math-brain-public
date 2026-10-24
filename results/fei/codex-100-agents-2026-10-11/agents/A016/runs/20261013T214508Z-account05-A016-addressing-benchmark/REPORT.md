# A016 stage 3: a shared bit defeats factor-only boundary pricing

## exact target, quantifiers, hypotheses and units

Test the stage-2 proposed repair of B04's C019 boundary mechanism: remove every exact tensor spectator before summing 2I(D_v) at nodes with exact spectral erasure B_v>K Inf_v. Use a growing Boolean family whose bent-splice modules share one physical data bit. Decide whether factor removal suffices on the selector-first rule, and produce a complete paid alternative with its terminal entropy retained. All variables are independent fair bits, signs are Boolean +/-1, entropy/costs are in bits, and derivative influence means L2 Dirichlet energy, not trinary edge-disagreement probability.

The theorem below holds for all integers a>=1 and even m>=4. The shared-bit family has n=1+am physical coordinates. The selector-first rule queries x_1,...,x_a and then stops. Factor removal is the strongest possible removal of exact independent sign factors on disjoint physical coordinates, recomputed at every reached node. The alternative queries the shared bit z first and stops with explicitly coded leaves.

Outcome: factor removal still leaves a quadratic-in-a boundary bill, although the root has no independent factor at all. For every fixed K choose m with (m-1)/2>K; all selected nodes are genuinely bad and their factor-minimized bill divided by I tends to infinity. This refutes that specified rule/repair, not the existence of a universal adaptive tree. Shared-bit-first has zero K=4 bad-node bill and keeps the terminal cost explicit. A fixed normalized root reference has complete cost <=(8/3)I on the same family. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md, 2026-10-13 21:44 UTC; complete B04 STREAM_NOTES.md (still v2, 2026-10-11 23:25 UTC); own STATUS.md; and EXECUTION_PROTOCOL.json (fei-execution-protocol/2, revision 2026-10-11-execution-v2). The lead has not replaced its old A016 bent-splice target. That target was closed locally in stage 2, so this run follows the recorded NEXT and the protocol's productive dependency/objection dispatch, rather than repeating code ratios.

Relevant updates: A018 stage 2 independently reconstructs B04-NODE-BOUNDARY@1 and explicitly names spectator-free shared-coordinate stopping payment as the next gap. Its source-complete REPORT.md, 20261012T010436Z run, was read, especially Sections 3-4 and its terminal-inclusive open line. The stage-2 A016 REPORT.md/CLAIMS.json gives the disjoint tensor spectator countercharge and the exact factor-removal correction; its pending-review status is preserved. A017's one-edit fiber and A020's finite caps do not address the growing coupled family here. A019's assigned overlapping-selector translation problem is different. No other agent's current/shared files were changed.

The only imported local bound used in the paid tree is C005's JS_i <=(2/ln2) Inf_i. Its elementary row proof is in A018 stage 1 REPORT.md Section 2; that report was already read and is pinned again. The new family identities, physical factorization certificate, charge formulas, terminal codes and normalized root reference are derived below. Exact source-file digests are in out/SOURCE_RECEIPTS.json. These hashes and the board are navigation/persistence evidence, not independent acceptance of this new theorem.

## complete derivation or exact first unsupported line

### 1. A single shared physical bit

For each module j use a private selector x_j and m-1 private data bits t_j=(t_{j,1},...,t_{j,m-1}), together with one COMMON data bit z. Define

    c_j(t_j)=(-1)^(t_{j,2}t_{j,3}+...+t_{j,m-2}t_{j,m-1}),
    b_j(z,t_j)=(-1)^(z t_{j,1}) c_j(t_j),
    f_j(z,x_j,t_j)=b_j(z,t_j)-2 x_j 1{z=0,t_j=0},
    F(z,x,t)=product_{j=1}^a f_j(z,x_j,t_j).

The values at a flipped point remain Boolean, since b_j(0,0)=1. Each b_j is exactly the m-bit paired quadratic bent core from stage 2, with its first bit identified across modules. This is not a disjoint product: all modules depend on the same z.

Set delta=2^{-m}. At z=0 the module is

    psi_j(x_j,t_j)=c_j(t_j)-2 x_j 1{t_j=0},

and at z=1 it is (-1)^(t_{j,1}) c_j(t_j). The private blocks tensorize only AFTER revealing z. Denote the z=0 module's data influence and total influence by

    J_0=(m-2)/2+2(m-1)delta,
    L_0=J_0+2delta=(m-2)/2+2m delta.

The private selector influences before revealing z are delta. At z=0 t_{j,1} has influence 2delta, and each other private data coordinate has influence 1/2+2delta; at z=1 these influences are 1 and 1/2. Averaging gives every private data coordinate of F influence 1/2+delta.

For the shared z edge, the ratio of the two branches is a product of independent block signs

    (-1)^(t_{j,1}) [1-2 x_j 1{t_j=0}].

Each such sign has mean -2delta. Thus

    d_z=Inf_z(F)=[1-(-2delta)^a]/2,
    V=(m-1)/2+m delta,
    I(F)=a V+d_z.

This is linear in a, and d_z>=3/8 (a crude bound sufficient below). The exact child influences are

    I(F|z=0)=a L_0,
    I(F|z=1)=am/2,
    I(F)=d_z+[I(F|z=0)+I(F|z=1)]/2.

The identity uses the actual physical coordinate z. No oblique or spectral basis change is used.

### 2. Exact physical factorization, including all descendants

Write F=(-1)^P, with the unique multilinear GF(2) algebraic normal form

    P=sum_j [z t_{j,1}+sum_{k=1}^{(m-2)/2}t_{j,2k}t_{j,2k+1}
                          +x_j(1+z) product_{l=1}^{m-1}(1+t_{j,l})].

Define its interaction graph by connecting all variables in every nonzero monomial. A sign factors over disjoint physical variable sets iff its ANF splits as a sum of polynomials on those sets. Uniqueness of the multilinear ANF proves the forward implication; the reverse follows by multiplying the corresponding signs. Consequently the graph components give the finest exact independent sign-factor partition. This applies to arbitrary Boolean factors, not only quadratic factors.

At the root, each monomial x_j z product_l t_{j,l} is present with coefficient one; none can cancel with another module or a quadratic term. It connects every coordinate of module j to z. Therefore F's interaction graph is connected: no proper independent tensor factor can be stripped at the root.

After fixing the first j selectors, each unqueried module still connects its entire block to z. A previously fixed selector with value 1 has monomial z product_l t_{j,l}; because m>=4 its degree exceeds that of the original quadratic terms, so its entire data block remains connected to z. A previously fixed selector with value 0 leaves z t_{j,1} connected to z and separates its m-2 other data bits into independent quadratic pairs. These and only these are removable components. The exclusion m=2 is deliberate: that endpoint has an additional cancellation making a flipped branch separable, and is outside this all-parameter charge formula.

The checker reconstructs the ANF from the full truth table at every reached node; it does not infer connectedness from the constructor's syntax.

### 3. The actual selector-first bill after optimal factor removal

At a selector x_j, the half-difference is a signed indicator of {z=0,t_j=0} multiplied by the other modules restricted to z=0. Its squared norm is delta. The indicator itself contributes I(D)=m delta/2. Every remaining independent z=0 spectator adds delta times its influence. After j previous selectors are fixed (j=0,...,a-1), earlier modules have average z=0 influence J_0 and later unqueried modules have influence L_0. Hence summing the ACTUAL probability-weighted raw charges yields

    T_raw=sum_v pi_v 2I(D_v)
         =a m delta+delta a(a-1)(J_0+L_0)
         =a m delta+delta a(a-1)[m-2+(4m-2)delta].

Now remove all disjoint sign factors not containing the queried coordinate, recomputing the finest partition at each node. By Section 2 only the quadratic pairs in earlier modules with selector value 0 can reduce the bill. Each such module's removed influence is (m-2)/2; its contribution to I(D) is delta(m-2)/2. There are on average j/2 such earlier modules. Therefore

    T_factor=T_raw-delta a(a-1)(m-2)/4
            =a m delta+delta a(a-1)[(3/4)(m-2)+(4m-2)delta].

This is the minimum derivative bill achievable by exact disjoint factor removal for this rule. Removing more would remove a variable in the queried component and would not be a permitted independent spectator operation. Equivalent factorizations and signs do not change retained-coordinate L2 energies.

At every fixed even m>=4, V is fixed and d_z is bounded, so

    T_factor/I(F) ~ delta[(3/4)(m-2)+(4m-2)delta] a/V -> infinity.

This is a connected-family obstruction to the factor-only repair, not the already known disjoint tensor obstruction.

### 4. The exact-B bad-node filter does not rescue that rule

The claimed divergence must survive the lead's localization; a scalar h2 upper bound would not suffice. Fix any selector-first descendant and any remaining selector. At z=0 the other restricted modules form one Boolean sign H_0; at z=1 they form another sign H_1. In data Fourier rows where the queried module's t_{j,1} is absent, the z=1 Fourier coefficient is zero. The module's m-2 private quadratic core has coefficients e*2u, where u=2^{-m/2}; the point indicator has coefficient 2delta. In each such row, for either Fourier z-bit, the parent selector-absent and selector-present coefficients are

    (e u-delta) hat(H_0)(R),    delta hat(H_0)(R).

Let q_e=(e u-delta)^2+delta^2. Since 1-2u+2u^2>=1/2, q_e>=delta/2. The conditional binary entropy in this row is at least

    hat(H_0)(R)^2 delta^2 log2(q_e/delta^2)
                      >=hat(H_0)(R)^2 delta^2 (m-1).

There are 2^{m-2} choices of the queried private quadratic index and two Fourier z-bits. Sum R using ||H_0||_2^2=1. Discarding the other nonnegative entropy rows gives, at EVERY selector node,

    B_v >= [delta/2](m-1),  Inf_v=delta,
    B_v/Inf_v >= (m-1)/2.

These quantities are unchanged by removing an independent factor. Given any fixed finite nonnegative K, choose even m>=4 with (m-1)/2>K. Every selector of the chosen rule is genuinely bad, so T_factor is exactly its bad-node charge and its ratio diverges as a grows. For K=4, m=10 already works. An exact formula-only certificate at (a,m)=(8192,10), which does NOT construct its truth table, proves T_factor/I>10 using d_z<=1; see out/GROWING_WITNESS.json. The all-dimensional proof above supplies the Boolean family and factorization, rather than extrapolating from the finite tests.

The refuted statement is specifically: stripping exact independent sign factors suffices to bound the bad-node 2I(D) sum of this selector-first stopping rule by an absolute multiple of I. No universal adaptive-tree theorem is refuted.

### 5. Shared-bit-first: the separator changes the payment

Reveal z first and stop. Since a one-bit conditional entropy is at most one,

    B_z<=1<4 d_z,

using d_z>=3/8. Thus this tree has ZERO internal nodes with B_v>4 Inf_v, and its bad-node derivative bill is zero. This statement concerns its one queried coordinate; it does not declare its leaves free.

At z=0 the product of private psi_j modules has a complete uniform-mask code of am bits. Since L_0>=(m-2)/2>=m/4 for m>=4,

    H(F|z=0)<=am<=4 I(F|z=0).

At z=1 the private t_{j,1} bits form a fixed character, while the m-2 private quadratic coordinates per module have a flat spectrum. Therefore

    H(F|z=1)=a(m-2)<=2 I(F|z=1).

The exact entropy split Delta_z=B_z+JS_z, the reviewed JS bound JS_z<=(2/ln2)d_z, and B_z<=1<=(8/3)d_z give the terminal-inclusive estimate

    H(F)<= (8/3+2/ln2)d_z +4 average_b I(F|z=b)
         <= (8/3+2/ln2) I(F).

The queried influence d_z and the average terminal influence are disjoint terms of the physical influence identity from Section 1. This pays one separator step and both leaves without reusing a data bank. It does not continue the tree by silently charging all leaf variables to a bank already spent.

The contrast is structural: root connectedness did not force large cumulative charges. The coordinate whose revelation exposes independent components was available and had a fixed positive influence. Selecting that coordinate, rather than relying only on factor removal at the initial node, is what repairs this family.

### 6. A complete normalized reference for the SAME paid separator

Let R be a subset of all am private coordinates. Define Q_0(R)=2^{-am}, the complete z=0 uniform-mask reference. Define Q_1(R)=2^{-a(m-2)} on the known z=1 flat support: every x_j is absent, every t_{j,1} is present, and each other private data coordinate is free; Q_1 is zero elsewhere. Both references have total mass one and include their complete terminal costs.

Fix the root reference across all sampled Fourier sets by

    Q(A,R)=[Q_0(R)+Q_1(R)]/4, A in {0,1},

where A records the Fourier z-bit. This is a literal normalized law: choose a physical branch label fairly, draw its terminal reference, then choose the Fourier z-bit fairly, finally erase the latent branch label. Its normalization is exactly one. Both label choices and every terminal mask are included; no known spectrum is provided as uncharged side information. Q_0 makes the law positive on every Fourier set, including the empty set.

On Q_1's support Q_1/Q_0=4^a. The true parent spectral marginal mass on that support is

    alpha=[1+delta^a]/2.

Indeed, the z=1 child puts all its mass there. In one z=0 psi_j factor, the event x_j absent and t_{j,1} present has mass delta: there are 2^{m-2} coefficients equal to -2delta, and their squared mass is delta. The private z=0 factors are independent, giving delta^a. The exact physical-child/spectral-marginal identity gives the displayed alpha after averaging the two children.

Thus the full expected reference cost has the closed form

    CE_Q=am+2-alpha log2(1+4^a)
        <=a(m-1)+2.

No posterior term is omitted: the log2(1+4^a) saving comes from summing the two complete reference probabilities, not counting extra descriptions of one generator run. Let x=a(m-1)>=3. Then I(F)>=x/2+3/8 and

    a(m-1)+2=x+2 <=(8/3)(x/2+3/8) <=(8/3)I(F).

Consequently H(F)<=CE_Q<=(8/3)I(F). This stronger complete-reference estimate closes C020's coding control for this particular shared-bit obstruction while simultaneously exhibiting the correct separator. It is not a universal claim that arbitrary overlapping leaves have these terminal reference laws.

### 7. First unsupported universal line

The new obstruction proves that factor removal alone does not make a fixed rule's boundary cost nonreusing, even on a physically connected family. The new paid rule proves only a one-bit-separator case with an explicit leaf reference and d_z bounded below. The first unsupported extension is: every Boolean function admits an adaptive sequence of physical separators or queries with both affordable exact-B boundary cost and complete terminal reference cost, all charged once to its original influence. Arbitrary irreducible functions may have no such positive-influence separator, and a separator itself may have low influence and rare-log debt. Neither connectedness nor a fixed small separator cardinality provides that missing selection/payment theorem.

## executed validation with domain, arithmetic, commands and outputs

Saved FROZEN_SPEC.json before the job. Executed from the A016 folder:

    python -X utf8 runs/20261013T214508Z-account05-A016-addressing-benchmark/code/check_shared_spine.py

Result: 19,600 exact assertions, zero failures, measured script runtime 2.0580824 seconds. Domain: (a,m)=(1,4),(2,4),(3,4),(1,6),(2,6),(1,10), dimensions 5,9,13,7,13,11. Every full truth table is transformed by integer FWHT; physical edge counts independently verify every coordinate's spectral influence. Every selector-first node, including every prior selector assignment, is reconstructed physically. A separate GF(2) Mobius transform reconstructs its ANF and finest tensor factorization. Actual derivatives are transformed, their squared norms are checked, and retained-coordinate energies verify the exact minimum-factor charge formula. Conditional spectral erasures are enclosed rigorously and certify the displayed uniform lower bound, including a genuine K=4 bad node at m=10.

The z-first children, terminal entropies and influence telescope are independently verified. The root reference is enumerated over all Fourier sets: sum Q=1 exactly; its true support mass is exactly alpha; physical-child Parseval holds in every data row; and its complete cost matches the closed form by exact rational coefficients of one logarithm. H<=CE and CE/I<=8/3 are certified with rational intervals. All entropy logs use a 36-term rational atanh series with proved positive geometric remainder, reduced to [1,2), followed by outward rounding to 2^-100. Displayed decimals are presentation only; no floating sign is accepted. Formula-only large-a rational witness bounds are in a separate receipt and are not labeled exhaustive high-dimensional checks.

Frozen memory estimate: 50 MB; no job was expected to exceed 300 MB, so the memory preflight was not required. Peak resident memory was not instrumented. No GPU, randomization, automatic dimension escalation or background job was used. Every completed case was saved immediately to out/PARTIAL.json; final results are in out/CHECK.json.

| a | m | I (exact) | factor-minimized selector bill/I | complete root CE/I (display) |
|---:|---:|---:|---:|---:|
| 1 | 4 | 37/16 | 4/37 | 2.06117868 |
| 2 | 4 | 511/128 | 102/511 | 1.99095991 |
| 3 | 4 | 5889/1024 | 560/1963 | 1.91064610 |
| 1 | 6 | 199/64 | 6/199 | 2.19365496 |
| 2 | 6 | 11647/2048 | 598/11647 | 2.10229383 |
| 1 | 10 | 5131/1024 | 10/5131 | 2.16293351 |

The selector bill column includes all selected nodes. Its interpretation as the K=4 bad-node bill is guaranteed by the analytic lower bound at m=10; no such interpretation is asserted merely from the m=4,6 formula checks. Exact costs and node-by-node erasure intervals are in CHECK.json.

## proof dependencies and changed downstream conclusions

This is a targeted repair/refutation of A016 stage 2's suggested factor-aware mechanism, not a new broad universal theorem candidate. The earlier claim is not retracted: its exact factor-removal repair was explicitly for disjoint tensor blocks. The new shared-bit graph shows why extending that repair to connected families would fail. A018's reconstructed JS normalization is used only for the separate terminal-inclusive physical-tree estimate; the stronger normalized reference proof and the boundary obstruction are self-contained.

Consumers B04 lead/A018/A020/A027 should refine their universal target from 'strip tensor factors' to 'select and pay a separator that exposes components, or provide a genuinely joint owned reserve.' A095/A008/A097 can use the explicit normalized leaf-mixture law and alpha calculation as a fixture for complete reference transfer. No stream claim registry or another agent's files were modified. Review cap discipline is respected by testing/refining the live mechanism instead of opening an unrelated broad candidate.

## one next mathematical action and independent reviewer

A018/A090/A091 should reconstruct the all-descendant factor partition and exact T_factor formula independently; A095/A008 can independently reconstruct the complete Q normalization and terminal cost. Next mathematical action: test the separator-first candidate on the smallest extension whose two shared coordinates cannot be resolved by a uniformly positive-influence first pivot, using one common induced reference and an exact owned physical budget. This is a falsifier/repair test of the selection mechanism, not a new census or a stand-alone class hunt. Keep the remaining child reference cost explicit after the first pivot; query cardinality alone is not a payment certificate.

## actual persistence receipts or precise save blocker

Saved REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, FROZEN_SPEC.json, code/check_shared_spine.py and code/persist.py, exact outputs, growing formula witness, source hashes and persistence receipts inside the assigned run. STATUS.md, WORKLOG.md and LEARNED.md are current. out/PERSISTENCE.json checks the protocol field sets, equal packet delta, statement hash, final Universal bridge paragraph and artifact sizes/hashes. Supervisor copy, independent review and mirror verification remain pending and are not claimed. No git, mail, brain write, external publication, shared-tree mutation or other-agent-folder write occurred.

## Universal bridge

This stage moves the live C019 boundary target by disproving the factor-only repair on a connected all-dimensional family: even after optimal exact spectator removal and exact-B localization, the selector-first bill is a m delta+delta a(a-1)[3(m-2)/4+(4m-2)delta], whereas total influence is O(a). It simultaneously supplies a paid physical separator with zero K=4 bad-node bill and explicit terminal influence, plus a normalized C020 whole-set reference of cost <=8I/3. What remains is universal adaptive separator selection and payment when no uniformly influential separator is available. NEXT tests that precise obstruction with two shared coordinates and one retained reference/budget; it advances the universal mechanism rather than repeating bent-code calibration or proving another disconnected class bound.
