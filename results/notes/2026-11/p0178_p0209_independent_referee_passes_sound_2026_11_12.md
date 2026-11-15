---
name: p0178_p0209_independent_referee_passes_sound_2026_11_12
description: "Outside referee passes on P0178 (Hasebe-Ueda stable unimodality counterexample) and P0209 (Aldous-Fill 4.30): both SOUND; P0178 had one false summary sentence (support as the dividing line), fixed"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T04:29:54+02:00
  status: verified
  evidence: "referee REPORT.md verdict SOUND for both; public 4beeb48a and 66cce3a3 match git ls-remote; ledger 68b4ac50 and e25d15c9"
---

Two more posted papers went through the outside referee on Mac mini 1 (Codex gpt-6.1-sol, high, normal speed, own programs, no repository code, no literature access). Both SOUND.

P0209 relaxation-time-normal-approximation (Aldous-Fill Open Problem 4.30): four-state construction and P(S_s <= 0) >= 1 - 4/s sound; 1,000,000-run checks at five (b,s) pairs all above 1 - 4/s; ten wording points fixed. Public 66cce3a3, ledger e25d15c9, Zenodo new version 10.5281/zenodo.24149781.

P0178 stable-unimodality-opposite-gaps (Hasebe-Ueda Conjecture 5.5, positive stable processes with finite 5/2-moment, classical and free): counterexample sound. Referee's own free grid (2,602 roots, residual < 3.0e-13) reproduces the zero-density image intervals and the positive densities at the atom images; H'(c) between 0.9558 and 0.9991 at 70 digits for alpha in {0.1,0.5,0.9}, t in {1,100}; classical grid has a strict valley. One sentence was WRONG as stated: "the dividing line is the support of mu and not its tail" - an exponential initial law (unbounded support) gives unimodal convolutions for every t. Replaced by what is proved: compact support suffices, no moment or exponential-moment condition does. Ten wording points fixed in public 4beeb48a; ledger 68b4ac50. SHA256SUMS.txt had 3 of 5 lines wrong before (CRLF working copy); rewritten from the index blobs.

What the referee cannot give: citation numbering and novelty (no literature access) - those rest on the citation hooks and the earlier checks. A remark that reads as an if-and-only-if is where a sound paper still carries a false sentence: test each summary sentence against the simplest unbounded or degenerate example.

Queue after these: P0211 (launched 04:05 local 12 Nov), P0220, P0341, P0456, P0458.


Related: [[p0253_p0033_p0032_independent_referee_passes_all_sound_2026_11_12]], [[p0452_p0243_independent_referee_passes_what_they_found_2026_11_12]], [[sha256sums_hash_the_stored_blob_not_the_crlf_working_copy_2026_11_12]].
