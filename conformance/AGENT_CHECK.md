# A prompt to give your agent

Paste the block below into Claude Code or Codex, opened at the root of your checkout. It has the agent check the
install, the hook wiring in its own runtime, and what reaches it on a prompt, and report what it found. It changes
nothing without asking you first.

```text
Check that the math brain in this repository is installed and wired into you. Do not edit any file or setting
without asking me first; report what you find.

1. Run `python --version` (or `python3 --version`). It must be 3.11 or newer. Use that interpreter below.
2. If local/population/brain.sqlite3 is missing, run `python tools/import_store.py --out
   local/population/brain.sqlite3` and confirm both digest-failure counts in its last lines are 0.
3. Run `python conformance/verify_install.py --report conformance_report.json` and give me its last line. If it
   says FAIL, read the FAIL lines and the section "When it fails" of conformance/README.md and tell me which case
   applies. The first search on a new install can take minutes; wait for it rather than starting it again.
4. Run one search the way you would use it while working:
   `python agent_tools/math_recall.py "spectral gap of a reversible Markov chain" --or "relaxation time mixing time"`
   and compare its shape with conformance/logs/*_two_wordings.txt: numbered hits with ids, kind and score, a
   'matched' line, a 'found by wording' line, and a --id hint. Then read the top card whole with --id.
5. Fire the prompt hook by hand:
   macOS/Linux: echo '{"hook_event_name":"UserPromptSubmit","session_id":"check1","prompt":"what is the spectral gap of a reversible Markov chain"}' | python agent_tools/math_sense.py
   Windows PowerShell: '{"hook_event_name":"UserPromptSubmit","session_id":"check1","prompt":"what is the spectral gap of a reversible Markov chain"}' | python agent_tools/math_sense.py
   It should print one JSON object with hookSpecificOutput.additionalContext, as in
   conformance/logs/*_hook_served.txt. An everyday prompt ("how to repot an orchid") should print nothing.
   If the math prompt also prints nothing, the hook wrote why to ~/.claude/dreaming/mathbrain_silence_harness.tsv
   (create that folder first and fire it again). `budget_exhausted_before_ranking` means this machine is slower
   than the hook's 30-second budget: tell me how long it took.
6. Find your own hook configuration and say whether math_sense.py is wired on UserPromptSubmit:
   - Claude Code: ~/.claude/settings.json (or .claude/settings.json in this project), key hooks.UserPromptSubmit.
   - Codex: ~/.codex/hooks.json, key hooks.UserPromptSubmit. Codex runs a hook only after it is trusted: the
     person must open /hooks in Codex and approve it. Codex also uses only JSON output from a hook, which is
     what math_sense.py prints.
   Give me the exact command line it runs and check that the Python and the path in it exist.
7. If it is wired, tell me whether a block from the math brain appeared in the context of my message. If it is
   not wired, show me the entry you would add, with absolute paths, and wait for my answer.

End with a short table: Python version, store present, verify_install verdict, search shape matches the logs,
hook by hand served/silent as expected, hook wired in this runtime, hook block seen in context.
```

## The entry for the hook

Both runtimes take the same shape. Use absolute paths and the full path of a Python 3.11 or newer:

```json
{"hooks": {"UserPromptSubmit": [{"hooks": [{"type": "command", "timeout": 60,
  "command": "/full/path/to/python3 -X utf8 /full/path/to/repo/agent_tools/math_sense.py"}]}]}}
```

In Claude Code this goes into `~/.claude/settings.json` (merge with any hooks already there). In Codex it goes into
`~/.codex/hooks.json`, and then the person approves it under `/hooks`. The hook finds the store at
`local/population/brain.sqlite3` beside `agent_tools/`; set `MATHBRAIN_STORE` if yours is somewhere else.

Run one search by hand (step 4 above) before the first session with the hook. The first search builds the
prepared recall state, which can take minutes, and a hook that hits that build inside its time limit stays silent.

The hook is a source of leads, not the way to search: in an earlier test it stayed silent on 85 of 100 recall
questions. Tell the agent to call `math_recall.py` itself, as section 3 of AGENTS_GUIDE.md describes.
