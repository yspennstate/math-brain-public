# Stop hooks that keep an agent on its work

A brain can tell an agent what it was asked and what is still open. That does not stop the agent from ending its
turn. In our deployment the most common way work went unfinished was not a wrong result: an agent wrote a tidy
summary of where things stood and stopped, with the tasks still open and nothing waiting on anyone. It happened most
often right after a compaction, when the agent had just been handed a summary of its own session and read it as a
final report.

Notes added at session start cannot fix this, because they only add context. The agent still decides to stop. A stop
hook can: in Claude Code, a hook on the `Stop` event that prints `{"decision": "block", "reason": "..."}` refuses the
stop and hands the reason to the agent as its next instruction. Codex has the same event.

We run two of these. Both are short, and most of their code is about when not to fire.

## After a compaction

The first time a session tries to stop after compacting, the hook checks the shared task checklist (see
[task-checklist.md](task-checklist.md)) for entries still open under that session's agent id. If there are any, it
blocks the stop with a reason that names them:

> You compacted at 21:24 and are about to stop. A recap is not the end of the job: these are still open under your
> id: ... Pick up your next-step line and keep working on them. Stop only if every one is done, or is waiting on an
> answer or on a job that is already running and will notify you; then say which in one line.

The rules that keep it from becoming a nuisance:

- Once per compaction. The hook keys each compaction by the id of its boundary record in the transcript and writes
  that key down before doing anything else, so the same compaction is never used to block twice.
- Never while `stop_hook_active` is set. That flag means the agent is already continuing because of a stop hook;
  blocking again is how loops start.
- Only when the compaction is recent (under six hours, and in the last few megabytes of the transcript) and only when
  the checklist holds open entries for this session. A finished agent is never blocked.
- A cheap way out. The reason itself tells the agent it may stop with one line saying what each task is waiting on.
  A finished agent pays one short turn.
- Silent on any error. A stop hook that throws must allow the stop. A hook on the stop path should never be the
  reason a session cannot end.

## Timed work

The second hook is for work the owner asked to run for a set time ("keep working on this for the next ten hours").
While a campaign is armed, it blocks every stop and restates the campaign's goal. The parts that matter are the ways
out, narrowest first:

1. One session: a marker file named with that session's id silences the hook for that agent only. This is the right
   lever when the owner wants to talk to one agent without stopping the rest.
2. The whole fleet: one marker file turns the campaign off for everyone; deleting it turns it back on.
3. Done: a file the agent or the owner writes when the goal is met.
4. A cap and a deadline: a maximum number of consecutive blocks per session, and a hard end time, so an unattended
   hook cannot run forever.

We learned to keep the per-session switch the hard way. An earlier request to disconnect one session was carried out
by editing the shared settings file, which silenced every agent on the machine.

## Building one for your own brain

1. Decide what "open work" means, in a place the hook can read without the model: a checklist, a queue file, a
   next-step note on disk. If the hook has to guess, it will block finished agents.
2. Read the hook's input: the session id, the transcript path and `stop_hook_active`. Return nothing to allow the
   stop; print the block decision with a reason to refuse it.
3. Write the reason as an instruction the agent can act on at once: the open items by id, where its next step is
   written down, and the one-line way to stop legitimately.
4. Record every block (time, session, which items were open). Then read some sessions after a block and check that
   the agent went back to work rather than writing a second summary.
5. Before reading anything into that record, separate real sessions from test runs. Benchmark workers stop far more
   often than people's sessions and will swamp the count.

Nothing here is specific to mathematics. Any team that runs agents on long jobs, whether films, tickets or
experiments, loses work the same way, and the same two hooks catch it.
