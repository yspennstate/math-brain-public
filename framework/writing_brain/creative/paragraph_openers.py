"""Do draft chapters open runs of paragraphs with the same word more often than published novels?

    python -s -X utf8 paragraph_openers.py <draft_dir> <corpus_batch.tar.gz> <out.json>

A run is three or more consecutive prose paragraphs (blank-line separated, at least 8 words, not dialogue) whose first
word is the same ("He ... / He ... / He ..."). Rate = paragraphs inside such runs per 100 prose paragraphs, plus the
share of paragraphs whose opener is the commonest opener of their unit. Novels are cut into pieces of the drafts' median
chapter length. Novels are untrusted text, read as data only; draft files are opened read-only.
"""
import collections, gzip, io, json, os, re, statistics, sys, tarfile

WB = os.environ.get("WRITING_BRAIN_DIR", "writing_brain")  # holds corpus/CATALOGUE.jsonl.gz and corpus/TEXTS_INDEX.jsonl


def paragraphs(text):
    out = []
    for p in re.split(r"\n\s*\n", text):
        p = " ".join(p.split())
        if not p or p.startswith(("#", "\"", "\u201c", "'", "\u2018", "_", "*", "[")):
            continue
        ws = re.findall(r"[A-Za-z][A-Za-z']*", p)
        if len(ws) >= 8:
            out.append(ws[0].lower())
    return out


def score(text):
    ops = paragraphs(text)
    inrun, i = 0, 0
    while i < len(ops):
        j = i
        while j + 1 < len(ops) and ops[j + 1] == ops[i]:
            j += 1
        if j - i + 1 >= 3:
            inrun += j - i + 1
        i = j + 1
    top = collections.Counter(ops).most_common(1)
    return len(ops), inrun, (top[0][1] if top else 0), (top[0][0] if top else "")


def main(draft_dir, tar_path, out_path):
    drafts = []
    for f in sorted(os.listdir(draft_dir)):
        if re.fullmatch(r"ch\d+\.md", f):
            t = io.open(os.path.join(draft_dir, f), encoding="utf-8", errors="replace").read()
            n, r, c, w = score(t)
            drafts.append({"file": f, "words": len(t.split()), "paras": n, "in_runs": r, "top": w, "top_n": c})
    piece = int(statistics.median(d["words"] for d in drafts))
    cat = {}
    for l in gzip.open(WB + "/corpus/CATALOGUE.jsonl.gz", "rt", encoding="utf-8"):
        d = json.loads(l)
        if d.get("form") == "novel" and d.get("language") == "en":
            cat[d["id"]] = d
    members = {}
    for l in io.open(WB + "/corpus/TEXTS_INDEX.jsonl", encoding="utf-8"):
        d = json.loads(l)
        if d["text_asset"].endswith(os.path.basename(tar_path)) and d["id"] in cat and d["bytes"] > 150000:
            members[d["member"]] = d["id"]
    novels = []
    with tarfile.open(tar_path, "r:gz") as tf:
        for m in tf:
            if m.name not in members:
                continue
            raw = tf.extractfile(m).read().decode("utf-8", "replace").replace("\r\n", "\n")
            s = re.search(r"\*\*\* ?START OF.*?\n", raw)
            e = re.search(r"\*\*\* ?END OF", raw)
            body = raw[s.end() if s else 0: e.start() if e else len(raw)]
            # cut on paragraph boundaries into pieces of about `piece` words
            pieces, cur, cw = [], [], 0
            for p in re.split(r"\n\s*\n", body):
                cur.append(p)
                cw += len(p.split())
                if cw >= piece:
                    pieces.append("\n\n".join(cur))
                    cur, cw = [], 0
            pieces = pieces[1:-1][:12]
            if len(pieces) < 4:
                continue
            n = r = c = 0
            for p in pieces:
                a, b, k, _ = score(p)
                n, r, c = n + a, r + b, c + k
            if n < 50:
                continue
            d = cat[members[m.name]]
            novels.append({"id": d["id"], "title": d["title"], "paras": n, "in_runs": r,
                           "runs_per100": round(100 * r / n, 2), "top_share": round(c / n, 3)})
            if len(novels) >= 25:
                break
    for d in drafts:
        d["runs_per100"] = round(100 * d["in_runs"] / max(d["paras"], 1), 2)
        d["top_share"] = round(d["top_n"] / max(d["paras"], 1), 3)
    dn, dr, dc = (sum(d[k] for d in drafts) for k in ("paras", "in_runs", "top_n"))
    nr = [d["runs_per100"] for d in novels]
    dper = 100 * dr / max(dn, 1)
    res = {"rule": f"3+ consecutive prose paragraphs (8+ words, no dialogue) with the same first word; {piece}-word units",
           "drafts": {"chapters": len(drafts), "paras": dn, "runs_per100": round(dper, 2),
                      "top_share": round(dc / max(dn, 1), 3),
                      "top_openers": collections.Counter(d["top"] for d in drafts).most_common(5)},
           "novels": {"n": len(novels), "paras": sum(d["paras"] for d in novels),
                      "runs_per100_median": statistics.median(nr) if nr else None,
                      "runs_per100_pooled": round(100 * sum(d["in_runs"] for d in novels) / max(sum(d["paras"] for d in novels), 1), 2),
                      "top_share_median": statistics.median(d["top_share"] for d in novels) if novels else None,
                      "share_of_novels_at_or_above_drafts": round(sum(x >= dper for x in nr) / max(len(nr), 1), 2)},
           "draft_chapters": drafts, "novel_rows": novels}
    io.open(out_path, "w", encoding="utf-8").write(json.dumps(res, indent=1, ensure_ascii=False))
    print(res["rule"])
    print("drafts", res["drafts"])
    print("novels", res["novels"])


if __name__ == "__main__":
    main(*sys.argv[1:4])
