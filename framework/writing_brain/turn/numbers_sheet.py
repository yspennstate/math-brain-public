# Every number a chapter states, pulled into one list and grouped by the thing counted, so that the pairs which
# cannot both be true can be read side by side (a revision rule: clock times, ages, spans and counts are listed
# and read against each other).
#
#   python -I -X utf8 numbers_sheet.py <chapter.md> [<chapter.md> ...] [--all] [--width N]
#
# A group is printed when the same thing is counted two or more times with different numbers (forty people on
# line 8, thirty-nine on line 32). --all prints every group. Clock times are one group. A last list gives each
# number that counts four or more different things (forty people, forty minutes, forty storeys, forty years).
# The sheet decides nothing: thirty-nine and forty can both be right. It puts them where one reading sees them
# together.
import io
import re
import sys

UNITS = ("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
         "seventeen eighteen nineteen").split()
TENS = "twenty thirty forty fifty sixty seventy eighty ninety".split()
BIG = "hundred thousand million billion".split()
ORD = ("first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth twentieth thirtieth "
       "fortieth fiftieth hundredth").split()
W = UNITS + TENS + BIG
ATOM = r"(?:%s)" % "|".join(sorted(W, key=len, reverse=True))
NUM = re.compile(
    r"\b(?:(?:an?|several|some|many) (?=(?:%s)\b))?"
    r"(?:\d[\d,.]*|%s)(?:(?:[- ]| and | or | to )(?:\d[\d,.]*|%s|a half|a quarter))*"
    r"(?:-(?:%s))?\b" % ("|".join(BIG + ["dozen"]), ATOM, ATOM, "|".join(ORD)),
    re.I)
WORDS_AFTER = re.compile(r"[\s\-]*((?:of (?:the |them|us|those )?|more |odd |whole |full |other |or so )*)"
                         r"([A-Za-z][A-Za-z'\-]*)")
CLOCK = re.compile(r"\b(?:at|by|until|till|before|after|since|past|to|towards|about) "
                   r"((?:half past |a quarter (?:to|past) |twenty (?:to|past) |ten (?:to|past) |five (?:to|past) )?"
                   r"(?:%s)(?: o'clock)?)(?= (?:that|this|in the|on the|the next) (?:morning|evening|afternoon|night)"
                   r"|[.,;:]| o'clock| the (?:trams|lamps|sky))" % "|".join(UNITS[:12]), re.I)
NAMED = re.compile(r"\b(noon|midnight|midday|dawn|dusk)\b", re.I)
SKIP_AFTER = set("of and or to the a an in on at is was were had who that which but for from with by as it he she "
                 "they we i you not no so then there here when than into over under more less them us can could "
                 "time times".split())
PRON = {"one": {"of", "thing", "another", "day", "night", "morning", "evening", "place", "piece", "at", "by",
                "more", "who", "that", "was", "is", "could", "would", "had", "can", "does", "did", "or", "and",
                "i", "he", "she", "you", "we", "they"}}


def single(w):
    w = w.lower()
    for a, b in (("ies", "y"), ("ves", "f"), ("men", "man"), ("children", "child"), ("people", "person"),
                 ("feet", "foot")):
        if w.endswith(a):
            return w[:len(w) - len(a)] + b
    if w.endswith("s") and not w.endswith("ss") and len(w) > 3:
        return w[:-1]
    return w


def favourites(groups):
    # number -> {thing: [lines]}, for numbers above three
    by_num = {}
    for key, rows in groups.items():
        for ln, num, _ in rows:
            if num not in ("one", "two", "three"):
                by_num.setdefault(num, {}).setdefault(key, []).append(ln)
    return by_num


def sheet(path, show_all, width):
    lines = io.open(path, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    groups, clock = count(lines, width)
    return render(path, groups, clock, show_all)


def count(lines, width=45):
    groups = {}
    clock = []
    for ln, line in enumerate(lines, 1):
        if line.startswith("#") or not line.strip():
            continue
        for mo in CLOCK.finditer(line):
            clock.append((ln, mo.group(1).lower(), line[max(0, mo.start() - width):mo.end() + width]))
        for mo in NAMED.finditer(line):
            clock.append((ln, mo.group(1).lower(), line[max(0, mo.start() - width):mo.end() + width]))
        for mo in NUM.finditer(line):
            num = mo.group(0).lower()
            after = WORDS_AFTER.match(line, mo.end())
            if not after:
                continue
            unit = after.group(2)
            ul = unit.lower()
            if num in ("one", "a", "an") and (ul in PRON["one"] or ul in SKIP_AFTER):
                continue
            if ul in SKIP_AFTER:
                continue
            if ul in ("year", "years") and re.match(r"[\s]*years?[ -]old", line[mo.end():mo.end() + 12]):
                ul = "year-old"
            key = single(ul)
            groups.setdefault(key, []).append((ln, num, line[max(0, mo.start() - width):after.end() + width]))
    return groups, clock


def render(path, groups, clock, show_all):
    out = ["%s" % path, ""]
    if clock:
        out.append("clock (%d)" % len(clock))
        for ln, num, ctx in clock:
            out.append("  %4d  %-18s ...%s..." % (ln, num, ctx.strip()))
        out.append("")
    for key in sorted(groups, key=lambda k: (-len(set(n for _, n, _ in groups[k])), k)):
        rows = groups[key]
        if not show_all and len(set(n for _, n, _ in rows)) < 2:
            continue
        out.append("%s (%d mentions, %d different numbers)" % (key, len(rows), len(set(n for _, n, _ in rows))))
        for ln, num, ctx in rows:
            out.append("  %4d  %-18s ...%s..." % (ln, num, ctx.strip()))
        out.append("")
    often = [(n, u) for n, u in favourites(groups).items() if len(u) >= 4]
    if often:
        out.append("one number, many things (four or more; a writer's favourite number shows here)")
        for n, u in sorted(often, key=lambda x: -len(x[1])):
            out.append("  %-18s %d things: %s" % (n, len(u), ", ".join(
                "%s (%s)" % (k, ", ".join(str(x) for x in v)) for k, v in sorted(u.items(), key=lambda kv: kv[1][0]))))
        out.append("")
    out.append("%d things counted, %d of them with more than one number; %d clock times" % (
        len(groups), sum(1 for k in groups if len(set(n for _, n, _ in groups[k])) > 1), len(clock)))
    return "\n".join(out)


def main(argv):
    show_all = "--all" in argv
    width = 45
    if "--width" in argv:
        width = int(argv[argv.index("--width") + 1])
    files = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] != "--width")]
    if not files:
        print(__doc__ or "usage: numbers_sheet.py <chapter.md> [--all] [--width N]")
        return 2
    for p in files:
        print(sheet(p, show_all, width))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
