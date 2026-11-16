---
name: swiftc_bridging_modulemap_redefinition_vfs_overlay_mac1_2026_11_15
description: "[VERIFIED] swiftc on Mac mini 1 fails 'redefinition of module SwiftBridging'? The Command Line Tools ship two modulemaps for it; build with -vfsoverlay that maps bridging.modulemap to an empty file"
metadata:
  node_type: memory
  status: verified
  type: reference
  modified: 2026-11-15T12:04:10.985Z
---

Measured on a Mac mini, 15 Nov 2026, building ust_metal.swift (Metal UST sampler for P0133).

- Symptom: `swiftc -O ust_metal.swift -o ust_metal` stops with
  `/Library/Developer/CommandLineTools/usr/include/swift/module.modulemap:13:8: error: redefinition of module 'SwiftBridging'`.
  The Command Line Tools install has both `module.modulemap` and `bridging.modulemap` in that folder, each defining the module.
- Fix that worked, without touching /Library (no sudo, nothing system-wide): a VFS overlay that hides one of the two.
  `vfs.yaml`: `{ "version": 0, "case-sensitive": "false", "roots": [ { "type": "file", "name": "/Library/Developer/CommandLineTools/usr/include/swift/bridging.modulemap", "external-contents": "<dir>/empty.modulemap" } ] }`
  with `empty.modulemap` an empty file, then `swiftc -O -vfsoverlay vfs.yaml ust_metal.swift -o ust_metal`.
- The binary it built gave the validation draws of the ust-torus-dual-theta v1.1 release (see [[p0133_ust_torus_superbase_law_rotation_invariant_2026_11_14]]).
- What would change this: a Command Line Tools update that removes the duplicate; then the plain swiftc line works and the overlay is harmless.
