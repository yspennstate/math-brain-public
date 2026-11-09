# Suggestions

Ideas for prompts, loops and uses of the brain, newest first. Each comes with a prompt you can
paste. New ones are added as they come up.

## 9 November 2026

- Ask where each fact came from. An agent that writes "the library supports this" may be
  remembering an older version, or guessing. A source next to each claim, a file, a page or a
  command it ran, lets you check the one claim that matters without redoing the work.

  `when you state a fact in a note or a report, put where it came from beside it: the file and
  line, the link, or the command you ran.`

- Give it a chores list for slow rounds. Some rounds the main task is waiting on something: a
  download, a long test, you. A short list of small jobs (tidy a folder, fix a typo, update a
  README) keeps those rounds useful instead of idle.

  `if the main task is blocked this round, take the top item from CHORES.md instead, do it, and
  cross it off. Never let a chore take more than one round.`

- Let it learn from your old prompts. The things you keep asking for are the best guide to what
  you care about. Point the agent at your past prompts or notes once, and ask it to write down the
  patterns it sees, so later rounds work the way you would.

  `read my last few hundred prompts in <the folder>, write down in ABOUT_ME.md the five things I
  ask for most and how I like work reported, and read that file at the start of every round.`

- Keep a list of dead ends. An agent that tried something and watched it fail will, a week later,
  try it again unless the failure is written down somewhere it reads. One line per dead end is
  enough: what was tried, what happened, and why it is not worth another go.

  `when an approach does not work, add one line to DEAD_ENDS.md saying what you tried and why it
  failed, and read that file before you pick an approach.`

- Ask for a weekly digest. Per-round notes are good for the agent but too fine for you. Once a
  week, have it boil them down to a few lines you can read with coffee.

  `every Sunday, read this week's notes and write a short digest: what got done, what is stuck,
  and what you plan next week. Put it at the top of DIGEST.md.`

- Say what needs your OK. A loop that has to ask about everything stalls while you sleep; one that
  asks about nothing can do something you did not want. Write down the few things it must ask
  first, and let it decide the rest.

  `you may decide everything about <the project> yourself except: spending money, deleting
  anything, and publishing. For those, email me one short question and carry on with other work.`

- Ask for a test with anything it builds. A small test that runs in seconds tells the next agent,
  or the next round, when something broke. Without one, a loop can undo its own earlier work and
  nobody notices.

  `whenever you build or change <the thing>, add a short test that checks it still works, and run
  all the tests before you call a step done.`

- Ask it to say when it changes its mind. Over many rounds an agent learns things that contradict
  what it said earlier. If it just carries on, the old conclusion stays in your notes as if it
  were still true.

  `if anything you find contradicts an earlier conclusion, say so plainly, name the old note, and
  correct it rather than leaving both.`

- Compare with last time. A number on its own means little. Ask the agent to put each new result
  next to the previous one, so you see at a glance whether things got better or worse.

  `each time you measure <the thing>, show the last result beside the new one and say in one line
  what changed and why.`

- Ask why, not only what. The brain remembers decisions, and the reasons are often in there too.
  Before you undo something that looks odd, ask the agent why it was done that way.

  `before we change <the thing>, recall why it was set up like this. if the brain has a reason,
  tell me what it was and whether it still holds.`

- Keep a glossary of your own words. Every project grows its own names for things. A short file of
  those names, each with one line on what it means, saves every new agent from guessing.

  `keep a GLOSSARY.md for <the project>: each term we use, one line on what it means, and add to it
  whenever a new term comes up.`

- Let it read the error itself. When something fails, don't describe the failure in your own
  words. Paste the message, or tell the agent to run the command and read the output. The exact
  line usually names the problem.

  `<the thing> fails when I run it. run it yourself, read the full error, and fix the cause rather
  than the symptom.`

- When two agents disagree, make them compare. If one agent says a result holds and another says
  it does not, don't pick one. Hand each the other's reasoning and ask where exactly they part.

  `here is what another agent concluded: <its answer>. find the exact step where you and it
  differ, and run the check that decides which of you is right.`

- Ask whether an old note is still true. The brain keeps what was true when it was written. A
  path, a setting or a rule from last month may have changed since. Before acting on an old note,
  have the agent check it.

  `the brain says <the note>. check whether that is still true today before you rely on it, and
  if it is not, mark the note as out of date.`

- Ask for a handoff note when a job changes hands. When you move a job from one agent to another,
  or from one computer to another, a short note saves the new agent an hour of reading.

  `write a handoff note for whoever takes over <the job>: what it is, what is done, what is next,
  where the files are and what to watch out for.`

- Ask it to measure, not guess. "This should be faster" and "it is 3 seconds instead of 11" are
  different claims. When a result has a number in it, ask for the number and how it was measured.

  `don't tell me it got better; measure it before and after on the same input and give me both
  numbers.`

- Try it on a copy first. A change to something many things depend on, a shared script, a
  settings file, a database, is safer made on a copy, tested there, and then moved over.

  `make the change on a copy of <the thing>, test it there, show me the result, and only then
  replace the original.`

- End every report with what it is unsure of. An agent's report reads as equally confident from
  top to bottom. One closing line on the shakiest part tells you where to look.

  `end your report with one line on the part you are least sure of and why.`

- Ask for a README for whatever it builds. A script or a folder made by an agent is clear today
  and a puzzle next month. A short README beside it, saying what it does and how to run it, is
  cheap to write while the agent still remembers.

  `write a short README next to <what you built>: what it does, how to run it, what it needs, and
  what to check if it breaks.`

- Keep a decisions file. Over a long project you and the agents settle many small questions:
  which tool, which format, what to leave out. Writing each one down with its reason stops the
  next agent from reopening it.

  `whenever we settle a choice on <the project>, add one dated line to DECISIONS.md: what we chose
  and why. read that file before suggesting a change.`

- Ask it to explain as if you were new. When an agent's answer is full of terms you don't know,
  ask again. It costs one prompt and you learn the project instead of nodding along.

  `explain what you just did as if I had never seen this project: what the parts are, what you
  changed and why it matters, in plain words.`

- Type fast; don't fix your spelling. Agents read through typos and half sentences without
  trouble. A quick prompt sent now beats a careful one sent in ten minutes. Save the care for the
  parts that matter: names, numbers, dates and what done means.

- After a crash, ask it to pick up where it was. When the computer restarts or a window closes,
  the job is not lost if it kept its notes. Start a new session in the same folder and point it
  at them.

  `the session working on <the job> was interrupted. read its ORDER.md and the first line of
  NEXT.md, check what the brain saved about it, and carry on from the next undone step.`

- Ask for two ways before it picks one. An agent usually takes the first approach that comes to
  mind. Asking for two, with what each costs, shows you the choice it was about to make for you.

  `give me two different ways to do <the task>, what each costs in time and risk, and which you
  would pick. wait for my answer before starting.`

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
