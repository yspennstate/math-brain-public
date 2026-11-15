# The orders behind one loop, paraphrased

The loop recorded in this folder ran under three standing orders at once, each repeated as a prompt every three
minutes for ten days. They are given here in paraphrase, because the original wording is private and the paraphrase
is what the agent actually worked from: every order was first restated as one line on the task checklist
(`framework/docs/TASK_CHECKLIST.md`), and later ticks read that line, not the prompt.

| order, paraphrased | how it was turned into work |
|---|---|
| Find and fix the bugs in the brain framework, make it more robust and faster, and measure brain against no brain with Codex. | Bugs came from the framework's own logs (hook errors, hung jobs, failed pushes), each fixed with a test and recorded as a memory. The measurement became the preregistered tests in `ab_tests/`. |
| Keep improving the brain and working on open problems, and keep the idle GPUs busy. | Every tick checks each machine's GPU. An idle card gets the next open-problem job that fits it; the samplers in `CHANGES_2026-11-15.md` exist because of this order. |
| Publish the framework's methods, tools, records and mathematics, with proper credit to the people whose work they rest on. | The pages in this folder, `results/CREDITS.md`, `framework/docs/CHANGES_2026-11-15.md`, and the open-problem folders. |

## What a repeat means

A repeated order is not a new task. The checklist hook attaches each repeat to the open entry it matches, so a
ten-day order produces one entry with dated notes rather than thousands of entries. When a repeat arrives, the
agent reads its NEXT line and continues, and the order's text matters only when it differs from the last one.

## Where the orders conflict

Orders compete for the same hour. The rules used here:

- A later order wins over an earlier one on the same subject, and the checklist entry is updated to say so.
- Safety and cost rules (no windows popping up, no paid continuous-integration runs, nothing private published) are
  not traded against speed.
- When two orders need the same machine, the job that is already running keeps it. A new job waits in the queue and
  is never started by stopping someone else's.
- A choice that only the owner can make (spending money, a rule change, deleting the only copy of something) goes to
  the owner as a single question, and work that does not depend on the answer continues.

## What is left out

The orders also asked for reports, emails and drafts addressed to particular people. Those are private and are not
reproduced. Test answer keys are also kept off GitHub, because the questions are reused.
