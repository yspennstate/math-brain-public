---
name: mac_numpy_matmul_warnings_spurious_dream_vectors_finite_2026_11_09
description: "[VERIFIED] No: dream.py matmul divide-by-zero/overflow warnings are spurious on the second machine (numpy 2.2.3 Accelerate); vectors finite, result matches float64 to 1.4e-6"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T09:50:42+04:00
  status: provisional
  evidence: "live sidecar memory_embeddings.b24a0a59...npz, 50,553x384; check run 9 Nov 09:51"
---

No (9 Nov 09:51): the "divide by zero / overflow / invalid value encountered in matmul" warnings dream.py prints at line 319 are not bad numbers. Checked on the live sidecar (memory_embeddings.b24a0a59...npz, 50,553 x 384 float32): 0 non-finite values in the vectors, max |x| 0.645; a 1024-row block times all rows raised 3 such warnings yet held 0 non-finite results (range 0.352 to 1.000001), and matched the same product in float64 to 1.4e-6. The float64 product raises the warning too. numpy 2.2.3 on the second machine's Apple Accelerate BLAS flags these spuriously.

**Why:** a dream log full of matmul warnings looks like corrupted similarity scores; it is not.
**How to apply:** ignore these warnings in dream.py and other matmuls on this machine unless a result itself is non-finite; check the output, not the warning. Script: the 20-line vec_check.py idea (load the sidecar named in .embedding_current.json, count non-finite, compare with float64).


Related: [[dream_matmul_warnings_are_accelerate_blas_flags_vectors_clean_2026_11_07]] - the same finding from 7 Nov; this is a re-check on the 8 Nov sidecar (50,553 rows) that confirms it, not a new result. Read that one first.
