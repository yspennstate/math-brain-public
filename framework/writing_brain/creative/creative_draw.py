"""Creative draw: probability used to keep a writer off the obvious.

Part of the writing brain (14 November 2026). House rule: use the probability theory we study to make agents
more creative when they write.

  refs  --wing literature --role description --k 3 --agent ID [--pool 160] [--seed N] [--draw spread|dpp]
        Hands the writer k model passages of the kind it is about to write, chosen to differ in MANNER:
        sentence length and its spread, dialogue share, punctuation, word length, the profile of function
        words (style kernel, RBF at the median distance), mixed 0.7/0.3 with content-word cosine. Each
        agent has a self-repelling memory, in the manner of an excited walk that avoids its own trace:
        q = exp(-beta * times shown), so the draw keeps moving through the shelf instead of returning to
        favourites.
        --draw spread (default): first passage drawn with weight q, each next one the least like any drawn.
        --draw dpp: an exact k-determinantal draw from L = diag(q) S diag(q) (spectral algorithm of Hough,
        Krishnapur, Peres and Virag; k-DPP step of Kulesza and Taskar, Found. Trends ML 5 (2012), Alg. 8).
        MEASURED 14 Nov, 20 seeds, description and dialogue: style likeness of the three drawn is 0.09-0.15
        with spread, 0.34-0.39 with the k-DPP at every bandwidth tried (tau 1 to 0.03), 0.36 with a plain
        random draw; the k-DPP beat the plain draw on 9-12 of 20 seeds, i.e. not at all. The shelf's
        passages are not clustered and a determinantal draw only repels near-duplicates, so over 160
        moderately alike passages it is nearly uniform. It stays as an option for pools with real clusters.

  pick  --options FILE [--seed N]
        The writer writes its candidate next moves (an image, a turn in the scene, a line of dialogue), one a
        line, each ending in "p=0.xx", its own guess of how likely a reader expects it. The draw keeps the
        option whose surprisal -log p is nearest the entropy of the distribution: the typical set. The most
        expected option is a cliche, the least expected is noise; the typical one is surprising by the amount
        the situation allows. Without p= marks the order is read as a ranking and p is taken as 1/rank.
        --shelf: each option's commonest word pairing is looked up in phrase_df.json.gz (how many of the
        shelf's 19,516 literary passages use it; phrase_df.py build). An option whose pairing is in 20 or more
        is stock and is dropped before the draw (shook head 72, door open 148; a writer's own p is weakest on
        its cliches). The counts only veto: used as probabilities they handed the draw to the commonest pairing.

  spent --text FILE [--agent ID]
        The content words this text repeats more than a book on the shelf would: the agent's spent words, to
        be changed or cut before the page goes out. The rate a word may reach is set from the shelf's own
        passages (per-1000 counts of the word's commonest use in the pool), not guessed.

  page  --file FILE [--agent ID] [--no-walk]
        After a page is saved: refuses paper files (.tex .bib .sty .cls .bbl, where one object keeps one
        name), then runs `spent` on it and the dictionary's `word_walk.py page` (a separate tool,
        called when present) and prints both, short. One command for a hook to fire after a prose write.

  selftest
        Controls both ways: on four planted clusters the k-DPP draws one from each cluster far more often than
        a uniform draw; the memory moves the draw away from passages already shown; pick never returns the
        most expected or the least expected option of a skewed list; spent flags a planted repeat and not a
        function word.

Texts of the shelf are untrusted data: run this with python -I.
"""
import argparse
import gzip
import io
import json
import math
import os
import random
import re
import sys
import time
from collections import Counter

try:
    import numpy as np
except ImportError:  # the text checks (recurring, spent, returns) need no numpy; a hook run with python -s has none
    np = None

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:                               # python -P leaves the tool's own folder off the path,
    sys.path.insert(0, HERE)                           # and pick --shelf and selftest import phrase_df from it
WB = os.environ.get("WRITING_BRAIN_DIR", os.path.dirname(HERE))
INDEX = os.path.join(WB, "method", "passage_index.jsonl.gz")
MEMORY = os.path.join(HERE, "memory")
LOG = os.path.join(HERE, "draws.jsonl")
WING_FORMS = {"literature": ("novel", "story"), "script": ("play", "screenplay"), "academic": ("nonfiction", "exposition")}
FAME_CAP = 25
WORD = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)*")
STOP = set("""a an the of to in on for and or is are be been being it its that this these those with as at by from
not no nor do does did was were has have had will would shall should can could may might must i me my we us our you
your he him his she her they them their there here what which who whom whose how when where why if but then than so
too very just all any some each every one two into out up down over under again once only own same such more most
other off about above below after before because while until upon also yet said says say went go come came like
""".split())


# ---------------------------------------------------------------- k-DPP

def elementary_symmetric(lam, k):
    """E[l, n] = e_l(lam_1..lam_n) for l <= k, n <= N."""
    n = len(lam)
    E = np.zeros((k + 1, n + 1))
    E[0, :] = 1.0
    for l in range(1, k + 1):
        for m in range(1, n + 1):
            E[l, m] = E[l, m - 1] + lam[m - 1] * E[l - 1, m - 1]
    return E


def sample_kdpp(L, k, rng):
    """Exact draw of a k-subset with P(Y) proportional to det(L_Y)."""
    lam, V = np.linalg.eigh((L + L.T) / 2.0)
    lam = np.clip(lam, 0.0, None)
    N = len(lam)
    if np.count_nonzero(lam > 1e-12) < k:
        raise ValueError("kernel has rank below k")
    E = elementary_symmetric(lam, k)
    chosen, l = [], k
    for n in range(N, 0, -1):
        if l == 0:
            break
        if n == l or rng.random() < lam[n - 1] * E[l - 1, n - 1] / E[l, n]:
            chosen.append(n - 1)
            l -= 1
    B = V[:, chosen]                                   # N x k, orthonormal columns
    Y = []
    while B.shape[1] > 0:
        p = np.sum(B ** 2, axis=1)
        p = p / p.sum()
        i = int(rng.choices(range(N), weights=p.tolist())[0])
        Y.append(i)
        j = int(np.argmax(np.abs(B[i, :])))
        col = B[:, j].copy()
        B = np.delete(B, j, axis=1)
        if B.shape[1] == 0:
            break
        B = B - np.outer(col, B[i, :] / col[i])        # zero row i
        B, _ = np.linalg.qr(B)
    return sorted(Y)


# ---------------------------------------------------------------- text

def content_words(text):
    return [w.lower() for w in WORD.findall(text) if len(w) > 2 and w.lower() not in STOP]


def bow_matrix(texts):
    vocab = {}
    rows = []
    for t in texts:
        c = Counter(content_words(t))
        rows.append(c)
        for w in c:
            vocab.setdefault(w, len(vocab))
    df = Counter(w for c in rows for w in c)
    n = len(texts)
    X = np.zeros((n, len(vocab)))
    for i, c in enumerate(rows):
        for w, v in c.items():
            X[i, vocab[w]] = (1 + math.log(v)) * math.log((1 + n) / (1 + df[w]))
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return X / norms


FUNC = ("the a an and but or of in on at to with from by as that which who it he she they i you we "
        "not no never was is had have would could all then when while there here so if though").split()
SENT = re.compile(r"[^.!?]+[.!?]+")


def style_vector(text):
    """How a passage is written, not what it is about: sentence length and its spread, dialogue share,
    punctuation rates, word length, and the profile of function words."""
    words = WORD.findall(text)
    n = max(1, len(words))
    sents = [s for s in SENT.findall(text) if s.strip()] or [text]
    sl = np.array([len(WORD.findall(s)) for s in sents], dtype=float)
    low = [w.lower() for w in words]
    c = Counter(low)
    quoted = sum(len(WORD.findall(q)) for q in re.findall(r"[\"“]([^\"”]*)[\"”]", text))
    feats = [math.log1p(sl.mean()), (sl.std() / (sl.mean() + 1e-9)), quoted / n,
             text.count(",") / n, text.count(";") / n, (text.count("--") + text.count("—")) / n,
             text.count("?") / len(sents), text.count("!") / len(sents),
             np.mean([len(w) for w in words]) if words else 0.0,
             len(set(low)) / n]
    feats += [c[f] / n for f in FUNC]
    return np.array(feats)


def style_kernel(texts):
    X = np.vstack([style_vector(t) for t in texts])
    X = (X - X.mean(0)) / (X.std(0) + 1e-9)
    D2 = ((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)
    h2 = np.median(D2[np.triu_indices(len(texts), 1)])
    return np.exp(-D2 / h2)


def spread_draw(S, q, k, rng):
    """First passage drawn with weight q (the memory), each next one the passage least like any already
    drawn, its likeness raised by what the agent has already been shown. Measured 14 Nov on the shelf
    (20 seeds, description and dialogue): style likeness 0.09-0.13 against 0.36 for a plain draw, where
    the k-DPP at any bandwidth stayed at the plain draw's level (the passages are not clustered, and a
    determinantal draw only repels near-duplicates)."""
    n = len(q)
    first = int(rng.choices(range(n), weights=q.tolist())[0])
    sel = [first]
    while len(sel) < k:
        score = S[sel].max(0) + (1.0 - q)
        score[sel] = np.inf
        sel.append(int(np.argmin(score)))
    return sorted(sel)


def mean_pairwise(S, idx):
    idx = list(idx)
    vals = [S[a, b] for i, a in enumerate(idx) for b in idx[i + 1:]]
    return float(np.mean(vals)) if vals else 0.0


# ---------------------------------------------------------------- memory

def mem_path(agent):
    os.makedirs(MEMORY, exist_ok=True)
    return os.path.join(MEMORY, re.sub(r"[^A-Za-z0-9_.-]", "_", agent) + ".json")


def load_memory(agent):
    p = mem_path(agent)
    if os.path.exists(p):
        with io.open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"shown": {}}


def save_memory(agent, m):
    p = mem_path(agent)
    tmp = p + ".tmp"
    with io.open(tmp, "w", encoding="utf-8") as f:
        json.dump(m, f, ensure_ascii=False, indent=0)
    os.replace(tmp, p)


# ---------------------------------------------------------------- shelf

def load_index():
    with gzip.open(INDEX, "rt", encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def fetch_texts(rows):
    by_file = {}
    for r in rows:
        by_file.setdefault((r["shelf"], r["file"]), []).append(r)
    out = {}
    for (shelf, fn), rs in by_file.items():
        want = {int(r["line"]): r["id"] for r in rs}
        path = os.path.join(WB, *shelf.split("/"), fn)
        with io.open(path, "r", encoding="utf-8", errors="replace") as f:
            for ln, line in enumerate(f):
                if ln in want:
                    node = json.loads(line)
                    out[want[ln]] = node
    return out


def after_ok(r, after):
    """True when no year floor is set, or the passage is dated that year or later (undated ones fail)."""
    y = str(r.get("year") or "")
    return not after or (y.lstrip("-").isdigit() and int(y) >= after)


def author_death(author):
    """Death year of the first person named ("Scott, Walter, 1771-1832; ..." -> 1832), None when not given."""
    m = re.search(r"\b\d{3,4}\??-(\d{4})\b", author or "")
    return int(m.group(1)) if m else None


def written_after(node, after):
    """The shelf's year is often the edition's or the posting's (Scott 2005, Melville 2001): 99 of the 1,471
    passages a 1900 floor kept were by authors dead before 1900. A passage whose author died before the
    floor was written before it, whatever its year says."""
    d = author_death((node or {}).get("author"))
    return not after or d is None or d >= after


def bare(word):
    """lower case, possessive and punctuation off: doctor's -> doctor"""
    return re.sub(r"[^a-z]", "", re.sub(r"['’]s$", "", word.lower()))


def returns(text, word):
    """How many sentences of text use the word (same stem): 2 or more means the author comes back to it."""
    w0 = bare(word)
    s = stem(w0)
    forms = {w0, w0 + "s", w0 + "es"}                  # stem() keeps short plurals whole ("cups")
    return sum(1 for sent in re.split(r"(?<=[.!?])\s+", text)
               if any(w in forms or stem(w) == s for w in re.findall(r"[a-z]+", sent.lower())))


def cmd_refs(a):
    rng = random.Random(a.seed if a.seed is not None else time.time_ns())
    rows = load_index()
    forms = WING_FORMS[a.wing]
    pool = [r for r in rows if r["form"] in forms and (not a.role or r["role"] == a.role)
            and int(r.get("fame") or 0) <= FAME_CAP and after_ok(r, a.after)]
    about = getattr(a, "about", None)
    nodes = None
    if about or a.after:                               # read the whole wing once (about 4 s)
        nodes = fetch_texts(pool)
        pool = [r for r in pool if r["id"] in nodes and written_after(nodes[r["id"]], a.after)
                and (not about or returns(nodes[r["id"]].get("text", ""), about) >= 2)]
    if len(pool) < a.k:
        print("too few passages for wing %s role %s%s (%d)" % (a.wing, a.role, " about " + about if about else "", len(pool)))
        return 1
    pool = rng.sample(pool, min(a.pool, len(pool)))
    if nodes is None:
        nodes = fetch_texts(pool)
    pool = [r for r in pool if r["id"] in nodes and len(content_words(nodes[r["id"]].get("text", ""))) >= 40]
    texts = [nodes[r["id"]]["text"] for r in pool]
    X = bow_matrix(texts)
    W = X @ X.T                                        # what the passages are about
    St = style_kernel(texts)                           # how they are written
    S = 0.7 * St + 0.3 * W                             # both PSD, so the mix is a valid kernel
    mem = load_memory(a.agent)
    q = np.array([math.exp(-a.beta * mem["shown"].get(r["id"], 0)) for r in pool])
    if a.draw == "dpp":
        L = (q[:, None] * S * q[None, :]) + 1e-6 * np.eye(len(pool))
        Y = sample_kdpp(L, a.k, rng)
    else:
        Y = spread_draw(S, q, a.k, rng)
    U = rng.sample(range(len(pool)), a.k)
    how = ("each passage the least like the ones before it" if a.draw != "dpp" else
           "a DPP draw: like passages seldom come together, but any one draw can be close")
    print("CREATIVE DRAW  wing %s  kind %s  k=%d from a pool of %d (%s)" % (a.wing, a.role or "any", a.k, len(pool), how))
    if about:
        print("every passage comes back to '%s' in two or more sentences: read what each return does" % about)
    print("likeness of manner among the drawn: %.3f   (a plain random draw from the same pool: %.3f)\n"
          % (mean_pairwise(St, Y), mean_pairwise(St, U)))
    for n, i in enumerate(Y, 1):
        node = nodes[pool[i]["id"]]
        words = node["text"].split()
        cut = max(a.words, 260) if about else a.words  # the returns may sit past the usual cut
        print("--- %d. %s, %s (%s)" % (n, node.get("title") or "?", node.get("author") or "?", pool[i]["year"]))
        print(" ".join(words[:cut]) + (" ..." if len(words) > cut else ""))
        print()
        mem["shown"][pool[i]["id"]] = mem["shown"].get(pool[i]["id"], 0) + 1
    print("Read the three as three different answers to the same job. Then write yours so it is a fourth, not a copy of any.")
    save_memory(a.agent, mem)
    with io.open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "agent": a.agent, "wing": a.wing,
                            "role": a.role, "about": about, "drawn": [pool[i]["id"] for i in Y],
                            "style_likeness_drawn": round(mean_pairwise(St, Y), 4),
                            "style_likeness_uniform": round(mean_pairwise(St, U), 4)}) + "\n")
    return 0


# ---------------------------------------------------------------- pick

SHELF_STOCK = 20   # a pairing in 20+ of the ~19,500 literary passages is stock (shook head 72, heart beat 62)
P_MARK = re.compile(r"\bp\s*=\s*([0-9]*\.?[0-9]+)\s*$")


def typical_pick(options, probs, rng):
    p = np.array(probs, dtype=float)
    p = p / p.sum()
    s = -np.log(p)
    H = float(np.sum(p * s))
    d = np.abs(s - H)
    best = np.flatnonzero(d <= d.min() + 1e-12)
    i = int(rng.choice(list(best)))
    return i, H, s


def cmd_pick(a):
    rng = random.Random(a.seed if a.seed is not None else time.time_ns())
    with io.open(a.options, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    opts, probs = [], []
    for r, l in enumerate(lines, 1):
        m = P_MARK.search(l)
        if m:
            opts.append(l[: m.start()].strip())
            probs.append(float(m.group(1)))
        else:
            opts.append(l)
            probs.append(1.0 / r)
    if len(opts) < 3:
        print("write at least three options")
        return 1
    if a.shelf:
        # the shelf's count for each option's commonest word pairing replaces the writer's own guess, which is
        # weakest exactly on its cliches (the move it has read most feels natural, not stale)
        import phrase_df
        scored = [phrase_df.shelf_score(o) for o in opts]
        N = phrase_df.table()["passages"]
        med = sorted(probs)[len(probs) // 2]
        for o, pr, (ps, pair, k) in zip(opts, probs, scored):
            note = ""
            if k >= SHELF_STOCK and pr <= med:
                note = "  <- you rated it unexpected; the shelf has it %d times" % k
            print("  shelf: %-22s in %4d of %d passages%s | %s" % (repr(pair), k, N, note, o[:70]))
        # The counts are not a distribution over these moves (normalised, they hand the draw to the commonest
        # pairing: tried 14 Nov, it picked "heart beat ... door opened"). So the shelf only vetoes stock options
        # and the writer's own p= chooses among the rest.
        keep = [j for j, (_, _, k) in enumerate(scored) if k < SHELF_STOCK]
        if len(keep) >= 2 and len(keep) < len(opts):
            print("  dropped as stock: %d of %d options" % (len(opts) - len(keep), len(opts)))
            opts, probs = [opts[j] for j in keep], [probs[j] for j in keep]
    i, H, s = typical_pick(opts, probs, rng)
    print("entropy of your options: %.2f nats. The most expected (surprisal %.2f) is the cliche; the least "
          "expected (%.2f) is noise." % (H, s.min(), s.max()))
    print("TYPICAL PICK (surprisal %.2f, nearest the entropy): %s" % (s[i], opts[i]))
    return 0


# ---------------------------------------------------------------- spent

def cmd_spent(a, text=None):
    if text is None:
        with io.open(a.text, "r", encoding="utf-8") as f:
            text = f.read()
    words = content_words(text)
    n = len(words)
    if n < 80:
        print("too short to judge (%d content words)" % n)
        return 1
    c = Counter(words)
    limit = max(3, a.per_1000 * n / 1000.0)
    spent = [(w, v) for w, v in c.most_common() if v >= limit]
    if not spent:
        print("no spent words (none above %.1f uses in %d content words)" % (limit, n))
    else:
        print("SPENT WORDS (%d content words; above %.1f uses is more than a page of the shelf carries):" % (n, limit))
        for w, v in spent:
            print("  %-18s %d" % (w, v))
        print("Change or cut the repeats that are not the same thing named twice on purpose.")
    return spent


# ---------------------------------------------------------------- recurring business
# The same objects and gestures coming back paragraph after paragraph. On the 24 pages of the 14 Nov blind test
# (WBAB2, two judges) the share of content stems found in three or more paragraphs tracked a worse rank:
# Spearman +0.46, positive in all three tasks, permutation p 0.015; the judges' words for it were "physical
# business repeated without a new consequence". Control pages averaged 3.3 per 100 content words, brain pages 4.4.

RECUR_FLAG = 4.0
# Dialogue tags return by nature; they still count in the rate (as tested) but are not shown as business.
SPEECH_TAGS = {"said", "asked", "replied", "answered", "told", "says", "asks", "replies", "answers", "tells"}


def stem(w):
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[: -len(suf)]
    return w


def names(text):
    """Words capitalised at every occurrence and at least once mid-sentence: character and place names.
    A name that returns is the subject, not business; on the WBAB2 pages leaving names out kept rho at +0.46."""
    caps, low, mid = Counter(), Counter(), Counter()
    for m in re.finditer(r"[A-Za-z][A-Za-z'\-]+", text):
        w = m.group(0)
        if w[0].isupper():
            caps[w.lower()] += 1
            if m.start() > 0 and not re.search(r"[.!?\"“\n]\s*$", text[max(0, m.start() - 3):m.start()]):
                mid[w.lower()] += 1
        else:
            low[w.lower()] += 1
    return {w for w in caps if low[w] == 0 and mid[w] > 0}


def recurring(text, where=False):
    """(rate per 100 content words, [(word, paragraphs it is in), ...]) for stems found in 3+ paragraphs, names left out.
    With where=True a third value maps each listed word to the paragraph numbers (from 1) it is in."""
    ps = [p for p in re.split(r"\n\s*\n", text.lstrip("﻿")) if p.strip() and not p.lstrip().startswith("#")]
    per, surface, n = [], {}, 0
    for p in ps:
        ws = content_words(p)
        n += len(ws)
        st = set()
        for w in ws:
            s = stem(w)
            surface.setdefault(s, Counter())[w] += 1
            st.add(s)
        per.append(st)
    c = Counter(s for st in per for s in st)
    nm = names(text)
    hits = sorted(((surface[s].most_common(1)[0][0], k) for s, k in c.items() if k >= 3), key=lambda x: (-x[1], x[0]))
    hits = [h for h in hits if h[0] not in nm]
    rate = len(hits) * 100.0 / max(1, n)
    if not where:
        return rate, hits
    at = {w: [i + 1 for i, st in enumerate(per) if stem(w) in st] for w, k in hits}
    return rate, hits, at


def returns_in_place(text, word, win=4, most=6):
    """[(paragraph number from 1, the words around the word's first use in that paragraph)] for each paragraph
    that uses it, so the writer can see whether each return does something new or the same gesture again."""
    ps = [p for p in re.split(r"\n\s*\n", text.lstrip("﻿")) if p.strip() and not p.lstrip().startswith("#")]
    s = stem(re.sub(r"[^a-z]", "", word.lower()))      # quotes and dashes off, as the tokens below
    out = []
    for i, p in enumerate(ps, 1):
        toks = p.split()
        for j, t in enumerate(toks):
            if stem(re.sub(r"[^a-z]", "", t.lower())) == s:
                out.append((i, " ".join(toks[max(0, j - win): j + win + 1])))
                break
        if len(out) >= most:
            break
    return out


def print_recurring(text):
    rate, hits, at = recurring(text, where=True)
    if not hits:
        return rate
    head = ("RECURRING BUSINESS: %.1f per 100 content words come back in 3+ paragraphs" % rate)
    if rate > RECUR_FLAG:
        head += " (above %.1f: judges marked pages like this down)" % RECUR_FLAG
    print(head + " (word: the paragraphs it is in, counting from 1):")
    for w, k in hits[:15]:
        print("  %s: %s" % (w, ", ".join(str(i) for i in at[w])))
    print("What happens at each return of the top three (paragraph: the words around it):")
    shown = [h for h in hits if h[0] not in SPEECH_TAGS] or hits
    for w, k in shown[:3]:
        for pi, snip in returns_in_place(text, w):
            print("  %s  %d: ...%s..." % (w, pi, snip))
    print("Each return should change something (a new consequence, a turn); a gesture repeated for texture reads as repetition.")
    print("To see how books come back to an object: creative_draw.py refs --about %s --agent <your id>" % bare(shown[0][0]))
    return rate


# ---------------------------------------------------------------- page

PAPER_EXT = (".tex", ".bib", ".sty", ".cls", ".bbl")
WORD_WALK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dictionary", "word_walk.py")


def cmd_page(a):
    if a.file.lower().endswith(PAPER_EXT):
        print("not for papers: in a paper one object keeps one name (the paper lint); nothing checked")
        return 2
    if not os.path.isfile(a.file):
        print("no such file: %s; nothing checked" % a.file)
        return 2
    with io.open(a.file, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    res = cmd_spent(a, text=text)
    print_recurring(text)
    try:
        import abstract_close
        for ln in abstract_close.report(text):
            print(ln)
    except Exception as e:  # the noun cache or WordNet missing: the rest of the page check still runs
        print("abstract_close skipped: %s" % e)
    if a.no_walk or not os.path.exists(WORD_WALK):
        return 0
    import subprocess
    try:
        out = subprocess.run([sys.executable, "-I", "-X", "utf8", WORD_WALK, "page", a.file],
                             capture_output=True, text=True, encoding="utf-8", errors="replace",
                             timeout=a.timeout)
        lines = (out.stdout or "").strip().splitlines()
        if lines:
            print("WORD WALK (dictionary/word_walk.py page):")
            for ln in lines[:a.walk_lines]:
                print("  " + ln)
            if len(lines) > a.walk_lines:
                print("  ... %d more lines: run word_walk.py page yourself" % (len(lines) - a.walk_lines))
        elif out.returncode:
            print("word_walk.py page exited %d: %s" % (out.returncode, (out.stderr or "").strip()[-200:]))
    except subprocess.TimeoutExpired:
        print("word_walk.py page took over %ds; skipped" % a.timeout)
    return 0


# ---------------------------------------------------------------- selftest

def cmd_selftest(a):
    rng = random.Random(7)
    ok = True

    def check(name, cond):
        nonlocal ok
        ok = ok and cond
        print(("PASS " if cond else "FAIL ") + name)

    # four planted clusters of 10, points near four orthogonal directions
    nprng = np.random.default_rng(7)
    C = np.eye(4)
    pts = np.vstack([C[c] + 0.15 * nprng.standard_normal(4) for c in range(4) for _ in range(10)])
    pts /= np.linalg.norm(pts, axis=1, keepdims=True)
    S = pts @ pts.T
    L = S + 1e-6 * np.eye(40)
    cover_dpp = cover_uni = 0
    T = 400
    for _ in range(T):
        Y = sample_kdpp(L, 4, rng)
        cover_dpp += len({y // 10 for y in Y}) == 4
        U = rng.sample(range(40), 4)
        cover_uni += len({u // 10 for u in U}) == 4
    check("k-DPP draws all four clusters far more often than a uniform draw (%d vs %d of %d)"
          % (cover_dpp, cover_uni, T), cover_dpp > 0.6 * T and cover_uni < 0.3 * T)

    # exactness: on a random 6x6 kernel the draw frequencies match det(L_Y) / e_k(lambda)
    from itertools import combinations
    A = nprng.standard_normal((6, 4))
    L6 = A @ A.T + 0.05 * np.eye(6)
    subsets = list(combinations(range(6), 2))
    dets = np.array([np.linalg.det(L6[np.ix_(Y, Y)]) for Y in subsets])
    target = dets / dets.sum()
    M = 20000
    freq = Counter(tuple(sample_kdpp(L6, 2, rng)) for _ in range(M))
    emp = np.array([freq.get(Y, 0) / M for Y in subsets])
    tv = 0.5 * np.abs(emp - target).sum()
    check("the draw is exact: total variation to det(L_Y)/e_k is %.4f on %d draws" % (tv, M), tv < 0.02)

    # memory: weight the first cluster down; draws should leave it
    q = np.array([math.exp(-3.0 * 4)] * 10 + [1.0] * 30)
    Lq = q[:, None] * S * q[None, :] + 1e-9 * np.eye(40)
    hits = sum(any(y < 10 for y in sample_kdpp(Lq, 3, rng)) for _ in range(T))
    check("the memory moves the draw off passages already shown (cluster 1 drawn %d of %d)" % (hits, T), hits < 0.05 * T)

    opts = ["obvious", "expected", "fresh", "odd", "wild"]
    probs = [0.6, 0.2, 0.1, 0.07, 0.03]
    picks = Counter(typical_pick(opts, probs, rng)[0] for _ in range(50))
    check("pick never returns the most or the least expected option (%s)" % dict(picks),
          0 not in picks and 4 not in picks)

    planted = ("The lantern swung. " + "Grey light fell on the stair and on the door. " * 2 +
               " ".join(a + b + c for a in "bcdfg" for b in "aeiou" for c in "lmnprst") + " lantern lantern lantern lantern lantern")
    res = cmd_spent(argparse.Namespace(per_1000=8.0), text=planted)
    flagged = {w for w, _ in (res if isinstance(res, list) else [])}
    check("spent flags the planted repeat and no function word", "lantern" in flagged and "the" not in flagged)

    refused = [cmd_page(argparse.Namespace(file="paper" + ext)) for ext in PAPER_EXT + (".TEX",)]
    check("page refuses every paper file without opening it (%s)" % refused, all(r == 2 for r in refused))

    rows_y = [{"year": y} for y in ("1899", "1900", "1922", "", None, "c.1910", "-50")]
    kept = [r["year"] for r in rows_y if after_ok(r, 1900)]
    check("--after 1900 keeps 1900 and 1922, drops older, undated and odd years (%s)" % kept, kept == ["1900", "1922"])
    check("--after 0 keeps every passage", all(after_ok(r, 0) for r in rows_y))
    check("author_death reads the first person's dates",
          author_death("Ainsworth, William Harrison, 1805-1882; Gilbert, John, 1817-1897 [Illustrator]") == 1882
          and author_death("Gogol, Nikolai, 1809?-1852") == 1852 and author_death("Anonymous") is None)
    check("--after 1900 drops a 2005 posting of Scott, keeps Tolstoy (d. 1910) and an undated author",
          not written_after({"author": "Scott, Walter, 1771-1832"}, 1900)
          and written_after({"author": "Tolstoy, Leo, graf, 1828-1910"}, 1900) and written_after({}, 1900))
    busy = "\n\n".join("She set down the teacup by the window. %s" % s for s in
                       ("Rain fell on the yard.", "The clock struck nine.", "Her brother laughed at nothing.",
                        "A dog barked twice outside."))
    rate, hits = recurring(busy)
    words = [w for w, k in hits]
    check("recurring flags a cup set down in every paragraph", "teacup" in words and dict(hits)["teacup"] == 4)
    calm = "\n\n".join(("Rain fell on the yard.", "The clock struck nine.", "Her brother laughed at nothing.",
                        "A dog barked twice outside."))
    check("recurring is silent when no word returns", recurring(calm)[1] == [])
    check("recurring ignores a heading line", recurring("# teacup\n\nteacup one\n\nteacup two")[1] == [])
    named = "\n\n".join("Then Mara set down the teacup. %s" % s for s in ("Rain fell.", "The clock struck.", "A dog barked."))
    nw = [w for w, k in recurring(named)[1]]
    check("recurring leaves out a name but keeps the cup", "mara" not in nw and "teacup" in nw)
    check("recurring says which paragraphs the cup is in", recurring(busy, where=True)[2].get("teacup") == [1, 2, 3, 4])
    check("--about counts sentences that come back to the word, plural included",
          returns("He lifted the cup. Rain fell. The cups were cold. No word.", "cup") == 2
          and returns("A cupboard stood there. Rain.", "cup") == 0
          and returns("The doctor came. The doctor's bicycle fell.", "doctor's") == 2)
    rip = returns_in_place(busy, "teacup")
    check("page shows each return of the cup in place (%d, %s)" % (len(rip), rip[:1]),
          [i for i, _ in rip] == [1, 2, 3, 4] and all("teacup" in snip for _, snip in rip))
    # pick --shelf on a planted table: the stock option the writer rated unexpected is dropped, never picked
    import contextlib
    import tempfile
    import phrase_df
    saved = phrase_df._TABLE
    phrase_df._TABLE = {"passages": 1000, "df": {"heart beat": 300, "shook head": 200}}
    fd, opt_path = tempfile.mkstemp(suffix=".txt")
    os.close(fd)
    with io.open(opt_path, "w", encoding="utf-8") as f:
        # without --shelf these four pick a stock line on 8 of 10 seeds (checked 14 Nov), so the check is two-sided
        f.write("He shook his head. p=0.3\nHer heart beat fast. p=0.3\nThe dog brought the wrong shoe. p=0.3\n"
                "She salted the snow on the sill. p=0.1\n")
    outs = []
    for seed in range(10):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            cmd_pick(argparse.Namespace(options=opt_path, seed=seed, shelf=True))
        outs.append(buf.getvalue())
    phrase_df._TABLE = saved
    os.remove(opt_path)
    picks = [o.split("TYPICAL PICK", 1)[-1] for o in outs]
    check("pick --shelf never picks a stock pairing (10 seeds)", all("heart" not in x and "shook" not in x for x in picks))
    check("pick --shelf names the stock option rated unexpected", all("you rated it unexpected" in o for o in outs))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("refs")
    r.add_argument("--wing", default="literature", choices=sorted(WING_FORMS))
    r.add_argument("--role", default=None)
    r.add_argument("--k", type=int, default=3)
    r.add_argument("--agent", required=True)
    r.add_argument("--pool", type=int, default=160)
    r.add_argument("--beta", type=float, default=1.5)
    r.add_argument("--draw", default="spread", choices=("spread", "dpp"))
    r.add_argument("--words", type=int, default=140)
    r.add_argument("--seed", type=int, default=None)
    r.add_argument("--after", type=int, default=0, help="only passages from this year on (undated ones are left out)")
    r.add_argument("--about", default=None, help="only passages that come back to this word in 2+ sentences")
    p = sub.add_parser("pick")
    p.add_argument("--options", required=True)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--shelf", action="store_true",
                   help="use how often the shelf already pairs each option's words (phrase_df.py) instead of your p=")
    s = sub.add_parser("spent")
    s.add_argument("--text", required=True)
    s.add_argument("--agent", default=None)
    s.add_argument("--per-1000", dest="per_1000", type=float, default=8.0)
    g = sub.add_parser("page")
    g.add_argument("--file", required=True)
    g.add_argument("--agent", default=None)
    g.add_argument("--per-1000", dest="per_1000", type=float, default=8.0)
    g.add_argument("--no-walk", dest="no_walk", action="store_true")
    g.add_argument("--timeout", type=int, default=60)
    g.add_argument("--walk-lines", dest="walk_lines", type=int, default=25)
    sub.add_parser("selftest")
    a = ap.parse_args()
    if a.cmd == "page":
        return cmd_page(a)
    if a.cmd == "refs":
        return cmd_refs(a)
    if a.cmd == "pick":
        return cmd_pick(a)
    if a.cmd == "spent":
        res = cmd_spent(a)
        return 1 if res == 1 else 0
    return cmd_selftest(a)


if __name__ == "__main__":
    sys.exit(main())
