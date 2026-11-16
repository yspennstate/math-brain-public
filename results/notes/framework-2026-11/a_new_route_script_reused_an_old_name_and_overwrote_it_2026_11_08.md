---
name: a_new_route_script_reused_an_old_name_and_overwrote_it_2026_11_08
description: "[VERIFIED] P0434 8 Nov: a new w3tie script overwrote route item 28's w3tie of the same name; push_paths' removal guard caught it, old file restored from origin. List a route folder before naming a script."
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:53:52-05:00
  status: provisional
  evidence: "commit 31070528; origin 32c5ce28 holds the old w3tie"
---

On 8 Nov I wrote a new script as w3tie_agent.py in my P0434 route folder, which already held a w3tie (route item 28) with that exact name. The cat > overwrote my local copy, and the push guard refused because origin/main would lose 30 lines. I restored the old file from origin/main with git show and renamed the new one w3tielim.

The folder holds about 150 files from one day, and short names like w3tie get reused easily. Before writing a new script into a route folder, list the folder for the name, or pick a name that has never been used there. The push_paths.sh removal guard (ALLOW_REMOVALS) is what caught it. Without it, item 28's tie check would have been replaced on GitHub.


Recurrence 8 Nov 13:58 (an agent): the name check ran as `ls w3slope* ; cat > w3slope_agent.py` in ONE command, so ls printed the clash only after the write had already overwritten item 27's script. Restored from the brain repo copy (on origin as 08c1b99); the new one became w3slope2. Fix: run the ls on its own and read its output before writing, or write with `set -o noclobber` so an existing name fails loudly.
