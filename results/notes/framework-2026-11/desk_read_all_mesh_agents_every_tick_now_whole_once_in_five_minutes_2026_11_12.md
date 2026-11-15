---
name: desk_read_all_mesh_agents_every_tick_now_whole_once_in_five_minutes_2026_11_12
description: "Agent desk service.log says 'mesh read slow' with the time in agents? Until 12 Nov the desk read every row of the mesh's agents table (11,366) on each tick; a last_seen filter would still SCAN. Now whole once in 5 minutes, live rows through idx_agents_live each tick (0.006 s against 0.6 s, same rows). Run EXPLAIN before adding a WHERE to cut a read"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T03:56:54+02:00
  status: provisional
  evidence: "agent_run/mesh_lock/test_desk_agents.txt (13 of 13, control fails), live_desk_agents.txt (0 of 11,367 rows differ); ledger row of 12 Nov (p)"
---

The Agent desk (~/agent-desk/agent_desk_service.py) asked the mesh database for every row of its
agents table on every collector tick: 11,366 rows on 12 Nov, ten columns each with the task text, every 3 s with a
viewer open and every 30 s without. link_mesh() then dropped in Python every row older than six hours. The timing
line added at 03:24 on 12 Nov ("mesh read slow: N s (agents x, claims y, tasks z; n agents)" in service.log, written
when the read takes 2 s or more) fired three times in 29.5 minutes: 4.5 s, 5.4 s and 3.1 s. A mesh writer ready to
commit waits for a reader, so this is one source of the commit waits in mesh_slow.log. It is not shown to be the
only one.

A filter on last_seen would not have helped: EXPLAIN QUERY PLAN shows SCAN agents with or without it, because the
table has only its primary key and idx_agents_live ON agents(lease_until) WHERE status NOT IN ('done','offline').
An index on last_seen would be a mesh landing that every pulse then maintains.

What landed at 03:53 on 12 Nov, inside the desk only (_mesh_agents): the table is read whole at most once in 300 s
(AGENTS_FULL_EVERY). Between those reads each call reads the rows that can change: those in idx_agents_live with a
lease in the last six hours (29 rows on the live file, plan SEARCH agents USING INDEX idx_agents_live), and by
primary key the rows that were in that set at the last call and are not now, which is how an agent that said bye
shows as done on the same tick. When the database refuses the read the desk serves the rows of its last read and
logs it; before, it showed no mesh agents. A mesh file without the index is read as before.

The limit: a row that changes while it stays done or offline shows the change at the next whole read, up to 5
minutes late. Nothing the desk shows depends on that today.

Checks: mesh_lock/test_desk_agents.py, 13 of 13 on a throwaway database with the live schema, the same answer as the
old read in every case, 30 SQLite steps on a tick against 1,954, and the old file against itself fails that line.
Still to measure: "mesh read slow" lines per hour after the landing against about 6 an hour before, and whether the
claims and tasks statements (2.5 s each once) need the same treatment. tasks is a SCAN (no usable index).

How to apply: before adding a WHERE to cut a slow read, run EXPLAIN QUERY PLAN; a filter on an unindexed column
reads the same pages. Look for a partial index the writer already maintains and ask for a superset through it.
Rollback: agent_desk_service.py.bak_agents_20261112, then restart through STOP and launch.vbs.

