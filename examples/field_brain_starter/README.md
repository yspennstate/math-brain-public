# A starter brain for a field that is not mathematics

The rest of this repository builds a brain for mathematical research. Nothing in the method is specific to
mathematics. This folder is the smallest complete example for another field: twenty records kept by a small,
invented documentary studio, a search tool, and a ten-question test that measures whether the records help an agent.
Copy the folder, replace the records with your own, and you have the beginning of a brain for a company, a film
production, a lab or a support desk.

## What is here

| file | what it is |
|---|---|
| `memory/*.md` | twenty records, one fact per file, in the format of `framework/docs/MEMORY_CONVENTIONS.md` |
| `memory/MEMORY.md` | the index: one line per record, newest first, loaded into every agent session |
| `memory/MISTAKES.md` | dated corrections; the dream cycle turns a mistake that recurs into a reflex |
| `new_record.py` | write one record with its frontmatter, add its index line, and mark the record it supersedes |
| `recall.py` | search the records (BM25 over description and body; standard library only) |
| `ledger.py` | read and write the request ledger: list the open requests, record one, link a record that answers it, drop it |
| `claims.py` | let several agents share the store: claim a record or a piece of work before changing it, release it after; a second agent is refused and told who holds it |
| `check_store.py` | check that every record is indexed and every `[[link]]` and `superseded_by:` names a record that exists; run it after editing records by hand |
| `questions.json` | ten questions with graded answer phrases; one has no answer in the store |
| `three_arm.py` | the same questions asked three ways: with recall, with every record pasted in, with nothing |
| `dream/make_agenda.py` | builds the agenda a dreaming agent works from: mistakes without a rule, fresh records, superseded pairs, unchecked claims, open questions, unlinked records (see `dream/README.md`) |
| `dream/run_dream.py` | runs one dream with any agent command-line tool, keeps a backup, puts back deleted records, logs each section's count before and after; scheduling lines for Linux, macOS and Windows in `dream/README.md` |
| `hooks/wake_hook.py` | a session-start hook that gives the model the index and the newest mistakes once, so it knows what the store holds before anyone asks |
| `hooks/recall_hook.py` | a prompt hook for Codex or Claude Code that hands the matching records to the model before it answers (see `docs/codex-hooks-quickstart.md`) |
| `hooks/scar_hook.py` | a tool hook that warns the agent, once a session, when the command it is about to run resembles a recorded mistake |
| `hooks/write_back_hook.py` | a stop hook that asks the agent once to file a record when its turn ended on a lesson and nothing was written |
| `hooks/request_hook.py` | a prompt hook that writes each request into the request ledger and tells the model when the same request was asked before, and whether it was answered; under Stop with `--stop` it links the records the turn wrote to that request |

Everything in the records is invented. The studio, its films and its director do not exist.

## The records

Each record is one fact the studio paid to learn: a client decision, a licence term, a mistake and what it taught.
The four types do different jobs.

- `user` - who the partner is and how they want to work (the director reads reports on a phone; only the director
  approves a cut).
- `feedback` - a rule with its reason (clear music rights before picture lock, because a cue cleared after lock
  forced a re-edit). The **Why:** line is what lets an agent judge an edge case instead of obeying blindly.
- `project` - state that is not in any file (the harbour film ships at 12 minutes).
- `reference` - where something lives and what it says (the festival's delivery specification).

Two habits matter more than the format. A record that turns out wrong is superseded, not edited: the 18-minute plan
stays in the store, marked `superseded_by:` the 12-minute decision, so an agent that finds it also finds what
replaced it. And every claim carries its evidence class (`status: provisional` until it is checked), so a reader
knows how much doubt to carry.

## Asking the brain

```
python recall.py "how long should the harbour film be" --or "festival slot length"
python recall.py --id project_harbour_film_cut_to_twelve_minutes_2026_03_10
```

Give two or three wordings in one call; each is scored on its own and a record keeps its best score. Word them the
way a record would say it, not the way the question says it. A superseded record is pushed down and printed with
the slug that replaced it. When nothing fits, the output starts with `WEAK MATCH`: reword, and after a few tries
say the store does not have it rather than guessing. The same rules were measured on the mathematics brain
(`AGENTS_GUIDE.md`): two or three wordings in one call scored 86 of 100 against 76 with one wording a call, and when
the weak-match line showed, the answering card had been printed for only 4 of 21 questions.

If you keep a request ledger (`requests.jsonl` beside `recall.py`, `--requests`, or `MATH_BRAIN_REQUESTS`; see
`docs/prompts-as-nodes.md`), the requests you made earlier are part of the answer too: after the records, recall
lists up to three past requests that share at least half the words of one wording, with how often each was asked,
whether it is open or answered and the records linked to it. A request asked again after it was answered is
flagged. That is the most useful line in the block: someone asked, got an answer, and asked again, so the answer
did not land, and handing over the same record a third time will not help.

The ledger fills itself when `hooks/request_hook.py` runs on every prompt beside `recall_hook.py`. It writes the
same ask event, with the same id for the same words, that `math_brain.requests` writes, leaves out slash commands
and follow-ups of fewer than three content words, removes e-mail addresses and home paths, and stays silent unless
the request is already in the ledger. Then it tells the model how often it was asked and what answered it.

Wire the same script a second time under Stop, with `--stop`, and the ledger also learns what the work made: every
record created in `memory/` during the turn gets a `produced` link to the request the turn was on, and a short
follow-up keeps the request before it. It prints nothing. Whether a record answers the request stays a judgement
for the agent or the dream (`python ledger.py link <id> <record> answered_by`); a request with records produced
and no answer is the dream's cue to read them and decide.

Point the tool at your own folder with `--dir` or the `BRAIN_MEM_DIR` variable. The full brain's `brain.py recall`
adds an association graph (built from the `[[slug]]` links) and semantic search on top of the lexical score; this
starter keeps only the lexical part so it runs anywhere with no install.

## Measuring it

A brain is worth keeping only if it changes answers. `three_arm.py` asks every question three ways with the same
model:

- **brain**: the prompt carries the records recall finds for the question;
- **docs**: the prompt carries every record, unranked;
- **none**: the prompt carries the question alone.

```
python three_arm.py --write-prompts prompts/                  # read or send the 30 prompts yourself
python three_arm.py --model-cmd "your-model-cli --read-stdin"  # send each on stdin and grade the reply
```

On twenty records the docs arm should match the brain arm: everything fits in the prompt. The none arm should fail
everything except, with luck, the question the store cannot answer. The test becomes informative as the store grows
past what fits in a prompt, which is where the mathematics brain's three-arm test was run. By the night of 24
October, Claude agents on 988 items scored 95.4 percent with the brain, 82.0 with search over the research
repositories and no brain, and 18.9 for the model alone. On the items both of the first two arms finished in time
they were tied, so the brain's lead there is time: it finds in one call what the other arm finds in many searches
(`TESTS.md`, `docs/agency.md`, which also give the Codex figures, where the repositories came out ahead). Grading checks phrases and is crude on purpose; read the failing answers before
trusting a score. Write your own questions from things your agents actually got wrong, never from the records'
own sentences, or the test measures copying.

The weak-match line can be checked without a model. Run each question in `questions.json` through `recall.py -n 3`
and note whether the output starts with `WEAK MATCH` and whether the graded phrases appear in what it printed. On
the example store one question in ten printed the line, and it was the question the store cannot answer; each of
the other nine had its answer among the three records printed. In a store of your own, a weak-match line on a
question the store does answer means the records are worded differently from the way people ask, and the record
needs a sentence in the asker's words.

## Several agents at once

A brain is most useful when every agent on a team reads and writes the same store, and that is where stores get
damaged. Two things go wrong.

The first is the index. An agent that adds a record reads `MEMORY.md`, inserts its line and writes the file back; two
agents doing this in the same second each write back their own version, and one line is lost. `new_record.py` holds
a short lock on the index while it does this, so nothing needs to be done by hand. Twelve copies of `new_record.py`
started in the same second on a copy of this store all landed with the lock; with the lock removed, the same test
lost four or five index lines and three or four of the writers failed outright.

The second is two agents editing the same record, or doing the same piece of work twice. For that, an agent claims
what it is about to change:

```
python claims.py claim --agent ana --resource topic:pricing --purpose "move the ship date"
claimed topic:pricing  held by ana for 29 more min  (move the ship date)

python claims.py claim --agent ben --resource topic:pricing
REFUSED topic:pricing  held by ana for 29 more min  (move the ship date)
```

The refusal exits with code 3. The second agent then works on something else, or asks the holder, or waits; it does
not edit anyway. Claims expire (30 minutes by default; claiming again renews), so a crashed agent blocks no one for
long. `python claims.py list` shows who holds what, and `python claims.py selftest` runs the checks. Add one sentence
to the agents' standing instructions: "Before you change a record by hand or start a piece of work another agent may
also start, run claims.py claim; if it is refused, do not change that resource." `framework/mesh/` is the full
version, with heartbeats, mailboxes and handoffs, for a team of agents working all day.

## Growing it into a full brain

1. Keep writing records as the work happens: one fact, its reason, its date, links to related records. The index line
   carries the finding, not a description of it. `new_record.py` writes the file and the index line for you and
   refuses a link to a record that does not exist.
2. Install the hooks (`framework/bootstrap/`) so every agent session starts by reading the index and a few seed
   records, and so recall runs before work instead of after a mistake.
3. Run the dream cycle (`framework/dreaming/`) at night: it reads the day's records and transcripts, merges
   duplicates, links what belongs together, and compiles recurring mistakes from `MISTAKES.md` into reflexes that fire
   when an agent is about to repeat one.
4. When several agents work at once, start with `claims.py` (above); when they work all day and need to message and
   hand work to each other, move to the mesh (`framework/mesh/`).
5. Re-run the three-arm test whenever you change recall. If the brain arm stops beating the none arm, the change
   made the brain worse.

`docs/build-your-own-brain.md` walks through each step in full, and `docs/brain-in-an-afternoon.md` takes a company
from an empty copy of this folder to a measured brain in its first day.
