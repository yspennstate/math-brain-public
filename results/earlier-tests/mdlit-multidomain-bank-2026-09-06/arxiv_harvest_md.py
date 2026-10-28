# -*- coding: utf-8 -*-
"""arxiv_harvest_md.py - list arXiv papers in the multi-domain bank's categories through the official API and fetch
their LaTeX sources politely. Adapted (copied, then changed) from the probability campaign's arxiv_harvest.py
(2026-09-06); that lane's files are never edited by this one.

    python arxiv_harvest_md.py list --years 2026,2025,2024
    python arxiv_harvest_md.py download --max 6000
    python arxiv_harvest_md.py status

Domain groups (the bank's strata) and their listing queries:
    analysis      math.AP, math.FA, math.CA
    algebra_nt_co math.AG, math.NT, math.CO
    geom_top_log  math.DG, math.GT, math.AT, math.LO
    ml_theory     stat.ML; cs.LG cross-listed with math.ST / stat.TH / math.OC / cs.IT (papers with proofs)

RATE. arXiv asks for at most one request every three seconds from one client. The probability campaign's
harvester runs on this machine at one request per 4 s; while its download log has been written in the last
90 s this script sleeps PEER_SLEEP (12 s) so the two together stay under the limit, and SOLO_SLEEP (4 s)
otherwise. One connection, never two requests at once, backoff on 429/503, resumable, STOP file honoured.
Download order: round-robin over the four groups, inside a group newest first with primary-category papers
first, so the harvest is multi-domain from its first hundred papers.
"""
import argparse
import ctypes
import gzip
import hashlib
import io
import json
import os
import sys
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = "<HOME>/arxiv_multidomain_sources"
LISTING = os.path.join(ROOT, "listing.jsonl")
SRC = os.path.join(ROOT, "src")
TEX = os.path.join(ROOT, "tex")
DLLOG = os.path.join(ROOT, "download_log.jsonl")
STOP_FILE = os.path.join(ROOT, "STOP")
LOG = os.path.join(ROOT, "harvest.log")
PEER_LOG = "<HOME>/arxiv_mathpr_sources/download_log.jsonl"
UA = "multidomain-lit-bank/0.1 (research test bank; mailto:<CONTACT>)"
PEER_SLEEP = 12.0
SOLO_SLEEP = 4.0
LIST_PEER_SLEEP = 8.0
LIST_SOLO_SLEEP = 3.5
NS = {"a": "http://www.w3.org/2005/Atom", "os": "http://a9.com/-/spec/opensearch/1.1/",
      "ax": "http://arxiv.org/schemas/atom"}

GROUPS = {
    "analysis": ["cat:math.AP", "cat:math.FA", "cat:math.CA"],
    "algebra_nt_co": ["cat:math.AG", "cat:math.NT", "cat:math.CO"],
    "geom_top_log": ["cat:math.DG", "cat:math.GT", "cat:math.AT", "cat:math.LO"],
    "ml_theory": ["cat:stat.ML", "cat:cs.LG AND (cat:math.ST OR cat:stat.TH OR cat:math.OC OR cat:cs.IT)"],
}
PRIMARY_OF = {
    "analysis": {"math.AP", "math.FA", "math.CA"},
    "algebra_nt_co": {"math.AG", "math.NT", "math.CO"},
    "geom_top_log": {"math.DG", "math.GT", "math.AT", "math.LO"},
    "ml_theory": {"stat.ML", "cs.LG", "math.ST", "stat.TH"},
}


def log(msg):
    line = time.strftime("%Y-%m-%d %H:%M:%S") + " " + msg
    print(line, flush=True)
    with io.open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def below_normal():
    try:
        h = ctypes.windll.kernel32.GetCurrentProcess()
        ctypes.windll.kernel32.SetPriorityClass(h, 0x4000)
    except Exception:
        pass


def peer_active():
    try:
        return (time.time() - os.path.getmtime(PEER_LOG)) < 90.0
    except OSError:
        return False


def polite_sleep(listing=False):
    if listing:
        time.sleep(LIST_PEER_SLEEP if peer_active() else LIST_SOLO_SLEEP)
    else:
        time.sleep(PEER_SLEEP if peer_active() else SOLO_SLEEP)


def http_get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.headers.get("Content-Type", ""), r.read(), r.geturl()


def api_page(query, start, n):
    url = ("https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(query, safe="+:[]*()")
           + "&start=%d&max_results=%d&sortBy=submittedDate&sortOrder=descending" % (start, n))
    for attempt in range(6):
        try:
            st, ct, body, _ = http_get(url, timeout=120)
            root = ET.fromstring(body)
            total = int(root.findtext("os:totalResults", default="0", namespaces=NS))
            entries = root.findall("a:entry", NS)
            if total and not entries and start < total:
                log("api: empty page at start=%d (total %d), retry %d" % (start, total, attempt))
                time.sleep(15)
                continue
            return total, entries
        except (urllib.error.HTTPError, urllib.error.URLError, ET.ParseError) as e:
            log("api error %s at start=%d, attempt %d" % (e, start, attempt))
            time.sleep(30 * (attempt + 1))
    return None, []


def entry_to_row(e):
    aid = e.findtext("a:id", default="", namespaces=NS).rsplit("/abs/", 1)[-1]
    base = aid.rsplit("v", 1)[0] if "v" in aid.split("/")[-1] else aid
    cats = [c.get("term") for c in e.findall("a:category", NS)]
    prim = e.find("ax:primary_category", NS)
    return {
        "arxiv_id": aid, "base_id": base,
        "title": " ".join((e.findtext("a:title", default="", namespaces=NS) or "").split()),
        "published": e.findtext("a:published", default="", namespaces=NS),
        "updated": e.findtext("a:updated", default="", namespaces=NS),
        "authors": [a.findtext("a:name", default="", namespaces=NS) for a in e.findall("a:author", NS)],
        "categories": cats,
        "primary_category": prim.get("term") if prim is not None else (cats[0] if cats else ""),
        "comment": " ".join((e.findtext("ax:comment", default="", namespaces=NS) or "").split()),
        "journal_ref": e.findtext("ax:journal_ref", default="", namespaces=NS),
        "doi": e.findtext("ax:doi", default="", namespaces=NS),
        "summary": " ".join((e.findtext("a:summary", default="", namespaces=NS) or "").split()),
    }


def cmd_list(args):
    os.makedirs(ROOT, exist_ok=True)
    seen = set()
    if os.path.exists(LISTING):
        for ln in io.open(LISTING, encoding="utf-8"):
            try:
                seen.add(json.loads(ln)["base_id"])
            except Exception:
                pass
    years = [y.strip() for y in args.years.split(",") if y.strip()]
    groups = [g for g in args.groups.split(",") if g] if args.groups else list(GROUPS)
    with io.open(LISTING, "a", encoding="utf-8") as out:
        for g in groups:
            for cq in GROUPS[g]:
                for y in years:
                    if os.path.exists(STOP_FILE):
                        log("STOP file present - stopping listing")
                        return
                    q = "(%s) AND submittedDate:[%s01010000 TO %s12312359]" % (cq, y, y)
                    start, total, new = 0, None, 0
                    while True:
                        total, entries = api_page(q, start, args.page)
                        if total is None:
                            log("list %s %s: giving up at start=%d" % (cq, y, start))
                            break
                        for e in entries:
                            row = entry_to_row(e)
                            row["year_query"] = y
                            row["domain_group"] = g
                            row["list_query"] = cq
                            if row["base_id"] in seen:
                                continue
                            seen.add(row["base_id"])
                            out.write(json.dumps(row, ensure_ascii=False) + "\n")
                            new += 1
                        out.flush()
                        log("list %s %s: start=%d got=%d total=%d new_so_far=%d" % (cq, y, start, len(entries), total, new))
                        start += args.page
                        if start >= total or not entries or (args.cap_per_query and start >= args.cap_per_query):
                            break
                        polite_sleep(listing=True)
                    polite_sleep(listing=True)
    log("list done: %d ids in listing" % len(seen))


def load_listing():
    rows = []
    if os.path.exists(LISTING):
        for ln in io.open(LISTING, encoding="utf-8"):
            try:
                rows.append(json.loads(ln))
            except Exception:
                pass
    return rows


def done_ids():
    done = {}
    if os.path.exists(DLLOG):
        for ln in io.open(DLLOG, encoding="utf-8"):
            try:
                r = json.loads(ln)
                done[r["base_id"]] = r
            except Exception:
                pass
    return done


def extract_tex(base_id, raw, ctype):
    """Write every .tex/.bib/.bbl/.sty member into tex/<id>/. Returns (kind, n_tex)."""
    safe = base_id.replace("/", "_")
    outdir = os.path.join(TEX, safe)
    n_tex = 0
    try:
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tf:
            members = [m for m in tf.getmembers() if m.isfile() and m.size < 20_000_000]
            os.makedirs(outdir, exist_ok=True)
            for m in members:
                name = os.path.basename(m.name)
                low = name.lower()
                if not (low.endswith(".tex") or low.endswith(".bbl") or low.endswith(".sty")
                        or low.endswith(".cls") or low.endswith(".ltx") or low.endswith(".bib")):
                    continue
                data = tf.extractfile(m).read()
                dest = os.path.join(outdir, m.name.replace("/", "__").replace("\\", "__"))
                with open(dest, "wb") as f:
                    f.write(data)
                if low.endswith(".tex") or low.endswith(".ltx"):
                    n_tex += 1
            return "tar", n_tex
    except (tarfile.TarError, EOFError, OSError):
        pass
    try:
        data = gzip.decompress(raw)
        if data[:5] == b"%PDF-":
            return "pdf_only", 0
        if b"\\documentclass" in data[:20000] or b"\\begin{document}" in data or b"\\section" in data:
            os.makedirs(outdir, exist_ok=True)
            with open(os.path.join(outdir, "main.tex"), "wb") as f:
                f.write(data)
            return "single_tex", 1
        return "single_other", 0
    except (OSError, EOFError):
        pass
    if raw[:5] == b"%PDF-":
        return "pdf_only", 0
    if b"\\documentclass" in raw[:20000]:
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "main.tex"), "wb") as f:
            f.write(raw)
        return "single_tex", 1
    return "unknown", 0


def download_order(rows):
    """Round-robin over groups; inside a group primary-in-group first, then newest first."""
    by_g = {}
    for r in rows:
        g = r.get("domain_group", "?")
        by_g.setdefault(g, []).append(r)
    for g, lst in by_g.items():
        prim = PRIMARY_OF.get(g, set())
        lst.sort(key=lambda r: r.get("published", ""), reverse=True)
        lst.sort(key=lambda r: 0 if r.get("primary_category") in prim else 1)
    order = []
    names = sorted(by_g)
    idx = {g: 0 for g in names}
    while True:
        moved = False
        for g in names:
            if idx[g] < len(by_g[g]):
                order.append(by_g[g][idx[g]])
                idx[g] += 1
                moved = True
        if not moved:
            break
    return order


def cmd_download(args):
    below_normal()
    os.makedirs(SRC, exist_ok=True)
    os.makedirs(TEX, exist_ok=True)
    rows = load_listing()
    done = done_ids()
    todo = [r for r in download_order(rows) if r["base_id"] not in done]
    log("download: %d listed, %d done, %d to do, cap %d" % (len(rows), len(done), len(todo), args.max))
    fails = 0
    n = 0
    for r in todo:
        if n >= args.max:
            break
        if os.path.exists(STOP_FILE):
            log("STOP file present - stopping gracefully")
            break
        bid = r["base_id"]
        url = "https://export.arxiv.org/src/" + bid
        rec = {"base_id": bid, "arxiv_id": r.get("arxiv_id"), "domain_group": r.get("domain_group"),
               "primary_category": r.get("primary_category"), "ts": time.strftime("%Y-%m-%d %H:%M:%S"), "url": url}
        try:
            st, ct, raw, final = http_get(url, timeout=90)
            fails = 0
            rec.update({"status": st, "content_type": ct, "bytes": len(raw),
                        "sha256": hashlib.sha256(raw).hexdigest(), "final_url": final})
            with open(os.path.join(SRC, bid.replace("/", "_") + ".bin"), "wb") as f:
                f.write(raw)
            kind, n_tex = extract_tex(bid, raw, ct)
            rec.update({"kind": kind, "n_tex": n_tex})
        except urllib.error.HTTPError as e:
            rec.update({"status": e.code, "error": str(e)})
            if e.code in (429, 503):
                fails += 1
                log("rate/availability %s on %s - sleeping 120 s" % (e.code, bid))
                time.sleep(120)
            elif e.code == 404:
                rec["kind"] = "not_found"
            else:
                fails += 1
        except Exception as e:
            rec.update({"error": e.__class__.__name__ + ": " + str(e)[:200]})
            fails += 1
            time.sleep(30)
        with io.open(DLLOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        n += 1
        if n % 25 == 0:
            log("download: %d this run (%s %s %s bytes=%s kind=%s peer_active=%s)" % (
                n, bid, r.get("domain_group"), rec.get("status"), rec.get("bytes"), rec.get("kind"), peer_active()))
        if fails >= 8:
            log("8 consecutive failures - stopping")
            break
        polite_sleep()
    log("download run finished: %d fetched this run" % n)


def cmd_status(args):
    rows = load_listing()
    done = done_ids()
    kinds, groups = {}, {}
    for r in done.values():
        k = r.get("kind", r.get("error", "?"))
        kinds[k] = kinds.get(k, 0) + 1
        g = r.get("domain_group", "?")
        groups[g] = groups.get(g, 0) + 1
    lg = {}
    for r in rows:
        lg[r.get("domain_group", "?")] = lg.get(r.get("domain_group", "?"), 0) + 1
    print(json.dumps({"listed": len(rows), "listed_by_group": lg, "downloaded": len(done), "downloaded_by_group": groups,
                      "kinds": kinds, "tex_dirs": len(os.listdir(TEX)) if os.path.exists(TEX) else 0,
                      "peer_active": peer_active()}, indent=1))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("list")
    p.add_argument("--years", default="2026,2025,2024")
    p.add_argument("--page", type=int, default=1000)
    p.add_argument("--groups", default="")
    p.add_argument("--cap-per-query", type=int, default=6000, help="listing rows per (query, year); newest first")
    p.set_defaults(fn=cmd_list)
    p = sub.add_parser("download")
    p.add_argument("--max", type=int, default=6000)
    p.set_defaults(fn=cmd_download)
    p = sub.add_parser("status")
    p.set_defaults(fn=cmd_status)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
