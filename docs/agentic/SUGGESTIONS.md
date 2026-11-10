# Suggestions

Ideas for prompts, loops and uses of the brain, newest first. Each comes with a prompt you can
paste. New ones are added as they come up.

## 10 November 2026

- When a job waits for a computer to be free, have it judge busy by what is running, not by what is
  open. A program left open in the background, an editor or a 3D tool sitting idle, can look like
  someone at work, and a job that waits for it to close may wait all night. Ask the agent to measure
  how hard each program is working, and to write down on every check the reason it is still waiting,
  so a stalled job tells you why in one line.

  `before the job starts each heavy step, check what is actually using the processor and memory, not
  just which programs are open. if you decide to wait, write the reason in the log each time, and
  tell me if the same reason has held you up for more than an hour.`

- Drag a file into the terminal to hand the agent its path. Typing a long path by hand is where the
  typos come from. In most terminals, dropping a file or folder onto the window pastes its full path
  at the cursor, quoted if it has spaces. Then say what you want done with it.

  `<drop the file here> read this and tell me in five lines what is in it before we do anything
  with it.`

- If the terminal asks before every command, allow the safe ones once. A new terminal agent asks
  permission to read a folder, list files, run a search. Answering yes forty times an hour is how
  people end up approving without reading. Most terminal agents let you allow a kind of command for
  good (in Claude Code, the "don't ask again" choice or the permissions setting). Allow the
  read-only ones, keep asking for anything that deletes, installs, pushes or spends money, and then
  read the prompts that are left.

  `which commands have you asked me about most today? list the read-only ones and set them so you
  stop asking. keep asking me before anything that deletes, installs, publishes or costs money.`

- When the connection drops in the middle of a job, ask what finished before you start again. A
  dropped wifi, a closed laptop lid or a remote computer that went to sleep can cut a job halfway.
  Starting the whole thing again repeats what already worked and can leave two copies of the same
  output. Have the agent check what is on disk first and resume from there.

  `the connection dropped while you were working on <the job>. before you redo anything, check
  what finished, what is half written and what never started, then continue from the first
  unfinished piece.`

- Speak your prompts if typing slows you down. Windows has voice typing on Windows key + H and a
  Mac has dictation in its keyboard settings; both work in a terminal. A spoken request comes out
  longer and with more of the context the agent needs, and the agent reads through the odd misheard
  word. Read it once before you press Enter, mainly for names and numbers.

  `I dictated this, so a few words may be wrong. if something does not make sense, ask me rather
  than guessing: <your request>`

- When you are new to something, ask the agent what you should be asking it. You may not know what a
  good request looks like for a field you have never worked in. The agent can list the questions an
  experienced person would ask first, and you pick the ones that matter to you.

  `I am new to <the topic> and want to <the goal>. what are the five questions someone experienced
  would ask before starting? answer the first one, then wait for me to pick the next.`

- If you see it going the wrong way, stop it mid-turn and say so. In a terminal agent, pressing Esc
  stops the current step without closing the session; then type the correction. Waiting for it to
  finish a long turn in the wrong direction costs time and leaves work you then have to undo. Your
  correction lands sooner, and the agent keeps everything it learned up to that point.

  `stop. you are editing the copy, not the live file. undo what you changed in the copy, then make
  the same change in <the live file>.`

- Ask it to teach you the one command, so next time you can do it yourself. Some jobs come back
  every week: checking a log, restarting a stuck program, seeing what is using the disk. After the
  agent does one, ask for the shortest way to do it by hand and what each part means. A small note
  of these saves you a round trip when the fix takes ten seconds.

  `show me the one command you used for that, explain each part in a line, and add it to <my notes
  file> under a heading I will find later.`

- Ask the agent to check back once, later. Not everything needs a loop. A download, an upload being
  processed, a reply you are expecting: one look in two hours is enough. Say when, what to look at, and
  what to do with each outcome, and the agent will come back to it on its own instead of you having to
  remember.

  `check on <the thing> again in two hours. if it finished, <next step>; if it failed, tell me why;
  if it is still running, look once more an hour after that.`

- Keep your best prompts in one file. After a few weeks you will have a handful of requests that
  always work: the loop that keeps a project moving, the way you ask for a report, the line that stops
  an agent from cutting corners. Paste them into a plain file as you find them. A new agent can read
  that file on its first turn and start the way you like to work, instead of learning it again.

  `read <my prompts file> before you start. these are the requests that have worked for me; follow
  the same style, and add any new one I give you that works well.`

- Let the agent write the loop prompt for you. Describe the job in your own words, with how often and
  for how long, and ask it to turn that into a loop prompt: what to read first, what to do each round,
  where to save, when to stop and how to report. Read it once, fix what it got wrong, then start it.

  `I want an agent to <the job> every <interval> for the next <days>. write the loop prompt for that:
  what it reads first, what it does each round, where it saves, and when it stops. show it to me
  before you start it.`

- Use a loop to watch a listing for you. Job boards, grant calls, calls for papers and conference
  deadlines change every day, and checking them by hand is the kind of thing that slips. A loop can
  read the listing each round, add anything new to one tracker file with its deadline and a line on
  why it fits, skip what is already there, and tell you only when something is due soon.

  `/loop fire this every hour for the next 10 days. check <the listing> for new entries that fit
  <what I am looking for>, add each new one to <tracker file> with its deadline and one line on why
  it fits, and email me only when something is due within three days.`

- When you reply "keep working", say on what. After a long report, "keep working" leaves the agent
  to pick the next step, and it may pick the easy one or start something you didn't want. Adding the
  item you care about, or "the next line in your NEXT file", keeps it on the path you had in mind.

  `keep working, on <the item> first. when that is done, go on with the next line of your list.`

- With several agents running, have every report end by naming the request it answers. After a day
  of asks in different windows, a report that says "done, all three files are updated" can belong to
  any of them. One closing line in your own words, with the time you asked, tells you at a glance which
  job just finished and which ones are still out.

  `end every final report with one line saying which of my requests this was, in my words, with the
  time I asked it.`

- When the result is for someone else, ask for something you can forward as it is. A summary in a
  terminal is written for you and doesn't travel well. A short page, a document or an email draft
  with the context a stranger needs (what this is, what was found, where the files are) can go to a
  colleague in one step, without you rewriting it.

  `write this up so I can send it to <who> without editing: what it is, what we found, and the links.
  put it in <a page / a doc / an email draft> and give me the link.`

- Keep a checklist file that every agent writes to. When you give several agents several jobs, it is
  easy to forget who is doing what, and the agents don't know about each other. A plain list in one
  file, where each agent adds what you asked it, marks it done when it finishes, and leaves a box for
  you to tick once you have seen the result, answers "what did I ask for and where is it" in seconds.

  `keep a checklist in <file>: add what I just asked you, with the date and my words, update it as
  you go, and mark it done with one line on the result. don't tick the "seen" box, that one is mine.`

- Once an agent has the context, a short answer is enough. After it lays out a plan, "ok do it" or "yes,
  the second one" is a complete instruction, and you don't need to repeat the whole request. If it
  asks you something you already answered, that's a sign it lost track, and pointing it back to your
  earlier message works better than typing it all again.

  `yes, do the second option. you have everything you need from my last message; only ask me again
  if something new comes up.`

- After a crash or a restart, tell the agent to pick up where it stopped, not start over. A fresh
  window doesn't know what the last one finished, and the easy path is to begin again from the top,
  which can redo hours of work or overwrite what was already done. Point it at the notes and files the
  last run left and ask it to check them first.

  `this terminal was reopened after a restart. read the notes and output folders from the last run,
  tell me what was already finished, and continue from the first step that isn't done.`

- When something breaks, paste the exact error, not your summary of it. "It didn't work" sends the
  agent guessing. The error text, the command that produced it, or a screenshot of the window usually
  points straight at the cause, and the agent can often fix it in one step.

  `here is the exact error I got: <paste>. it came from <what I was doing>. find the cause, fix it,
  and run it again to show it works now.`

- Ask how long a job will take before it starts, and have the agent write the answer down. A render,
  a download or a big search can run for minutes or for a day. With an estimate on record you know
  when to look again, and the agent can tell you early if it is running far behind, instead of you
  finding out the next morning.

  `before you start, tell me roughly how long this will take and what the slowest step is. if it is
  going much slower than that, stop and tell me why.`

- When you hand an agent several things at once, say which one matters most. An agent with five asks
  and no order often starts with the easiest, and the one you cared about waits. One line fixes it:
  what comes first, and what can wait if time runs short.

  `do these in this order: <most important>, then <next>, then the rest. if you can't finish all of
  them, finish the first one properly and tell me where the others stand.`

- Say what finished looks like. "Make the film" can end at a script, at a rough cut or at a video
  posted online, and an agent will often stop at the first point that looks like an answer. Name the
  last step you want to see: a file in a folder, a link that plays, a test that passes. Then it keeps
  going until that is true, or tells you exactly what stopped it.

  `this is done when <the thing I can open or check>. don't stop before that. if something blocks
  you, tell me what it is and what you tried.`

- When the agent says it's done, ask for the link or the file path, not a description. "The video is
  uploaded" and a link you can click are different claims, and only the second one can be checked in
  a few seconds. If it can't give you the link, the step probably didn't finish.

  `give me the link (or the full path) to what you made, and one line on how you checked that it
  opens and is the right version.`

- If a newly released model doesn't show up in your terminal, the program usually needs updating.
  A coding agent only lists the models its installed version knows about, and a window opened before
  the update keeps the old list. An agent can update the program, open a fresh window and check that
  the new model is there and answers, so you don't have to look for the right command.

  `the new model <name> is out but I can't pick it here. update the agent program, open me a new
  terminal with that model selected, and send it one test prompt to show it works.`

- When you change something yourself, tell the agents. If you switch off a computer's sleep setting,
  sign in to a site or free some disk space, an agent that last saw the old state will keep working
  around a problem that is gone, or report it to you again. A one-line message, passed on to all of
  them, brings everyone up to date.

  `I just <what I changed> on <which computer>. tell every agent working with it, check that the
  change took, and let me know if anything still needs me.`

- When a step is only acceptable under one condition, say what to do if the condition can't be met.
  "Apply, but make sure they don't contact my referees without asking me" leaves the agent guessing
  when the form has no such option. Add the other half: "otherwise don't apply, and tell me". An agent
  told what to do in both cases won't quietly go ahead on the riskier one.

  `do <the step> only if <the condition>. if you can't confirm the condition, don't do it at all:
  stop, tell me what you found, and go on with the rest of the list.`

- On a computer you share, the owner's own background work counts as them using it. A person can be
  away from the keyboard while their renders, backups or builds are running, and a job of yours that
  starts then can push the machine into heavy swapping. Tell the agent to look for the owner's own
  heavy processes, not just the mouse and keyboard, and to stay out while those run.

  `on <their> computer, treat their own heavy programs (renders, builds, big downloads) the same as
  them sitting at it: don't start our jobs while those run, and wait a while after they finish.`

- When an agent tells you something can't be done, ask what it would take. "There is no room for
  the model" or "the account is out of usage" is often the first obstacle it hit, not the last word.
  The usual way through is ordinary: copy finished files somewhere safe and free the space, use a
  second account, run the job on another computer. Ask for the steps and the cost of each, then let it
  do the ones you agree with.

  `you said this can't be done. list what it would take to make it possible, step by step, with what
  each step costs or risks. do the safe ones now and ask me about the rest.`

- Before you put time into a new tool or model, ask the agent for links to real work other people made
  with it. A demo page shows the best case. A few ordinary examples from users (videos, papers, repos)
  show what you will actually get, and they take a minute to look at.

  `find three things real people made with <the tool> and posted publicly. give me the links, one line
  on each, and say how close they are to what we want to make.`

- You can ask a looping agent a quick side question, but tell it to go back to the loop afterwards.
  An agent that answers a one-off ("is anything due today?") can treat the answer as the end of the
  job and stop, and the loop you set up for the week goes quiet. One clause at the end of the side
  question keeps it going.

  `check now whether <the thing> needs me today. if it does, email me the details. if it doesn't,
  say so in one line and go straight back to the loop you were running.`

- Ask the agent now and then which of your computers are sitting idle, and what they could take on.
  A second laptop or a desktop in the corner often has free memory and cores all day. Have the agent
  check each machine's free memory against what the job needs before it moves anything there, because
  a large model that does not fit simply fails, and a report of what fits where is worth more than a
  failed launch.

  `check each of my computers: how busy it is, free memory, free disk. for each idle one, say which
  of our jobs would fit on it and which would not, with the memory each needs. move the ones that fit.`

- When you give feedback on something the agent made, say what to keep as well as what is wrong.
  "The pictures are great, the voice is in the wrong language, the mouths don't move" tells it to fix
  two things and leave the rest alone. A list of complaints alone often gets you a full redo, and the
  part you liked can come back worse.

  `keep: <what works>. change: <what is wrong>, one line each. don't touch anything on the keep list,
  and tell me which items you changed when you send the new version.`

- On a computer someone else is using, have heavy jobs step aside while that person is at it. A
  long render or a big download can make their mouse and typing lag. Ask the agent to check whether
  the person is active before each heavy step, and to pause or slow down while they are, then pick up
  again when the machine is quiet.

  `before each heavy step, check whether the person who owns this computer is using it. if they are,
  or the machine feels slow, pause or use less, and carry on when it is quiet. log each pause.`

- When an agent works on a hard research question, ask for its progress in research terms, with each
  claim marked by how sure it is. "Making good progress" tells you nothing. What you want is which
  directions it opened, which it ruled out and why, and for each result whether it is checked, a
  sketch with a gap, or only a hunch. That split keeps a promising idea from being read as a theorem.

  `report on the problem: new directions you found, routes you ruled out and why, and for each
  result say whether it is fully checked, a sketch with a named gap, or a guess. no summary words.`

- Give the agent the next job before it finishes the current one. An agent that submits a form or
  lands a change often stops and waits, and if you are away the hours go by with nothing happening.
  A short list of what comes next, in order, lets it move straight on and report once at the end.

  `when you have submitted this, don't wait for me. go on to the next items in this order: <one>,
  <two>, <three>. send me one short report when the list is done or when something needs me.`

- When a site will ask the agent to confirm many small steps, give it standing permission for those
  steps and name the ones that still need you. Submitting a paper or an application can take a dozen
  "are you sure" and "next" screens, and an agent that stops at each one turns a ten-minute job into an
  hour of waiting for you. Say which kinds of screens it may accept on its own, and which it must
  never pass without you, such as paying, signing or sending to another person.

  `you can click yes and next on the ordinary confirmation screens without asking me. stop and ask
  before anything that pays, signs an agreement in my name or sends something to another person.`

- Ask the agent to follow the conventions of the place the work is going. A journal, a preprint
  server and a job portal each have their own habits for titles, abstracts, author lists and file
  names, and work that ignores them looks careless to the people who read it there. Have the agent
  look at a few recent entries on the site and match them before it submits.

  `before you submit, look at five recent entries on this site and make our title, abstract and file
  names follow the same conventions: capitals, length, how authors are listed. show me what changed.`

- For a piece of writing that matters, ask the agent to think about the approach before it drafts.
  A letter, a statement or an application has a reader, a purpose and a few points that decide how
  it lands. Asking for a short plan first (who reads it, what they need to believe at the end, which
  three points carry it, what to leave out) gives you something quick to correct, and the draft that
  follows is usually close to right the first time.

  `before you write anything, think about how to do this well. tell me in five lines who will read
  it, what it has to achieve, the points that carry it and what you would leave out. then wait.`

- When someone else is writing about you, such as a recommendation letter, have the agent give them
  material rather than finished prose. A referee writes in their own voice and knows what they saw.
  Two short paragraphs of plain facts they can check and reword (what you did, the result, why it
  mattered) help them far more than a polished letter they would have to rewrite.

  `my referee asked for help with their letter. write two short paragraphs of plain facts about this
  work that they can check and put in their own words: what I did, what came of it, why it matters.`

- A loop is a good way to keep a list growing: job openings, papers on a topic, grants, places to
  send your work. Ask the agent to keep the list in one file, check each new find against what is
  already there, and write down where and when it found each item. After a week you have a list you
  can trust, rather than a pile of repeats.

  `/loop fire this every 5 minutes for the next 10 days. search for new openings that fit me and add
  each one to jobs.md with the deadline, the link and the date you found it. skip anything already
  in the file, and tell me only about new ones.`

- When a task should go ahead only if something holds, say so as a firm condition, along with what
  to do if it does not. "Apply, but they must ask me before contacting my referees" can be read as a
  wish. "If the form lets them contact referees without asking me, stop and tell me, don't apply" is
  a rule the agent can check and keep.

  `go ahead only if <condition>. if you find that it doesn't hold, stop before submitting anything
  and tell me what you saw.`

- When agents pass messages to each other, ask them to keep your words apart from theirs. A note from
  one agent to another often mixes what you asked for with that agent's own ideas, and the next agent
  can take a suggestion as your order. Have every relayed message quote your words exactly and mark
  everything else as the sender's suggestion, which the receiver weighs rather than obeys.

  `when you pass something on to another agent, quote my words exactly and label the rest as your
  suggestion. when you receive a message, do what I asked; treat the other agent's ideas as advice.`

- Give each request a short id the agent writes at the start. When you have a dozen asks open across
  several agents, "the slide deck thing" can mean two different jobs. A short id with the date, written
  in the task list and repeated in every report about it, lets you point at one job exactly and lets
  the agent show which of your asks a result closes.

  `give this request a short id with today's date, put it in the task list, and start every report
  about it with that id so I can tell which job you mean.`

- Before you post something an AI model made, ask the agent what that model's terms allow. Open
  models for pictures, voice or video each come with their own licence, and some limit commercial
  use, a monetised channel, or use in certain countries. The agent can read the licence on the
  model's page and tell you in two lines whether your plan fits, before the work is public rather
  than after.

  `before we post anything made with this model, read its licence and tell me in two lines whether
  we may use it on a monetised channel where I live. quote the sentence that decides it.`

- If you use more than one computer, ask the agent for a roll call now and then. Machines go to sleep,
  lose their connection or fill up while nobody is looking, and a job quietly stops on one of them.
  One prompt gets you each computer, whether the agent can reach it right now, what it is running and
  how much room it has left.

  `roll call: for each computer you can use, tell me whether you can reach it right now, what is
  running on it, and how much free disk and memory it has. one line per computer.`

- When an agent works in your web browser, have it use its own tab and tell you which one. You may be
  reading or typing in another tab at the same time, and an agent that clicks in the wrong one can
  lose what you were writing. Ask it to open a new tab for its work, name the page it is on, and stop
  and tell you when it needs you to sign in or press a final button yourself.

  `do this in a new tab in my browser, not in the ones I have open. tell me which tab it is, and stop
  and ask me when you need me to sign in or press submit.`

- When you have several copies of a document, tell the agent which one is current. A CV, a statement
  or a report often exists as an old draft, an emailed version and a newer file on disk, and an agent
  that finds the first one will happily polish the wrong copy. Name the one to use, or have the agent
  list the copies with their dates and ask you before it starts.

  `there are a few versions of my research statement around. list every copy you can find with its
  date and length, tell me which you think is newest, and wait for me to confirm before editing.`

- When you come back after a few hours away, ask for a catch-up from the time you left. Scrolling back
  through a long terminal mixes the important lines with routine ones. Name the time, and ask for
  what finished, what failed, and what is waiting on you, in that order. Ask it to keep the list short
  and to point you to a file for the detail.

  `I was away from about 11pm. since then: what finished, what failed or got stuck, and what is
  waiting on me? a few lines each, newest last, and tell me where the details are.`

- When the computer feels slow, ask the agent what is using it before anything gets closed. The cause
  is often one job you forgot about, or several agents each starting the same heavy thing. Have it list
  the busiest programs, say which ones it started and what each is for, and suggest what could wait.
  Then you decide what to stop. Closing things blindly can throw away hours of work that was nearly done.

  `the computer feels slow. list what is using the most memory and processor right now, mark the ones
  you started and what each one is doing, and suggest what could wait. don't stop anything yet.`

- When an agent opens a new terminal window for you, ask it to start the window clean. A window started
  from inside the agent's own shell can carry over that agent's settings, and the new session may then
  behave differently from one you opened yourself: history not saved, colours off, a different working
  folder. Have the agent open it the same way you would, then check one thing that would show the
  difference, such as whether the new session is being saved.

  `open me a new terminal with a fresh session, started the way I would start it myself, not as a child
  of your own shell. then check that the new session is saving its history and tell me.`

- When an agent says it is waiting on someone, another agent or a person, ask who, since when, and what
  it will do if no answer comes. "Waiting" with no deadline can last all night. A good answer names the
  one it asked, the time it asked, a time it will ask again, and what it can get on with in the meantime
  without the reply.

  `you said you're waiting on another agent. who exactly, since what time, and when will you ask again?
  what can you do now that doesn't need their answer? do that while you wait.`

- When several agents work for you at once, ask each report to end with one line naming which of your
  requests it answers and when you asked it. After a few hours of asks to five terminals, a report that
  says "done, all three files are updated" is hard to place. "This was your 9:40 ask to rewrite the
  cover letter" tells you at a glance which job it closes.

  `end every report with one line that names which of my requests it answers, in my words, with the
  time I asked. if it answers more than one, name each.`

- When an agent hits "database is locked" or "file in use", have it wait and try again rather than
  delete the lock or work on a copy. The message usually means another program, often another agent,
  is writing at that moment. Removing the lock or editing a copy can lose that other writer's work.
  A short pause and a second try almost always clears it; if it does not, ask the agent to find out
  who holds it.

  `if a file or database says it is locked, don't remove the lock or use a copy. wait thirty seconds
  and try again, up to five times, and if it is still locked tell me which program is holding it.`

- When an agent fills in a web form for you, ask which fields will make the site contact someone.
  An application form may email your referees the moment their addresses go in, a booking form may
  message a host, a sign-up may invite your contacts. Tell the agent what you do not want sent yet,
  and have it list those fields and leave them empty before it presses submit.

  `before you submit this form, tell me which fields will make the site email or message anyone. leave
  the referee details empty for now; we will add them later. show me the filled form before you send.`

- When you turn down a draft, say what is wrong in a word or two and ask for a new version rather than
  a patch. "Too casual", "too long", "reads like a list" tells the agent the direction; a fresh draft
  in that direction usually reads better than the old one with words swapped. Ask it to say in one
  line what it changed, so you can tell it heard you.

  `this is too casual. write it again from the start in a formal, professional voice, keep the same
  facts, and tell me in one line what you changed.`

- Ask the agent to open the result in front of you. A path in a report means you still have to find
  the folder, pick the file and choose a program. The agent can open the video, the page or the
  document itself, in the right program, so you only have to look. For several results, it can
  open them all at once, in order.

  `open the finished <video / page / report> for me so I can look at it now. if there are several,
  open them all, in order.`

- Before you close a set of terminals, have each one write down what it was doing. A terminal you
  close takes its unsaved plans with it: the step it was on, what it was waiting for, what it
  meant to do next. One prompt to each before you close it, or one agent that reads their
  histories afterwards, keeps that work from being lost.

  `I am about to close these terminals. before I do, write down in the project notes what you were
  working on, what is finished, what is half done and what the next step was.`

- When the agent cannot reach another computer, ask it what you need to type there. Connecting to a
  second machine often needs one step only the person sitting at it can do: turning on remote
  login, adding a key, allowing a connection. The agent cannot do that from where it is, but it
  knows exactly what is missing. Ask for those steps as lines you can paste, then let it test the
  connection again.

  `if you cannot reach <the other computer>, tell me exactly what to type on it, as lines I can
  paste, and test the connection again once I say it is done.`

- When an action does nothing visible, have the agent check before it tries something else. A
  window that should have opened, a program that should have started, a file that should have
  appeared: sometimes nothing happens and no error appears. An agent that checks right away,
  sees that nothing started and tries a second way saves you from waiting on something that is
  not coming.

  `after you start it, check that it really started. if nothing came up, say so and try another
  way, and tell me which way worked.`

- When a job could cost money, ask for the price before it starts and set a ceiling. Cloud
  computers, paid models and storage are all billed by use, and a loop that runs for days can spend
  far more than one test suggested. Ask the agent to estimate the cost in plain numbers, to stop at
  a ceiling you name, and to tell you when it is halfway there.

  `before you run this on anything that costs money, tell me roughly what it will cost. don't go
  over <amount>. tell me when you reach half of it, and stop at the limit and ask me.`

- Ask for one page you can open to see where everything stands. With several agents and loops
  running, reading each terminal is slow. An agent can keep a small status page or file, one line
  per job with what it is doing, when it last moved and what it waits on, and refresh it as it
  works. Then a glance tells you what is moving and what is stuck.

  `keep one status page I can open: one line per job, what it is doing, when it last made
  progress and what it is waiting on. update it every round.`

- An agent can open a new terminal for you, already set up. When you want a second agent on
  another job, you do not have to open a window, find the folder and remember the right command and
  model name. Ask the agent you are talking to; it knows the folder, the model and the settings you
  use, and it can check that the new window actually started.

  `open a new terminal for me in my home folder with <the model> running in it, and check that it
  started.`

- Watchers often stop on their own after a while. Many agent tools give a watch a time limit,
  half an hour or so, and when it runs out nothing is watching any more, often with no message
  you would notice. If you need the watch for longer, tell the agent to start it again each time it
  ends, for as long as the thing it watches is still running.

  `keep watching <the job> until it finishes. if your watcher stops before then, start it again
  right away, and tell me if you ever had to stop watching.`

- When a loop keeps reporting "unchanged", ask once what it compared against. A check that compares
  today's state with its own note from the last round will say "unchanged" forever, even after the
  real thing broke, because both sides of the comparison came from the agent. A good check reads the
  real source each time: the file on the server, the version on GitHub, the job's own log.

  `you have said "unchanged" for a while. tell me exactly what you compared, where each side came
  from, and whether one of them is your own earlier note. if it is, check the real source now.`

- When one agent tells another that something is done, have the second one check before it builds
  on it. Agents pass each other short reports, and "the model is installed" or "the files are
  pushed" is easy to write and easy to get wrong. One quick look, the file listed or the page
  loaded, costs a minute and saves an afternoon built on a step that never happened.

  `another agent says <the step> is done. before you rely on it, check it yourself in one command,
  tell me what you saw, and only then carry on.`

- When a plan is set, ask what would make the agent change it. A plan made at the start rests on a
  few guesses: that a model is fast enough, that a computer stays free, that a result comes out as
  expected. Naming those guesses up front tells the agent what to keep an eye on, and it tells you
  which surprise in the next report actually matters.

  `you have a plan now. name the two or three things that would make you change it, and if one of
  them happens, tell me right away instead of carrying on with the old plan.`

- When the work runs on a computer you cannot see, ask for the first piece of output as soon as it
  exists. The first clip, the first page or the first row of results is the earliest point where you
  can tell whether it looks right. Waiting for the whole batch means finding a wrong setting only
  after hours of work have gone into it.

  `the moment the first piece is finished, send me where it is, or a copy, before the rest is done,
  so I can check it looks right.`

- When one message asks for several things, have the agent list them back before it starts. A long
  message typed quickly often holds four or five requests, and an agent tends to do the first two
  well and lose the last one, usually the small one at the end. A numbered list at the start, ticked
  off in the final report, makes a dropped request easy to see.

  `before you start, list every separate thing I asked for in that message, numbered. at the end,
  go through the same list and say for each one: done, not done, or waiting on something.`

- Ask to see a new check catch a known bad case. A check that has only ever passed may be passing
  because it looks at nothing: the wrong folder, an empty file, a pattern that never matches. Feed it
  one case you know is wrong and watch it complain. Then you know the green result means something.

  `before you trust this check, give it one example you know is bad and show me that it fails. then
  run it on the real data.`

- Ask the agent to name the exact variant of a model or tool it used. One model name often covers
  several things: a full release, a faster distilled one, a compressed copy that fits a smaller
  computer. They can give quite different results, and a report that just says the name leaves you
  comparing the wrong things later. Have it write the variant, the size and where it came from next
  to every result.

  `in every result you report, say exactly which variant of the model you ran (full, distilled,
  compressed, and how big), where it was downloaded from, and the settings you used.`

- When you give the same order to several agents, name one to bring the answers together. Otherwise
  each agent reports its own piece in its own window, and you are left to work out whether the whole
  job is done. One agent who collects the pieces and sends you a single short summary, with what is
  still missing, saves you reading every terminal.

  `you are the one who reports back on this. check with the other agents working on it, and when the
  whole job is done, or stuck, send me one short summary: what is finished, what is missing, who has it.`

- When a long job is too slow at full quality, ask for the whole thing at a lower setting first. A
  film rendered at a smaller size, a model trained on fewer steps or a report built from a sample
  finishes in a fraction of the time and shows you the shape of the result. You can then spend the
  slow, expensive settings only on the parts that are worth it. Ask the agent to say what the lower
  setting costs in quality, in one line, so the choice is yours.

  `full quality will take too long. do the whole thing at a lower setting first, tell me in one line
  what that costs, and list the parts you would redo at full quality.`

- When you change plans, ask the agent what it stopped. A new order often means an older job should
  end: a test, a queue, a watcher. Agents are good at starting the new thing and less good at
  noticing the old one is still running, still holding a computer or still about to send an email.
  One line on what was stopped, and what was left running on purpose, keeps the two plans from
  overlapping.

  `you have switched to the new plan. tell me what you stopped from the old one, and what is still
  running from it and why.`

- Don't let a test hold up the real work. A small test of a new tool is worth running, but if it has
  to wait for something (a free machine, a download, someone's reply) while the real job sits
  queued behind it, the computers do nothing in the meantime. Once one item has run cleanly, it is
  usually better to start the real job and judge the new tool on its first real results.

  `don't wait for the test to finish before starting the real job. start the full run now, and
  compare the first real results with the old ones when they come in.`

- When several agents work together, ask who is waiting on whom. Agents are polite: one holds its
  queue until another finishes a test, the other waits for a free machine, and both report that
  they are waiting. Each report looks reasonable, and nothing moves. A one-line list of who waits on
  whom, and for what, shows a circle like that at once.

  `list every agent on this project, what each is waiting for and from whom. if anyone is waiting
  in a circle, or waiting on something that no longer matters, tell me and unblock it.`

- If your agents work on more than one computer, give each computer a few house rules in writing.
  What it is for, what must never be touched on it, how much disk must stay free, whether it may run
  on battery. A laptop you use every day, a spare desktop and a friend's machine you were lent need
  very different care, and an agent juggling all three will mix them up unless the rules sit in a
  file it reads before it does anything there.

  `write a short rules file for each computer you work on: what it is for, what you must never touch
  there, how much disk stays free, and anything else I have told you about it. read the right one
  before you start work on a machine.`

- Before an agent edits a script or config that already works, have it keep a dated copy next to it
  and tell you the one command that puts the old version back. Most edits go fine, but when one
  doesn't, the difference between a two-second undo and an hour of reconstruction is that copy.

  `before you change this file, save a copy next to it with today's date in the name, and tell me
  the exact command that would restore it if your change goes wrong.`

- After a watcher passes its test on a dummy job, have the agent check that it also sees the real one.
  A watcher usually finds the job by its name or its command line, and the real job may be started a
  little differently from the dummy: from another folder, with a shorter path, under another name.
  Then the watcher reports that all is well while the job it was built for runs unwatched. Ask the
  agent to show you the watcher picking out the real process once it is running.

  `the real job is running now. show me that your watcher sees this exact process, by its id, and
  that it would pause it. if it doesn't see it, fix the match and test again.`

- When a job can only run part of the time, ask for the rate you will actually get, not the speed of
  one item. A render that takes twenty minutes a clip, on a computer that is free only when its owner
  steps away, may finish three clips an hour at night and none in the afternoon. The agent knows the
  per-item time from its test; the waiting is what makes the plan, so have it say both.

  `how long does one item take, and how many will actually finish per hour given when this computer
  is free? give me a realistic finish time for the whole batch, not the best case.`

- When a tool refuses to do something on a safety check, ask the agent what the check protects before
  it goes around it. Sometimes the check is too cautious and skipping it is fine; sometimes it is the
  only thing standing between you and a frozen computer. An agent that names the risk, says what will
  catch the problem if it goes wrong, and tries once while watching is very different from one that
  just adds the flag that makes the error go away.

  `that tool refused. before you work around it, tell me what the check is protecting against, what
  will stop things if it goes wrong, and then try it once while you watch.`

- Have the agent stop a long-running script before it edits that script. Some scripts, shell scripts
  especially, are read a piece at a time while they run, so changing the file underneath a running
  copy can make it do strange things later. Stop it, edit, check the edit, start it again, and look
  at the first lines of its log to see that the new version is the one running.

  `before you change a script that is running, stop it first. after the change, check it, start it
  again, and show me the first lines of its log so I know the new version is running.`

- When an agent tells you it will do something later, have it write that promise down. "I'll email
  you the comparison when the test finishes" lives only in the conversation, and a restart or a long
  session that gets summarised can drop it. A line in the task list or the NEXT file, with what was
  promised and to whom, survives both.

  `whenever you tell me you will do something later, add it to your task list in one line: what you
  promised, to whom, and what has to happen first. check that list before you say you are done.`

- A watcher that reports nothing is not the same as nothing happening. A monitor can time out, lose
  its connection or look for the wrong words in a log, and from outside that looks exactly like a
  quiet, healthy job. When a watch has been silent for a while, ask the agent to look at the job
  directly once before it trusts the silence.

  `if your watcher has said nothing for half an hour, don't assume the job is fine. look at the job
  itself, tell me what it is doing right now, and fix the watcher if it missed something.`

- Before a long batch, have the agent run and time one item first. One clip, one page, one file run
  end to end tells you how long the whole batch will take, how much memory it needs and whether the
  output looks right, before hours go into it. Ask for the timing and the estimate in plain numbers.

  `before you start the batch, run one item from start to finish, time it, show me the result, and
  tell me how long the full batch will take at that speed.`

- Before an agent deletes something large to make room, ask whether it can be brought back and how.
  A model or dataset that is also published elsewhere can go safely if the agent first checks that
  your copy matches the published one and writes down where it came from and the one command that
  fetches it again. Something that exists only on your machine needs a copy somewhere else first.

  `before you delete this to free space, check whether it can be downloaded again exactly as it is,
  write the source and the command to restore it next to where it was, and only then delete it.`

- If a loop has to run longer than the scheduler allows, put the renewal date in the prompt itself.
  Some schedulers drop a repeating job after a few days, so a ten-day loop quietly ends on day seven.
  Write the date the job must be re-created, and the date it ends for good, into the loop prompt, so
  every run reminds the agent.

  `/loop fire this every 5 minutes for the next 10 days. the scheduler drops repeating jobs after 7
  days: on day 6 re-create this job to run to <end date>, and after <end date> stop it and send me
  a final report.`

- Give every long job an off switch you can use without the agent. A small file that the job checks
  before each step (if it exists, the job finishes the current step and stops) lets you or any other
  agent stop it cleanly from anywhere, even when the session that started it is gone. Ask the agent
  to tell you the file's name when it starts the job.

  `give this job a stop file it checks before every step, so it can be stopped cleanly without you,
  and tell me where the file goes.`

- When one order covers several machines or several pieces, have the agents split it with one owner
  per piece and say who owns what. Two agents doing the same download or the same render waste hours
  and can overwrite each other; nobody doing the last piece is just as common. A short line on a
  shared board ("A has machine 1 and 2, B has machine 3, C does the re-renders once both are done")
  settles it.

  `this order touches several machines. split it with the other agents, one owner per piece, write
  the split where all of you can read it, and tell me who has what.`

- Ask a job that waits to say what it is waiting for. A queue that sits quietly behind a condition
  (the machine is busy, it is on battery, another job holds the lock) looks exactly like a job that
  hung. One line in its log each time it starts waiting, and again when it resumes, saves you and the
  next agent from killing a healthy job or trusting a dead one.

  `when your job has to wait for something, write one line to its log saying what it is waiting for,
  and another when it starts again.`

- If an agent runs heavy work on a computer someone else also uses, ask it to make the work give way
  to that person. A small watcher that pauses the job as soon as the keyboard or mouse moves, ends it
  if they keep working or memory gets tight, and starts again only after they have been away for a
  while, costs little and keeps the machine pleasant for its owner. Ask the agent to test it once
  with a dummy job before trusting it.

  `this computer is shared. before you run anything heavy on it, set up a watcher that pauses our
  work when someone is using it and stops it if memory runs low, test it with a dummy job, and tell
  me what it did.`

- Before a large download, have the agent check the free space it will leave and verify the files
  afterwards. Big model and data downloads fail half way, land in the wrong folder or fill the disk.
  A one-line rule about how much space must stay free, plus a check of every file's size or hash
  against the source when it finishes, turns "it downloaded" into something you can rely on.

  `before you download this, tell me how much disk will be left, keep at least 20% free, and when it
  is done check every file against the source and tell me the result.`

- When one agent passes on your words to another, have the second one check them at the source. A
  request that reaches an agent through a colleague can be shortened, misread or out of date by the
  time it arrives. If your own prompts are kept somewhere both can read, the second agent can find
  the original line in a few seconds before it acts, especially when money or deleting is involved.

  `if another agent tells you I asked for something, find my own words for it in <where prompts are
  kept> before you act, and quote them back to me in your report.`

- Have the agent tell you the one thing you need to do in a separate, short message. A blocker that
  only you can clear (a login, a payment, a key, a yes) gets lost when it sits in the middle of a
  long report. A short message with a plain subject, the steps in order and how long they take
  gets done the same day.

  `when you need something only I can do, send it to me as its own short message: what to do, step
  by step, how long it takes, and what you will do the moment it is done.`

- When two tools could do a job, have the agent try both on the same small piece. Reviews and
  leaderboards tell you which model or program is better in general, not on your material. Three
  examples run through each, shown side by side, settle it in an hour, before a whole project is
  built on the wrong one.

  `before we commit to <tool>, run the same three examples through it and through <other tool>,
  put the results side by side, and tell me which you would pick and why.`

- Ask what something costs before the agent spends money on it. Some steps call a paid service or
  rent a machine, and an agent working on its own may not stop to ask. A rule that it states the
  price and waits for your yes keeps the bill where you expect it, while the free work goes on.

  `if any step costs money (a paid service, a rented machine, a subscription), stop before it, tell
  me the price and what it buys, and carry on with the free parts while you wait for my answer.`

- When an agent makes pictures, video or sound, have it look at the result before it uses it. A
  script can report success on a clip that is frozen, garbled or full of noise. A few frames laid
  side by side, or a short listen, catch most of that in seconds, before the bad piece is buried
  inside something longer.

  `after you make each picture or clip, look at a few frames of it (or listen to a few seconds) and
  tell me in one line whether it looks right. set aside anything that does not.`

- Tell a generating model what you do not want, as well as what you do. Image and video models fill
  every gap with something. Ask for people "turning and breathing" and you may also get them
  talking in a made-up language. Naming what must not happen (no talking, no text, no logos) is
  often the difference between a usable result and a redo.

  `when you write prompts for the image or video model, add a line saying what must not appear,
  for example: no speech, no writing on screen, no extra people.`

- Give a long loop a cheap check first and do the heavy work only when it finds a change. Most
  rounds of a ten-day loop find the world as it was five minutes ago. A one-line test (has the
  file changed, has the other repository moved, has a reply come) settles that in seconds, and the
  slow part, a rebuild, a merge or an upload, runs only on the rounds that need it.

  `each round, first check whether <the thing> has changed since last time. if it has not, write
  one line saying so and stop. only when it has, do the full update.`

- Have agents mark each message from another agent as handled. When agents talk through a shared
  inbox, a note that was answered but never marked comes back every round, and each time the agent
  rereads it and wonders whether it owes a reply. Ask it to answer what needs an answer and mark
  everything else as seen, so the inbox shows only what is really open.

  `when you read a message from another agent, either answer it or mark it handled the same round,
  and say in one line which you did. never leave a message you have dealt with sitting as new.`

- When a loop runs the same checks every round, have it save them as one small script. Typed out
  fresh each time, five commands are five chances for a slip and a lot of reading. Saved once, the
  round becomes one line, and the script can stop with a clear message the moment a result is not
  what it expects.

  `you have run the same checks in the last three rounds. put them in one script in this folder,
  make it stop and say so when a result changes, and from now on run that script each round.`

- Keep the newest note at the top of a notes file. A loop that adds its note at the bottom makes
  every reader scroll past days of history to find where things stand. With the newest line first,
  the next round, another agent or you can read one line and know what is done and what comes
  next.

  `keep NEXT.md newest first: after each round put one dated line at the very top saying what you
  did and what comes next, and leave the older lines below it.`

- On a laptop, have long jobs check the power and the heat. A render or a long build on battery can
  drain it flat halfway through, and a laptop that runs hot for hours slows itself down or shuts
  off. Ask the agent to start heavy work only when the machine is plugged in, and to rest between
  pieces if it is getting hot.

  `before each long piece of work on this laptop, check it is on mains power and not running hot.
  if it is on battery, wait and tell me; if it is hot, pause a few minutes between pieces.`

- When you lend an agent someone else's computer, set the limits first and keep them. Say what it
  may use the machine for, how much disk must stay free, and what it must never touch or copy. Ask
  it to check those limits before each job, not once at the start, because the owner keeps using
  the machine and the free space moves.

  `you may use <the other computer> only for <this job>. keep at least a fifth of its disk free,
  check that before every job, never copy its keys or private files, and stop and tell me if a
  job would break any of this.`

- When you type fast, have the agent say back what it understood. A quick prompt full of typos is
  fine, but a long job built on a wrong reading costs an hour. One sentence from the agent before
  it starts, in plain words, lets you catch "the second film" read as "the second clip" while it
  is still cheap to fix.

  `before you start, tell me in one sentence what you think I am asking for, then go ahead unless
  that sentence is wrong.`

- Ask where every file it made ended up. "Saved it" tells you nothing a week later. With the
  folder, the file name and, for anything online, the link, you or another agent can find the work
  without a search. Have it list them at the end of the report, one per line.

  `at the end of your report, list every file you made or changed, one per line, with the full
  folder and name, and the web link for anything you uploaded.`

- Look at a long video through its stills before you sit through it. An agent can take one frame
  from the middle of every clip and lay them out as a grid of small pictures with the clip names
  under them. A minute on that page shows a black clip, a wrong order or a repeated shot, and you
  watch the full video only once it looks right.

  `take one still from the middle of every clip in this video, put them on one page in order with
  each clip's name under it, and show me the page before I watch the video.`

- When the next step waits on someone's reply, have the agent wait for the reply instead of asking
  every few minutes. Checking a mailbox on a timer spends a round each time and still answers late.
  Most agents can start a small waiter that sits until the message lands and then wakes them with
  it. Ask it to say what it is waiting for, so you know why it is quiet.

  `you are waiting on an answer from <the other agent>. start a waiter that wakes you when that
  message arrives, tell me in one line what you are waiting for, and carry on with the rest.`

- Paste the whole error, not your summary of it. "It says something about permissions" sends the
  agent guessing. The exact text names the file, the line and the program that complained, and
  the agent can often fix it from that alone. Copy everything from the first red line down, even if
  it looks like noise.

  `here is the full error, copied as it appeared. tell me in one sentence what went wrong, then fix
  it.`

- Let a loop say "nothing to do" when there is nothing to do. A loop told to make progress every
  round will sometimes invent work to look busy: a needless rewrite, a check that checks nothing.
  Tell it that a round with nothing new is fine, as long as it says so in one line and says what
  it is waiting for.

  `/loop fire this every 10 minutes for the next 3 days. do the next step in NEXT.md. if nothing can
  move this round, write one line saying what you are waiting on and stop, do not make up work.`

- Put a big file in the cloud through the folder your computer already syncs. Upload tools that an
  agent calls often refuse anything over a few megabytes, and a long video is hundreds. If your
  cloud drive shows up as a folder on the computer, the agent can copy the file there and the sync
  program does the upload with no size limit. Have it compare the copy with the original before it
  says done.

  `copy this file into my cloud drive folder, check the copy matches the original byte for byte,
  and tell me where to find it on the web.`

- Ask for one file that gathers pieces spread over several places. Clips, pages or results that
  live on two or three computers are hard to look at together. The agent can fetch them, make them
  the same size and format, add a short title before each group and join them, so you watch or read
  the whole thing at once. Ask for a list of what went in, in order, so a missing piece shows.

  `collect every finished clip of these two projects from wherever they are, join them into one
  video with a title card before each project, and give me the list of clips in the order they
  play.`

- Before a change to something that matters goes live, have a second agent read it. The agent that
  wrote a change reads it the way it meant it. A second one, asked only to read and not to change
  anything, finds the case the first one never pictured. Ask it for a verdict first, then its
  notes, each marked as blocking or not, so the first agent knows whether to stop.

  `read this change without editing anything. start with go or stop, then list what you found,
  each marked blocking or not blocking, with the line it is about.`

## 9 November 2026

- If a program you just installed is "not recognized", open a new terminal. A terminal reads the
  list of places to look for programs when it starts, so one opened before the install does not
  know the new program exists. Closing it and opening a fresh one fixes this more often than
  anything else. If it still fails, the agent can find where the program went and why the
  terminal cannot see it.

  `I installed it but the terminal says the command is not recognized. tell me whether opening a
  new terminal will fix it, and if not, find where it was installed and fix the path.`

- Make the terminal comfortable to read. Small grey text on a black window is tiring for an hour of
  work. Every terminal lets you raise the font size and pick a theme with more contrast, and the
  agent can tell you where the setting is on your computer.

  `tell me how to make the text in my terminal larger and easier to read on this computer, step by
  step.`

- Ask what a setting called an environment variable is before you set one. Install guides often
  say "set this variable" as if everyone knows how. It is a named value the computer hands to
  programs when they start, and it can be set for one terminal or for good. Knowing which one you
  set saves a confusing hour when it seems to vanish.

  `the guide says to set an environment variable. explain in two sentences what that is, then set
  it so it stays after I restart, and show me how to check it is there.`

- Have it pack a folder before you send it to someone. Zipping a whole project folder by hand
  usually sweeps in things that should not travel: a file of keys, a cache of several gigabytes, a
  copy of your notes. The agent can make the zip, leave those out, and tell you what is inside.

  `make a zip of this project that I can send to a colleague. leave out keys, passwords, caches and
  anything large we can rebuild, then list what went in and how big the zip is.`

- If every line of a file shows as changed, suspect line endings. Windows and Mac end a line with
  different invisible characters, and a file that passes between them can look entirely rewritten
  to git even though only one word changed. Ask the agent to check before you trust the diff.

  `git says every line of this file changed but I only edited one. check whether it is line endings
  and set the project up so it does not happen again.`

- Ask for results in a file you can open by double-clicking. A table printed in the terminal
  scrolls away and is hard to send. A small web page or a spreadsheet file opens with a
  double-click, keeps its layout, and can be shared or looked at again tomorrow.

  `save these results as a file I can open with a double-click, a .csv or a simple .html page, and
  tell me where you put it.`

- Put quotes around paths with spaces. A folder called My Documents or Project Notes looks like two
  separate words to a terminal, and the command fails or, worse, acts on the wrong thing. Quoting
  the whole path fixes it. Ask the agent to do this always, so a space never surprises either of you.

  `always put double quotes around file and folder paths in the commands you give me, even when
  there is no space in them.`

- Write down the package versions that worked. A project that runs today can break next month when
  a library it uses releases a new version. A short list of the exact versions installed when
  everything worked lets you, or another computer, rebuild the same setup.

  `now that this works, save the exact versions of the packages it uses to requirements.txt, and
  tell me the one command that installs them on another computer.`

- Get everything it needs before you go offline. On a train or a plane the agent itself may still
  work, but any step that downloads a model, a package or a page will fail. Ask it before you leave
  what the next few hours of work will need from the internet, and fetch it while you still can.

  `I will be offline for a few hours. list everything the next steps will need to download, get it
  now, and tell me which steps will still need the internet.`

- Ask it to walk you through new code before you rely on it. You do not need to read every line,
  but you should know what the code does with your files and what it assumes about them. A short
  walk-through in plain words often turns up an assumption that is wrong for your case.

  `walk me through the script you just wrote in plain words: what it reads, what it changes, what
  it writes, and anything it assumes about my data.`

- When it fixes a bug, ask for a test that would have caught it. A bug fixed once tends to come
  back when the code is changed later. A small test that fails on the old code and passes on the
  new one keeps it fixed, and running the tests tells the next session at once if it returns.

  `now that this is fixed, add a small test that fails on the old code and passes on the new one,
  and run all the tests.`

- Read a Python error from the bottom. The long block of text Python prints when something breaks
  ends with the line that matters: the kind of error and the message. The lines just above it name
  the file and line where it happened. Paste the whole block to the agent, but read the last line
  yourself first.

  `here is the full error. tell me in one sentence what the last line means, which line of our code
  it points to, and what you will change.`

- When there is a real choice, ask for two options and a recommendation. An agent left alone picks
  one way and builds it, and you only learn there was another way when the first one hurts. Asking
  for two, with what each costs, takes a minute and keeps the decision with you.

  `before you build this, give me two ways to do it, what each one costs in time and risk, and
  which one you would pick and why.`

- Ask for comparisons as a table. Three results described in three paragraphs are hard to hold in
  your head. The same numbers in a small table, one row per option and one column per measure, show
  at a glance which is best and where the differences are.

  `put these results in a table: one row per run, columns for the setting, the time it took and
  the score.`

- When it says something failed, ask for the exact error. "The connection failed" or "the install
  did not work" hides the one line that says why: a refused key, a missing file, a wrong version.
  The exact text is what you search for, what you paste to a colleague, and usually what tells the
  agent its own fix.

  `when something fails, show me the exact error message and the command that produced it, then
  say what you think it means.`

- To let agents use a second computer, have one set up SSH with a key and test it. A terminal on one
  machine can run commands on another over SSH, which is how one agent uses a spare desktop or a
  rented server for long jobs. The agent can make the key, tell you which half to copy to the other
  machine, and then prove the link works with a harmless command.

  `help me let you run commands on my other computer over SSH. make a key, tell me exactly what to
  copy and where, then test it by printing that computer's name.`

- Have it explain a command from the internet before running it. An install line copied from a web
  page or a forum may download and run a script you have not read. Asking first costs a minute and
  tells you what will change on your machine.

  `before you run this command, explain in plain words what it downloads, what it changes, and
  whether it needs administrator rights.`

- If you write your own hooks, wire the failure event too. In Claude Code a tool call that fails is
  sent to PostToolUseFailure, not to PostToolUse, so a hook that should react to errors and is wired
  only to PostToolUse never sees a real failure. Test the hook once with a command you know will
  fail.

  `check my hook settings: is every hook that should see errors also wired to PostToolUseFailure?
  run one failing command and show me the hook fired.`

- On a math or logic claim, have it check every small case by computer. A statement about all
  functions, graphs or numbers can usually be tested exhaustively for small sizes in a few seconds.
  A clean pass is not a proof, but one counterexample saves days, and the largest value seen tells
  you how tight the bound is.

  `before we try to prove this, write a short script that checks it on every case up to size 4,
  and on random cases up to size 7. report the worst case you found.`

- Give a long loop a second job for when the first one is done. A loop set for ten days often
  finishes its main work in two, and then spends the rest repeating the same check. Name a standing
  second task (improve the docs, add tests, look for related work) so the time is not wasted.

  `when the main job is finished, keep checking it each round, and spend the rest of the round on
  this: <second task>. say in one line which one you worked on.`

- When you ask whether an idea is already known, ask for the closest known result too. A plain "not
  found" tells you little: the search may have missed it, or the idea may sit one step from a paper
  everyone cites. The nearest published statement, and what separates it from yours, is what you
  need to judge whether the idea is new and how to describe it.

  `is this already in the literature? if not, give me the closest published result, where it is,
  and exactly what it would take to get from that result to mine.`

- Ask it to list the sources it could not read. A paywall, a failed download or a page that came
  back as binary is easy to skip over in a report, and then "no paper says this" quietly means "no
  paper I managed to open says this". A short list of what was not read tells you where to look
  next.

  `at the end, list every source you meant to read but could not open, and why.`

- Ask for the exact sentence when it says a source supports a claim. A summary of a paper can drift
  from what the paper says, especially after a long session. Asking for the line itself, with the
  section or page it comes from, lets you check it in seconds.

  `when you say a paper or document says something, quote the sentence and give its section or
  page number.`

- Have it write dates as year-month-day. 03/04/2026 is March in one country and April in another,
  and files named that way sort in the wrong order. 2026-03-04 means one thing everywhere and sorts
  correctly as plain text, in file names, folder names and tables alike.

  `write every date as YYYY-MM-DD, in file names, tables and notes. never 03/04/26 or 4 March.`

- Be suspicious of a result that looks too good. A sudden large improvement is more often a bug than
  a discovery: test data that leaked into training, a filter that dropped the hard cases, a number
  divided by the wrong total. Ask the agent to try to break the result before either of you believes
  it.

  `this result is better than I expected. before we trust it, list the three most likely ways it
  could be wrong and check each one.`

- Test new code on a case where you already know the answer. If a calculation is right, it should
  get a small example right that you can check on paper or that is printed in a textbook. Running
  that first tells you whether to trust it on the cases you cannot check.

  `before you run this on the real data, run it on a small example whose answer we already know,
  and show me that it matches.`

- Ask it to explain each command while you are learning the terminal. An agent can run twenty
  commands in a minute, and you come away with a result but no idea how it got there. One short
  line per command, saying what it does, turns every session into a small lesson.

  `I am new to the terminal. before each command you run, tell me in one plain sentence what it
  does and why you need it.`

- Ask how many cases a result rests on. "This works better" can mean a thousand examples or three.
  A finding built on a handful of cases can flip on the next one, and the agent will not always
  say so unless asked.

  `next to every finding, say how many examples or data points it is based on, and tell me if
  that is too few to trust.`

- Have it check a fix from a fresh start. A change can seem to work only because something is
  still loaded from earlier: an old setting, a file in memory, a variable set by hand. Closing
  everything and running it again from a new terminal shows whether it really works.

  `once the fix works, open a new terminal, start from nothing and run it again exactly as a new
  user would. tell me if anything differs.`

- Have it change one thing at a time when hunting a bug. Three fixes tried together may work, but
  then nobody knows which one mattered, and the other two stay in the code for no reason. One
  change, one test, then the next keeps the cause clear.

  `while we look for this bug, change one thing at a time and run the test after each change.
  undo any change that did not help before you try the next.`

- Ask it to go gently on websites. An agent downloading many pages can send hundreds of requests a
  minute, and a site will slow it down or block it, sometimes for the whole network. A pause
  between requests and stopping when the site says too many is enough.

  `when you download from a website, wait a second or two between requests, and stop and tell me
  if the site answers "too many requests" instead of retrying straight away.`

- Watch a long job's log in a second terminal. While a job runs you can open another window and
  follow its log as lines are added, without disturbing it. Ask the agent for the one command that
  does this on your computer, and keep it handy.

  `this job writes to run.log. give me the command that shows the log as it grows, for my system,
  in a second terminal window, and how to stop watching without stopping the job.`

- Ask how you could check the result yourself. Trusting a result is easier when you know one quick
  way to test it without the agent: a number to compare, a file to open, a command to run. Ask for
  that check along with every result that matters.

  `along with the result, give me one check I can do myself in under a minute that would show if
  it were wrong.`

- Ask how to take something out again before it goes in. A tool, a background task or a startup
  item is easy to add and easy to forget. Have the agent write down how to remove it at the time it
  sets it up, while it still knows every piece.

  `before you install or schedule anything, write in SETUP.md what you are adding and the exact
  steps to remove it again.`

- Have it interview you, one question at a time. When you are not sure what you want, a page of
  twelve questions is hard to answer. Ask the agent to ask one question, wait, and use your answer
  to choose the next, until it knows enough to start.

  `I want <a rough idea>. ask me questions one at a time, each building on my last answer, until
  you can write a one-paragraph plan. then show me the plan.`

- Ask it to keep an eye on the computer's memory and disk. Several loops at once can fill the disk
  or the memory without anyone noticing until everything slows down. One short check in each round
  catches it early and says which job is using the most.

  `at the start of each round, check free disk space and free memory. if either is low, tell me
  which jobs are using the most before you start anything new.`

- List the files it must never touch. Every project has a few things that must not change: a
  signed copy, a published version, a settings file another program reads. Put their names in one
  short file and ask every session to read it first.

  `read NEVER_TOUCH.md before you start. never edit, move or delete anything it lists, even if a
  task seems to need it; ask me instead.`

- Write to it in whatever language you think in. Agents read most languages well, and a request
  written in your own words is clearer than one translated in your head. Say which language you
  want the notes and the code comments in, so the brain stays readable for everyone who uses it.

  `I will write to you in Spanish. answer me in Spanish, but write the notes and code comments in
  English so the others on the project can read them.`

- Try a change to the brain on a copy first. A new way of storing or finding notes can lose things
  in ways you only notice later. Run it on a copy, compare what the copy and the original find for
  the same questions, and switch only when the copy does at least as well.

  `make a copy of the brain folder, apply the change there, and run the same ten questions on both.
  show me what each one found before we touch the real one.`

- Let the loop read its instructions from a file. A loop started with a long prompt keeps that
  prompt until you stop it. If the prompt only says to read a file and follow it, you can change
  the plan by editing the file, and the next round picks it up.

  `/loop fire this every 10 minutes for the next 7 days. read PLAN.md and do the next step it
  lists. I will change PLAN.md when I want something different.`

- Tell it when you need it by. "Make the slides" means one thing for tomorrow morning and another
  for next month. A deadline lets the agent choose how far to go, and tell you early if the job will
  not fit in the time.

  `I need this by Thursday at noon. plan the work to fit, tell me now if it will not, and give me
  a rough version by Wednesday evening.`

- Have the computer make a sound when a long job ends. Waiting on a job you cannot see means
  checking the window every few minutes. A short beep or a desktop notification at the end lets
  you do something else until it is ready.

  `when this job finishes, or fails, play a short sound and show a desktop notification with one
  line saying which.`

- Ask for short answers when you are busy. An agent will often explain everything it did when you
  only wanted the result. Say how long the reply should be, and ask for the detail only when you
  need it.

  `keep your replies to three lines unless I ask for more. if there is a problem, say it in the
  first line.`

- Ask it to say the task back before it starts. A prompt typed in a hurry can be read two ways,
  and the agent picks one without saying so. Three lines in its own words, before any work, show
  you at once whether it understood, and cost far less than an hour spent on the wrong reading.

  `before you start, tell me in three lines what you think I am asking for and what you will
  produce. wait for my yes, then go.`

- Save the heavy jobs for when you are away. A big download, a long test or a search over every
  file slows the whole computer while it runs. Tell the agent which jobs are heavy and have a loop
  start them in the evening, so the machine is quick when you sit down to use it.

  `anything that will use most of the computer for more than ten minutes, queue it in HEAVY.md
  and start it after 11 pm. during the day, do only light work.`

- Give every project its own folder and its own notes. When two projects share a folder, an agent
  working on one reads the other's notes and mixes them up. A folder per project, each with a short
  README and a notes file, keeps every session on the right job.

  `make a folder for <the project> with README.md saying what it is for and NOTES.md for what we
  learn. keep all of its files inside it and nothing from other projects.`

- Let it make the small calls itself. An agent that stops to ask about every file name and folder
  waits for you all night. Say which choices are its own and which are yours, and it keeps moving
  on the first kind and saves the second kind for one message.

  `decide small things yourself (names, folders, the order of steps) and tell me afterwards. ask
  me only about money, deleting things that have no copy, or anything public.`

- Have each round say only what changed. A loop that repeats the full status every five minutes
  buries the one new line under fifty old ones. Ask it to report the difference from the last
  round, and one short line when nothing moved.

  `in each round, report only what changed since the last one. if nothing changed, write one line
  saying so and what you are waiting for.`

- Keep a few questions you already know the answer to. After you change how the brain stores or
  finds notes, ask it the same five questions you asked before. If an answer it used to find is
  now missing, the change broke something, and you know before you rely on it.

  `here are five questions and the notes that should answer them. after any change to the brain,
  ask all five and tell me which ones no longer find the right note.`

- Tell it who will read the result. A summary for yourself, one for a colleague in another field
  and one for a referee need different words and different detail. One line naming the reader saves
  a rewrite afterwards.

  `this summary is for a colleague who knows statistics but not this project. keep it to one page
  and explain any term from the project the first time it appears.`

- Learn three keys before anything else in a terminal. The up arrow brings back the last command so
  you can run it again or change it. Tab finishes a file or folder name for you. Ctrl+C stops what
  is running. With those three, most of the fear of the terminal goes.

  `I am new to the terminal. show me the up arrow, Tab and Ctrl+C on a harmless command, and tell
  me how to copy text out of this window on my computer.`

- Use a loop to follow new papers in your field. Keeping up with a busy subject takes an hour a day
  by hand. A daily loop can search for new papers on your topics, write one line on each and keep
  the ones that touch your work in the brain, so the reading list builds itself.

  `/loop fire this every day for the next 30 days. search for new papers on <your topics> from
  the last day, write one line on each in READING.md, and put the ones that bear on our work into
  the brain with a note on why.`

- Ask it to review changes before you accept them. When another person, or another agent, hands you
  a batch of changes, a second agent reading them cold catches things the author stopped seeing: a
  file deleted by accident, a test switched off, a number changed without a reason.

  `read the changes in this branch as a reviewer. list anything deleted, any test removed or
  skipped, and any number or setting changed, with the file and line for each.`

- Check on your loops from your phone. You do not have to be at the computer to know a long job is
  fine. If each loop sends a short email or writes its progress to a page you can open on your phone,
  a glance on the bus tells you whether to worry.

  `once an hour, email me three lines: what you finished, what you are on now, and anything that
  needs me. keep it short enough to read on a phone.`

- Give every script a --help. A script that only its author knows how to call is lost the moment
  that session ends. A few lines of help, printed when the script is run with --help, tell the next
  person or agent what it does and what it needs.

  `add a --help option to every script you write here: one line on what it does, the arguments it
  takes, and one example command.`

- Keep a file of open questions. Every project has things nobody knows yet: why a number moved,
  whether a source can be trusted, which of two methods is right. Written in one place, they get
  answered one by one; left in old chat sessions, they are forgotten.

  `keep OPEN_QUESTIONS.md: one line per question we have not answered, with the date it came up.
  when you answer one, move it to the bottom with the answer and where you found it.`

- When one step is blocked, have it move to the next and say so. A loop that waits on a single
  missing file or a password can sit idle all night. Tell it to note what is blocking, go on with
  work that does not depend on it, and check the blocked step again later.

  `if a step is blocked on something only I can do, write what you need from me at the top of
  NEXT.md, carry on with the next task that does not depend on it, and retry the blocked one each
  hour.`

- Ask what it needs from you, in one list. Questions scattered through a long report are easy to
  miss. One short list at the end, of things only you can give (a login, a decision, a file),
  turns a stalled job into a few minutes of your time.

  `end the report with a list headed "Needed from you" naming each thing only I can provide. if
  there is nothing, leave the list out.`

- Turn a routine you keep explaining into a skill. If you tell every new session the same five
  steps (where the notes are, how to search them, what to check before saving), write them once as
  a skill file. The agent loads it when the task comes up, and you stop repeating yourself.

  `write a skill called brain-search that explains, step by step, how to search my notes and read
  a result in full. keep it under a page and test it in a new session.`

- Ask it to note which copy of the brain it is reading. With the brain on two computers, or a
  laptop copy and the one on GitHub, an answer can come from the stale one. One line naming the
  folder and the date of its last update makes that visible.

  `before you answer from the brain, say which copy you read (the folder) and when it was last
  updated. if it is more than a day old, pull the newest one first.`

- Hand a new person a starter prompt, not a tour. Someone joining a project learns fastest when
  their first session starts from a prompt that names the goal, the main folders and the rules.
  Ask the agent to write that prompt from what it knows of the project.

  `write a starter prompt a newcomer can paste into their first session: what this project is for,
  where the notes and code live, the three rules that matter most, and a first small task.`

- Give a loop a heartbeat file. From outside, a loop that is working and a loop that hung an hour
  ago look the same: a quiet terminal. If every round writes the time to one small file, a glance at
  that file tells you whether it is still going.

  `at the end of every round, write the current time and one line on what you did to
  HEARTBEAT.txt in the project folder, replacing what was there.`

- Know when a scheduled loop runs out. Some agent tools let a recurring job run only a fixed number
  of days before it lapses on its own, which is shorter than "for the next 10 days". Put the end
  date in the loop prompt and have the agent renew the job before it lapses.

  `/loop fire this every 5 minutes until 19 November 03:00. if the scheduler stops the job before
  then, create it again with the same prompt, and after 19 November 03:00 stop it and send me a
  final report.`

- Have each round leave one dated line. A loop that only changes files gives you no story of what
  it did overnight. One line per round in a progress file, newest at the top, reads in a minute
  and shows where the night went.

  `after each round, add one line at the top of PROGRESS.md: the date and time, what you finished,
  and what you will do next.`

- Ask it to say what it did not check. A report lists what passed, and the reader assumes that is
  everything. One line naming the parts it skipped, or could not test, tells you where the remaining
  doubt is before you rely on the result.

  `end every report with a line starting "Not checked:" that names anything you skipped or could
  not test. write "Not checked: nothing" only if that is true.`

- Have it write a short description under each picture in public pages. Someone using a screen
  reader, or reading on a slow connection, sees only the text. A sentence saying what the picture
  shows costs nothing and makes the page readable for them.

  `for every image in the docs, add alt text of one sentence saying what it shows, not just its
  file name.`

- Clean a log before you post it for help. A log pasted into a forum or an issue often carries your
  user name, home folder, machine name or email address. Ask the agent to replace those with
  placeholders first and show you the result before you share it.

  `before I post this log, replace my user name, folder paths, machine name and any email address
  with placeholders like <user> and <path>, then show me the cleaned version.`

- Have it keep the original next to a translation. A translated page reads smoothly even where it
  is wrong, and nobody can tell which sentence drifted. With each paragraph of the original above its
  translation, a reader who knows a little of both languages can check the parts that matter.

  `translate this document paragraph by paragraph, with each original paragraph directly above its
  translation. mark any sentence you were unsure how to translate.`

- Ask it to turn a recording into notes with times. A transcript of an hour-long call is too long to
  reread, and a summary alone loses the exact words. Short notes with the minute each point was
  made let you jump back to the recording when the wording matters.

  `transcribe this recording, then write one-line notes of each decision and question with the
  minute and second it was said. keep the full transcript in a separate file.`

- Have it fill in a form and list what it left blank. An agent filling a form from your notes will
  sometimes guess a missing date or number to make the form look complete. Asking for the gaps as
  a list keeps every guess out of the form and in front of you.

  `fill in this form from my notes. leave a field empty if the notes do not say it, and list every
  empty field at the end instead of guessing.`

- Have it pull tables out of a PDF into a spreadsheet. Numbers locked in a PDF report are slow to
  copy by hand and easy to mistype. An agent can extract them into a CSV, but PDF tables break in
  odd ways, so ask it to check a few rows against the page.

  `extract the tables on pages 4 to 9 of this PDF into one CSV each. then pick five rows at random
  and show me them next to the same rows read from the page.`

- Ask it to turn a long log into a short timeline. A night of output from a loop is thousands of
  lines. What you want in the morning is ten: when it started, what finished, what failed and when
  it stopped.

  `read last night's log and give me a timeline of at most ten lines, each with the time and what
  happened. put any failure first.`

- Ask which files it actually read. An agent can describe a project confidently after opening two
  files out of forty. A short list of what it looked at tells you how far to trust the description.

  `at the end of your answer, list the files you opened to get it. if you are guessing about any
  part, say which.`

- Ask it to check the key number a second way. A result that comes out of one script has only been
  computed once. Working it out again by a different route, even a rough one, catches the slips
  that rereading the same code never will.

  `before you report the final figure, get it a second way (a different script, a hand calculation
  or a smaller sample) and tell me whether the two agree.`

- Ask it to read back what it saved. A save can fail quietly: a full disk, a wrong folder, a file
  cut short. Reading the first and last lines back, or checking the size, takes a second and turns
  "I saved it" into something you can trust.

  `after you write an important file, read back its first and last few lines and its size, and tell
  me if anything looks cut short.`

- Keep one fact to a note. A note that covers five things gets found for one of them and then has
  to be read in full every time. Short notes with one fact each, linked to each other, are easier
  for an agent to find and to correct when one of them turns out wrong.

  `when you add to the brain, write one fact per note, with a title that says the fact, and link it
  to the notes it relates to.`

- Ask it to say which folder it is working in. With two copies of a project, or a terminal that
  opened somewhere unexpected, an agent can edit the wrong one and report success. One line naming
  the folder at the start of a task makes that mistake visible before it costs anything.

  `at the start of each task, tell me which folder you are working in and which copy of the project
  that is. stop and ask if it is not the one I meant.`

- Have it write a version a colleague could follow. Notes written for the agent itself are full of
  shorthand. When you want to pass work on, ask for a short page that someone who was not there
  could pick up: what the goal is, what is done, how to run it and what is left.

  `write HANDOVER.md for someone new to this project: the goal, what works now, the one command to
  run it, and what is still to do. no shorthand.`

- Keep each run's output in the same shape. If a weekly report comes back with different columns or
  headings every time, comparing one week with the next turns into a puzzle. Ask the agent to fix the
  layout once and keep to it.

  `use the same headings and column order every time you write this report, so this week can be put
  next to last week. if you need a new field, add it at the end.`

- Ask whether a number makes sense before it is reported. A script can print a total ten times too
  big because a file was read twice, and the agent will pass it on as calmly as a correct one. One
  question about size and sign catches most of these before you see them.

  `before you report a number, say whether its size and sign make sense against what you would
  expect, and why. if it looks off, check it before telling me.`

- Have it put the most important finding first. A review or audit that lists twelve points in the
  order they were found makes you read all twelve to learn which one matters. Sorted by how much
  each one matters, the first two lines are often enough.

  `list your findings from most to least important. mark anything that would change a result or
  lose data at the top.`

- Ask what it would do with more time. When a job is finished but rough, the agent usually knows
  where the weak spots are. Asking costs one line and gives you the next round of work in its own
  words.

  `when you finish, add a short list: what you would improve or check next if you had another hour,
  most useful first.`

- Ask it to match the style already in the project. A new script written in a different style from
  the ones around it, with other naming, other indentation and another way of reading settings, makes
  the whole project harder to follow. Have the agent read two or three existing files first.

  `before you write new code here, read two of the existing scripts and follow the same naming,
  layout and way of handling settings.`

- Have long jobs print where they are. A job that runs for an hour in silence gives you no way to
  tell a slow run from a stuck one. A line every few minutes with how far it has got and roughly how
  long is left settles that at a glance.

  `for anything that runs longer than a few minutes, print a progress line every so often: items
  done, items left and a rough time remaining.`

- Ask it what it expects before it runs anything. If the agent writes down the result it expects
  before a test or a calculation, a surprise shows up straight away instead of being explained after
  the fact. Most real mistakes turn up as a result nobody predicted.

  `before you run this, write one line saying what result you expect and why. afterwards, say whether
  it matched and what you make of it if it did not.`

- Have it put big numbers in terms you already know. 40,000 rows, 3 GB or 0.2 seconds mean little
  on their own. Compared with something familiar, like a day of data or a film's size, you can tell
  at a glance whether a number is fine or wrong.

  `when you report a size, a count or a time, add a short comparison that tells me whether it is a
  lot or a little for this project.`

- Ask for the smallest version that works first. A full tool planned all at once takes longer and
  hides its mistakes until the end. A rough version that does one thing end to end shows you early
  whether the idea is right, and the rest can be built on it.

  `build the smallest version that does the whole job once, roughly. show it to me before you add
  options, polish or speed.`

- Ask what it could not check. A report that sounds complete may rest on a step the agent could not
  run: a page that would not load, a file it had no permission to open, a test that timed out. A short
  list of what went unchecked tells you where the soft spots are.

  `end your report with a list of anything you could not verify, and why: no access, too slow,
  missing file. if there is nothing, say so.`

- Ask which words it searched for. When an agent says the brain or a folder has nothing on a topic,
  it often searched for one phrase that the notes happen to word differently. Seeing the search terms
  lets you suggest the words you would have used.

  `when you search the notes or the brain and find nothing, show me the exact words you searched for
  and try two other ways of saying it before you give up.`

- Keep other people's details out of anything you share. Notes and logs pick up names, email
  addresses and phone numbers without anyone deciding to keep them. Before a file goes into a public
  repository or to someone else, have the agent look for them.

  `before this goes anywhere public, search it for names of people, email addresses, phone numbers
  and home addresses, and list what you find so I can decide what to remove.`

- Keep the prompt next to what it made. A picture, a report or a summary is much easier to improve
  when you can see the exact request that produced it. Ask the agent to save the prompt beside each
  output, so the next attempt starts from what was asked rather than from memory.

  `whenever you make an image, report or summary, save the prompt you used in a .txt file with the
  same name next to it.`

- Check that a scheduled job really ran. A job set to run every night can stop without a sound: a
  password expires, a folder moves, the computer was asleep. Ask the agent to look at what the job
  produced and when, not at whether it is scheduled.

  `for each scheduled job in this project, find the newest file it wrote and tell me when that was.
  flag any job whose newest output is older than it should be.`

- Have it read the first error, not the last. When a long build or script fails, the last lines are
  often a pile of errors caused by the one near the top. An agent fixing the last message can chase
  symptoms for a while; the first one is usually the cause.

  `when this fails, find the first error in the output, not the last one, and start from there.`

- Have it ask before anything leaves your computer. Reading and writing files on your own machine
  is easy to undo. An email sent, a post published or a file uploaded to a shared folder is not. A
  rule that the agent stops and shows you the thing first costs one extra reply.

  `you may read and write files here freely, but before you send an email, post anything or upload a
  file anywhere, show me exactly what will go and wait for me to say yes.`

- Ask for charts whose axes do not mislead. A bar chart whose axis starts at 95 makes a two percent
  difference look like a doubling, and an agent will pick whatever range the plotting library
  chooses. Asking for honest axes, labelled with units, keeps the picture true to the numbers.

  `start bar chart axes at zero, label both axes with their units, and if you zoom in on a small
  range, say so in the caption.`

- Test it on data it has not seen. Code tuned on one file will often work on that file and nothing
  else, because the agent fixed each problem it met there. Keeping a second file aside and running
  it only at the end shows whether the code works in general.

  `build this using january's file only. when you think it is done, run it once on february's file
  and tell me what broke, without changing anything first.`

- Give a hard problem a time budget. An agent stuck on a bug will keep trying variations for as long
  as you let it, and an hour can go by on the fifth version of the same idea. Saying how long it has,
  and what to hand back when the time runs out, turns a dead end into a short report you can act on.

  `spend at most twenty minutes on this. if it is not fixed by then, stop and tell me what you tried,
  what you ruled out and what you would try next.`

- Ask for a second source on any fact that matters. A date, a figure or a quote that one web page
  gives can be a copying error passed along from page to page. Two independent sources that agree are
  worth far more than one, and when they disagree you want to know.

  `for every number or date that the conclusion rests on, find a second source that does not copy the
  first. if the two disagree, show me both.`

- Ask it to lay out the options before a choice you will live with. Picking a library, a file format
  or a way to store data is cheap to change on day one and expensive a month later. Two or three
  options with what each costs and gives up let you choose instead of inheriting its first idea.

  `before you pick a database for this, give me two or three options, what each is good and bad at
  for this project, and which one you would choose.`

- Keep outputs in their own folder. When results land beside the scripts that made them, the code
  folder fills with files nobody can tell apart from source, and a clean-up can delete the wrong
  thing. One output folder can be emptied and rebuilt without touching the code.

  `write every generated file to out/ and nothing generated next to the scripts. I should be able
  to delete out/ and get it all back by running the scripts again.`

- Ask it to round only at the end. Rounding a number halfway through a calculation and then using
  the rounded value again lets small errors pile up, and the final figure drifts. Keep full
  precision inside the work and round once, for display.

  `keep full precision in every intermediate step and round only the numbers you show me at the
  end.`

- Have it comment the surprising parts, not the obvious ones. A comment that says "add one to the
  counter" helps nobody. A comment that says why a value is skipped or why a strange-looking step is
  needed is the one a later reader, or a later agent, actually needs.

  `add a short comment wherever the code does something a reader would not expect, saying why. do
  not comment lines that already say what they do.`

- Have it look for repeated rows. A file joined twice, an export run two days running or a copy
  pasted by hand can leave the same record in the data more than once, and every total built on it
  is then too high. A quick count of repeated rows and IDs catches it early.

  `before any totals, check the data for repeated rows and repeated IDs, tell me how many there are
  and show me two examples.`

- Ask it to check that the parts add up to the whole. When a report splits a total by month, region
  or category, the pieces should sum back to the total. If they do not, something was dropped or
  counted twice, and it is far easier to find now than after the report has gone out.

  `whenever you break a total into parts, add the parts back up and show me that they match the
  total. if they do not, find out why before going on.`

- Have it draft the message you need to send. Once the work is done there is often an email or a
  note to write about it, and the agent already knows the details. A short draft in plain words
  that you edit and send yourself saves the last half hour of the job.

  `when you finish, draft a short email I could send to a colleague about the result: what we did,
  what we found and what happens next. do not send it; leave it for me.`

- Ask for one name per thing, everywhere. When the same column is price in one script, px in another
  and close in a third, every later change has to remember all three, and a search finds only one.
  Picking a single name and using it in code, files and notes keeps the project searchable.

  `use one name for each thing across every script, file and note. if you find two names for the
  same thing, list them and ask me which to keep.`

- Have it check how big a file is before reading all of it. An agent that opens a two-gigabyte log
  in one go can stall, run out of memory or fill its own working space with lines it does not need.
  The size and the first few lines are usually enough to decide how to read the rest.

  `before you read a file in full, check its size and line count. if it is large, read the first
  and last few lines and search it instead of loading the whole thing.`

- Ask it to use a date library rather than doing the arithmetic by hand. Adding thirty days, finding
  the last business day of a month or counting the days between two dates goes wrong around month
  ends, leap years and clock changes. A tested library already handles those.

  `do date and time arithmetic with a proper date library, never by adding numbers to days or
  months yourself, and show me one example around a month end.`

- Ask for short functions that each do one job. A two-hundred-line function that reads, cleans,
  computes and plots is hard to test and hard to change without breaking something. Small pieces
  with plain names can be checked one at a time and reused later.

  `keep each function to one job and under about forty lines. if one grows past that, split it and
  tell me what the pieces are.`

- Have it use the official download or API before scraping a page. A scraper breaks the day the
  site changes its layout, and some sites forbid it. Most data sources have a proper download link
  or API that is steadier and often faster.

  `before you write code that scrapes a web page, check whether the site offers a download or an
  API for the same data, and use that if it does.`

- Ask it to open the output in the program you will use. A file can be written without errors and
  still come out wrong in the place you need it: dates that turn into numbers in a spreadsheet,
  columns that run together, a chart that is blank. One check in the real program catches that.

  `after you write the file, open it the way I will (in a spreadsheet, a browser or a PDF viewer)
  and tell me whether it looks right there.`

- Ask for variable names that say what they hold. Code full of x, tmp, df2 and data_new reads fine
  on the day it is written and is a puzzle a week later, for you and for the next agent. A name
  like daily_prices or rows_after_cleaning explains itself.

  `name variables for what they hold, like daily_prices or failed_files. no single letters outside
  short loops, and no tmp, new or 2 in a name.`

- Have it check file sizes before it commits. One large data file or video added by accident makes
  every later clone slow, and it stays in the history even after it is deleted. A quick size check
  before each commit catches it while it is still easy to undo.

  `before every commit, list any file over 10 MB that is about to be added and ask me before
  including it.`

- Ask it to write files so an interruption cannot leave half of one. A script stopped in the middle
  of writing leaves a truncated file that looks real and breaks the next step. Writing to a
  temporary name and renaming at the end means the file is either the old one or the whole new one.

  `when a script writes an output file, write it to a temporary name first and rename it only once
  it is complete.`

- Ask for tables sorted by what you care about. A table in whatever order the data happened to come
  in makes you hunt for the row that matters. Sorted by the column you will act on, the answer is
  usually in the first line or two.

  `sort every table you give me by the column that matters most for the question, largest first,
  and say which column you sorted by.`

- Have it read the release notes before an upgrade. A newer version of a library or tool can rename
  an option or change a default, and the failure shows up somewhere far from the upgrade. A short
  read of what changed, before installing, tells you what to test.

  `before you upgrade any package, read its release notes from my version to the new one and list
  anything that could affect this project.`

- Do not let it run things as administrator unless it must. An agent that hits a permission error
  will sometimes reach for admin rights, which lets a mistake touch the whole computer instead of one
  folder. Ask it to stop and explain why it needs them first.

  `never run a command as administrator or with sudo without asking me first and saying exactly why
  it needs it.`

- Have it list the assumptions it made. Every piece of work rests on a few guesses about what you
  meant: which file, which year, whether blanks count as zero. Written down at the end, they take
  seconds to check, and a wrong one is caught before it spreads into the next step.

  `at the end of your answer, list every assumption you made that I did not state, one per line.`

- Ask it to read the whole function before changing a line. An edit made from a three-line window
  can contradict something twenty lines further down, like a variable reused later or an early
  return. Reading the whole thing first is cheap and prevents the change that looks right and is not.

  `before you edit a function, read all of it and the functions it calls, tell me in one sentence
  what it does and what else the change touches, then make the change.`

- Have it say what period the data covers. A result from one month of data and the same result
  from ten years mean very different things, and the dates are easy to leave out. One line with the
  first and last date makes every number easier to judge.

  `in every report on data, give the first and last date in the data and the number of rows used.`

- Compare every result with a simple baseline. A model that predicts sales to within ten percent
  sounds good until you learn that "same as last week" does just as well. Ask the agent to put the
  plainest possible method beside its answer, so you can see what the clever part adds.

  `next to every result, show what a simple baseline gets (the average, or the last value carried
  forward), so I can see how much better the method really is.`

- Ask it to check that a backup can be restored. A backup that has never been opened is a hope,
  not a backup. Have the agent restore one file from it into a spare folder and compare it with the
  original.

  `after you set up the backup, restore one file from it into a temporary folder and confirm it is
  identical to the original. tell me if anything differs.`

- Have it read the formulas in a spreadsheet, not just the numbers. A total that looks right can
  come from a formula that skips a row or points at the wrong sheet. Ask the agent to list the
  formulas behind the key cells and check what each one covers.

  `open the spreadsheet and list the formula behind every total and average, with the range it
  covers. flag any that leave out rows or refer to another sheet.`

- Keep the settings in one file. When a folder name, a threshold or a date range is typed into
  five scripts, changing it means finding all five, and the one you miss gives a quietly different
  answer. One small settings file that every script reads keeps them in step.

  `move every setting that appears in more than one script (paths, dates, thresholds) into
  settings.toml and have the scripts read it from there.`

- Ask what it did with blank and missing values. Empty cells get dropped, filled with zero or
  carried forward from the row above, and each choice changes the result. The agent will pick one
  without saying so unless you ask.

  `before you analyse this table, tell me how many values are missing in each column and what you
  plan to do with them. do not fill or drop anything until I agree.`

- Have it show what a search pattern matches before it changes anything. A find-and-replace across
  many files can hit far more than intended: a short word inside longer ones, a name in a comment.
  A list of the matches first costs a few seconds.

  `before you replace anything, list every line the pattern matches, with file names, and wait for
  me to say go.`

- Ask for a time limit and a retry on anything that goes over the network. A download or an API
  call with no time limit can hang for hours and look like the agent is still working. A limit of a
  minute or so, with two or three retries and a short wait between them, turns a silent hang into a
  clear error.

  `give every network call a timeout of 60 seconds and retry it up to three times with a growing
  wait. if it still fails, stop and tell me which address failed.`

- Have it draw charts that colour-blind readers can follow. Red against green is the most common
  pair in a default chart and the one many people cannot tell apart. A palette made for colour
  blindness, plus line styles or labels on the lines, costs nothing.

  `use a colour-blind-safe palette in every chart, and label each line directly instead of relying
  on colour alone.`

- Ask for page numbers when it reads a long document. A summary of a sixty-page report is only as
  good as your ability to check it. Page numbers next to each point let you open the original and
  see the sentence for yourself.

  `summarise this PDF section by section and put the page number after every point, so I can check
  any of them against the original.`

- Ask it to tag the versions that worked. A project goes through good states and broken ones, and
  finding the last good one in a long history is slow. A git tag on each version you were happy
  with gives you a name to go back to.

  `when a version works and I say so, tag it in git with a short name like v1-working and the date,
  and tell me the tag.`

- Have it count rows before and after every cleaning step. Removing duplicates, blanks or bad
  dates can quietly throw away far more than expected. A count before and after each step shows
  at once where data went missing.

  `print how many rows there are before and after each cleaning step, and stop and tell me if any
  step drops more than five percent.`

- Ask for a proofread before anything goes public. A README, a post or an email written in a hurry
  carries typos, a wrong name or a half-finished sentence. One pass by the agent before it leaves
  your computer catches most of them.

  `before this goes public, proofread it for spelling, grammar, names and numbers, and list what you
  changed.`

- Have it make a small fake dataset to practise on. When the real data is private, huge or slow to
  load, a hundred made-up rows with the same columns let the agent build and test the code freely.
  Once it works, you point it at the real file.

  `make a small fake version of this file with the same columns and about 100 made-up rows, save it
  as data/sample_fake.csv, and build the script against that first.`

- Ask for a one-line caption under every chart and picture. A chart pasted into notes means little
  a week later without a word on what it shows. A caption saying what is plotted, from which data
  and what to notice makes it readable on its own.

  `under every chart or picture you make, add one line saying what it shows, which data it came from,
  and the one thing to notice.`

- Have it save a copy of a web page you depend on. Pages change or disappear, and a project built on
  a rule or a table from one can lose its footing. Ask the agent to keep a dated copy in the project
  so you can always see what it said.

  `this page matters to the project. save a copy of its text in sources/ with today's date and the
  address in the file name.`

- Ask which account it is using before anything online. Many people have a personal and a work
  login for the same service, or two cloud projects. An agent that uploads, sends or creates
  something under the wrong one makes a mess that is slow to undo. One line naming the account first
  catches it.

  `before you upload, send or create anything online, tell me which account and project you are
  logged into and wait for my yes.`

- Have it take out its debugging lines when it is done. While chasing a problem an agent adds extra
  print lines, test values and commented-out code. Left in, they clutter the output and confuse the
  next reader. A last pass to remove them keeps the code clean.

  `when the fix works, remove any print lines, test values and commented-out code you added while
  debugging, and show me the final diff.`

- Ask for commands you can paste exactly as written. A command with a placeholder like <your
  folder> or a step that says "then run the usual thing" fails when you try it. Full commands, one
  per line, ready to copy, save time and guessing.

  `when you give me a command to run, write it in full with real paths and values, one per line, so
  I can paste it as it is.`

- Have it check that the links in your notes still open. Notes collect links to pages, files and
  other notes, and some of them stop working as things move. A quick pass that tries each one and
  lists the dead ones keeps the notes trustworthy.

  `go through the links in NOTES.md and README.md, try each one, and list the ones that no longer
  open, with a suggested replacement if you can find one.`

- Ask how a number was worked out. A total, an average or a percentage in a report is only as good
  as the steps behind it. Having the agent write the formula and the inputs next to it lets you
  redo the sum yourself in a minute.

  `for each number in your summary, show how you got it: the formula, the inputs, and the file they
  came from.`

- Ask it to read the documentation for the version you have. Tools change their options between
  versions, and an agent working from memory may use a flag that no longer exists or means
  something else now. Checking the installed version first avoids a confusing error.

  `before you use this tool's options, check which version is installed and read its help for that
  version, not what you remember.`

- Ask for a dry-run switch on anything that moves, deletes or sends in bulk. A script that renames,
  moves or removes files, or emails a whole list, should be able to print what it would do without
  doing it. You read the list, and only then run it for real.

  `give this script a --dry-run option that prints every file it would move or delete and changes
  nothing. run it that way first and show me the list.`

- Have it compare files with diff instead of reading both. Two long versions of a file look the
  same at a glance. A diff shows exactly which lines changed, and the agent can paste it so you can
  check the change yourself.

  `compare the old and new config with diff and show me only the lines that changed.`

- Point it at a file instead of pasting a long text. A page of pasted data or notes gets cut, wrapped
  or mixed up with your instructions. Save it to a file and give the agent the file name; the
  instructions stay short and the data stays whole.

  `the data is in notes/input.txt. read it from there; my instructions are only what I type here.`

- Have it work on a branch for anything risky. A branch is a side copy of the project inside git.
  If the experiment works you merge it, and if it does not you throw the branch away and the main
  line never knew. It costs one command and makes a bold change cheap to try.

  `make a new git branch before you start this change. tell me its name, and do not merge it into
  main until I have looked at the result.`

- Keep the question with the answer. A results file read a month later often makes no sense,
  because nobody remembers what it was trying to find out. One line at the top saying what was
  asked, and when, turns a bare table into something a stranger can use.

  `start every results file with one line saying the question it answers and the date. keep that
  line when you update the file.`

- Ask it to save text as UTF-8. Names with accents, quote marks and symbols turn into strange
  characters when one program writes a file in one encoding and another reads it in a different
  one. Saying the encoding once in the prompt avoids a slow, confusing hunt later.

  `save every text, csv and json file you write as UTF-8, and read files as UTF-8 too. if a file
  will not read that way, tell me instead of guessing.`

- Ask for output in a fixed order. If a script prints its results in whatever order the computer
  happens to find them, two runs that agree look different, and a real change hides among the
  shuffled lines. Sorted output can be compared line by line.

  `sort every list and table your scripts write, by name or date, so I can compare two runs with
  a simple diff.`

- Have it show a few rows of the result, not only the count. "Wrote 4,812 rows" says nothing about
  whether the rows are right. Five real lines from the output let you spot a wrong column, a
  shifted date or an empty field at a glance.

  `after each step that writes a file, print the first five rows of it so I can see what it looks
  like.`

- Ask scripts to say so when they find nothing. A search that quietly prints nothing looks the same
  as one that never ran. One line saying "no matches for ..." tells you the script worked and the
  answer really is empty.

  `when a script finds nothing, have it print a line saying what it searched for and that nothing
  matched. never exit silently.`

- Ask for a .gitignore before the first commit. Without one, an agent will happily commit caches,
  large data files and the odd file with a key in it, and getting those back out of the history
  is far harder than never putting them in.

  `before the first commit, write a .gitignore that leaves out caches, virtual environments, large
  data files and anything holding a key or password. show it to me first.`

- Have it write commit messages that say why. "Update script" tells nobody anything a month later.
  One plain sentence about what changed and why makes the history useful when you are hunting for
  the day something broke.

  `write each commit message as one short sentence saying what changed and why, like "skip empty
  rows so the totals stop coming out low".`

- Ask for two lines at the top of every script. When a folder fills up with scripts, the quickest
  way to know what each one does is a short note at the top saying what it is for and how to run
  it. The agent writes it in seconds; you save minutes every time you come back.

  `at the top of every script you write, add a two-line comment: what it does, and the exact
  command to run it.`

- Ask for a time zone on every date and time. A log line that says 14:00 means one thing on your
  laptop, another on a server and a third in a spreadsheet someone opens abroad. Writing the zone,
  or using UTC throughout, saves a confusing hour of mismatched records later.

  `store and print every time with its time zone, or in UTC with a Z at the end. never a bare
  clock time in a file.`

- Have it tell you when the job turns out bigger than it looked. A small fix sometimes opens onto
  a much larger problem, and an agent left alone will often keep digging for hours. A quick note
  at that point lets you decide whether the bigger job is worth doing now.

  `if this turns out to need more than about an hour, or changes to more than three files, stop
  and tell me what you found before going further.`

- Ask it to install things inside the project, not system-wide. A package installed for the whole
  computer can break another project that needed a different version. A virtual environment or a
  local folder keeps each project's tools to itself.

  `install any packages this project needs into a virtual environment in the project folder. ask
  me before installing anything for the whole computer.`

- Have it describe the data before it analyses it. How many rows, which dates, how many values are
  missing: three facts that catch a truncated download or a wrong file before any chart is drawn
  from it.

  `before any analysis, tell me how many rows the file has, the first and last date in it, and how
  many values are missing in each column.`

- Ask for error messages that say what to do. "KeyError: 'price'" means something to the person who
  wrote the script and nothing to anyone else. A message that names the problem and the fix saves
  the next person, or the next session, a search.

  `when your scripts fail, make the error say in plain words what went wrong and what to try next,
  like "no price column in input.csv; check the file has a header row".`

- Keep one small example that runs. A folder with a tiny input and the one command that uses it
  shows a new reader, or a new agent, how the tool is meant to work faster than any page of
  explanation, and it doubles as a quick check that nothing is broken.

  `make an examples/ folder with one small input file and a short note giving the exact command to
  run on it and what the output should look like.`

- Ask for numbers rounded to what they mean. A result printed as 0.43829174 suggests a precision
  nobody measured, and the extra digits hide the part that matters. Two or three significant
  figures are usually honest and much easier to compare.

  `round the numbers in your reports to two or three significant figures unless I ask for more.
  keep the full values in the data files.`

- Keep one command that rebuilds everything. When a result comes from five scripts run in the
  right order, nobody remembers the order a month later. A single script that goes from the raw
  data to the final figures makes the work repeatable by you, a colleague or a new session.

  `write run_all.sh (or run_all.py) that rebuilds every output from the raw data in the right
  order, and keep it working whenever you add a step.`

- Fix the random seed. Anything that shuffles, samples or trains gives a slightly different answer
  each run, and then you cannot tell a real change from noise. A fixed seed makes the same run give
  the same result.

  `wherever the code uses randomness, set a fixed seed and write it in the output, so running it
  again gives the same numbers.`

- Ask for paths that work on another computer. A script that opens a file by its full path from
  your home folder breaks the moment someone else runs it, or you move the folder. Paths written relative to the
  project folder travel with it.

  `use paths relative to the project folder, never a full path that starts with my user name or
  drive letter. if a path must be set per computer, read it from one settings file.`

- Have it name files for what they hold. A folder of final.csv, final_v2.csv and final_really.csv
  tells nobody which one to trust. A name that says what is inside and when it was made settles it
  without opening anything.

  `name every output file for what it contains, like prices_cleaned_2026-11-09.csv. never final,
  new, v2 or copy in a file name.`

- Ask it to check the licence before it copies code. Code found online is not always free to reuse,
  and a pasted function can carry terms you never agreed to. A one-line check before copying is far
  cheaper than finding out later.

  `before you copy code from a website or another repository, tell me where it came from and what
  licence it is under. if there is no licence, write it yourself instead.`

- Ask it to point at the file and line. "The function already handles that" is easy to say and
  hard to check. When the agent makes a claim about code or notes, have it name the file and line
  number, so you can open it and see for yourself in seconds.

  `when you tell me what some code does, give the file and line number you are reading from.`

- Have it write the unit next to every number. A result of 0.4 could be a fraction, a percent, a
  number of seconds or of gigabytes. Units cost a word and stop the kind of mix-up that is
  invisible until much later.

  `write the unit next to every number you report: seconds, percent, GB, dollars, rows. never a
  bare number.`

- Keep the original data untouched. An agent cleaning a file will sometimes write the cleaned
  version over the original, and then there is nothing to compare against or start again from. Ask
  it to treat the raw folder as read-only and write everything new elsewhere.

  `treat everything under data/raw/ as read-only. write cleaned or processed files to data/work/
  and never overwrite the originals.`

- Ask what else would break before a change. A file or setting is often read by more than one
  script. Before the agent changes it, have it search for everything that uses it, so a fix in one
  place does not quietly break three others.

  `before you change this function, find every place that calls it and tell me which of them the
  change could affect.`

- Have it try the awkward inputs. Code that works on a clean example often fails on an empty file,
  a very large one, a name with an accent or a date in another format. Ask the agent to try a few
  of those on purpose.

  `after it works on the normal case, try it on an empty input, a very large one and one with odd
  characters, and tell me what happened with each.`

- Ask for a simple diagram of how the parts connect. Once a project has more than a handful of
  scripts and folders, a picture of what feeds what is easier to hold in your head than any list.
  A plain text diagram in the README is enough.

  `draw a short text diagram in README.md showing which scripts read which files and what each one
  produces.`

- Say what is out of scope. An agent fixing one thing will happily tidy three others on the way,
  and each extra change is one more thing to review. Naming what it should leave alone keeps the
  work the size you asked for.

  `fix the date parsing only. do not reformat, rename or reorganise anything else, even if it
  looks wrong; list it at the end instead.`

- Ask for the answer first and the reasoning after. A long explanation that ends in a conclusion
  makes you read everything to find out what happened. One line with the answer, then the detail
  for anyone who wants it, is faster to read and easier to check.

  `start every report with one line that answers the question. put the reasoning and the details
  underneath.`

- Keep a list of the services a project uses, without the passwords. When a project touches a
  cloud account, an email sender or an API, a new session has no idea those exist until something
  breaks. A short file naming each one and what it is for fixes that.

  `write SERVICES.md listing every outside service this project uses and what it is for. never put
  a password or key in it; say where the key is kept instead.`

- Ask for a short summary at the top of long notes. A note that grows over weeks gets read from
  the top by the next agent, and the conclusion is often buried at the bottom. Two or three lines
  at the head saying what it found and what is still open save every later reader the scroll.

  `keep a three-line summary at the top of each note you write: what it is about, what we found,
  and what is still open. update it when the note changes.`

- Give it a real sample of the input. A description of the data ("a CSV of prices") leaves the
  agent guessing at column names, date formats and empty cells. Twenty real lines settle all of
  that before it writes code that breaks on the first file.

  `here are the first 20 lines of the real file. read them before writing the parser, and tell me
  anything in them that surprises you.`

- Have it date what it finds online. A version number, a price or a rule copied from a web page is
  true on the day it was read. Ask the agent to write the date and the address next to each fact,
  so a later session knows how old it is and where to check again.

  `when you take a fact from a web page, write the date you read it and the page address next to
  it in the note.`

- Tell it how sure the answer needs to be. A quick estimate for a chat and a number that goes into
  a paper need very different amounts of checking. Say which one you want, and the agent can spend
  a minute or an hour accordingly.

  `this is a rough estimate for my own planning, a few minutes of work is enough.` or `this number
  goes into a paper: check it two independent ways before you give it to me.`

- Have it reproduce a bug before fixing it. A fix written from a description often fixes something
  nearby. Ask the agent to make the error happen first, then fix it, then show the same steps no
  longer fail.

  `before you change any code, reproduce the error with the smallest example you can. then fix
  it, and run the same example again to show it is gone.`

- Turn the questions you keep asking into a FAQ. If you ask an agent the same thing every week,
  where a file lives or how to restart a job, the answer belongs on a page, not in your head. Ask
  it to collect them.

  `look through what I have asked you more than once and write FAQ.md with each question and a
  short answer. add to it whenever I ask something again.`

- Have it read a tool's own help before guessing. Agents remember options for most tools, and
  sometimes they remember an older version or a different tool. Running the tool's help first
  costs a second and saves the error that follows a made-up option.

  `before you use a command-line tool you have not used in this project, run its --help and use
  the options it actually lists.`

- Ask it to link each new note to related ones. A brain is more than a pile of notes: what makes
  recall work is the links between them. When the agent saves something, have it name two or
  three earlier notes that bear on it.

  `when you save a new note to the brain, add links to the two or three existing notes most
  closely related to it, and say in a few words how they connect.`

- Let long jobs run in the background. A build, a download or a big test run does not need the
  agent to sit and watch it. Ask it to start the job in the background, carry on with something
  else, and come back when it finishes.

  `start the long job in the background and write its output to a log. while it runs, work on the
  next item, and check the log when it is done.`

- Show it an example of what you do not want. One bad example often teaches more than a page of
  rules: the report that was too long, the paragraph that sounded like a brochure, the chart nobody
  could read. Point at it and say what is wrong with it.

  `here is an example of what I do not want: <file>. it is too long and buries the answer. keep
  your report unlike this one.`

- Ask it to send long output to a file. A command that prints ten thousand lines floods the
  terminal and fills the agent's memory with noise. Have it write the output to a log and show you
  only the last few lines, or the lines that matter.

  `when a command prints a lot, send its output to a log file and show me only the last 20 lines
  and any errors.`

- Have it make shortcuts for what you type every day. If you start the same three things each
  morning, or retype the same long command, the agent can turn it into one short command or a
  small script with a clear name.

  `look at the commands I run most often and make short scripts or aliases for the ones I type
  every day. tell me their names.`

- Give it a place to park ideas for later. A good agent notices ten things worth doing while it
  works on one, and chasing them is how a two-hour task becomes a lost afternoon. A short ideas
  file keeps them without derailing the job.

  `if you notice something worth doing that is not part of this task, add one line to IDEAS.md and
  carry on. we will go through the list when this is finished.`

- Have it check that a library is alive before relying on it. Agents pick packages from memory,
  and some of those were abandoned years ago. A quick look at when it was last updated and whether
  people still use it saves a rewrite later.

  `before you add a new package, check when it was last released and whether it is still
  maintained. if it looks abandoned, suggest an alternative.`

- Tell it which files are generated. Some files in a project are built by a script: an index, a
  table, a page made from data. An agent that edits one by hand loses the change at the next build.
  Say which files are made, and from what.

  `INDEX.md and the tables under results/ are built by make_index.py. never edit them by hand;
  change the script or its inputs and rebuild.`

- Keep every result next to the command that made it. A number in a report is only useful if
  someone can make it again. Ask the agent to write the exact command and input files under each
  result, so a later session can rerun it instead of trusting it.

  `under every result you report, give the exact command and the input files that produced it, so
  anyone can run it again and get the same answer.`

- Prefer plain text formats. Notes in Markdown, tables in CSV and settings in a small text file can
  be read by any agent, searched by any tool and compared line by line. Spreadsheets, word files
  and binary formats hide their contents from all three.

  `save notes as .md and tables as .csv unless I ask for something else, so other agents and tools
  can read and search them.`

- Ask what it would need to finish without you. An agent that stops every half hour for an answer
  is usually missing one thing: a password it cannot have, a rule nobody wrote down, a choice only
  you can make. Ask once and fix the cause.

  `what would you need from me to finish this without asking me again? list it, and I will give
  you what I can in one go.`

- Ask it to explain each command in one line. If the terminal is new to you, the agent is also the
  best teacher you have. A short note beside each command it runs turns a month of watching into a
  working knowledge of the terminal.

  `while you work, put one plain line under each command you run saying what it does, so I can
  learn the terminal as we go.`

- Have it look for an existing script before writing a new one. In a project that has run for a
  while, the tool it is about to write often already exists under another name. Ask it to search
  first; a second copy of the same tool is how two versions drift apart.

  `before you write a new script, search the project for one that already does this or nearly
  does. if you find one, use it or extend it, and tell me which.`

- Start a fresh session when it goes in circles. A very long conversation fills up with old
  attempts, and the agent starts repeating fixes it already tried. When that happens, ask it to
  write down where things stand, then open a new session with that note.

  `we are going in circles. write NOTES.md with what works, what failed and the next step, and I
  will start a fresh session from it.`

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
