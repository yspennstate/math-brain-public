# Suggestions

Ideas for prompts, loops and uses of the brain, newest first. Each comes with a prompt you can
paste. New ones are added as they come up.

## 9 November 2026

- Tell it which computer and shell you are on. An agent that assumes a Mac will hand a Windows user
  commands that fail on the first line, and the other way round. One sentence at the top of the
  project notes stops a whole class of errors.

  `I am on Windows 11 and the terminal is PowerShell. give me commands for that, and say so when a
  step works differently on a Mac or Linux.`

- Put the date at the front of file names. Reports, logs and results named report_final, report_new
  and report_new2 stop meaning anything after a week. A name that starts with the date sorts itself
  and tells you at a glance which one is newest.

  `name every report, log and result file starting with the date, like 2026-11-09_backtest.md, so
  they sort by day. never overwrite an older one.`

- Have it write down the versions it installs. A setup that worked in March can break in June
  because a package moved on. Ask the agent to keep a list of what it installed and at which
  version, so the same setup can be rebuilt later or on another computer.

  `whenever you install a package or tool, add its name and exact version to SETUP.md, with the
  command you used.`

- Keep files small enough to read in one go. An agent that has to open a five-thousand-line file
  reads part of it, guesses the rest, and pays for every line it does read. Ask it to split big
  notes and scripts into pieces with clear names, and to keep an index at the top.

  `when a notes file or script grows past about 500 lines, split it into smaller files by topic and
  keep a short index file that says what is in each.`

- Have it follow its own install steps in a fresh folder. Setup instructions written from memory
  skip the step the writer did months ago. Ask the agent to start from an empty folder and follow
  the page word for word, fixing the page wherever it gets stuck.

  `make a new empty folder and follow the README's setup steps exactly as written. wherever you get
  stuck or have to guess, fix the README so the next person does not.`

- Ask for the simplest tool that works. Agents like to build: a database where a text file would
  do, a web page where a printed table would do. Say that you prefer the plain option and want to
  hear why before anything bigger gets built.

  `use the simplest thing that does the job: a text file before a database, a script before a
  service. if you think something bigger is needed, tell me why first.`

- Have it reread your request before it says done. A long prompt with three questions in it often
  gets two answered. Ask the agent to go back to your words, count what you asked for, and check
  each part against its report.

  `before you report, reread my message. list each thing I asked for and say done, not done, or
  not done because, for every one.`

- Tell it what you already tried. An agent starting on a problem you have been fighting will try
  the obvious fixes first, the same ones you tried yesterday. Two lines on what failed save it an
  hour.

  `I already tried <the fixes> and they did not work. start from there, and do not repeat them
  unless you have a reason to think something has changed.`

- Paste a screenshot when words fail. An error dialog, a page that looks wrong or a chart with a
  strange shape is often faster to show than to describe. Terminal agents can read an image file;
  save it and give the agent the path.

  `here is a screenshot of what I see: <path to the image>. tell me what is wrong in it and how to
  fix it.`

- Start a new agent read-only on anything that matters. The first hour with a new project is when
  an agent knows least about it. Let it read, map and propose for that hour, and only then let it
  change files.

  `for the first hour, only read. do not edit, move or delete anything in this folder. at the end,
  tell me what you found and what you would change first.`

- Keep a changelog that a reader can follow. Commit messages are written for the people doing the
  work. A short dated list of what changed, in plain words, tells everyone else what is new
  without reading the history.

  `each time you change something a reader would notice, add one dated line to CHANGES.md saying
  what changed, in words someone new to the project would follow.`

- Ask for a chart when the numbers pile up. A table of forty rows hides the one row that matters.
  Asking for a small picture of the same numbers often shows the trend, the outlier or the broken
  run at a glance.

  `when a result has more than about ten numbers, also make a simple chart of them, save it next to
  the table, and tell me what stands out in it.`

- Set a size above which it asks before downloading. An agent that decides it needs a model or a
  data set will fetch tens of gigabytes without a second thought. One number in the prompt stops a
  full disk before it starts.

  `ask me before you download or install anything larger than 2 GB. say what it is, how big, and
  why you need it.`

- Tell it which job wins when two compete. With several loops on one computer, two jobs will want
  the same thing at the same time: the processor, the disk, your attention. A short ranking in the
  project folder lets each agent decide without waiting for you.

  `PRIORITY.md lists my jobs in order. when two of them need the same thing, the one higher on the
  list goes first and the other waits or does something smaller.`

- Have names checked against a source, not memory. Agents misspell people, places and titles with
  full confidence, and a wrong name in a published page or a film is the error readers notice
  first. Ask for every proper name to be checked against a page it can open.

  `before you publish, check the spelling of every person, place and title against a source you can
  open, and list any you could not confirm.`

- Ask it to number the steps it proposes. When an agent offers a plan, numbered steps let you
  answer in a few words ("do 1 and 3, skip 2") instead of retyping what you want. It also makes the
  report afterwards easy to check against the plan.

  `when you propose a plan, number the steps. I will answer with the numbers I want you to do.`

- Keep the commands that worked in one file. Agents rediscover the same install command or the same
  fix for a stubborn error again and again. A file of commands that worked, one line each with a
  note on what it is for, saves that search in every later session.

  `when a command finally works after some trial and error, add it to COMMANDS.md with one line on
  what it does. check that file before you try something new.`

- Have it ask its questions as a choice, with its own pick marked. A loose question waits until you
  have time to think. Two or three options with the agent's recommendation on top can be answered
  from a phone in seconds, and the agent can carry on with the rest meanwhile.

  `if you need a decision from me, give me two or three options, put the one you recommend first,
  and keep working on anything that does not depend on my answer.`

- Ask it to point out instructions that contradict each other. After a few weeks a project
  collects rules that pull in different directions, and an agent will quietly pick one. Have it
  stop and name the clash instead, so you decide which rule stands.

  `if two of my instructions disagree, do not choose between them silently. tell me which two,
  quote both, and say which one you would follow and why.`

- See what changed before it goes to GitHub. A push is easy to make and awkward to take back once
  others have pulled it. Ask the agent to list the files it is about to send and show the changed
  lines for anything you did not expect.

  `before you push, list every file in the commit and show me the changed lines of any file I did
  not ask you to touch.`

- Give it a short list of words to keep out of public writing. Pages written by an agent drift
  toward the same filler words and the same bold headings. A list of a dozen words to avoid, kept
  in the project folder, does more than asking for a better style every time.

  `before you publish a page, check it against STYLE.md in this folder. rewrite any sentence that
  uses a word on the avoid list.`

- Say what it may delete and what it never deletes. An agent cleaning up to save disk space will
  happily remove whatever looks old. Give it two short lists, and tell it to ask about anything on
  neither.

  `you may delete temporary files and copies that are already saved on GitHub. never delete <the
  folders that matter>. if a file is on neither list, ask me first.`

- Have it open a link before it sends you one. A link to a file that was never uploaded, or to the
  wrong branch, wastes your time. Ask the agent to fetch every link it gives you and confirm it
  shows what it should.

  `before you give me a link, open it yourself and check that it shows the file you mean. if it
  does not, fix it first.`

- Ask for an estimate, then compare it with what happened. Before a long step, the agent says how
  long it expects it to take; afterwards it writes down how long it really took. After a few rounds
  its estimates get better, and you learn which jobs always run over.

  `before each long step, write down how long you expect it to take. when it finishes, add how long
  it actually took next to the estimate.`

- Tell it which copy is the real one. When the same file lives in two places (a working folder and
  a GitHub repository, or two computers), an agent can edit the wrong one and then wonder why
  nothing changed. Name the copy that counts and where the others come from.

  `the file in <folder> is the one that counts; the copies elsewhere are made from it. edit only
  that one, and if you find a copy that differs, tell me before you overwrite either.`

- Have it read the clock instead of assuming the time. An agent that has been running for hours
  can lose track of the date, and a loop with an end date depends on it. Ask it to check the
  computer's clock whenever a deadline or a schedule is involved.

  `whenever a step depends on the date or time, read it from the computer first and write it into
  your note, instead of working it out from earlier messages.`

- Group small changes into one save. Twenty commits of one line each make a history nobody can
  read, and on repositories with automatic tests each push can start a run. Ask the agent to
  collect related changes and save them together when a piece is finished.

  `collect related small changes and commit them together once the piece is finished, with one
  short message that says what changed.`

- Ask it to correct its own numbers out loud. An agent that sends a warning and then finds it
  measured wrong should say so in a new message, with both numbers and the reason, rather than
  quietly changing course. Others may already be acting on the first one.

  `if you find that a number you reported earlier was wrong, send a short correction straight away:
  the old number, the new one, and how you measured it the second time.`

- Have agents reuse each other's finished work. When two computers both need the same slow result
  (an index, a converted file, a computed table), one can publish it and the other can check it and
  take it, instead of computing it again. Ask the agent to look for a published copy first.

  `before you compute this from scratch, check whether another computer has already published it.
  if so, check a sample of it against your own and use it if they match.`

- Measure a falling resource twice before raising the alarm. A single reading of free disk or
  memory can mislead: a temporary file, a different unit, a reading from a different tool. Two
  readings with the same tool a few minutes apart show the real trend.

  `before you warn anyone that disk space or memory is running out, take two readings with the same
  tool five minutes apart and report the rate, not just one number.`

- Ask for the result where you will see it. A finished result buried in a log file on another
  computer may as well not exist. Say where you look (an email, a page in your Downloads folder, a
  file in the repository's front page) and the agent will put it there.

  `when this is finished, put a one-page summary in my Downloads folder and email me the link to
  it. do not leave the result only in a log.`

- Let a loop pause itself when it is waiting. Some rounds cannot do anything until another job
  finishes. A loop that knows what it is waiting for can say so in one line and skip the rest of
  the round, instead of starting new work that gets in the way.

  `if the step you need is waiting on another job, write one line saying what you are waiting for
  and end the round. pick it up again when that job is done.`

- Ask which old notes it never uses. A brain grows faster than anyone reads it. Every so often,
  ask the agent which notes it has not needed in months; some are stale, some are wrongly named and
  should be easier to find.

  `look at which notes in the brain have not been recalled in the last three months. for each, say
  whether it is out of date, hard to find, or simply rarely needed.`

- Tell the agents what they share. Two computers on the same home internet line, two jobs on the
  same disk: agents cannot see that from inside one job. A short note on what is shared lets them
  explain a slowdown correctly and agree on who goes first.

  `these two computers share one internet connection. if a download is slow, check what the other
  computer is downloading before you blame the server.`

- Keep keys out of logs and printouts. An agent that is given a login token for a service will
  sometimes print it while debugging or write it into a log that later gets pushed. Say once that
  the key is used but never shown, and where it lives.

  `the access token is in the credentials file. use it, but never print it, put it in a log, a
  commit or a message, and never copy it anywhere else.`

- Have it listen to a sample, not just trust a score. An automatic check on audio, pictures or
  text catches most problems and misses some. Ask the agent to list the few items its check was
  least sure of, so you can look at those yourself.

  `after the automatic check, give me the five items it was least sure about so I can look at them
  myself.`

- Ask it to say what it will not stop and why. When a computer is busy, an agent may be tempted to
  stop someone else's work to make room for its own. A standing rule that it reports instead of
  stopping, and says what would free the resource, keeps one loop from quietly killing another.

  `never stop or pause another job to make room for yours. if the machine is too busy, tell me
  which jobs are using it and what you would need, and carry on with what you can.`

- Have it turn a fix into a rule other agents see. A lesson one agent learns at two in the morning
  is lost by the next session unless it is written where the others read it. Ask for the rule as
  one short line in a shared file, with the date and the reason.

  `when you fix a problem that another agent could run into, add one dated line to RULES.md saying
  what to do and why, so the next agent does not repeat it.`

- Name the one thing that would make the job go faster. Agents often work around a slow step
  without saying what would remove it: a login, a faster disk, a larger allowance. Ask for that
  one thing, so you can decide whether to provide it.

  `if something outside your control is slowing this job down, tell me the single change that
  would help most and roughly how much faster it would be.`

- Save the expensive part before the risky part. A long job often ends with a short step that can
  fail: decoding, writing a file, uploading. If the hours of work before it are only in memory, a
  failure at the end loses all of them. Ask the agent to write the costly intermediate result to
  disk first, so a failed last step can be redone alone.

  `write the result of the slow step to disk before you start the final step, and make the final
  step something I can rerun from that file without redoing the rest.`

- Let one agent point out what another is slowing down. When several jobs share a computer, one
  can quietly starve another (of network, memory or disk). An agent that notices should say so to
  the job's owner with the numbers, rather than stopping someone else's work on its own.

  `if you see that another job on this machine is slowing yours, measure it, and leave a short note
  for whoever runs that job with what you saw. do not stop it yourself.`

- Give a memory limit along with the task. A job that fits on paper can still run out of memory at
  its peak. Telling the agent how much it may use makes it plan for the peak instead of finding out
  when the job dies.

  `this computer has about 10 GB free. keep the job under 8 GB at its peak, and if it would need
  more, process it in smaller pieces.`

- Let agents on different computers share one queue. If two machines can both do a job, a shared
  list (a file in a GitHub repository works) where each one marks the item it took keeps them from
  doing the same work twice, and either can pick up what the other left.

  `before you start an item, check the shared queue file; if nobody has it, write your name and the
  time next to it, push, and only then begin. when it is done, mark it done and push again.`

- Let it take turns on a shared resource. When two jobs need the same graphics card or the same
  disk, running them at once can make both slower than running them one after the other. Ask the
  agent to use a simple lock so one waits while the other works.

  `these two jobs both use the graphics card. make them take turns: one holds a lock file while it
  runs, the other waits for the lock to clear.`

- Ask for a second check by a different method. A result checked the same way twice can repeat the
  same mistake twice. Recomputing it another way (different code, a different data path, a census by
  hand on small cases) is what catches the error.

  `after you get the number, check it a second way that does not reuse your first code, and tell me
  whether the two agree.`

- Let a slow download pick up where it stopped. Large files (models, data sets) often drop partway
  through. A script that starts the whole file again on every drop can run for hours without ever
  finishing. Ask the agent to resume from the last byte it has and to keep retrying with a pause,
  rather than giving up after a few tries.

  `when you download anything large, resume from where a dropped download stopped instead of
  starting over, wait a little between retries, and check the finished file against its size or
  checksum.`

- Have it test a fix on a small piece first. Before a change runs on the whole job, run it on one
  file, one page or a few megabytes, and compare the result with what you get without the change.
  A mistake then costs a minute instead of a night.

  `before you run this fix on everything, run it on one small piece, compare the result with the
  old way, and show me both before going further.`

- Ask it to say how much is left. "Working on it" tells you nothing on day three. A count (40 of
  100 done, about 6 hours to go at the current rate) tells you whether to wait, help or change the
  plan.

  `at the end of each round, write how many pieces are done out of the total and how long the rest
  will take at this round's pace.`

- Give each loop one owner for each file. When two loops can both edit the same page, one will
  sooner or later undo the other's work without noticing. Say in each prompt which folders that
  loop writes to and which it only reads.

  `you write only in docs/notes/ and results/. everything else you may read but not change; if a
  fix is needed somewhere else, write it down in NEXT.md for me instead of making it.`

- Ask for the reason a round did nothing. A quiet round can mean the work is finished, the agent is
  waiting on something, or it is stuck and not saying so. One line on why tells you which.

  `if a round makes no change, still write one dated line saying why: finished, waiting on what, or
  stuck on what.`

- Keep a short list of what you never want it to do. Some rules matter more than any task: never
  delete without a copy, never post in public, never spend money. Put them in a file the loop reads
  every round, so a long run does not forget them on day four.

  `read RULES.md at the start of every round before anything else. if a step would break one of
  those rules, skip the step and write in NEXT.md what you skipped and why.`

- Keep the computer awake. A loop only runs while the machine does. Many laptops and small desktops
  go to sleep after a few minutes with nobody at the keyboard, and the loop simply pauses, often
  without any message saying so. Turn sleep off in the power settings while a long loop runs, or
  ask the agent to do it.

  `before you start this loop, check whether this computer will go to sleep when I am away, and if
  it will, tell me how to stop that for the next few days (or do it yourself if you can).`

- Try a loop for an hour before you leave it for days. The first rounds show whether the prompt
  says what you meant: whether the agent finds its NEXT file, saves where you expect, and stops
  when it should. Fixing that at noon is easier than finding out on day three.

  `run this every 5 minutes for the next hour only. at the end, tell me what went wrong or was
  unclear in the prompt, and suggest a better version I can run for ten days.`

- Have it merge notes that say the same thing. After weeks of work the brain collects near
  copies: three notes on the same fix, written on different days. Recall then spends its room on
  repeats. A weekly pass that merges them keeps answers short.

  `once a week, look for notes in the brain that cover the same thing, merge each group into one
  note that keeps every fact and date, and mark the old ones as replaced rather than deleting them.`

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
