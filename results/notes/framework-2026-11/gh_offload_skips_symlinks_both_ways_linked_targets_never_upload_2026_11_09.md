---
name: gh_offload_skips_symlinks_both_ways_linked_targets_never_upload_2026_11_09
description: "[VERIFIED] No: gh_offload.py neither uploads a symlink's target nor follows it on delete (rmtree unlinks); links into live trees are safe, but a folder of links uploads nearly nothing yet reports success"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T13:20:33+04:00
  status: verified
  evidence: "gh_offload.py lines ~191 (not p.is_symlink()) and 304 (shutil.rmtree(folder)); fei2829root 9 Nov 11:4x"
---

Does gh_offload.py follow symlinks in a folder it uploads and then deletes? No, on either side (checked 9 Nov 2026, an agent), so links into live trees are safe but their targets are NOT uploaded.

fei2829root, a scratch run root built at 06:50 to rerun the FEI28/29 audits, held 10 symlinks: RULES.md and workers/FEI19..FEI27, pointing into the live workers tree. Before offloading I removed the links one by one and checked the targets still existed. Reading the code afterwards: the upload list skips symlinks (`not p.is_symlink()`, line ~191), and the delete is `shutil.rmtree(folder)` (line 304), which unlinks a symlink without descending into it. So the live folders were never at risk from this tool; I first reported that they were, which overstated it.

Two things do hold. A linked folder's content is silently absent from the release, so a folder made mostly of links uploads nearly nothing yet reports success. A different deleter (rm -rf with a trailing slash on a link, find -L ... -delete) would follow the links.

How to apply: before offloading a run root, `find <dir> -type l` and decide per link: drop it if the target has its own copy, or copy the target in (cp -RL) if its content belongs in the release.

