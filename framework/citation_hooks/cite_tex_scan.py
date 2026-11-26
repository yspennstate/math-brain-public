# -*- coding: utf-8 -*-
"""Helpers for the text-reading citation hooks C27-C32.

find_tex(p): the .tex the tool call is about - a path named in the command or file_path, else main.tex in the cwd,
its repo/ or paper/ folder. text(path): the source without comment lines. sentences(t): rough sentence split.
declaration(t): the AI declaration section, or ''.
"""
import os
import re

TEX = re.compile(r"[A-Za-z]:[\\/][^\s\"']+?\.tex\b|[~./\w-][^\s\"';|&]*?\.tex\b")


def _cmd(p):
    ti = p.get("tool_input") or {}
    if isinstance(ti, dict):
        return " ".join(str(ti.get(k, "")) for k in ("command", "file_path", "path"))
    return str(ti)


def _base(p):
    """The directory the command runs in: the last `cd` in it (as the core resolves it), else the payload cwd."""
    import cite_hook_core as C
    cmd = _cmd(p)
    cds = C.CD.findall(cmd)
    return C._win(cds[-1]) if cds else str(p.get("cwd") or os.getcwd())


def find_tex(p):
    import cite_hook_core as C
    cwd = _base(p)
    for m in TEX.findall(_cmd(p)):
        q = C._win(m)
        if not os.path.isabs(q):
            q = os.path.join(cwd, q)
        if os.path.isfile(q):
            return q
    for sub in ("", "repo", "paper"):
        q = os.path.join(cwd, sub, "main.tex")
        if os.path.isfile(q):
            return q
    return None


def text(path):
    try:
        raw = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""
    return "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in raw.splitlines())


def sentences(t):
    t = re.sub(r"\s+", " ", t)
    return re.split(r"(?<=[.!?])\s+(?=[A-Z\\])", t)


def declaration(t):
    m = re.search(r"\\section\*?\{[^}]*(?:generative AI|AI declaration|artificial intelligence)[^}]*\}(.*?)(?=\\section|\\begin\{thebibliography\}|\\bibliography|\Z)",
                  t, re.S | re.I)
    return m.group(1) if m else ""


def body(t):
    """Text before the acknowledgements/declarations and the bibliography."""
    m = re.search(r"\\section\*?\{\s*(?:Acknowledg|Declaration|Competing|Funding|Data availability)", t)
    return t[:m.start()] if m else t
