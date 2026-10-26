# A brain for a company in one afternoon

This is the short road: an empty folder at lunch, a brain your agents search by the evening, and a number that
says whether it helps. It uses the starter in `examples/field_brain_starter/`, which needs Python and nothing
else. [build-your-own-brain.md](build-your-own-brain.md) covers the full design; this page is the first day.

The example is an invented software company with a billing and support team. Every command below was run on an
empty copy of the starter, and the output shown is what it printed.

## 1. Copy the starter and empty it (twenty minutes)

```
cp -r examples/field_brain_starter acme_brain
cd acme_brain
rm memory/*.md
printf '# Memory index\n' > memory/MEMORY.md
printf '# Mistakes\n' > memory/MISTAKES.md
```

Then decide what one record is. For a company the useful units are a decision, an incident and what it taught, a
policy with its reason, and a pointer to where something lives. A record holds one fact. If a sentence needs
"and also", it is two records.

## 2. Write the first thirty records (two hours)

Take them from the places where the company already wrote down something it paid to learn: the decision log,
incident reviews, the policy pages, the handful of answers new staff always ask for. Leave chat history out.
A brain fed everything returns everything, and the agent learns to skim past it.

`new_record.py` writes the file, its frontmatter and its index line:

```
python new_record.py feedback "Refunds over 500 dollars need a second approver" \
    --why "a refund went to a closed account and could not be recovered" \
    --apply "ask for the second approver before you issue it"
python new_record.py project "The Q2 pricing change ships on 1 June, not 15 May" \
    --body "Moved after the billing migration slipped."
python new_record.py reference "Enterprise contract template lives in the legal drive under Templates/2026" \
    --link refunds_over_500_dollars_need_a_second_approver_2026_03_02
```

Each command prints the file it wrote. The name is the description cut to a few words plus the date it was
written (these examples were written in March, so yours will carry today's date); use that name wherever a
command asks for another record, as `--link` does here.

The `--why` line matters more than it looks. An agent that knows why the rule exists can handle the case the rule
did not foresee, and one that only knows the rule cannot.

When a fact changes, write the new one and point it at the old:

```
python new_record.py project "The Q2 pricing change ships on 15 June" \
    --supersedes the_q2_pricing_change_ships_on_1_june_2026_03_05
```

The old record stays, marked `superseded_by:`. An agent that finds the 1 June date also finds that it moved,
which is better than not finding it and later hearing it from someone who remembers.

Every record starts `provisional`. Pass `--verified` only for facts someone has checked against the source.

## 3. Ask it questions (twenty minutes)

```
python recall.py "when does the pricing change ship" --or "Q2 pricing date" -n 2
```

```
(score 2.3)
== the_q2_pricing_change_ships_on_15_june_2026_03_09  [project, provisional]
The Q2 pricing change ships on 15 June

Related: [[the_q2_pricing_change_ships_on_1_june_2026_03_05]].

(score 0.8)
== the_q2_pricing_change_ships_on_1_june_2026_03_05  [project, provisional]  SUPERSEDED by the_q2_pricing_change_ships_on_15_june_2026_03_09
Moved after the billing migration slipped.
```

Now ask something the store words differently:

```
python recall.py "who approves a large refund"
WEAK MATCH: nothing here fits the question well. Reword it, or answer that the store does not have it.
```

The record says "second approver" and "500 dollars", not "approves" and "large". The search counts shared words,
so the fix is a second wording in the record's own terms:

```
python recall.py "who approves a large refund" --or "refund second approver"
(score 3.2)
== refunds_over_500_dollars_need_a_second_approver_2026_03_02  [feedback, provisional]
```

This is the habit to teach the agents: two or three wordings in one call, phrased the way a record would phrase
it, and when `WEAK MATCH` survives a few tries, say the store does not know. On the mathematics brain, two or three
wordings per call answered 86 of 100 questions against 76 for one wording per call (`AGENTS_GUIDE.md`).

Asking for something the store does not hold should look like this:

```
python recall.py "what is our vacation policy"
WEAK MATCH: nothing here fits the question well. Reword it, or answer that the store does not have it.
```

## 4. Measure it before you trust it (forty-five minutes)

Write twenty questions in `questions.json`. Take them from things your agents or new staff actually got wrong,
not from the records' own sentences, or the test only measures copying. Include two or three questions the
store cannot answer, marked `"absent": true`; the right reply says so.

```
{"id": "q01", "question": "Can support issue a 700 dollar refund alone?",
 "any_of": [["no", "second approver", "two people"]]}
```

Check the plumbing first with a "model" that returns its prompt. The docs arm should pass every question, since
every record is in the prompt:

```
python three_arm.py --model-cmd "python -c \"import sys; print(sys.stdin.read())\""
```

Then run it with your model's command line, which reads the prompt on stdin:

```
python three_arm.py --model-cmd "your-model-cli --read-stdin"
```

You get three scores: **brain** (recall's results in the prompt), **docs** (every record pasted in) and **none**
(the question alone). With thirty records, docs and brain should tie, because everything fits in a prompt. The
none arm should fail almost everything. The brain arm starts to pull ahead once the store is too big to paste.
On the mathematics store (988 questions) the brain arm answered 95.4 percent, search over the same repositories
without the brain 82.0, and the model alone 18.9 (`TESTS.md`).

Read the failing answers yourself. The grader only checks for phrases.

## 5. Put it in front of the agents (thirty minutes)

Two pieces. First, a paragraph in the agent's standing instructions (`AGENTS.md` for Codex, `CLAUDE.md` for
Claude Code):

```
Before you answer a question about how we work, or start a task we may have done before, search the
company brain: python <path>/recall.py "<wording 1>" --or "<wording 2>". Read the records it prints.
A superseded record tells you what changed; use its replacement. If it says WEAK MATCH after two
rewordings, say the brain does not have it. When you learn something we will need again, write it with
new_record.py, with the reason.
```

Second, the hooks. `hooks/wake_hook.py` runs once when a session starts and gives the model the index and the
newest mistakes, so it knows what the store holds before anyone asks. `hooks/recall_hook.py` runs before the model
sees each request and hands it the records that match, so the agent gets them even when it forgets to ask.
`python hooks/recall_hook.py --selftest` shows what the model would receive.

Recall answers questions; it does nothing when the agent is about to act. `hooks/scar_hook.py` runs before each tool
call and compares the command with the records of mistakes and rules only. Here it is on the starter's own records,
which belong to a small film studio, with a command an agent short of disk space might reach for:

```
echo '{"session_id": "s1", "tool_name": "Bash", "tool_input": {"command": "rm -rf footage/harbour/raw"}}' | python hooks/scar_hook.py
```

The model receives, before the command runs:

```
[brain] This action resembles something that went wrong before. A scar is a question, not an order: check
whether it applies here before you go on.
- feedback_ask_before_deleting_raw_footage_2026_03_27 [verified]
  Never delete raw footage to free disk space without two checked copies (sizes and checksums compared) and the
  director's yes.

  **Why:** the camera cards are the only source; a finished edit cannot be re-cut without them.
  **How to apply:** when disk runs short, report it and list candidates; delete only what was approved and verified.
```

`ls footage/harbour` gets nothing, and the same scar fires at most once a session, so the warning stays rare enough
to be read. For your company, the records that earn this are the ones written after something broke: the refund
issued twice, the migration run against the live database. `hooks/write_back_hook.py`, at the end of the turn, asks
the agent to file a lesson it has just stated and not written down.
[codex-hooks-quickstart.md](codex-hooks-quickstart.md) shows where each hook goes in Codex and in Claude Code.

## 6. The first night (ten minutes to set up)

```
python dream/make_agenda.py
```

This writes `DREAM_AGENDA.md`: mistakes with no rule yet, the week's new records and what they might contradict,
superseded pairs and the records that still link the old one, provisional records waiting for a check, and records
with no links. Give the agenda to an agent at the end of the day and let it work through it: link, merge, verify,
turn a repeated mistake into a rule (`dream/README.md` says what to do with each section).

Once that works by hand, let `dream/run_dream.py` do the whole night with any agent command-line tool that reads a
prompt on stdin:

```
python dream/run_dream.py --agent-cmd "claude -p --permission-mode acceptEdits"
```

It backs up `memory/` first, puts back any record the agent deleted, and writes a log with each agenda section's
count before and after. It also runs `check_store.py`, which lists any record the night left out of the index and
any `[[link]]` or `superseded_by:` that names a record nobody wrote; the run exits 1 when it finds one, so a
scheduler can flag the night. Run `python check_store.py` yourself after editing records by hand. `dream/README.md`
has the cron, launchd and Task Scheduler lines for running it every night.

## When more than one agent writes

If several agents share the store from the first day, two of them will sooner or later change the same thing.
`new_record.py` already locks the index while it adds a line, so records written at the same moment are all kept.
For hand edits and shared pieces of work, have each agent claim first:

```
python claims.py claim --agent support-bot --resource record:refunds_over_500_dollars_need_a_second_approver_2026_03_02
```

A second agent asking for the same record is refused (exit code 3) and told who holds it and why. The starter's
README, under "Several agents at once", has the rest.

## After the first week

By now the store will have outgrown pasting, and the questions will show where recall misses. That is the point to
move to the full framework in `framework/`: the association graph and semantic search on top of word matching,
mistakes compiled into reflexes that fire before an agent repeats one, and the mesh for many agents writing at once.
[build-your-own-brain.md](build-your-own-brain.md) walks through it, and [agency.md](agency.md) describes the
working loop that keeps an agent moving with the brain behind it.
