Current validated local draft: drafts/bundle_002.json. Current queued draft: ~/math-brain-inbox/w389/bundle_002.json. Its designated independent receipts are in AUDIT_RECEIPTS.jsonl, and its lifecycle is in BUNDLE_LIFECYCLE.json.

prepare_bundle.py and complete_packet.py are retained historical preparation helpers for the original pending-review version. Do not execute their main functions to recreate the final packet: they contain pre-audit metadata and the superseded relation wording. verify_packet.py imports only prepare_bundle.validate, without executing the old generator. refresh_reviewed_packet.py produced the reviewed version and preserves the older queued submission.

Run final mechanical checks with python -X utf8 verify_packet.py. These checks are separate from mathematical audit and do not integrate or probe the live store.
