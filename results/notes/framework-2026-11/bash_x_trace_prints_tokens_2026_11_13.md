---
name: bash_x_trace_prints_tokens_2026_11_13
description: "bash -x on a script holding a GitHub token prints the token (xtrace expands vars; grep -v TOK misses it); debug with echo steps or logs, never -x"
metadata:
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T21:51:38+02:00
  status: verified
  evidence: "13 Nov 21:4x publish.sh xtrace printed the gh token line"
---

Running `bash -x` on a publish script that reads a GitHub token into a variable prints the token: xtrace expands variables in every traced line, so `[ -n "$TOK" ]` shows up with the token value in it. Filtering the trace with grep -v TOK does not catch that line, because the variable name is gone after expansion.

Seen 13 Nov 2026 21:4x (an agent): the token was printed into a session transcript while debugging publish.sh for the I0003 paper. It was not pushed anywhere, but session transcripts are offloaded to the private brain repo, so the token should be treated as exposed and rotated (the author's call: `gh auth refresh` / revoke the OAuth token).

**Why:** a debug trace is output like any other; secrets in it reach the transcript and then GitHub.
**How to apply:** to see where a token-holding script stops, use `set -e` plus `echo step N` lines or read the log files it writes (create.log, push.log), never `bash -x`. If a trace is unavoidable, `set +x` around the token lines.

