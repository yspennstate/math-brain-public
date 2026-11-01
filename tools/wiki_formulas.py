"""A Wikipedia lead with its formulas kept, for the harvester.

The REST summary's `extract` is plain text: every formula is dropped and the gap closed ("states that if is a
continuous function"). The MediaWiki parse API (action=parse, section=0) keeps each formula's TeX in its fallback
image's alt text. This module rebuilds the lead paragraph by paragraph with each inline formula as $TeX$ and each
display formula (a <dl><dd> block, or a paragraph holding only math) appended to the paragraph before it as $$TeX$$,
and returns the paragraph prefix that best matches a given plain-text extract.

Guards, each from a defect found on 2026-09-23 while repairing harvested cards:
  - only reference-class <sup> elements are footnotes; a plain <sup>/<sub> is mathematics (a<sup>2</sup> -> a^{2});
  - <style>/<script> contents are dropped (a TemplateStyles box leaked CSS into the text);
  - a first paragraph of fewer than four prose words is not the lead (a stray "<formula> since <formula>" paragraph);
  - a trailing TeX space must not leave a lone backslash escaping the closing dollar;
  - formula_lead() refuses a text that drops a word of the extract or puts a formula ahead of the first stretch that
    matches the extract.
Standard library only; no local paths."""
import collections
import difflib
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://en.wikipedia.org/w/api.php"
UA = "math-brain-population/1.0 (local research corpus; polite rate with backoff)"
MATH_SPAN = re.compile(r'<span[^>]*class="[^"]*mwe-math-element[^"]*"[^>]*>', re.S)
ALT_IMG = re.compile(r'<img[^>]*\balt="([^"]*)"[^>]*class="[^"]*mwe-math-fallback[^"]*"|'
                     r'<img[^>]*class="[^"]*mwe-math-fallback[^"]*"[^>]*\balt="([^"]*)"', re.S)
ALTTEXT = re.compile(r'<math\b[^>]*\balttext="([^"]*)"', re.S)
REF_SUP = re.compile(r'<sup\b[^>]*class="[^"]*(?:reference|noprint|Inline-Template)[^"]*"[^>]*>.*?</sup>', re.S)
BLOCK = re.compile(r"<p\b[^>]*>(.*?)</p>|<dl\b[^>]*>(.*?)</dl>", re.S)
TOK = re.compile(r"\$\$.*?\$\$|\$[^$]*\$|[A-Za-z0-9]+", re.S)


def tex(s):
    t = html.unescape(s).strip()
    t = re.sub(r"^\{\\displaystyle\s*(.*)\}$", r"\1", t, flags=re.S).strip()
    t = re.sub(r"\s+", " ", t)
    return re.sub(r"(?<!\\)\\$", "", t).rstrip()


def split_math(par):
    """Replace each math element in a paragraph's HTML by a marker carrying its TeX; None if a formula has no TeX."""
    out, pos, n = [], 0, 0
    for m in MATH_SPAN.finditer(par):
        if m.start() < pos:
            continue
        img = re.search(r"<img[^>]*mwe-math-fallback[^>]*>", par[m.end():], re.S)
        if not img:
            return None, 0
        seg = par[m.start(): m.end() + img.end()]
        close = par.find("</span>", m.end() + img.end())
        end = close + len("</span>") if close >= 0 else m.end() + img.end()
        a = ALT_IMG.search(seg) or ALTTEXT.search(seg)
        if not a:
            return None, 0
        out.append(par[pos:m.start()])
        out.append("\x00%s\x01" % tex(next(g for g in a.groups() if g is not None)))
        pos = end
        n += 1
    out.append(par[pos:])
    return "".join(out), n


def clean(s, as_tex=False):
    s = REF_SUP.sub("", s)
    s = re.sub(r"<(style|script)\b[^>]*>.*?</\1\s*>", "", s, flags=re.S | re.I)
    if as_tex:
        s = re.sub(r"<sup\b[^>]*>(.*?)</sup>", lambda m: "^{%s}" % re.sub(r"<[^>]+>", "", m.group(1)), s, flags=re.S)
        s = re.sub(r"<sub\b[^>]*>(.*?)</sub>", lambda m: "_{%s}" % re.sub(r"<[^>]+>", "", m.group(1)), s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace("⁠", "")
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r"\s+([,.;:)])", r"\1", s)


def words(s):
    return re.findall(r"[a-z0-9]+", s.lower())


def flat(s):
    """TeX flattened the way a plain-text extract flattens a formula: a^{2} -> a2."""
    return re.sub(r"[\^_{}\\$]", "", s)


def overlap(a, b):
    ca, cb = collections.Counter(words(a)), collections.Counter(words(b))
    if not ca or not cb:
        return 0.0
    return sum((ca & cb).values()) / max(sum(ca.values()), sum(cb.values()))


def fetch_lead(title, timeout=30, retries=3):
    """(lead HTML, revision id) through the parse API; prop names revid, or the API returns none. A 429 waits for
    Retry-After (capped at two minutes) and tries again, as the harvester's own summary fetch does."""
    q = {"action": "parse", "page": title, "prop": "text|revid", "section": "0", "format": "json", "formatversion": "2",
         "redirects": "1", "disablelimitreport": "1", "disableeditsection": "1"}
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(q), headers={"User-Agent": UA})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = json.loads(r.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == retries:
                raise
            try:
                wait = float(exc.headers.get("Retry-After", "30"))
            except (TypeError, ValueError):
                wait = 30.0
            time.sleep(min(wait, 120.0) + 2.0)
    if "error" in d:
        raise ValueError(d["error"].get("info", "api error"))
    return d["parse"]["text"], d["parse"].get("revid")


def best_prefix(stored, page_html):
    """The paragraph prefix of the lead whose formula-free text best matches `stored`: its overlap, its text with
    formulas, and how many formulas it holds."""
    best = None
    acc_with, acc_without, nforms = [], [], []
    for m in BLOCK.finditer(page_html):
        if m.group(1) is not None:
            par = m.group(1)
            if not clean(re.sub(r"<span[^>]*mwe-math-element.*?</span>", "", par, flags=re.S)):
                marked, n = split_math(par)
                if acc_with and marked is not None and n > 0 and not clean(re.sub("\x00(.*?)\x01", " ", marked)).strip(" .,;:"):
                    acc_with[-1] += " " + " ".join("$$%s$$" % t for t in re.findall("\x00(.*?)\x01", marked))
                    nforms[-1] += n
                continue
            if len(acc_with) >= 8:
                break
            marked, n = split_math(par)
            if marked is None:
                return {"verdict": "FAILED", "why": "a formula without TeX"}
            if not acc_with and len(words(clean(re.sub("\x00(.*?)\x01", " ", marked)))) < 4:
                continue
            acc_with.append(clean(re.sub("\x00(.*?)\x01", lambda mm: " $%s$ " % mm.group(1), marked), as_tex=True))
            acc_without.append(clean(re.sub("\x00(.*?)\x01", " ", marked)))
            nforms.append(n)
            ov = overlap(" ".join(acc_without), stored)
            if best is None or ov > best[0]:
                best = (ov, len(acc_with))
        elif acc_with:
            marked, n = split_math(m.group(2))
            if marked is None or n == 0 or clean(re.sub("\x00(.*?)\x01", " ", marked)).strip(" .,;:"):
                continue
            acc_with[-1] += " " + " ".join("$$%s$$" % t for t in re.findall("\x00(.*?)\x01", marked))
            nforms[-1] += n
    if not best:
        return {"verdict": "FAILED", "why": "no paragraphs"}
    ov, k = best
    return {"overlap": ov, "text": " ".join(acc_with[:k]), "formulas": sum(nforms[:k]), "paragraphs": k}


def leading_formulas(stored, current):
    """Formulas that come before the first stretch (three words or more) of `current` that matches `stored`."""
    stream = [("F", t) if t.startswith("$") else ("W", t.lower()) for t in TOK.findall(current)]
    widx = [i for i, (k, _) in enumerate(stream) if k == "W"]
    sm = difflib.SequenceMatcher(a=words(stored), b=[stream[i][1] for i in widx], autojunk=False)
    blocks = [b for b in sm.get_matching_blocks() if b[2] >= 3]
    if not blocks:
        return []
    return [t for k, t in stream[:widx[blocks[0][1]]] if k == "F"]


def tex_ok(text):
    """Balanced dollars, no escaped closing dollar, balanced braces inside each formula."""
    if re.search(r"(?<!\\)\\\$", text) or text.replace("$$", "").count("$") % 2 or text.count("$$") % 2:
        return False
    return all((f[0] or f[1]).count("{") == (f[0] or f[1]).count("}")
               for f in re.findall(r"\$\$(.*?)\$\$|\$([^$]*)\$", text))


def formula_lead(title, extract, min_overlap=0.85):
    """The lead text with formulas for a harvested `extract`, or None with a reason. Returns (text, revid, why)."""
    try:
        page, rev = fetch_lead(title)
    except Exception as e:  # noqa: BLE001
        return None, None, "fetch failed: %s" % str(e)[:80]
    b = best_prefix(extract, page)
    if b.get("verdict") == "FAILED":
        return None, rev, b["why"]
    if b["formulas"] == 0:
        return None, rev, "no formula in the matching lead"
    if b["overlap"] < min_overlap:
        return None, rev, "lead moved since the extract (overlap %.2f)" % b["overlap"]
    text = b["text"]
    have = set(words(text)) | set(words(flat(text)))
    dropped = sorted(w for w in set(words(extract)) if w not in have)
    if dropped:
        return None, rev, "would drop words of the extract: %s" % dropped[:6]
    if leading_formulas(extract, text):
        return None, rev, "a formula ahead of the matching text"
    if not tex_ok(text):
        return None, rev, "TeX check failed"
    return text, rev, "%d formulas kept, overlap %.2f" % (b["formulas"], b["overlap"])
