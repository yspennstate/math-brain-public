---
name: a_chained_claim_failed_on_path_form_and_the_push_ran_2026_11_08
description: "[VERIFIED] 8 Nov 01:4x: a mesh claim in relative path: form was refused (exit 2) inside a chained command behind a grep, and push_paths.sh ran unguarded; third instance of the 2026-08-18 chained-claim scar"
metadata:
  type: feedback
  created: 2026-11-08
  created_at: 2026-11-08T02:06:40-05:00
  status: verified
  evidence: "this session's transcript: claim exit 2 'non-absolute path resource', commit e0a39dcc"
---

What happened (8 Nov 01:4x): `claim --resource path:private-repo/...` (a relative path) was refused with exit 2, "non-absolute path resource". A grep after it hid the refusal, and push_paths.sh ran in the same command and pushed a commit to the private repository. The target was my own new folder, so no peer was harmed. Run alone, the second claim printed the reason: the mesh wants an absolute path (C:\...) or a topic: name.

How to apply: run claim by itself, read its exit code, and only then mutate in a separate command. Claim file paths in absolute Windows form.

Same scar as [[chain_past_claim_two_instances_2026_08_18]].

Symptom as an agent meets it (SYMSWEEP1, 8 Nov, written from this note alone): A command that requests a mesh claim and then runs push_paths.sh pushes a commit even though the claim returned exit 2. Running the claim separately prints "non-absolute path resource" for a resource such as path:private-repo/....
