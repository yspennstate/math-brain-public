
NOTE from the launcher (an agent, Fri Nov 13 10:29:56 +04 2026): the full STRAT11 folder (all verify_*.py, certificates, STRAT9/, STRAT10/) is now in STRAT11/; replay_all.py can run from there.

08:40 note (an agent): STRAT11/ now holds all nine verify_*.py (rsynced after your first listing). Rerun STRAT11/replay_all.py before the final report.

09:05 note (an agent): the 9 depth-16 leaves (nodes 12091 12407 14175 15603 15773 19750 20736 21058 21550) persist one per box: splitting will not close them. Suggest: for each, find the exact point where min over the feasible closure of T is attained; if it is a boundary point where T=0 (det->0, t->0, or the disconnected limit), close it with a local lower bound T >= c*dist (as STRAT11 did for the corner) or with your exact obstruction replay, and report which leaves are of which kind.
