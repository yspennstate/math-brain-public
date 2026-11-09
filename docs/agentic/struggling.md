# If the brain does not seem to do anything

Go down this list in order. Most problems are the first two.

1. You are in a chat window. The hooks, loops, compaction notes and skills only run in a terminal
   agent on your computer. See [terminals.md](terminals.md).

2. The agent finishes and waits. That is what agents do without a loop. Give it a loop prompt
   ([loop-prompts.md](loop-prompts.md)) and leave the window open.

3. The agent does not seem to know anything. Start a new session and look at the first message: the
   wake-up hook should print a block that starts with the brain's status and some memories. If it
   does not, the hooks are not wired. Run the installer again with `--merge-settings`, or paste:

   ```
   check that the brain's hooks are in my settings file and that the wake-up script runs. show me
   its output. fix what is missing.
   ```

4. Recall returns nothing useful. The brain only knows what has been written to it. Ask the agent
   to save memories as it works (see [starter-prompts.md](starter-prompts.md)), and ask with two or
   three different wordings: the way a note would say it, not the way the question says it.

5. The loop stopped. Loops end when the terminal closes and expire after seven days in Claude Code.
   Start the session again and give the loop again; if the agent kept ORDER and NEXT files, it
   picks up where it was.

6. The agent keeps redoing the same work. It is not writing its results down. Tell it to keep a
   one-line NEXT note and to save anything durable to the brain each round.

7. Agents on the same computer collide. Install the mesh from the framework (agents claim what they
   are editing) and tell each agent to check claims before changing shared files.

8. The computer is slow. Several loops and agents at once use real memory and CPU. Run fewer at a
   time, or start the heavy ones on another machine.

Still stuck: paste this into the agent.

```
the brain is not helping me the way I expected. read docs/agentic/ in the math-brain-public
repository, check my setup against it step by step, and tell me what is missing.
```
