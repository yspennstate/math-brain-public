# Suggestions

Ideas for prompts, loops and uses of the brain, newest first. Each comes with a prompt you can
paste. New ones are added as they come up.

## 9 November 2026

- Have a second agent check a result before it goes public. The agent that produced a result is
  the worst judge of it. A second agent that reruns the work without reading the first one's code
  catches most of what slips through.

  `before this goes public, start a second agent that has not seen your work. have it redo the
  check on its own and tell me whether it agrees.`

- Tell the loop what finished looks like. "Keep working on X" can run forever. If you know the
  end state, say it, and say what to do when it is reached.

  `/loop fire this every 5 minutes for the next 10 days. keep working on <the project> until <what
  done means>. when it is done, check it once more, send me a short report and stop.`

- Keep one dated line per round. A loop that writes one dated line each time it runs leaves a
  diary you can read in a minute: what it did at 3 a.m., where it got stuck, when it finished.

  `at the end of every round, add one dated line to <the log file> with what you did and what is
  next.`

- Ask the agent to say back what it understood before a long job. Ten days of work on a
  misunderstanding is expensive. A short note in its own words, before it starts, catches the
  mistake while it is cheap.

  `before you start, write me three or four lines on what you understand I want and how you plan
  to do it. then begin.`

- Ask whether the machine is being used. A loop can sit on a computer that is half idle because
  nothing told it to take more. One question finds out.

  `is the processor, memory and graphics card on this computer being used fully right now? if
  something sits idle, tell me what could use it.`

- Run a loop whose only job is to find what got stuck. Long pipelines leave things behind: a file
  made but never uploaded, a job that died halfway. A sweep that looks for those is cheap and
  catches what the working loops miss.

  `/loop fire this every 5 minutes for the next 10 days. make sure everything we made is finished
  and in its place, that nothing got stuck halfway, and fix anything that did.`

- Put a second computer to work. An old laptop or a desktop that sits idle can run its own agent
  with the same brain. Ask the first agent to check what the other one is doing and hand it a job
  when it is free.

  `check how busy <the other computer> is. if it has free memory and processors, give it <the
  job>, and tell me what it is running.`

- Tell agents to check before they start. With several loops running, two of them will sooner or
  later pick the same piece of work. One sentence in the prompt prevents it.

  `before you start a piece, check whether another agent already has it. if one does, take a
  different piece and say which.`

- Ask for one lesson per finished piece. A long loop learns things nobody writes down. Ask it to
  save one line to the brain each time it finishes something, so the next agent starts from there.

  `each time you finish a piece, save one line to the brain: what worked, what did not, and what
  you would do differently.`

- Give the loop a fallback for when it runs out of something. A daily upload limit, a usage cap or
  a credit balance will stop the main job partway through the day. Say what the loop should do
  instead, so the rounds are not wasted.

  `/loop fire this every 5 minutes for the next 10 days. keep making <the things>. when <the
  limit> is used up for the day, finish what is in hand and spend the rounds on <the other job>
  until it resets.`

- Have every round read a shared inbox first. If you or another agent leave a note in one file,
  each loop picks it up within five minutes without you visiting its window.

  `at the start of every round, read <the inbox file>. act on anything new meant for you before
  your own next step, and mark it as read.`

- Ask for the bottleneck, not the next step. When a project feels slow, an agent can usually find
  the one thing holding the rest up.

  `find what is slowing <the project> down the most right now, fix that one thing, and tell me in
  two lines what it was and what changed.`

- Point a loop at a task list, not one task. If you keep a list of your top priorities in a file or
  a repository, one loop can work through it for days and pick up whatever you add.

  `/loop fire this every 5 minutes for the next 10 days. keep working on the top 10 highest
  priority tasks in <the task list>. mark what you take and what you finish.`

- Use a sweeping loop for things that pile up unfinished. Some work is never one job: results that
  never got written up, files that were made but never uploaded. A sweep finds the next one each
  round, finishes it, and moves on.

  `/loop fire this every 5 minutes for the next 10 days. find the next result we have that is not
  written up yet, write it up and publish it, then go to the next one.`

- Chain one prompt onto another. A loop can wait for something else to be done first. Say what it
  waits for, and what it does after.

  `/loop fire this every 5 minutes for the next 10 days. once the tests described above are on the
  task list, start building and running them.`

- Ask for a short summary in a fixed shape. When you come back to a terminal after hours away, a
  long report is hard to read. Ask for two parts: what you asked for, in your words, and what has
  been done so far.

  `give me at most 8 short lines in two parts: what I told you to do, in my words with the times,
  and what you have done so far. no tool names.`

- Tell one agent to pass a message to all of them. When you change a rule, you do not have to
  visit every terminal. Ask one agent to write it where every agent reads at the start of each
  prompt (a shared inbox file or a hook), and to say which agents saw it.

  `tell all the other agents: <the new rule>. put it where every session reads it, and tell me
  which agents acknowledged it.`

- Give the agent a rule for when space runs short. A loop that runs for days will sooner or later
  meet a full disk or low memory, and then it sits and waits. Tell it in advance what to do.

  `if the disk or memory gets low, don't stop. find files that already have a checked copy on
  github, delete those, and carry on with the task.`

- Ask every report to say which task it answers. With five terminals open you will not remember
  which prompt a report belongs to. Put one line in your global instructions file:

  `end every report with one line naming the task it answers, in my words, with the time I asked.`

- When you are not watching, ask for questions by email. An agent that ends its report with a
  question waits for an answer you never see. Tell it to decide what it can, carry on, and send
  you one short email only for choices that are really yours.

  `do what you can decide yourself and keep going. if something needs me, send me one short email
  with the choice and what you recommend.`

- Put the end time inside the loop prompt. Some schedulers drop a recurring job after a few days.
  If the prompt itself says "until 19 November 03:15", the agent knows to set the schedule up again
  when it lapses, and to stop and report when the time is reached.

- Turn a habit into a hook. When you find yourself telling agents the same thing every day, ask
  for it to become a hook, so every new session gets it without you typing it.

  `I keep telling agents <the instruction>. make it a hook that reminds every session at the right
  moment, show me the hook firing once, and save the reason in the brain.`

- Your later words win. When you change your mind halfway through a long loop, just say the new
  thing. Ask the agent to add your new words, dated, under the old ones in its ORDER file instead
  of replacing them, so it can see how the request changed.

- Ask for a page, not a wall of text. For a status check across many agents, ask for one page
  that opens in your browser, with what each agent is doing and what is waiting on you.

  `make me one page with every agent's current job, its last result and anything waiting on me,
  and open it in my browser.`

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
