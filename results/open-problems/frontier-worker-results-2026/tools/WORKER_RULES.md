# Frontier rules for a solver on a top-200 row

These replace "improve what you can certify". F below is
`python -X utf8 ~/brain-repo/06_math_research/frontier/frontier.py`.

1. Start from the frontier, not from our history. Your first action is `F brief TNNN` and reading it in full: the
   statement, the frontier papers, how their proof goes, the exact place it fails, the obstruction, what is settled and
   the targets. Then read the frontier paper's own pages at the failure point. Earlier attempts by our workers appear
   only as settled facts and dead routes; do not go looking for more of them.
2. Before you start any route or lemma, run `F check TNNN "<the route in one sentence>" --open --by <you>`.
   Exit 2: a settled fact or a dead route matches. Do not redo it; read the evidence. You may go on only with a
   concrete reason it differs, written into your ROUTES.jsonl line. Exit 1: someone holds or claimed something close;
   build on it. Exit 0: go ahead. On exit 0 or 1, --open writes the route on the row as live at that moment, so the
   route chooser (rule 8) learns how long routes live and which stall; close it later with
   `F route TNNN dead|done "<the same sentence>" --why "..."`.
3. Keep `ROUTES.jsonl` in your own folder, one line per route:
   {"row": "TNNN", "route": "<one sentence>", "status": "live" | "dead" | "done", "why": "<for dead: the precise
   reason, with the witness or the failing step>", "evidence": "<claim id or file>", "at": "<ISO time>"}.
   Open a route as live when you start it; close it as dead or done when you stop. A dead route without a why is
   useless to the next worker.
4. Every CLAIMS.jsonl entry carries two more fields: "kind" - one of moved, narrowed, special, bound, literature,
   route-failure - and "target" - the TARGETS number in the dossier it serves, or "none".
   moved: a step of the frontier architecture now goes through where it failed. narrowed: the statement itself is
   proved on a whole new part of its range (a parameter interval, an infinite family). Everything else is recorded but
   does not count as progress on the row.
5. Work the TARGETS in their order. A sharper constant, a further isolated case or a better certified bound that is
   not a named target is not the job, however cleanly it certifies. If you think a target is wrong or a better one
   exists, write why in STATUS.md; the lead decides.
6. Your STATUS.md NEXT line names the target number you are on.
7. A literature finding that answers the row or a target outranks everything: stop, write it as a claim of kind
   literature with the locator, and say so in STATUS.md.
8. When choosing among the row's live routes, run `python -X utf8 route_bandit.py order TNNN`: it orders them by
   Thompson sampling over what every agent has recorded, and marks DROP on a route the record is confident rarely
   pays. After each attempt on a route, record its outcome on the row, failures included:
   `python -X utf8 route_bandit.py record TNNN --route "<the route as written>" --outcome useful|tried --by <you>`.
   useful: the attempt produced a step you would log as moved, narrowed or a checked partial result. tried: it did
   not. Without the failed attempts the ordering cannot learn which routes stall.
