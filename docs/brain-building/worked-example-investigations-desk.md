# A worked example: a brain for an investigations desk

[build-your-own-brain.md](../build-your-own-brain.md) describes the parts of a brain and how to build them for a new
field. This page builds one, for an invented company whose investigators trace payments across public blockchains,
using only the starter in [examples/field_brain_starter/](../../examples/field_brain_starter/) and Python. Every
command below was run on a clean copy of the repository and the output shown is what it printed. The company and its
cases are invented.

The desk is a good test of the method because its knowledge is the kind that gets lost: rules learned from a report
that went wrong, limits that changed after a case, labels that go stale. None of it is in the code that does the
tracing.

## 1. An empty brain

```
python examples/field_brain_starter/new_field.py inv_brain --field "the investigations desk of a company that traces payments across public blockchains"
```

```
made .../inv_brain: 23 files copied, an empty store, an empty questions.json
check_store.py: clean
next: write ten records with new_record.py and ten questions in questions.json (README.md has the steps)
```

The new folder has every script and hook from the starter and no records. Work inside it from here on.

## 2. The first records

Write the first records by hand, from what the desk has already paid to learn. A `feedback` record is a rule with
its reason and what to do next time; the reason is what lets an agent handle a case the rule did not foresee.

```
python new_record.py feedback "Stop a trace at an exchange deposit address and open a records request" \
  --why "Funds that reach a custodial exchange are pooled; following outputs past the deposit address attributes other customers' coins to the case." \
  --apply "When a hop lands on a labelled exchange deposit address, end that branch, record the address and amount, and draft the records request."

python new_record.py feedback "Treat a coinjoin output as a branch point, not a continuation" \
  --why "A March report followed one equal-value coinjoin output as if it were the suspect's and named an unrelated wallet." \
  --apply "At an equal-output mixing transaction, split the trace into every output and carry each with a probability, never a single path."

python new_record.py project "Case reports go to clients as a hop table plus a one-page summary" \
  --body "Clients asked for a table of every hop (txid, block height, amount, confidence) and one page in plain words; graphs are an appendix."

python new_record.py reference "Exchange deposit labels live in the team's label table, refreshed weekly" \
  --body "The label table maps addresses to services with a source and a date; a label older than ninety days is checked before it ends a trace."

python new_record.py user "The lead investigator signs every report that names a person"
```

Each call prints the record's name:

```
wrote .../memory/stop_a_trace_at_an_exchange_deposit_address_2026_03_02.md
name for --link: stop_a_trace_at_an_exchange_deposit_address_2026_03_02
```

Use that printed name, or the same name without its date, wherever another command asks for a record. The name is
built from the first words of the description, so it is shorter than the description and cannot be guessed from it
reliably; copy it. A name that matches no record stops the command with `no record named ...` and exit code 1, and
nothing is written.

## 3. A rule that changed

In January the desk stopped every trace at 25 hops. In April, after two cases where the money reached an exchange at
hop 31 and hop 44, the limit went to 60. The old record stays in the store, marked as replaced:

```
python new_record.py project "Traces stop at 25 hops unless the client pays for a deeper pass" --date 2026-01-20
python new_record.py project "Traces stop at 60 hops; the 25-hop limit cut off two recoveries" \
  --supersedes traces_stop_at_25_hops_unless_the_client \
  --body "Raised after two cases where the funds reached an exchange at hop 31 and hop 44." \
  --link stop_a_trace_at_an_exchange_deposit_address
```

An agent that searches for the old limit finds it, and finds what replaced it in the same line (next section). If
the old record were edited in place or deleted, the next person to ask why the limit is 60 would have no answer.

Link records that depend on each other. The label-age rule depends on both the label table and the stopping rule:

```
python new_record.py feedback "Check a label's age before it ends a trace" \
  --why "A ninety-day-old label ended a trace at an address the exchange had stopped using." \
  --apply "Before stopping at a labelled address, read the label's date in the label table; older than ninety days, confirm it first." \
  --link exchange_deposit_labels_live_in_the_team_s --link stop_a_trace_at_an_exchange_deposit_address
python check_store.py
```

```
orphan  treat_a_coinjoin_output_as_a_branch_point_2026_03_09.md: no [[link]] in or out, so a walk along links never reaches it
9 records: 0 error(s), 0 warning(s), 4 orphan(s)
```

An orphan is not an error. It is a record nothing links to yet, and linking orphans is part of the nightly dream's
work (`dream/README.md`).

## 4. Asking

```
python recall.py "how many hops do we follow" --or "trace depth limit"
```

```
(score 2.2)
== traces_stop_at_60_hops_the_25_hop_2026_04_02  [project, provisional]
Raised after two cases where the funds reached an exchange at hop 31 and hop 44.
...
(score 0.7)
== traces_stop_at_25_hops_unless_the_client_2026_01_20  [project, provisional]  SUPERSEDED by traces_stop_at_60_hops_the_25_hop_2026_04_02
```

The current limit comes first and the old one is printed with the record that replaced it. A question the store
cannot answer says so instead of returning the nearest card as if it fitted:

```
python recall.py "what is our retention period for case files"
```

```
WEAK MATCH: nothing here fits the question well. Reword it, or answer that the store does not have it.
```

Wording matters. Records are found by the words they contain, so ask the way a record would put it. "mixing
transaction equal outputs" finds the coinjoin rule at the top (score 7.9); a question in the client's words may not.
That is why recall takes two or three wordings in one call.

## 5. Connecting the agents

Print the hook block for Claude Code or Codex with this folder's paths and paste it into the settings file:

```
python hooks/print_wiring.py
```

From then on, each session starts with the index and the newest mistakes (`wake_hook.py`). Before the agent answers,
`recall_hook.py` puts the matching records in front of it. Before a command that resembles a recorded lesson,
`scar_hook.py` warns it once: it scores the command against the `feedback` records and the records `MISTAKES.md`
links, so a trace command that mentions a coinjoin transaction can bring up the branch-point rule before it runs. When a turn ends on a lesson with nothing filed, `write_back_hook.py` asks once for a record.
[codex-hooks-quickstart.md](../codex-hooks-quickstart.md) has the details for each runtime.

## 6. Measuring before building more

Write ten questions an investigator actually asked last month into `questions.json`, with the phrases a correct
answer must contain, and include one the store cannot answer. Then:

```
python three_arm.py --model-cmd "<an agent command line that reads the prompt on stdin>"
python three_arm.py --write-prompts out/     # or write the 30 prompts to files and send them by hand
```

It asks every question three ways: with recall, with every record pasted into the prompt, and with no records. On a
store of ten records, pasting them all in is cheap and will do about as well as recall. The point of the test is to
run it again at a few hundred records, where pasting everything no longer fits and an agent reading the documents
runs out of time. On the mathematics store the brain's lead came from finishing in time, at about a quarter of the
input tokens, rather than from better answers where both finished ([TESTS.md](../../TESTS.md)).

## 7. What to add for this desk

Three things in this field that the starter does not do:

- **Records from cases, not chats.** Import the closed-case reviews (`import_docs.py <folder> --dry-run`, then
  without `--dry-run`), and promote to `feedback` only the lessons that held up on a second case.
- **Labels as references with dates.** The label table changes weekly. Keep it outside the store and keep one
  `reference` record that says where it is, how fresh it must be, and who maintains it.
- **The mistakes file.** Every report a client or the lead sends back goes into `memory/MISTAKES.md` with its date,
  what was wrong and the rule that would have caught it. The dream turns a mistake that recurs into a reflex that
  `scar_hook.py` fires.
