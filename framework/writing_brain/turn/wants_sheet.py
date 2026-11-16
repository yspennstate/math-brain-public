# Wants sheet: how the people on a page use their turns to speak. For each spoken turn (the quoted speech of one
# paragraph) it records whether the turn asks, orders or refuses, and how long it runs. Three tests of one chapter
# beside published openings gave the same reason for the published side: its people want things that cut across one
# another, where ours handed the narrator what his question needed. This sheet counts the plainest trace of a want.
# It is a count, not a verdict: a turn can want something without asking, ordering or refusing.
# Usage: python -I -X utf8 wants_sheet.py <page.md> [<page.md> ...]
import io
import re
import sys

ORDER = set("""go come eat send take look listen sit stand stop wait tell give bring let leave hold get put keep move
say ask read try mind hush hurry run show fetch drink sleep open shut close write answer speak stay help forget
remember hear watch follow call do be never don't""".split())
MUST = re.compile(r"\byou (must|will not|shall|are not|had better|ought|can't|cannot|won't|needn't|are to|have to)\b"
                  r"|\byou'll have to\b|\bi want you\b|\bi forbid\b|\bi won't have\b", re.I)
REFUSE = re.compile(r"^(no\b|not\b|never\b|nonsense\b|certainly not|i won't|i will not|i shan't|i can't|i cannot|"
                    r"i don't|i do not|you are not|you're not|and i said)", re.I)
DQ = re.compile(r'["“]([^"“”]{1,2000}?)["”]')
SQ = re.compile(r"(?:(?<=\s)|^)[‘'](?=[A-Za-z“\"])(.{1,2000}?[,.!?—…-])[’'](?=\s|$|[),;:.])")


def turns(text):
    pars = [p.strip() for p in text.split("\n") if p.strip() and not p.startswith("#")]
    body = "\n".join(pars)
    double = len(DQ.findall(body))
    single = len(SQ.findall(body))
    rx = DQ if double >= single else SQ
    out = []
    for p in pars:
        if p.startswith("*") and p.endswith("*"):
            continue  # a line of verse or a letter set in italics is not a turn
        segs = [s.strip() for s in rx.findall(p) if s.strip()]
        if segs:
            out.append(segs)
    return out, ("double" if rx is DQ else "single")


def sheet(text):
    ts, style = turns(text)
    n = len(ts)
    asks = orders = refuses = wants = long40 = 0
    lengths = []
    for segs in ts:
        whole = " ".join(segs)
        words = re.findall(r"[A-Za-z']+", whole)
        lengths.append(len(words))
        a = "?" in whole
        firsts = [re.findall(r"[A-Za-z']+", s)[:1] for s in re.split(r"(?<=[.!?])\s+", whole)]
        o = any(f and f[0].lower() in ORDER for f in firsts) or bool(MUST.search(whole))
        r = bool(REFUSE.match(whole.lstrip("—- ")))
        asks += a
        orders += o
        refuses += r
        wants += (a or o or r)
        long40 += len(words) >= 40
    lengths.sort()
    pct = lambda k: round(100.0 * k / n, 1) if n else 0.0
    return {"quote_style": style, "words": len(text.split()), "turns": n,
            "turns_per_1000_words": round(1000.0 * n / max(1, len(text.split())), 1),
            "asks_pct": pct(asks), "orders_pct": pct(orders), "refuses_pct": pct(refuses),
            "any_of_three_pct": pct(wants), "median_words_a_turn": lengths[n // 2] if n else 0,
            "turns_of_40_words_or_more_pct": pct(long40)}


if __name__ == "__main__":
    for path in sys.argv[1:]:
        s = sheet(io.open(path, encoding="utf-8").read())
        print(path.replace("\\", "/").split("/")[-1])
        for k, v in s.items():
            print("  %-32s %s" % (k, v))
