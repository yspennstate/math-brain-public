# Dreaming in the starter brain

A brain that only collects records gets worse with time: old plans sit next to the decisions that replaced them,
mistakes are written down and made again, and new records never get linked to the old ones they touch. The dream is
the pass that keeps the store usable. It runs when nobody is working (at night, or between projects), reads what
changed, and writes back links, corrections and rules.

`framework/dreaming/` has the prompts and the runner the mathematics brain uses. Those prompts read an agenda but
do not build one, because the agenda depends on the field. This folder shows how to build one for a field that is
not mathematics.

## Run it

```
python dream/make_agenda.py
```

It reads `memory/` and writes `dream/DREAM_AGENDA.md`. The copy in this folder was built from the twenty example
records, so you can see what a dreaming agent receives before you write a single record of your own.

If you keep a request ledger (`requests.jsonl` beside `memory/`, or wherever `MATH_BRAIN_REQUESTS` points; see
`docs/prompts-as-nodes.md`), the agenda gains a seventh section, "Requests still waiting": the questions you asked
that nothing has answered yet, the ones asked more than once first, each with whether any record has been
produced for it. The dreaming agent links a record that answers one (`python ledger.py link <id> <record>
answered_by`, standard library like the rest), so the count of that section falls as the
dreams catch up with what you asked. The script folds the ledger itself and still needs only the standard library.

To run a whole dream, give `run_dream.py` any agent command-line tool that takes a prompt on stdin and can edit files:

```
python dream/run_dream.py --write-prompt dream/prompt.md                     # see the prompt, run nothing
python dream/run_dream.py --agent-cmd "claude -p --permission-mode acceptEdits"
python dream/run_dream.py --agent-cmd "codex exec --full-auto -"
```

It builds the agenda, copies `memory/` to `dream/backups/<stamp>/`, hands the agent the agenda with the three rules
below, puts back any record the agent deleted, rebuilds the agenda and writes `dream/logs/dream_<stamp>.md` with the
files changed and each section's count before and after. The count to watch is the line "Mistakes with no rule for
next time": a dream that leaves it unchanged did not do the most useful part of its job. Only one dream runs at a
time (`dream/.dream.lock`). Write paths in the agent command with forward slashes, also on Windows. The backups are
yours to prune once you have read the log.

## A night of dreams

One long dream is the wrong shape for a long night. The agent reads the agenda once, so what it fixes in its first
hour never reaches the agenda it is still working from, and a session that runs for hours is more likely to be cut
off with nothing written down. `dream_night.py` runs short dreams back to back instead, each from an agenda rebuilt
from what the last one wrote:

```
python dream/dream_night.py --agent-cmd "claude -p --permission-mode acceptEdits" --hours 5
python dream/dream_night.py --agent-cmd "codex exec --full-auto -" --hours 3 --rest 15 --max-cycles 6
```

Every cycle is an ordinary `run_dream.py` run, with its own backup and log. Between cycles the night rests
(`--rest`, 10 minutes by default). It stops at the deadline (a cycle starts only when `--min-cycle` minutes remain),
after `--max-cycles` cycles, when `dream/STOP` exists, when another dream holds the lock, or after two cycles in a row
that changed no file (`--idle-stop`). That last count is read from each cycle's own log, not from the agent's exit
status, because an agent can exit cleanly having written nothing. The night's summary is
`dream/logs/night_<stamp>.md`: one row per cycle with the files it changed and the agenda counts after it.

## Filing and connecting

A night of sleep is not one kind of sleep. Slow-wave sleep settles the day into what was already known; REM sleep,
later, links things from different places. In one prompt the two jobs compete for the same session: careful
correction and loose connection want different reading, and whichever comes first in the agenda tends to get the
time. So a dream can run as one of two stages:

```
python dream/run_dream.py --agent-cmd "..." --stage file       # sections 1-4 and 7: mistakes, fresh, superseded, provisional, requests
python dream/run_dream.py --agent-cmd "..." --stage connect    # sections 5-6: open questions and unlinked records
python dream/dream_night.py --agent-cmd "..." --stages file,connect
```

The filing pass links, corrects and writes rules, and writes no new ideas. The connecting pass links each unlinked
record to the record elsewhere in the store it bears on most, with a clause saying why, reads the newer records for
an answer to each open question, and may write up to three new records of what two records suggest together, each
`status: provisional`. With `--stages file,connect` the night alternates them, filing first, so the links are made
between settled records. Each cycle's log names its stage, and the night's table has a stage column. The default,
`all`, is the single dream described above. `framework/dreaming/dream_prompt_sws.md` and `dream_prompt_rem.md` are the
same split as the mathematics brain runs it.

## Run it every night

The dream works best when nobody is editing the store. Point the scheduler at the folder that holds `memory/` and
log the output somewhere you will read.

Linux, with cron (`crontab -e`), every night at 03:00:

```
0 3 * * * cd /path/to/your-brain && /usr/bin/python3 dream/run_dream.py --agent-cmd "claude -p --permission-mode acceptEdits" >> dream/cron.log 2>&1
```

macOS, with launchd: save as `~/Library/LaunchAgents/local.brain.dream.plist`, then `launchctl load` it.

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>local.brain.dream</string>
  <key>WorkingDirectory</key><string>/path/to/your-brain</string>
  <key>ProgramArguments</key><array>
    <string>/usr/bin/python3</string><string>dream/run_dream.py</string>
    <string>--agent-cmd</string><string>claude -p --permission-mode acceptEdits</string>
  </array>
  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>3</integer><key>Minute</key><integer>0</integer></dict>
  <key>StandardOutPath</key><string>/path/to/your-brain/dream/launchd.log</string>
  <key>StandardErrorPath</key><string>/path/to/your-brain/dream/launchd.log</string>
</dict></plist>
```

Windows, with Task Scheduler: create a daily task whose action is `python dream/run_dream.py --agent-cmd "..."`
with the brain folder as "Start in". Set it to run whether the user is logged on or not, or a console window opens
on the desktop at every run; the agent tool must then be signed in for that account.

A scheduler starts with a short `PATH`, so give the full path to `python3` and, if the agent tool is not found, to
the agent tool as well. Read the first week of logs: a dream that stops changing anything, or stops running, is the
usual way such a system decays without anyone noticing.

## What the agenda found in the example store

Every section found something, which is the point of the example:

- **Mistakes.** The 12 March mistake (an agent applied the 18-minute plan after the 12-minute decision) has no
  "How to apply" line in the record it links. A mistake without a rule for next time will be made again.
- **Superseded pairs.** `method_a_note_is_a_hint_not_an_order` links the superseded 18-minute plan but not the
  12-minute decision that replaced it. An agent that follows the link lands on the wrong plan, which is exactly the
  mistake above. The fix is one link.
- **Provisional records.** Five claims are unchecked, among them the client's warmer grade on the interviews, which
  stays provisional until the graded interviews are approved.
- **Open questions.** Festival first or online first is still open, and the festival delivery specification
  (31 March) is the newest record that bears on it.
- **Unlinked records.** Four records link nothing and nothing links them. The clipped interview audio and the
  rule about raw footage both belong next to the lighthouse interviews planned for April.

## Hand the agenda to an agent

Give the agent the agenda, the memory folder, and three instructions:

1. Work through the sections in order. Do not invent work the agenda does not list.
2. Every change is a new line or a new record with a date and a reason. Never delete a record; mark a wrong one
   `superseded_by:` the record that corrects it.
3. When a mistake has happened twice, write a reflex: one sentence that names the situation and the check to run.
   A reflex is the dream's most valuable output, because it fires during work, before the mistake.

Then rebuild the agenda. Sections that come back empty are the measure of a good dream; sections that come back
the same mean the agent read but did not write.

## Make it fit your field

The six sections are generic. What changes from field to field is what counts as a mistake and what counts as
evidence. A support desk might add a section for tickets reopened within a week; a lab might add one for results
that were never reproduced. Add a section when you can say what an agent should do with each item in it.
