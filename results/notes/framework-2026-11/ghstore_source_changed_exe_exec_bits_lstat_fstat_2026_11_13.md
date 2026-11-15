---
name: ghstore_source_changed_exe_exec_bits_lstat_fstat_2026_11_13
description: "[VERIFIED] ghstore put says 'source changed: <x>.exe' on an untouched file? Windows lstat gives .exe mode 0o777, fstat 0o666; signature now masks exec bits"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T10:16:16+02:00
  status: provisional
  evidence: ""
---

13 Nov 10:1x, an agent. w682 (checks/BalancedBp.exe) and w676 (a build .exe) failed gh_offload with 'source changed' on files untouched for 28 days. Measured: os.lstat(p).st_mode 0o100777, os.fstat(open(p).fileno()).st_mode 0o100666; every other field equal. Python on Windows makes up exec bits from the extension (.exe .bat .cmd .com) for path stats only. ghstore compares signature(lstat) with signature(fstat), so every folder holding an .exe refused. Fix: signature() on nt returns st_mode & ~0o111 (backup ghstore.py.bak_execbits_1113); exe, text and dir controls match; tests 57 pass. Same family as the NTFS directory st_size false alarm: [[ghstore_source_changed_false_alarm_ntfs_dir_size_2026_11_13]]. status: verified
