# Fixes from one bug hunt

Between 10 and 15 November 2026 one agent swept the framework's own logs for faults: hook errors, jobs that hung,
daemons started twice, pushes that reported success and were not on GitHub. Each fix below was tested before it
landed, on a copy first and then on the live file, and each records what was seen before and what the test showed
after. Fixes to private parts of the deployment are left out. 40 fixes are listed.

## 1. hook dispatcher: a raise in its own code skipped every hook of every session in silence

Change: hook_dispatch.py falls back to hook_dispatch.lkg.py (same payload, arguments, exit code) when its own code raises; the copy is promoted from the live file after it has stood 600 s unchanged and completed a run; the fatal log line keeps the error name (was cut at 400 chars); HOOK_DISPATCH_LOG / HOOK_DISPATCH_LKG env overrides for tests

Before: six incidents 18 Sep - 10 Nov (36 fatal lines; 19 over 7 min on 1 Nov; 9 in 4 s at 19:30 on 10 Nov, NameError _arm_deadline): exit 0, no hook ran, nothing surfaced it

After: test_lkg.py 12/12: old code broken the 10 Nov way = exit 0 and no output; new code = the last-known-good copy runs, exit code and stderr relayed, non-ASCII payload intact, no second fallback, no promotion of a fresh edit; old and new agree on --selftest (27 checks)

Not covered: a file that does not compile (SyntaxError) never reaches the fallback; nothing in the wake check reads the fatal lines yet

## 2. hook dispatcher: an edit landed by hand left the fast list stale (every hook spawning) four times, 17 Sep - 10 Nov

Change: hook_dispatch_land.py is the one way to land a dispatcher edit: refuses on a moved base sha, compiles the copy, runs its --selftest against the live file's, breaks the copy with a NameError in main() and requires the last-known-good fallback to run, backs up, re-signs hook_dispatch_allow.json ahead of the replace and again after it, then reads what the log gained (fatal, fallback ran, stale list). hook_liveness.py prints 'dispatcher raised N time(s) in 24 h' and reports it as bad. The dispatcher docstring named a re-sign tool that never existed (hook_dispatch_allowlist.py); it names the lander now ()

Before: 10 Nov 21:55:40-22:06:29, my own hand landing: list stale for 11 min, PostToolUse 8.9 s against 0.14 s, PreToolUse calls with 295 hooks over 200 s; 21 Sep the same for 32 h; 36 fatal lines since 18 Sep that no check read

After: first landing through the tool 22:22:03: list signed 10 ms after the dispatcher, 30 dispatches in the next 25 s, 0 fatal, 0 fallback runs, 0 stale lines. Liveness block controls 5/5 (quiet log, served and skipped raises counted exactly, a test copy's traceback not counted, no log = UNKNOWN); on the real log it reads 9 raises on 10 Nov in 0.9 s

Not covered: an edit made with a plain file write still bypasses the lander (the reflex on hook_dispatch.py edits should name it); the liveness block's path match is slash-sensitive until the follow-up lands

## 3. bm25 refresh: MemoryError while writing the index (6 in bm25_refresh.log: 15 Oct, 30 Oct, four in a row on 9 Nov 04:22)

Change: bm25.py _write_json_text emits the text of json.dumps(payload) in pieces (_json_pieces: a large dict or list goes to the C encoder 256 entries at a time, flushed every 8 MB) instead of building one 234-million-character string

Before: one json.dumps of the payload: 232 MB of extra private memory while writing; the refresh died and published nothing when that allocation failed

After: same bytes as json.dumps on the live payload (233,683,627 bytes, same sha256, also in each writer's own process); 33 MB extra while writing; time at parity in three alternating warm rounds (old 4.33/3.38 s, new 3.68/4.37 s); first refresh with it at 01:06 on 11 Nov wrote 61,710 docs and the file on disk equals json.dumps of its loaded payload

Not covered: the gzip compressor and the reader (json.load of the whole index) still hold the full payload; the control's 1.5x timing check is unreliable on a cold, loaded machine (failed once at 1.56x from page-in)

## 4. core_steer.py daemon ran twice after every boot (two logon launchers, no single-instance check)

Change: single_instance(): a named mutex taken at the top of main(); a second copy writes one log line and returns before any sweep; --restore unguarded; a failed mutex call lets the daemon run

Before: core_steer.log: two starts at each of the last three boots (18 Oct 00:56/00:58, 2 Nov 08:56/08:57, 10 Nov 16:36/16:38); on 10 Nov both copies alive with dead parents, 83 and 339 cpu-seconds, each sweeping every process every 5 s and writing the same state file

After: test_single.py 10/10 on the copy and on the live file: second process refused while the first lives, next start is the daemon after the holder exits or is killed, main() of a second copy returns at once with no sweep, removing the guard gives the old file byte for byte

Not covered: the two copies running since 10 Nov keep the old code until the next boot (not stopped); the second logon launcher is not identified

## 5. nothing ran core_steer_selftest.py, so a failing check sat unread from 18 Sep to 11 Nov

Change: hook_liveness.py gains SELFTESTS and _run_selftests(): each listed selftest runs as a windowless child under each listed interpreter flag set (core_steer_selftest.py with and without -s); a failure goes into _artifact_bad, so it reaches.liveness_status.json and the wake line; a run that does not finish in 120 s is printed as a note, not raised; HOOK_LIVENESS_SELFTESTS=0 skips the section

Before: no hook, dream step or scheduled task ran the selftest; its last two failures were found by hand on 11 Nov

After: test_selftest_runner.py 17/17 on the copy and on the live file, 1 fails on the old file; control_old_daemon.py: with the pre-fix daemon beside today's selftest the runner raises the no-psutil check under both runs and the post-bridge check under -s; full live run prints the section with two ok rows and adds nothing to the status file

Not covered: slow_sense_selftest.py, bm25_lane_selftest.py, graph_lane_ties_selftest.py, math_answer_closure_selftest.py and graph_fire/owner_convention_selftest.py are still run by nothing (slow_sense passes by hand; the others were not run: sizes unknown on a starved box); the full liveness run took 154 s on the loaded laptop

## 6. the shared GitHub REST quota hit zero twice in 80 minutes and every API push waited 300 s at a time

Change: push_paths_gitdata.py tries a GraphQL lane first: read the tip with our paths' blobs, then createCommitOnBranch with expectedHeadOid; contents ride in the mutation; same refusal rules as the REST lane, which stays as the fallback (other file modes, over 200 paths or 20 MB, any GraphQL error; PP_GQL=0 switches it off); the tally row counts GraphQL requests

Before: 01:42-02:42: 1,554 REST calls from 49 pusher runs on this laptop, 191 ref updates tried, 248 blob uploads, six calls per lost race; core quota 5000 of 5000 used at 01:22 and at 02:37 while GraphQL stood at 1 of 5000; one push at 02:47 on the old code cost 48 REST calls

After: a try is 2 GraphQL requests and 0 REST calls; first real landings 02:50 (try 1, and another agent's push 13 s later); test_gql_lane.py 24/24 on the live file, 16 fail on the old; probe_real_github.py PASS against the real API without landing anything

Not covered: the Mac minis' copies until they take the mirror; about two thirds of the hourly REST calls are outside the laptop's tally; a rewound main is not detected by this lane; an hour-long after-measurement is still owed

## 7. math hook edge reader (math_sense._revision_edge_reader) and the selftests nothing ran

Change: the reader declines (whole-edge read) for a store with no connection instead of raising AttributeError, as its docstring already said; the distinct edge kinds come from one index seek per kind instead of a walk of the whole kind index; math_answer_closure_selftest.py gets --quick (fixtures plus a dozen live answer targets, a different dozen each day, on a three-kind edge read); hook_liveness SELFTESTS lists slow_sense, graph_lane_ties and math_answer_closure --quick beside core_steer, an entry may carry script arguments, and a check printed as 'FAIL <label>' is named by its label

Before: math_answer_closure_selftest.py red at its first fixture (AttributeError: 'FakeStore' object has no attribute 'connection') with nothing running it; reader build 0.025-0.027 s best of 7 on the live store (167,685 edges, 12 kinds); the selftest's full run 84 s; one selftest on the liveness schedule

After: selftest 7/7 on the full run (208 live answer targets) and on --quick in 1 s; reader build 0.011 s, 1,757 records and the pools of 16 answer targets identical to the old file's; four selftests on the schedule, five runs in 8 s; test_selftest_runner.py 23/23 on the live file (5 fail on the old one); test_closure_reader.py all pass

Not covered: the whole-edge fallback itself costs 17.5 s on today's store (an unknown edge kind, a query error or a non-ASCII id in the pool would put it on a math prompt); bm25_lane_selftest.py writes the live index and owner_convention_selftest.py runs over 170 s, so neither is scheduled; the saving per math prompt is about 0.015 s, small

## 8. improvement ledger appends (ledger_append.py)

Change: the ledger tool appends through GraphQL first: one query for the tip of main and the ledger's blob id there, the blob's bytes from the local clone (main fetched once if the clone lacks it; the bytes must hash to the id), createCommitOnBranch with expectedHeadOid, and the landed blob id in the reply must be the hash of the bytes sent; a moved tip is retried up to 15 times, a lost reply is followed by a fresh read so a row is never added twice; the REST contents route it used since 2 Nov stays as the fallback (LEDGER_GQL=0 forces it); one row per run in the laptop's call tally

Before: at 03:25 on 11 Nov a ledger row failed HTTP 403: the REST core allowance (5,000 an hour, shared by every agent, computer and connector on the account) read 5000 of 5000 used, and the tool had no other route; each append cost 4 REST calls

After: at 03:39, with the REST allowance still at 0 left, the same row landed on try 1 in commit using 2 GraphQL requests and 0 REST calls; a second run of the same rows added nothing; test_ledger_append.py 16 controls on a fake (moved tip, a peer's row landing in between kept, lost reply, rate limit and missing local blob hand over to REST, CRLF and no-final-newline files, a landed blob that differs is rc 1) and 3 on the real API (a 1,610,449-byte append against the tip's parent is refused as stale and the ledger is unchanged), all pass

Not covered: the route needs a local clone of the repository to read the 1.6 MB ledger (GraphQL truncates a blob's text); without one it falls to REST; a tip that moves under 15 tries in a row also falls to REST; the Mac minis' copies of the tool, if any, are not changed

## 9. API pusher, GraphQL lane (push_paths_gitdata.py _gql_kind)

Change: a moved tip that GitHub reports as FORBIDDEN 'is at <oid> but expected <oid>' (the tip moved while the commit was being made) is now read as stale and retried on the new tip through GraphQL, like the STALE_DATA wording; it was read as 'other' and sent the push to the REST lane; the ledger tool's GraphQL route reads the same wording as stale

Before: hour 02:50-03:50 on this laptop: 44 pusher processes, 32 landed on GraphQL with 0 REST calls, 8 tried GraphQL and fell back to the REST lane (201 REST calls, 23 ref tries), 4 took the REST lane without a GraphQL mutation (75 calls); my own 03:46 push was one of the 8: one GraphQL mutation refused with that wording, then 32 REST calls and four ref tries

After: test_gql_lane.py 26 controls, 0 failed on the live file; the new control (two tips moved mid-commit, then a landing: six GraphQL requests, no REST call) fails on the old file with exactly the 03:46 log line; hour before the GraphQL lane (01:42-02:42): 52 pusher processes, 1,566 REST calls, 191 ref tries; hour after (02:50-03:50): 276 REST calls from the pusher, 82 pct fewer, and 201 of those were this fallback

Not covered: I read the cause in one of the eight fallbacks (my own push log); the other seven left no log I can read, so the share of them that had this wording is not measured; the four REST-only runs are not explained yet (more than 200 paths, a non-plain file mode, or a failed tip read); the Mac minis' copies of the pusher are not changed

## 10. math index build (math_prefilter.py build, the publish of brain.sqlite3.prefilter.pkl and.lexdf.pkl)

Change: both files are now published by one step, _publish: a temp name that carries the pid and the thread, and a move that is tried again while a reader has the destination open (45 s in all, env MATHBRAIN_PREFILTER_PUBLISH_WAIT), with the temp file removed whatever happens; before, the temp name was fixed (<index>.tmp) and the move was one bare os.replace, which Windows refuses while any process has the index open

Before: nine builds in the logs to 10 Nov died at line 235 with PermissionError WinError 5 after doing all their work (traceback_census_20261110_2150.txt); on this machine a bare os.replace over a file held open for reading is refused (control 1)

After: test_prefilter_publish.py on the live file: 17 controls, 0 failed (a reader holding the file 1.2 s is waited out in 1.56 s; a reader that outlasts the wait raises and leaves the old file and no temp; a writer that dies mid-file leaves the old file; three writers at once, 75 publishes, none fails; against another process loading the file in a loop, 17 publishes none fails while the reader made 8,488 loads); on the old file 3 of its 4 controls fail; a query on the live store returns the same three ids from the old and the new file

Not covered: no full build was run on the 35 MB live index (it takes minutes and the box is loaded), so the fix is shown on the publish step alone; a reader that holds the index longer than the wait still fails the build, with the old index left in place; a reader that opens the index in the instant of the move sees a PermissionError of its own (11 of 8,499 loads in the control), which load()'s callers must already tolerate and I did not check each caller

## 11. GitHub REST allowance shared by the three computers and the scheduled tasks

Change: none; a ten-minute sample of the allowance beside the commits landing and this laptop's own tally (gql_lane/quota_sampler.py)

Before: hour 01:42-02:42: this laptop's pusher alone made 1,566 REST calls

After: 03:53:19-04:03:26, 40 samples: 1,188 REST calls spent (7,128 an hour against 5,000), 4 of them from this laptop; 119 task commits (71 brain repo, 48 math repo), 14 other unsigned commits, 12 commits signed by GitHub (the GraphQL lane); spend per half minute 23 to 106 and unrelated to the task commits in the same half minute (least squares slope 0.5, R^2 0.01; the two half minutes with no task commit spent 41 and 38)

Not covered: the sample cannot tell the scheduled tasks' connector from the Mac minis: both are callers outside this laptop; whether the connector draws on the same 5,000 is inferred from the allowance falling while only task commits land, not read from GitHub; one ten-minute window

## 12. fleet inbox on this laptop (fleet_board.py: inbox_cache.json, the page cache, the per-agent seen list, the resurfaced list)

Change: the four cache writers move their temp file into place through one step, _swap: a refused move (another session has the file open) is tried again for 1.5 s (3 s for the per-agent lists), then the temp is removed and the caller goes on; the refresh returns the inbox it fetched whether or not the copy could be written; before, one bare os.replace raised out of the refresh, the fetched inbox was dropped for that prompt and the temp file stayed

Before: eleven inbox_cache.json.<pid> files left in `fleet_board` between 30 Oct and 8 Nov (5.6 KB to 515 KB each), one per refresh that died at the move; on the old file 8 of 13 controls fail (PermissionError out of _refresh and mark_seen under a reader, temp files left)

After: test_fleet_board_swap.py on the live file: 13 controls, 0 failed (a reader holding the copy 0.5 s is waited out; a reader holding it 3.5 s costs the prompt 1.56 s, the fetched inbox is still returned, the old copy is whole, no temp is left); the live hook runs clean on a prompt payload; the eleven stale temp files removed by name

Not covered: what the hook did with the exception each of the eleven times was not read from a log (I infer the inbox was not shown at that prompt and came at the next); the Macs run their own copies of fleet_board.py, where os.replace over an open file succeeds, so nothing changes there; a prompt can now wait up to 1.5 s for a reader where it used to fail at once

## 13. the primary directive line every session gets every three minutes (primary_hook.py: the record of when a session last got it, and the sub-clocks of the directive lines)

Change: each session keeps its fire record in its own small file under `primary_hook_state.json.d`/ instead of every session's entries in the one shared primary_hook_state.json; the save goes through a temp of its own and a move retried for 0.3 s, never raises and removes its temp; a fire still recorded in the shared file is honoured and moved, read-only, so the switch fired nothing twice; entries older than a day, day-old session files and crash temps are dropped at most once an hour; due() keeps its signature and return

Before: every prompt of every session read the whole shared file (71 KB), set its own key and wrote the whole file back through one bare os.replace; five temp files primary_hook_state.json.<pid>.tmp dated 16 Oct to 8 Nov sat beside it, each a save that was refused; on the old file 5 of 18 controls fail: a fire of another session that lands between this session's read and its write is lost, and eight sessions saving at once lose 47 of 48 fires (a lost fire means the line is sent again at the next prompt instead of after three minutes)

After: test_primary_hook_state.py on the live file: 25 controls, 0 failed (eight sessions at once lose 0 of 48; an interleaved fire is kept; a reader holding the file 2 s costs 0.47 s, nothing raised, no temp left; a damaged session file fires once and is repaired; an unwritable folder never raises); in the 40 minutes after the landing 29 other sessions' own hooks wrote their session files, the shared file was not written again (mtime 04:54) and no temp was left; the five stale temps removed by name

Not covered: how often the line was in fact sent early because of a lost record was not counted from transcripts; the 47 of 48 was not traced step by step (a read that fails while another process moves the file makes the old code start from an empty dict and write that back, which fits); the shared primary_hook_state.json stays as the source for sessions not yet moved and can be removed after 12 Nov 05:00; the same read-all write-all shape is still in other hooks' state (push_reminder_state, supersession_frontmatter_cache, spread_graph_cache, several other hooks)

## 14. the agent mesh command (agent_mesh.py main and write_tx): what happens when the mesh database is locked by another agent

Change: main() runs the command again, up to four attempts inside 27 s of wall clock, when SQLite answers locked or busy and this process wrote nothing that stayed (no transaction committed, none open, every row change inside a rolled-back transaction); write_tx counts commits and rolled-back changes for that rule; AGENT_MESH_BUSY_ATTEMPTS (1 = old behaviour), AGENT_MESH_BUSY_BUDGET_S and AGENT_MESH_BUSY_TIMEOUT_MS set it; exit codes unchanged (2 database error, 3 refusal)

Before: one attempt with a 15 s busy timeout, then 'agent mesh database error: database is locked' and exit 2, which every caller had to know to retry (six memories since September are about callers that did not); the event log of 8-11 Nov has 95 moments with no event for 8 s or more followed by three or more agents inside one second, 17 to 31 a day, 40 of them 15 s or longer (33 of those 40 at most 27 s, longest 64 s); on the old file the control with a 20 s write lock returns exit 2 after 19.7 s

After: test_mesh_busy_retry.py on the live file, on a temp database: 17 controls, 0 failed (a 20 s write lock is waited out and the claim lands once; a send retried after a lock lands exactly one message and one event; a reader that blocks the COMMIT gives one claim and one event after the rollback and retry; a lock that outlasts the attempts or the budget still ends in exit 2 with no row left; a 29 s lock returns exit 2 at 28.7 s, before a 30 s caller timeout; a held claim is still refused with exit 3 at once; --json output stays one document; the retry rule is false after a commit, after a write outside a transaction and inside an open transaction); the folder's own unit suite passes 48 of 48 on the live file; a live claim, assert, pulse, inbox and release each returned 0

Not covered: a failed command leaves no event, so how many commands a day ended in exit 2 before the change is not known and the effect on the live fleet is not yet measured; the cause of the stalls is not fixed (a 597 MB store in DELETE journal mode where one slow reader holds up a COMMIT and everything queues behind it; 795k events never pruned); callers that go through the Mesh class directly (the hooks) are unchanged; a caller with a subprocess timeout under about 28 s (fleet.py 10 and 15 s, conditioning_guard.py 20 s) can still be killed during a stall, as before

## 15. the ledger appender (ledger_append.py, GraphQL route): an HTTP 499 or 408 on the commit

Change: gql() sorts HTTP 408 and 499 as 'network' (ask again: read the tip, add only rows that are not there) instead of 'other' (give up the GraphQL route)

Before: at 06:30 on 11 Nov GitHub answered HTTP 499 with an empty body to the 2 MB createCommitOnBranch; the tool called that 'other', went to the REST route, found the REST allowance spent (403 five times) and appended nothing: an earlier ledger row waited

After: gql_lane/test_ledger_http_codes.py: 12 controls, 0 failed (499, 408 and 5xx are 'network', 403 and 429 'rate', 400, 401 and 422 'other', a timeout 'network'; a 499 after a commit that did land ends rc 0 with the row on the branch once and one mutation); the 16 older controls of test_ledger_append.py still pass; two earlier ledger rows then landed through GraphQL

Not covered: why GitHub answered 499 is not known (one sighting); the same sorting in the scratchpad pusher gql/push.sh and in fleet_board.py was not checked

## 16. the path pusher (`push_paths_gitdata.py`, both lanes): an HTTP 499 or 408 from GitHub

Change: _gql_kind sorts HTTP_408 and HTTP_499 as 'network' (read the tip again, land only what is not there) instead of 'other' (leave for the REST lane); the REST lane's call() asks again on 408 and 499 as it already did on a 5xx

Before: same fault as an earlier ledger row, one file over: a 499 on the commit request or on the tip read sent the whole push to the REST lane, about 30 REST calls against an allowance that is often spent; the old file fails the new 499 and 408 controls of gql_lane/test_gql_lane.py

After: gql_lane/test_gql_lane.py on the live file: all controls pass, the 8 new ones among them (two 499 then a landing stays on GraphQL with one commit; a 499 on a commit that did land is found at the next read, one commit; 408 likewise; a 499 every time goes to the REST lane after three more asks; 400 and 401 still go at once; 502 as before)

Not covered: fleet_board.py's own GitHub calls were not read for the same sorting; why GitHub answers 499 is still not known (seen five times on 11 Nov between 06:30 and 06:42, all on the 2 MB ledger commit)

## 17. math hook (math_sense._revision_edge_reader): a store holding an edge kind the reader's build does not know

Change: the reader finds the first non-retracted edge of an unknown kind through the kind index and raises the store's own UnknownEdgeKindError there, instead of declining so that the caller reads every edge to reach the same refusal; when every such edge is retracted the fast path goes on

Before: the whole-edge read behind the decline costs 17.5 s on 167,685 edges (measured 11 Nov 03:20), inside a read transaction, and would be paid on every math prompt from the day a new kind is written until the build is upgraded (it happened on 9 Aug with semantic_association); in the controls the old file needs one whole-edge read for every refusal

After: closure_reader/test_unknown_kind.py: every control passes on the live file; the refusals equal the old file's word for word with no whole-edge read; run old against old the test fails; test_closure_reader.py and math_answer_closure_selftest.py --quick still pass

Not covered: no timing on a store that holds an unknown kind (the live store has none); a non-ASCII pool id and a failed query still take the whole-edge read; a NULL kind is not looked for; the hook is still silent while the kind is unknown

## 18. push_paths.sh (the laptop's pusher)

Change: After the secret scan, when the fetched history of main holds 5 or more commits in the last 600 s and the API lane may be used, the scanned commit goes to the API lane without a git push; if that lane does not land it the script runs itself again in the old order (PUSH_PATHS_API_FIRST=0).

Before: One real one-file push at 07:16 with one git attempt: 111 s, of which 32 s a git push rejected on a moved tip and 4 s sleep; with the default budget a second fetch and a second rejected push before the API lane.

After: First real push after landing (08:06, five paths, 50 commits on main in 600 s): 57 s, no git push attempted, landed by GraphQL on try 2. About 20 s of the difference is the faster fetch after the pack index was rebuilt the same hour, not this change.

Not covered: the Macs' own copies of push_paths.sh; callers that wrap the script in timeout; the fetch itself

## 19. agent mesh (agent_mesh.py, the laptop's mesh database)

Change: Took the whole-table reads out of the mesh's ordinary commands. Two indexes, made at open when missing and built once by hand on the live file: idx_messages_sender ON messages(sender_agent) and idx_agents_live ON agents(lease_until) WHERE status NOT IN ('done','offline'). The claims-expiry UPDATE in prune, claim and assert and prune's orphaned-tasks UPDATE look the owner up by primary key (EXISTS) instead of listing every dead agent (IN subquery). send --to all sorts its targets in Python so the query can use the live-agents index. board() reads the pending mail once (GROUP BY recipient, totals summed in Python) instead of three times.

Before: Statement census on an empty database: 66 distinct data statements, 19 with a scan in the plan. receipts read every message to find one sender (181 MB of message text): 47.4 s on a cold cache at 08:50, 0.74 s warm. board(), which digest, status and doctor all call, read the pending mail three times (99,294 of 208,237 messages are pending; one pass took 5.6 s cold at 08:40). claim and assert listed all 11,213 agents inside their write transaction. In DELETE journal mode a commit waits for every reader, so a slow whole-table read held the fleet's writers for their whole busy limit.

After: Census: 65 statements, 13 with a scan, none of them a read of all agents or of the messages table outside purge, one pass over the pending mail (through the covering index). On the live file the plans are SEARCH... USING INDEX idx_messages_sender for receipts, a MULTI-INDEX OR for the desk's per-agent mail query with no change to the desk, SEARCH... idx_agents_live for prune and board. receipts 0.41 s and 0.39 s after (warm cache; a cold run after the change was not measured). The index build held the write lock 4.8 s once; the file grew from 598.3 MB to 603.2 MB. agent_mesh.py sha256 (was ).

Not covered: Whether the locked stretches fell is not counted yet (rerun mesh_stalls/lock_fsync_watch.py). Every digest and status still reads all 99,294 pending rows once; most are addressed to agents that are gone, which is a purge question for the fleet, with the history on GitHub first. WAL against DELETE is untested. The Macs' databases get the indexes at the first open with the new code, best effort.

## 20. agent mesh database (laptop)

Change: No change. The 20-minute lock watch was run again after the 08:53 landing of the two indexes and the one board pass, to count whether the locked stretches fell.

Before: 05:59Z-06:19Z, before the landing: 1186 lock probes, 5 locked stretches of 3 or more samples holding 81 samples (33, 7, 12, 3, 26), journal up to 18.0 s old, 8 stretches of 1-2 samples. Syncs: median 6 ms, p99 174 ms, max 2.6 s, 4 over 1 s.

After: 06:58Z-07:18Z, after the landing: 1185 lock probes, 3 locked stretches of 3 or more samples holding 32 samples (18, 5, 9), journal up to 17.6 s old, 8 stretches of 1-2 samples. Syncs: median 6 ms, p99 149 ms, max 4.7 s, 5 over 1 s. So the time spent in long locked stretches fell by 60 percent, and the longest stretch is as long as before: some writer still holds the database for 9 to 18 s at a time, and the slowest sync inside those stretches was 0.1 s, so it is not the disk.

Not covered: Who holds the database during the 9-18 s stretches is not known. The next step is a line in the mesh's own log whenever a write transaction lasts more than 2 s (command, pid, seconds), so the holder names itself; WAL against DELETE on a copy under load is still untested.

## 21. Codex hooks (both Codex homes): 46 hook commands, no dispatcher

Change: Wrote codex_hook_dispatch.py (one process per event; imports hook_dispatch.py as a module, which is not edited), make_codex_hook_list.py (hooks.json to a list file, a second prompt list and a proposed hooks.json) and test_codex_dispatch.py. Nothing is installed: a changed hook line needs the owner's /hooks review in each Codex home.

Before: Each Codex home runs 46 hook commands as 46 processes: 27 on a prompt, 9 before a tool call, 4 after, 6 at a stop. The rig logs show Codex starts the hooks of one event together. In one rig log 40 of 157 hook lines end Failed; which hooks is not named.

After: Proposed: 1 line before a tool call, 1 after, 1 at a stop, 4 on a prompt (two dispatcher lines, the owner-prompts line and the slowness advisory unchanged). Test: blocking and fallback 25 of 25; 25 hooks give the same output in process as in their own process twice; whole event passes on all four events with every deterministic context inside and no cut (prompt: 1,912 + 6,271 chars). Wall seconds against Codex's all-at-once start, three pairs of runs on a busy box: before a tool call 0.81-1.39 today, 0.72-1.32 wrapper; after 0.29-0.49, 0.19-0.23; stop 0.53-0.95, 0.32-1.93; prompt 3.34-4.23, 2.14-3.36. The wall gain is inside the noise; what falls is the number of processes started.

Not covered: CPU seconds and memory of the two ways (the number that decides whether this is worth the owner's review); which hooks Codex marks Failed; restart_handoff_hook.py prints plain text on Codex, which Codex discards; the in-process proof decays when a hook file is edited and has no scheduled re-proof; prompt_archive.py, task_checklist_hook.py and live_inbox_hook.py were never run by the test

## 22. Codex hooks: CPU and memory of 46 separate hook processes against the one-process dispatcher

Change: cpu_tree.py puts each way in its own Windows job object and reads the user + kernel time of the whole process tree. The dispatcher prototype now puts the user site at the end of sys.path (it starts with python -s; today's Codex hook lines do not).

Before: Hook CPU per event today, median of 5: before a tool call 2.44 s, after 0.64 s, stop 1.25 s, first prompt 10.88 s; peak committed memory before a tool call 105 MB; 18 processes (9 pythons, each with a console host). In the first prototype a hook that imports a user-site package failed open: a made-up guard needing psutil did not deny.

After: With the dispatcher: 0.66 s, 0.14 s, 0.28 s, 5.91 s; 33 MB; 2 processes. One tool call 3.1 s to 0.8 s of hook CPU (74 percent less); ranges of the two ways do not overlap. The same guard denies inside the new prototype and not inside the old one (usersite_control.py, 4 of 4). Blocking tests again 25 of 25.

Not covered: At the 10 Nov volume the saving is about 0.4 CPU hours a day, because 28 of 41 rig briefs run with hooks off; the gain that matters (workers running with hooks on again) is not measured yet. Codex's own matcher rule against hook_dispatch's on a tool name only one of them matches. The steady-state prompt (not a session's first) was not measured.

## 23. codex hooks / guards

Change: Measured which Codex tool calls run the brain's hooks. Two five-minute probes (codex_probe/STDIN1 and STDIN2, 10:15-11:03) each made a file with the patch tool, ran three one-off commands and typed four lines into an open PowerShell session. Hooks ran before and after every exec_command call (8 hook starts) and every apply_patch call (7), and on none of the typed lines.

Before: Assumed every shell command of a Codex worker passes the PreToolUse guards (help guard, orders hook, voice guard, disk hook, reflexes).

After: Text typed into an open shell (the write_stdin tool) passes no hook. STDIN1: 12 hooked calls = 10 exec_command + 2 apply_patch; 4 typed lines and 13 polls with no hook block. features.unified_exec=false does not remove the open-shell tool (STDIN2: 4 typed lines, 20 polls, 7 hooked calls = 5 + 2). In one Codex home, 8-11 Nov, 100 of 617 commands were typed: 90 in one worker (rig brief GHA, hooks on, 90 of its 98 commands), 8 in the two probes, 2 elsewhere. Not fixed.

Not covered: Why the GHA worker moved into an open console (its own notes speak of a small Python console; no hook line asks for one). Whether a newer Codex hooks write_stdin. An after-the-run check of typed lines against the guards is the next step and is not built.

## 24. codex hooks / measurement

Change: Two figures of this loop corrected. (1) an earlier ledger row, NEXT and the dispatcher memory said 10 Nov had 458 hooked Codex tool calls; that was every tool call, and hooks run on exec_command and apply_patch calls only. (2) My first reading of the open-shell share (52 pct of that home's calls, 132 of 140 in GHA) counted polls as commands; counting only calls that typed text gives 16 pct (100 of 617) and 90 of 98 in GHA. Also read off the probe logs: 8 of the 9 PreToolUse lines and 26 of the 27 UserPromptSubmit lines start in Codex, which matches the two hook lines the liveness check has reported as untrusted (44 of 46) since 10 Nov.

Before: 458 hooked calls a day; 52 pct of calls typed into an open shell

After: hooked calls are the exec_command and apply_patch calls (641 of the 1,223 exec_command, apply_patch and write_stdin calls in that home over 8-11 Nov; waits and other tools come on top); typed share of commands 16 pct, nearly all from one worker; the dispatcher's daily saving is below the 0.4 CPU hours given in an earlier ledger row

Not covered: Which two hook lines are untrusted was not read from Codex itself; the count match is the evidence. the owner's /hooks review settles it.

## 25. codex hooks / brain against no brain

Change: Read the one same-brief pair the rig already holds: GHA (hooks on) and GHB (hooks off), 10 Nov, same PROMPT.md, both at the ceiling of the task.

Before: The cost of hooks to a Codex worker was known only from 8 Nov under memory pressure (2 commands in 50 minutes).

After: Hooks on: 35.5 min, 12.51M input tokens (12.40M cached), 23.2k output tokens, 98 commands. Hooks off: 24.0 min, 5.08M input (5.02M cached), 23.2k output, 92 commands. So 11.5 min and 2.5 times the input tokens more with hooks, same score. Median time from a command to its output 3.66 s against 3.02 s.

Not covered: One pair, not a distribution. The hooks-on worker also worked another way (an open console, so only 8 of its commands were hooked), so the 11.5 minutes are not a clean price of hooks; the extra input tokens are mostly the hook text carried in every later turn.

## 26. codex hooks / guards

Change: Built codex_probe/codex_typed_audit.py: it reads a finished Codex rollout, never runs anything, and hands every line the worker typed into an open shell (write_stdin with real text) to the deny-only guard codex_help_guard_hook.py as a PreToolUse payload, the way Codex does for a command started as its own process. It prints how many write_stdin calls it read, how many were polls, how many typed something, how many typed a text built at run time that it could not read, and each line the guard would have refused. Exit 0 nothing refused, 4 refused, 1 usage.

Before: A line typed into an open shell passed no hook and nothing looked at it afterwards (an earlier ledger row of 11 Nov).

After: Five controls pass (typed_audit_controls.py, 11 Nov 20:10): P1 a typed --help on an unapproved local script is refused (exit 4, one refusal, the harmless line beside it passes); N1 the same command run as its own process is not counted as a typed refusal; N2 the real STDIN1 probe rollout reads four typed lines and refuses none; P2 a typed text built at run time is reported as not read; B1 with a guard that never refuses, P1's rollout passes, so the refusal comes from the guard and not from the audit's own matching. Real runs: rig brief GHA 132 write_stdin calls = 42 polls + 90 typed, 0 refused; GHB 10 polls, none typed, 0 refused; STDIN2 24 = 20 polls + 4 typed, 0 refused.

Not covered: Only the stateless guard is replayed (no-subagents policy, picture policy, local --help guard). The hooks that keep state for each session (orders, reflexes, disk, voice) are not run. It reads a run after it ended, so it reports and does not prevent. Not wired as a Stop hook: that is a new hook line and needs the owner's /hooks review. The three real runs were clean, so no real refusal has been seen yet; the positive case is the made-up rollout only.

## 27. codex hook dispatch

Change: In the proposed Codex hooks file (codex_dispatch/hooks.proposed.json, for the owner's /hooks review) the two hook lines that stay their own process, the slowness advisory and owner_prompts_hook --runtime codex, now start with python -s like the dispatcher lines. make_codex_hook_list.py adds the flag to kept lines; the two list files it writes are byte for byte what they were. Suggested by an agent (the user-site start costs 73-80 ms a python start on this machine).

Before: python.exe -B on those two lines: the user-site folder and its start files are read at every start.

After: python.exe -s -B. Checked first that neither hook imports anything from the user-site folder (new codex_dispatch/usersite_imports.py: reads the import statements of the script and of every module it imports from its own folder, locates each name; slow_sense.py 4 names all standard library, owner_prompts_hook.py 10 files and 33 names, 23 standard library and 10 own folder, 0 user-site). Controls: a made-up script importing psutil inside a function is reported NOT CLEAN (exit 3), one importing json and os is CLEAN. slow_sense with fresh session ids prints the same 3,127 chars with and without -s (cmp equal) in 210 and 163 ms against 445 and 286 ms.

Not covered: owner_prompts_hook was not run both ways (it keeps a delivery queue per session); its case rests on the import reading. A name imported through importlib at run time would not be seen: the check prints such lines and there were none. Four timings on a loaded box are a direction, not a size. My first reading (the hook printed nothing under -s) was the hook's own once-per-half-hour rule for one session id, shown by the rerun with fresh ids. modulefinder could not be used: it stops with an AttributeError on Python 3.14.

## 28. slowness probe / hung-producer detector

Change: slow_probe.hung_producers no longer names a process that never started. New helper _never_started(pr): no CPU time at all and no handles. Such a process is skipped before the byte test, counted in the state file on its own lines (never_started_producers, never_started_note) and not as a hung producer.

Before: pid 27804 (publish_board.py, created 11 Nov 15:32:32) was named a hung producer from about 16:00 on 11 Nov past midnight: every session got the advisory, the prompt hook repeated it, and a peer broadcast it to the fleet. Measured 12 Nov 00:14: one thread in state Wait/Suspended, 0 ms CPU, no modules, no handles, parent gone. Windows creates a process with its first thread suspended and the creator resumes it; the launcher died in between. Its byte counters are zero and never move, which is exactly the detector's test. A second one sat beside it, created in the same second: pid 57720 (claude_pool/usage_week_alert.py), watched 22 cycles.

After: Test test_never_started.py, all pass: a live sleeping child is not called never-started (0.09 s CPU, 88 handles); a child created suspended on purpose and never resumed is (0 CPU, 0 handles, 1 thread); the test's own process is not; with the state the probe itself saved, the live probe returns hung 1 naming pid 27804 and the patched copy returns hung 0 with both pids on the never-started line; the copy drops from its watch exactly those two; the other 14 watched processes and the waiting count are the same in both.

Not covered: The two leftover processes are still in the table (about 1 MB each, nothing held); they are not mine and were left alone. Why two launchers died in the same second on 11 Nov 15:32 is not established (the network outage of that afternoon is the only event known near it). slow_sense prints nothing about never-started processes; the count is only in slow_state.json. My first fix assumed the process had exited and was pinned by a handle; its own test refuted it (GetExitCodeProcess said still active, and an exited child whose handle is held does not appear in the snapshot), and it was thrown away.

## 29. Codex hooks / trust

Change: trust_census.py: per Codex home, how many hooks.json lines that home's own config.toml trusts. Reads only, writes no hash.

Before: The notes said both Codex homes carry the 46 lines and two lines are untrusted.

After: Five homes carry the same 46-line file (same sha256) and in each of the five the same two lines have no trust record: the disk hook before a command and on a prompt. Codex skips an untrusted hook silently, so the disk hook has not run in Codex. Two more homes hold one mesh hook line each with no trust record. Sessions written on 10 and 11 Nov: 232, 188, 102, 0 and 0 in the five homes. The recorded trusted_hash (sha256:..., 71 chars) is not the plain sha256 of the command or of the handler's JSON, so a record that no longer matches its line cannot be told from a good one here; the nightly liveness check counts presence only. Also seen in the installer's own test: on Windows sys.stdin.isatty() is True for the NUL device, so a console check needs GetConsoleMode.

Not covered: How Codex computes trusted_hash was not found; the liveness check therefore still cannot see a stale record. Which home each running worker uses was read from the session folders, not from the processes.

## 30. agent mesh / locked database

Change: agent_mesh.py: Mesh(..., patient_s=0.0). With patient_s set, a locked database is tried again every quarter second until patient_s has passed, at the open, at BEGIN IMMEDIATE and at COMMIT (SQLite keeps the transaction when COMMIT is refused as busy). Default 0, so every caller that does not ask behaves as before. A slow-transaction log, mesh_slow.log next to the database: one line when a write transaction's wait for BEGIN, its work and its wait for COMMIT add up to 2 s (AGENT_MESH_SLOW_S), one for a slow open, one for a slow CLI command; tag is the CLI command or the script name, no statement text or agent names. ingest_repository_reports.py (the board's report ingester) now opens the mesh with patient_s=30.

Before: PUBLISH.log, 5-11 Nov: 25 board cycles refused with 'database is locked' out of the ingester, which imports the mesh and had no retry (only the command line retried). Where: BEGIN IMMEDIATE 19, COMMIT 3, the open's PRAGMA journal_mode 2, the schema repair 1. Each cost the board mirror 15 minutes. Nothing recorded who held the file or for how long.

After: On throwaway databases with a second process holding the lock (test_patient.py, 23 of 23): the old file and the new file without patience are refused at the open under an exclusive lock, at BEGIN behind a writer, and at COMMIT behind a reader (three controls each way); with patient_s=20 all three succeed about 5 s later, the write lands exactly once, and the log line names the wait (open_wait 5.00, begin_wait 5.04, commit_wait 4.99). patient_s=3 behind a 12 s writer is refused after 3.3 s with nothing written. A non-lock error and the caller's own exception are raised at once. Fast transactions write no line. The command line still retries by itself. The mesh folder's own suites give the same result on the old and new file (94 tests).

Not covered: The cause of the long locks is not fixed: the log is there to name it, and its first lines have to be read. Callers that hold their own SQLite connection to the mesh (hooks reading it directly) write no line. Long-lived processes keep the old code until they restart. team_comm.py (3 s) and bridge/mesh_bridge.py still have no patience; whether they should is not measured. The ingester's gain is proven on the mesh, not yet on a live board cycle that met a lock.

## 31. project memory / hourly review reader

Change: runtime/hourly_runner.py`: the reader commands (read-offer, read-latest, ack) reconfigure stdout and stderr to UTF-8 before they write. The fix is in the package, so both wrappers get it.

Before: The command the hot hook prints for every session, project_memory_cli.py read-offer <token> --shard 0 (live-brain review), exited 1 with UnicodeEncodeError on U+25CF: a piped Python stdout on Windows encodes with cp1252. The failure came before the shard was marked served, so the review could not be read through or acknowledged; 12 of 1,385 sessions in the signed cache hold any acknowledgement, and this session received 288 'review is due' lines (about 60,000 chars) in 27 hours. The 20 Aug fix for this sat only in the nested wrapper; the 11 Nov move of the hook line to the top-level wrapper lost it.

After: Same command on the live file with no encoding variables set: read-latest rc 0, read-offer --shard 0 rc 0, output valid UTF-8 with the characters that used to kill it. The status command still answers through the new file.

Not covered: The size of a review (56 shards of about 48,000 chars for live-brain) and the number of projects offered to one session (eight here) are untouched; the reminder lines will keep coming until that is decided. PowerShell 5.1 decodes a native command's output with the console code page, so the unusual characters may show as mojibake there (no crash). The runtime folder is not a git repository: the patch and its proof are pushed, the file itself is not.

## 32. project memory / hot hook review lines

Change: runtime/project_memory_hot_hook.py: the reviews that are due in one call share one line that names every project with its occurrence count and gives the command once. One review alone keeps the old sentence word for word. Stamps, acknowledgements, the failed-attempt line and the line budget are untouched.

Before: One line per project, each with the same 150-character command. Fixture with eight due reviews: 8 lines, 2,552 chars. This session received 288 such lines, about 60,000 chars, in 27 hours.

After: Same fixture: 1 line, 482 chars. test_combined.py 14 of 14 with every case run on the old and the new file; the hook's own suite 50 passed on both. On the live file the hook answers a real call with rc 0.

Not covered: Not yet seen at a receiver: the first combined line arrives when the next review window opens. project_memory/hook.py _render_hot still writes one line per project. The size of a review is untouched.

## 33. agent mesh / slow-transaction log

Change: agent_mesh.py: when an open, a BEGIN IMMEDIATE or a COMMIT has waited AGENT_MESH_HOLDERS_S seconds (5; 0 turns it off), a timer thread asks Windows which processes have the database file open (Restart Manager) and writes one 'holders' line to mesh_slow.log: pid, script base name and age of each, youngest first. No timer is armed when the call cannot wait that long (busy timeout plus patience under the threshold), so hooks with short waits pay nothing. No folders and no arguments are written.

Before: The slow log showed the victims of a long lock (12 Nov 01:24: a COMMIT waited 17.11 s, two opens 11 and 16 s) but not the reader, because the reader was not this file's CLI.

After: test_holders.py 20 of 20 on throwaway databases: a commit behind two readers names both by pid and script; BEGIN, the open and the CLI path likewise; the old file and the feature switched off leave no line; a 3 s wait under the default leaves none, an 8 s wait is named at 5 s; no timer thread is left behind; an uncontended write measured 4.50 ms before and 4.81 ms after (median of 300). test_patient.py and the folder's five suites give the same results as before.

Not covered: No live catch yet: the 01:24 reader is still unnamed until the next long wait. A holder is any process with the file open, so waiting victims are listed with the reader. Processes of another Windows user would show without a script name. workspace.py report still reads the whole messages table.

## 34. global workspace / report reads the mesh

Change: global_workspace/workspace.py _mesh_traffic: the messages of the report window are read newest first, 2,000 rows a query by rowid, and the read stops after 1,000 rows older than the window minus an hour of slack. It was one 'WHERE created_at >= ?' query, which no index serves (EXPLAIN QUERY PLAN: SCAN messages).

Before: One report read the whole messages table (416 MB on 12 Nov) inside one read transaction; in the mesh's rollback journal every commit waits behind such a reader. A diagnostic scan of that table took 35 s on 11 Nov.

After: test_ws.py 9 of 9, old file against new on throwaway databases: the same answer at seven window positions with stamps up to 30 s out of table order, and with stamps up to 30 minutes out of order; a table without a rowid falls back to the old query; on an 83 MB table with the window on the newest 2 per cent, one statement over all 40,000 rows became three short ones over 6,000 rows (84 ms against 26 ms with the file in the cache). The folder's own suite: 50 tests OK before and after.

Not covered: Nothing scheduled runs the report, so this was a trap and is not shown to be the 01:24 reader. Not measured on the live mesh file (no scan of it is allowed). Stamps more than an hour out of table order, or a run of 1,000 old-stamped rows above newer ones, would be undercounted. agent_mesh.py inbox --include-acked, which the live inbox hook's footer advertises, was not examined.

## 35. agent desk / reads the mesh

Change: `agent_desk_service.py` mesh_snapshot: the selected agent's mail comes from index walks (newest 25 row ids sent, received unacked, received acked, each from a covering index) and only those rows are then read. It was one query, sender=? or recipient=? or recipient='all' order by created_at desc limit 25.

Before: The mesh slow log's first holders lines (12 Nov 01:54:03-01:54:10) named agent_desk_service.py as the only process, other than waiting mesh commands, with the database open during a 16.2 s commit wait. The old query loads with bodies every message the agent sent and every received message newer than the 25th newest seen so far; for an agent that never sends, all of its mail.

After: test_desk.py 13 of 13 old file against new on throwaway databases with the mesh's own table and indexes: the same 25 messages in the same order for a busy agent, two ordinary agents, an unknown agent, with and without recipient 'all' rows; bytes read from the file by the process read counter: busy agent 6.5 MB against 1.2 MB (half acked) and 7.2 against 0.24 (none acked); an agent that only receives 20.7 against 0.70 and 37.1 against 0.15 MB. Control: old against old fails the byte and step checks (7 of 13).

Not covered: The old query was not timed on the live mesh file, so the 16 s is tied to the desk process by the holders lines, not to this query by a measurement; the service's other three mesh queries are small table reads. Ties in created_at at the 25th place can order differently. The desk folder is outside the brain repository: only the patch and tests are pushed.

## 36. project memory / hourly review reader

Change: `hourly_runner.py` read-latest: a review of three shards or more now answers with its newest twelve owner prompts for the project, newest first, each cut to 600 characters, inside 8,000 characters, and one closing line with the packet's size and the command that lists the shards. --full, read-offer, the shards, the receipts and the acknowledgement rule are unchanged; a review under three shards answers as before; a shard that fails its hash gives the old answer.

Before: The command the hourly notice tells every session to run printed one command line per shard: 126 lines, 24,654 characters for brain-framework (123 shards, 5.9 MB); the largest review is 559 shards, 26.8 MB. The store holds 31 acknowledgements since 22 July, 1 since 1 October, and 15 shard reads since 1 November (review_counts.txt).

After: test_digest.py 16 of 16 old file against new on throwaway packets cut by the publisher's own code; control old against old fails 7 of 16. On the live store for this session: brain-framework answers in 14 lines, 3,905 characters; --full is byte for byte the old answer.

Not covered: The notice still comes every hour for every project a session ever touched, and a window is republished whenever the project gets a new prompt, so an acknowledgement silences it for an hour at most. Reading the digest leaves no receipt and does not quiet the notice. Whether the hourly review should exist beside the owner-prompts hook, which already sends each session the owner's recent prompts by thread, is the owner's to decide. Prompts are filed to projects loosely: unrelated prompts appear under brain-framework.

## 37. hook liveness / wake check

Change: `hook_liveness.py`: (1) the Stop-order check accepts loop_keeper.py and loop_rewake.py as standalone Stop entries (wired 11 Nov on the owner's 03:13 and 07:07 orders; loop_rewake.py is an asyncRewake watcher and can only be a settings-level entry); an unknown standalone entry still fails. (2) A hook wired only on the events whose own-process hooks the dispatcher starts first and collects last (UserPromptSubmit, Stop, SessionStart) is named as running beside the in-process hooks instead of as waiting for the fast list; a hook wired on any other event is named as before.

Before: Every liveness run and every wake since 11 Nov read 'Stop order unsafe: work_timer.py is not final' and a verdict of 2 safety failures, one of them false. The same report told agents to test and add fleet_inbox_hook.py and waste_sense.py to the in-process list. Measured on 5,597 profiled prompts since 10 Nov 22:15: in-process hooks median 2,135 ms, slowest child median 644 ms, the child longer than the in-process sum on 467; waste_sense.py as a child ran over 5 s 51 times. In-process it would add its own time and tail to the wait.

After: judge_liveness.py 6 of 6 on four full runs of main() (new and old file, live settings and a settings copy with an unknown Stop entry plus two patched unlisted hooks); the old file passes 0 of the 4 checks the change is meant to move and both guard checks. Live: the Stop order reads ok, the verdict counts 1 failure (Codex hook trust 44 of 46, which waits on the owner).

Not covered: hook_dispatch_extend.py --only waste_sense.py would still add it to the in-process list (it passes the exact test); nothing refuses a prompt-only hook there. The wake text a session already received keeps the old warning until its next startup. fleet_inbox_hook.py is not deterministic between two runs, so it could not join the list in any case.

## 38. math hook / repeat memo

Change: `math_sense.py`: the repeat memo (MATHBRAIN_REPEAT_SKIP, 5 Nov) also keeps generic_only_match and no_chosen_after_select, the two silences reached before the shown-ids guard. They are kept for the same two hours, are not scoped to the context, and answer only while the session's shown-ids shard has the size and write time it had at the record (the use layer ranks with that set, and the shard is written only on a serve). The two older reasons are unchanged. Dial MATHBRAIN_REPEAT_STORE_ONLY=0 restores the 5 Nov memo.

Before: Three days to 12 Nov 02:4x, real sessions (mathbrain_silence.tsv): 717 full runs ended in one of the two verdicts, 688 of them on a prompt identical to one the same session had sent in the two hours before (93 inside one context, 595 across a compaction). In the profile of 11 Nov 16:39-22:03 a run ending in generic_only_match took a median 1,362 ms (35 runs, max 3,152) in-process on the path a prompt waits for; a run answered by the memo takes a median 20 ms (227 runs).

After: judge_ms.py 20 of 20 on three runs of test_ms.py (new, old, new with the dial at 0): the old file gives the wanted answer on 0 of the 6 cases the change is meant to move and the same answer on all 13 guard cases; with the dial at 0 the new file answers all 19 cases as the old one. Replay of the same three days under the landed rule (ms_gain2.py): 683 of the 717 full runs are answered from the memo, in 4 sessions; 5 are rerun because the session was served a block in between.

Not covered: A run ending in no_chosen_after_select was not timed (none fell in the profiled window). The store and the fleet-wide use layer can change inside the two hours, as for the 5 Nov memo. 221 of the 234 math blocks served in three days were the same first card going to the same session again after a compaction, 3 to 5 s each: by design since 5 Nov, left to the math lane. The two 40 s runs of 11 Nov 18:39-18:42 were the whole box stalling (fok_probe 17.8 s in the same dispatch), not this hook.

## 39. agent mesh / release and bye

Change: agent_mesh.py Mesh._pending_handoffs: both sub-selects name the partial index (INDEXED BY idx_messages_open_handoffs). A file without that index gets the unhinted statement; any other error is raised as before.

Before: The check runs inside the BEGIN IMMEDIATE of release() and bye(). Since idx_messages_sender was added on 11 Nov (by this loop) the planner, with no statistics on the file, answered the outgoing side from it and the incoming side from idx_messages_recipient: every row the agent ever sent and every unacked row it ever received, loaded with the write lock held. Live counts: 34,202 sent rows for brain-high, 464 for a busy session, 5,793 unacked for agent-desk; 10 open handoffs in all. The partial index made for this check on 8 Oct was no longer used.

After: test_handoff.py 13 of 13 on a throwaway database with the live table and indexes (40,000 messages, 60 open handoffs): same rows in the same order for six agents and four direction pairs; a broadcaster's check reads 0.17 MB against 46.9 MB, an agent with unacked mail 0.13 against 31.5; the old file against itself fails the bytes line; without the partial index the unhinted statement runs; a locked database raises as before with one statement sent. The folder's five suites: same result on the old and the new file.

Not covered: The old statement was never timed on the live file (for a broadcaster it would read tens of thousands of rows). The 26 s bye of the memory mirror at 03:07 is mostly the release of about 150 claims in one transaction, not this check. The commit waits of the 03:01-03:08 burst are behind readers the log does not name; the desk memory stays provisional.

## 40. agent desk / mesh read

Change: agent_desk_service.py: new _mesh_agents(). The mesh's agents table is read whole at most once in 300 s. Between those reads each call reads the rows in the mesh's partial index idx_agents_live (status not done/offline) with a lease in the last six hours, and looks up by primary key the rows that were in that set at the last call and are not now. A refused read serves the rows of the last read and logs it. A mesh file without the index is read as before.

Before: mesh_snapshot() read all rows of the agents table (11,366 on 12 Nov, ten columns, the task text of each) on every collector tick: every 3 s with a viewer, every 30 s without. The timing line added at 03:24 logged three reads of 2 s or more in 29.5 minutes (4.5 s, 5.4 s, 3.1 s), and a mesh writer ready to commit waits for a reader. A refused read showed no mesh agents at all.

After: test_desk_agents.py 13 of 13 on a throwaway database with the live schema (3,250 agents): the same agents, order, claims and tasks as the old read at the first call, after no change, after a pulse, two byes, a return, a stale pulse, a new agent and a deleted row, after the index is dropped, and after a lock; SQLite steps on a tick 30 against 1,954; the old file against itself fails the steps line. Stated limit, tested: a row edited while it stays done or offline is seen at the next whole read (up to 5 minutes). On the live file the statement runs as SEARCH agents USING INDEX idx_agents_live and returns 29 rows. The 03:24 mail test, backup against live: its seven sameness lines pass, its six cost lines fail as they must (both files carry that fix).

