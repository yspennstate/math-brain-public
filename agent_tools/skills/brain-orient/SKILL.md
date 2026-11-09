---
name: brain-orient
description: Orient in the brain before substantive work - read the wake-up message, recall what is known and what went wrong before on the task, and decide what to trust. Use at the start of a session or a new task, or when someone says "check the brain first".
---

# Orienting in the brain

The brain is a folder of memories (one fact per file), an index, a graph of links between them and
the scripts that search it. A session that starts without reading it repeats old work and old
mistakes. This takes a minute.

1. Read the wake-up block the session-start hook printed. It names the brain's state, the newest
   memories and anything flagged as broken. If no block appeared, the hooks are not installed;
   say so and run the installer before going on.

2. Recall the task, with two or three wordings in one call. Word them the way a note would say it
   (the object, the method, the name), not the way the question is phrased:

   ```
   python brain.py recall "<wording 1>" --or "<wording 2>" --or "<wording 3>"
   ```

3. Recall the mistakes in the same area:

   ```
   python brain.py recall "<area> mistakes"
   ```

4. Open the two or three notes that look most relevant (`python brain.py node <slug>`) and their
   neighbours (`python brain.py neighbors <slug>`).

5. Weigh each note. A note says "this resembles a place we have been", not "this is right here".
   Check its status line (verified, provisional, superseded) and whether what it describes still
   matches what you see. A superseded note points to the one that replaced it; read that one.

6. Say in two or three lines what you found, what you will rely on and what you will check, then
   start the work.

If recall finds nothing after three rounds of different wordings, the brain does not have it. Say
so, do the work, and write what you learned back with `brain.py remember` so the next session
finds it.
