# Heeding gates

A reflex that fires is not a reflex that is heeded. On the reference
deployment the detection layer works — scars surface at the moment of action,
and a change measured this month roughly doubled how often the mistake-linked
ones reach the top — while the same scar was read past three and four times in
a single session. Detection and compliance are different muscles, and the
second one was never instrumented.

Showing the warning again is the move that does not work. A signal repeated
without consequence trains its reader to skip it, and the repetition itself
becomes the habituation. Two gates address this from opposite ends.

## The acknowledgment gate (`brain/ack_gate.py`)

Covers the first encounter, and inverts the mechanism: rather than delivering
more text, it asks the agent to produce the connection. When a high-charge
act-hazard reflex fires on a command and no acknowledgment is on file for that
`(session, reflex)`, the host may hold the call once and ask for the command
to be reissued carrying an inert comment:

```
# heeded:<reflex_id> <one line: how the scar applies here, or why it does not>
```

The signature is validated mechanically — no model call, one round trip — and
the retry always proceeds. Even a thin rationale releases the hold: quality is
reviewed offline from `dreaming/ack_log.tsv`, never argued inline, because a
gate that debates the rationale is a gate agents learn to route around. An
agent that signs on its first attempt is never held at all, which is the
intended steady state.

The design bets that generation beats reception — that an agent which states
the lesson in its own words applies it, while an agent that merely receives it
does not. That bet is supported by the reference deployment's own trials but
is not yet established here.

## The repeat gate

Covers the other end: a scar already read past several times in one session,
on an action linked to a recent real failure, is a case where more prose has
demonstrably failed. There the correct intervention is a single hard stop
rather than another line of text. That gate lives in the upstream framework
(`upstream/brain-framework/dreaming/graph_fire/`); this repository carries the
acknowledgment half, which is the one that composes with a shadow-mode reflex
layer.

## Status

**Proven.** A held command can always be completed: the stop is claimed before
it is issued and never repeats for the same `(session, reflex)`; the
per-session cap holds; a signature releases and is banked; a rationale below
the minimum length does not count as one; ledger rows survive tabs and
newlines in the command; an unreadable ledger cannot stop work. Fourteen tests
in `tests/test_ack_gate.py` cover these against the real module.

**Partial.** Enforcement is opt-in per call. The default is advisory: the same
situation is recorded and allowed, so a deployment can measure its own
intervention rate before holding a single call. This mirrors `brain/reflexes.py`,
which stays shadow-mode pending a precision eval. Whether the default should
change is an operator decision, not a library default.

**Open.** Whether signed rationales stay substantive or decay into boilerplate
is unmeasured here. The ledger exists precisely so that a later review can
sample them; until that sampling has run on real sessions, the claim is that
the gate makes heeding *visible*, not that it makes heeding *real*.

**Open.** Reflex selection is inherited. This module decides whether an
already-chosen reflex needs an acknowledgment; it does not judge whether that
reflex should have fired. A noisy reflex layer would surface here as
acknowledgment fatigue, and the fix would belong upstream in selection.
