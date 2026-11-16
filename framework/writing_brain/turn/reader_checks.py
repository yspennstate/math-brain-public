"""Reader checks: faults a start-to-finish read finds on a page the machine checks pass.

Usage:  python -I -X utf8 reader_checks.py <draft.md> [--sheet] [--totals] [--speeches [N]] [--figures] [--all]
        (places are printed for R7 only; --all prints the places for the other checks too)

Eight leads, each a place to look, not a verdict:
  R1  a connective doubled inside one sentence (so that ... so that; because ... because)
  R2  the same spelled-out quantity twice in one paragraph (a hundred and thirty-four years ... twice)
  R3  a short sentence that ends on a bare pointer (that, it, him, her, them, this, one): is its noun in sight?
  R4  the same fact told twice: two sentences, more than 300 words apart, that share four or more rare words
  R5  a default beat: one word (not an article, a pronoun or a person's name) opening three or more sentences
      within twelve lines ("Nobody sat down." ... "Nobody was buying anything." ... "Nobody was saying anything.")
  R6  a noun handed on: it ends one clause and at once opens the next ("with a letter, and the letter says"; "the hall
      has a door, and the door opens on a yard"). Forty published novels do it 0.44 times in 10,000 words and
      none of them more than 1.03 times; three in one chapter is a habit
  R7  the narrator's maxim: a sentence outside speech that leaves the scene to state a general truth in the
      present tense ("A town is a promise kept by its pumps." "Waiting is a kind of work."). The
      openings of forty published novels have 0.3 in 10,000 words; ask of each whether the scene
      before it has already shown what it says
  R8  an echo across a full stop: a sentence that opens on the word, or the two words, the sentence before it
      ended on ("...as far as the river. The river was low that year..."; "...whatever was there. There
      was a chair..."). It is R6 one size up. Forty published openings
      have 0.5 in 10,000 words pooled: none in more than half of them, 0.9 at three quarters, 3.5 at the most.
      A repeated cry ("I must! I must!") is not counted.
--sheet prints every quantity in the draft grouped by its unit (years, kilometres, storeys, people ...), with the
line it stands on, so that a reader can hold the spans against each other (a town founded a hundred and forty years
back and a "seventy years" since its founding cannot both stand).

--totals prints every sentence that makes a claim about all or none of a group of people (everybody, nobody, not one,
she alone, of the forty of us ...), with its line, so that a reader can hold them against each other ("Everybody
clapped" and, six lines on, "Of the thirty of us he alone had not clapped" cannot both stand).

--figures counts fourteen habits of narration per 10,000 words of narration (speech left out) and prints each beside
the same count on the openings of forty published novels and of 387 later works (authors born 1880 to 1945): a clause hung on the end of a sentence with ", which"; a
comparison made with "the way" or "as you"; "like" before a noun; "as if" or "as though"; and the three forms of
comparison together; "had"; "something", "somewhere", "someone"; "did not", "was not" and the like; and three or more sentences of twelve words or
fewer following one another; the short sentence that only says what a thing is ("It is a street."); the short sentence that opens on
"Not" ("Not peaceful."); and the denial followed by a sentence on the same subject ("He did not look up. He
said my name."); the paragraph of narration that lands on a short sentence; and the paragraph that is one short
sentence ("He waited.").
Where the draft stands above three quarters of both shelves it lists every place,
for the writer to keep the ones that earn it. The forty openings are older than "the way" used to join a
clause; the later shelf is not, and that count is judged against it.

--speeches N prints every stretch of more than N spoken words (55 if no number is given, about four printed lines)
that runs from one quotation mark to the next with nothing told inside it. Published novels do run speeches of that
length, so this is a sheet for a draft whose own plan asks that something happen inside a long speech.

Source of the four: the fourth pass on a draft chapter of 10,700 words (15 Nov 2026), where 28 of 28 machine checks
were green and a read still changed 22 sentences. Source of --totals: the eighth read of the same chapter.
"""
import io
import re
import sys
from collections import Counter, defaultdict

NUM = (r"(?:a|an|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|"
       r"seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|"
       r"half|quarter|\d[\d,.]*)")
QUANT = re.compile(r"\b(" + NUM + r"(?:[ -](?:and[ -])?" + NUM + r")*)[ -]"
                   r"(years?|centur(?:y|ies)|months?|weeks?|days?|hours?|minutes?|kilometres?|metres?|storeys?|"
                   r"people|students|ships?|domes?|lines?|flights?|paces|dishes|names|floors?)\b", re.I)
TOTAL = re.compile(r"\b(everybody|everyone|nobody|no one|not one|none of (?:us|them)|all of (?:us|them)|"
                   r"every one of (?:us|them)|(?:he|she|i|they) alone|the only (?:one|person)|"
                   r"of the [a-z-]+ of us|each of (?:us|them))\b", re.I)
POINTERS = {"that", "it", "him", "her", "them", "this", "one", "those", "these"}
OPEN_SKIP = set("the a an i he she it and but we they in on at you there his her my our their".split())
HAND = re.compile(r"\b([A-Za-z]{3,})(?:,|;| --|\u2014)? (?:and |but |and then )?(?:the|that|this) \1\b")
HAND_SKIP = set("that this the and but had was her his more much very long far out all way".split())
MAXIM = [re.compile(p) for p in (
    r"^(?:A|An) [a-z]+(?: [a-z]+)? (?:is|are|does|has|can|cannot|will|keeps|makes|needs|goes)\b",
    r"^You (?:do not|don't|cannot|can't|can|have to|never|learn|would not)\b",
    r"^[A-Z][a-z]+ing(?: [a-z]+)? (?:is|are)\b",
    r"^(?:It|That|This) is the (?:oldest|only|one|first|last|whole)\b",
    r"^(?:Memory|Time|Grief|Love|Death|Loneliness|Silence|Consciousness|Wanting) (?:is|has|does|keeps|will)\b")]
FIG = [
    ("a clause hung on a sentence with ', which'", re.compile(r", which\b", re.I)),
    ("a comparison made with 'the way' or 'as you'", re.compile(
        r"(?<!on )(?<!all )(?<!by )(?<!in )(?<!this )(?<!that )(?<!half )\bthe way "
        r"(?!down\b|up\b|out\b|in\b|back\b|to\b|home\b|of\b|through\b|across\b|over\b|there\b|here\b|was\b|is\b)"
        r"|\bas (?:you|one|a man|a woman|people|men|children) (?:are|is|do|does|might|would|will)\b", re.I)),
    ("'like' before a noun", re.compile(
        r"\blike (?:a|an|the|some|one|two|something|someone|people|men|women|children)\b", re.I)),
    ("'as if' or 'as though'", re.compile(r"\bas (?:if|though)\b", re.I)),
]
FIG.append(("the three forms of comparison together", re.compile(
    "|".join(p.pattern for _, p in FIG[1:4]), re.I)))
FIG.append(("'had'", re.compile(r"\bhad\b", re.I)))
FIG.append(("'something', 'somewhere', 'someone', 'somehow'", re.compile(
    r"\bsome(?:thing|how|where|one|body)\b", re.I)))
FIG.append(("'did not', 'was not', 'could not' and the like", re.compile(
    r"\b(?:did|was|were|could|would|had|does|is|do) not\b", re.I)))
# A row too frequent to list place by place: its paragraphs with four or more are listed.
FIG_BY_PARAGRAPH = (5,)
# Per 10,000 words of narration in the openings of forty published novels: quarter, median, three quarters, highest.
FIG_REF = [(8.2, 11.3, 18.3, 59.5), (0.0, 0.0, 1.1, 7.6), (3.7, 5.4, 10.2, 27.6), (1.2, 6.2, 9.5, 30.4), (5.5, 13.3, 20.1, 58.9), (78.7, 95.1, 113.6, 148.6), (2.2, 5.6, 10.9, 25.5), (24.8, 32.8, 45.6, 63.4)]
STOP = set("""the a an and or but of to in on at by for with from as is was were be been are it its he she his her
they them their we our you your i my me that this which who whom what when where there here then than so not no had
has have did do does would could should will can may might into out up down over under off again still only one two
said went came like just very more most much some any all each every had been being about after before through""".split())


def sentences(par):
    marked = re.sub(r'([.!?]["\u201d*]?)\s+(?=["\u201c*A-Z])', "\\1\x00", par)
    return [s.strip() for s in marked.split("\x00") if s.strip()]


def words(s):
    return re.findall(r"[A-Za-z']+", s.lower())


RUN_MAX_WORDS = 12
RUN_REF = (0.9, 2.4, 6.4, 91.4)


def told_of(par):
    """The narration of a paragraph: what stands outside double quotation marks."""
    return " ".join(par.replace("\u201c", '"').replace("\u201d", '"').split('"')[0::2])


def short_runs(par):
    """Runs of three or more short sentences following one another in a paragraph that is mostly narration."""
    told = told_of(par)
    if len(told.split()) < 0.5 * len(par.split()):
        return []
    out = []
    ss = sentences(told)
    i = 0
    while i < len(ss):
        j = i
        while j < len(ss) and len(words(ss[j])) <= RUN_MAX_WORDS:
            j += 1
        if j - i >= 3:
            out.append(" ".join(ss[i:j]))
        i = max(j, i + 1)
    return out


FLAT_MAX_WORDS = 8
FLAT_HEAD = re.compile(r"^(it|that|this|there) (is|was|were|had been|would be|would have been)\b", re.I)
FLAT_REF = (0.0, 0.9, 2.3, 20.8)


def flat_statements(par):
    """Short sentences of narration that open on It/That/This/There and is/was: 'It is a street.'"""
    told = told_of(par)
    if len(told.split()) < 0.5 * len(par.split()):
        return []
    return [b.strip() for b in sentences(told)[1:]
            if len(words(b)) <= FLAT_MAX_WORDS and FLAT_HEAD.match(b.strip(" *_\u2014"))
            and not b.rstrip().endswith("?")]


NOT_MAX_WORDS = 8
NOT_REF = (0.0, 0.0, 0.0, 3.6)
DENY_MAX_WORDS = 14
DENY_HEAD = re.compile(r"^(it|that|this|he|she|they|i|we) (was|were|is|did|had|could|would)(n't| not)\b", re.I)
DENY_REF = (0.0, 0.0, 0.0, 3.2)


def not_fragments(par):
    """Short sentences of narration that open on Not: 'Not peaceful.'"""
    told = told_of(par)
    if len(told.split()) < 0.5 * len(par.split()):
        return []
    return [s.strip() for s in sentences(told)
            if re.match(r"^Not\b", s.strip(" *_\u2014")) and len(words(s)) <= NOT_MAX_WORDS
            and not s.rstrip().endswith("?")]


def denial_pairs(par):
    """A short denial, then a sentence on the same subject that is not a denial: 'He did not look up. He said
    my name.'"""
    told = told_of(par)
    if len(told.split()) < 0.5 * len(par.split()):
        return []
    ss = sentences(told)
    out = []
    for a, b in zip(ss, ss[1:]):
        a0 = a.strip(" *_\u2014")
        b0 = b.strip(" *_\u2014")
        if (DENY_HEAD.match(a0) and len(words(a0)) <= DENY_MAX_WORDS and words(b0)[:1] == words(a0)[:1]
                and not DENY_HEAD.match(b0)):
            out.append(a0 + " " + b0)
    return out


ECHO_SKIP = set("it he she i you they we him her them me us this that no yes so then there here not now one "
                "all too again".split())
ECHO_ART = ("the", "that", "this", "a", "an")


def echo_places(par):
    """Pairs (first sentence, second sentence) where the second opens on what the first ended on."""
    out = []
    ss = sentences(par)
    for a, b in zip(ss, ss[1:]):
        wa, wb = words(a), words(b)
        if len(wa) < 2 or len(wb) < 2:
            continue
        if wa == wb or a.rstrip(' "*\u201d\u2019').endswith("!"):
            continue          # a repeated cry ("I must! I must!") is speech, not this fault
        k = wa[-1]
        two = wa[-2:] == wb[:2]
        one = len(k) >= 3 and k not in ECHO_SKIP and (wb[0] == k or (wb[0] in ECHO_ART and wb[1] == k))
        if two or one:
            out.append((a, b))
    return out


CLOSE_MAX_WORDS = 6
CLOSE_BEFORE_MEAN = 10
CLOSE_REF = (0.0, 0.0, 2.9, 14.7)
LINE_MAX_WORDS = 8
LINE_REF = (0.0, 1.2, 6.0, 29.9)
LAND_ABBR = re.compile(r"\b(Mr|Mrs|Ms|Dr|St|Mons|Messrs|Capt|Col|Rev|Hon|Gen|Lieut|Mme|Mlle|No|Esq|Sr|Jr|[A-Z])\.$")
LAND_SKIP = re.compile(r"^\s*[\u2014\u2015\u2013\-_\u2018'\[(*#>]")
LAND_HEADING = re.compile(r"^(chapter|book|part|volume|letter|section)\b", re.I)


def _narration_sentences(par):
    told = told_of(par)
    if len(told.split()) < 0.5 * len(par.split()):
        return None
    return [s.strip() for s in sentences(told) if s.strip()]


def short_closers(par):
    """A paragraph of narration, three sentences or more, that lands on a sentence of CLOSE_MAX_WORDS words or fewer
    after sentences averaging CLOSE_BEFORE_MEAN words or more: "... Nobody had touched it." """
    if LAND_SKIP.match(par):
        return []
    ss = _narration_sentences(par)
    if not ss or len(ss) < 3:
        return []
    last = ss[-1]
    n = len(words(last))
    if n == 0 or n > CLOSE_MAX_WORDS or not re.search(r"[.!]$", last) or LAND_ABBR.search(ss[-2]):
        return []
    before = [len(words(s)) for s in ss[:-1]]
    if sum(before) / len(before) < CLOSE_BEFORE_MEAN:
        return []
    return [ss[-2][-70:] + " || " + last]


def one_line_paragraphs(par):
    """A paragraph of narration that is one sentence of LINE_MAX_WORDS words or fewer: "He waited." """
    if '"' in par or "\u201c" in par or LAND_SKIP.match(par) or par.upper() == par or LAND_HEADING.match(par):
        return []
    ss = _narration_sentences(par)
    if not ss or len(ss) != 1:
        return []
    n = len(words(ss[0]))
    if n == 0 or n > LINE_MAX_WORDS or not re.search(r"[.!]$", ss[0]):
        return []
    return [ss[0]]


# The same counts on a later shelf: the openings of 387 novels and stories by authors born 1880 to 1945.
# (quarter, median, three quarters, highest), in the order of the rows of the sheet.
LATER_REF = [(2.2, 4.5, 8.3, 32.0),
             (0.0, 0.0, 1.5, 8.6),
             (4.2, 7.2, 12.7, 39.8),
             (2.9, 5.8, 10.0, 32.2),
             (8.9, 15.8, 22.3, 65.6),
             (81.8, 110.3, 138.5, 285.0),
             (5.7, 10.0, 15.0, 35.9),
             (17.3, 28.1, 39.4, 92.3),
             (4.5, 10.8, 21.5, 101.7),
             (1.3, 2.8, 5.7, 26.4),
             (0.0, 0.0, 0.0, 9.7),
             (0.0, 0.0, 0.0, 6.4),
             (1.6, 4.1, 7.9, 21.1),
             (1.8, 5.4, 13.4, 160.8)]


def _beside(i, ref):
    """What is printed beside row i, and the mark a count has to pass before its places are listed: the higher of the
    two shelves' three-quarter marks."""
    text = ""
    mark = None
    if ref:
        text += "   published openings: quarter %.1f, median %.1f, three quarters %.1f, highest %.1f" % tuple(ref)
        mark = ref[2]
    if i < len(LATER_REF):
        text += "; later shelf: median %.1f, three quarters %.1f, highest %.1f" % tuple(LATER_REF[i][1:])
        mark = LATER_REF[i][2] if mark is None else max(mark, LATER_REF[i][2])
    return text, mark


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    path = argv[0]
    sheet = "--sheet" in argv
    lines = io.open(path, encoding="utf-8").read().split("\n")
    pars = [(i + 1, l) for i, l in enumerate(lines) if l.strip() and not l.startswith("#")]
    allw = Counter(w for _, p in pars for w in words(p))
    total = sum(allw.values())
    found = defaultdict(list)
    sent_index = []
    pos = 0
    for ln, par in pars:
        qs = [(m.group(1).lower().replace("-", " ") + " " + m.group(2).lower().rstrip("s")) for m in QUANT.finditer(par)]
        qs = [q for q in qs if len(q.split()) >= 3]
        for q, n in Counter(qs).items():
            if n > 1:
                found["R2"].append((ln, "'%s' %d times in this paragraph" % (q, n)))
        for m in HAND.finditer(par):
            seg = m.group(0)
            if m.group(1).lower() in HAND_SKIP or not ("," in seg or ";" in seg or " and " in seg or " but " in seg):
                continue
            found["R6"].append((ln, "...%s..." % par[max(0, m.start() - 50):m.end() + 40]))
        told = " ".join(par.replace("\u201c", '"').replace("\u201d", '"').split('"')[0::2])
        for s in sentences(told):
            if any(p.search(s) for p in MAXIM):
                found["R7"].append((ln, s))
        for a, b in echo_places(par):
            found["R8"].append((ln, "...%s || %s" % (a[-60:], b[:60])))
        prev = ""
        for s in sentences(par):
            low = " " + " ".join(words(s)) + " "
            for c in (" so that ", " because ", " although ", " in order to "):
                if low.count(c) > 1:
                    found["R1"].append((ln, "%s twice: %s" % (c.strip(), s[:150])))
            w = words(s)
            if 2 <= len(w) <= 6 and w[-1] in POINTERS and not s.startswith('"'):
                found["R3"].append((ln, "%s   [before it: ...%s]" % (s, prev[-70:])))
            rare = frozenset(x for x in w if x not in STOP and len(x) > 3 and allw[x] <= 4)
            sent_index.append((pos, ln, s, rare))
            pos += len(w)
            prev = s
    for a in range(len(sent_index)):
        pa, la, sa, ra = sent_index[a]
        if len(ra) < 4:
            continue
        for b in range(a + 1, len(sent_index)):
            pb, lb, sb, rb = sent_index[b]
            if pb - pa < 300:
                continue
            common = ra & rb
            if len(common) >= 4:
                found["R4"].append((la, "lines %d and %d share %s" % (la, lb, ", ".join(sorted(common)))))
    # R5: a default beat. The same word opens three or more sentences within twelve lines of the file.
    # A word the draft never writes in lower case is taken for a name and left out.
    lower_seen = set(re.findall(r"(?<![A-Za-z'])[a-z][a-z']*", "\n".join(p for _, p in pars)))
    first = defaultdict(list)
    for _, ln, s, _ in sent_index:
        w = words(s)
        if len(w) >= 2 and w[0] not in OPEN_SKIP and w[0] in lower_seen:
            first[w[0]].append(ln)
    for k in sorted(first):
        ls = first[k]
        a = 0
        while a + 2 < len(ls):
            if ls[a + 2] - ls[a] <= 12:
                b = a + 2
                while b + 1 < len(ls) and ls[b + 1] - ls[b] <= 6:
                    b += 1
                found["R5"].append((ls[a], "'%s' opens %d sentences between lines %d and %d" % (k.capitalize(), b - a + 1, ls[a], ls[b])))
                a = b + 1
            else:
                a += 1
    found["R5"].sort()
    names = {"R1": "a connective doubled in one sentence", "R2": "the same quantity twice in a paragraph",
             "R3": "a short sentence ending on a bare pointer", "R4": "the same fact told twice, far apart",
             "R5": "one word opening three sentences close together",
             "R6": "a noun that ends one clause and opens the next",
             "R7": "a general truth stated by the narrator",
             "R8": "a sentence opening on the word the last one ended on"}
    n_sent = len(sent_index)
    print("%s: %d words, %d sentences" % (path.replace("\\", "/").split("/")[-1], total, n_sent))
    # Beside the blind readers' own complaints (CH1P, CH1Q) only R7 pointed at sentences a reader also named;
    # the shape checks matched none. Their counts are still printed, their places only with --all.
    show_all = "--all" in argv
    for k in ("R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"):
        print("%s  %s: %d" % (k, names[k], len(found[k])))
        if k == "R7" or show_all:
            for ln, msg in found[k][:12]:
                print("   %4d: %s" % (ln, msg[:230]))
    print("R7 is provisional (5 of its 9 flags fell on sentences a blind reader named). Places for the other"
          " checks: --all.")
    if sheet:
        by = defaultdict(list)
        for ln, par in pars:
            for m in QUANT.finditer(par):
                by[m.group(2).lower().rstrip("s")].append((ln, m.group(0)))
        print("\nQuantity sheet (unit: line quantity)")
        for unit in sorted(by, key=lambda u: -len(by[u])):
            print("  %s: %s" % (unit, "; ".join("%d %s" % (ln, q) for ln, q in by[unit][:40])))
    if "--totals" in argv:
        rows = [(ln, m.group(1).lower(), s) for _, ln, s, _ in sent_index for m in [TOTAL.search(s)] if m]
        print("\nTotals sheet: %d sentences that speak for all or none of a group (line [word] sentence)" % len(rows))
        for ln, w, s in rows:
            print("   %4d [%s] %s" % (ln, w, s[:170]))
    if "--speeches" in argv:
        i = argv.index("--speeches")
        lim = int(argv[i + 1]) if i + 1 < len(argv) and argv[i + 1].isdigit() else 55
        rows = []
        for ln, par in pars:
            pieces = par.replace("“", '"').replace("”", '"').split('"')
            for q in pieces[1::2]:
                if len(q.split()) > lim:
                    rows.append((ln, len(q.split()), q))
        print("\nSpeeches: %d stretches of more than %d spoken words with nothing told inside them (line words opening)"
              % (len(rows), lim))
        for ln, n, q in rows:
            print("   %4d %3d  %s ..." % (ln, n, q[:100]))
    if "--figures" in argv:
        nw = 0
        hits = [[] for _ in FIG]
        runs = []
        flats = []
        nots = []
        denials = []
        closers = []
        oneliners = []
        for ln, par in pars:
            flats.extend((ln, s) for s in flat_statements(par))
            nots.extend((ln, s) for s in not_fragments(par))
            denials.extend((ln, s) for s in denial_pairs(par))
            closers.extend((ln, s) for s in short_closers(par))
            oneliners.extend((ln, s) for s in one_line_paragraphs(par))
            runs.extend((ln, r) for r in short_runs(par))
            told = " ".join(par.replace("\u201c", '"').replace("\u201d", '"').split('"')[0::2])
            nw += len(told.split())
            for i, (_, pat) in enumerate(FIG):
                for m in pat.finditer(told):
                    hits[i].append((ln, told[max(0, m.start() - 60):m.end() + 50]))
        print("\nFigures sheet: %d words of narration (speech left out); per 10,000 words" % nw)
        for i, (name, _) in enumerate(FIG):
            rate = 1e4 * len(hits[i]) / max(1, nw)
            ref = FIG_REF[i] if FIG_REF else None
            line = "  %-46s %3d places, %5.1f" % (name, len(hits[i]), rate)
            beside, mark = _beside(i, ref)
            print(line + beside)
            if mark is not None and rate > mark and i in FIG_BY_PARAGRAPH:
                per = {}
                for ln, _e in hits[i]:
                    per[ln] = per.get(ln, 0) + 1
                print("     above three quarters of both shelves; paragraphs with four or more:")
                for n, ln in sorted(((n, ln) for ln, n in per.items() if n >= 4), reverse=True):
                    print("     %4d  %d places" % (ln, n))
            elif mark is not None and rate > mark:
                print("     above three quarters of both shelves; every place:")
                for ln, e in hits[i]:
                    print("     %4d ...%s" % (ln, e))
        rate = 1e4 * len(runs) / max(1, nw)
        line = "  %-46s %3d places, %5.1f" % ("three or more short sentences in a row", len(runs), rate)
        beside, mark = _beside(len(FIG), RUN_REF)
        print(line + beside)
        if mark is not None and rate > mark:
            print("     above three quarters of both shelves; every run:")
            for ln, r in runs:
                print("     %4d  %s" % (ln, r[:170]))
        rate = 1e4 * len(flats) / max(1, nw)
        line = "  %-46s %3d places, %5.1f" % ("a short 'It is', 'That was', 'There was' sentence", len(flats), rate)
        beside, mark = _beside(len(FIG) + 1, FLAT_REF)
        print(line + beside)
        if mark is not None and rate > mark:
            print("     above three quarters of both shelves; every place:")
            for ln, s in flats:
                print("     %4d  %s" % (ln, s[:170]))
        for k, (label, found, ref) in enumerate((("a short sentence that opens on 'Not'", nots, NOT_REF),
                                  ("a denial, then the same subject again", denials, DENY_REF),
                                  ("a paragraph that lands on a short sentence", closers, CLOSE_REF),
                                  ("a paragraph of one short sentence", oneliners, LINE_REF))):
            rate = 1e4 * len(found) / max(1, nw)
            line = "  %-46s %3d places, %5.1f" % (label, len(found), rate)
            beside, mark = _beside(len(FIG) + 2 + k, ref)
            print(line + beside)
            if mark is not None and rate > mark:
                print("     above three quarters of both shelves; every place:")
                for ln, s in found:
                    print("     %4d  %s" % (ln, s[:170]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
