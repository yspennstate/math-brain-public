---
name: zsh_unquoted_leading_equals_word_aborts_rest_of_line_2026_11_08
description: "[VERIFIED] Scar (8 Nov): why did a command stop with '=== not found'? zsh equals expansion: an unquoted word starting with = (echo ====) is a fatal error that drops the rest of the line, ; commands too; quote separators"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:18:42+04:00
  status: verified
  evidence: "zsh -c 'echo ====; echo rc=$?' prints only the error; bash prints ===="
---

Why did a shell command stop halfway with "(eval):1: === not found" and exit 1? zsh's equals expansion: an unquoted word that starts with "=" is replaced by the path of the command named after it (=ls becomes /bin/ls). `echo ====` asks for a command called "===", there is none, and zsh treats that as a fatal expansion error. Everything after it on the line is dropped, `;`-separated commands included.

Measured on this machine, 8 Nov 13:2x, zsh -c:
- `echo ====; echo rc=$?` prints only "zsh:1: === not found". The second echo never runs.
- `printf '%s\n' ====` fails the same way.
- `echo "===="` prints ====. So does bash.

How it bit (8 Nov 13:13, DIAG2 setup): I used `echo ====` as a separator between two reads in one Bash call. The second half, a grep of run_audit.py, never ran, and the hook flagged a traceback that was really the first file's text.

How to apply: quote separators (`printf '%s\n' '----'` or `"===="`) or use dashes. This is not the =() process substitution. Any unquoted word with a leading "=" is at risk. Same family as [[zsh_echo_backslash_math_card_grep_counts_nothing_2026_11_06]] (zsh echo differs from bash) and [[rc_after_command_substitution_in_echo_reads_its_status_2026_11_05]].

Status: verified (reproduced three ways above, plus the bash control).

