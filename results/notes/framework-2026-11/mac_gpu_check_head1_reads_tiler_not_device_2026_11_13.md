---
name: mac_gpu_check_head1_reads_tiler_not_device_2026_11_13
description: "Mac mini GPU looks idle (0%)? The usual ioreg | head -1 check reads the Tiler counter; MLX compute shows only in Device Utilization %"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T01:46:57+02:00
  status: verified
  evidence: "mini2 13 Nov 01:5x: head -1 line 0 x20 while Device Utilization 100 with MLX job running"
---

The Mac mini GPU check `ioreg -r -d 1 -w 0 -c IOAccelerator | grep -o "Utilization %\"=[0-9]*" | head -1` reads the
TILER counter, because ioreg prints "Tiler Utilization %" first. Compute work (MLX Metal kernels) does not use the
tiler, so a GPU running at full compute reads 0 on that line.

Seen 13 Nov 2026 ~01:50 on Mac mini 2: my MLX excited-walk loop was running and the head -1 line read 0 twenty times in
ten seconds, while the full counter list showed "Device Utilization %"=100, "Renderer Utilization %"=100,
"Tiler Utilization %"=0. On Mac mini 1 the three counters happened to agree (96/96/98) because its jobs drive the tiler
too, which is why the wrong line went unnoticed for days. Earlier "mini2 GPU 0%" readings taken with head -1 may have
been wrong in the same way; they cannot be re-checked now.

Use: `ioreg -r -d 1 -w 0 -c IOAccelerator | grep -o '"Device Utilization %"=[0-9]*'`, and sample it several times
(a single read lands between kernel launches).

Also learned the same hour: a GPU filler that starts a fresh python per batch and writes one JSON line per walker keeps
the GPU idle most of the time (each batch ran 0.2-1 s on the GPU). One long-lived process that loops on the GPU and
writes one summary line per batch keeps Device Utilization at 100. The job is ~/gpu_work/c0132_mc/ew_loop.py on mini2
(run.pid, STOP file), exit-time scaling of balanced excited walks M(1,1), M(1,2), M(2,1) in boxes; first numbers:
M(1,1) mean exit time from a box of side L grows 3.93-3.97x per doubling of L (diffusive, L^2).

