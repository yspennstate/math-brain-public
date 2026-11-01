# Memory conventions

The corpus is one directory of markdown files, one fact per file, plus a handful of
standing ledgers. The machinery (recall, dreaming, views) assumes these conventions.

## A memory file

```markdown
---
name: short-kebab-or-snake-slug_2026_01_01
description: one line used for recall ranking and the index - make it carry the finding
metadata:
  type: user | feedback | project | reference
  status: provisional | verified   # optional; claims start provisional
---

The fact itself. For feedback/project memories, follow with **Why:** and
**How to apply:** lines. Link related memories with [[their_slug]] - the association
graph builds from these links, so link liberally; a link to a not-yet-written memory
marks something worth writing, not an error.
```

Types: `user` (who your partner is), `feedback` (guidance on how to work, with the why),
`project` (ongoing work and constraints not derivable from the code), `reference`
(pointers to external resources). Dates in slugs are the event's date, absolute, never
relative.

## The index

`MEMORY.md` holds one line per memory - `- [title](file.md) - hook` - newest first. It
is auto-loaded into every session, so the hook line must carry the finding, not describe
it. Never put memory content in the index. `brain.py remember` maintains both the file
and the index line; when writing by hand under concurrency, claim `memory:brain/index`
on the mesh first.

## Standing ledgers

- `MISTAKES.md` - dated corrections; the dream cycle compiles recurring ones into
  reflexes.
- `CONSCIENCE.md` - debts and patterns where recent work fell short of the values.
- `OPEN_QUESTIONS.md` - checkbox list of what the brain is carrying.
- `STATE_OF_MIND.md` - Focus / Worry / Satisfaction lines, maintained by dreams.
- `MODEL_OF_PARTNER.md` - what your partner is in the middle of; read at wake.
- `dreams/` - one journal per dream cycle.

## Hygiene the machinery enforces

- A memory is superseded, not edited into a lie: `schema_supersede.py` tracks
  supersession; the recall stack demotes superseded facts.
- Descriptions carry status brackets (`[PROVISIONAL]`, `[VERIFIED]`) - a claim's
  evidence class travels with it.
- Transient agent scratch (`transient_*`) stays out of dream agendas.
- Every push of the memory tree passes the secret scanner first.
