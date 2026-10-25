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
