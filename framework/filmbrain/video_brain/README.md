# Video brain: pictures, geometry, natural narration, and verified cuts

This is a substantial craft and delivery extension to the existing
`<HOME>/filmbrain`, not a replacement graph or another rendering service.
The source is maintained in the **private** AI memories repository. The running
copy belongs at `<HOME>/filmbrain/video_brain`.

Start with `HANDBOOK.md`, then use:

```powershell
python -B <HOME>/filmbrain/video_brain/video_brain.py brief "make a mathematical lecture video"
python -B <HOME>/filmbrain/video_brain/video_brain.py check path/to/delivery.json
python -B <HOME>/filmbrain/filmbrain.py recall "brisk Microsoft narration and geometric lecture pictures"
```

The owner thinks through pictures and geometry. Every explanatory slide needs a
relevant visual; each mathematical slide needs a geometric or graphical carrier
of the idea. The narration should sound natural and move a little quickly.
**Use Microsoft natural/neural voices only for videos.** Andrew at +10% is the
current working choice, not a claim that one voice will always sound best.
Remove unnecessary pauses and introductory self-commentary, while retaining
every needed proof step. Watch and listen to the actual exported result several
times; code, a contact sheet, a voice metric, or a successful encode is not that
review.

The September 5 follow-up names **3Blue1Brown** as the visual teaching reference.
Plan object-first explanations and purposeful transformations, with Blender for
3D scenes when they make the idea clearer. The direction is carried by the existing
intent, geometry and design cards; exact source wording is retained separately in
`provenance/OWNER_DIRECTION_20260905_3B1B.json`. It supplements the earlier prompt
review and does not change that review's coverage counts.

The documentary, five-hour ReLU lecture, and new two-hour NMKC lecture are
different projects. Share craft and scars. Keep their source papers, schedules,
asset manifests, recordings, chapter order and review receipts separate.

## What this extension contains

- `catalog.py`: the authored source for ten connected craft modules and their
  individual rules, with owner-prompt and scar provenance.
- `HANDBOOK.md`, `modules/`, `knowledge.json`: generated operational guidance.
- `video_brain.py`: a narrow brief router and a fail-closed delivery-receipt
  checker. It never launches a renderer or changes compute policy.
- `test_video_brain.py`: clean adversarial fixtures, including stale recordings,
  missing visual evidence, repeated footage and recycled review receipts.
- `provenance/`: private prompt-occurrence ledger and explicit coverage limits.
- `STATUS.json` → `DASHBOARD.md`: evidence stages and unresolved work, generated
  by `build_catalog.py` rather than hand-maintained counts.

## Evidence loop, fixed before implementation

**Baseline:** the existing graph has a large harvested tool catalogue and useful
film craft. Current owner preferences were scattered; the older shared voice
node still allowed a Kokoro fallback. Actual scars include skipped spoken proof
steps, stale timing shards, missing rendered glyphs, repeated images and GPU
workers colliding. The new lecture agent separately corrected old no-LaTeX
guidance in `craft/lecture_geometry.py`; this extension preserves that work.

**Intervention:** attach source-bound owner preferences to concrete production
steps, provide a targeted brief, and check the integrity and coverage of
delivery manifests and review receipts. Integrate the cards into filmbrain's
existing graph and into the main brain's supported recall path.

**Mechanism/prediction:** a production agent can retrieve the right workflow;
the checker will reject a stale recording, missing explanatory picture,
non-Microsoft voice, reused documentary asset or insufficient review coverage
even when the media encoder returned success. Frozen negative cases should
remain silent. Test outcomes measure those bounded behaviors, not beauty or a
global improvement factor.

**Stop:** malformed provenance, unknown required evidence, conflicting live
claims, or actual UI pressure stops the dependent write or heavy job. At 12:26
Jerusalem on September 5, the owner explicitly authorized GPU movie work before
the restart. That permission supersedes the earlier restart gate; one-job GPU
coordination, current health checks and terminal CPU protections remain. The
driver repair's stability is still unverified. This extension performs no GPU work.

**Rollback:** disable this extension's production caller; retain prior artifacts
and receipts. Restore only its owned graph rows from the saved pre-import
snapshot under a fresh store claim. Do not replace the whole live database and
erase another agent's work. Main-brain policy changes use explicit supersession.

## Maintenance

Edit the catalog once, regenerate the handbook and graph payload, run the tests,
inspect the generated diff, and import only the `owner.video.*` namespace.
Never run the broad craft loader merely to add this small pack: it rewrites
unrelated live nodes. New useful lessons need a source, a condition where they
apply, a condition where they do not, and an actual outcome before promotion
from an engineering hypothesis to a verified lesson. Negative test wording
stays outside indexed graph bodies.

The running copy intentionally omits raw prompts, synthetic test receipts and
the maintenance scripts. Maintain the source in the isolated worktree
`<HOME>/codex-video-brain-20260905/12_cognitive_architecture/video_brain`
or a fresh checkout of `codex/video-brain-0905`. Before changing it, join the mesh
and claim the source, live `filmbrain/video_brain`, and `filmbrain/store` together.
Also claim the relevant memory slugs and index when changing the brain node.
Assert each exact target before writing; do not run these commands over a peer's
live claim.

After a catalog change, run `python -B build_catalog.py`. After a template change,
run `python -B build_templates.py`. Run `python -B -m unittest test_video_brain -q`
with TEMP/TMP pointing inside your claimed scratch directory. Read the generated
diff and preserve the distinction between initial held-out results and later
regressions. The additional eight wording controls initially passed six cases;
after two bounded fixes they pass eight, which is regression evidence.

Use `integrate_filmbrain.py --filmbrain-root <HOME>/filmbrain
--evidence-dir <absolute-evidence-directory> --mesh-script <absolute-agent_mesh.py>
--mesh-agent <your-live-id> --apply` to import only this pack. A second run must
leave its node and edge counts unchanged. The importer preserves the first
pre-import row snapshot; rollback only those owned rows under a fresh claim.

Update `STATUS.json` with actual evidence first, then run
`python -B build_catalog.py --dashboard-only`. Use `deploy_runtime.py
--destination <HOME>/filmbrain/video_brain --evidence-dir
<absolute-evidence-directory> --mesh-script <absolute-agent_mesh.py> --mesh-agent
<your-live-id>` to copy and byte-check the 21 runtime/guidance files. Read back
the deployed brief/check output, hashes and live graph, not only the source tree.

The three files in `existing_filmbrain/` are a byte-bound versioned mirror of the
NMKC agent's existing core/geometry/machine corrections. They are not an install
of the entire filmbrain application. Coordinate with their live owner before
editing or restoring them. `evidence/peer_rows_updated.json` names the seven
selected live rows updated here; two older lesson corrections are recorded
separately. No broad craft reload is needed.

The main brain node is
`video_making_owner_contract_and_filmbrain_workflow_2026_09_05`. Update it through
`brain.py remember`; attach a changed handbook through `brain.py attach`, never
by replacing attachment bytes. Run `brain.py node` and `verify-attachments`,
read every part, then test a natural retrieval query. Export the exact node,
supersession marker and attachment manifest/bytes into the private repository.
Secret-scan staged files, make a small commit, pull with rebase and push; never
force-push. Give the producing agent the actual commit and live paths, and keep
delivery/acknowledgement separate from observed use on a completed movie.

The prompt review searched both UI histories and the redacted archive, then
checked available original sessions. **106 related-thread occurrences were
reviewed; 87 qualify as video instructions or immediate production followups.**
Nineteen topic detours do not count. Two old paste bodies were unavailable,
including one qualified occurrence. Thus the requested latest 100 complete
video prompts is **DATA INCOMPLETE**, not a fabricated hundred. Current direct
requirements and all recent substantive video corrections were readable.

No video is certified beautiful, accurate or fully watched by this extension's
unit tests. A receipt checker checks consistency of recorded evidence; a real
reviewer must actually inspect the identified media.

The 15:36 September 5 owner follow-up requires **actual GPU use** for suitable
production stages. This is stronger than permission alone. Read the GPU policy
node's `owner-active-gpu-video-use-20260905.md` supplement and the current compute
module. Record a real workload and measured GPU use, or the concrete reason a
stage is still CPU-only. Exact source: `provenance/OWNER_GPU_USE_20260905.json`.
