"""Do draft chapters write the same sentence twice more often than published novels do?

    python -s -X utf8 sentence_repeat_rate.py <draft_dir> <corpus_batch.tar.gz> <out.json>

The test is process_lint.repeats() moved to prose: a sentence of at least 14 words whose word pairs are at least 70 pct
shared with an earlier sentence of the same chapter, at least 3 sentences back. A draft chapter is one unit; a novel is cut
into pieces of the drafts' median chapter length so both sides see the same distance. Rate = repeating sentences per 1,000
qualifying sentences. Novels are untrusted text, read as data only. Draft files are opened read-only.
"""
import gzip, io, json, os, re, statistics, sys, tarfile

WB = os.environ.get("WRITING_BRAIN_DIR", "writing_brain")  # holds corpus/CATALOGUE.jsonl.gz and corpus/TEXTS_INDEX.jsonl
N, SHARE, GAP = 14, 0.7, 3


def sentences(text):
    out = []
    for s in re.finditer(r"[^.!?]+[.!?]", text):
        ws = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", s.group(0))]
        if len(ws) >= N:
            out.append((ws, set(zip(ws, ws[1:]))))
    return out


def repeats(text):
    """(qualifying sentences, repeating sentences, examples) for one unit; a bigram index keeps it linear-ish."""
    ss = sentences(text)
    idx, hits, ex = {}, 0, []
    for i, (ws, pa) in enumerate(ss):
        cand = {}
        for p in pa:
            for j in idx.get(p, ()):
                if i - j >= GAP:
                    cand[j] = cand.get(j, 0) + 1
        for j, c in cand.items():
            if c / min(len(pa), len(ss[j][1])) >= SHARE:
                hits += 1
                if len(ex) < 3:
                    ex.append((" ".join(ss[j][0][:14]), " ".join(ws[:14])))
                break
        for p in pa:
            idx.setdefault(p, []).append(i)
    return len(ss), hits, ex


def main(draft_dir, tar_path, out_path):
    drafts = []
    for f in sorted(os.listdir(draft_dir)):
        if re.fullmatch(r"ch\d+\.md", f):
            t = io.open(os.path.join(draft_dir, f), encoding="utf-8", errors="replace").read()
            n, h, ex = repeats(t)
            drafts.append({"file": f, "words": len(t.split()), "sents": n, "repeats": h, "examples": ex})
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
            words = raw[s.end() if s else 0: e.start() if e else len(raw)].split()
            pieces = [" ".join(words[k:k + piece]) for k in range(0, len(words) - piece + 1, piece)]
            pieces = pieces[1:-1][:12]                       # skip front matter and the last scrap
            if len(pieces) < 4:
                continue
            n = h = 0
            ex = []
            for p in pieces:
                a, b, e2 = repeats(p)
                n, h, ex = n + a, h + b, ex + e2
            d = cat[members[m.name]]
            novels.append({"id": d["id"], "title": d["title"], "year": d.get("year"), "pieces": len(pieces),
                           "sents": n, "repeats": h, "per1000": round(1000 * h / max(n, 1), 2), "examples": ex[:2]})
            if len(novels) >= 25:
                break
    for d in drafts:
        d["per1000"] = round(1000 * d["repeats"] / max(d["sents"], 1), 2)
    dn, dh = sum(d["sents"] for d in drafts), sum(d["repeats"] for d in drafts)
    nn, nh = sum(d["sents"] for d in novels), sum(d["repeats"] for d in novels)
    res = {"rule": f"{N}+ words, {SHARE:.0%} shared word pairs, {GAP}+ sentences back, within a {piece}-word unit",
           "drafts": {"chapters": len(drafts), "sents": dn, "repeats": dh, "per1000": round(1000 * dh / max(dn, 1), 2),
                      "chapter_median_per1000": statistics.median(d["per1000"] for d in drafts)},
           "novels": {"n": len(novels), "sents": nn, "repeats": nh, "per1000": round(1000 * nh / max(nn, 1), 2),
                      "novel_median_per1000": statistics.median(d["per1000"] for d in novels) if novels else None,
                      "share_of_novels_above_draft_rate": round(sum(d["per1000"] > 1000 * dh / max(dn, 1) for d in novels)
                                                                / max(len(novels), 1), 2)},
           "draft_chapters": drafts, "novel_rows": novels}
    io.open(out_path, "w", encoding="utf-8").write(json.dumps(res, indent=1, ensure_ascii=False))
    print(res["rule"])
    print("drafts", res["drafts"])
    print("novels", res["novels"])


if __name__ == "__main__":
    main(*sys.argv[1:4])
