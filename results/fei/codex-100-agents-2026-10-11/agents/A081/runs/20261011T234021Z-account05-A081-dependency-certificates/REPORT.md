# exact target, quantifiers, hypotheses and units

A081, B17, stage 20261011T234021Z-account05-A081-dependency-certificates. Full FEI remains OPEN: exists a finite absolute C such that every uniform Boolean f in every finite physical dimension has H_2(f)<=C I(f). This stage updates the dependency certificate requested by B17 lead v2. It does not replace a universal payment by a finite census.

Write B_i=H(S_i|S_-i), I_i=Pr[f(X)!=f(X^i)], B=sum_i B_i and I=sum_i I_i. Entropies are bits except explicitly natural primary-source entropy. K_sel(n)=max_f min_relevant_i B_i/I_i, K_agg(n)=max_f B/I and C(n)=max_f H/I over functions with at most n relevant coordinates. These are different quantities. The lead names K_sel K_B; its note saying K_B(4) is about 2.704153 mixes it with aggregate K_agg(4). The exact lead CLAIMS.json uses the correct selectable value 2.67248898.... Ratios omit irrelevant coordinates and constant functions.

The graph now has 41 exact-version nodes and 49 byte-pinned sources, with 16 admitted nodes. All six requested B17 claim statements are imported unchanged; hypotheses, evidence states, units, exact dependency versions, and scope relations remain explicit. Six alternative full-FEI routes still require an unproved universal premise.

# sources actually read, revisions and theorem locators

Read the supervisor board dated 23:39 UTC, B17 STREAM_NOTES.md v2 dated 23:40 UTC, own STATUS and LEARNED, and reread the full execution protocol 2026-10-11-execution-v2. The lead now supplies six focused claims and says not to repeat the four-bit census, B09 number or affine4 bridge. This stage follows that direction. Source snapshots are frozen in out/source_snapshots; each keeps its original path and raw-byte SHA256 in the graph.

Read lead CLAIMS.json, its write_records.py, certlog.py and census output; source-pin census_n4.py, search_n56.py, b09_interval.py and its output. Read A082 CLAIMS.json and EXHAUSTIVENESS_LEMMA.tex, both the finite Theorem 1 and scoped affine Theorem 2; source-pin its FINITE_INEQUALITY_CERTIFICATE.json. Read B18 lead CLAIMS.json and review_verdicts: A082-FINITE-TRUE-ERASURE is HOLDS at the original finite scope. The independent review and exact author certificate are retained; no new census is run. The entire compound B17 census statement, including its separate H/I and aggregate maxima, is not newly independently accepted.

Read A093 REPORT.md, CLAIMS.json and PRIMARY_SOURCE_OVERLAP.md. A093 already independently accepted B09 v1 at core-only scope, so the old missing dependency is consumed rather than rediscovered as an open source problem. Read the original B09 report section 3, matrix (3.1), uncertainty (3.2), and scope. Its literal statement SHA256 remains 988abea63a1906de7c54826cb36bb40c443bc1f346d25715d0826d3740985695.

Primary source: [Maassen–Uffink, final 1988 article](https://www.math.ru.nl/~maassen/papers/EntrUncert.pdf), DOI [10.1103/PhysRevLett.60.1103](https://doi.org/10.1103/PhysRevLett.60.1103). Visually inspected saved page images pp.1103–1104: definition (3), overlap (5), entropy bound (6), Riesz theorem (10), and limit (11)–(13). The author PDF and page images recovered by A093 are pinned by exact bytes here. Browsed publisher metadata and the university final-version record as cross-checks. The theorem node includes finite dimension, unitary transform, normalized vector, zero atoms, and natural-to-bit conversion. No abstract alone is used to accept the theorem.

Stage-1 sources and literal statement versions remain intact; the current run contains its own snapshots and graph delta. No shared tree, previous run, other-agent folder, brain database, git repository, or external messaging channel was modified.

# complete derivation or exact first unsupported line

**Restriction identities and noncircular JS proof.** For a physical coordinate, write u_T=fhat(T), v_T=fhat(T+i), s_T=u_T^2+v_T^2. Child coefficients are u_T+v_T and u_T-v_T. Their squared-law average is s_T. The spectral entropy chain rule gives B_i=sum_T s_T h2(v_T^2/s_T), while subtracting child entropies gives Delta_i H=B_i+JS_i. Physical edge averaging gives I=I_i+avg I(children). Conditioning decreases entropy, so sum_i B_i<=H. These identities are a separate primitive node containing no JS upper bound.

For 0<=z<1 let d(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2 and r(z)=1-sqrt(1-z^2). Then d'(z)=atanh(z), r'(z)=z/sqrt(1-z^2), and

    (r'-d')'=(1-z^2)^(-3/2)-(1-z^2)^(-1)>=0.

Both derivative difference and value difference start at zero. Integrating twice gives d<=r; evenness and continuity handle negative z and endpoints. On a packet with s>0 use z=2uv/s. Its JS is s*d(z)/ln2, bounded by [s-sqrt(s^2-4u^2v^2)]/ln2=2min(u^2,v^2)/ln2. Summing proves the exact B17-JS-PACKET-SCALAR statement and JS_i<=(2/ln2)min(I_i,1-I_i). The graph does not use the old BASE-ERASURE node, which already contains this inequality, as a premise proving it; it rebuilds BASE-ERASURE from the separate primitive plus the newly reconstructed scalar lemma.

**Selectable bridge.** For a fixed n, K_sel(n) is nondecreasing in n. Every nonconstant f with at most n relevant variables has a relevant i with B_i<=K_sel(n)I_i. The JS lemma yields Delta_i H<=(K_sel(n)+2/ln2)I_i. Restricting reduces the number of relevant variables, so induction with the same constant and exact influence decomposition proves C(n)<=K_sel(n)+2/ln2. Conversely the influence-weighted average of B_i/I_i is B/I<=H/I; the minimum is no larger. Maximizing gives K_sel(n)<=K_agg(n)<=C(n). Taking suprema proves equivalent finiteness, not a finite universal constant. The exact first unpaid line is sup_n K_sel(n)<infinity (or the separate aggregate payment B<=KI).

**Zero-erasure transport.** Each packet entropy is nonnegative and vanishes precisely when u*v=0. Thus B_i=0 iff all supported pairs have at most one endpoint. Projection removing i is injective on the supported spectrum. Both children have the same squared coefficients s_T, hence H(child)=H(f), JS_i=0 and I(child)=I-I_i. For n>=2 a two-variable AND sign has H/I=2, so a maximizing nonconstant f has H>0. If relevant i had B_i=0, a child with I>0 would have strictly larger H/I in the same at-most-n domain. A child with I=0 would have H=0, contradicting H(child)=H(f)>0. Thus every relevant coordinate of a maximizer has positive erasure. This proves the literal lead statement without a finite census.

**Exact five-bit cutoff and scope.** Let g=-1 exactly at integer vertices 5,12,13. Independently constructing its 32 signs and applying integer FWHT gives the Walsh vector in out/FIVEBIT_EXACT.json. Parseval is sum W_S^2=1024. Physical edge counts independently match spectral influences: I_i=3/16 at i=1,2,4 and 1/16 at i=0,3. For each coordinate,

    1024 B_i=sum_T [(a+b)log2(a+b)-a log2 a-b log2 b],
    a=W_T^2, b=W_(T+i)^2.

Factoring these integers gives exactly the two expressions in B17-KB5-CUTOFF@1. At i=1,2,4 the ratio is q=16/3-(3/8)log2 3-(169/24)log2 13+(89/24)log2 89. At i=0,3 it is 16-(63/8)log2 3+15log2 5-(169/8)log2 13+(85/8)log2 17. Rational logarithm enclosures certify that the latter is larger and

    q in [2.695887520153100810486497, 2.695887520153100810486498],
    q-107/40 in [0.020887520153100810486497, 0.020887520153100810486498].

The four-variable constant is in [2.672488983973203053133973, 2.672488983973203053133974], strictly below 107/40. Its finite optimum premise is imported from A082 Theorem 1 plus the recorded B18 HOLDS review. Therefore K_sel(5)>K_sel(4). This is a checked lower bound, not an upper bound or exhaustive K_sel(5) computation. A082's original <=4-variable theorem and affine4/disjoint-product bridge remain intact. The witness has five relevant variables, and only their unsupported universal extension is refuted. Its aggregate B/I is [2.861152584249921501929567, 2.861152584249921501929568], further illustrating the two metrics' distinction. Output negation, translation and two irrelevant dummy bits preserve the five relevant ratios in the second fixed fixture.

**Pinned B09 application.** The primary node is: for finite unitary U and unit vector a, with c=max|U_kj|, H_nat(|a|^2)+H_nat(|Ua|^2)>=-2ln c. Divide by ln2 for bits. For a nonzero residual fiber T use q_T=sum_R fhat(R union T)^2, a_R=fhat(R union T)/sqrt(q_T) and b_z=sqrt(P_A(z))*fhat_z(T)/sqrt(q_T). Parseval makes both normalized. Product-basis evaluation gives b=U_A a, U_A=tensor_i [[sqrt(1-p_i),-sqrt(p_i)],[sqrt(p_i),sqrt(1-p_i)]], so c_A=product_i sqrt(max(p_i,1-p_i)). The two squared laws are the spectral conditional law and physical posterior Z|T. Average the primary entropy bound with weights q_T to obtain M_A+H(Z|T)>=-sum_i log2 max(p_i,1-p_i). Boolean child Parseval makes the Z marginal exactly the physical product law; hence H(Z)=sum_i h2(p_i) and J_A=H(Z)-H(Z|T)>=0. Subtracting gives exactly J_A<=M_A+Delta_A, with L_A=M_A+J_A. Empty A has the trivial identity experiment. The first unsupported universal implication is nonreused tree payment of conditional spectral costs, tax and terminal entropy, not the now-pinned uncertainty theorem. Necessity/optimality of the displayed tax and general substitution additivity are excluded.

# executed validation with domain, arithmetic, commands and outputs

Frozen spec out/FROZEN_SPEC.json precedes the fixed arithmetic checks: exactly one named five-bit table plus one seven-coordinate translation/negation/dummy fixture; no symmetry reduction, no dimension escalation, no census, no float screening. Forty exact mathematical assertions passed in 0.0500 seconds. Prime logarithms use dyadic mantissas in [1,2), 48 rational atanh terms and tail <=2z^97/[97(1-z^2)], z<=1/3. Signed coefficients multiply the correctly reversed interval endpoints; decimals are rounded outward. No floating estimate supplies a sign or an upper bound.

All seven lead statement hashes match. The integrated graph checks source bytes, exact dependency versions/hashes, units and admitted closure. Eight new mutation fixtures passed in 0.0276 seconds, including a cycle through FEI using the new selectable bridge, primary hash drift, unresolved MU blocking B09, stale finite version and isolated source-byte tampering. No admitted node has an unresolved premise. The cycle engine is unchanged, and its existing stage-1 66,067-case DFS/Kahn check is retained without repetition. B17's compound finite census and stronger thirty-decimal B09 number were not rerun or silently newly accepted.

Commands executed from A081:

```text
python -X utf8 runs/20261011T234021Z-account05-A081-dependency-certificates/code/stage2.py
python -X utf8 runs/20261011T234021Z-account05-A081-dependency-certificates/code/audit_updates.py
python -X utf8 runs/20261011T234021Z-account05-A081-dependency-certificates/code/finalize.py
```

Estimated working memory was 32 MB; the checks were far below the 300 MB threshold, so memok was not required. Each observed pilot was under 60 seconds. No heavy search, GPU, solver, external process window, git command or asynchronous worker was started. Source snapshots are individually below the 20 MB cap. Structural validation cannot replace theorem reconstruction or establish a universal FEI inequality.

# proof dependencies and changed downstream conclusions

Changed source closure: B09 core v1's unversioned source leaf is resolved by MU-FINITE-UNITARY-1988@1 and A093's acceptance. The B09 literal statement/version/hash is preserved. The historical unpinned node remains disconnected history. Three analytic B17 claims receive independent A081 reconstruction records, and the finite cutoff receives an independent exact reconstruction with its narrower A082 premise explicit. The source graph is acyclic and its admitted closure has sixteen nodes.

The selectable and aggregate definitions have separate type descriptions. Six FEI routes are alternatives with explicit unpaid assumptions, not a conjunction of every campaign gap. The new selectable route cannot use FEI to discharge its own premise. Scope relations are separate from proof edges: KB5 blocks extending A082; it does not refute A082's accepted version. The whole compound KB4 census and thirty-decimal B09 enclosure retain pending finite-audit status. Floating search evidence is not imported as a mathematical premise.

This run creates A081-VERSIONED-DEPENDENCY-CERTIFICATE@2, superseding only this agent's v1 certificate description; original mathematical statements and histories are preserved. CLAIMS.json also records the independent scoped reviews. Shared registry adoption, review of the certificate itself, mirror verification and downstream mathematical use remain separate and are not inferred from saving.

# one next mathematical action and independent reviewer

NEXT: consume the next complete A097/A064/A099 stopping-tree residual at its exact version and check whether its paid conditional erasure plus prescribed terminal reference entropy is bounded by one nonreused physical influence budget on arbitrary-core balanced tensor activations. Keep the arbitrary core's entropy as an unpaid premise when it survives, and reject any dependency cycle or finite-class substitution. This directly tests the universal C019 bridge; another finite census or repeated classical uncertainty calculation would not close the retained global debt. Primary independent reviewer of this certificate/review package: A090; alternate A094. A085 retains the independent compound-census audit, and A083 can consume the source-pinned JS scalar statement without inheriting a claim that the real-log proof is already kernel-checked.

# actual persistence receipts or precise save blocker

Saved all required run files, exact graph, validator guide, code, fixed-witness rational output, mutation audit, claim hashes and source snapshots inside A081. PROGRESS.json and PACKET_DELTA.json are byte-identical with packet_ids=[A081]. The annotated protocol field label is serialized as packet_ids according to the explicit user compatibility instruction. STATUS.md has two lines; WORKLOG.md is appended and LEARNED.md updated. out/ARTIFACT_RECEIPTS.json records output sizes and SHA256 hashes; out/FINAL_VALIDATION.json records schema, source, closure and size checks. No persistence blocker remains. Independent certificate acceptance, supervisor copying, external mirror receipts and downstream mathematical use are pending. Finalized 2026-10-11T23:56:56.132090+00:00.

# Universal bridge

This stage moves C018 erasure payment by independently closing the JS/selection implication and certifying a necessary selectable constant of at least 2.695887520153100810486497, about 0.02339853618 above the finite four-variable optimum; it improves no universal upper constant. It also moves C019 by removing one exact primary-source gap in B09's core uncertainty input. What remains is a dimension-independent B<=KI or selectable B_i<=KI_i theorem, or a terminal-inclusive stopping-tree payment with every influence spent once. NEXT audits that same universal residual on arbitrary-core tensor activations, where arbitrary seed entropy cannot be disguised as a small terminal class; it is the shortest source-bound route available to this dependency packet because it can expose or close the missing full-FEI implication rather than add another isolated class theorem.
