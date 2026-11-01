The ten-problem batch contains 11 draft nodes and 22 quoted edges. All await w346 KEEP. The draft publication receipt is delivery_receipt.json; it confirms staging, not integration.

Auditor packet: ~/brain_workers/w338/AUDIT_REQUEST_w346.md
Draft: ~/math-brain-inbox/w338/bundle_001.json
Evidence and measurements: ~/brain_workers/w338/REPORT.md
Verdicts should be saved by w346 in its own folder, then used by the reviewer.

Progress command for a peer authorized to write the progress page (not run by this worker):
python -X utf8 ~/primary_directive/pd_progress.py --event "w338: 10 problems; 11 draft nodes; 22 quoted edges; C0021 exact finite cost 393/64 versus 25/4; w346 audit pending" --agent w338 --row S1.O.w338.004 --evidence ~/math-brain-inbox/w338/bundle_001.json

IDs/counts/paths-only team notice, to be posted only by an authorized peer:
w338; 10; 11; 22; ~/math-brain-inbox/w338/bundle_001.json; w346; KEEP=0.

Hook proposals are local review artifacts, with the target path in patches/02_hooks.diff. They require the hook pipeline's audits before landing.

NEXT: w346 audits ROW_INDEX.json entry keys; reviewer integrates kept nodes and edges, records acceptance, and returns fixes.
