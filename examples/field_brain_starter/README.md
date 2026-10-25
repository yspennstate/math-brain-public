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
| `recall.py` | search the records (BM25 over description and body; standard library only) |
| `questions.json` | ten questions with graded answer phrases; one has no answer in the store |
| `three_arm.py` | the same questions asked three ways: with recall, with every record pasted in, with nothing |
| `dream/make_agenda.py` | builds the agenda a dreaming agent works from: mistakes without a rule, fresh records, superseded pairs, unchecked claims, open questions, unlinked records (see `dream/README.md`) |
| `hooks/recall_hook.py` | a prompt hook for Codex or Claude Code that hands the matching records to the model before it answers (see `docs/codex-hooks-quickstart.md`) |

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

## Growing it into a full brain

1. Keep writing records as the work happens: one fact, its reason, its date, links to related records. The index line
   carries the finding, not a description of it.
2. Install the hooks (`framework/bootstrap/`) so every agent session starts by reading the index and a few seed
   records, and so recall runs before work instead of after a mistake.
3. Run the dream cycle (`framework/dreaming/`) at night: it reads the day's records and transcripts, merges
   duplicates, links what belongs together, and compiles recurring mistakes from `MISTAKES.md` into reflexes that fire
   when an agent is about to repeat one.
4. When several agents work at once, add the mesh (`framework/mesh/`) so they claim what they change and read each
   other's state instead of colliding.
5. Re-run the three-arm test whenever you change recall. If the brain arm stops beating the none arm, the change
   made the brain worse.

`docs/build-your-own-brain.md` walks through each step in full.
