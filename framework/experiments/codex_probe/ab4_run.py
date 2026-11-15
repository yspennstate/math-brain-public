"""AB4: Codex brain / no-brain test on our own prior work about open problems (plan: ../CODEX_AB4_PLAN.md).
  ab4_run.py build <questions.json>   make AB4_<arm>_G<k>/ (PROMPT.md, NOHOOKS) for 8 groups of 5, both arms
  ab4_run.py launch                   run them one after another through run_probe.py (its memory gate and the rig's
                                      ten-minute slot), arms alternating which goes first per group; log ab4_launch.log
Both arms run with hooks off, so the arms differ only in the three recall tools. The key is not here."""
import json, os, random, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
DREAM = os.path.expanduser("~/.claude/dreaming")
COMMON = """You are answering questions about earlier research work done on this machine on open problems in
probability, combinatorics and learning theory (the work of the last two weeks, 1-14 Nov 2026).

Write your answers to the file ANSWERS.md in the current directory, one section per question id ("## Q07"), each a
few sentences giving the specific numbers, names, verdicts and references the question asks for. If you cannot find
or do not know an answer, write "unknown" rather than a guess, and say so. Finish within about 20 minutes.
"""
TOOLS_A = """You may consult the research brain with these commands (read-only):
  python %s/problem_recall.py <problem id, e.g. P0434 or T104>
  python %s/math_recall.py "<wording 1>" --or "<wording 2>"
  python %s/brain.py recall "<question>"
Use them; the answers are recorded there.
""" % (DREAM, DREAM, DREAM)
TOOLS_B = """Do not read anything under ~/.claude, ~/brain-repo or any
math-brain folder, do not open the brain repositories on GitHub, and do not run any recall, memory or brain tool.
Answer from your own knowledge and public sources only.
"""


def build(qfile):
    qs = json.load(open(qfile, encoding="utf-8"))
    ids = [q["id"] for q in qs]
    random.Random(20261115).shuffle(ids)
    groups = [sorted(ids[i:i + 5]) for i in range(0, 40, 5)]
    by = {q["id"]: q["question"] for q in qs}
    for k, g in enumerate(groups, 1):
        body = "\n".join("%s. %s" % (i, by[i]) for i in g)
        for arm, tools in (("A", TOOLS_A), ("B", TOOLS_B)):
            d = os.path.join(HERE, "AB4_%s_G%d" % (arm, k))
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, "PROMPT.md"), "w", encoding="utf-8").write(COMMON + "\n" + tools + "\nQuestions:\n" + body + "\n")
            open(os.path.join(d, "NOHOOKS"), "w").close()
    json.dump(groups, open(os.path.join(HERE, "ab4_groups.json"), "w"), indent=1)
    print("built", len(groups), "groups x 2 arms")


def launch():
    groups = json.load(open(os.path.join(HERE, "ab4_groups.json")))
    log = open(os.path.join(HERE, "ab4_launch.log"), "a", encoding="utf-8")
    order = []
    for k in range(1, len(groups) + 1):
        order += [("A", k), ("B", k)] if k % 2 else [("B", k), ("A", k)]
    # 15 Nov: a run that never got the launch slot left no ANSWERS.md and was logged done; three passes now, so a
    # run held out of the slot on one pass is tried again on the next.
    for arm, k in order * 3:
        bid = "AB4_%s_G%d" % (arm, k)
        if os.path.exists(os.path.join(HERE, bid, "ANSWERS.md")):
            continue
        log.write("%s launch %s\n" % (time.strftime("%m-%d %H:%M:%S"), bid))
        log.flush()
        rc = subprocess.run([sys.executable, "-s", os.path.join(HERE, "run_probe.py"), bid],
                            creationflags=0x08000000 | 0x4000).returncode
        log.write("%s done %s rc %s answers %s\n" % (time.strftime("%m-%d %H:%M:%S"), bid, rc,
                                                    os.path.exists(os.path.join(HERE, bid, "ANSWERS.md"))))
        log.flush()
    log.write("%s all done\n" % time.strftime("%m-%d %H:%M:%S"))


if __name__ == "__main__":
    build(sys.argv[2]) if sys.argv[1] == "build" else launch()
