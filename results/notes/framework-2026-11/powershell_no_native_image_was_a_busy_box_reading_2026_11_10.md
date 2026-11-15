---
name: powershell_no_native_image_was_a_busy_box_reading_2026_11_10
description: "slow sense says powershell_no_native_image / run ngen elevated? It was false: the native images are present and loaded; the probe named it from start CPU > 0.8 s alone (18 of 806 busy-box samples). slow_probe.py now reads the image file from disk (10 Nov). Do not grep the folder for the full assembly name - folder names are truncated"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T04:22:35+02:00
  status: verified
  evidence: "806 probe samples; loaded-module listing of a fresh powershell.exe; three controls on ps_native_image_present"
---

10 Nov 2026 04:1x, an agent, first hour of the 10-hour brain upgrade loop (the author's 03:54 order).

What was wrong. slow_probe.py named `powershell_no_native_image` whenever one bare PowerShell start used more than 0.8 s of CPU. The advisory told the reader to run bin\ngen_powershell.vbs elevated for twenty minutes. The images were there the whole time: `C:\Windows\assembly\NativeImages_v4.0.30319_64\System.Manaa57fc8cc#\<ver>\System.Management.Automation.ni.dll` exists, and a fresh powershell.exe lists it among its loaded modules with ConsoleHost, Security and Commands.Management. Over the last 806 probe samples the start CPU has median 0.39 s and p90 0.56 s; 18 samples (2.2 pct) were over 0.8 s, median 0.94 s. Those are a full box, not a missing image (a missing image measured 1.2-1.8 s on 15 Sep).

The fix. `ps_native_image_present()` in slow_probe.py lists the native image folder; the verdict is appended only when CPU is over 0.8 s and the file is absent. The state row carries `ps_native_image` on such samples. Controls: real box True, the image folder removed from the listing False, an unreadable folder None (no verdict). Live file and the canonical copy in 12_cognitive_architecture/dreaming are byte-identical, sha256 65d798e0b999b283.

How to check next time. Do not grep the native image folder for "System.Management.Automation": the folder names are truncated ("System.Manaa57fc8cc#"), so the grep counts zero while the image is there. Ask a running PowerShell: `(Get-Process -Id $PID).Modules | ? ModuleName -match 'Automation.*ni.dll'`.

Seen on the way, not changed: in those same samples a bare PowerShell start waits a median of 19 s wall at 0.39 s CPU. That is the run queue of a full box. Every hook that starts PowerShell pays it; python -s helpers do not.

Same hour, the other unowned hook_liveness item: the math transport queue (11 rows, oldest 52 h) was reviewed by hand - 3 ingested, 7 dismissed, the stale symmetric-FEI claim corrected to 4.650431. `math_transport.py correct` writes only the ledger; the queue row for a STALE IN STORE item closes at the next scheduled scan, once the supersedes edge exists (lines 1125-1140), so status shows it queued for a few minutes after a successful correct.

What would change this: a Windows servicing run that really drops the images. Then the file check returns False and the verdict fires as before.

