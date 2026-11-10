# Why a terminal, and how to get one

## Why the brain works better in a terminal

A chat window answers one message at a time and forgets most of it. A terminal agent runs on your
own computer, with your files, and the brain is built around that:

- Hooks. The framework installs small scripts that run when a session starts, before each prompt
  and before each tool call. They hand the agent its memories, the scars from past mistakes and the
  notes the brain thinks are relevant. Hooks only run in a terminal agent.
- Loops. `/loop` keeps an agent coming back to a job every few minutes for days
  ([loop-prompts.md](loop-prompts.md)). A chat window cannot do that.
- Compaction. When a long session fills its context, the terminal agent summarises it and keeps
  going. The framework saves each summary as a brain node, so the next session can read where the
  last one stopped.
- Skills. A skill is a folder with a `SKILL.md` that teaches the agent a procedure. The agent loads
  it when a task matches. See [../../agent_tools/skills/](../../agent_tools/skills/).
- Files and git. The agent can read the brain, run recall, write a memory and push it to GitHub
  itself. In a chat window you would be copying text back and forth.

If you have been trying the brain in a chat window and it felt like nothing happened, this is
usually why.

## Getting a terminal

You already have one.

- Windows 11: Windows Terminal is installed. Press the Windows key, type `terminal`, open it. On
  Windows 10, install "Windows Terminal" from the Microsoft Store.
- macOS: Applications, then Utilities, then Terminal. Many people use iTerm2 instead; either works.
- Linux: your desktop's terminal (often Ctrl+Alt+T).

You also need Python 3.10 or newer (`python --version` to check) and git (`git --version`). If
either is missing, the next step can install them for you.

## Installing a terminal agent

Claude Code (Anthropic). Check the official install page for the current command; at the time of
writing it is:

```
# macOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

# or, with Node.js 18+ installed, on any system
npm install -g @anthropic-ai/claude-code
```

Then type `claude` in the terminal and sign in.

Codex CLI (OpenAI):

```
npm install -g @openai/codex
codex
```

Both read instruction files in your home folder (`CLAUDE.md` for Claude Code, `AGENTS.md` for
Codex). The brain's installer writes those for you.

## Let the agent install the rest

Once one terminal agent runs, it can set up everything else. Start it in your home folder and paste:

```
I want to set up the brain framework from github.com/yspennstate/math-brain-public on this
computer. Check that Python 3.10+ and git are installed and install them if not. Clone the
repository somewhere permanent, read framework/bootstrap/README.md, do the dry run of the
installer, show me what it plans, and after I say yes run it with --apply --merge-settings.
Then start a new session and tell me what the wake-up message says.
```

The agent will ask before it changes anything outside its folder. Read what it plans and say yes.

## Where to start the agent

Start it in the folder you want it to work in. For general brain work that is your home folder,
because that is where the installer puts the instruction file and the hooks look for the memory
folder. For a project, start it in the project folder; the brain's hooks still run.

Keep the window open while a loop runs. Loops live inside the session, and closing the window ends
them.

## Several terminals, one job each

Once one agent works well, open a second terminal for a second job rather than giving the first
agent two. Each terminal gets one task, its own folder and its own loop. Give each a short name in
its first prompt, so its notes and its saved memories say which job they belong to. If two jobs
touch the same files, have the agents claim a file before they edit it (the framework's mesh does
this), or keep them in separate folders.

```
you are the <name> agent. your only job is <task>, in <folder>. keep your ORDER and NEXT files
there. before you edit anything outside that folder, check that no other agent has claimed it.
```

## After a restart

A restart closes every terminal, and every loop with it. The work itself is safe if the agents
kept their ORDER and NEXT files current. Open one terminal per job again and paste:

```
the computer restarted. read <folder>/ORDER.md and the first line of <folder>/NEXT.md, check what
actually finished before the restart, and carry on from there. start the loop again with the
same end date as before.
```

If you run many terminals, keep a short list of them, one line each with the folder and the
loop prompt, so reopening them after a restart takes minutes instead of an evening.
