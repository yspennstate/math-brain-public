# Wiring a brain into Codex with hooks

A brain helps only if the agent reads it at the right moment. Asking the agent to "check the memory first" works
some of the time. A hook works every time: the runtime runs your script at a fixed point in the turn and puts what
the script prints in front of the model. Below are the Codex CLI format, a recall hook you can copy, and at the end
the differences in Claude Code, where the scripts are the same apart from the output format.

Tested with Codex CLI 0.160.

## Where hooks live

Codex reads `~/.codex/hooks.json`. One file holds every hook, grouped by event:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      { "hooks": [ { "type": "command", "command": "python3 /path/to/recall_hook.py", "timeout": 60 } ] }
    ],
    "PreToolUse": [
      { "matcher": "Bash|apply_patch",
        "hooks": [ { "type": "command", "command": "python3 /path/to/scar_hook.py", "timeout": 30 } ] }
    ],
    "Stop": [
      { "hooks": [ { "type": "command", "command": "python3 /path/to/write_back_hook.py", "timeout": 60 } ] }
    ]
  }
}
```

- `UserPromptSubmit` runs before the model sees a new request. Recall goes here.
- `PreToolUse` and `PostToolUse` run around a tool call. `matcher` is a regular expression over the tool name
  (`*` for every tool). Use them for warnings that should fire when the agent is about to act, such as "the last
  time someone ran this export, the preset had reset to 8-bit".
- `Stop` runs when the turn ends. Use it to remind the agent to write back what it learned.
- On Windows, add `"commandWindows"` next to `"command"`; Codex runs that one there.

## What the script receives

The hook gets one JSON object on stdin. The fields you will use:

| field | events | what it holds |
|---|---|---|
| `hook_event_name` | all | `UserPromptSubmit`, `PreToolUse`, ... |
| `prompt` | UserPromptSubmit | the user's text |
| `tool_name`, `tool_input` | Pre/PostToolUse | the tool and its arguments |
| `session_id`, `cwd` | all | which session, which directory |

## What the script must print

Codex passes a hook's output to the model only as JSON in this shape:

```json
{"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": "the text the model should see"}}
```

Plain text on stdout is discarded without an error. A hook that prints plain text runs, exits 0, writes its log,
and the model never sees a word of it. Check delivery in the session's rollout file, where the context appears as
a developer message, not in the hook's own log.

Keep `additionalContext` under about 10,000 characters. Longer text is cut wherever the limit falls. Put the most
useful lines first: five short, ranked records do more than fifty.

## Trusting a hook

Codex runs a new or changed hook only after you approve it. Run `/hooks` in a Codex session to review and trust
them. The approval is stored in `~/.codex/config.toml` under `[hooks.state]`, keyed by the hook's position and a
hash of its definition, so editing the command means approving it again. If a hook stops firing after an edit,
look there first.

## A recall hook you can copy

`examples/field_brain_starter/hooks/recall_hook.py` searches the starter brain's records with `recall.py` and hands
the top matches to the model before it answers.

```
python3 examples/field_brain_starter/hooks/recall_hook.py --selftest
```

prints what the model would receive for a sample request. To wire it in, add it under `UserPromptSubmit` in
`~/.codex/hooks.json` with its absolute path, approve it with `/hooks`, and ask Codex something the records answer
("what does the festival want for delivery?"). The answer should quote the 31 March delivery record.

The other two hooks in the example above are in the same folder. `scar_hook.py` runs before a tool call, scores
the command against the records of mistakes only, and adds one short warning when a scar matches well (at most two
scars, each once per session). `write_back_hook.py` runs when the turn ends: if the agent's last message reads like
a lesson and no record changed in the last two hours, it returns `{"decision": "block", "reason": ...}` once per
session, which both runtimes read as one more step, filing the record with `new_record.py`. Set
`BRAIN_WRITE_BACK=queue` and it appends the lesson to `memory/WRITE_BACK_QUEUE.md` instead of asking. Both keep
their per-session state in `hooks/.state/`, and each has a `--selftest`.

`request_hook.py` keeps the starter's request ledger and is wired twice, once per event:

```json
"UserPromptSubmit": [
  { "hooks": [ { "type": "command", "command": "python3 /path/to/request_hook.py", "timeout": 30 } ] }
],
"Stop": [
  { "hooks": [ { "type": "command", "command": "python3 /path/to/request_hook.py --stop", "timeout": 30 } ] }
]
```

At the prompt it writes the request into `requests.jsonl` and says so only when the same request was asked before.
At the stop it prints nothing and links each record the turn created in `memory/` to that request as `produced`,
so the dream finds the work already attached to the question that started it. The stop step knows a turn's
request from the prompt step's state file, so it links nothing for requests recorded by `math_brain.request_hook`
below; use one recorder per ledger. For Claude Code add `--runtime claude` to the prompt command.

Recall finds a record only when the request uses its words. `wake_hook.py` covers the rest: once per session it
hands the model the index (one line per record, newest first, cut to fit) and the newest lines of `MISTAKES.md`, so
the agent knows a delivery spec or a past mistake exists before anyone asks, and can read it by name. In Codex, put
it under `UserPromptSubmit` beside the recall hook; it speaks on the first prompt of a session and is silent after.

Three rules from running hooks like this every day:

1. **Fail silent.** A hook that crashes or hangs blocks every turn. Catch every exception, print nothing on error,
   and finish well inside the timeout.
2. **Say how far to trust each record.** Print its status (`verified`, `provisional`, `superseded`) next to it. A
   recalled note says that something similar happened before; it is not an instruction, and an agent given no
   status tends to obey it.
3. **Fire less.** A hook that injects records on every prompt teaches the agent to skip them. Return nothing when
   the best match is weak.

## The same hook in Claude Code

Claude Code reads hooks from `settings.json` (`~/.claude/settings.json` applies to every project). The events have
the same names and the stdin fields are the same. The output differs: for `UserPromptSubmit`, Claude Code gives
the model plain stdout, so the script prints its lines directly. `recall_hook.py --runtime claude` does that.
Claude Code also cuts one hook's output at about 10,000 characters, so the ordering advice holds for both.

The six starter hooks in `~/.claude/settings.json` (or `.claude/settings.json` inside one project), with your own
absolute paths. `python3 hooks/print_wiring.py --runtime claude` prints this block with the paths of your copy filled
in, and `--runtime codex` prints the one for `~/.codex/hooks.json`:

```json
{
  "hooks": {
    "SessionStart": [
      { "hooks": [ { "type": "command", "command": "python3 /path/to/hooks/wake_hook.py --runtime claude", "timeout": 30 } ] },
      { "matcher": "compact",
        "hooks": [ { "type": "command", "command": "python3 /path/to/hooks/compaction_hook.py --runtime claude", "timeout": 30 } ] }
    ],
    "UserPromptSubmit": [
      { "hooks": [ { "type": "command", "command": "python3 /path/to/hooks/request_hook.py --runtime claude", "timeout": 30 } ] },
      { "hooks": [ { "type": "command", "command": "python3 /path/to/hooks/recall_hook.py --runtime claude", "timeout": 60 } ] }
    ],
    "PreToolUse": [
      { "matcher": "Bash|Edit|Write",
        "hooks": [ { "type": "command", "command": "python3 /path/to/hooks/scar_hook.py", "timeout": 30 } ] }
    ],
    "Stop": [
      { "hooks": [ { "type": "command", "command": "python3 /path/to/hooks/request_hook.py --stop", "timeout": 30 } ] },
      { "hooks": [ { "type": "command", "command": "python3 /path/to/hooks/write_back_hook.py", "timeout": 60 } ] }
    ]
  }
}
```

`compaction_hook.py` keeps each context compaction as a record. When the context fills, the runtime replaces the
conversation with a summary the agent wrote: what it was asked, what it finished, what it still owes. Claude Code then
starts the session again with source `compact`, which the matcher picks; the hook reads the newest summary from the
transcript, files it in `memory/` as a provisional project record linked to the session's previous compaction and to
the request it was working on, and prints one line naming it. Codex has no compaction event, so there it sits under
`UserPromptSubmit` and saves a compaction it has not seen yet. `--backfill` reads old transcripts once.

The tool names differ between the runtimes (`Bash`, `Edit`, `Write` here; `Bash`, `apply_patch` in Codex), so the
matcher does too. `scar_hook.py` and `write_back_hook.py` print JSON in both runtimes and need no flag. Under
`SessionStart`, `wake_hook.py --runtime claude` speaks when a session starts and again after a compaction or
`/clear`, when the earlier copy of the index has left the context. Claude Code
does not ask you to trust a hook, but it reads `settings.json` when a session starts: open a new session after an
edit. Run `/hooks` to see what it loaded, and check delivery in the session transcript, where an injected context
appears next to the turn, rather than in the hook's own output.

## The request hook from the math brain

`math_brain.request_hook` (see [prompts-as-nodes.md](prompts-as-nodes.md)) is one more `UserPromptSubmit` hook. It
shows the agent the earlier requests that look like the new one, with what they produced, so a question asked last
week is not worked from scratch again. It needs the package importable (`pip install -e .` in the repository) and
the ledger's path in `MATH_BRAIN_REQUESTS`. On Linux and macOS the variable can go in the command itself:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      { "hooks": [ { "type": "command",
                     "command": "env MATH_BRAIN_REQUESTS=/path/to/requests.jsonl MATH_BRAIN_REQUESTS_RECORD=1 python3 -m math_brain.request_hook --codex",
                     "timeout": 30 } ] }
    ]
  }
}
```

That is `~/.codex/hooks.json`. For Claude Code, put the same entry in `settings.json` and drop `--codex`, since
Claude Code takes plain stdout. On Windows, set `MATH_BRAIN_REQUESTS` (and `MATH_BRAIN_REQUESTS_RECORD`) as user
environment variables and keep only `python -m math_brain.request_hook` in the command. To see what the model will
get, pipe prompts in by hand. A new ledger is empty and the hook prints nothing until a request is recorded, so
record one first and then ask something close to it:

```
echo '{"prompt": "is every group of prime order cyclic?"}' | MATH_BRAIN_REQUESTS=requests.jsonl MATH_BRAIN_REQUESTS_RECORD=1 python3 -m math_brain.request_hook
echo '{"prompt": "are groups of prime order always cyclic?"}' | MATH_BRAIN_REQUESTS=requests.jsonl python3 -m math_brain.request_hook
```

The second command prints the first request, its match score (0.43 here) and whether it is still open.

Record from one runtime only. A request is keyed by its text, so if two runtimes record into the same ledger, a
prompt that reaches both is counted as asked twice, and the nightly pass lists it among the repeated requests.
