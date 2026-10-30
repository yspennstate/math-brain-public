# A016 stage11: adaptive shared-bit cleanup and a paid padding continuation

Full FEI remains OPEN. This stage independently reconstructs A019's complete averaged ghost-prefix obstruction and proves a different scoped continuation: after every adaptive cleanup-complete source history in a product of at least five overlapping-bit blocks, the SAME original rate4 reserve exceeds5/8. Every subsequent padding-only adaptive policy retains expected reserve>5/16; arbitrary mixed policies with at most nine further nonzero source queries per path retain>1/32, with optional zero-influence cleanup. Individual mixed terminals can still be arbitrarily negative. New theorem awaits independent review.

## exact target, quantifiers, hypotheses and units

Bits are independent uniform0/1, chi_b=(-1)^b, and all entropy/cost units are bits. Put g3=-1 only at000, E(a,b,c,d,e)=g3(a,b,c)g3(a,d,e), and G=product of j disjoint E blocks. The SAME physical a occurs in both tests inside each E. Fix j>=5,k>=5,rho=2^-k,mu=(5/8)^j, A=point_k(v)(1-G)/2,p=rho(1-mu)/2. Let h=chi_u off A and chi_q on A; F=1 at fresh gate0 and h*w at gate1, with w=[-1,1,1,1] on two fresh bits. The ONE supplied original reference is Q_h=(P_h+delta_q)/2 and Q_F(e,T)=[Q_h(Tcore)P_w(Tmask)+delta_empty(T)]/4 at BOTH gate frequencies. All descendants receive literal frequency marginals. Original debit U=Lq+Econv is defined below and is never renewed.

First query q. Allow ANY finite adaptive source-coordinate query policy, with arbitrary interleaving between E blocks and either q sign. At each admitted source frontier erase every remaining coordinate on which its restricted E block is physically constant in that coordinate; retain all cleanup outcomes. Padding,u,mask and gate remain unqueried in this first phase. Every such cleaned terminal has W=4I-CE-U>5/8. From any such terminal allow ANY finite padding-only adaptive policy and any zero-influence cleanup, retaining all outcomes. Its conditional expected W is>5/16. Consequently the entire two-phase physical policy has expected W>5/16. More generally any finite continuation with at most r further nonzero source queries per path, arbitrarily interleaved with padding and zero-influence cleanup, retains expected W>5/8-(2k+r)rho. In particular r1 retains>9/32 and r9 retains>1/32. This does not fund unbounded mixed query counts or certify individual mixed terminals.

Separately review unchanged A019-AVERAGED-ADAPTIVE-GHOST-PREFIX-OBSTRUCTION@1, statement hash e43587675e926a4cf1f30be1edd0c8582c5c0332bcdf96cb145014d7125a296e. Its one-balanced hierarchy is DIFFERENT from the balanced h/Q_h above; numerical owner allowances are not transplanted.

## sources actually read, revisions and theorem locators

Read current BOARD snapshot2026-10-23 13:48UTC, full B04 STREAM_NOTES v2, own STATUS, machine AGENTS relevant rules and full execution protocol2026-10-11-execution-v2. Earlier packet campaign/paper readings are carried forward; no new external paper theorem is assumed. Read A019 run20261023T125104Z REPORT and claim statement/hypotheses/hash, including its sharp full-cost coefficient and explicit all-k source eligibility. Read A020 run20261023T132008Z report/claims via its actual latest directory recorded in source receipts; its predetermined-set proof and adaptive gap motivate the new block certificate. Exact source directory names and byte hashes in out/SOURCE_RECEIPTS.json govern if this descriptive locator differs. Read own stage10 report/helper. A020's unchanged independent acceptance of own stage10 mixed obstruction is recorded; no rewrite of old immutable files.

The current-session wake completed; its entire output was read. Brain self-care is degraded/unverified: owner-model100.3h,state84.9h,dream35.6h stale, with recurrence-monitor status unresolved. These notes affect personal-context freshness and are not mathematical premises. Owner deadline2026-10-23 14:49UTC supersedes the older protocol endpoint. No external novelty or priority claim is made.

## complete derivation or exact first unsupported line

1. Finite interacting-block contract, with portable exact certificates. Direct32-point characters give mean(E)=5/8 and influences(3/8,1/4,1/4,1/4,1/4), total11/8. Treating its two g3 factors as independent would give incorrect physical influence. Enumerate EVERY one of the3^5=243 partial physical assignments. Compute its restricted truth table, find essential coordinates by literal edges, erase all other coordinates, and project ORIGINAL P_E to the remaining frequency coordinates. Call the resulting actual law P_i, reference R_i, mean nu_i, and actual influence I_i. Every case satisfies

CE(P_i,R_i)<=4I_i.

This assertion is certified by exact integers, not by a floating sign. If N is the restricted truth-table length, P_i(t)=w_t^2/N^2. Writing R_i(t)=a_t/b_t and D=N^2, the certificate is

2^(4I_i D) product_t a_t^(P_i(t)D) >= product_t b_t^(P_i(t)D).

All exponents are integers; all positive true atoms have positive R_i. Each saved row includes the complete P/R vectors, assignment, essential coordinates, truth table and both integers. Constant cleaned blocks have R_i=delta_empty, CE=I=0. There are45 distinct essential-coordinate/truth states. A separate direct-character verifier reconstructs the original and restricted spectra, physical edges, projection and both certificate integers without importing the Walsh/log helper.

For a physical adaptive leaf, remaining bits are a cylinder with independent uniform coordinates. Independence between genuinely disjoint E blocks therefore gives actual P_G=product_i P_i and inherited R=product_i R_i, with any accumulated constant phase included in nu. Code additivity yields CE(P_G,R)<=4I_G for ANY adaptive interleaving and ANY j. No averaging over overlapping partial assignments is used. In particular this is a pointwise source contract after mandatory cleanup, not A020's fixed-set mean substituted at a random set.

2. New vacuum argument. The old tensor inequality R(empty)>=nu^2 FAILS for some cleaned E states; saved exact negative differences are counterexamples to that intermediate line. One independently reconstructed witness has assignment [-1, -1, -1, -1, 1], R(empty)=7/16, actual mean=3/4, and difference=-1/8. Here -1 in the assignment denotes unqueried, not a bit value. We do not use it. Instead j>=5 gives mu<=3125/32768<1/8. Put a=rho(1-nu)/2, and let L replicate a seed measure equally over u and all padding frequencies, multiplying its mass by2^(k+1). Exact true and inherited core laws at a cleaned q terminal are

Pc=(1-2a)delta_u+(rho^2/4)L[PG+(1-2nu)delta_empty],
Qc=(1-2p)delta_u/2+delta_empty/2+(rho^2/8)L[R+(1-2mu)delta_empty].

Coincident rows are added; these are normalized measures, not renewed slices. For nu<=1/2, replace PG by R in Pc to get a normalized nonnegative M. The combined vacuum condition for Qc>=M/8 is

Dvac=3R(empty)+3-8mu+2nu >=1-8mu>=971/4096>0.

The principal atom also dominates since(1-2p)/2>31/64>1/8. This argument keeps negative phases and needs NO comparison between R(empty) and nu^2. Latent principal/rare coding, followed by the seed/point mixture, gives

CE(Pc,Qc)<=3+h2(2a)+2a(k+2)+(rho/2)CE(PG,R).

For detail, the rare normalized mixture is[PG+(1-2nu)delta]/[2(1-nu)], with seed mixing weight1/[2(1-nu)] in[0,1]. Its label cost is at most1; its PG cross-entropy coefficient after multiplying the rare mass2a is rho/2. Qc>=M/8 costs3 additional bits. All labels and the full reference remain present.

3. High-mean repair without the tensor exception list. If nu>1/2, the rare true vector PG+(1-2nu)delta remains nonnegative and is bounded above by PG. The principal reference atom is>1/4, and every rare row has Qc>=rho^2 R/8. Therefore, directly by linearity of CE,

CE(Pc,Qc)<=2+2a(2k+3)+(rho/2)CE(PG,R).

Here the constant row code length is bounded by2, the true rare mass is2a, and its residual seed log cost is bounded by the PG cost because log(1/R)>=0. Support is guaranteed by the block certificates. This bypasses any unsupported assertion R=PG in high-mean interacting states.

4. Complete outer code, old debit, and physical reserve. The original full reference is uniform in gate frequency. Actual gate interference remains in the true law, whose data marginal is(Pc P_w+delta_empty)/2. Full latent-mixture coding gives CE_F<=CE_core/2+3. Exact physical edges give, for either q sign sigma,

4I_F=6+2(k-1)a+rho I_G-sigma*a.

The single original debit is

Lq=log((9+p^2)/8)/2+(p^2/8)log((9+p^2)/(1+p^2)),
Econv=(1+(p/2)^2)[1-h2((1+p/2)^2/(2(1+(p/2)^2)))]/2.

KL<=chi-square/ln2 and ln2>1/2 imply0<=Econv<=p^2; Lq<1/2+p^2/2, so0<=U<5/8. This is a bound on the existing debit, not a fresh booking. In the low-mean case,

4I-CE_F >=3/2+(k-5)a-h2(2a)/2+rho[I_G-CE(PG,R)/4]>5/4,

because a<=rho<=1/32 and h2(1/16)<1/2. Hence W>5/8. In the high-mean case a<rho/4<=1/128, so

4I-CE_F>=2-6a+rho[I_G-CE(PG,R)/4]>125/64,

and W>85/64, which is stronger. The entropy signs have exact integer certificates15^15>2^56 and31^31>2^152. No independent factors are assumed within E.

The original root is actually eligible. Using the original block contract H(P_G)<=4I(G), the complete root code c/2+3 with c<=H(P_h)+1 and the principal/rare entropy bound give

4I_root-CE_root>=5/2+(k-2)p-h2(2p)/2+rho[I(G)-H(P_G)/4]>19/8.

Here p<=1/64 and h2(1/32)<1/4. Thus no ineligible initial source is silently supplied.

5. ANY subsequent padding policy is paid in expectation. Fix an arbitrary cleaned source history. For a query, literal frequency marginalization gives CE_parent=average CE_child+L_i with L_i=sum P(e,T)log(Qmarg(T)/Q(e,T))>=0; physical edges give I_parent=Inf_i+average I_child. The SAME original U consequently obeys

E W_final=W_start-4Pi+sum_v reach(v)L_v.

Each initial padding coordinate has Inf_i=a/2 in F. For a policy querying only padding, the nodes at which a particular coordinate is first queried correspond to disjoint cylinders in its other bits. Their weighted pivotal-edge measure is at most the original Inf_i. Thus4Pi<=2ka<=2k*rho<=5/16 for every k>=5. Optional queries of physically irrelevant coordinates cost zero influence and have nonnegative CE release. All physical outcomes are retained. Therefore

E[W_final | cleaned source history]>5/8-5/16=5/16.

This proves every finite padding policy, including adaptive stopping, not merely the complete endpoint checked numerically. Both q signs and every source history also average to the same strict bound. Already committed padding influence is retired with a MINUS sign exactly once. An essential active leaf can have negative W; no pointwise mixed eligibility follows. Returning to a new nonzero-influence source query after padding is outside the theorem.

5b. First source query and a genuinely mixed finite-budget continuation. Keep the same admitted source history and original padding-point event V. At ANY later cylinder with remaining source bits, u/mask/gate unqueried, let rho_v=Pr(V | history). The queried source edge changes the activation iff the original padding point holds and G flips; the independent u disagrees with the fixed q sign with probability1/2 and the gate is open with probability1/2. Thus direct physical edges give4Inf_source=rho_v*Inf_source(G_restricted)<=rho_v. This holds after any padding/source interleaving; physically shared source bits are counted once. For a fixed query ordinal ell, nodes where the ell-th further NONZERO-influence source query occurs form a prefix-free collection of physical cylinders. Thus sum_v reach(v)rho_v=sum_v Pr(V intersect cylinder_v)<=Pr(V)=rho. No optional-stopping limit or independence of selected coordinates is assumed. Policies that stop earlier contribute zero. With at most r such source queries per path their total original4-influence retirement is<=r*rho. Zero-influence cleanup contributes zero. The original padding bound still holds because the first-query nodes for each padding coordinate are disjoint pivotal-edge cylinders even when source queries intervene. Consequently total4Pi<=2ka+r*rho<=(2k+r)rho and the SAME signed CE-release identity yields E W_final>5/8-(2k+r)rho. Since(2k+9)2^-k<=19/32 for k>=5, r9 retains>1/32; r1 retains>9/32. The all-k monotonicity follows from[2(k+1)+r]/2<2k+r for k>=5,r>=0. This pays the previously saved ONE-source-query NEXT and nine such genuinely interacting queries, but not an unbounded query occupation. No extra original owner is minted. Direct actual-F edges on all45 cleaned E states, both phases/q signs and zero/one remaining padding bit check these caps in360 profiles with exact Fractions.

6. Independent reconstruction of A019's unchanged averaged ghost obstruction. In its one-balanced hierarchy, short-circuiting a g3 seed without cleaning leaves four physical outcomes with probabilities1/2,1/4,1/8,1/8 and original ghost-empty masses5/8,3/4,1,1. Consequently the expected ghost log debt is

lambda=log(8/5)/2+log(4/3)/4=2-log(75)/4>3/8,

with strict integer certificate75^2<2^13. The nonempty live-seed sector has true full atoms rho^2/1024, reference atoms rho^2*r/2048, and global mass7rho/128 after retaining q0. Its EXACT global CE is(7rho/128)[2k+11+(m-1)lambda]. Its exact ghost-cleanup contribution is D=(7rho/128)(m-1)lambda, and every other cleanup release is nonnegative. Literal fresh truth tables and original marginals reconstruct this without importing A019's checker.

Actual edges give global4I=6+3rho/8+(2k-3)p/2<=6+(14k-15)rho/16. Thus, for ANY U>=0, the original whole-frontier W is<6+(14k-15)rho/16-21rho(m-1)/1024. At m=2^(k+9)+1,k>=8, this is<-4; faster m=2^(2k+1)+1 tends to minus infinity while disagreement p/2 tends to0. Initial eligibility also reconstructs: H0=4-9log3/8 in(2,3), H(h1)=rho*m*H0/2+rH with |rH|<2+(2k+7/2)rho<3; original c1-H(h1) in[0,1] gives |rc|<4 and B=rho*m*(3-H0)/8+7/4+(k-1)p-rc/4>3/4. Root mixture KL<=1/2 and selector entropy excess Delta<=15p/4 yield Wroot-B>=3/4-11p/8>5/8. For the Delta bound, f(t)=eta((1-t)^2)<=3t, eta(p^2)<=p at p<=1/512, and the other terms in Delta=f(p/2)-f(p)/2+eta(p^2)/4+2p-p^2/2 have the displayed signs.

For m>=4, outside the active sector the original vacuum gives full nonempty-data reference atoms>=rho^2/512; the empty-data pair costs at most2 and q0 costs<7/2. Hence0<=C_frontier-D<(7rho/128)(2k+11)+k+8. True entropy is at most k+7, so the full KL has the same exact linear ghost coefficient. Original influence retirement is3rho(m-1)/8 at global reach and is not a new bank. Verdict HOLDS for the unchanged full stated claim, without a material repair. This does not refute A020 cleanup or the new two-phase theorem.

First unsupported universal line: fund UNBOUNDED nonzero-influence source-query occupation in mixed padding histories, or source overlaps across the independent E-block boundary, from the SAME diminished expected account with old U and complete terminal costs retained. The first nine additional source queries are paid; a count growing with j is not. The finite block contract and small mu supply a sufficient source; no universal initial reference supplier is proved. A019 rules out omitting cleanup, and our stage10 rules out pointwise mixed admission even with cleanup.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC and REVIEW_FROZEN_SPEC precede their searches; CONTINUATION_FROZEN_SPEC precedes continuation checks. All jobs use python -B -X utf8, Fraction/integer Walsh/physical edges, and the unchanged hash-bound A016 stage10 helper with90bit outward dyadic40term atanh logs. The block pilot passes27 assignments; full checker passes all243 assignments/45 states and portable integer certificates. The A019 review pilot passes4 physical leaves; full checker covers k1m2,k2m2,k1m3 and ALL24 q1 leaves with exact reaches, plus q0 at its true half reach. Small fixtures validate identities outside the k>=8 asymptotic theorem hypotheses; the displayed proof supplies that all-k bridge. Continuation checks use all45 block states,k5,8,32,64,both phases/both q signs, original j5 reference/U, entire padding endpoints and original influence retirement. Individual unsupported interval equality is never a proof: literal no-ghost identities prove exact zero; strict positive release signs use certified endpoints. Final jobs total94257 exact assertions, excluding pilots/superseded runs. Block3516 in0.919721s; independent integer reader2589 in0.941775s; ghost review29949 in3.101741s; continuation57174 in37.906997s; mixed physical cap1029 in0.539500s. All mathematical checks PASS. Finalizer fixes for legacy claim-container and source hash serialization are preserved as persistence diagnostics; no mathematical hypothesis changed. out/VALIDATION_SUMMARY.json and individual outputs preserve execution receipts.

The independent certificate reader uses direct characters and integer products without the Walsh/log helper. Fixed finite domains are never raised automatically. Estimated memory120MB/job, runtime guard60seconds; no >300MB job or compiler was launched, so no memok admission was required. No GPU, detached process, window, git, messages, research-brain write or other-agent edit. No formal proof-assistant result is claimed.

## proof dependencies and changed downstream conclusions

Two claim records: independent HOLDS for unchanged A019 ghost-prefix theorem; one new interacting-cleanup/two-phase continuation theorem, locally proved and exact-checked with review pending. The new theorem's proof uses its own finite block certificates, normalized original-reference identities, full latent coding and the physical once-retired-influence ledger. It does not assume A020's fixed-frontier average at an adaptive set. A020's acceptance of A016 stage10 is recorded as actual downstream review, distinct from proof premises. The old R(empty)>=nu^2 shortcut is specifically rejected here, not silently assumed or repaired in another author's source. No registered theorem is refuted and no full FEI proof/counterfamily is asserted.

## one next mathematical action and independent reviewer

A020/A019 should independently reconstruct the243-state integer contract, new vacuum argument and arbitrary-padding influence cap; A018/A094 should challenge the full owner ledger. Next mathematical action: control UNBOUNDED mixed source-query occupation using compulsory cleanup/code release from the SAME original diminished expected account. The first nine additional source queries are already paid; do not relabel the next finite count as a universal bridge. Retain all siblings and original U. Do not replace this averaged account by a false local terminal invariant or recredit queried influence.

## actual persistence receipts or precise save blocker

Four protocol files, code, frozen specs, exact outputs, raw integer certificates, independent verifier and source receipts are saved locally. Rolling STATUS is two lines; dated WORKLOG/LEARNED entries record exact scope and NEXT. out/PERSISTENCE_RECEIPTS.json checks exact schemas, canonical statement hashes, equal progress/delta, report fields and local hashes/sizes. Final save/validation status is recorded there. Independent review of the new theorem, supervisor copying, registry adoption and remote mirror verification remain pending. Brain self-care remains degraded/unverified for stale personal context. No background research work remains at finalization and no other work was stopped.

## Universal bridge

This stage advances C024 history transfer toward C019 stopping-tree payment by independently accepting the complete averaged ghost obstruction, replacing the failed tensor vacuum shortcut, and proving an actual interacting-source adaptive cleanup contract. Every cleaned source history at j>=5 retains>5/8; ANY subsequent adaptive padding policy retains expected>5/16 and ANY mixed continuation with at most nine additional nonzero source queries/path retains>1/32 with SAME original Q/U, all siblings and influence retired once. Unbounded mixed source-query occupation, cross-block physical overlap and a universal initial supplier remain open. NEXT targets unbounded occupation/cleanup payment after selected padding histories from the diminished account; this is the missing ownership operation between a valid two-phase policy and the lead's unrestricted adaptive stopping tree, rather than another benchmark entropy calculation.
