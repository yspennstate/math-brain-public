# Suggestions

Ideas for prompts, loops and uses of the brain, newest first. Each comes with a prompt you can
paste. New ones are added as they come up.

## 9 November 2026

- Run two loops on one project from two angles. One loop builds ("keep working on X"), the other
  checks ("every 20 minutes, test what the first loop made and write down what is broken"). The
  checker's notes go into the brain, so the builder reads them on its next round.

  `/loop fire this every 20 minutes for the next 2 days. test what was built on <project> since
  the last round, write each problem you find to the brain, and do not fix it yourself.`

- Ask for the summary of your own prompts. Your prompts are the best record of what you want. Every
  few days, have an agent read them and turn them into tasks.

  `read the last 50 prompts I gave agents, group them by project, and list what is done and what
  is not. put the open ones on the task list.`

- Make a loop end with an email. A long loop is easier to trust if it reports. Add to the prompt:
  "when you finish a piece, send me a two-line email with what changed".

- Turn a correction into a rule. When you correct an agent, ask it to write the correction into
  the brain so no agent makes the same mistake again.

  `write what I just corrected into the brain as a rule, with what went wrong and how to check for
  it next time.`

- Keep a task list in a GitHub repository. Several agents on several computers can all read one
  file. Each agent marks what it took and what it finished; you read one page to see everything.

- Give every long job a folder with ORDER.md and NEXT.md. It costs nothing and means a crash, a
  closed window or a full context loses at most one step.

- Use a loop to keep the disk free. "every 10 minutes, upload finished files to github, check
  each copy, then delete the local one." The brain records where each file went.

- Let the brain test itself. A brain that is never tested drifts. Once a week, run the same
  questions with and without the brain and keep the scores.

  `/loop fire this every 10 minutes for the next 2 days. build 30 questions about <project> whose
  answers are in the brain, run them with recall and without it, and write down where the brain
  helped and where it did not.`

- Start the agent in the right folder. The hooks look for the brain from your home folder; a
  project agent started deep in a subfolder still gets them, but its files land there.

- When a loop is not producing anything, read its NEXT line. If the line has not changed in an
  hour, the loop is stuck on one step; tell it to split the step or skip it.
