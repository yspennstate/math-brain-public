# A task checklist that every agent writes to

When one person runs many agents at once, two things get lost. The person forgets what they asked which agent, and
the agents do not know that another agent is already on the same request. We kept finding two agents rebuilding the
same file, and requests that nobody had picked up because each agent assumed another had.

The checklist is one shared, dated record of every request the owner makes of any agent, who is working on it, and
where it stands. It lives in the brain, next to the memories, so it survives every session.

## What an entry holds

- the request in the owner's own words, with the time they made it
- the agent it went to, and the runtime (Claude Code, Codex, a scheduled job)
- one line, written by the agent, of what it is doing about it
- dated progress notes worth the owner's attention
- a done mark with a one-line result, or blocked with the reason, or dropped
- a seen mark, which only the owner sets

The last two are separate on purpose. Done means the agent finished. Seen means the owner has looked at the result.
A long list of done but unseen entries is the owner's reading queue, and an agent must never mark one seen on the
owner's behalf.

## How entries get there

A hook on every prompt registers the owner's request under the session that received it. Short follow-ups ("ok do
it", "yes") attach to that session's open entry instead of creating new ones. The same hook prints what other agents
have open, so a session sees at once that the request it just received is already being worked on elsewhere.

The rest is the agent's job, by hand:

```
checklist.py working <id> "<one line: what you are doing>"
checklist.py note    <id> "<dated progress>"
checklist.py done    <id> "<the result in one line>"
checklist.py blocked <id> "<why>"
```

An agent that finishes without marking done leaves the list wrong, so a stop hook reminds it of its open entries
before the session ends, and the closing line of each report names the entry it closed.

## Answering "what did I ask?"

When the owner asks what the agents are doing, any session can answer from the checklist instead of guessing:
open entries first (who, doing what, since when), then done and not yet seen, with the result lines, then the
seen ones. Every entry carries the owner's words and the date, so the answer is checkable.

## Storage

Three files are enough: an append-only ledger of every change (one JSON line each, never rewritten), a state file
rebuilt from the ledger, and a Markdown view grouped into open, done and unseen, and seen, by day. The ledger is
the record. If the state file is ever damaged, it is rebuilt from the ledger.

## Outside mathematics

Nothing in this is specific to research. A studio running agents on many films, or a team running agents on many
tickets, has the same two problems, and the same three files and one hook solve them.
