#!/usr/bin/env python3
"""voice_guard_hook.py - PreToolUse gate for public-facing prose (owner order 2026-09-09).

The owner, 2026-06-10: papers, READMEs, repos and anything published must read as if a human
wrote it - "headline" is an instant tell, no bold-fests, no emoji, state a correction once,
never write a note about sounding human. On 2026-09-09, on his personal website, he added a
second family: self-introspection about the artifact itself ("Every paper on this site will
get...", "the cards below track...", "click Abstract to read...") - prose that narrates the
page instead of saying the thing. Written at the author's request..

The voice_human reflex already existed but was ranked behind other reflexes and capped out
of the fire list on the very session that produced the tells. A rule that must always hold
is a spec for machinery (the ps1_guard precedent), so this hook reads the prose an Edit or
Write is about to put into a prose file and REFUSES the write when it carries a tell, naming
the tell and the line. The agent fixes the sentence and writes again. Nothing is blocked in
code, data, logs or private notes: only prose files (.html .md .tex .txt .rst .bib .markdown
and README-like names), and never paths under the brain's own memory/dreaming/audit trees,
where the notes are for us and quote the user's words verbatim.

Since 2026-11-11 (his 06:29 words on a grant deck: "i don't like the self introspection (referring
directly to the flyer for example)") the hook also reads deck BUILDERS - a .py that writes a
.pptx, wherever it lives - and refuses slide text that points at the deck itself or at the
paperwork behind it (the flyer, the form, "this deck", "this slide", a slide number). A finished
file is checked with:  python voice_guard_hook.py --pptx FILE [FILE ...]  (exit 1 on a hit).

Bypass: put the token  voice-ok  anywhere in the file (an HTML comment, a LaTeX comment)
for a file that legitimately quotes a tell (this hook's own docs, the brain memory).

Fail-open by construction: any internal error -> exit 0, no output. Cost: one regex pass
over the new text. Selftest: python voice_guard_hook.py --selftest
"""
import json
import os
import re
import sys

PROSE_EXT = (".html", ".htm", ".md", ".markdown", ".tex", ".txt", ".rst", ".bib")
SKIP_DIRS = (
    "\\.claude\\", "/.claude/", "\\.codex\\", "/.codex/",
    "brain-repo", "\\audits\\", "/audits/",
    "\\scratchpad\\", "/scratchpad/", "\\Temp\\", "/Temp/", "node_modules",
)

# Hard tells: the words he has named, plus the AI register he keeps pointing at.
WORD_TELLS = [
    r"\bheadline\b", r"\bdelve\b", r"\bdelves\b", r"\bremarkabl[ey]\b", r"\bstrikingly\b",
    r"\bnotably\b", r"\bcrucially\b", r"\bcomprehensive\b", r"\bgame-changing\b",
    r"\bcutting-edge\b", r"\bseamless(?:ly)?\b", r"\brobust and scalable\b",
    r"\bit'?s worth noting\b", r"\bin today'?s\b", r"\bunlock(?:s|ing)?\b", r"\btestament to\b",
    r"\bat its core\b", r"\bin the realm of\b", r"\bnavigat(?:e|ing) the\b", r"\ba tapestry\b",
    r"\bsound(?:s|ing)? human\b", r"\bhuman-sounding\b", r"\bnot (?:like )?an? AI\b",
]
# Self-introspection: prose that narrates the artifact instead of saying the thing.
META_TELLS = [
    r"\bevery (?:paper|page|section|card|entry|item|video|post) (?:on|in|of) this (?:site|page|list|section)\b",
    r"\b(?:the )?cards? below (?:track|show|list|say)s?\b",
    r"\bclick (?:on )?[\"'“]?(?:abstract|summary|here|the button)\b",
    r"\bthis (?:page|site|section) (?:collects|contains|lists|tracks|shows|describes|is a)\b",
    r"\bbelow (?:you will|you'll) find\b",
    r"\b(?:cards?|entries|items) without an? \w+ (?:yet )?say so\b",
    r"\bwhen (?:a|the) \w+ is (?:recorded|added|ready),? the card becomes\b",
    r"\bin this (?:section|page),? (?:we|I) (?:will )?(?:describe|discuss|present|explain)\b",
]
# A paper never narrates its own history (owner, 2026-09-15, "for the love of god").
# It states mathematics and attributions; a correction to a citation is silent, the corrected
# citation simply appears. The AI declaration is the ONE place the process may be named, so
# "prepared the first draft of this manuscript" stays legal - see the selftest's negative control.
PAPER_TELLS = [
    r"\bthe first version of (?:this|the present) (?:paper|manuscript|note|article)\b",
    r"\b(?:an|the) (?:earlier|previous|original) (?:record|draft|version) of (?:this|the present)\b",
    r"\bin (?:an|the) (?:earlier|previous) draft\b",
    r"\bwas corrected when\b",
    r"\bwe found no (?:later|other|subsequent)\b",
    r"\bre-?derived line by line\b",
    r"\bthe reviews? found\b",
    r"\breferee agents?\b",
    r"\b(?:verified|checked|re-?derived|confirmed|corrected)[^.]{0,60}before inclusion\b",
    r"\bwas obtained afterwards\b",
    r"\bthis (?:paper|manuscript) originally\b",
]
# A deck, a slide or a one-pager never points at itself or at the paperwork behind it (owner,
# 2026-11-11 06:29, on a grant deck whose slides said "the three questions on the flyer, answered",
# "as on the form", "written for this deck"): "i don't like the self introspection (referring
# directly to the flyer for example) ... it does not sound that human to refer to a flyer, just
# have the slides without referring to it". Say what the grant is and what the work is; never
# cite the flyer, the form, the deck or a slide number from inside the deck.
DECK_SELF_TELLS = [
    r"\b(?:on|in|for|of|from|to) this (?:deck|slide|presentation|pitch)\b",
    r"\bthis (?:deck|slide) (?:shows|says|lists|describes|is|was|gives|covers|answers)\b",
    r"\b(?:written|drawn|made|built|prepared|created) for (?:this|the) (?:deck|slide|talk|presentation|meeting)\b",
    r"\banywhere in the deck\b",
    r"\b(?:unless|as|what) the slide says\b",
    r"\b(?:shown|described|listed|explained|answered) on (?:the )?(?:next |previous |following )?slides?\b",
    r"\b(?:on|see|in) slides? \d+\b",
    r"\bin one slide\b",
    r"\bthe (?:next|previous|following|earlier) slide\b",
]
DECK_PAPERWORK_TELLS = [
    r"\bflyer(?:'s)?\b",
    r"\bas on the (?:form|application)\b",
    r"\bon the (?:application )?form\b",
    r"\bas (?:its|the|their) (?:call|form|website|brochure) (?:describes|says|asks|states|puts)\b",
    r"\b(?:application )?form,? \(?(?:field )?F\d+\)?",
    r"\bone-page (?:pitch|proposal)\b",
    r"\brestates the\b",
    r"\bas discussed for this meeting\b",
    r"\bas (?:submitted|sent|written) (?:on|in) the (?:form|application|proposal)\b",
]
DECK_NAME = re.compile(r"(?:deck|slide|pitch|beamer|one_?pager)", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\u2705\u274C\u2714\u2716\u2728\u2B06\u2B07]")


def _is_prose(path):
    p = path.replace("/", "\\")
    low = p.lower()
    if any(s.lower() in low for s in SKIP_DIRS):
        return False
    base = os.path.basename(low)
    if base.startswith("readme"):
        return True
    return low.endswith(PROSE_EXT)


def _strip_code(text, path):
    """Drop script/style/pre blocks and HTML comments so code inside a page is not judged."""
    if path.lower().endswith((".html", ".htm")):
        text = re.sub(r"<script\b.*?</script>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<style\b.*?</style>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<pre\b.*?</pre>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    if path.lower().endswith((".md", ".markdown")):
        text = re.sub(r"```.*?```", " ", text, flags=re.S)
    return text


def _is_deck_text(path, text):
    """A prose file that is a deck: named like one, or beamer frames inside."""
    return bool(DECK_NAME.search(os.path.basename(path or ""))) or "\\begin{frame}" in (text or "")


def _is_deck_builder(path, text):
    """A Python file that writes slides (python-pptx). These live anywhere, the scratchpad included,
    so SKIP_DIRS does not apply; the brain's own hook and memory trees stay out."""
    low = (path or "").replace("/", "\\").lower()
    if not low.endswith(".py"):
        return False
    if "\\.claude\\" in low or "\\.codex\\" in low or "brain-repo" in low:
        return False
    if "pptx" in (text or "") or DECK_NAME.search(os.path.basename(low)):
        return True
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                return "pptx" in fh.read(200000)
    except Exception:
        pass
    return False


_STR = re.compile(r'"(?:[^"\\\n]|\\.)*"' + "|" + r"'(?:[^'\\\n]|\\.)*'")


def deck_tells(text, paperwork=True):
    """Self-reference in slide text: (kind, match, line_no)."""
    hits = []
    for i, line in enumerate((text or "").splitlines(), 1):
        for pat in DECK_SELF_TELLS:
            m = re.search(pat, line, re.I)
            if m:
                hits.append(("deck-self-reference", m.group(0), i))
        if paperwork:
            for pat in DECK_PAPERWORK_TELLS:
                m = re.search(pat, line, re.I)
                if m:
                    hits.append(("deck-paperwork", m.group(0), i))
    return hits


def find_builder_tells(text):
    """The string literals of a deck builder (what will be printed on a slide or in its notes);
    comments, docstrings and code are not judged."""
    body = re.sub(r'(?s)""".*?"""|' + r"'''.*?'''", lambda m: "\n" * m.group(0).count("\n"), text or "")
    hits = []
    for i, line in enumerate(body.splitlines(), 1):
        code = line.split("#", 1)[0] if line.lstrip().startswith("#") else line
        for m in _STR.finditer(code):
            lit = m.group(0)[1:-1]
            if len(lit) < 8:
                continue
            for k, w, _ in deck_tells(lit):
                hits.append((k, w, i))
            for pat in META_TELLS + PAPER_TELLS:
                mm = re.search(pat, lit, re.I)
                if mm:
                    hits.append(("meta", mm.group(0), i))
    return hits


def lint_pptx(path):
    """Every slide's text and notes of a finished .pptx: [(slide_no, where, kind, match)]."""
    from pptx import Presentation
    out = []

    def texts(shapes):
        for sh in shapes:
            if sh.shape_type == 6:
                for t in texts(sh.shapes):
                    yield t
                continue
            if sh.has_text_frame:
                for par in sh.text_frame.paragraphs:
                    if par.text.strip():
                        yield par.text
            if getattr(sh, "has_table", False) and sh.has_table:
                for row in sh.table.rows:
                    for c in row.cells:
                        if c.text.strip():
                            yield c.text

    for n, slide in enumerate(Presentation(path).slides, 1):
        for t in texts(slide.shapes):
            for k, w, _ in deck_tells(t):
                out.append((n, "slide", k, w))
            for pat in META_TELLS + PAPER_TELLS:
                m = re.search(pat, t, re.I)
                if m:
                    out.append((n, "slide", "meta", m.group(0)))
        if slide.has_notes_slide:
            for k, w, _ in deck_tells(slide.notes_slide.notes_text_frame.text.replace("\n", " ")):
                out.append((n, "notes", k, w))
    return out


def find_tells(text, path=""):
    """Return a list of (kind, match, line_no)."""
    hits = []
    body = _strip_code(text, path)
    lines = body.splitlines()
    if _is_deck_text(path, body):
        hits += deck_tells(body)
    for i, line in enumerate(lines, 1):
        for pat in WORD_TELLS:
            m = re.search(pat, line, re.I)
            if m:
                hits.append(("word", m.group(0), i))
        for pat in META_TELLS:
            m = re.search(pat, line, re.I)
            if m:
                hits.append(("meta", m.group(0), i))
        for pat in PAPER_TELLS:
            m = re.search(pat, line, re.I)
            if m:
                hits.append(("paper-history", m.group(0), i))
        if EMOJI.search(line):
            hits.append(("emoji", EMOJI.search(line).group(0), i))
    # bold-fest: share of paragraphs (blank-line separated) that open with **bold**
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    if len(paras) >= 8:
        bold_open = sum(1 for p in paras if p.startswith("**") or p.startswith("<b>") or p.startswith("<p><b>"))
        if bold_open / len(paras) > 0.35:
            hits.append(("bold-fest", "%d of %d paragraphs open in bold" % (bold_open, len(paras)), 0))
    return hits


def _new_text(data):
    ti = data.get("tool_input", {}) or {}
    name = data.get("tool_name", "")
    if name == "Write":
        return ti.get("content", "") or ""
    if name == "Edit":
        return ti.get("new_string", "") or ""
    if name == "MultiEdit":
        return "\n".join((e.get("new_string", "") or "") for e in (ti.get("edits") or []))
    return ""


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
        ti = data.get("tool_input", {}) or {}
        path = ti.get("file_path", "") or ""
        if not path:
            return
        text = _new_text(data)
        if not text or "voice-ok" in text:
            return
        if _is_deck_builder(path, text):
            hits = find_builder_tells(text)
            if not hits:
                return
            shown = "; ".join("%s '%s' (line %d)" % (k, m, n) for k, m, n in hits[:8])
            reason = (
                "[voice_guard] REFUSED: slide text that points at the deck itself or at the paperwork "
                "behind it - %s. Rule (owner 2026-11-11 06:29, memory "
                "owner_rule_no_self_reference_in_decks_2026_11_11): 'i don't like the self introspection "
                "(referring directly to the flyer for example) ... it does not sound that human to refer "
                "to a flyer'. A slide says what the grant is and what the work is. It never cites the "
                "flyer, the form or a form field, 'this deck', 'this slide', a slide number, or what "
                "was 'written for this deck'; speaker notes follow the same rule. Rewrite the line and "
                "write again; check the finished file with: python voice_guard_hook.py --pptx FILE. "
                "If the file must quote a tell on purpose, put the token voice-ok in it." % shown
            )
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                                     "permissionDecision": "deny",
                                                     "permissionDecisionReason": reason}}))
            return
        if not _is_prose(path):
            return
        # a file that already carries the bypass token stays bypassed on edits
        try:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                    if "voice-ok" in fh.read(200000):
                        return
        except Exception:
            pass
        hits = find_tells(text, path)
        if not hits:
            return
        shown = "; ".join("%s '%s'%s" % (k, m, (" (line %d)" % n) if n else "") for k, m, n in hits[:8])
        reason = (
            "[voice_guard] REFUSED: this prose carries what the author calls an AI tell - %s. "
            "Rule (owner 2026-06-10 and 2026-09-09, memory research_writing_human_voice_2026_06_10): "
            "public text reads as if a person wrote it. Say the thing; do not narrate the page "
            "('every paper on this site...', 'the cards below...', 'click Abstract'); no 'headline', "
            "no 'delve/remarkably/notably', no emoji, no bold-fests, no note about sounding human. "
            "Rewrite the sentence and write again. If the file must quote a tell on purpose, put "
            "the token voice-ok in it." % shown
        )
        out = {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                      "permissionDecision": "deny",
                                      "permissionDecisionReason": reason}}
        print(json.dumps(out))
    except Exception:
        return


def _selftest():
    ok = True
    good = "A trained network is a stack of matrices. The Marchenko-Pastur law says which part is noise.\n\nThe proof ends in a threshold."
    bad1 = "Every paper on this site will get a short recorded talk. Headline: it works remarkably well."
    bad2 = "Cards without a video yet say so. When a talk is recorded the card becomes the player."
    cases = [
        ("C:/x/site/index.html", good, 0),
        ("C:/x/site/index.html", bad1, 3),
        ("C:/x/site/videos.html", bad2, 2),
        ("C:/x/site/site.js", bad1, None),          # not prose -> not judged
        ("C:/home/u/.claude/projects/m/memory/note.md", bad1, None),  # brain tree -> skipped
        ("C:/x/README", bad1, 3),
        ("C:/x/site/page.html", "<script>var s='Every paper on this site';</script><p>Plain text.</p>", 0),
        # the 2026-09-15 paper rule, positive controls
        ("C:/x/paper/p.tex", "The first version of this paper presented $W$ as new, and the "
                             "attribution was corrected when \\cite{j} was obtained.", 2),
        ("C:/x/paper/p.tex", "That paper does not mention Problem 11, and we found no later "
                             "paper that draws the conclusion.", 1),
        ("C:/x/paper/p.tex", "The reviews found the following errors.", 1),
        ("C:/x/paper/p.tex", "An earlier record of this computation exists.", 1),
        # negative controls: ordinary attribution, and the AI declaration, which is the one
        # place the process may be named and must keep passing
        ("C:/x/paper/p.tex", "The operator $W$ was introduced by Jamilov, who determined its "
                             "two fixed points.", 0),
        ("C:/x/paper/p.tex", "The software was written and executed by Claude Code and Codex, "
                             "which also prepared the first draft of this manuscript. The author "
                             "reviewed the code, the numbers, and the text.", 0),
    ]
    for path, text, expect in cases:
        if expect is None:
            got = None if not _is_prose(path) else len(find_tells(text, path))
        else:
            got = len(find_tells(text, path))
        res = (got == expect)
        ok = ok and res
        print("%-55s expected %s got %s %s" % (path, expect, got, "OK" if res else "FAIL"))
    # end-to-end through main(): a deny must be printed for a bad Write
    import io
    payload = json.dumps({"tool_name": "Write", "tool_input": {"file_path": "C:/x/site/index.html", "content": bad1}})
    sys.stdin = io.StringIO(payload)
    buf = io.StringIO(); old = sys.stdout; sys.stdout = buf
    try:
        main()
    finally:
        sys.stdout = old
    denied = '"deny"' in buf.getvalue()
    print("end-to-end deny on bad Write:", "OK" if denied else "FAIL"); ok = ok and denied
    payload = json.dumps({"tool_name": "Write", "tool_input": {"file_path": "C:/x/site/index.html", "content": good}})
    sys.stdin = io.StringIO(payload)
    buf = io.StringIO(); sys.stdout = buf
    try:
        main()
    finally:
        sys.stdout = old
    silent = buf.getvalue().strip() == ""
    print("end-to-end silent on good Write:", "OK" if silent else "FAIL"); ok = ok and silent
    # the 2026-11-11 deck rule: positive and negative controls on a builder's string literals
    b_bad = [
        'sub = "The three questions on the flyer, answered"',
        'head = "THE PITCH IN ONE SLIDE"',
        'bul("Available from 9 November 2026, as on the form.")',
        "cap = 'Written for this deck as an example.'",
        'lab = "shown on slides 11 to 20"',
        'notes = "Title as on the Axia BRAG form (field F07)."',
        'n = "No amount is stated on this slide or anywhere in the deck."',
        'h = "WHAT AXIA DOES, AS ITS CALL DESCRIBES IT"',
    ]
    b_good = [
        'sub = "What the benchmark tests, why it is hard, and the time I can give"',
        'bul("Available from 9 November 2026.")',
        'cap = "Example verse."',
        'prs.save(os.path.join(out, "deck.pptx"))  # slide 8 of this deck',
        'title = "Hunts of a hundred steps and more, over hours and days"',
        'x = "The grant: about $10,000 over sixty days."',
        'h = "WHAT AXIA DOES"',
        'print("patched slide", 8)',
    ]
    fb = [bool(find_builder_tells(t)) for t in b_bad]
    sb = [not find_builder_tells(t) for t in b_good]
    print("deck builder controls: fire %d/%d silent %d/%d" % (sum(fb), len(fb), sum(sb), len(sb)))
    ok = ok and all(fb) and all(sb)
    print("deck builder path recognised:",
          "OK" if _is_deck_builder("C:/t/scratchpad/build_v4.py", "from pptx import Presentation") else "FAIL",
          "OK" if not _is_deck_builder("C:/t/scratchpad/trace_case.py", "import json") else "FAIL")
    ok = ok and _is_deck_builder("C:/t/scratchpad/build_v4.py", "from pptx import Presentation") \
        and not _is_deck_builder("C:/t/scratchpad/trace_case.py", "import json")
    payload = json.dumps({"tool_name": "Write", "tool_input": {
        "file_path": "C:/t/scratchpad/build_deck.py", "content": "from pptx import Presentation\n" + b_bad[0]}})
    sys.stdin = io.StringIO(payload)
    buf = io.StringIO(); sys.stdout = buf
    try:
        main()
    finally:
        sys.stdout = old
    denied = '"deny"' in buf.getvalue()
    print("end-to-end deny on a deck builder that cites the flyer:", "OK" if denied else "FAIL"); ok = ok and denied
    payload = json.dumps({"tool_name": "Write", "tool_input": {
        "file_path": "C:/t/scratchpad/build_deck.py", "content": "from pptx import Presentation\n" + "\n".join(b_good)}})
    sys.stdin = io.StringIO(payload)
    buf = io.StringIO(); sys.stdout = buf
    try:
        main()
    finally:
        sys.stdout = old
    silent = buf.getvalue().strip() == ""
    print("end-to-end silent on a clean deck builder:", "OK" if silent else "FAIL"); ok = ok and silent
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def _pptx_cli(paths):
    bad = 0
    for p in paths:
        try:
            hits = lint_pptx(p)
        except Exception as e:
            print("%s: could not be read (%s)" % (p, e))
            bad += 1
            continue
        print("%s: %d line(s) that point at the deck or its paperwork" % (os.path.basename(p), len(hits)))
        for n, where, k, w in hits:
            print("  slide %d %s: %s '%s'" % (n, where, k, w))
        bad += 1 if hits else 0
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    if "--pptx" in sys.argv:
        sys.exit(_pptx_cli(sys.argv[sys.argv.index("--pptx") + 1:]))
    main()
