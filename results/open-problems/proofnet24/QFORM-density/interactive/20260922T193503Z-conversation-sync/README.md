# QFORM conversation source archive and proof-status check

Record: 20260922T193503Z-conversation-sync. Repository: yspennstate/math-open-problems, branch master. Programme: QFORM-DENSITY-3EIG-20260922.

## What was synchronized

All 33 UTF-8 text members of the five proof packages delivered in this conversation are now recoverable from committed sources. These include the mathematical proofs, corrections, LaTeX source, checking scripts, executed result files, package instructions, and manifests.

Fifteen text members were already byte-exact in the canonical research directories. Seventeen missing or differently formatted text members were copied into the five subdirectories of this archive. The remaining regularized-determinant report differs from the canonical report by exactly two spaces: the lossless patch preserves the delivered variant without modifying the canonical mathematics. All source Git blob hashes were read back and compared with the package bytes. Local reconstruction of all 33 text members and a second idempotent reconstruction both passed.

The manifest records exact paths, immutable source commits and hashes. The source copies are present at commit c45f1de26dafdd64f5f725eb64dfa6f599251413. The manifest was added at e7973b92563f3357c2750d23bd7fe7934683b9ba; the reconstruction helper at 769ba793b971c80e940e356a6cfed52a076bac87; the reconstruction check result at 7c66dc7bd05e574c145be79844aae10d0d93c3fc.

**Binary exclusion:** the five original ZIP byte streams and the compiled PDF were not uploaded in this synchronization. The complete LaTeX source is present. The manifest explicitly marks those binary exclusions and records their hashes. This is a complete text-source archive, not a claim that every binary attachment was uploaded.

From an existing local clone containing the source commits, run:

    python restore_sources.py --repo-root /path/to/math-open-problems --output /path/to/restored-qform

The helper uses only local files or local git show, checks every reconstructed text file, and refuses conflicting output. It does not access the network, execute mathematical checkers, compile LaTeX, or launch workflows. The raw ZIP byte streams are not reconstructed.

## Mathematical map

The canonical directories, relative to proofnet24/QFORM-density/interactive/, are:

- 20260922T120815Z-separable-perturbations: diffuse quadratic component plus coordinate-separable phases; the longer delivered exposition and its complete LaTeX source are preserved here in initial_note/.
- 20260922T131746Z-regularized-determinant: cross-block regularized determinant and entire-range diffuse branch.
- 20260922T151048Z-ridge-window: one-scale ridge certificate and spectral-window branch allowing small nonseparable tails.
- 20260922T161801Z-rank-two-fusion: arbitrary-orientation rank-two affine half-Riesz theorem and scalar-Schur consequences.
- 20260922T180015Z-pair-log: pair logarithmic envelope, arbitrary-rank physical-pair extension, and counterexamples to the arbitrary-joint coarea lemma and conditional-vector-density moment.

Every result retains its stated scope. Historical wrappers and status records are preserved as historical documents, not updated certificates of mathematical correctness or current worker execution. This archive does not claim a proof of the unrestricted universal density conjecture or a literature-wide novelty result.

## Check of the latest shared outline and the requested Claude comparison

The shared owner-side outline was inspected at brain commit 8b508713b9edf3ae1c92824be781da39a8c0d948 (revision 2026-09-22.13) and refreshed at ef0cb60d59dc03d4272b137da01591bb22757924 (revision 2026-09-22.15). The latter explicitly leaves the general coupled estimate to be proved. Its scalar L3/Hausdorff-Young argument is valid in the stated separable scope: the square density h obeys integral h^(3/2)<=5, so three independent scalar factors give integral |phi|<=2*pi*25. It does not establish the coupled-matrix step.

The same refreshed outline still proposes a uniform conditional-density supremum after conditioning on the scalar remaining quadratic contribution. SCALAR_CONDITIONING_OBSTRUCTION.md gives an exact counterexample to that sufficient gate: it uses n=128 independent cap-one uniforms, three flat orthonormal large directions, and a full-rank matrix with spectrum 1,1,-1,1/128,...,1/128. Extreme residual-energy conditioning forces the three-direction energy into an arbitrarily short interval, contradicting every finite uniform conditional density bound. This is NOT a counterexample to the unconditional QFORM conjecture.

The correction was committed at 24b033307e114fe98c1dad1d4ce910076fa7be9a, blob bf2b9b2dcc4b4da3f7bead8f59b132afeafad448. It continues to apply to the scalar-conditioning gate repeated in revision .15. The earlier arbitrary-joint coarea counterexample also remains relevant; the rank-three general case cannot be declared solved on that premise.

No current Claude-authored session, final proof file, or authenticated handoff was identified in the accessible repository search, file search or context lookup. The generic owner-side outline is not attributed to Claude without evidence. A shared request is being sent for Claude's exact repository, commit, proof path, scope, and remaining gap. No direct private-session access, live conversation with Claude, receipt by Claude, or full solution is claimed.

## Worker check: evidence rather than registration alone

At the initial brain snapshot 8b508713b9edf3ae1c92824be781da39a8c0d948, the existing request QFORM-SIGNIN-20260922T145401Z had response directories for 20 account01 slots, 20 account02 slots, 17 account03 slots, and 4 account04 slots: 61 distinct slots of 80. These counts are directory-level evidence, not independent verification of every response body, fresh hourly execution, or completed proof.

Account03 lacked B02, B10, B11 in that request. Account04 had B11, B14, B15, B16 and lacked B01-B10, B12, B13, B17-B20. Repeated responses within one slot were counted once. Other hourly receipts may exist; absent request artifacts are not proof of an outage.

The single actual native scheduler read in this invocation, around 19:25 UTC, showed all 20 account04 tasks enabled, hourly, exclusively QFORM-assigned, with email and push flags false. Every exposed last-run timestamp was within the previous hour at that observation. These are execution/configuration observations, not proof of substantive success. No native scheduler mutation was needed or performed. Other-account native configurations were not directly accessed; their older coordinator summaries are distinguished from this live observation.

The standing full-target assignment is unchanged. Existing coordinators must reconcile outstanding sign-ins against real run receipts, obtain missing worker-authored confirmations, and report blocked writes honestly. No fabricated acknowledgements, backdating, speculative restarts, duplicate tasks, schedule changes, notification changes or cross-account authentication are authorized.
