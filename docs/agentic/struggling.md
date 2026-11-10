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

9. The agent stops halfway and says it is done. Agents like to report early. A loop helps, and so
   does writing the finish line into the prompt: what has to exist, and how the agent proves it.

   ```
   do not stop until <the result> exists and you have checked it yourself. if you are about to stop
   for any other reason, write down what is left, then keep going on it.
   ```

10. Work stopped overnight. The computer went to sleep, and every loop and job on it paused. Ask the
    agent to keep it awake while the work runs, and to check that the setting survives a restart.

    ```
    my jobs stopped while I was away, probably because the computer went to sleep. keep it awake
    while our work is running, show me how you did it, and check it still holds after a restart.
    ```

11. Jobs fail with odd errors about writing files. The disk is full. Do not let the agent delete
    to make room without a copy somewhere else first.

    ```
    check how much free disk this computer has. if it is low, list the biggest folders we made, move
    finished results to <the backup place>, check the copies, and only then remove the local ones.
    ```

12. The agent says its usage ran out. Most plans have a limit per few hours or per week. If you
    have a second account or another agent program, keep a terminal open on it as a fallback, and
    keep the ORDER and NEXT files current so the other one can pick the work up mid-stride.

13. The agent keeps stopping to ask you questions, and the loop waits for an answer while you are
    away. Most of those questions have a sensible default, so tell it once to decide those itself.
    Keep the real questions (money, deleting something that has no second copy, publishing) for
    you, sent one way you will actually see, and let the work that does not depend on the answer
    carry on.

    ```
    decide small things yourself and tell me what you chose in the report. if something really
    needs me, write one short question with your recommendation at the top of <folder>/QUESTIONS.md
    (or email it), then keep working on whatever does not depend on the answer. never stop and wait.
    ```

14. The agent says the job is done, but when you look, the file is not there, or the change never
    reached GitHub. A report is easy to write and a step is easy to skip, especially near the end
    of a long round. Ask for proof that you can check in ten seconds: the path of every file it
    wrote and the commit hash of every push. Then check one of them yourself now and then. An
    agent that knows its report gets checked tends to check its own work before writing it.

    ```
    end every report with the full path of each file you changed and the commit hash of each
    push. before you write "done", open the file or run git log on the remote and confirm the
    change is really there. if it is not, say so and fix it instead of reporting it as done.
    ```

Still stuck: paste this into the agent.

```
the brain is not helping me the way I expected. read docs/agentic/ in the math-brain-public
repository, check my setup against it step by step, and tell me what is missing.
```
