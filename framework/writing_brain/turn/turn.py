#!/usr/bin/env python3
"""turn.py - plan a page of fiction from what blind readers placed first.

    python -I -X utf8 turn.py plan                 the plan a writer fills in before drafting, and the cutting pass
    python -I -X utf8 turn.py draw [--alone]       a random scene shape and route for one page (--alone: one person)
                         [--seed N] [--json]
    python -I -X utf8 turn.py commons F1 F2 ...    what several drafts of ONE brief share (the page everyone writes)
                         [--brief "<the brief>"]   leave the brief's own words out of the count
                         [--min N]                 a word counts when N drafts hold it (default: half of them)
                         [--json]
    python -I -X utf8 turn.py bank                 the shared page of six judged briefs, for reference
    python -I -X utf8 turn.py selftest

Where the plan comes from is in README.md beside this file. Standard library only.
"""
import collections
import glob
import itertools
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

PLAN = """\
THE PLAN FOR ONE PAGE (write these five lines in your notes before you draft; a line each, no more)

1. THE PAGE EVERYONE WRITES. Put down, in a few short phrases, the page any capable writer would make of this
   brief: how it opens, the two or three objects in it, how it ends. Twelve writers were once given one brief
   (a father teaching his grown son to drive the farm truck); all twelve opened on the father's instruction
   at the pedals, seven showed a pale shape on a wall where something used to hang, seven had a socket or a
   spanner loose in the cab, ten used the dashboard. A reader who has met that page once has met it twelve
   times. Yours may share the setting. It may not share the opening, the thing the page turns on, or the
   ending.

2. WHO THEY ARE. For each person, one habit or want that the brief did not give you and that will show in how
   he talks or handles things. (One person alone: one habit that decides HOW she does the task.) A person is
   known by a choice only that person would make, not by a list of things noticed about them.

3. THE TURN. One sentence: what is different between these people at the last line from the first, and the
   single act, object or line that carries it. A change, not a mood: who gives way, who takes over, what is
   offered and taken, what is let pass. (One person alone: a choice she makes that the page did not promise,
   and that tells us what the next day is to her.) Think of three; keep the one a stranger could not have
   guessed from the brief but would believe at once.

4. WHERE IT FALLS. In the last third, in something done or said, and nobody on the page remarks on it.

5. WHAT IS LEFT OUT. The one thing the reader would most expect to be told, which you will not tell.

WHILE YOU DRAFT
   Every exchange either moves toward the turn or shows who one of them is. The routine of the task (the gears,
   the strokes of the oar, the running total) gets only as many lines as the turn needs to stand on.

THE CUTTING PASS (after the draft, before you save)
   Cut or change each of these where you find it:
   - an object that comes in once and changes nothing;
   - a gesture used a second time that brings nothing new the second time;
   - a line, spoken or narrated, that says what the scene means, or names a feeling;
   - a reply that sounds prepared: a quip that would do as a caption;
   - a last line that says again what the page has already shown. End on the act, and stop.
   And look hard at any object you planted early so that it could come back and close the page. If it would
   not have come back by itself, the reader sees your hand. Let the ending be something these two do.
"""

# A sixth line, under test. It is printed only by `plan --want`; the default plan is unchanged.
WANT = """\
3. THE OTHER WANT. Name one person on the page, other than the one we follow, who wants something the one
   we follow does not want, and the one thing that person does about it on this page: asks for it, takes
   it, refuses, stalls, changes the subject, does the job a different way. Agreeing, helping, listening and
   explaining do not count. It can be small (who holds the brush, which way round the job is done), and
   nobody has to raise a voice. (One person alone: something in the task that will not go the way she
   wants, and what she does when it does not.)
"""


def plan_want():
    p = PLAN.replace("write these five lines", "write these six lines")
    for old, new in (("5. WHAT IS LEFT OUT", "6. WHAT IS LEFT OUT"), ("4. WHERE IT FALLS", "5. WHERE IT FALLS"),
                     ("3. THE TURN", "4. THE TURN")):
        p = p.replace(old, new)
    return p.replace("4. THE TURN", WANT + "\n4. THE TURN")

STOP = set("""the a an and or but of to in on at by for with from his her he she it its is was were be been had
has have i you your my me we they them their that this then there here not no yes as if so do did does don didn
t s ll ve re d m what where when how who which into out up down over off back again now just than too very can
could would should will shall one two all some any more less like get got go going went come came put take
took let make made said say know knew see saw look looked him himself herself after before until till while
through about still only also once""".split())


def stem(w):
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[: -len(suf)]
    return w


def read(path):
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        return f.read()


def content_stems(text, brief=""):
    drop = {stem(w) for w in re.findall(r"[a-z]+", brief.lower())}
    out = []
    for w in re.findall(r"[a-z]+", text.lower()):
        if w in STOP or len(w) < 3:
            continue
        s = stem(w)
        if s not in drop:
            out.append(s)
    return out


def first_line(text):
    for line in text.splitlines():
        line = line.strip()
        if line:
            return re.sub(r"[^a-z ]", "", line.lower()).split()
    return []


def commons(texts, brief="", min_docs=None):
    """What a set of drafts of one brief share. Returns a dict."""
    n = len(texts)
    if min_docs is None:
        min_docs = max(2, (n + 1) // 2)
    sets = [set(content_stems(t, brief)) for t in texts]
    df = collections.Counter(s for st in sets for s in st)
    shared = [(w, c) for w, c in df.most_common() if c >= min_docs]
    pairs = list(itertools.combinations(range(n), 2))
    jac = [len(sets[a] & sets[b]) / max(1, len(sets[a] | sets[b])) for a, b in pairs]
    opens = collections.Counter(" ".join(first_line(t)[:2]) for t in texts)
    typical = []
    for st in sets:
        typical.append(round(sum(df[s] for s in st) / max(1, len(st)), 2))
    return {
        "drafts": n,
        "min_docs": min_docs,
        "shared": shared,
        "mean_pairwise_jaccard": round(sum(jac) / max(1, len(jac)), 3),
        "openings": opens.most_common(3),
        "typicality": typical,
    }


def print_commons(res, names=None):
    print("drafts: %d   a word counts when %d of them hold it" % (res["drafts"], res["min_docs"]))
    print("shared invention (%d words the brief did not give): %s" % (
        len(res["shared"]), " ".join("%s:%d" % wc for wc in res["shared"][:60])))
    print("first two words, most common: %s" % ", ".join("'%s' x%d" % oc for oc in res["openings"]))
    print("mean overlap between two drafts (Jaccard on content words): %.3f" % res["mean_pairwise_jaccard"])
    if names:
        order = sorted(range(len(names)), key=lambda i: -res["typicality"][i])
        print("closest to the shared page first: " + ", ".join(
            "%s %.2f" % (os.path.basename(names[i]), res["typicality"][i]) for i in order))


def cmd_commons(argv):
    brief, min_docs, as_json, files = "", None, False, []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--brief":
            brief = argv[i + 1]; i += 2
        elif a == "--min":
            min_docs = int(argv[i + 1]); i += 2
        elif a == "--json":
            as_json = True; i += 1
        else:
            files.extend(sorted(glob.glob(a)) or [a]); i += 1
    if len(files) < 3:
        print("commons needs three or more drafts of one brief")
        return 2
    res = commons([read(f) for f in files], brief, min_docs)
    if as_json:
        print(json.dumps(res))
    else:
        print_commons(res, files)
    return 0


def cmd_bank():
    p = os.path.join(HERE, "evidence", "commons_bank.json")
    if not os.path.exists(p):
        print("no bank beside this file")
        return 1
    for row in json.load(open(p, encoding="utf-8")):
        print("\n%s  (%d drafts, mean overlap %.3f)" % (row["brief"], row["drafts"], row["mean_pairwise_jaccard"]))
        print("  opens: %s" % ", ".join("'%s' x%d" % tuple(o) for o in row["openings"]))
        print("  shared: %s" % " ".join("%s:%d" % tuple(wc) for wc in row["shared"][:40]))
    return 0


# ---------------------------------------------------------------------------------------------------------------
# The draw. Writers given one brief condition on the same words and land on the same page (README). A writer
# cannot randomise himself out of that: asked for something unexpected, each produces the same unexpected thing.
# So the choice of branch is made outside the writer, by a random leaf of a small tree of scene shapes, and the
# route to the turn is a +-1 walk pinned at its end. What the brief fixes is never drawn.
OPENS = [
    "a thing being handled, before anyone has spoken",
    "a line of speech that is not about the task",
    "the task already half done",
    "one of them watching the other, not yet noticed",
    "a small mishap: something dropped, stuck, spilled or forgotten",
    "a sound or the weather in one clause, then straight to a hand at work",
]
OPENS_ALONE = [
    "a thing being handled, already in the hand",
    "the task already half done",
    "a small mishap: something dropped, stuck, spilled or forgotten",
    "a sound from outside the room in one clause, then straight to a hand at work",
    "a thing looked for and not found where it is kept",
    "a thing put down again after being picked up",
]
TURNS = [
    "something is offered and taken without remark",
    "something is refused, and then done anyway",
    "one of them takes over what the other was doing",
    "a thing is let pass that would once have been answered",
    "a thing is handed back, or left behind on purpose",
    "a question is answered with an act and not with words",
]
TURNS_ALONE = [
    "does one thing out of the order it has always been done in",
    "leaves out the thing that was meant to go first",
    "takes one thing that had been decided against",
    "does for himself or herself what someone else always did",
    "changes one small thing kept the same for years",
    "stops to finish a different, older task before going on",
]
CARRIED = [
    "an act of the hands",
    "an object that has been in plain use on the page all along (not one brought in for the purpose)",
    "one short line of speech, about something else",
]
ENDS = [
    "an act, in mid-motion",
    "a line of speech that is about something else",
    "the act itself, with the other's answer to it left off the page",
]
ENDS_ALONE = [
    "an act, in mid-motion",
    "a thing set down in a place it has not been before",
    "a small sound the person makes or stops making",
]
HABITS = [
    "how this one handles a tool or a thing that is not his own",
    "what the hands do when this one is not talking",
    "a thing this one always checks, twice",
    "how this one counts, measures or keeps track",
    "a word or turn of phrase this one leans on",
    "what this one will not throw away",
    "what this one does in place of answering a question",
    "an order this one always does things in",
]
STEPS = 5  # exchanges before the turn


def draw(alone=False, rng=None):
    """One random scene shape and one route. Returns a dict; the caller prints it."""
    if rng is None:
        import random
        rng = random.SystemRandom()
    shape = {
        "opens": rng.choice(OPENS_ALONE if alone else OPENS),
        "turn": rng.choice(TURNS_ALONE if alone else TURNS),
        "carried": rng.choice(CARRIED[:2] if alone else CARRIED),
        "ends": rng.choice(ENDS_ALONE if alone else ENDS),
        "habits": rng.sample(HABITS, 1 if alone else 2),
    }
    if not alone:
        shape["mover"] = rng.choice(["the first person the brief names", "the other one"])
    # the route: a walk of STEPS +-1 steps pinned to end one step from where it began, uniform over such paths,
    # so that at the turn the two stand about where they started and nothing before it has given it away.
    net = rng.choice([1, -1])
    ups = (STEPS + net) // 2
    up_at = set(rng.sample(range(STEPS), ups))
    shape["route"] = ["+" if i in up_at else "-" for i in range(STEPS)]
    return shape


def print_draw(s, alone=False):
    near = "nearer the choice" if alone else "nearer each other"
    far = "further from it" if alone else "further apart"
    print("THE SHAPE DRAWN FOR THIS PAGE (it is yours alone: every other writer of this brief drew a different one)\n")
    print("  opens on:     %s" % s["opens"])
    if "mover" in s:
        print("  who moves:    %s" % s["mover"])
    print("  the turn:     %s%s" % ("the person " if alone else "", s["turn"]))
    print("  carried by:   %s" % s["carried"])
    print("  ends on:      %s" % s["ends"])
    for i, h in enumerate(s["habits"]):
        print("  %s %s" % ("habit:       " if alone else "habit, %s: " % ("one" if i == 0 else "two"), h))
    print("  the route:    %s  then the turn" % " ".join(s["route"]))
    print("""
HOW TO USE IT
  Write the plan's five lines inside this shape. The shape says what kind of thing happens; what it is, who these
  people are and every particular are yours to find.
  The route is the %d exchanges or movements before the turn, in order: + leaves them %s than
  the one before, - leaves them %s. It ends about where it began, so the turn has not been given away
  before it comes. An exchange may be a line and its answer, or a thing done and how it is met.
  What the brief fixes always wins. If the shape cannot be made to fit the brief, draw once more (twice at most)
  and say so in your notes. Nothing of the shape is named on the page.""" % (STEPS, near, far))


def cmd_draw(argv):
    alone = "--alone" in argv
    rng = None
    if "--seed" in argv:
        import random
        rng = random.Random(int(argv[argv.index("--seed") + 1]))
    s = draw(alone, rng)
    if "--json" in argv:
        print(json.dumps(s))
    else:
        print_draw(s, alone)
    return 0


def selftest():
    ok = True

    def check(name, cond):
        nonlocal ok
        print(("pass  " if cond else "FAIL  ") + name)
        ok = ok and cond

    same = ["The clutch went down. A socket rolled on the dashboard past the pale rectangle.",
            "He pressed the clutch. The socket rolled over the dashboard near a pale rectangle.",
            "Clutch first. A socket rolled along the dashboard; a pale rectangle marked the wall.",
            "Clutch down, he said. The socket rolled across the dashboard, below the pale rectangle."]
    apart = ["The heron stood in the reeds while the tide went out under the bridge.",
             "She salted the dough and left the oven door open for the cat.",
             "Two surveyors argued over a chain and a brass plumb line at noon.",
             "The telegram boy leaned his bicycle against the chapel railings."]
    a = commons(same)
    b = commons(apart)
    words = {w for w, _ in a["shared"]}
    check("planted shared props are found", {"socket", "dashboard", "rectangle", "clutch"} <= words)
    check("unrelated drafts share nothing", len(b["shared"]) == 0)
    check("overlap is higher for the alike set", a["mean_pairwise_jaccard"] > b["mean_pairwise_jaccard"] + 0.2)
    c = commons(same, brief="clutch socket")
    check("brief words are left out", not ({"clutch", "socket"} & {w for w, _ in c["shared"]}))
    mixed = commons(same[:3] + [apart[0]])
    check("the odd draft is the least typical", mixed["typicality"][3] == min(mixed["typicality"]))
    check("plan has the five lines and the cutting pass", all(k in PLAN for k in (
        "1. THE PAGE EVERYONE WRITES", "2. WHO THEY ARE", "3. THE TURN", "4. WHERE IT FALLS",
        "5. WHAT IS LEFT OUT", "THE CUTTING PASS")))
    check("plan is ASCII", all(ord(ch) < 128 for ch in PLAN))
    pw = plan_want()
    check("plan --want has six lines in order and leaves the rest alone", all(k in pw for k in (
        "write these six lines", "1. THE PAGE EVERYONE WRITES", "2. WHO THEY ARE", "3. THE OTHER WANT", "4. THE TURN",
        "5. WHERE IT FALLS", "6. WHAT IS LEFT OUT", "THE CUTTING PASS")) and "3. THE TURN" not in pw
        and pw.count("WHAT IS LEFT OUT") == 1 and all(ord(ch) < 128 for ch in pw)
        and pw.replace(WANT + "\n", "").replace("six lines", "five lines").replace("4. THE TURN", "3. THE TURN")
        .replace("5. WHERE", "4. WHERE").replace("6. WHAT IS", "5. WHAT IS") == PLAN)
    import random
    a1, a2 = draw(False, random.Random(7)), draw(False, random.Random(7))
    check("a seeded draw repeats", a1 == a2)
    check("a pair draw has every part", set(a1) == {"opens", "turn", "carried", "ends", "habits", "mover", "route"}
          and len(a1["habits"]) == 2 and a1["habits"][0] != a1["habits"][1])
    al = draw(True, random.Random(7))
    check("a draw for one person alone has no mover and one habit", "mover" not in al and len(al["habits"]) == 1
          and al["turn"] in TURNS_ALONE and al["opens"] in OPENS_ALONE)
    rng = random.Random(11)
    many = [draw(False, rng) for _ in range(6000)]
    check("every route has %d steps and ends one step from its start" % STEPS, all(
        len(m["route"]) == STEPS and abs(m["route"].count("+") - m["route"].count("-")) == 1 for m in many))
    routes = collections.Counter(" ".join(m["route"]) for m in many)
    # 20 paths (10 ending one up, 10 one down), each with chance 1/20: 300 expected of 6000, sd about 17
    check("the route is uniform over the 20 pinned paths", len(routes) == 20 and all(230 < c < 370 for c in routes.values()))
    for key, table in (("opens", OPENS), ("turn", TURNS), ("carried", CARRIED), ("ends", ENDS)):
        c = collections.Counter(m[key] for m in many)
        e = 6000 / len(table)
        check("%s: every branch is drawn, about equally" % key, len(c) == len(table) and all(abs(v - e) < 5 * (e ** 0.5) + 1 for v in c.values()))
    sys_draws = [json.dumps(draw(False), sort_keys=True) for _ in range(6)]
    check("six unseeded draws give at least five different shapes", len(set(sys_draws)) >= 5)
    check("draw tables are ASCII", all(ord(ch) < 128 for t in (OPENS, OPENS_ALONE, TURNS, TURNS_ALONE, CARRIED, ENDS, ENDS_ALONE, HABITS) for s in t for ch in s))
    print("ALL PASS" if ok else "FAILED")
    return 0 if ok else 1


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "plan":
        sys.stdout.write(plan_want() if "--want" in argv[1:] else PLAN)
        return 0
    if argv[0] == "draw":
        return cmd_draw(argv[1:])
    if argv[0] == "commons":
        return cmd_commons(argv[1:])
    if argv[0] == "bank":
        return cmd_bank()
    if argv[0] == "selftest":
        return selftest()
    print("unknown command: %s" % argv[0])
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
