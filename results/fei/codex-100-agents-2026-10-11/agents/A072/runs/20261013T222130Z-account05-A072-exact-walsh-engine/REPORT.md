## exact target, quantifiers, hypotheses and units

Let h on six uniform bits be -1 exactly on A={0,1,2,4,8,16,32,6,17,40}. For a nonconstant six-bit Boolean core g, E(g)=min_relevant_i B_i(g)/Inf_i(g), B_i=H(S_i|S_-i), spectral masses ghat(S)^2, entropy in bits. Study F=h(g_1,...,g_6) with disjoint identical core blocks, and retain all 36 physical coordinates. Output orientation is not quotiented before composition.

The finite guarded repair proved here is: if E(g)>=14/5, some COMMON output sign sigma makes every coordinate ratio in F=h((sigma*g)^6) at least its corresponding core ratio, hence E(F)>=E(g). To implement it, first orient g0 to M<=32 negative points. Use g0 for M=4..15 or 21..32, and -g0 for M=16..20. The high-E condition excludes M<=3. In particular this covers the intended harder threshold K6>14/5, with no assumption that a reserve is always nonnegative. The theorem quantifies over all six-bit cores; the dimension restriction is essential. It is not an all-depth assertion, since F has 36 inputs.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start, supervisor snapshot 2026-10-13 22:15 UTC; B15 STREAM_NOTES v2 remains unchanged from 2026-10-11 23:25; read own STATUS.md. The lead's A072 baseline target is already completed. Dispatch consumes new A075/A071 dependencies rather than repeating the B09 grid, f5/f6 baseline or a matching-growth scan.

Read A075 REPORT.md and DERIVATION.md, run 20261013T212622Z: matching/path/graph mechanism closure, and the final arbitrary-core signed-collision NEXT. Read A071 REPORT.md, CLAIMS.json, code/search.py, signatures.py and orientation_verify.py, run 20261013T215901Z: equation (1), 559-signature domain and both-orientation obstruction. Read A056 REPORT.md, run 20261011T233147Z, equations (3)-(6) and signed recentering proof. Reread EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2. Reuse A072 stage 1 Walsh/biased inverse/edge engine and stage 2 prime-log erasure engine with source hashes. No other agent's code is imported or executed; only A071's saved sign table is read AFTER independent reconstruction for exact agreement. Papers and broad campaign sources retain prior-stage context pins; no fresh manuscript or literature audit is claimed. Source receipts record exact local bytes and consultation scopes.

## complete derivation or exact first unsupported line

### Signed reserve and physical influence, with an independent engine

Write p=P(g=-1), m=1-2p, v=1-m^2, beta_i=ghat({i}), t=beta_i^2. Expand the outer sign as h(y)=A(y_-j)+y_j D(y_-j), where y_j=+1 corresponds to physical bit x_j=0. For T on the other five outputs take normalized product Fourier coefficients a_T,d_T; set C_T=a_T+m d_T, U_T=C_T^2, D_T=d_T^2 and q=sum_T D_T. Exact boundary enumeration gives q=2p(1-p)^3(2-p)>0. Define phi(x,y)=(x+y)log2(x+y)-x log2 x-y log2 y and

    R_p(t)=sum_T phi(U_T,t D_T)-q phi(m^2,t).

For a nonempty selected-child residual spectral set, the coordinate-pair amplitudes both have multiplier d_T times the normalized nonempty spectra of occupied other blocks. Homogeneity of phi and Parseval on those blocks give q times the corresponding child's pair contribution. For the selected empty residual, the no-i amplitude is C_T and the with-i amplitude is beta_i d_T. Consequently, including the child's removed empty pair precisely once,

    B_(j,i)(F)=q B_i(g)+R_p(beta_i^2),
    Inf_(j,i)(F)=q Inf_i(g).                                 (1)

The influence equality also follows directly: a physical edge can change F iff it changes g_j and the outer gate is pivotal given the other five block outputs. Outer matching-pair permutations and swaps act transitively on all six j, so the same reserve function applies in every block. No square of a signed sum is replaced by an incoherent mixture. Constants are excluded; irrelevant core coordinates have beta=0, B=0 and no influence, so none become newly relevant.

The new independent path directly sums signed conditional sections h0,h1 over the 32 other-output assignments. For each T it computes expectation of centered-bit products times (h0+h1)/2+m(h0-h1)/2 and (h0-h1)/2. Dividing their squared moments by [p(1-p)]^|T| gives U_T,D_T. A second, reused checked uniform-Walsh-to-biased polynomial conversion on the actual outer truth table verifies these exact masses, sign inverse, Parseval and all physical pivotal probabilities at every one of 63 biases. Those checks precede the reserve comparisons. out/outer_bias_M.json saves all 32 rational U,D packets, all 64 outer spectral masses and the physical multiplier q for every M.

### Complete signature domain and one orientation for every coordinate

Let M be the number of negative points of a six-bit core. For a chosen coordinate let M0,M1 be its half counts, d=|M0-M1|. Necessarily

    1<=M<=63, 0<=d<=min(M,64-M), d congruent M (mod 2),
    p=M/64, |beta|=d/32.                                    (2)

Conversely place (M+d)/2 lex-first negatives in its zero half and (M-d)/2 in its one half. This constructs an actual sign core realizing every signature. Each witness is checked with integer Walsh, exact sign inverse, Parseval and independent physical edges. There are exactly 559 signatures, all reconstructed. The sign counts are 440 positive,31 zero,88 negative; every one agrees with A071's independently saved result. Zero cases have d=0 and exact R=0. Fraction/outward logarithm intervals decide every other sign without tolerance.

For each minority count M=4..32, at least one orientation has R>=0 for EVERY feasible d simultaneously. The common choice is p=M/64 except choose p=1-M/64 for M=16..20. The exact 29-row policy, including all alternative safe signs, is saved in out/orientation_policy.json. Since this policy is uniform across d, it applies to all coordinates of one actual core using a single sign, rather than selecting a different sign per coordinate. Combining this with (1) gives the desired ratio inequality as soon as M>=4.

### Exclude all sparse bad sectors under the high-E hypothesis

Output complement preserves B,I and E, so take the smaller negative side. If it has at most three points, physical input translation normalizes one point to zero. Singleton support has one orbit. Two points are classified by their Hamming distance 1..6, yielding six orbits. For three points {0,u,w}, each nonconstant coordinate column belongs to one of the three patterns (10),(01),(11). Let their counts be a,b,c. Coordinate permutations reorder columns; changing the anchored point and relabeling the unordered triple permutes the three counts. Thus sorting 0<=a<=b<=c, with a+b>0 and a+b+c<=6, is a COMPLETE cube-isometry covering. The remaining columns are dummy coordinates. This gives sixteen triple representatives. No general affine transformation, which could change physical influence, is used.

The total 1+6+16=23 representatives is not a sampled sparse search. For every representative the prior checked Walsh/erasure engine constructs its six-bit truth table, every physical child, exact B_i/JS_i/decrement, inverse and edges. It finds a relevant coordinate with B_i/Inf_i<14/5; each strict inequality is certified by its exact rational prime-log form and a denominator-cleared integer prime-power comparison. These 23 certificates cover every actual six-bit core with at most three minority points. Hence E(g)>=14/5 excludes M<=3, and the common-orientation policy proves the finite guarded theorem. The integer certificate out/guard_gap.json separately proves K6>14/5, where K6=16/3-(21/8)log2 3+(95/24)log2 5-(121/24)log2 11+(65/24)log2 13. A075's all-dimensional matching theorem is not a premise.

### Full terminal entropy is retained

Let pi_p(T) be the exact normalized biased outer spectrum, and let rho(S)=ghat(S)^2/v for nonempty S, the centered core spectral law. Each occupied outer block is filled by a nonempty inner spectral set; the occupied-block pattern and actual nonempty inner sets determine the physical set uniquely. Therefore the Fourier law is a disjoint hierarchical law and

    H(F)=H_p(h)+sum_j [v q] H(rho)
        =6q H(g)+C_p,
    C_p=H_p(h)-6q h2(v),
    I(F)=6q I(g).                                            (3)

To verify the second equality, v H(rho)=H(g)+m^2 log2(m^2)+v log2 v; zero conventions cover m=0. No terminal H(g) is discarded. Every out/outer_bias_M.json saves the exact rational-log terms for C_p and its signed coefficients. The guarded E theorem neither bounds C_p by physical influence nor pays a whole normalized reference or a stopping tree. That remains a distinct obligation, including after physical restrictions change block biases.

### Scoped independent review of the original obstruction

Four fixtures independently reconstruct h and the six-bit point defect, each in both output orientations. Physical transitivity of the core and the outer matching automorphisms acts transitively on all 36 composed coordinates. The engine checks equality of every core coordinate's exact B/I form before using that argument. The point defect has E>9/4 but both compositions have E<9/4 and negative reserve. The positive fixture satisfies 323/100<E(h(h^6))<324/100; the complemented seed composition has E<8/3. out/fixtures.json contains exact outward bounds and core erasure forms. These accept the signature and compressed-fixture clauses of A071-F6-BIASED-ADMISSION-OBSTRUCTION@1 at their stated scope. The separate A071 408-core family and direct18 implementation are not reviewed here; out/REVIEW.json makes that scope explicit. A072 contributes the guarded repair and does not claim independent acceptance of its own new theorem.

### Arithmetic enclosure and first unsupported line

For integer n>0 write n=2^k r with 1<=r<2. Put z=(r-1)/(r+1)<1/3. The positive series ln r=2 sum_(j>=0)z^(2j+1)/(2j+1), after 48 terms, has remainder between zero and 2z^97/[97(1-z^2)]. Each term is floored at scale 2^128; add 48 units plus the ceiling of that scaled remainder to obtain an upper bound. Independently enclose ln2 by z=1/3, divide nonnegative endpoints outward at scale 2^96, and add k exactly after division. Powers of two are exact. Homogeneity cancels the common denominator in phi(x,y), leaving a linear combination of positive integer logarithms; negative coefficients use opposite endpoints. This independently ranged enclosure differs from A071's correlated k ln2 enclosure. For sparse rational prime-log forms, clear coefficient denominators and compare arbitrary-precision integer products; a preconstruction 8000000-bit bound enforces the resource limit. No floating entropy chooses a sign or coordinate.

The first unsupported universal line is that the safe orientation policy holds for all continuous feasible p,t arising from arbitrary-dimensional hard cores, or that every remaining bad signature can be excluded by E>=14/5 in all dimensions. The six-bit signature grid and 23 sparse isometry classes do not prove those lines. Applying the six-bit admission again to a 36-bit composed core is unsupported, even if its E exceeds 3.23. No unbounded E or H/I family, global C018 bound or terminal C019 payment is asserted.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes all signature/sparse computation; FIXTURE_SPEC.json precedes the four-fixture review. Pilot: M in {1,4,16,32}, exactly 30 feasible signatures, runtime 0.18095979999634437 seconds; all signs resolved. Main: 559 signatures,63 biases,29 orientation-policy rows,23 complete sparse representatives,zero failures; runtime 6.0721914999885485 seconds. Initial successful main reconstruction took 6.2049824 seconds; a second run added persistence of each exact outer packet/terminal-correction profile without changing domain or arithmetic. Four fixtures: zero failures, runtime 0.1923636000137776 seconds. No full36-bit truth table or dimension growth is attempted. Mathematical arithmetic is Python int/Fraction and outward fixed-scale integer logs; estimated RAM <=100 MB (not measured), one serial job, caps 55 seconds pilot/fixtures and120 seconds main. No job expected above300 MB, GPU, background helper or memory-gate override.

    python -X utf8 runs/20261013T222130Z-account05-A072-exact-walsh-engine/code/check.py --pilot
    python -X utf8 runs/20261013T222130Z-account05-A072-exact-walsh-engine/code/check.py
    python -X utf8 runs/20261013T222130Z-account05-A072-exact-walsh-engine/code/fixtures.py
    python -X utf8 runs/20261013T222130Z-account05-A072-exact-walsh-engine/code/persist.py

Each signature JSONL row is flushed immediately. Each sparse certificate, bias profile and fixture is saved on completion. ENGINE_CERTIFICATE.json and fixture_summary.json supply exact counts and runtime receipts.

## proof dependencies and changed downstream conclusions

The signed split and full terminal identity are rederived here from Walsh expansion and physical edges; A056 equations (3)-(6) provide source context, not an assumed unreviewed universal result. The reused A072 algebraic engine is pinned, and all actual outer/core inputs still run its inverse/Parseval/edge checks. A071's signatures are compared only after independent reconstruction, not used as a sign oracle. Source-complete pending claims are handled by scoped reconstruction and this finite repair, rather than another broad candidate. One bundled A072-F6-SIXBIT-GUARDED-ADMISSION@1 is recorded, review pending; out/REVIEW.json independently supports the specified clauses of A071@1. C018/C019 and full FEI remain open. No shared claim index is changed and no prior correctly scoped theorem is refuted.

## one next mathematical action and independent reviewer

Next: A075/A071 should formulate the same common-orientation policy on the continuous feasible (p,t) domain, then either certify it or produce an actual high-E core in a bad sector. Use the exact outer profiles and retain C_p from (3) along with inherited B and one physical influence ledger. This is a continuum/realizability bridge, not an n=7 census. A074/A092 should independently reconstruct the sparse triple covering and selected-coordinate prime-power signs; A085/A089 should check that the orientation is common to every coordinate and audit the arbitrary-dimension boundary. All reviews and downstream use remain pending unless explicitly recorded here.

## actual persistence receipts or precise save blocker

Saved REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json with packet_ids=[A072], both frozen specs, code, ENGINE_CERTIFICATE.json, exact signatures/outer profiles/sparse records/fixtures and scoped REVIEW.json in the requested A072 stage directory. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. The persistence script checks exact protocol field sets, statement hash, delta equality and each file below20 MB, then saves source hashes and out/manifest.json. Only local saving/readback is claimed. Independent review of the new repair, supervisor copy, mirror verification, registry adoption and publication are pending. All writes remain within A072; no external messaging or brain write occurs.

## Universal bridge

This stage moves B15's signed-admission bridge toward C018 by replacing the false unguarded transfer with a proved common-orientation repair for ALL six-bit cores having E>=14/5, including the K6 hard-core threshold. It independently reconstructs all559 reserve signs and the actual36-bit obstruction E>3.23, and retains full terminal H(g) via (3). It changes no all-dimensional erasure constant and pays no universal terminal correction. What remains is the continuum reserve policy plus a dimension-independent high-E exclusion of bad sectors and an owned physical price for C_p; NEXT attacks that exact dimension/realizability gap using the saved signed profiles rather than repeating a finite census or the closed sparse matching mechanism.
