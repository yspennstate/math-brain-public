# STRAT16 work log

2026-11-13 14:36 +04 — Task received at workspace launch, 14:34 +04.
Read STRAT7/RESULT.md in full, its concavity, boundary and tree scripts;
read STRAT15/RESULT.md, exact_bernstein.py, local_uniform.py and replay_all.py.
Brain orientation and area recall completed. Mesh hello/digest/claim/assert
and shared checklist registration were attempted; the sandbox denies their
shared databases. No live conflicting claim was reported. All new artifacts
are confined to this workspace; supplied trees are read-only.

OPEN: the 2+5 theorem and equality classification. First check: derive the
fixed-selected-projector functional and test the n=5 concavity quadratic.

2026-11-13 14:38 +04 — PROVED (concavity_certificate.py): the full fixed-u
concavity certificate passed. Sorted zero-sum U has four nonnegative gaps;
all 24 ordered subcones have 252 coefficient matrices, each exactly PSD by
rational symmetric elimination. This certifies -R k^2 Q, including its
leading padding coefficient. NUMERICAL random Hessian discovery also found
no failure, but is not used as proof.

PROVED dimension count: rank-four extreme points have at most four edges
(three tree types); rank-three ones have at most seven edges. The latter
are an additional boundary absent from the n=4 reduction. OPEN: positivity
on these boundary families; exploring a uniform spectral relaxation first.

2026-11-13 14:43 +04 — PROVED (rank_two_certificate.py): rank-at-most-two
A boundary endpoints g=0 and g=R/(5p) pass coefficientwise PSD, with 252
and 858 raw matrices respectively. Concavity supplies intermediate g.
The larger relaxed g=1 endpoint is not coefficientwise certified; this
is certificate insufficiency, not a concavity or graph counterexample.

PROVED (tree_certificate.py): star, path and fork each pass direct
nonnegative-coefficient tests in four positive edge fluxes and k=5+h.
NUMERICAL relaxed rank-two-gap projection tests give negative values if
entrywise nonnegativity is dropped. Such matrices are infeasible and are
not counterexamples. The rank-three A boundary therefore needs graph
feasibility, rather than that spectral relaxation alone.

2026-11-13 14:54 +04 — PROVED (disconnected_certificate.py): the only new
lower-component situation in a disconnected extreme point is a lower edge
alongside a three-vertex carrier. Its exact increment is nonnegative,
strict for a positive lower edge, after k=5+z and t=1-q substitutions.
Together with STRAT7 this closes disconnected extreme points. The full
theorem is still OPEN pending connected rank-three A.

PROVED (extreme_inventory.py): the connected rank-three support candidates
are 12 nonbipartite graphs, four each with 5, 6, 7 edges. The three rank-four
supports are precisely the trees. The face-map injectivity criterion decides
extremality within these support families.

NUMERICAL: a matrix extension F+S on the complete rank-two-gap zero-edge
chart had selected minimum 0.54137 and full restricted-matrix minimum
0.48253 in 20,000 random endpoints. These are discovery values only. A
degree-four SOS ansatz with scalar constraint multipliers was rejected by
the numerical SDP; a matrix-multiplier ansatz is being tried. No SOS
candidate is accepted as proof without rational coefficient reconstruction.

PROVED elementary equality restriction: the external edge weight is
1/(2M)>=1/5 because tr L5<=4, so the balanced-triangle-only graph cannot
lie in this class's closure, for any padding size. OPEN: excluding other
zeros until rank-three positivity is proved.

2026-11-13 15:04 +04 — PROVED (verify_rank_three_algebra.py): independent
universal polynomial operator identity for the rank-three matrix target,
including its annihilating S/J terms, all compact-chart bound identities
and the three padding controls. This is stronger than fixture checks.

NUMERICAL resource breach: dense SOS attempts for controls zero and one
had individual peaks 3,290,120,192 and 3,292,807,168 bytes, violating the
2.5 GB budget. The ten-second guards were too slow. They terminated;
no artifact from those attempts is accepted as proof. The earlier dense
control-two run reached numerical Solved but a queued interrupt prevented
its candidate save. The qdldl dense retry was stopped by the new 100 ms
guard at 2,133,540,864 bytes. These failed attempts are retained as logs.

NUMERICAL: a smaller overlapping-block SOS ansatz held around 1.36 GB
under qdldl but factorization was too slow. Switched that same smaller
ansatz to faer, still one compute process, one numerical-library thread,
with the rapid 1.95 GB guard. No numerical solve is a proof until exact
rational coefficient reconstruction and integer PSD residual checks pass.

PROVED (replay_all.py): all nine exact stages passed. NUMERICAL seconds 39.01730033301283, child peak bytes 61095936.

2026-11-13 15:08 +04 — PROVED (verify_sos.py): rational_sos_2.json passed
all exact polynomial identities and integer PSD residual checks. The sparse
SOS solve took NUMERICAL 180.55238 seconds, peak 1,626,324,992 bytes. Its
22 Gram matrices have a rational I/100 margin after reconstruction.
PROVED (padding_monotonicity.py): a new Schur-product identity gives
F'(1/k)<=-3I/50 at rank A<=3, so only N=7 needs the SOS certificate.
This closes every rank-three support at once and includes infinity.

PROVED: convex reduction now closes 2+5, strict for connected five-parts,
equality in the closure only two equal edges and isolates. Full first replay
passed nine exact stages in NUMERICAL 39.01730 seconds, child peak
61,095,936 bytes. RESULT.md updated with the full argument.

2026-11-13 15:18 +04 — PROVED (split34_trees.py; split34_boundary.py):
optional 3+4 extension's new tree and low-rank certificates all passed.
Four scalar tree/triangle-corner numerators have 135,927,117,801 positive
coefficients. Four boundary certificates have 84,198,588,1386 PSD
coefficient matrices, with strict finite/infinite pure-axis witnesses.
PROVED (split34_audit.py; split34_reduction.py): original-matrix rational
audits, universal separate triangle-gap concavity and two-triangle
equality at infinity passed. Full 15-stage replay is now running.

NUMERICAL operational correction: the attempted early termination of the
slow qdldl worker was denied by the sandbox; its own 900-second guard
eventually stopped it. It overlapped the successful faer worker, whose
individual peaks were 1.36 and 1.63 GB; aggregate RSS was not sampled.
The log's earlier wording about switching immediately was inaccurate.
Discovery now takes an exclusive workspace lock, uses the smaller ansatz
by default, and supports an owned stop flag. All discovery workers have
now ended. The exact replay is sequential and uses no numerical solver.

2026-11-13 15:25 +04 — PROVED (disconnected_certificate.py): the lower-edge
increment includes the additional nonnegative X1 term 2t(1-t); it vanishes
at the original extreme endpoints. The formula in RESULT.md is corrected.
The more general trace comparison s<=k-4 proves split 2+3 with arbitrary
lower components, not just a single lower edge.

PROVED (lower_components.py): the general lower-trace endpoint identity
extends four-vertex double carriers and split 2+4,3+3 to arbitrary lower
components. Nonzero endpoint prefactors are bounded below by 1/4,1/8,1,
5/9; the remaining zero-gap clique corners have positive X3. Exact
nonnegative coefficient identities verify each bound. Inherited
four-double equality at infinity is independently replayed.

PROVED: the 15-stage replay (before the added lower-component extension)
passed in NUMERICAL 56.51963 seconds, child peak 85,229,568 bytes.
The final 17-stage replay, including prior_four.py and lower_components.py,
is running. The remaining class ledger in RESULT.md is updated.

PROVED (replay_all.py): all 15 exact stages passed. NUMERICAL seconds 56.51963483399595, child peak bytes 85229568.

PROVED (replay_all.py): all 17 exact stages passed. NUMERICAL seconds 70.75303520800662, child peak bytes 82608128.

PROVED (replay_all.py): all 17 exact stages passed. NUMERICAL seconds 59.235993332986254, child peak bytes 86016000.

2026-11-13 15:36 +04 — Final audit: all seventeen proof stages PASS,
input hashes current, three inherited copies byte-identical, no numerical
solver in replay. PROVED: 2+5 and 3+4 with isolates, and four-double /
2+3 / 2+4 / 3+3 with arbitrary lower components. Exact equality and OPEN
class ledger are in RESULT.md. NUMERICAL: final replay 59.235993 seconds;
child peak 86,016,000 bytes, parent peak 18,087,936 bytes. Workspace about
4.5 MB. Earlier discovery memory-limit breaches remain explicitly recorded.

Task: “STRAT16: T104 split simple top carrier 2+5 ... plus isolated vertices,
every N >= 7” — received 2026-11-13 14:34 +04. Shared checklist and brain
write paths remain unavailable in this sandbox; durable proof artifacts and
the operational lesson are retained locally rather than deleting history.
