"""Polite ProofWiki harvester -> draft bundles (.part until human-sampled).

Fetches a curated list of ProofWiki pages via the MediaWiki API, extracts the
Theorem/Definition statement section (and Proof section for theorems), performs
conservative wikitext cleanup, and writes a mathbrain-draft-v1 bundle to the
inbox as .part. Pages whose statement will not extract cleanly are skipped;
theorems without a clean proof section are demoted to concept entries rather
than shipped with a fake proof. Rate limited; honest User-Agent; CC-BY-SA
attribution carried per entry.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request

API = "https://proofwiki.org/w/api.php"
UA = "math-brain-population/1.0 (research corpus build; contact: local)"
RATE_S = 1.6
OUT_DIR = r"~\math-brain-inbox\proofwiki-harvester"
MAX_STATEMENT = 1500
MIN_STATEMENT = 40

PAGES = [
    "Pythagoras's Theorem",
    "Fermat's Little Theorem",
    "Euclid's Theorem",
    "Fundamental Theorem of Arithmetic",
    "Bezout's Lemma",
    "Euclid's Lemma",
    "Chinese Remainder Theorem",
    "Wilson's Theorem",
    "Fermat's Two Squares Theorem",
    "Cantor's Theorem",
    "Cantor-Bernstein-Schroeder Theorem",
    "Zorn's Lemma",
    "Well-Ordering Theorem",
    "Intermediate Value Theorem",
    "Mean Value Theorem",
    "Rolle's Theorem",
    "Bolzano-Weierstrass Theorem",
    "Heine-Borel Theorem",
    "Extreme Value Theorem",
    "Squeeze Theorem",
    "Taylor's Theorem",
    "L'Hopital's Rule",
    "Fundamental Theorem of Calculus",
    "Banach Fixed-Point Theorem",
    "Baire Category Theorem",
    "Monotone Convergence Theorem (Measure Theory)",
    "Fatou's Lemma",
    "Dominated Convergence Theorem",
    "Cayley's Theorem",
    "First Isomorphism Theorem",
    "Orbit-Stabilizer Theorem",
    "Burnside's Lemma",
    "Cauchy's Group Theorem",
    "Fundamental Theorem of Finite Abelian Groups",
    "Rank-Nullity Theorem",
    "Cayley-Hamilton Theorem",
    "Cramer's Rule",
    "De Morgan's Laws (Set Theory)",
    "Inclusion-Exclusion Principle",
    "Pigeonhole Principle",
    "Binomial Theorem",
    "Vandermonde's Identity",
    "Hall's Marriage Theorem",
    "Ramsey's Theorem",
    "Definition:Prime Number",
    "Definition:Greatest Common Divisor of Integers",
    "Definition:Equivalence Relation",
    "Definition:Partial Ordering",
    "Definition:Bijection",
    "Definition:Cardinality",
    "Definition:Metric Space",
    "Definition:Open Set (Metric Space)",
    "Definition:Cauchy Sequence",
    "Definition:Complete Metric Space",
    "Definition:Continuous Mapping (Metric Space)",
    "Definition:Normal Subgroup",
    "Definition:Quotient Group",
    "Definition:Ring (Abstract Algebra)",
    "Definition:Field (Abstract Algebra)",
    "Definition:Ideal of Ring",
    "Definition:Homomorphism (Abstract Algebra)",
    "Definition:Eigenvalue",
    "Definition:Determinant of Matrix",
    "Definition:Convex Function",
    "Definition:Uniform Convergence",
]


def fetch_wikitext(title: str) -> str | None:
    params = urllib.parse.urlencode(
        {
            "action": "query",
            "prop": "revisions",
            "rvprop": "content",
            "rvslots": "main",
            "format": "json",
            "formatversion": "2",
            "titles": title,
        }
    )
    req = urllib.request.Request(f"{API}?{params}", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
        page = data["query"]["pages"][0]
        if page.get("missing"):
            return None
        return page["revisions"][0]["slots"]["main"]["content"]
    except Exception:
        return None


SECTION_RE = re.compile(r"^==\s*([^=]+?)\s*==\s*$", re.M)


def sections(wikitext: str) -> dict[str, str]:
    out: dict[str, str] = {}
    matches = list(SECTION_RE.finditer(wikitext))
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(wikitext)
        out.setdefault(m.group(1).strip().lower(), wikitext[start:end].strip())
    if matches:
        out.setdefault("_preamble", wikitext[: matches[0].start()].strip())
    else:
        out["_preamble"] = wikitext.strip()
    return out


LINK_RE = re.compile(r"\[\[(?:[^\]|]*\|)?([^\]|]+)\]\]")
BOLD_RE = re.compile(r"'{2,}")
HTML_RE = re.compile(r"<[^>]+>")
HEAVY_TEMPLATE_RE = re.compile(r"\{\{(?!(?:begin-eqn|end-eqn|eqn)\b)[^}]*\}\}")


def clean(text: str) -> str | None:
    if text.count("{{") > 6:
        return None
    text = LINK_RE.sub(r"\1", text)
    text = HEAVY_TEMPLATE_RE.sub(" ", text)
    text = BOLD_RE.sub("", text)
    text = HTML_RE.sub(" ", text)
    text = re.sub(r"^[:;*#]+\s*", "", text, flags=re.M)
    text = re.sub(r"\s+", " ", text).strip()
    if "{{" in text or "}}" in text:
        return None
    return text


def slugify(title: str) -> str:
    slug = title.lower()
    slug = slug.replace("definition:", "")
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug[:80] or "untitled"


def main() -> int:
    import os

    os.makedirs(OUT_DIR, exist_ok=True)
    entries = []
    skipped = []
    for title in PAGES:
        time.sleep(RATE_S)
        wikitext = fetch_wikitext(title)
        if wikitext is None:
            skipped.append((title, "fetch-failed-or-missing"))
            continue
        secs = sections(wikitext)
        is_definition = title.lower().startswith("definition:")
        raw_stmt = secs.get("definition") if is_definition else secs.get("theorem")
        if raw_stmt is None:
            raw_stmt = secs.get("_preamble", "")
        statement = clean(raw_stmt or "")
        if not statement or not (MIN_STATEMENT <= len(statement) <= MAX_STATEMENT):
            skipped.append((title, "statement-unextractable"))
            continue
        kind = "definition" if is_definition else "theorem"
        proof_text = None
        if kind == "theorem":
            proof = clean(secs.get("proof", "") or "")
            if proof and MIN_STATEMENT <= len(proof) <= 4000:
                proof_text = proof
            else:
                kind = "concept"
        display = title.replace("Definition:", "")
        entries.append(
            {
                "key": f"pw-{slugify(title)}"[:60],
                "namespace": "harvest.proofwiki",
                "logical_name": slugify(title),
                "kind": kind,
                "title": display,
                "statement": statement,
                "proof_text": proof_text,
                "assumptions": [],
                "domain": "harvested (ProofWiki)",
                "source": {
                    "source_id": f"proofwiki:{title}",
                    "url": "https://proofwiki.org/wiki/"
                    + urllib.parse.quote(title.replace(" ", "_")),
                    "revision": "api-read-2026-08-02",
                    "license": "CC-BY-SA-4.0",
                    "excerpt": None,
                },
            }
        )
        print(f"OK   {title} -> {kind} ({len(statement)} chars)")
    draft = {
        "spec": "mathbrain-draft-v1",
        "author_agent": "proofwiki-harvester",
        "bundle_slug": "proofwiki-harvest-001",
        "entries": entries,
        "relations": [],
    }
    out_path = f"{OUT_DIR}\\bundle_001.part"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(draft, fh, indent=1)
    print(f"\nwrote {out_path}: {len(entries)} entries, {len(skipped)} skipped")
    for title, why in skipped:
        print(f"SKIP {title}: {why}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
