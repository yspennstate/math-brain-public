---
name: fleet_resources_sampler_dash_s_hides_psutil_on_windows_2026_11_08
description: "[VERIFIED] Fleet resource sampler (fleet_resources.py) dies at once with exit 1 on the first machine: '-s' (copied from the second machine's launchd line) skips the user site where psutil lives; run pythonw without -s. On a loaded box one sample takes ~33 s and the process scan longer at BelowNormal; the local copy opts out of EcoQoS."
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T22:47:20+02:00
  status: provisional
  evidence: ""
---

8 Nov 22:1x-22:4x, an agent, owner order a fleet message (resources on every computer). Task FleetResourcesSampler on the first machine ran pythonw -s ...fleet_resources.py sample and exited 1 (LastTaskResult 1, no state dir); a foreground run showed ModuleNotFoundError psutil - psutil is in the user site, which -s disables. Fixed by dropping -s (22:38). Readings then came slowly (first 2 min after start; python start + process scan under 98 pct CPU); added SetProcessInformation(ProcessPowerThrottling) opt-out in fleet_resources.py, priority kept BelowNormal. Check liveness by samples-<UTC date>.jsonl growing under fleet_resources, not by the process existing.
