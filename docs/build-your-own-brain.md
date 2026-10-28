# Building a brain for your own field

This repository holds one brain, built for mathematical research: a store of results, proofs, attempts and mistakes that agents search while they work, and the tests that measure what it does for them. The same design carries over to other fields. A company can build one over its decisions, incidents and policies; a film studio over its craft and its failures; a lab over its experiments. This note says what the parts are, where each lives in this repository, and how to build them for a new field. How to connect an agent to the math store is in [AGENTS_GUIDE.md](../AGENTS_GUIDE.md); what the tests measured is in [TESTS.md](../TESTS.md). Before writing the first import, read [everything-is-a-node.md](everything-is-a-node.md): it says what has to become a record and how the records are linked, so that prompts, compactions, mistakes, files and code all end up in the store.

## 1. What the parts are

A brain here has five parts, and each can be built and tested on its own.

1. **A store.** One record per fact, with a type, a status and links. In the math store a record is a claim (a theorem, a lemma, a counterexample, an open problem, a failed attempt) together with the evidence for it and a verification state that says how far it has been checked. The code is in `src/math_brain/`, the exported store in `export/population/`.
2. **Recall.** A search that agents call while they work. It ranks records by shared words (BM25), by meaning (a sentence encoder) and by links, prints whole cards with their ids, and says `WEAK MATCH` when nothing fits well. The tools agents call are in `agent_tools/`.
3. **Notes served while the agent works.** Hooks that read what the agent is doing and put one or two relevant records in front of it before it acts: a past mistake in the same territory, a result it is about to rederive. Each note carries a line saying how far to trust it. The hook machinery is in `framework/hooks/` and `framework/dreaming/instinct_prime.py`.
4. **Dreaming.** A scheduled pass that runs while no one is working. It merges near-duplicate records, files the day's results as summaries, turns repeated mistakes into reflexes the hooks fire, grades yesterday's fires so that a reflex which keeps firing in the wrong place gets quieter, and checks that each part is still running. The code is in `framework/dreaming/` (`run_dream.ps1`, `dream.py`, `dream_prompt.md`, `instincts.py`, `fire_judge_nightly.py`, `hook_liveness.py`).
5. **Coordination.** When many agents share one machine and one store, they need to know who is changing what. `framework/mesh/` gives each agent an identity, lets it claim a file or a resource before writing, and passes messages and handoffs between agents. `framework/dreaming/task_checklist_hook.py` keeps a dated list of every request a person made and which agent took it.

The first two are what make an agent better at recall. The last three are what keep the store useful as it grows and as more agents use it.

## 2. What is in this repository

| Path | What it is |
|---|---|
| `src/math_brain/`, `tools/`, `tests/` | the math store: schema, import and export, verification states, recall, and its tests |
| `export/population/` | the store itself, as JSON lines (claims, cards, links, packets, mistakes, reflexes) |
| `agent_tools/` | the recall tools agents call, as a shell command or as an MCP tool |
| `framework/` | the general machinery the math brain grew out of, for any field (section 3) |
| `results/`, `papers/` | the work agents did with the brain, and the papers describing it |
| `TESTS.md`, `AGENTS_GUIDE.md`, `docs/agency.md` | the measurements, how to connect an agent, and the working loop that keeps it moving |

`framework/` is a copy of the general brain framework: the memory corpus and its recall, the hooks, dreaming, the agent mesh, the compute governor, a film-making brain (`framework/filmbrain/`) and an older copy of the math brain (`framework/mathbrain/`). The store code at the top level of this repository is the newer one, and the one the tests ran; use it for mathematics and read `framework/mathbrain/` as an example of how a field brain is laid out.

## 3. Building one for a new field

### Choose the unit

Decide what one record is. It should be small enough that a single card answers a single question, and it should carry its own status.

| Field | One record | Status it carries |
|---|---|---|
| mathematics | a claim, an attempt, a mistake | verified, checked by machine, sketched, refuted |
| a company | a decision, an incident, a policy, a customer commitment | who decided, when, still in force or superseded |
| film-making | a craft rule, a failure and its symptom, a recipe | measured on a real render, or authored and untested |
| a lab | an experiment, a protocol, a negative result | replicated, single run, abandoned |

A record that is wrong is marked superseded and linked to the record that replaced it. It is not deleted, because the next agent needs to know the old answer was tried.

### Fill it

Ingestion is deny by default: a source enters the store only when someone has decided it should. For a company that means the decision log, the incident reviews and the policy pages, not every chat message. For film-making, `framework/filmbrain/` shows both halves: an authored craft layer (about six hundred nodes on camera, light, editing, sound, narration and their failure symptoms) and an `ingest/` step that harvests what the local tools can do. Keep anything that is used to grade the brain (answer keys, held-out questions) outside every corpus the brain can search.

### Make it searchable

Start from the recall in `agent_tools/math_recall.py` and `framework/dreaming/brain.py`, and change only the card format to suit your records. Three choices made the largest difference in our measurements, and none of them is specific to mathematics: print whole cards with their ids rather than titles (83 of 100 questions against 34), let the agent ask in two or three wordings in one call (86 against 76), and print `WEAK MATCH` when the best card is a poor fit so that the agent rewords instead of answering from it. Lexical search does poorly on records made mostly of numbers and codes; if your records are like that, give agents a plain text search over the exported files as well.

### Connect the agents

Give agents the recall as a tool and a short paragraph on how to use it. [AGENTS_GUIDE.md](../AGENTS_GUIDE.md) has the configuration for Claude Code and Codex and the paragraph the tests used, and [codex-hooks-quickstart.md](codex-hooks-quickstart.md) shows the hook files for both runtimes, including the output format Codex requires. The wake step in `framework/hooks/` has an agent read the store's index and its own last notes at the start of a session, so it picks up the work where the last session left it instead of starting cold. [agency.md](agency.md) sets out the working loop that turns faster recall into more finished work: a next-step note on disk, leases on shared state, an audit before each report, and results written back to the store.

### Turn mistakes into reflexes

Write every correction down as a mistake record: what happened, the evidence, and the rule that would have prevented it. `framework/dreaming/instincts.py` compiles those records into reflexes, each with a pattern for when it should fire, and `instinct_prime.py` fires them from the hooks while an agent works. Two rules keep this from becoming noise. Fire at most two notes before an action, and back off once a note has fired in a session. And treat every note as a hint: on our tests, served notes helped where they matched the fault and made a wrong argument look legitimate where they did not, so the agent has to weigh each one against what is in front of it (`framework/docs/NOTES_ARE_HINTS.md`).

### Schedule the dream

Run `framework/dreaming/run_dream.ps1` nightly, through a hidden launcher so that no window opens. The dream reads the day's records and transcripts, writes summaries, merges duplicates, compiles new reflexes and grades a sample of the day's fires. Read the dream's log for the first week: a dream that stops committing its results or a part that stops firing is the most common way such a system decays without anyone noticing, and `hook_liveness.py` exists to catch it. [framework/dreaming/README.md](../framework/dreaming/README.md) describes the agenda's sections, the three kinds of dream (filing, connecting and the midday nap) and how to add a section for your own field.

### Measure it

Test the brain against two controls on the same questions: agents with the brain, agents with read access to the same documents but no brain, and the model alone. Count a timeout as a wrong answer, rerun a session that never reached the model, and keep the answer keys out of every searchable corpus. Our test of this design is in [TESTS.md](../TESTS.md). Its main lesson applies to any field. Where both agents finished, the agent with the brain and the agent reading the documents were about equally accurate; the brain's lead came from finishing in time, at about a quarter of the input tokens. A brain is worth building when the documents are too many or too scattered to read within the time an agent has, and that is easy to test before building much.

## 4. Where to start

The shortest path is [examples/field_brain_starter/](../examples/field_brain_starter/), which runs on Linux, macOS and Windows with nothing but Python: twenty example records, the recall tool, the hooks, a nightly dream and a ten-question test. [brain-in-an-afternoon.md](brain-in-an-afternoon.md) walks a team from an empty copy of it to a measured brain in a day, and [codex-hooks-quickstart.md](codex-hooks-quickstart.md) wires its hooks into Codex and Claude Code. Move to the full framework below once the starter has shown that the records help.

Once a first store exists, [brain-building/everything-to-brain-10-day-loop.md](brain-building/everything-to-brain-10-day-loop.md) is a prompt to hand an agent that can run on a schedule. It fires every ten minutes for ten days; each round brings new material in, links it, tests recall against the controls and leaves a checkpoint, so the store keeps growing without someone starting each step by hand.

```
git clone <this repository>
cd framework
python bootstrap/install.py --project-dir <a new home> --timezone <tz>          # read the plan
python bootstrap/install.py --project-dir <a new home> --timezone <tz> --apply
python scripts/smoke_framework.py                                              # does the copy work
```

`framework/bootstrap/README.md` goes through the install step by step: the corpus layout, the hook wiring, the seed records the wake step reads, and the optional parts (the dream, the compute governor, the agent mesh). `framework/docs/ARCHITECTURE.md` describes how the parts fit, `framework/docs/MEMORY_CONVENTIONS.md` the record format, `framework/docs/METHOD.md` the working rules, and `framework/docs/PORTING.md` what was removed when the framework was taken from a working system and what you have to supply yourself. The scripts assume Windows with Python 3.13 or later unless a file says otherwise; the store code is portable Python.

A small first version is enough to learn whether the brain helps: a store of a few hundred records, the recall tool, and the three-arm test on fifty questions. Add the hooks, the dream and the mesh once agents use the store every day.
