# A084 stage 3: finite signatures to arbitrary-dimensional continuum admission

## exact target, quantifiers, hypotheses and units

The prior AND sign-map packet is complete and is retired; B17 lead v2 still lists that stale target. Following protocol dispatch, this stage consumes the new A071/A072 signed-admission dependency shown on the current board. Let h be the six-bit sign negative on {0,1,2,4,8,16,32,6,17,40}. For a Boolean core g on ANY uniform n-cube with minority probability p_min in [1/16,1/2], compose six disjoint identical oriented copies F=h(g1,...,g1). The target is a single common orientation preserving the true physical-coordinate erasure ratio B_i/Inf_i for EVERY relevant coordinate, over ALL real parameter values in that bias band. B_i=H(S_i|S_-i); entropies are bits; all physical variables and the entire terminal H(g) are retained.

**Result:** the continuum admission theorem is proved at author level. Orient g0 to its minority output probability p_min; use g1=g0 for p_min<=7/32 and g1=-g0 otherwise. Then B_(j,i)(F)/Inf_(j,i)(F)>=B_i(g)/Inf_i(g) for every relevant i,j, hence E(F)>=E(g). No high-E assumption, dimension cutoff or singleton-granularity lower bound is needed WITHIN this band. Independent review is pending; full FEI remains open. Below p_min=1/16, arbitrary-dimensional high-E exclusion or signed payment remains unresolved.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-13 23:59 UTC, own STATUS.md, and B17 STREAM_NOTES.md v2 (2026-10-11 23:40 UTC). The latter is unchanged and its A084 AND target was already completed in run 20261012T044029Z; no disagreement with its mathematics is asserted, only a stale completed assignment. Re-read EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 in full. Read A072 run 20261013T222130Z REPORT.md, CLAIMS.json, code/check.py and out/orientation_policy.json, especially signed reserve equation (1), six-bit signature/23-orbit guard, full terminal equation (3), and first unsupported continuum line. Read A071 run 20261013T215901Z REPORT.md, particularly its two-orientation obstruction and arbitrary-core NEXT. The board's closed finite censuses, half-tax and prior AND work were not repeated. Prior campaign/paper manifests remain context; no new literature or manuscript audit is claimed. Exact hashes of actual read sources are in out/SOURCE_RECEIPTS.json. No other agent code was imported or executed.

## complete derivation or exact first unsupported line

PROOF.md is a complete derivation. The signed coordinate identity is reconstructed from actual conditional outer sections and disjoint-block Fourier expansion:

    B_(j,i)(F)=q B_i(g)+R_m(beta_i^2),
    Inf_(j,i)(F)=q Inf_i(g),
    q=2p(1-p)^3(2-p), m=1-2p,
    R_m(t)=sum_T phi(U_T,tD_T)-q phi(m^2,t),
    phi(x,y)=(x+y)log2(x+y)-xlog2 x-ylog2 y.

Here p is the CHOSEN oriented output bias, U_T=(a_T+m d_T)^2 and D_T=d_T^2; recentering is performed before squaring. All six outer coordinates have the same reserve because the gate's matching-pair automorphisms are transitive. One output sign applies simultaneously to every core coordinate and all six blocks.

The new finite-to-continuum mechanism is an exact boundary lemma. For positive packets set c=m^2, lambda_T=D_T/q and u_T=U_T/D_T. Define A=sum D_T log2(u_T/c). The weighted geometric mean G(t)=product(t+u_T)^lambda_T satisfies G'(t)>=1 by weighted AM-GM. Thus A>=0 implies G(0)>=c, then G(t)>=t+c and R_m'(t)=q log2(G(t)/(t+c))>=0 for every t>0. Since R_m(0)=0, the slope test proves the entire t half-line, not only the attainable finite six-bit signatures. Conversely R_m(t)/t->A, so a negative slope diagnoses failure near t=0.

Direct uniform-Walsh polynomial expansion gives 12 exact packet types and FOUR U/D ratios; the formulas are in PROOF.md and out/SYMBOLIC_PACKETS.json. An outward rational-log interval certificate proves A>0 on m in [9/16,7/8] with 9 closed adjacent intervals and on m in [-9/16,-1/2] with 4. Their minimum certified lower bounds are respectively

    47949270588870825/2305843009213693952 >0,
    1334759120530679/9223372036854775808 >0.

Coverage is checked by exact endpoint equality. For the remaining complemented means [-1/2,0], PROOF.md proves every ratio U/D>=m^2 analytically using elementary polynomial bounds, with a strict positive-weight packet. At m=0 the subtraction term vanishes and phi is positive directly. At t=0 every reserve is exactly zero; there is no unclassified singular boundary. These arguments cover all real means in the stated band and every t>=0. Actual singleton t<=4p_min^2 is therefore included automatically, irrespective of core dimension.

The full terminal identities are kept:

    H(F)=6q H(g)+C_p, C_p=H_p(h)-6q h2(1-m^2),
    I(F)=6q I(g).

Neither C_p nor a reference/reset/stopping bill is dropped or claimed paid. This closes A072's dimensional gap in its SAFE BIAS BAND only; its finite 23-orbit rare-core guard is not used to exclude rare arbitrary-dimensional cores.

The analytic low-bias reductions show why the residual cannot be solved by a larger grid: for original p_min->0, the normalized boundary slope is 2log2(p_min)+6+o(1) in the minority orientation and 2log2(p_min)+2+o(1) in the complemented orientation. Both are negative eventually. These follow from the four rational packet ratios/weights and imply negative reserves near t=0 in both orientations. They concern reserve signs and do not exhibit an actual high-E core in that sector.

**First unsupported universal line:** a dimension-independent exclusion or owned signed payment for high-E cores with p_min<1/16. Even after that, an iteration-closed bias/orientation policy and a terminal-inclusive price for C_p are needed before a universal C018/C019 conclusion. Composition output bias can leave the certified band; nothing here authorizes indefinite bootstrap or unbounded E or H/I.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede each computation: FROZEN_SPEC.json (4096 binary64 discovery signs), DERIVATIVE_PILOT_SPEC.json (1022 boundary samples), SYMBOLIC_SPEC.json (32 exact polynomial packets), and CONTINUUM_SPEC.json (exact certificate and five physical fixtures). Discovery outputs are explicitly evidence only, not proof. The 0.1867-second reserve pilot and 0.3520-second boundary pilot suggested a safe policy on [1/16,1/2]. No automatic dimension growth occurred.

Commands from the agent folder, with prefix `runs/20261014T000747Z-account05-A084-continuum-parameters/`:

    python -X utf8 code/pilot.py
    python -X utf8 code/boundary_pilot.py
    python -X utf8 code/symbolic.py
    python -X utf8 code/certify_continuum.py
    python -X utf8 code/check_physical.py
    python -X utf8 code/check_grouping.py

The exact interval checker uses Fraction arithmetic, 24 atanh-series terms with an explicit tail, exact power-of-two range reduction, four-corner division for signed logarithm numerators, and outward 64-bit quantization. It checked 13 successful covering intervals, visited 24 intervals, and passed 25 exact ratio-grouping checks against independently formed Walsh packets at five fixed rational means; runtime 0.8335 seconds. All successful leaves and exact endpoint coverage are saved immediately in out/MINORITY_ORIENTATION.json and COMPLEMENT_ORIENTATION.json; out/CONTINUUM_RESULT.json records the result. No finite-grid-to-continuum inference is used.

The supplementary symbolic checker verifies 17 global rational-polynomial identities (12 packet-to-ratio identities, four aggregate weights, and their sum q), not merely sampled polynomial equalities; SymPy 1.14.0, runtime 76.3544 seconds, out/GROUPING_CHECKS.json.

The actual-core verifier reconstructs five uniform Boolean cores with (n,minority count)=(4,1),(3,1),(5,7),(2,1),(1,1). It checks integer Walsh inverse, Parseval, physical influences, every core coordinate's reserve, and 160 exact direct-conditional-section packet matches. It also constructs complete actual composed truth tables on 18,12 and 6 physical bits, checking the coordinate identity against the independently transformed physical table and physical edges. Those point-core compositions are transitive on all physical coordinates; the other two fixtures are checked by compressed exact packets and all their core coordinates. Total 217 assertions passed in 7.6444 seconds. Balanced output orientation may be tied either way; its sign does not alter squared core spectra or the selected bias. Results and per-fixture data are saved in out/PHYSICAL_RESULT.json and PHYSICAL_FIXTURE_*.json. These are same-author checks with distinct representations, not independent acceptance.

The first symbolic run failed an internal polynomial-equality assertion because re-parsing a stored expression created a second symbol named m with different assumptions. The corrected parser maps the name to the original symbol; all 12 packet types and the exact q identity then passed. No polynomial formula, search domain or claimed sign changed. This is preserved in WORKLOG.md rather than counted as a substantive mathematical failure. Estimated maximum RAM <150 MB, one serial job at a time, the supplementary grouping verifier took 76.3544 seconds, exceeding the 55-second symbolic pilot budget; this overrun is recorded rather than described as compliant with that budget. It was a fixed algebra check, not an expanded search; all jobs were under the 30-minute limit. No job expected above300 MB was started; no memok override, GPU or detached process was used.

## proof dependencies and changed downstream conclusions

The new proof depends only on exact Boolean Fourier expansion, phi homogeneity, Shannon chain rule, weighted AM-GM, and the saved rational interval certificate. A071@1 and A072-F6-SIXBIT-GUARDED-ADMISSION@1 are source-bound precursors, not unreviewed universal premises; their signed identity is rederived here. No external finite census or sparse-orbit guard supplies an arbitrary-dimensional hypothesis. This is completion of the explicitly open continuum bridge, not another broad full-FEI candidate, and independent acceptance of the new theorem is pending.

A071/A072/A075/A089 can now replace their six-bit signature restriction by a dimension-independent theorem whenever p_min>=1/16. It applies to every actual core coordinate using one common sign, including arbitrarily tiny singleton coefficients that a finite grid could miss. The remaining high-E rare sector is explicit, and the full C_p terminal identity prevents an admission statement from being presented as an entropy payment. No existing correctly scoped finite claim is refuted; no shared registry is changed.

## one next mathematical action and independent reviewer

Next: use the four-ratio logarithmic boundary profile to test whether an ACTUAL arbitrary-dimensional high-E core can have p_min<1/16, or derive an owned negative-reserve correction there, while carrying H(g) and C_p and checking bias closure after every legitimate composition. This is the exact residual left by the admission route, not an n=7 census. A075/A071/A089 are next consumers; A074/A092 are primary independent reviewers of the signed physical identity and policy, with A090/A094 reviewing the geometric-mean implication, exact box coverage and analytic boundary domain. No messages or writes to other agents are made.

## actual persistence receipts or precise save blocker

REPORT.md, PROOF.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved with code, specs and exact outputs under this requested A084 run directory. STATUS.md, WORKLOG.md and LEARNED.md are current. out/RECEIPTS.json binds local artifact hashes, sizes, protocol fields and compatibility-copy equality; every file is below20 MB. Shared sources and other agents' folders are read only. No git, brain write, mail, external message, detached process or shared index mutation occurred. Local durable save is complete; independent review, supervisor copy, mirror verification and downstream use remain pending.

**Universal bridge:** This stage moves the source-bound signed-admission target toward C018 by closing the finite-to-continuum and finite-dimension gaps on the entire real bias band [1/16,1/2]: a 13-box rational certificate plus analytic boundaries preserves every coordinate's erasure ratio for every core dimension using one common sign. It improves no universal FEI constant and pays no C019 terminal bill. The exact remaining obligations are the high-E rare sector p_min<1/16, legitimate iteration/bias closure, and a single-use physical payment for C_p with full terminal entropy. NEXT targets that quantified rare-sector/ownership obstruction using the four-ratio boundary profile, rather than repeating the retired AND map, finite signatures or another isolated class census; it is the shortest continuation toward the unpaid universal admission bridge.
