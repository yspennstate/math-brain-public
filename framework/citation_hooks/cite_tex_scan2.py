# -*- coding: utf-8 -*-
"""Helpers for the who-did-what and prior-work hooks C33-C62."""
import os
import re

import cite_tex_scan as S


def tex(p):
    f = S.find_tex(p)
    return f, (S.text(f) if f else "")


def intro(t):
    """First numbered section (the introduction), or the text before the second \\section."""
    secs = [m.start() for m in re.finditer(r"\\section\{", t)]
    if not secs:
        return S.body(t)[:6000]
    end = secs[1] if len(secs) > 1 else len(t)
    return t[secs[0]:end]


def abstract(t):
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", t, re.S)
    return m.group(1) if m else ""


def bibitems(t):
    """{key: entry text} from \\bibitem lines."""
    out = {}
    for m in re.finditer(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}(.*?)(?=\\bibitem|\\end\{thebibliography\}|\Z)", t, re.S):
        out[m.group(1).strip()] = m.group(2)
    return out


def cites(s):
    keys = []
    for m in re.finditer(r"\\cite[pt]?\*?(?:\[[^\]]*\])?\{([^}]+)\}", s):
        keys += [k.strip() for k in m.group(1).split(",")]
    return keys


def surnames(entry):
    """Surnames in a bibitem's author part (before the first comma-run that ends the authors)."""
    head = re.split(r",\s*(?=[A-Z][a-z]+\s)|\\emph|\\textit", entry)[0]
    return re.findall(r"~?([A-Z][a-z\\\"'`{}]+(?:[- ][A-Z][a-z]+)?)\b", head)


def repo_dir(f):
    return os.path.dirname(f) if f else ""


UNREAD = re.compile(r"in preparation|preprint|manuscript|personal communication|to appear|submitted", re.I)
NEWCLAIM = re.compile(r"\b(is new|are new|new result|we prove for the first time|first proof|for the first time|"
                      r"has not been (?:proved|studied|considered)|no (?:previous|prior) (?:work|result)|"
                      r"results of (?:the|this) paper are|what is new)\b", re.I)
SYSTEM = re.compile(r"\b(Claude|Codex|GPT|Gemini|ChatGPT|o\d|Opus|Sonnet|Fable)\b")
DIDVERB = re.compile(r"\b(wrote|proved|proposed|computed|ran|supplied|checked|found|drafted|derived)\b")
