# Suggestions

Ideas for prompts, loops and uses of the brain, newest first. Each comes with a prompt you can
paste. New ones are added as they come up.

## 9 November 2026

- Keep passwords out of prompts. Whatever you type can end up in a log, a summary or a note the
  brain saves. Put a key in a file or your system's password store and tell the agent where it
  is, not what it is.

  `the key for <the service> is in <the file>. read it from there when you need it, never copy it
  into a note, a log or the brain.`

- Give each loop its own terminal and a name. With six windows open they all look alike. Ask the
  agent to set its window title to the job it runs, so you can find the right one at a glance.

  `set this terminal's title to "<short job name>" so I can tell it apart from the others.`

- Have a morning question ready. After a night of loops, one standing question gets you the
  picture in a minute: what finished, what broke, what waits on you.

  `what finished overnight, what failed or got stuck, and what is waiting on me? one line each,
  most important first.`

- Have the agent improve your prompt. A loop prompt written in a hurry leaves things out: an end
  date, what done means, what to do when something runs out. Hand it to an agent before you start
  the loop and ask what is missing.

  `here is a loop prompt I am about to run: <the prompt>. tell me what is missing or unclear,
  then give me a better version I can paste.`

- Say who the result is for. A report for you, a page for strangers on GitHub and an email to a
  colleague need different words. One line naming the reader saves a rewrite.

  `write this for <the reader>: someone who <what they know and don't know>. keep it to what they
  need.`

- Ask for the pieces before the work. A big job described in one sentence is easy to start and
  hard to finish. Ask the agent to break it into numbered pieces and put them in its NEXT file, so
  each round takes the next one and you can see how far it has got.

  `break <the job> into numbered pieces small enough to finish in one round each, write them into
  NEXT.md, and then start on piece 1.`

- Ask how to undo a change before it is made. When an agent is about to change something that
  already works, a setting, a script, a shared file, ask it first to save the old version and
  say how to put it back. Undoing then takes one line.

  `before you change <the thing>, keep a copy of how it is now and tell me the one step that puts
  it back if the change goes wrong.`

- Ask the agent what it would work on next. After a few days on a project the agent has read more
  of it than you have. Asking it for the next three things worth doing often turns up work you had
  not thought of.

  `from what you have seen of <the project>, list the three things most worth doing next and why.
  don't start them; I'll pick.`

- Let it say "I don't know". An agent pressed for an answer will sometimes make one up. Saying in
  the prompt that not knowing is an acceptable answer makes that less likely.

  `if you are not sure, say so and say what would settle it. a plain "I don't know" is better than
  a guess.`

- Show it one example of what good looks like. Describing the result you want takes a paragraph
  and still leaves room to guess. Pointing at one file, page or email you liked takes a line and
  leaves much less.

  `here is an example of what I want: <file or link>. make <the new thing> in the same style and
  at the same length, and tell me where yours differs from it.`

- Ask for a rough cost before a big job. Before a loop runs for days, ask how long it expects
  each piece to take and how much of your usage it will spend. A guess that is far off is worth
  hearing before the work starts, not after.

  `before you start, estimate how long each piece will take, how many pieces there are and roughly
  how much of my usage it will need. if it looks too large, suggest a smaller version.`

- Ask the agent to clean up after itself. Long jobs leave scratch files, half-finished copies and
  programs still running in the background. One line at the end of a prompt keeps the computer
  from filling up with them.

  `when you finish, delete the temporary files you made, stop any background program you started,
  and tell me what you removed and what you left on purpose.`

- Save a prompt you use often as a command. If you paste the same long loop prompt every few days,
  ask the agent to turn it into a slash command or a skill, so next time you type one word.

  `turn the prompt I just gave you into a command called /<name> that I can type in any session,
  and show me it working once.`

- Do one first, then the rest. Before an agent makes a hundred of something, have it make one and
  show you. A mistake caught on the first costs one; caught on the hundredth it costs a hundred.

  `make one <thing> first and show it to me. once I say it looks right, make the other <number> the
  same way.`

- Ask for the strongest case against a result. An agent asked whether it is right will usually say
  yes. Asked to argue that it is wrong, it often finds the weak spot.

  `write the strongest case that this result is wrong, and the one check that would settle it.
  then run that check.`

- Keep a restart list. When the computer restarts, every open loop is gone, and remembering ten
  prompts from memory is hard. Ask for one file that holds each running loop's prompt and end time,
  so a single request brings them all back.

  `keep a file with every loop running on this computer: its prompt, which folder it works in and
  when it ends. after a restart, read it and start each one again in its own terminal.`

- Ask for proof before "done". An agent can report a step finished when the upload failed or the
  file never got written. Asking it to check the result itself, every time, stops that.

  `don't call a step done until you have checked it worked: read the file back, open the link,
  or run the test, and say which check you did.`

- Ask which loops are running and when each ends. After a few days you lose track of what is
  still working for you. One question gives you the list.

  `list every loop running on this computer, what each one works on, when it started and when it
  ends, and which ones have stopped producing anything.`

- Ask what the brain already knows before the agent starts. Agents tend to work out from scratch
  what an earlier session already found. Asking for a short recall first costs a minute and often
  saves an hour.

  `before you start, recall what the brain has on <the topic>: earlier attempts, mistakes, results.
  give me five lines, then begin from there.`

- Give a loop a stop file. Finding the right terminal among ten to stop one loop is tedious. If the
  prompt says to look for a file, you can stop it from anywhere, even from another agent.

  `/loop fire this every 5 minutes for the next 10 days. keep working on <the project>. at the start
  of every round, if the file <folder>/STOP exists, finish nothing new, write a short report and
  stop.`

- Put a time limit on a hard question. An agent will dig at one problem for hours if nothing tells
  it when to step back. A limit turns a stuck afternoon into a note you can act on.

  `spend at most 30 minutes on <the problem>. if it is not solved by then, write down what you
  tried, what you ruled out and what you would try next, and stop.`

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
