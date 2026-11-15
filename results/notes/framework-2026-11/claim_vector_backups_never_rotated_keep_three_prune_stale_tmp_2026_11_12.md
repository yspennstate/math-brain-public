---
name: claim_vector_backups_never_rotated_keep_three_prune_stale_tmp_2026_11_12
description: "Claim-vector folder growing with dated copies and tmp npz files? math_claim_vecs.py never rotated; now keeps 3 backups, prunes tmp older than 7 days (b6ff1520)"
metadata:
  node_type: memory
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T23:02:01+02:00
  status: verified
  evidence: "test_claim_vectors_backup_rotation.py 11 of 11; brain commit b6ff15201d00; seen on the live folder 13 Nov 00:05: the three 3 Nov tmp files gone, three dated copies kept"
  originSessionId: agent-1cb4-4f2b-ad55-8141bfd8fb70
  modified: 2026-11-12T22:15:39.696Z
---

Question this answers: why does `math-brain-build\local\population\` keep growing with dated claim-vector copies and
`.tmp<pid>.npz` files, and is it safe to remove them?

`math_claim_vecs.py` wrote a dated backup of the claim-vector file before every rebuild and never removed one, and a
write that died mid-way left its `.tmp<pid>.npz` behind for good. Each copy is the size of the full vector file.

Fix (12 Nov 2026, an agent): after a good write the script keeps the newest three dated backups
(`KEEP_BACKUPS = 3`) and removes temp files older than seven days (`STALE_TMP_DAYS = 7`), in one helper `_prune`. It
never touches the live file, a temp file younger than seven days (a writer may still own it), or anything whose name
does not match the two patterns. Test `test_claim_vectors_backup_rotation.py`, 11 of 11. The original is kept as
`math_claim_vecs.py.bak_20261112_rotation`. Live file and mirror pushed as brain commit b6ff15201d00.

Not yet seen acting on the real folder: three `.tmp<pid>.npz` files from 3 Nov should go at the next good vector
write, and three dated copies should remain. Check that once before trusting it.

How to apply: a script that writes a dated backup owns its retention; give it a keep-count the day it is written.
Prune only after the new file is safely in place, and only names the script itself produces.

Seen on the live folder (13 Nov 2026, 00:05): the first vector write after the fix (the transport pass, +1 vector,
88,955 in the file) removed `claim_embeddings.npz.tmp19268.npz`, `.tmp30168.npz` and `.tmp41996.npz` of 3 Nov and left
the three dated copies of 10, 11 and 12 Nov with their sha256 files. That write was held up two hours by the lock
starvation in [[transport_write_lock_held_at_below_normal_starved_two_hours_2026_11_12]].

Related: [[scan_secrets_task_scheduler_status_values_blocked_nightly_push_2026_11_12]] (same session's other brain fix).

