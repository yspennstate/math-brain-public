# -*- coding: utf-8 -*-
"""The paper-writing hooks W01..W73 (W01..W50 an agent, 12 Nov 2026; W57..W73 17-18 Nov). Engine: pw_core.py.

W01..W38 read the LaTeX and fire only on something found in it. W39..W50 are one line each at a moment that matters.
A text hook is a dict: id, kind ("line" runs on any text, "doc" only on a whole document), title, rule (what to do),
must (True: paper_lint exits 1), and either pat (a regex, searched line by line) or fn(doc) -> [(line, excerpt)];
min = how many findings before it speaks; skip_decl = lines inside an acknowledgment or declaration section do not count;
skip_ack = only an acknowledgment or funding section is exempt (a declaration may not narrate the manuscript either).

Where the rules come from: the opinion Probability Theory and Related Fields sent on 11 Nov 2026 (the novelty named in
labels nobody outside the paper knows, old proofs carried over, "does not appear to have undergone a thorough editing
process"), an earlier referee's "generic and mechanical", and his own orders on papers (10 Jun, 15 Sep, 4 Oct, 1 Nov,
2 Nov, 11 Nov, 12 Nov 2026).
"""
import datetime
import sys
import glob
import json
import os
import re

import pw_core as C

HERE = os.path.dirname(os.path.abspath(__file__))
RULES = "~/.claude/dreaming/paper_writing_hooks/PAPER_RULES.md"
LINT = "python ~/.claude/dreaming/paper_writing_hooks/paper_lint.py"
AUDIT = "python ~/.claude/dreaming/paper_writing_hooks/paper_audit.py"

# ---------------------------------------------------------------- patterns for the line hooks
DOCN = r"(?:paper|article|manuscript|note|work|preprint|text|write-?up|version)"
P01 = (r"\b(?:the present|this|our|the current) (?:paper|article|manuscript|note|work|preprint|text|"
       r"write-?up) (?:does not|doesn't|do not|is not|isn't|was not|will not|won't|has been|makes no|should not|cannot|"
       r"can't|is intended|is meant|aims? to be|tries to|attempts to|goes (?:well |far |much |substantially )?beyond|"
       r"is more than|avoids|differs from|departs from|no longer|relies neither|never)\b|"
       r"\bis not intended (?:to|as)\b|\bthe purpose of (?:this|the present) "
       r"(?:paper|note|article) is not\b|\b(?:this|the present) (?:paper|note|article) should be read as\b|"
       r"\bnot\b[^.;\n]{0,40}\bas a black box\b|"
       r"\bgo(?:es)? (?:well |far |much |substantially |significantly )?beyond (?:\\cite|\[\d|our (?:earlier|previous)|the "
       r"(?:earlier|previous|square))")
P02 = (r"\b(?:first|earlier|previous|prior|original|initial|preliminary) (?:version|draft|iteration|write-?up)s? of (?:this|"
       r"the present|the|our) " + DOCN + r"\b|\bin (?:an|the) (?:earlier|previous|first) (?:version|draft)\b|"
       r"\b(?:was|were|has been|have been) (?:corrected|revised|rewritten|updated|fixed|amended) (?:when|after|once|in "
       r"(?:this|the current|the present) version)\b|\bsince the (?:first|previous|earlier) version\b|\ban earlier record\b|"
       r"\bwas obtained afterwards\b|\b(?:before|prior to) inclusion\b|\bpresented \S+ as new\b|"
       r"\bthe attribution was corrected\b|\b(?:version|v\.?) ?\d+ of (?:this|the|our) " + DOCN + r"\b|\bin v\d\b|"
       r"\b(?:has|have) since been (?:fixed|corrected|amended|revised|repaired)\b|\b(?:citation|attribution|statement|"
       r"claim|proof) (?:was|has been|had been) (?:amended|changed|fixed|corrected|repaired)\b|"
       r"\bchanges (?:from|since|in|relative to) (?:v\d|version|the (?:first|previous|earlier))\b|\bearlier versions\b|"
       r"\brevision history\b|\ba (?:previous|prior|earlier) (?:write-?up|iteration)\b|"
       r"\ban earlier (?:draft|version) (?:of this|had|claimed|stated|contained)\b|"
       r"\bbecame aware of\b[^.;\n]{0,60}\bafter\b|\bafter the first posting\b")
P03 = (r"\bwe (?:found|could find|could locate|were able to (?:find|locate)|have found|did not find|were unable to find) "
       r"(?:no|any) (?:later |earlier |other |such |prior |published )?(?:paper|reference|work|result|source|proof|"
       r"statement|record)s?\b|\bwe (?:have )?searched\b|\b(?:a|our) (?:literature )?search (?:of|on|in|did|found|turned|"
       r"reveal|return)\w*\b|\bdoes not mention (?:Problem|Conjecture|Question)\b|\bno later paper\b|"
       r"\b(?:are|were|am) not aware of any\b|\b(?:could|did|can) not (?:find|locate)\b|\b(?:were|are) unable to "
       r"(?:find|locate)\b|\bmakes no mention\b|\bto our knowledge,? no\b|\bnothing was found\b|"
       r"\bwe (?:know|knew) of no (?:paper|reference|proof|work|source)\b")
# names are matched with their capitals (Claude Shannon and Claude Berge are people); everything else in any case
P04N = (r"\bClaude(?! (?!Opus|Sonnet|Haiku|Fable|Code|Mythos)[A-Z])\b|\b(?:ChatGPT|GPT(?:-?[0-9][\w.]*)?|Codex|Anthropic|"
        r"OpenAI|Gemini|Copilot|Grok|LLMs?|Opus [0-9]|Sonnet [0-9]|Fable [0-9]|Mythos)\b")
P04 = (r"\b(?:audit|referee|review) (?:pass|passes|agent|agents)\b|\bsub-?agents?\b|\b(?:in|during|after) (?:a|an|one|"
       r"the|another) (?:earlier |later |previous )?session\b|\bthe (?:agent|agents|swarm|mesh) (?:found|checked|verified|"
       r"wrote|proved|produced)\b|\b(?:AI|machine)[- ](?:generated|written|assisted) (?:proof|draft|text)\b|"
       r"\b(?:large )?language models?\b|\bAI (?:system|assistant|tool|model|agent)s?\b|"
       r"\bautomated (?:assistant|referee|reviewer|audit)s?\b|\bhuman voice\b|\bsound(?:s|ing)? (?:more )?human\b|"
       r"\b(?:AI|machine)[- ]written\b|\bread(?:s|ing)? as machine\b|\bwritten by an? (?:AI|LLM|model)\b")
P05 = (r"\bre-?derived (?:line by line|independently|from scratch)\b|\b(?:checked|verified|read|compared|audited|"
       r"reviewed|confirmed) line[- ]by[- ]line\b|\bline[- ]by[- ]line (?:check|verification|audit|re-?derivation|"
       r"comparison|review|reading)\b|\bdouble[- ]checked\b|"
       r"\bwe (?:have )?(?:carefully|independently|thoroughly) (?:checked|verified|re-?derived|confirmed)\b|"
       r"\b(?:was|were) (?:checked|verified|re-?derived) (?:before|after|prior to) (?:inclusion|submission|posting)\b|"
       r"\b(?:checked|verified) prior to (?:inclusion|submission|posting)\b|"
       r"\bthis was found (?:only )?(?:before|after)\b|\bthe reviews? (?:found|turned up|identified|uncovered|flagged)\b|"
       r"\bsanity[- ](?:check|test)s?\b|\bindependent(?:ly)? "
       r"(?:re-?derivation|second pass|audit)\b|\bcross[- ]checked (?:by|against) (?:a second|an independent|another)\b|"
       r"\b(?:verified|checked|confirmed) (?:twice|several times|repeatedly|many times|multiple times)\b|"
       r"\bindependently (?:reproduced|verified|confirmed|re-?checked)\b|\bvetted\b|"
       r"\bgone through the proof\b|\ban independent (?:verification|check|confirmation|computation) (?:confirm|show|"
       r"agree|g[ai]ve|reproduc)\w*\b")
P06 = (r"\b(?:clearly|carefully|explicitly|plainly|honestly) (?:labell?ed|marked|flagged)\b|"
       r"\b(?:labell?ed|marked|flagged) (?:honestly|as such)\b|\bwe do not claim\b|\bwe make no claim\b|"
       r"\b(?:flagged|marked) as (?:a )?(?:conjectur|heuristic|unproved|open)\w*\b|\badmittedly\b|\bwe caution\b|"
       r"\bhonest(?:ly)? (?:label\w*|account|assessment|caveat|statement|about)\b|"
       r"\bto be (?:clear|honest|fair|transparent|upfront)\b|\bfor (?:full |the sake of )?"
       r"transparency\b|\bin the interest of (?:transparency|honesty|full disclosure)\b|\bfull disclosure\b|"
       r"\bwe (?:openly |freely )(?:acknowledge|admit|concede) that\b|\bit must be (?:admitted|conceded)\b|"
       r"\bwe are (?:careful|explicit) (?:to|about|not to)\b|\bcandid(?:ly)?\b|\bwhat is and (?:what )?is not proved\b|"
       r"\bhonest(?:y)? (?:ledger|accounting|summary|list|scope)\b|\bwe want to be (?:clear|explicit|upfront)\b|"
       r"\blest (?:the reader|there be)\b|\bwe hasten to add\b")
P07 = (r"\b(?:remarkabl[ey]|striking(?:ly)?|notably|delv(?:e|es|ed|ing)|crucially|importantly|interestingly|"
       r"worth noting|noteworthy|pivotal|sheds? (?:new )?light|paves? the way|underscor(?:e|es|ed|ing)|showcas(?:e|es|ed|"
       r"ing)|tapestry|nuanced|seamless(?:ly)?|holistic(?:ally)?|testament to|meticulous(?:ly)?|multifaceted|"
       r"in the realm of|the landscape of|a rich (?:interplay|tapestry)|unlock(?:s|ing)?|game[- ]chang\w+|synerg\w+|"
       r"intriguing(?:ly)?|fascinating|myriad|plethora)\b")
P08 = (r"\bis not the (?:true|real|actual) (?:source|reason|cause|origin)\b|\bthe (?:[a-z-]+ )?heuristic is simple\b|"
       r"\bthe key (?:insight|takeaway|message|point|observation) is\b|\bin a nutshell\b|\bat (?:its|their) (?:heart|core)\b|"
       r"\bthe (?:moral|upshot|punchline|take-?away|bottom line)\b|\bthe (?:whole |real |full )?story is\b|"
       r"\btells? (?:the|a) (?:whole|same|different|fuller) story\b|\bthe picture that emerges\b|\bone slogan\b|"
       r"\bin plain (?:terms|words|language)\b|\bthe lesson is\b|\bthe short answer\b|"
       r"\b(?:the )?(?:new|novel|additional|extra|main new|key new|principal new) (?:ingredients|components|inputs|"
       r"additions|features|elements) (?:are|is|here are|of the proof are)\b")
P09 = (r"\b(?:explain|clarif|account|describ)\w* (?:exactly|precisely|fully|completely) (?:how|why|what)\b|"
       r"\bgives? a (?:full|complete) account\b|\bexplain\w* exactly\b|\bfully (?:explain|resolv|settl|understand)\w*\b|\bcompletely (?:resolv|settl|solv|explain)\w*"
       r"\b|\b(?:settl|resolv|answer|clos|solv)\w* [^.;]{0,60}once and for all\b|\bfor the first time\b|"
       r"\bdefinitive(?:ly)?\b|\bcomplete (?:answer|picture|understanding|"
       r"resolution)\b|\bany and all\b|\bclos(?:es|ing) the (?:question|problem|gap) (?:completely|entirely)\b|"
       r"\bthe (?:first|only) (?:known )?(?:proof|result|bound|construction) of (?:its|this) kind\b")
P10 = (r"\b(?:clearly|obviously|trivially|evidently|of course|needless to say|it is (?:easy|straightforward|not hard|"
       r"immediate|elementary|routine) to (?:see|check|verify|show|prove))\b")
PARTS = r"(?:sections?|appendix|appendices|remarks?|proofs?|paragraphs?|discussion|references?|examples?|figures?|tables?)"
P20 = (r"\b(?:these|the above) (?:additions|modifications|(?:new|additional|novel|extra) (?:ingredients|additions|"
       r"components|inputs|elements|features))\b|\bwhat is (?:added|changed) (?:here|in this|relative to)\b|"
       r"\bwhat is new (?:in this (?:version|revision|draft)|(?:here )?(?:relative to|compared (?:with|to)) (?:the |an? |our )?(?:previous|earlier|first|old|original) (?:version|draft|manuscript|preprint))\b|"
       r"\bwhat (?:has )?changed (?:relative to|since|from|compared)\b|"
       r"\bthe old (?:section|lemma|theorem|proof|appendix|argument|statement)\b[^.;\n]{0,40}\b(?:was|were|has been) "
       r"(?:dropped|removed|replaced|cut|rewritten)\b|"
       r"\bnew in this (?:version|paper|revision|draft)\b|"
       r"\b" + PARTS + r" [^.;]{0,40}(?:has|have) (?:now )?been (?:added|removed|moved|expanded|shortened|rewritten|"
       r"reorgani[sz]ed|replaced)\b|"
       r"\bwe (?:have )?(?:added|removed|expanded|rewrote|rewritten|reorgani[sz]ed) (?:a |an |the |new )?" + PARTS + r"\b|"
       r"\bcompared (?:with|to) (?:the )?(?:previous|earlier|first) version\b|\bin (?:this|the) (?:revision|revised version)\b|"
       r"\bthe main changes are\b")
P24 = (r"\bTODO\b|\bFIXME\b|\bXXX+\b|\bTBD\b|\?\?\?|\[citation needed\]|\[cite\]|\[ref\]|\\(?:ref|eqref|cref|cite\w*)\{\s*\}|"
       r"\[\?+\]|\bto be (?:added|written|filled in|completed|inserted)\b|\blorem ipsum\b|\bplaceholder\b|"
       r"\binsert (?:reference|citation|figure|proof) here\b")
P28 = (r"\bin order to\b|\bthe fact that\b|\bit turns out that\b|\bit (?:should|must|may) be noted that\b|"
       r"\bit is (?:worth|important|interesting|useful|instructive) (?:noting|to note|mentioning|to mention|pointing out|"
       r"to point out|to observe|emphasi[sz]ing) that\b|\bbasically\b|\bit goes without saying\b|\bas a matter of fact\b|"
       r"\bin a certain sense\b|\bmay potentially\b|\bcould possibly\b|\bto the best of our knowledge\b|"
       r"\bplay(?:s|ed)? an? (?:important|key|central|crucial|fundamental|vital) role\b|\bha(?:s|ve) (?:attracted|received|"
       r"drawn) (?:considerable|significant|much|a lot of|increasing|growing|great) (?:attention|interest)\b|"
       r"\ba (?:wide|broad|vast) (?:range|variety|array) of\b|\bdue to the fact that\b|\bfor the sake of completeness\b|"
       r"\bat this point in time\b|\bit is (?:important|essential|crucial) to (?:note|stress|emphasi[sz]e|recogni[sz]e)\b")
P32 = (r"\bnot only\b[^.;]{0,90}\bbut(?: also)?\b|\b(?:is|are|was|were) not (?:merely|just|simply|only) [^.;]{0,70}[;,:] "
       r"(?:it|they|but|rather)\b|\bnot (?:because|by|from) [^.;]{0,80}\bbut (?:because|by|from)\b|"
       r"\bless (?:a|an) [^.;]{0,40} than (?:a|an) \b|\bis not (?:a|an|the) [^.;]{0,50}; it is\b|"
       r"\bnot [a-z]+, but [a-z]+\.")
P33 = (r"\bwe now turn to\b|\bhaving established\b|\barmed with\b|\bwith (?:this|these|that) (?:in hand|preliminaries|"
       r"tools|preparations)\b|\bwe are now (?:ready|in a position|able)\b|\bis organi[sz]ed as follows\b|"
       r"\bthe (?:rest|remainder) of (?:this|the) (?:paper|article|section|note)\b|\bin (?:this|the next|the following|the "
       r"present) (?:sub)?section,? we\b|\bas (?:mentioned|noted|discussed|explained|described|stated|promised|announced) "
       r"(?:above|earlier|before|previously|in the introduction)\b|\bwe (?:begin|start|conclude|end|close) (?:this section "
       r")?(?:by|with)\b|\blet us now\b|\bbefore (?:proceeding|turning|stating|we (?:state|turn|proceed))\b|"
       r"\bwe (?:first|next|then|finally) (?:recall|collect|record|turn|gather)\b|\bit remains (?:only )?to\b|"
       r"\bwith these preparations\b|\bwe pause to\b")
P38 = (r"\b(?:novel|powerful|elegant|beautiful|surprising(?:ly)?|remarkable|groundbreaking|state[- ]of[- ]the[- ]art|"
       r"cutting[- ]edge|unprecedented|far[- ]reaching|major (?:advance|breakthrough|step)|breakthrough|"
       r"significant(?:ly)? (?:advance|improve|extend|strengthen)\w*|substantial(?:ly)? (?:advance|improve|extend|"
       r"strengthen)\w*|landmark|seminal contribution of (?:this|the present)|highly non-?trivial)\b")


# ---------------------------------------------------------------- functions for the hooks that need more than a regex
AI_TOPIC = re.compile(r"\b(?:agents?|language models?|llm|artificial intelligence|\bai\b|brain|neural|chatgpt|claude|"
                      r"copilot|machine learning|deep learning|transformer)\b", re.I)


# Words that name the AI ("AI agents", "language models") are treated like a model's name; the rest of P04 narrates the
# process (sessions, audit agents, sub-agents, "the agents found") and is MUST everywhere.
P04_AI = r"\b(?:large )?language models?\b|\bAI (?:system|assistant|tool|model|agent)s?\b"
assert P04_AI + "|" in P04
P04_PROC = P04.replace(P04_AI + "|", "")
# A cited work whose author is a company ("a 2026 preprint of OpenAI proves it") names the source, not the process.
CITED_ORG = re.compile(r"\b(?:preprints?|papers?|reports?|articles?|notes?|surveys?|works?|results?)\s+(?:of|by|from)\s+"
                       r"(?:the\s+)?(?:OpenAI|Anthropic|Google(?:\s+DeepMind)?|DeepMind)\b(?!['’]s\s+[A-Z])")


APP_DOC = re.compile(r"\b(?:research|teaching|diversity|mentoring)\s+statement\b|\bstatement of (?:teaching|research)|"
                     r"\bcover letter\b|\bDear (?:Members|Hiring|Search|Selection|Committee|Professor|Dr)\b", re.I)
APP_PATH = re.compile(r"statement|cover[_-]?letter|(?:^|/)cl[_\d.]", re.I)


def application_doc(d):
    """A research, teaching or diversity statement or a cover letter, not a paper: AI work is its subject there, and it
    carries no declaration section or funding line (24 Nov: W04 and W51 fired on a teaching statement's paragraph on
    checking AI-written proofs). A file with an abstract is always a paper."""
    if re.search(r"\\begin\{abstract\}", d.nc):
        return False
    return bool(APP_PATH.search(d.path or "") or APP_DOC.search(d.nc[:4000]))


def f04(d):
    """MUST, except a model named outside the declaration in a paper he named (AUTHOR_READ_OK holds the date and his
    words): there the AI sentence in the abstract and introduction is the author's rule (14 Nov), so it is a note that the
    sentence must also credit the mathematicians. Process words (sessions, audit agents) stay MUST everywhere.
    Not applied to a statement or cover letter (application_doc)."""
    if AI_TOPIC.search(d.title()):
        return []
    skip = d.decl_lines()
    got = {ln: C.MUST_TAG + ex for ln, ex in C.line_hits(d, P04_PROC, skip)}
    if application_doc(d):      # AI as the statement's subject is allowed; the process words stay MUST
        return sorted(got.items())
    cited = set(d.line_of(m.start()) for src in (d.prose, d.flat) for m in CITED_ORG.finditer(src))
    names = sorted(dict(C.line_hits(d, P04_AI, skip) + C.line_hits(d, P04N, skip, 0)).items())
    nam = named(d.path) if names else False
    for ln, ex in names:
        if ln in got:
            continue
        if ln in cited and not re.search(r"\b(?:Claude|ChatGPT|GPT|Codex|Gemini|Copilot|Grok|LLMs?|Opus|Sonnet|Fable|"
                                         r"Mythos)\b", ex):
            continue
        # 18 Nov: no AI statement in the abstract or the introduction; it stays in the declaration at the end.
        # The 14 Nov exception for papers he named is withdrawn: outside the declaration it is a MUST.
        got[ln] = C.MUST_TAG + ("the AI statement goes only in the declaration at the end, never in the abstract or "
                                "the introduction (rule of 18 Nov 2026): " + ex)
    return sorted(got.items())


KNOWN = re.compile(r"\b(?:well[- ]known|folklore|it is known that|as is known|it is (?:a )?classical (?:fact|result)|"
                   r"(?:a|the|by a|by the) (?:standard|classical|usual|routine|familiar) (?:fact|result|argument|theorem|"
                   r"estimate|lemma|inequality|computation|calculation|bound)|by standard (?:arguments|results|theory|"
                   r"estimates))\b", re.I)


def f11(d):
    out = []
    for ln, s in d.sentences():
        m = KNOWN.search(s)
        if m and not re.search(r"\\(?:cite|ref|eqref|cref|Cref)", s) and not re.search(r"\bsee\b", s, re.I):
            out.append((ln, C.excerpt(C.plain(s))))
    return out


CITE = re.compile(r"\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]*)\}")


def f12(d):
    """Five or more references behind one statement: in one bracket, or in a run of brackets in one sentence."""
    out, seen = [], set()
    for ln, s in d.sentences():
        keys = [k.strip() for m in CITE.finditer(s) for k in m.group(1).split(",") if k.strip()]
        if len(keys) >= 5 and ln not in seen:
            seen.add(ln)
            how = "in one bracket" if max(len(m.group(1).split(",")) for m in CITE.finditer(s)) >= 5 else \
                "in one sentence"
            out.append((ln, "%d references %s: %s" % (len(keys), how, C.excerpt(", ".join(keys), 60))))
    return out


EMOJI = re.compile(u"[\u2600-\u27bf\u2b50\u2b55\U0001f300-\U0001faff]|"
                   u"(?<=[A-Za-z)\\]}])(?:\\\\[,;]|[ \\t])*!(?=\\s|$|[)\\]}'\"])|\\bheadlines?\\b", re.I)
MARKS = re.compile(r"\\(?:checkmark|bigstar|cmark|xmark|ding\{\d+\}|faCheck\w*|faStar\w*|starredtext)\b|\\ding\{\d+\}")


def f13(d):
    out, seen = [], set()
    skip = d.decl_lines()
    for i, ln in enumerate(d.lines, 1):
        if i in skip:
            continue
        m = EMOJI.search(ln)
        if m and not ln[: m.end()].endswith("\\!"):
            seen.add(i)
            out.append((i, C.excerpt(ln[max(0, m.start() - 50): m.end() + 30])))
    start = d.nc.find("\\begin{document}")           # marks set inside $...$ are masked in the prose: read the source
    first = d.nc.count("\n", 0, start) + 1 if start >= 0 else 1
    for i, ln in enumerate(d.nc.split("\n"), 1):
        if i < first or i in skip or i in seen:
            continue
        m = MARKS.search(ln)
        if m:
            out.append((i, C.excerpt(ln[max(0, m.start() - 50): m.end() + 30])))
    return sorted(out)


BOLD = re.compile(r"\\textbf\{|\{\\bf\b|\\bfseries\b")
BOLDHEAD = re.compile(r"^\s*\\textbf\{(?:Step|Case|Claim|Proof|Part)\b")


def f14(d):
    hits = C.line_hits(d, BOLD.pattern, None, 0)
    heads = C.line_hits(d, r"^\s*\\textbf\{(?:Step|Case|Claim|Proof|Part)\b", None, re.M)
    n = len(hits) - len(heads)
    if n >= 8 and n > d.words / 450.0:
        return [(hits[0][0], "%d bold phrases in about %d words" % (n, d.words))] + hits[:1]
    out = []
    for para in re.finditer(r"(?:[^\n]|\n(?!\s*\n))+", d.prose):       # a paragraph that is mostly bold
        t = para.group(0)
        k = len(BOLD.findall(t)) - sum(1 for ln in t.split("\n") if BOLDHEAD.match(ln))
        if k >= 4:
            out.append((d.line_of(para.start() + len(t) - len(t.lstrip())), "%d bold phrases in one paragraph" % k))
    return out[:3]


def f15(d):
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", d.nc, re.S)
    if not m:
        return []
    a, ln = m.group(1), d.nc_line(m.start())
    out = []
    w = len(re.findall(r"[A-Za-z]{2,}", C.plain(C.MATH.sub(" M ", a))))
    if w > 220:
        out.append((ln, "the abstract has %d words" % w))
    if re.search(r"\\begin\{(?:itemize|enumerate)\}", a):
        out.append((ln, "a list inside the abstract"))
    if len(re.findall(r"\((?:i{1,3}|iv|v|[1-5]|[a-e])\)", a)) >= 3:
        out.append((ln, "the abstract enumerates its contents (i), (ii), (iii)"))
    if a.count(";") >= 3 or re.search(r":\s*(?:\(|first\b|we\b)[^.]{0,300};[^.]{0,300};", a, re.I):
        out.append((ln, "the abstract is a colon list of clauses"))
    if re.search(r"\b(?:we also|in addition|moreover|furthermore|additionally|finally,)\b.*\b(?:we also|in addition|"
                 r"moreover|furthermore|additionally|finally,)\b", a, re.I | re.S):
        out.append((ln, "the abstract strings results together with also / in addition / finally"))
    return out


TOOL_NOUN = (r"(construction|estimate|decomposition|argument|lemma|bound|method|trick|scheme|principle|analysis|inequality|"
             r"technique|identity|formula|base|law|exponent|mechanism|phenomenon|reduction|criterion|dichotomy|step|"
             r"condition|property|regime|coupling|expansion|representation)s?")
LABEL = re.compile(r"\b([a-z]{2,}(?:-[a-z]{2,})+(?:/[a-z]{2,}(?:-[a-z]{2,})+)*)\s+" + TOOL_NOUN + r"\b")
COMMON = re.compile(
    r"^(?:non|sub|super|semi|pre|post|co|self|quasi|pseudo|multi|anti|re|bi|tri|half|well|ill|so|a|log|[a-z]|lower|upper|"
    r"high|low|large|small|long|short|first|second|third|one|two|three|worst|best|average|mean|union|leading)-|"
    r"-(?:dimensional|valued|order|sided|type|like|wise|based|free|independent|dependent|invariant|preserving|theoretic|"
    r"adjoint|definite|continuous|measurable|integrable|bounded|smooth|regular|point|step|term|body|scale|time|space|"
    r"parameter|variable|field|form|rank|norm|moment|deviation|ball|probability|limit|bulk|case|side|hand|off|up|"
    r"down|out|in|to|one|two|known|posed|defined|behaved|tailed|range|root|layer|level|degree|rate|size|sum|product|"
    r"square|squares|neighbor|neighbour|state|energy|value|values|function|functions|matrix|vector|kernel|norm|"
    r"gaussian|exponential|linear|convex|concave|stable|uniform|normalized|adapted|optimal|sharp|tight|asymptotic|"
    r"negative|positive|zero|trivial|empty|degenerate|singular|random|deterministic|standard|classical|density|"
    r"concentrated|concave|bound|bounds|moments|tails|entries|case)(?:$|/)")
# Emphasis alone defines nothing: \emph{marked-row construction} is still a bare label. Emphasis followed by what the
# word means ("a row is \emph{marked} if ...") is a definition.
DEFCUE = re.compile(r"\bwe call\b|\bcalled\b|\bsaid to be\b|\brefer(?:red)? to as\b|\btermed\b|\bdefin(?:e|ed|es|ition)\b|"
                    r"\bby which we mean\b|\bmeaning (?:that|a|an|the)\b|\bthat is,|\bi\.e\.|\bnamely\b|\bintroduced (?:by|in)\b|"
                    r"\\cite|\bCITE\b|\\(?:emph|textit|textsl)\{[^}]*\}[^.]{0,80}\b(?:if|when|means|denotes|stands for)\b",
                    re.I)
TOOL_ITEM = re.compile(r"\b(?:an?|the)\s+((?:[^\s,;:.()]+\s+){1,4}?)" + TOOL_NOUN + r"\b", re.I)


def _labels(d, a, b):
    """[(pos, label, noun, sentence index)] of coined tool names between prose offsets a and b."""
    out = []
    low = d.prose[a:b].lower()
    for m in LABEL.finditer(low):
        lab = m.group(1)
        orig = d.prose[a + m.start(): a + m.start() + len(lab)]
        if COMMON.search(lab) or any(part[:1].isupper() for part in re.split(r"[-/]", orig)):
            continue                                   # a common compound, or a name (Cauchy-Schwarz, Berry-Esseen)
        out.append((a + m.start(), lab, m.group(2)))
    return out


def f16(d):
    a, b = d.intro()
    title = C.norm(d.title())
    sents = d.sentences()
    seen, out = set(), []
    low = d.prose.lower() if d.whole else ""
    for pos, lab, noun in _labels(d, a, b):
        if lab in seen or lab.replace("-", " ").replace("/", " ") in title:
            continue
        seen.add(lab)
        if low and low.count(lab) < 2:
            continue                                   # used once: a description, not a name the paper relies on
        ln = d.line_of(pos)
        key = lab.split("/")[0]
        near = [s for l2, s in sents if key in s.lower()] if d.whole else \
            ([s for l2, s in sents if abs(l2 - ln) <= 1 and key in s.lower()] or
             [s for l2, s in sents if abs(l2 - ln) <= 1])
        if any(DEFCUE.search(s) or "\\ref" in s or "\\eqref" in s for s in near):
            continue                                   # some sentence of the paper says what it is
        # in the abstract or the first two pages this is what the referee stopped on: a MUST there
        out.append((ln, "%s\"%s %s\" is used here and nothing near it says what it is"
                    % (C.MUST_TAG if pos - a < 7000 else "", lab, noun)))
    # a sentence of the abstract or introduction that lists three or more tools by name, hyphenated or not, and neither
    # cites nor defines any of them (the paragraph the PTRF referee quoted, in any wording)
    la, lb = d.line_of(a), d.line_of(b)
    got = set(l for l, _ in out)
    for ln, s in sents:
        if not la <= ln <= lb or ln in got or DEFCUE.search(s):
            continue
        items = ["%s%s" % (m.group(1), m.group(2)) for m in TOOL_ITEM.finditer(C.plain(s))
                 if not re.match(r"(?:following|same|above|next|main|first|second|third|key|basic|general|new|required|"
                                 r"desired|resulting|corresponding|previous|preceding|standard|classical|usual|"
                                 r"well-known|triangle|union|chain|product|upper|lower|matching)\s", m.group(1), re.I)
                 and not re.search(r"\b[A-Z][a-z]", m.group(1))]          # Brunn--Minkowski: a name, not a coinage
        if len(items) >= 3:
            # the paragraph the editor quoted: on the first pages this is a MUST
            out.append((ln, "%s%d tools named in one sentence and none defined or cited: %s"
                        % (C.MUST_TAG if ln - la <= 70 else "", len(items), C.excerpt("; ".join(re.sub(r"\s+", " ", x) for x in items), 90))))
    return sorted(out, key=lambda x: (0 if x[1].startswith(C.MUST_TAG) else 1, x[0]))[:6]


SYN = {}
for _k, _ws in (("PAIR", "two pair double twin dual couple"), ("GOOD", "good typical generic regular nice"),
                ("BAD", "bad exceptional atypical irregular singular"), ("MARK", "marked tagged distinguished selected "
                "labelled labeled chosen"), ("EXTRA", "surplus redundancy redundant excess extra oversampling "
                "oversampled"), ("SMALL", "small tiny little"), ("LARGE", "large big huge"),
                ("ROW", "row rows"), ("COL", "column columns"), ("NORMAL", "normal normals"),
                ("OVERLAP", "overlap overlaps overlapping intersection")):
    for _w in _ws.split():
        SYN[_w] = _k
NOUN_CLASS = {}
for _k, _ws in (("EST", "estimate bound inequality"), ("METH", "construction scheme method technique argument trick"),
                ("SPLIT", "decomposition dichotomy expansion representation")):
    for _w in _ws.split():
        NOUN_CLASS[_w] = _k


def f17(d):
    groups = {}
    low = d.prose.lower()
    for m in re.finditer(r"\b([a-z]{2,}(?:-[a-z]{2,})+)\b", low):
        lab = m.group(1)
        parts = [SYN.get(w, w.rstrip("s")) for w in lab.split("-")]
        if not any(p.isupper() for p in parts):
            continue
        groups.setdefault("-".join(parts), {}).setdefault(lab, d.line_of(m.start()))
    # the same with the words set apart: "two normal estimate", "double normal bound", "pair normal inequality"
    for m in re.finditer(r"\b([a-z]{3,}(?:[ -][a-z]{3,}){1,2}) " + TOOL_NOUN + r"\b", low):
        mods = re.split(r"[ -]", m.group(1))
        if COMMON.search("-".join(mods)) or mods[0] in ("the", "and", "for", "with", "this", "that", "these", "our"):
            continue
        parts = [SYN.get(w, w.rstrip("s")) for w in mods]
        if not any(p.isupper() for p in parts):
            continue
        key = "-".join(parts) + "-" + NOUN_CLASS.get(m.group(2), m.group(2))
        groups.setdefault(key, {}).setdefault("%s %s" % (m.group(1), m.group(2)), d.line_of(m.start()))
    out = []
    for key, forms in sorted(groups.items()):
        stems = set(f.rstrip("s").replace("-", " ") for f in forms)
        if len(stems) >= 2:
            fs = sorted(forms.items(), key=lambda x: x[1])
            out.append((fs[1][1], "one thing, %d names: %s" % (len(fs), ", ".join("\"%s\" (l.%d)" % f for f in fs[:4]))))
    return out[:4]


def f18(d):
    seen = {}
    for m in C.MATH.finditer(d.nc):
        body = m.group(0)
        # a definition, not every formula with an equals sign: ":=" or "let / denote / define / write / set" before it
        if not re.search(r":=|\\coloneqq|\\stackrel\{\\text\{def\}\}\{=\}|\\triangleq", body):
            if "=" not in body or not re.search(r"\b(?:let|denote[sd]?|define[sd]?|write|set|put)\b[^.]{0,60}$",
                                                d.nc[max(0, m.start() - 80):m.start()], re.I):
                continue
        k = re.sub(r"\\(?:left|right|,|;|!|quad|qquad|displaystyle|begin\{[^}]*\}|end\{[^}]*\}|label\{[^}]*\})|[\s$.,&]|"
                   r"\\\[|\\\]|\\\(|\\\)|\\\\", "", body)
        if len(k) < 14:
            continue
        seen.setdefault(k, []).append((d.nc_line(m.start()), body))
    out = []
    for k, v in seen.items():
        lines = sorted(set(l for l, _ in v))
        if len(v) >= 3 and len(lines) >= 2:
            out.append((lines[0], "the same formula is written %d times (l.%s): %s"
                        % (len(v), ", ".join(str(x) for x in lines[:5]), C.excerpt(v[0][1], 60))))
    return sorted(out)[:3]


CMP = re.compile(r"\b(?:in contrast|unlike|whereas|improv\w+|extend\w*|generali[sz]\w+|sharpen\w*|strengthen\w*|previously|"
                 r"earlier|(?:was|were|is|are) (?:proved|proven|shown|obtained|established|known|treated|considered|"
                 r"studied|introduced|solved|settled)|(?:prove[ds]?|show(?:ed|s)|obtain(?:ed|s)|establish(?:ed|es)|treat"
                 r"(?:ed|s)|consider(?:ed|s)|stud(?:ied|ies)|introduc(?:ed|es)|determin(?:ed|es)|comput(?:ed|es)|g[ai]ve[sn]?"
                 r"|conjectur(?:ed|es)|ask(?:ed|s))\b|due to|goes back to|only (?:for|when|in|under)|remain(?:s|ed) open|"
                 r"fails?|breaks down|does not (?:apply|extend|cover|give|yield)|no longer|the case\b)", re.I)


NOT_A_NAME = re.compile(r"department|universit|institut|school|college|laborator|email|e-mail|@|street|road|\d", re.I)
CITE_KEYS = re.compile(r"\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]*)\}")


def _surnames(d):
    out = set()
    for a in re.findall(r"\\author\s*(?:\[[^\]]*\])?\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}", d.nc):
        a = re.sub(r"\\(?:thanks|footnote|email|address|affiliation|inst)\b.*", "", a, flags=re.S)
        for person in re.split(r"\\and\b|\\\\|,|\band\b|\\quad|\\qquad", a):
            if NOT_A_NAME.search(person):
                continue
            w = re.findall(r"[A-Z][A-Za-z'-]{2,}", C.plain(person))
            if w:
                out.add(w[-1].lower())
    return out


NOT_A_PAPER = re.compile(r"supplementary|\brepository\b|source code|code and data|\bsoftware\b|\bdata ?set\b", re.I)


def own_keys(d):
    """Citation keys of the reference-list entries written by one of this paper's authors."""
    names = _surnames(d)
    if not names:
        return []
    keys = []
    for m in re.finditer(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}([^\\]{0,160})", d.nc):
        head = m.group(2).lower()
        nxt = d.nc.find("\\bibitem", m.end(1))
        if NOT_A_PAPER.search(d.nc[m.end(1):nxt if 0 <= nxt - m.end(1) <= 900 else m.end(1) + 900]):
            continue        # supplementary material or the paper's own code: not an earlier paper to compare with
        if any(re.search(r"\b%s\b" % re.escape(n), head) for n in names):
            keys.append(m.group(1).strip())
    base = os.path.dirname(d.path) if d.path else ""
    for m in re.finditer(r"\\(?:bibliography|addbibresource)\s*(?:\[[^\]]*\])?\{([^}]+)\}", d.nc):
        for nm in m.group(1).split(","):
            fp = os.path.join(base, nm.strip() if nm.strip().lower().endswith(".bib") else nm.strip() + ".bib")
            try:
                if os.path.getsize(fp) > 3000000:
                    continue
                with open(fp, encoding="utf-8", errors="replace") as f:
                    bib = f.read()
            except OSError:
                continue
            for e in re.split(r"\n\s*@", "\n" + bib):
                k = re.match(r"\w+\s*\{\s*([^,\s]+)\s*,", e)
                au = re.search(r"\bauthor\s*=\s*[{\"](.*?)[}\"]\s*,?\s*(?:\n|$)", e, re.I | re.S)
                if k and au and not NOT_A_PAPER.search(e) and \
                        any(re.search(r"\b%s\b" % re.escape(n), au.group(1).lower()) for n in names):
                    keys.append(k.group(1))
    # an own entry cited only in the closing declaration / data / acknowledgment section (the brain, its repository,
    # the framework that produced the paper) is not earlier work the introduction must set itself against
    late = [m.start() for m in re.finditer(
        r"\\(?:section|subsection|subsubsection|paragraph)\*?\{[^}]*(?:acknowledg|declar|use of ai|generative|"
        r"funding|availab)[^}]*\}|\\begin\{(?:acknowledg\w*|ack|funding|declaration\w*)\}", d.nc, re.I)]
    if late:
        cut = late[0]
        cites = {}
        for m in CITE_KEYS.finditer(d.nc):
            for k in m.group(1).split(","):
                cites.setdefault(k.strip(), []).append(m.start())
        keys = [k for k in keys if not (cites.get(k.strip()) and min(cites[k.strip()]) >= cut)]
    return sorted(set(keys))


def f19(d):
    a, b = d.intro()
    la, lb = d.line_of(a), d.line_of(b)
    intro = [(ln, s) for ln, s in d.sentences() if la <= ln <= lb]
    tops = [x for x in d.sections() if x[0] == 1]
    la = tops[0][4] if tops and la <= tops[0][4] <= lb else la      # report at the introduction's heading
    own = own_keys(d) if d.words >= 600 else []
    if own:
        # the paper has an earlier paper by the same author in its references: the introduction must set itself
        # against it in so many words (the first reason the PTRF editors gave)
        said = False
        for _, s in intro:
            if CMP.search(s) and any(k.strip() in own for m in CITE_KEYS.finditer(s) for k in m.group(1).split(",")):
                said = True
                break
        if not said:
            return [(la, "%sthe reference list has the author's own earlier work (%s) and no sentence of the "
                         "introduction says what it proved or where it stops" % (C.MUST_TAG, ", ".join(own[:4])))]
    if d.words < 1500 or len(intro) < 8:
        return []
    cited = [s for _, s in intro if "\\cite" in s]
    both = [s for s in cited if CMP.search(s)]
    if not cited:
        return [(la, "the introduction cites nothing: the reader cannot tell what was known")]
    if len(both) < 2:
        return [(la, "%d of %d introduction sentences say what a cited paper proves or where it stops (need the prior "
                     "result, why it does not give this one, and the new idea)" % (len(both), len(intro)))]
    return []


def f21(d):
    idx = C.load_own_index()
    if not idx.get("keys"):
        return []
    title = C.norm(d.title())
    me = os.path.normcase(os.path.abspath(d.path)) if d.path else ""
    here = os.path.dirname(me)
    mine = set()                       # this paper itself, another draft of it, or a file beside it
    for n, src in enumerate(idx["sources"]):
        sp = os.path.normcase(os.path.abspath(src["path"]))
        if (title and src.get("title") == title) or sp == me or (me and os.path.dirname(sp) == here):
            mine.add(n)
    out = []
    # a statement or a proof printed again, formulas included
    units = idx.get("units") or []
    runs = idx.get("runs") or {}
    if units:
        got = C.unit_matches(C.unit_list(d), lambda k: [u for u in runs.get(k, ()) if units[u][0] not in mine])
        for (ln, env, lab, ks), u, c in got[:4]:
            n, l2, env2, lab2 = units[u]
            out.append((ln, "this %s%s stands, formulas included, in %s (the %s at l.%d%s): cite it by its number there "
                            "instead of printing it again" % (
                                env, " (\\label{%s})" % lab if lab else "", "/".join(idx["sources"][n]["path"].split("/")[-3:]),
                                env2, l2, ", \\label{%s}" % lab2 if lab2 else "")))
    keys = C.sent_keys(d)
    by = {}
    for ln, s, k in keys:
        ns = idx["keys"].get(k)
        if ns is None:
            continue
        for n in ([ns] if isinstance(ns, int) else ns):
            if n not in mine:
                by.setdefault(n, []).append((ln, s))
    for n, hits in sorted(by.items(), key=lambda x: -len(x[1])):
        if len(hits) >= 5 or (len(keys) >= 40 and len(hits) >= 0.03 * len(keys)):
            src = idx["sources"][n]["path"]
            out.append((hits[0][0], "%d sentences are word for word in %s, e.g. \"%s\""
                        % (len(hits), "/".join(src.split("/")[-3:]), C.excerpt(C.plain(hits[0][1]), 70))))
    return out[:5]


GEN_TITLE = re.compile(r"\b(?:templates?|take-?aways?|road-?map|design rules?|key insights?|at a glance|sanity checks?|"
                       r"summary of (?:contributions|results|findings)|further applications and consequences|big picture|"
                       r"high-level overview|practical implications|limitations and future (?:work|directions)|"
                       r"discussion and outlook|broader (?:impact|context|picture)|intuition and heuristics|why (?:this|it) "
                       r"matters|what is new|key (?:ideas|contributions|results)|main (?:takeaways|insights)|"
                       r"putting it (?:all )?together|a closer look|deep dive|recap|in summary)\b", re.I)


def f22(d):
    secs = d.sections()
    out = [(ln, "section title \"%s\"" % C.excerpt(t, 70)) for lv, t, a, b, ln in secs if GEN_TITLE.search(t)]
    tops = [s for s in secs if s[0] == 1 and not C.DECL.search(s[1])]     # declarations are not sections of the paper
    body = d.nc[max(0, d.nc.find("\\begin{document}")):]
    pages = max(1.0, d.words / 420.0, len(body) / 3300.0)
    if len(tops) >= 10 and pages / len(tops) < 2.6:
        out.append((tops[0][4], "%d sections and appendices for about %d pages of text" % (len(tops), round(pages))))
    names = [t.lower() for _, t, _, _, _ in tops]
    if any("conclusion" in t for t in names) and any("open problem" in t or "future" in t or "outlook" in t for t in names) \
            and any("discussion" in t or "consequence" in t or "application" in t for t in names):
        out.append((tops[-1][4], "separate sections for applications, open problems and a conclusion: a mathematics paper "
                                 "ends when the proof ends"))
    return out[:5]


def f23(d):
    secs = d.sections()
    out = []
    for i, (lv, t, a, b, ln) in enumerate(secs):
        if C.DECL.search(t) or re.search(r"reference|bibliograph|notation|data availab", t, re.I):
            continue
        if i + 1 < len(secs) and secs[i + 1][0] > lv:
            continue
        if i + 1 == len(secs) and d.prose[a:b].count("\\bibliography") + len(d.bib) and b - a < 200:
            continue
        # a masked formula counts as five words: a subsection that is mostly displayed mathematics is not a stub
        w = len(re.findall(r"[A-Za-z]{2,}", C.plain(d.prose[a:b]))) + 5 * len(re.findall(r"(?<![A-Za-z])M(?![A-Za-z])", d.prose[a:b]))
        if w < 60:
            out.append((ln, "\"%s\" has %d words" % (C.excerpt(t, 50), w)))
    return out[:5]


def f25(d):
    if not d.path or not d.path.lower().endswith(".tex"):
        return []
    log = d.path[:-4] + ".log"
    try:
        if os.path.getmtime(log) + 5 < os.path.getmtime(d.path) or os.path.getsize(log) > 6000000:
            return []
        with open(log, encoding="utf-8", errors="replace") as f:
            t = f.read()
    except OSError:
        return []
    out = []
    for name, pat in (("undefined citations", r"Citation [`']([^']+)' .{0,40}undefined"),
                      ("undefined references", r"Reference [`']([^']+)' .{0,40}undefined"),
                      ("labels defined twice", r"Label [`']([^']+)' multiply defined")):
        got = sorted(set(re.findall(pat, t)))
        if got:
            out.append((0, "the log has %d %s: %s" % (len(got), name, ", ".join(got[:5]))))
    # his 2 Nov words about a posted paper: "one line is overflow ... this is not how we write paper"
    over = [(float(a), b) for a, b in re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)[^\n]*?lines? (\d+)", t)
            if float(a) > 1.0]
    if over:
        over.sort(reverse=True)
        out.append((0, "the log has %d overfull lines (text running into the margin); the worst: %s"
                    % (len(over), ", ".join("%.0fpt at source l.%s" % x for x in over[:4]))))
        # 16 Nov: an abstract placed in the preamble made every line of a short amsart paper overflow (200+ lines)
        a, b = d.raw.find("\\begin{abstract}"), d.raw.find("\\begin{document}")
        if len(over) > 30 and 0 <= a < b:
            out.append((0, "the abstract sits before \\begin{document}; move it after \\begin{document} (amsart: before "
                           "\\maketitle) - that alone makes nearly every line overflow"))
    return out


# ---------------------------------------------------------------- W51..W55 (added after the audit of 12 Nov)
FUND_SAYS = re.compile(r"\bgrants?\b|funded|funding|supported (?:in part )?by|support (?:from|of)|fellowship|"
                       r"no (?:external |specific |outside )?(?:funding|support)", re.I)
AI_HEAD = re.compile(r"declaration|use of (?:generative )?(?:ai|artificial)|\bai\b|generative|artificial intelligence|"
                     r"language models?|computational assistance", re.I)
AI_SAYS = re.compile(r"\bAI\b|language models?|Claude|GPT|Codex|artificial intelligence|generative|Anthropic|OpenAI")
AFFIL = re.compile(r"\\(?:address|affiliation|affil|institute|email|curraddr|urladdr)\b|department|universit|institut|"
                   r"laborator|college|school of", re.I)
CODE_LINE = re.compile(r"\b(?:code|data|scripts?|computations?|notebooks?|software)\b[^.]{0,160}\b(?:available|repository|"
                       r"github|zenodo|doi|archived?|deposited)\b|\b(?:github\.com|zenodo\.org|doi\.org)\b", re.I)


def f51(d):
    """What every posted paper carries (his 2 Nov order; PAPER_RULES.md): a funding statement and an AI declaration
    (MUST), the author's affiliation and a data-and-code line."""
    if d.words < 800 or application_doc(d):
        return []
    at = max(0, d.nc.find("\\begin{document}"))
    ln = d.nc_line(at)
    heads = [t for _, t, _, _, _ in d.sections()]
    heads += re.findall(r"\\(?:paragraph|subparagraph|textbf|textit|emph|textsc)\*?\{([^{}]{3,90})\}", d.nc)
    heads += re.findall(r"\\begin\{(acknowledg\w*|ack|funding|declaration\w*)\}", d.nc)
    out = []
    fund = (any(re.search(r"funding|acknowledg|thanks|support", h, re.I) for h in heads) and FUND_SAYS.search(d.nc)) or \
        re.search(r"\\thanks\{[^{}]*(?:grant|support|fund)", d.nc, re.I) or re.search(r"\\funding\b", d.nc)
    if not fund:
        out.append((ln, "%sno funding statement (a heading \"Funding\" or \"Acknowledgments\" that says who paid, or that "
                        "nobody did)" % C.MUST_TAG))
    folder = os.path.dirname(d.path) if d.path else ""
    if not (folder and os.path.exists(os.path.join(folder, "NO_AI_DECLARATION"))):
        if not (any(AI_HEAD.search(h) for h in heads) and AI_SAYS.search(d.nc)):
            out.append((ln, "%sno AI declaration (its own short section: which system produced what; a file "
                            "NO_AI_DECLARATION beside the .tex records that he said this paper carries none)" % C.MUST_TAG))
    m = re.search(r"\\author\b", d.nc)
    front = d.nc[:at + 6000]
    if not m:
        out.append((ln, "no \\author"))
    elif not AFFIL.search(front):
        out.append((ln, "the author has no affiliation or address in the front matter"))
    if not CODE_LINE.search(C.plain(d.nc[at:])):
        out.append((ln, "no line saying where the code and data are (or that the paper has none)"))
    return out


KIND = {"thm": "Theorem", "theorem": "Theorem", "lem": "Lemma", "lemma": "Lemma", "prop": "Proposition",
        "proposition": "Proposition", "cor": "Corollary", "corollary": "Corollary", "def": "Definition",
        "defn": "Definition", "definition": "Definition", "rem": "Remark", "remark": "Remark", "conj": "Conjecture"}
BYKIND = re.compile(r"\b(Theorem|Lemma|Proposition|Corollary|Definition|Remark|Conjecture)s?[~\s]*\\(?:ref|cref|autoref)\{"
                    r"(thm|theorem|lem|lemma|prop|proposition|cor|corollary|def|defn|definition|rem|remark|conj)[:._-]"
                    r"[^}]*\}", re.I)


# The label's prefix is the writer's guess at the kind; the environment the \label sits in is the kind the reader sees
# (paper16 labels a corollary prop:fs-uniform and cites it as "Corollary" correctly and as "Proposition" wrongly). So a
# label is judged by its innermost theorem-like environment, named as the paper's own \newtheorem lines name it; the
# prefix decides only for a label that is not in the file read (an \input that was not followed, an edit fragment).
STDKIND = {"theorem": "Theorem", "thm": "Theorem", "lemma": "Lemma", "lem": "Lemma", "proposition": "Proposition",
           "prop": "Proposition", "corollary": "Corollary", "cor": "Corollary", "definition": "Definition",
           "defn": "Definition", "remark": "Remark", "conjecture": "Conjecture", "conj": "Conjecture"}
WORDS52 = ("Theorem", "Lemma", "Proposition", "Corollary", "Definition", "Remark", "Conjecture")
SAID52 = re.compile(r"\b(Theorem|Lemma|Proposition|Corollar(?:y|ies)|Definition|Remark|Conjecture)s?(?=[~\s]*\\(?:ref|cref|"
                    r"autoref)\{)", re.I)
REFRUN52 = re.compile(r"(?:[~\s]|\\,|\\ )*\\(?:ref|cref|autoref)\{[^}]*\}(?:(?:\s*,\s*|\band\b|~|\s)+"
                      r"\\(?:ref|cref|autoref)\{[^}]*\}){0,6}")
REF52 = re.compile(r"\\(?:ref|cref|autoref)\{([^}]*)\}")
PFX52 = re.compile(r"(thm|theorem|lem|lemma|prop|proposition|cor|corollary|def|defn|definition|rem|remark|conj)[:._-]", re.I)


def _env_kinds(src):
    """env name -> the word it prints, from the paper's own declarations (the class defaults when it has none)."""
    m = {}
    for g in re.finditer(r"\\(?:newtheorem|spnewtheorem)\*?\{(\w+)\}(?:\[[^\]]*\])?\{([^}]*)\}", src):
        m[g.group(1)] = g.group(2).strip()
    for g in re.finditer(r"\\declaretheorem\[([^\]]*)\]\{(\w+)\}", src):
        n = re.search(r"name\s*=\s*\{?([A-Za-z ]+)", g.group(1))
        m[g.group(2)] = n.group(1).strip() if n else g.group(2).capitalize()
    for g in re.finditer(r"\\declaretheorem\{(\w+)\}", src):
        m.setdefault(g.group(1), g.group(1).capitalize())
    for k, v in STDKIND.items():
        m.setdefault(k, v)
    return m


def label_kinds(d):
    """label -> the kind word of its innermost theorem-like environment; built once per Doc."""
    got = getattr(d, "_label_kinds52", None)
    if got is not None:
        return got
    src, names, out, stack = d.nc, None, {}, []
    names = _env_kinds(src)
    for m in re.finditer(r"\\begin\{([^}]*)\}|\\end\{([^}]*)\}|\\label\{([^}]*)\}", src):
        if m.group(1):
            stack.append(m.group(1))
        elif m.group(2):
            if m.group(2) in stack:
                while stack and stack.pop() != m.group(2):
                    pass
        elif stack:
            e = stack[-1]
            k = names.get(e, names.get(e.rstrip("*")))
            if k:
                out.setdefault(m.group(3).strip(), k)
    d._label_kinds52 = out
    return out


def f52(d):
    out, kinds = [], None
    for m in SAID52.finditer(d.nc):
        r = REFRUN52.match(d.nc, m.end())
        if not r:
            continue
        said = m.group(1).capitalize()
        said = "Corollary" if said.startswith("Corollar") else said
        if kinds is None:
            kinds = label_kinds(d)
        for lab in REF52.findall(r.group(0)):
            for one in lab.split(","):
                one = one.strip()
                real = kinds.get(one)
                if real is None:
                    p = PFX52.match(one)
                    real = KIND.get(p.group(1).lower()) if p else None
                    how = "a label named as a %s"
                else:
                    how = "a label that sits in a %s"
                if not real or said.lower() in real.lower().split() or real.split()[-1] not in WORDS52:
                    continue
                out.append((d.nc_line(m.start()), ("\"%s\" in front of " + how + ": %s")
                            % (said, real.lower(), C.excerpt(d.nc[m.start(): r.end()], 70))))
    return out[:6]


def f53(d):
    return [(d.nc_line(m.start()), "the finished grant is named: %s" % C.excerpt(d.nc[max(0, m.start() - 40): m.end() + 10], 80))
            for m in re.finditer(r"OISE[-\s~]*2401227|2401227", d.nc)][:3]


COMMENT_SAYS = re.compile(r"\b(?:TODO|FIXME|XXX)\b|\b(?:Claude|Codex|ChatGPT|GPT-?\d|Gemini|LLM|subagents?|referee agents?|"
                          r"audit(?:or|ed|s)?|AI[- ](?:generated|written|tells?))\b|sound(?:s|ing)? (?:more )?human|"
                          r"human[- ]voice|(?:first|earlier|previous|old) (?:version|draft)|was (?:corrected|wrong|fixed)|"
                          r"fixed (?:in|after|on)|his (?:order|words|rule)|owner", re.I)


def f54(d):
    """Comments ship with the arXiv and GitHub source. One that talks about the process is read by whoever opens it."""
    out = []
    for i, raw in enumerate(d.raw.split("\n"), 1):
        m = C.COMMENT.search(raw)
        if m and len(m.group(0)) > 6 and COMMENT_SAYS.search(m.group(0)):
            out.append((i, "in a comment of the source: %s" % C.excerpt(m.group(0), 90)))
    return out[:6]


HIST = re.compile(
    r"\b(?:original|previous|earlier|prior|first|initial|preliminary|revised|current|final|arxiv|posted) (?:submission|"
    r"version|draft|manuscript|preprint|write-?up)s?\b|"
    r"\b(?:submission|draft|manuscript|preprint|exposition|presentation|write-?up|text) (?:has been|have been|was|were|is now|"
    r"now|asserted|claimed|stated|contained)\b|"
    r"\b(?:referees?|reviewers?|colleagues?|readers?) (?:of|asked|pointed|suggested|noticed|observed|remarked|requested|"
    r"found|raised)\b|"
    r"\bliterature search|\bin hindsight\b|\bon (?:re-?examination|reflection|closer inspection)\b|\bsupersedes?\b|"
    r"\b(?:update|note added|erratum|correction)\s*:|"
    r"\b(?:has|have) (?:since )?been (?:streamlined|rewritten|reorgani[sz]ed|shortened|expanded|corrected|revised|updated|"
    r"repaired|removed|replaced|added)\b|"
    r"\b(?:were|was|been) (?:cross-?checked|double-?checked|re-?checked|re-?verified|re-?derived|caught|repaired|audited)\b|"
    r"\b(?:first|second|third|final|another) (?:pass|round|reading|audit)\b|\bmachine assistance\b|"
    r"\bnow (?:holds|reads|credits|states|cites|gives|covers)\b|\bto (?:our|my) knowledge\b[^.]{0,80}\b(?:print|literature|"
    r"exist|appear)", re.I)


def f55(d):
    """A wide net for sentences about the paper's own history. Each hit is read, not obeyed: some are ordinary."""
    skip = d.ack_lines()
    out = []
    for ln, s in d.sentences():
        if ln in skip:
            continue
        m = HIST.search(s)
        if m:
            out.append((ln, "\"%s\" in: %s" % (m.group(0), C.excerpt(C.plain(s), 100))))
    return out[:8]


def f26(d):
    # with every \input file read in, the labels are all here; when one is missing (or the text was never expanded)
    # a label may live in the part that was not read
    if d.unresolved or d.cut or (d.unresolved is None and re.search(r"\\(?:input|include|subfile|import)\b", d.nc)):
        return []
    labels = set(re.findall(r"\\label(?:\[[^\]]*\])?\{([^}]+)\}", d.nc))   # cleveref: \label[lemma]{key}
    out, seen = [], set()
    for m in re.finditer(r"\\(?:ref|eqref|cref|Cref|autoref|pageref)\*?\{([^}]+)\}", d.nc):
        for k in m.group(1).split(","):
            k = k.strip()
            if k and k not in labels and k not in seen:
                seen.add(k)
                out.append((d.nc_line(m.start()), "\\ref{%s} points at no label" % k))
    if d.bib:
        items = set(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", d.nc))
        for m in re.finditer(r"\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]*)\}", d.nc):
            for k in m.group(1).split(","):
                k = k.strip()
                if k and k not in items and k not in seen:
                    seen.add(k)
                    out.append((d.nc_line(m.start()), "\\cite{%s} is not in the reference list" % k))
    return out[:6]


I_VERB = re.compile(r"(?<![A-Za-z.\\])I (?:prove|show|thank|am|will|have|use|do|would|give|consider|believe|claim|find|note|"
                    r"obtain|was|construct|define|recall|conjecture|expect)\b")
WE_VERB = re.compile(r"\b[Ww]e (?:prove|show|use|give|consider|obtain|note|have|will|find|construct|define|recall|"
                     r"conjecture|expect)\b")


def f27(d):
    skip = d.decl_lines()
    i_hits = [(i, C.excerpt(ln[max(0, m.start() - 30): m.end() + 50])) for i, ln in enumerate(d.lines, 1)
              if i not in skip for m in [I_VERB.search(ln)] if m]
    if i_hits and any(WE_VERB.search(ln) for ln in d.lines):
        return [(i_hits[0][0], "\"I\" here and \"we\" elsewhere: " + i_hits[0][1])]
    return []


def f29(d):
    out = []
    for ln, s in d.sentences():
        w = len(C.plain(s).split())
        if w > 45:
            out.append((w, ln, s))
    if len(out) < 3:
        return []
    # one line for the whole paper: a line per sentence buried everything else under it on every paper
    out.sort(reverse=True)
    w, ln, s = out[0]
    return [(ln, "%d sentences over 45 words; the longest are at l.%s; this one has %d: %s" % (
        len(out), ", ".join(str(d.src(x[1])[1]) for x in out[:5]), w, C.excerpt(C.plain(s), 70)))]


OPENER = re.compile(r"^(?:Moreover|Furthermore|Additionally|Importantly|Notably|Specifically|Overall|In summary|"
                    r"In conclusion|Crucially|Interestingly|That said|In essence|Taken together|Collectively|"
                    r"Consequently|Ultimately|Simply put|Put differently|To summarize|In short)\b")


def f30(d):
    sents = d.sentences()
    hits = [(ln, C.excerpt(C.plain(s), 70)) for ln, s in sents if OPENER.match(C.plain(s))]
    if len(hits) >= max(6, len(sents) / 30.0):
        return [(hits[0][0], "%d of %d sentences open with Moreover / Furthermore / Additionally / Specifically ..."
                 % (len(hits), len(sents)))] + hits[:1]
    return []


def f31(d):
    hits = C.line_hits(d, u"(?<!-)---(?!-)|\u2014", None, 0)
    n = len(re.findall(u"(?<!-)---(?!-)|\u2014", d.prose))
    if n >= max(6, d.words / 450.0):
        return [(hits[0][0], "%d em dashes in about %d words" % (n, d.words))] + hits[:1]
    return []


def f33(d):
    hits = C.line_hits(d, P33)
    if len(hits) >= max(6, d.words / 700.0):
        return [(hits[0][0], "%d signposts in about %d words" % (len(hits), d.words))] + hits[:2]
    return []


def f34(d):
    t = d.title()
    if not t:
        return []
    m = re.search(r"\\title", d.nc)
    ln = d.nc_line(m.start()) if m else 1
    w = len(t.split())
    out = []
    if w > 14:
        out.append((ln, "the title has %d words: \"%s\"" % (w, C.excerpt(t, 90))))
    elif t.count(",") >= 2:
        out.append((ln, "the title is a list: \"%s\"" % C.excerpt(t, 90)))
    if re.search(r"\b(?:novel|towards?|on the way to|a (?:new|unified|general) (?:framework|approach|perspective))\b", t,
                 re.I):
        out.append((ln, "the title advertises instead of naming the theorem: \"%s\"" % C.excerpt(t, 90)))
    return out


def f35(d):
    if d.words < 2500:
        return []
    start = d.prose.find("\\begin{document}")
    start = 0 if start < 0 else start
    m = re.search(r"\\begin\{(\w*(?:theorem|thm|theo|mainthm)\w*)\}(.*?)\\end\{\1\}", d.prose[start:], re.S | re.I)
    if not m:
        return [(1, "no theorem environment in a paper of about %d words" % d.words)]
    out = []
    frac = m.start() / float(max(1, len(d.prose) - start))
    ln = d.line_of(start + m.start())
    if frac > 0.30:
        out.append((ln, "the first theorem is stated %d%% of the way into the paper" % round(100 * frac)))
    w = len(C.plain(m.group(2)).split())
    if w > 170:
        out.append((ln, "the first theorem's statement runs to %d words" % w))
    return out


def f36(d):
    first, again = {}, {}
    for ln, s, k in C.sent_keys(d, 10):
        if k in first and first[k][0] != ln:
            again.setdefault(k, []).append(ln)
        first.setdefault(k, (ln, s))
    if sum(len(v) for v in again.values()) < 3:
        return []
    out = []
    for k, lns in sorted(again.items(), key=lambda kv: -len(kv[1]))[:12]:
        ln0, s = first[k]
        out.append((lns[0], "the sentence at l.%d stands %d more time%s (l.%s): %s" % (
            ln0, len(lns), "" if len(lns) == 1 else "s", ", ".join(str(x) for x in lns[:4]),
            C.excerpt(C.plain(s), 70))))
    return out


UNRETR = re.compile(r"\bin preparation\b|\bprivate communication\b|\bpersonal communication\b|\bunpublished\b|"
                    r"\bmanuscript\b|\bsubmitted\b|\bforthcoming\b|\bwork in progress\b|\bto be published\b", re.I)
RETR = re.compile(r"arxiv|doi|https?://|zenodo|hal-|\\url|\\href|eprint", re.I)


def f37(d):
    out = []
    for m in re.finditer(r"(?:\\bibitem|^@\w+\s*\{)(?:(?!\\bibitem|^@\w+\s*\{).)*", d.nc, re.S | re.M):
        item = m.group(0)
        u = UNRETR.search(item)
        if u and not RETR.search(item):
            out.append((d.nc_line(m.start()), "a reference nobody can look up (\"%s\"): %s"
                        % (u.group(0), C.excerpt(C.plain(item), 80))))
    return out[:5]


# ---------------------------------------------------------------- the table
# ---------------------------------------------------------------- W57..W66: "the author has read the paper" (17 Nov)
# Most papers that go out have not been read by the author: they carry the standing sentence, unless the author
# named the paper as one being made ready for a journal.
# A paper he named carries a file AUTHOR_READ_OK beside its .tex holding the date and his words naming it. Every other
# paper carries the standing sentence and no claim that he read, checked or verified it.
READ_OK = ("AUTHOR_READ_OK", "AUTHOR_READ_OK.txt", "AUTHOR_READ_OK.md")
STANDING = ("The author directed the work and is responsible for the content of the paper and for decisions concerning "
            "its dissemination.")
_NOTAI = (r"(?:(?!Claude|Codex|GPT|Gemini|models?\b|agents?\b|systems?\b|who\b|whom\b|whose\b|thank\w*|grateful|acknowledg\w*|referees?\b|reviewers?\b|"
          r"colleagues?\b)"
          r"(?:\b[A-Z]\.(?=\s)|[^.;]))")  # an initial ("A. B.") does not end the sentence
# 18 Nov: "the authors of [5] verified the conjecture" is someone else's check, not the author's.
_AUTH = r"(?<!\bits\s)(?<!\btheir\s)(?<!\bwhose\s)\bauthors?\b(?!\s+(?:of|in)\s+(?!this\b|the\s+present\b|the\s+current\b))(?!\s*~?\\cite)"
A_READ = re.compile(
    _AUTH + _NOTAI + r"{0,120}?\b(?:has\s+|have\s+|had\s+)?read\s+(?:through\s+)?(?:the|all|every|each|this|it\b)"
    r"[^.;]{0,40}|\bread\s+(?:and\s+\w+\s+)?by\s+the\s+authors?\b|"
    r"(?<![A-Za-z.\\])I\s+(?:have\s+)?read\s+(?:the|all|every|each)\b[^.;]{0,40}\b(?:proofs?|paper|manuscript)", re.I)
# 18 Nov: "the author ... reviewed the mathematics" was missed (no noun), and "the author set the objective of extending
# the verified capacity results" fired on an adjective; the verb must not follow an article, and the nouns include the
# mathematics itself (a recall pass over 42 papers).
_ADJ = r"(?<!\bthe\s)(?<!\ba\s)(?<!\ban\s)"
_WHAT = (r"\b(?:papers?|(?:all\s+of\s+)?the\s+above|proofs?|manuscript|arguments?|content|text|results?|steps?|statements?|computations?|mathematics|"
         r"maths?|theory|derivations?|calculations?|analysis)\b")
A_CHECK = re.compile(
    _AUTH + _NOTAI + r"{0,120}?\b" + _ADJ + r"(?:has\s+|have\s+|had\s+)?(?:checked|verified|reviewed|proofread|"
    r"examined|validated|confirmed|went\s+through|gone\s+through)\b[^.;]{0,70}" + _WHAT + r"|\b(?:checked|verified|"
    r"reviewed|proofread)\s+(?:and\s+\w+\s+)?by\s+the\s+authors?\b", re.I)


A_STRONG = re.compile(
    _AUTH + _NOTAI + r"{0,120}?\b" + _ADJ + r"(?:has\s+|have\s+|had\s+)?(?:checked|verified|proofread|examined|"
    r"validated|confirmed|went\s+through|gone\s+through)\b[^.;]{0,70}" + _WHAT + r"|\b(?:checked|verified|proofread)\s+"
    r"(?:and\s+\w+\s+)?by\s+the\s+authors?\b", re.I)


def read_ok_file(path):
    """The marker beside the .tex (or one folder up, for a paper kept in a paper/ subfolder), or ''."""
    if not path:
        return ""
    folder = os.path.dirname(path)
    up = os.path.dirname(folder) if os.path.basename(folder).lower() in ("paper", "tex", "latex", "src", "manuscript") else ""
    for f in (folder, up):
        for n in READ_OK:
            p = os.path.join(f, n)
            if f and os.path.isfile(p):
                return p
    return ""


def named(path):
    """He named this paper: the record is there and holds a date and his words."""
    mk = read_ok_file(path)
    return bool(mk and read_ok_good(mk))


def read_ok_good(marker):
    """A marker counts when it holds a date and at least a few of his words; a bare touched file does not."""
    try:
        t = open(marker, encoding="utf-8", errors="replace").read()
    except OSError:
        return False
    return bool(re.search(r"20\d\d", t)) and len(re.findall(r"[A-Za-z]{2,}", t)) >= 6


def _claims(d, pat):
    out, seen = [], set()
    try:
        sents = list(d.sentences())
    except Exception:
        sents = []
    if not sents:
        sents = [(i, l) for i, l in enumerate(d.nc.split("\n"), 1)]
    for ln, sn in sents:
        m = pat.search(C.plain(sn))
        if m and ln not in seen:
            seen.add(ln)
            out.append((ln, C.excerpt(C.plain(sn), 110)))
    return out


def f57(d):
    if named(d.path):
        return []
    return [(ln, "says the author read it, and he has not named this paper: %s" % ex) for ln, ex in _claims(d, A_READ)][:5]


def f58(d):
    if named(d.path):
        return []
    strong = _claims(d, A_STRONG)
    hard = set(ln for ln, _ in strong)
    out = [(ln, C.MUST_TAG + "says the author checked or verified it, and he has not named this paper: %s" % ex)
           for ln, ex in strong]
    out += [(ln, "says the author reviewed it (the publishers' \"reviewed and edited by the author\" too); in a paper "
                 "going out now that he has not read, write the standing sentence instead: %s" % ex)
            for ln, ex in _claims(d, A_CHECK) if ln not in hard]
    return out[:5]


CREDIT = re.compile(r"education[\s~]+credits?[\s~]+program(?:me)?", re.I)


def f73(d):
    """W73 (18 Nov 2026): the cloud education-credits sentence comes out of the papers."""
    out, seen = [], set()
    for m in CREDIT.finditer(d.nc):
        ln = d.nc_line(m.start())
        if ln in seen or (ln - 1) in seen:  # the number and the phrase sit in one sentence: report it once
            continue
        seen.add(ln)
        out.append((ln, "the Google Cloud education-credits sentence: %s"
                    % C.excerpt(d.nc[max(0, m.start() - 90): m.end() + 20], 120)))
    return out[:3]


def f59(d):
    mk = read_ok_file(d.path)
    if mk and not read_ok_good(mk):
        return [(1, "%s is empty or carries no date and none of his words: write the date and the words in which he named "
                    "this paper, or delete the file and the sentence" % mk.replace("\\", "/"))]
    return []


def f60(d):
    mk = read_ok_file(d.path)
    if not (mk and read_ok_good(mk)) or d.words < 800:
        return []
    if _claims(d, A_READ):
        return []
    return [(1, "he named this paper (%s) and no sentence says he read it: add it to the AI declaration at the end "
                "(never the abstract or introduction)" % os.path.basename(mk))]


def f61(d):
    mk = read_ok_file(d.path)
    if not mk or not d.path or not os.path.exists(d.path):
        return []
    try:
        late = os.path.getmtime(d.path) - os.path.getmtime(mk)
    except OSError:
        return []
    if late > 3600 and _claims(d, A_READ):
        return [(1, "the .tex changed %.0f h after %s was written: he read an earlier text, so tell him in one line what "
                    "changed since, and write the new date into the file when he has seen it"
                 % (late / 3600.0, os.path.basename(mk)))]
    return []


SIDE = ("README*", "readme*", "rg_description*", "*description*.txt", "*cover*letter*", "*cover_letter*", "zenodo*.md",
        "zenodo*.txt", "zenodo*.json", ".zenodo.json", "abstract*.txt", "ABSTRACT*")


def f62(d):
    """The same claim on the hosting page, the README or the cover letter is made in his name as much as in the paper."""
    if not d.path or not d.whole or named(d.path):
        return []
    folder = os.path.dirname(d.path)
    if not folder:
        return []
    out, seen = [], set()
    for f in (folder,):
        for pat in SIDE:
            for p in glob.glob(os.path.join(f, pat))[:6]:
                if p in seen or not os.path.isfile(p) or os.path.getsize(p) > 400000:
                    continue
                seen.add(p)
                try:
                    t = open(p, encoding="utf-8", errors="replace").read()
                except OSError:
                    continue
                m = A_READ.search(t) or A_STRONG.search(t)
                if m:
                    out.append((1, "%s says it too: %s" % (os.path.basename(p), C.excerpt(m.group(0), 90))))
    return out[:4]


def _read_state(ctx):
    """[(name, has marker, claims in the .tex)] for the whole documents of this call."""
    rows = []
    for d in [x for x in ctx.get("docs") or [] if x.whole and x.path][:4]:
        mk = read_ok_file(d.path)
        n = len(_claims(d, A_READ)) + len(_claims(d, A_CHECK))
        rows.append((os.path.basename(os.path.dirname(d.path)) + "/" + os.path.basename(d.path), bool(mk and read_ok_good(mk)), n))
    return rows


def c64(ch, p, ctx):
    bad = ["%s (%d sentences)" % (n, k) for n, ok, k in _read_state(ctx) if k and not ok]
    return ("a paper he has not named says he read or checked it: %s. Replace each with: \"%s\"" % ("; ".join(bad), STANDING)) \
        if bad else None


def c65(ch, p, ctx):
    rows = _read_state(ctx)
    if not rows:
        return ("the .tex is not known from this call; before it is submitted, a paper that says he read it has "
                "AUTHOR_READ_OK beside it with the date and his words")
    out = []
    for n, ok, k in rows:
        if k and not ok:
            out.append("%s says he read it and has no AUTHOR_READ_OK: take the sentence out, or ask him by email" % n)
        elif ok and k:
            out.append("%s: he named it; the email that goes with it says the sentence is a statement in his name" % n)
        elif ok and not k:
            out.append("%s: he named it and the sentence is missing" % n)
    return "; ".join(out) or None


def _fitz():
    """PyMuPDF, or None. Hooks run "python -s", which leaves out the user site where it lives; try that once."""
    try:
        import fitz
        return fitz
    except ImportError:
        import site
        site.addsitedir(site.getusersitepackages())
        try:
            import fitz
            return fitz
        except ImportError:
            return None


def c66(ch, p, ctx):
    """The compiled pages: a claim that sits in an \\input file, a macro or the title page is in the PDF and not in main.tex."""
    out, unread = [], []
    for d in [x for x in ctx.get("docs") or [] if x.whole and x.path][:3]:
        if named(d.path):
            continue
        pdf = d.path[:-4] + ".pdf"
        if not os.path.isfile(pdf) or os.path.getsize(pdf) > 30000000:
            continue
        fitz = _fitz()
        if fitz is None:
            unread.append("%s (PyMuPDF is not importable)" % os.path.basename(pdf))
            continue
        try:
            t = re.sub(r"\s+", " ", " ".join(pg.get_text() for pg in fitz.open(pdf)))
        except Exception as e:
            unread.append("%s (%s)" % (os.path.basename(pdf), type(e).__name__))
            continue
        m = A_READ.search(t) or A_CHECK.search(t)
        if m:
            out.append("%s: \"%s\"" % (os.path.basename(pdf), C.excerpt(m.group(0), 90)))
    msg = []
    if out:
        msg.append("the compiled PDF of a paper he has not named says he read or checked it - %s" % "; ".join(out))
    if unread:
        msg.append("the compiled PDF was NOT read, so this check did not run: %s" % "; ".join(unread))
    return ". ".join(msg) or None



# ---------------------------------------------------------------- W67..W72: the private record of submissions (17 Nov)
# A private record of where each paper was submitted and when, and whether it is still in process, so that no
# paper is submitted twice. The folder holds submissions.py and SUBMISSIONS.jsonl.
SUB_DIR = (os.environ.get("PW_SUBMISSIONS_DIR") or os.path.expanduser("~/.claude/paper_submissions")).replace("\\", "/")
# The tool itself: the private folder's copy when there is one, else the copy shipped beside these hooks.
SUB_CODE = SUB_DIR if os.path.isfile(os.path.join(SUB_DIR, "submissions.py")) else \
    os.path.join(HERE, "paper_submissions").replace("\\", "/")
SUB_TOOL = "python " + SUB_CODE + "/submissions.py"
TITLE = re.compile(r"\\title\s*(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}")


def _subs():
    """(the submissions module, its rows) or (None, [])."""
    try:
        if SUB_CODE not in sys.path:
            sys.path.insert(0, SUB_CODE)
        import submissions as S
        return S, S.load(os.environ.get("PW_SUBMISSIONS") or None)
    except Exception:  # noqa: BLE001
        return None, []


def _titles(ctx):
    out = []
    for d in [x for x in ctx.get("docs") or [] if x.whole][:3]:
        m = TITLE.search(d.nc)
        if m:
            t = re.sub(r"\s+", " ", C.plain(re.sub(r"\\(?:thanks|footnote)\s*\{[^{}]*\}", " ", m.group(1)))).strip()
            if len(t) > 8:
                out.append(t)
    return out


def _short(r):
    return "%s at %s%s (%s, %s)" % (r.get("title", "?")[:46], r.get("journal", "?")[:34], (" " + r["ms_id"]) if r.get("ms_id") else "",
                                   r.get("status", "?"), r.get("submitted") or "no date")


def c67(ch, p, ctx):
    S, rows = _subs()
    if S is None:
        return "the submissions tool could not be loaded (%s/submissions.py): find out why before anything is submitted" % SUB_CODE
    out = []  # an empty record is a fresh install: every paper is a first submission
    for t in _titles(ctx):
        op, cl = S.verdict(rows, t)
        if op:
            out.append("STOP: \"%s\" matches a row that is open - %s. If it is this paper it goes nowhere else until that "
                       "journal decides or the author withdraws it" % (t[:60], "; ".join(_short(r) for r in op[:3])))
        elif cl:
            out.append("\"%s\" is free on this record; it does not go again to: %s"
                       % (t[:60], ", ".join(sorted(set(r.get("journal", "?") for r in cl)))))
        else:
            out.append("\"%s\" has no row: a first submission. Record it the minute it goes through" % t[:60])
    if out:
        return "; ".join(out)
    op = [r for r in rows if r.get("status") in S.OPEN]
    if not op:
        return "nothing is open on the record. After the submission goes through: %s add --title \"...\" --journal \"...\"" \
               " --date <day>" % SUB_TOOL
    names ="; ".join("%s @ %s" % (r.get("title", "?")[:34], r.get("journal", "?")[:26]) for r in op[:16])
    return "%d rows are open now: %s. Before this one: %s check \"<title>\"" % (len(op), names, SUB_TOOL)


def c70(ch, p, ctx):
    S, rows = _subs()
    dr = [r for r in rows if r.get("status") == "draft_started"]
    return ("%d drafts were started in journal systems and never finished: %s. Each is finished or deleted in that system "
            "and its row closed (status <row> draft_deleted)" % (len(dr), "; ".join(
                "%s %s @ %s" % (r.get("rid"), r.get("title", "?")[:30], r.get("journal", "?")[:30]) for r in dr[:6]))) if dr else None


def c71(ch, p, ctx):
    S, rows = _subs()
    if S is None:
        return None
    old = []
    for r in rows:
        if r.get("status") in S.OPEN:
            try:
                age = (datetime.date.today() - datetime.date.fromisoformat(str(r.get("checked"))[:10])).days
            except ValueError:
                age = 999
            if age > 30:
                old.append((age, r))
    old.sort(key=lambda x: -x[0])
    return ("%d open rows have not been looked at for a month: %s. Read the author's mail and the journal's page, then write the "
            "status, or `looked <row>` when nothing moved" % (len(old), "; ".join(
                "%s %s @ %s (%d d)" % (r.get("rid"), r.get("title", "?")[:28], r.get("journal", "?")[:24], a) for a, r in old[:5]))) if old else None


def c72(ch, p, ctx):
    d = ctx.get("dir") or ""
    if not d or os.path.normcase(os.path.abspath(d)).startswith(os.path.normcase(os.path.abspath(SUB_DIR))):
        return None
    try:
        hit = [f for f in os.listdir(d) if re.match(r"(?i)submissions?[._-]|submission_(?:log|record|history)|where_submitted", f)]
    except OSError:
        return None
    return ("%s holds %s: where a paper was sent and what a journal answered stay in the private record, not beside the "
            "paper" % (os.path.basename(d.rstrip("/\\")), ", ".join(hit[:3]))) if hit else None



def T(i, kind, title, rule, must=False, **kw):
    h = {"id": "W%02d" % i, "kind": kind, "title": title, "rule": rule, "must": must}
    h.update(kw)
    return h


TEXT = [
    T(1, "line", "the paper is the subject of the sentence",
      "delete the sentence, or state the mathematics it stands for; a paper states theorems, it does not describe itself "
      "(his 15 Sep and 11 Nov orders; the PTRF referee quoted one of these)", True, pat=P01, skip_decl=True),
    T(2, "line", "the manuscript's own history",
      "a paper has no earlier versions inside it; a corrected citation simply appears", True, pat=P02, skip_ack=True),
    T(3, "line", "the search is narrated",
      "attribution is one neutral clause in the present tense (\"introduced by X [4], who ...\"); never what was looked "
      "for and not found", True, pat=P03, skip_decl=True),
    T(4, "line", "a model, an agent or a session is named outside the declaration",
      "the AI declaration is the only place the process is named, in one short factual record", fn=f04, tagged=True),
    T(5, "line", "checking is narrated",
      "say what is proved; how often it was checked belongs nowhere in a paper (a computer-assisted step names the "
      "computation and where the code is)", True, pat=P05, skip_ack=True),
    T(6, "line", "a defensive aside",
      "state the claim and its hypotheses; cut \"to be clear\", \"honest\", \"we do not claim\", \"for transparency\"", True,
      pat=P06, skip_decl=True),
    T(7, "line", "a word that reads as machine-written",
      "use the plain word or cut the sentence (remarkably, notably, delve, "
      "crucially, sheds light, underscores)", pat=P07, skip_decl=True),
    T(8, "line", "a slogan where a statement belongs",
      "replace it with the displayed inequality or the theorem it gestures at", pat=P08),
    T(9, "line", "more is promised than is proved",
      "say exactly what the theorem gives and under which hypotheses; \"explain exactly\", \"for the first time\" need a "
      "proof or a citation behind them", pat=P09),
    T(10, "line", "\"clearly\", \"obviously\", \"it is easy to see\"",
      "give the one-line reason or cite it; a referee stops at each of these", pat=P10, min=4),
    T(11, "line", "\"well known\" or \"standard\" with no reference",
      "name the theorem and cite where it is proved, with the theorem number", fn=f11),
    T(12, "line", "many references in one bracket",
      "say in a clause what each cited paper does, or cite the two that matter; a block of five as \"background\" tells "
      "the reader nothing", fn=f12),
    T(13, "line", "an emoji, a star, a check mark, an exclamation mark, or the word \"headline\"",
      "remove it", True, fn=f13),
    T(14, "doc", "bold type everywhere",
      "keep bold for theorem heads; emphasis comes from the order of the sentences", fn=f14),
    T(15, "doc", "the abstract's shape",
      "one paragraph of plain sentences: the object, the theorem with its constant, what it improves; no list, no "
      "citation, under 200 words", fn=f15),
    T(16, "doc", "a label of our own, used before it is defined",
      "the first time a name of ours appears, define it in that sentence or the next, or show the estimate itself; the "
      "PTRF referee: \"written in terms of jargon that is not explained in the introduction\"", fn=f16),
    T(17, "doc", "one object under several names",
      "one name per object, everywhere: section titles, appendix titles and running text (a referee's complaint)", fn=f17),
    T(18, "doc", "the same formula defined again and again",
      "define it once, number it, and refer to the number", fn=f18),
    T(19, "doc", "the novelty is not set against earlier work",
      "the introduction says, with citations: what was proved before, why that proof does not give this theorem, and the "
      "one new idea, shown as a displayed estimate", fn=f19),
    T(20, "line", "a change-log sentence",
      "\"these additions\", \"new in this version\", \"a section has been added\" describe an edit; write what the estimate is and "
      "why the earlier argument fails without it", True, pat=P20, skip_ack=True),
    T(21, "doc", "sentences reused from his earlier papers",
      "cite the earlier lemma by number instead of reprinting it; a referee who finds an old lemma verbatim concludes the "
      "paper is the old one again (PTRF, 11 Nov 2026)", True, fn=f21),
    T(22, "doc", "the outline looks generated",
      "a mathematics paper has an introduction, preliminaries, the proofs, and at most a short closing section; cut "
      "\"template\", \"design rule\", \"takeaways\", and fold one-page sections into their neighbours", fn=f22),
    T(23, "doc", "stub sections",
      "a section of a few lines is a remark: fold it in or cut it", fn=f23, min=2),
    T(24, "line", "a placeholder is still in the text",
      "finish it or remove it before anyone else reads the file", True, pat=P24),
    T(25, "doc", "the LaTeX log reports undefined citations or references",
      "fix every one and compile twice; the PDF shows [?] and ?? where these are", True, fn=f25),
    T(26, "doc", "a reference or citation that points nowhere",
      "add the label or the reference, or remove the pointer", True, fn=f26),
    T(27, "doc", "\"I\" and \"we\" mixed",
      "choose one voice for the whole paper", fn=f27),
    T(28, "line", "filler",
      "cut \"in order to\", \"the fact that\", \"it is worth noting that\", \"plays a key role\"; his 1 Nov words: less wordy, "
      "stronger and more to the point", pat=P28, min=3),
    T(29, "line", "sentences too long to follow",
      "one statement per sentence; split at the second \"which\" or \"and\"", fn=f29),
    T(30, "doc", "sentences opening with Moreover, Furthermore, Additionally",
      "let the mathematics order the sentences; most of these openers can simply go", fn=f30),
    T(31, "doc", "em dashes",
      "use a comma, a colon or two sentences", fn=f31),
    T(32, "line", "\"not only ... but\", \"is not X; it is Y\"",
      "say what it is; the contrast with something nobody claimed reads as machine prose", pat=P32, min=3),
    T(33, "doc", "signposting",
      "one paragraph at the end of the introduction says where things are; after that, state and prove", fn=f33),
    T(34, "doc", "the title",
      "a title names the theorem's object in under about twelve words; three things joined by commas is a table of "
      "contents", fn=f34),
    T(35, "doc", "where and how the main theorem is stated",
      "the main theorem stands in the first pages, in one statement a reader can quote", fn=f35),
    T(36, "doc", "the paper repeats itself",
      "say it once; a restated theorem is restated by reference to its number", fn=f36),
    T(37, "line", "a reference nobody can look up",
      "post the cited manuscript (arXiv or Zenodo) and cite that, or remove the citation; \"Manuscript, 2026\" and \"in "
      "preparation\" cannot be checked by a referee", fn=f37, bib=True),
    T(38, "line", "praise of our own result",
      "let the theorem and the comparison with earlier bounds do it; cut novel, powerful, elegant, surprising", pat=P38,
      min=3, skip_decl=True),
    T(51, "doc", "what every posted paper carries",
      "a funding statement, an AI declaration in its own short section, the author's affiliation, and a line saying "
      "where the code and data are (his 2 Nov order: \"it does not include funding statement, or AI acknowledgment, "
      "this is not how we write paper\")", fn=f51),
    T(52, "line", "a lemma cited as a theorem",
      "write the kind the statement has: Lemma~\\ref{lem:...}, Proposition~\\ref{prop:...}; or use \\cref and let the "
      "label decide", fn=f52),
    T(53, "line", "a finished grant in the funding line",
      "funding lists current support only; NSF OISE-2401227 has ended and is never named", True, fn=f53),
    T(54, "line", "a comment in the source that talks about the process",
      "delete it: the .tex is public on arXiv and GitHub, and a comment about a model, an audit, an earlier draft or "
      "how the text should sound is read by whoever opens the source", True, fn=f54),
    T(55, "line", "a sentence about the paper's own history (read each one)",
      "a wide net, so some hits are ordinary; where the sentence tells what was changed, checked, asked for or found "
      "out along the way, delete it or state the mathematics", fn=f55),
    T(57, "line", "\"the author has read the paper\" in a paper he has not named",
      "delete the sentence and keep the standing one: \"" + STANDING + "\" He has not read most papers that go out. The "
      "sentence stays only when a file AUTHOR_READ_OK beside the .tex holds the date and his words naming this paper",
      True, fn=f57),
    T(58, "line", "\"the author checked / verified the proofs\" in a paper he has not named",
      "the same rule as W57: nothing is said in his name that he did not do. Say which system checked what, and that "
      "the author directed the work and is responsible for it. \"Checked\", \"verified\" and \"proofread\" are a MUST; "
      "the publishers' template \"reviewed and edited by the author\" is reported", fn=f58),
    T(59, "doc", "an AUTHOR_READ_OK file with nothing in it",
      "the file is a record, not a switch: it holds the date and his own words naming this paper; no agent writes it "
      "on its own judgment", True, fn=f59),
    T(60, "doc", "a paper he named that does not say he read it",
      "for a paper he asked to be made ready for a journal, the sentence that the author has read the paper and the "
      "proofs goes in the AI declaration at the end (never the abstract or introduction; rule of 18 Nov 2026)", fn=f60),
    T(61, "doc", "the text changed after he read it",
      "the sentence is about the text as it stands; when the .tex moves after the record, tell him what changed", fn=f61),
    T(62, "doc", "the README, hosting description or cover letter says he read it",
      "the page beside the paper follows the paper: without AUTHOR_READ_OK it does not say he read, checked or "
      "verified anything", True, fn=f62),
    T(73, "line", "the Google Cloud education-credits sentence (rule of 18 Nov 2026)",
      "delete it from the acknowledgements or funding text. A posted paper: fix the source and its public repository now, the "
      "hosted PDF at its next version", fn=f73),
]


# ---------------------------------------------------------------- event hooks
def _newest_tex(ctx):
    paths = [d.path for d in ctx.get("docs") or [] if d.path and os.path.exists(d.path)]
    return max(paths, key=os.path.getmtime) if paths else ""


AUDIT_INDEX = os.path.join(HERE, "audit_index.json")


def audit_state(tex):
    """(state, verdict line, report path) of the audit on record for a paper. state: none / stale / notready / ready.
    Only a record written by paper_audit.py counts: a file named AUDIT or REFEREE beside the .tex may be the author's
    own note, or a brief for a referee, and says nothing about what a second reader found."""
    try:
        with open(AUDIT_INDEX, encoding="utf-8") as f:
            rec = json.load(f).get(os.path.abspath(tex).replace("\\", "/").lower())
    except (OSError, ValueError):
        rec = None
    if not isinstance(rec, dict) or not os.path.exists(str(rec.get("report") or "")):
        return "none", "", ""
    verdict = str(rec.get("verdict") or "")
    try:
        same = rec["tex_sha"] == C.paper_sha(tex) if rec.get("tex_sha") else \
            rec.get("tex_mtime", 0) >= os.path.getmtime(tex) - 60
    except OSError:
        same = False
    if not same:
        return "stale", verdict, rec["report"]
    ready = re.search(r"SEND AS IS", verdict) and re.search(r"MUST-FIX:\s*0\b", verdict)
    return ("ready" if ready else "notready"), verdict, rec["report"]


def c43(ch, p, ctx):
    docs = [d.path for d in ctx.get("docs") or [] if d.whole and d.path and os.path.exists(d.path)]
    if not docs:
        return "no audit could be looked for (the paper is not known from this call): %s run <main.tex>" % AUDIT
    out = []
    for tex in docs[:3]:
        name = os.path.basename(os.path.dirname(tex)) + "/" + os.path.basename(tex)
        st, verdict, rep = audit_state(tex)
        if st == "none":
            out.append("%s has no audit on record: %s run \"%s\"" % (name, AUDIT, tex))
        elif st == "stale":
            out.append("%s changed after its audit (%s): have the text as it now stands audited again (%s run \"%s\")"
                       % (name, verdict or "no verdict line", AUDIT, tex))
        elif st == "notready":
            out.append("%s was audited and is not ready (%s): fix what %s lists, then audit again" % (name, verdict, rep))
    return "; ".join(out) or None


def must_count(docs):
    """(MUST findings, their hooks, introduction-group findings that are not MUST, their hooks)."""
    n, ids, n2, ids2 = 0, [], 0, []
    for h in TEXT:
        if not h.get("must") and not h.get("tagged") and h["id"] not in C.INTRO_GROUP:
            continue
        got = C.scan(h, docs)
        m = C.must_n(h, got)
        if m:
            n += m
            ids.append(h["id"])
        if len(got) > m:
            n2 += len(got) - m
            ids2.append(h["id"])
    return n, ids, n2, ids2


def c49(ch, p, ctx):
    docs = [d for d in ctx.get("docs") or [] if d.whole]
    if not docs:
        return "the .tex is not known from this call: run %s on it first" % LINT
    n, ids, n2, ids2 = must_count(docs)
    stale = []
    for d in docs:
        log = d.path[:-4] + ".log"
        try:
            if os.path.getmtime(log) + 5 < os.path.getmtime(d.path):
                stale.append(os.path.basename(d.path))
        except OSError:
            pass
    aud = []
    for d in docs[:3]:
        st, verdict, _ = audit_state(d.path)
        aud.append("%s: %s" % (os.path.basename(d.path), {"none": "no audit on record", "stale": "audited before its "
                   "last change", "notready": verdict, "ready": verdict}[st]))
    if not n and not n2 and not stale:
        return None
    parts = ["audit verdict - " + "; ".join(aud)]
    if n:
        parts.append("%d MUST findings in %s (%s)" % (n, ", ".join(os.path.basename(d.path) for d in docs), " ".join(ids)))
    if n2:
        parts.append("%d findings on what the introduction says is new and in which words (%s): the journal's three "
                     "reasons were of this kind, so answer each before this leaves" % (n2, " ".join(ids2)))
    if stale:
        parts.append("the PDF is older than %s: compile again" % ", ".join(stale))
    return "; ".join(parts)


def c56(ch, p, ctx):
    msg = str(ctx.get("commit_msg") or "")
    first = msg.split("\n")[0].split("\\n")[0]
    bad = []
    if first.count(";") >= 2 or first.count(",") >= 4:
        bad.append("a chain of clauses")
    if len(first) > 90:
        bad.append("%d characters in the first line" % len(first))
    m = re.search(r"\b(?:headline|comprehensive|robust|enhanc\w+|streamlin\w+|human[- ]?(?:voice|sounding)|"
                  r"sound(?:s|ing)? (?:more )?human|de-?AI|AI[- ]tells?|polish\w*|self-?introspection|audit findings?)\b",
                  msg, re.I)
    if m:
        bad.append("\"%s\" describes the editing" % m.group(0))
    return ("\"%s\": %s" % (C.excerpt(first, 70), "; ".join(bad))) if bad else None


EVENT = [
    T(39, "event", "his rules for a paper, in one place",
      "read %s before the first sentence, and python ~/brain-repo/"
      "12_cognitive_architecture/his_voice/tools/voice.py brief \"<topic>\" for his own way of putting things" % RULES,
      on=("start",)),
    T(40, "event", "the novelty in three sentences, before writing",
      "write down: (1) what was proved before, with the citation and theorem number; (2) why that argument does not give "
      "the new statement; (3) the one new idea as a displayed estimate. If (2) or (3) will not come, the paper is not "
      "ready. These three sentences become the introduction's second paragraph.", on=("start",)),
    T(41, "event", "his earlier papers on the same topic",
      "open them first; what they prove is cited by theorem number, never reprinted. Check with: %s <new.tex> --against "
      "<earlier.tex>" % LINT, on=("start",)),
    T(42, "event", "read the compiled pages, not the source",
      "after this compile, read the PDF's first three pages as rendered (pdftotext drops overlines and bars: look at the "
      "page) and the log's warnings", on=("compile",), cool=7200),
    T(43, "event", "an independent audit before the paper leaves",
      "a second reader who has not seen your reasoning reads the PDF as a referee and writes AUDIT_<date>.md beside the "
      ".tex; the author's own reread is not an audit (his 12 Nov words: \"more auditing\")", on=("publish", "submit"),
      check=c43, cool=1800),
    T(44, "event", "the journal is his decision",
      "where a paper is submitted is his: one short email with the proposed journal, the two closest papers it printed "
      "in the last three years, and your recommendation; never submit on your own", on=("submit",)),
    T(45, "event", "pages one to three, read as the referee reads them",
      "before this goes out, answer from the first three pages alone: what is the theorem, what was known, why is the "
      "extension not routine. If the pages do not answer, rewrite them (the PTRF referee stopped on page 3)",
      on=("publish", "submit"), cool=3600),
    T(46, "event", "the cover letter and his earlier paper",
      "when the paper extends a paper of his, the letter and the introduction say so in one plain sentence each, with "
      "what is carried over and what is new", on=("submit",)),
    T(47, "event", "a rejection or a referee report is a lesson to file",
      "read the whole report; write one mistake memory with the referee's words; map each point to a hook W01..W56 and "
      "add a hook where none covers it (edit pw_hooks.py, extend the selftest); then say in plain words whether the "
      "referee is right", on=("reject",), cool=3600),
    T(48, "event", "the AI declaration",
      "if the venue or he asks for one, it is a short factual record of which system produced what, in its own section; "
      "nothing about the process anywhere else in the paper or the README", on=("publish", "submit"), cool=7200),
    T(49, "event", "zero MUST findings, and the introduction findings answered, before it leaves",
      "the lint must come back with no MUST and no open finding of W08 W09 W11 W12 W16 W17 W19 W21 on the .tex being "
      "sent", on=("publish", "submit"), check=c49, cool=900),
    T(50, "event", "publishable as is",
      "his 12 Nov words: \"make sure that the papers we are writing are publishable as is\". That means, for this paper: "
      "the lint clean (%s <tex>), an audit report newer than the text, no sentences shared with his earlier papers, "
      "the citation hooks answered, and the PDF read page by page" % LINT, on=("publish", "submit", "start"), cool=7200),
    T(56, "event", "the commit message of a paper's repository",
      "short and plain (\"fix section heading\", \"add appendix B\"): no chain of clauses, nothing about how the text "
      "was edited or by whom", on=("commit",), check=c56, cool=0),
    T(63, "event", "who read the paper",
      "the default for every paper is the standing sentence (\"" + STANDING + "\"). \"The author has read the paper and "
      "the proofs\" is written only into a paper he named for publication, recorded in AUTHOR_READ_OK beside the .tex "
      "(rule of 17 Nov)", on=("start",), cool=7200),
    T(64, "event", "a posted paper does not say he read it",
      "papers going to GitHub, Zenodo or ResearchGate are the ones he has mostly not read: no sentence that he read, "
      "checked or verified them", on=("publish",), check=c64, cool=900),
    T(65, "event", "a submitted paper says he read it only on his word",
      "before a journal submission, the sentence and AUTHOR_READ_OK agree, and he is told the sentence is made in his "
      "name", on=("submit",), check=c65, cool=900),
    T(66, "event", "the compiled PDF and the sentence that he read it",
      "search the PDF text, not only main.tex: the abstract, a title-page note or an \\input file can carry it",
      on=("compile", "publish", "submit"), check=c66, cool=1800),
    T(67, "event", "is this paper already at a journal",
      "one paper is at one journal at a time. Before a submission page is opened or filled, look the paper up in the "
      "private record: " + SUB_TOOL + " check \"<title>\" (exit 3: it is in process, do not submit)", True, on=("submit",), check=c67, cool=600),
    T(68, "event", "record the submission the minute it goes through",
      SUB_TOOL + " add --title \"...\" --journal \"...\" --date <day> --id <manuscript number> --account <the login "
      "used> --agent <you>. A submission that is on a journal's site and not in SUBMISSIONS.jsonl is the one that "
      "gets sent twice", on=("submit",), cool=900),
    T(69, "event", "record the journal's answer the day it arrives",
      SUB_TOOL + " status <row> declined|desk_returned|revision|accepted|withdrawn --date <day> --note \"...\". A "
      "paper is free to go elsewhere only when its open row is closed, and a journal with a closed row does not get "
      "that paper again", on=("reject",), cool=900),
    T(70, "event", "a draft left in a journal's system",
      "a submission started and not finished is recorded too (--status draft_started): it sits there in his name "
      "and the next agent takes the paper for unsubmitted", on=("submit",), check=c70, cool=3600),
    T(71, "event", "open rows nobody has looked at",
      "the record says \"still in process\" only as of the day someone last looked", on=("submit", "reject"),
      check=c71, cool=3600),
    T(72, "event", "the record of submissions is private",
      "journals, manuscript numbers and decisions live in " + SUB_DIR + " (a private folder) and nowhere "
      "else: not in the paper's repository, its README, a hosting page or a public board",
      on=("publish", "commit"), check=c72, cool=900),
]

HOOKS = TEXT + EVENT


def load():
    return HOOKS
