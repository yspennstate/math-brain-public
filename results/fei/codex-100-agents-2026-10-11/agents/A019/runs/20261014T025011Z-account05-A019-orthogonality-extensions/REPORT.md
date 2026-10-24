# A019 stage 4: arbitrary-core edits and the exact internal-pivotal correction

Full FEI remains OPEN. The half-private derivative account used by A016 extends from bent point edits to point edits of every Boolean core, and to every edit region with no internal core pivotal edges. A two-bit Boolean witness rules out removing that condition. A018's new actual Boolean entropy-excess certificate is consumed and independently verified at its eleven-bit scope; the old optional paired-row inequality is retired.

## exact target, quantifiers, hypotheses and units

Private and shared physical bits are independent and uniform; outputs are signs. Entropy and complete reference cross-entropy (CE) are in bits. For a Boolean core g on an arbitrary finite private cube and any edit region E, set a=g, b=g(-1)^1_E, D=(a-b)/2=g1_E, J=(I(a)+I(b))/2, and kappa=I(D), with real Dirichlet energy for D. Define P_in and P_out as the contributions to I(g) of directed pivotal edges with both endpoints in E and both endpoints outside E, respectively, using the same normalization as total influence. Then exactly

2 kappa - J = P_in - P_out.

Consequently kappa<=J/2 if and only if P_in<=P_out. This includes arbitrary cores and independent edit sets (no two vertices of E are adjacent), not only flat-spectrum cores. For a point edit in dimension m, delta=2^-m, kappa=m delta/2 and J>=m delta. There is no neighboring-disagreement lower bound.

For any number of disjoint arbitrary private cores g_j, two shared bits z,w, and arbitrary Boolean shared masks A_j(z,w), form F=product_j g_j(y_j)(-1)^(A_j(z,w)1_Ej(y_j)). Assume each E_j has density<=1/2 and P_in,j<=P_out,j. With J=I_private(F), d=Inf_z(F)+Inf_w(F), and E_zw the squared spectral mass containing both shared bits, the z-then-w stopping prefix has exact derivative bill T=T_private+2E_zw, T_private<=2J, and T<=2J+d<=2I(F). Filtering any exact bad-node threshold decreases T. All terminal reference costs are retained: if four supplied normalized complete terminal references have average cost cbar, a normalized root reference exists with CE<=cbar+T+(3/ln2)d. In particular cbar<=C J implies CE<=max(C+2,1+3/ln2)I(F). This is a conditional certificate transfer, not an assertion that arbitrary cores have such references.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json completely, revision2026-10-11-execution-v2; BOARD.md snapshot2026-10-14 02:43 UTC; B04 STREAM_NOTES.md v2; own STATUS.md, LEARNED.md, and previous stage REPORT.md and checker/finalizer. Required campaign and paper context was read in earlier stages; no new paper or external source is used as a theorem dependency here.

New sources read: A016 run20261014T011255Z-account05-A016-addressing-benchmark REPORT.md and CLAIMS.json, especially derivation sections3-4 and7; A018 run20261014T022025Z-account05-A018-shared-data-collision-law REPORT.md, especially sections1-4 and6. The latter supplies the actual Boolean refutation of the prior paired-row proposal. A019-FOLDED-SEPARATOR-OWNER@1 supplies the product derivative identity, rederived below. A016 independently reconstructed that previous ownership claim in its section2; its own new two-pivot theorem has A018 independent acceptance. The board records A020's scope-limited independent review of A019 as well. No assumption of universal paired-row subadditivity survives in this stage. Source hashes are saved in out/SOURCE_RECEIPTS.json. No mutable shared registry was edited.

The bent-splice falsifier remains mandatory: common branch Fourier magnitudes cannot be assumed for point surgery on a bent core. The present edge proof allows arbitrary magnitudes and therefore does not invoke the orthogonality corollary. It imports A016's actual bent point-splice family as a contained control, rather than treating it as an excluded normalized-array example.

## complete derivation or exact first unsupported line

### 1. Edge partition proves the exact correction

For an oriented private edge (x,x^i), a real function h contributes (h(x)-h(x^i))^2/(4*2^m) to I(h). Partition those edges into inside E, outside E, and crossing its boundary. Inside E, both a and b have the same pivotal status as g, while D=g; thus their contributions to J and kappa agree. Outside E, J receives the contribution of g and D is zero. Across the boundary, one child has the original two signs and the other reverses one endpoint. Exactly one child is pivotal, so the contribution to J is 1/(2*2^m), while D has one sign and one zero, contributing 1/(4*2^m). Hence crossing terms cancel in 2kappa-J, inside terms contribute P_in, and outside terms contribute -P_out. This proves the identity and its iff condition with no Fourier regularity assumption.

An independent edit set has P_in=0, so every core satisfies half-private. The stronger structural condition is only absence of internal CORE pivotal edges: adjacent vertices inside E are allowed if g agrees along them. For a point edit, let r be the number of original pivotal directions incident to that point. Each original edge contributes 2delta to I(g), so I(g)>=2r delta. Reversing the point changes private influence by 2delta(m-2r), giving J=I(g)+delta(m-2r)>=m delta. The signed point indicator has kappa=m delta/2, agreeing with the general partition formula. This closes A016's half-private arbitrary-core subquestion without requiring a new class census.

### 2. Sharp obstruction to arbitrary edit regions

On two private bits, indexed x1 as the low bit, take g=[1,1,-1,1] and E={0,2}, i.e. x1=0. Then b=[-1,1,1,1], I(g)=I(b)=1, J=1, and D=[1,0,-1,0] has kappa=3/4. Its internal pivotal contribution is1/2 and external pivotal contribution is0; thus 2kappa-J=1/2. The child disagreement is1/2 and child correlation is0, so separator-character folding does not repair this failure. The false statement 'all arbitrary certified-core edits have kappa<=J/2' is refuted already on an actual two-bit core. Nothing here is an FEI counterexample.

### 3. Product ownership, including the signed term

Fix one shared edge, holding the other shared bit constant, and let a_j,b_j be its module endpoint functions. Write J_j,edge=(I(a_j)+I(b_j))/2, kappa_j=I((a_j-b_j)/2), q_j=E[a_j b_j], Q_-j=product_(h!=j)q_h. The edge changes either no private region or E_j. In the changed case q_j=1-2density(E_j)>=0; in the unchanged case q_j=1. The hypotheses ensure kappa_j<=J_j,edge/2 in both cases.

A private Fourier cross-energy expansion gives C_j=sum_U |U| ahat_j(U)bhat_j(U), kappa_j=(J_j,edge-C_j)/2, and

I(D_product)=sum_j t_j,  t_j=(1-Q_-j)J_j,edge/2+Q_-j kappa_j.

Indeed the two product endpoint energies are additive over disjoint blocks, while their cross-energy is sum_j C_j Q_-j. This rederives the prior ownership formula without an entropy claim. Since Q_-j is in[0,1], t_j<=J_j,edge/2. More precisely define R_j,edge=P_in,j,edge-P_out,j,edge for the effective edit region (empty when unchanged). Then

t_j=J_j,edge/2+Q_-j R_j,edge/2.

Thus the term controlling an arbitrary-region extension is signed and exactly localized to an owned private block. It is not the total private influence charged again.

Average the two possible edges for each shared direction and add both directions. Let u_j=sum_direction E_other t_j,edge. The average J_j,edge in either direction is the same physical private J_j. Therefore u_j<=J_j, with one total account per module, and

T_private=2sum_j u_j = 2J+W,
W=sum_j sum_direction E_other[Q_-j R_j,edge].

Under the structural hypothesis W<=0. Parseval proves T_private=2sum_S |S_private| |S intersect {z,w}| Fhat(S)^2. The root z derivative also charges the remaining w coordinate, exactly2E_zw. The child w derivatives have no remaining shared coordinate. Thus T=T_private+2E_zw. Since E_zw<=min(Inf_z,Inf_w), 2E_zw<=d, proving T<=2J+d. This is uniform in module count, private dimension and small disagreement. For arbitrary regions of density<=1/2, the exact formula with W remains true even when W is positive; the two-bit witness shows why dropping W is unsupported.

### 4. Complete terminal reference transfer and its limitation

Let P_b be the actual private product spectrum at shared leaf b in{0,1}^2, with supplied normalized finite-cost reference Q_b, and cost c_b. Set R=average_b P_b and Qbar=average_b Q_b. Define Q(L,U)=nu_actual(L|U) Qbar(U), where nu_actual is the parent's conditional shared Fourier law on a private row; on a zero true row choose any fixed normalized conditional. This is a finite normalized reference, with support wherever the true law is positive. Joint-to-marginal log-sum gives KL(R||Qbar)<=average_b KL(P_b||Q_b). Consequently

CE_Q(F)<=cbar+H(F)-average_b H(F_b).

Telescoping the reviewed B04 node bound on the prescribed physical tree gives the entropy difference <=T+(3/ln2)d. Both terminal CE costs and the remaining shared mixed energy are included. Inserting T<=2J+d gives the conditional rate stated above. No product terminal-reference assumption is needed: arbitrary supplied complete references for the four actual products are allowed.

For a proposed rate K, the exact signed sufficient ledger is

cbar+2J+W+2E_zw+(3/ln2)d <= K(J+d).

This formula exposes the next gap. Half-private ownership by itself does NOT show that supplied terminals leave enough rate4 slack: the term (1+3/ln2)d may require a positive unused core reserve, unlike A016's bent point-edit reserve. The first unsupported universal line is existence of complete terminal references and an admissible separator policy whose SAME remaining slack pays that signed inequality through repeated prefixes. Repeating the conditional C+2 overhead at every level is not a universal proof. This stage does not claim the rate4 bent-spine theorem for arbitrary cores. The new A018 point-product witness moreover forbids replacing this debt by a universal loss-only entropy price.

### 5. Source-bound independent check of the new Boolean obstruction

Independently construct the actual eleven-bit parent and both six-bit modules from the point-defect truth-table rule. Recursive Walsh transforms and rational prime-log bookkeeping reproduce

131072 ln(2)[H(parent)-2H(module)] = 491071 ln31 -231361 ln481 -27900 ln15 -262144 ln2.

Pure integer arithmetic verifies 31^491071 > 481^231361*15^27900*2^262144. Hence the positive entropy excess is independently confirmed. This review covers the finite Boolean falsifier only; it does not certify A018's entire asymptotic or reference theorem. The earlier zero-mean scalar candidate in A019 stage3 is now explicitly retired. None of the proved ownership identities depends on it.

## executed validation with domain, arithmetic, commands and outputs

All job specs were saved before execution. No planned job exceeded40MB, so the >300MB memok gate did not apply. Peak memory was not measured. Jobs were sequential; no GPU, randomization, automatic dimension escalation, background job or window was used.

From the A019 directory: `python -X utf8 runs\20261014T025011Z-account05-A019-orthogonality-extensions\code\check_edits.py --pilot` checked every core/edit-set pair in dimensions1,2:272 cases,1359 exact assertions,0.0100seconds. The full command without --pilot checked all core/edit pairs in dimensions1,2,3,256 ordered two-bit core pairs with AND/OR shared masks, and256 ordered shared-mask pairs with fixed AND/XOR private cores:66320 cases,287311 exact assertions,11.7892seconds. All actual truth tables, edge energies, independent integer Walsh energies, exact partition identities, point/independent-set cases, every per-edge ownership formula and the full two-query derivative telescope passed. There were9084 independent-edit-set core pairs. Exhaustion is evidence for the proved all-dimensional identity, not its infinite-dimensional justification. No entropy signs or floating tolerances occur in this checker.

`python -X utf8 runs\20261014T025011Z-account05-A019-orthogonality-extensions\code\review_excess.py` independently reproduced A018's finite Boolean positive-excess witness in0.9452seconds. The exact comparison integers have2432863 and2432549 bits; hashes and rational prime-log coefficients are in out/EXCESS_REVIEW.json. This small job stayed below its frozen30MB estimate; no elapsed resource-use claim beyond recorded runtime is made.

## proof dependencies and changed downstream conclusions

The edge identity, arbitrary-core half-private extension, explicit failure, signed private ownership and exact T<=2I are self-contained. The CE consequence uses B04-NODE-BOUNDARY@1, already independently reconstructed by A018, plus the fully rederived conditional reference lift. A019-FOLDED-SEPARATOR-OWNER@1 is reconstructed at its exact product-derivative scope; no optional scalar strengthening is used. A016's point-indicator hypothesis is weakened to arbitrary Boolean cores and edit regions satisfying P_in<=P_out. Its terminal bent-code reserve is NOT transferred automatically.

The new scoped claim is author-proved, independently unreviewed. A018's finite actual Boolean counterexample receives an independent reproduction with no supplied repair; its broader theorem remains outside this review's scope. B04/A016/A018/A020/A090/A091/A095/A097 should retain W and complete terminal slack, and retire the averaged paired-row proposal. Artifacts serve as handoff; no messages were sent and no other folder was modified.

## one next mathematical action and independent reviewer

Test the exact signed rateK ledger with a non-flat arbitrary supplied certified core whose activation region has internal pivotal edges: retain W, cbar and2E_zw, and determine whether unused terminal slack pays W without reuse. Use the two-bit half-private failure and A018's eleven-bit positive-excess parent as mandatory controls. A016/A018 can independently review the arbitrary-core edge partition and two-query ownership; A090/A091 can review the terminal reference insertion. This is the enabling core-slack problem, not another search for an isolated positive-disagreement class.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, code/, frozen specs, exact outputs and source receipts are saved in this run. STATUS.md has two lines; WORKLOG.md and LEARNED.md receive dated updates. code/finalize.py checks protocol key sets, statement hash, required report headings, compatibility identity, JSON syntax and20MB file limits, then saves out/PERSISTENCE_RECEIPTS.json with local hashes. Independent review of the new scoped claim, supervisor adoption, remote copying and mirror verification remain pending and are not inferred from local persistence.

## Universal bridge

This stage moves C019/C020's arbitrary-core shared-prefix payment interface by replacing the bent-core half-private hypothesis with the exact identity2kappa-J=P_in-P_out, proving a uniform two-query derivative billT<=2I for arbitrary cores edited on internally nonpivotal regions, even as neighboring disagreement tends to zero. It quantifies precisely the signed obstructionW for general regions and independently confirms the actual Boolean falsifier of the paired-row shortcut. No universal terminal-slack or recursive payment theorem is obtained: complete terminal references, internal-pivotal surplus and repeated physical-budget ownership remain unpaid in general. NEXT tests that surplus against the same unused arbitrary-core terminal slack, the shortest remaining route toward a reusable universal stopping-tree bridge rather than another bent-family bound.
