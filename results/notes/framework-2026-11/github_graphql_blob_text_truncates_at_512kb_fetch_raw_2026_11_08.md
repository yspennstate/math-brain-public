---
name: github_graphql_blob_text_truncates_at_512kb_fetch_raw_2026_11_08
description: "GraphQL Blob.text silently cut at 512,000 bytes (isTruncated); a file of exactly 512000 bytes / a sha mismatch on a big repo file -> fetch raw, check byteSize; blobless clone for path checks"
metadata:
  type: reference
  created: 2026-11-08
  created_at: 2026-11-08T04:55:46+02:00
  status: verified
  evidence: "8 Nov 04:4x: GraphQL read of navigation/cards.jsonl gave 512000 bytes (sha bf3b70a1); raw fetch gave 976748 bytes, sha fa141412 = MANIFEST.json; blobless clone of 2fd6ca9c listed 111204 files"
---

GitHub GraphQL `Blob.text` stops at 512,000 bytes and says so only in `isTruncated`. On 8 Nov 2026 a check of math-brain-public's navigation/cards.jsonl (976,748 bytes) came back as exactly 512,000 bytes. nav_query.py then refused it against MANIFEST.json's sha256, which looked like a broken publish. It was not: the raw file at raw.githubusercontent.com matched the manifest (fa141412...).

**Why:** a cut file does not look cut. JSONL ends mid-line, its byte count is a round number, and the check that catches it reads as a repo fault.

**How to apply:** any GraphQL blob read asks for `text isTruncated byteSize`. When `isTruncated` is true, fetch raw.githubusercontent.com/<owner>/<repo>/<ref>/<path> (public repos, no API quota) and assert len == byteSize. A file of exactly 512,000 bytes is a cut file until proven otherwise. To check many paths against a big repo, a `git clone --filter=blob:none --no-checkout --depth 1` plus `git ls-tree -r --name-only HEAD` beats batched GraphQL: 1,968 paths batched gave HTTP 502, while the clone listed 111,204 files in seconds.

