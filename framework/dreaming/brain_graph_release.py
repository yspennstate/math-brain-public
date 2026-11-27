"""Publish the full brain graph store as a dated GitHub release, once a day.

The store (~/.claude/brain_graph/store, rebuilt every six hours) goes to yspennstate/brain-repo as
release brain-graph-full-<YYYY-MM-DD>, in the same shape as the first one (an agent, 1 Nov 2026):
edges.npz, nodes.json.gz, uses.json.gz, first_touch.json.gz and manifest.json (bytes and sha256 of every
uncompressed file, plus the build's meta). The Mac's brain_release_check.py takes the newest brain-graph-full-* tag,
checks every file against that manifest and swaps it in. A README and the manifest also go to main under
12_cognitive_architecture/brain_graph/exports/brain_graph_full_<date>/.

Old releases are never deleted (brain data law). net.sqlite3 is not re-sent: it is the older network, unchanged since
20 Oct, and it sits in brain-graph-full-2026-11-01.

Asked by the Mac (a fleet message, an agent) under the author's 1 Nov order that brain results reach every
computer's agents; written by an agent on 3 Nov 2026.

    python brain_graph_release.py            publish today's release if the store changed since the last one
    python brain_graph_release.py --dry-run  snapshot and hash only, upload nothing
"""
import datetime, gzip, hashlib, importlib.util, json, os, shutil, sys, time, urllib.error, urllib.request

HOME = os.path.expanduser("~")
STORE = os.path.join(HOME, ".claude", "brain_graph", "store")
STAGE = os.path.join(HOME, "bgr_stage")            # a copy, removed after the upload is checked
LOG = os.path.join(HOME, ".claude", "brain_graph", "logs", "graph_release.log")
REPO = "yspennstate/brain-repo"
PREFIX = "brain-graph-full-"
FILES = ("nodes.json", "uses.json", "first_touch.json", "edges.npz")
GZ = ("nodes.json", "uses.json", "first_touch.json")

spec = importlib.util.spec_from_file_location("fb", os.path.join(HOME, ".claude", "dreaming", "fleet_board.py"))
fb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fb)


def log(msg):
    line = "%s %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), msg)
    print(line, flush=True)
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def snapshot():
    """Copy the four store files while no rebuild is writing them: the mtimes must not move during the copy, and
    the four must come from one build (written within ten minutes of each other)."""
    for attempt in range(6):
        before = {n: os.stat(os.path.join(STORE, n)).st_mtime for n in FILES}
        # 600 s, not 120 (9 Nov, an agent): on the loaded laptop one build wrote its four files over 295 s
        # (run_graph.log 10:41 build line), so 120 s refused a single build six times and failed the release.
        if max(before.values()) - min(before.values()) > 600:
            log("store files are from different builds (spread %.0f s); waiting" % (max(before.values()) - min(before.values())))
            time.sleep(300)
            continue
        if time.time() - max(before.values()) < 120:
            time.sleep(180)                         # a rebuild may still be writing
            continue
        shutil.rmtree(STAGE, ignore_errors=True)
        os.makedirs(STAGE)
        for n in FILES:
            shutil.copy2(os.path.join(STORE, n), os.path.join(STAGE, n))
        after = {n: os.stat(os.path.join(STORE, n)).st_mtime for n in FILES}
        if after == before:
            return max(before.values())
        log("store changed during the copy; again")
    raise RuntimeError("could not take a still snapshot of the store")


def build_manifest():
    man = {}
    for n in FILES:
        p = os.path.join(STAGE, n)
        man[n] = {"bytes": os.path.getsize(p), "sha256": sha256(p)}
        if n in GZ:
            with open(p, "rb") as fi, open(p + ".gz", "wb") as raw:
                with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as fo:
                    shutil.copyfileobj(fi, fo, 1 << 20)
            man[n]["gz"] = n + ".gz"
            man[n]["gz_bytes"] = os.path.getsize(p + ".gz")
    nodes = json.load(open(os.path.join(STAGE, "nodes.json"), encoding="utf-8"))
    man["meta"] = nodes.get("meta", {})
    import numpy as np
    z = np.load(os.path.join(STAGE, "edges.npz"))
    counts = {"nodes": len(nodes["names"]), "lagged": int(z["keys"].size), "co": int(z["co_keys"].size)}
    del nodes, z
    with open(os.path.join(STAGE, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(man, f, indent=1)
    return man, counts


def last_release():
    # Three tries (7 Nov, an agent): on the loaded laptop the first API call of the run timed out as HTTP 0 on
    # 3 Nov and 6 Nov and the whole day's release was lost; a 5xx or a timeout is retried after 60 s and 180 s.
    # 9 Nov (an agent): 8 and 9 Nov failed on HTTP 403 - the fleet drains the core REST limit most of each hour
    # and a 403/429 was treated as final. A rate-limit refusal now waits for the hourly window (10, 20, 30 min).
    # timeout/5xx: retry after 60 s and 180 s; rate limit (403/429): retry after 10, 20 and 30 min; other 4xx: stop.
    plan = {"transient": [60, 180], "ratelimit": [600, 1200, 1800]}
    while True:
        st, r = fb.api("GET", "/repos/%s/releases?per_page=50" % REPO, timeout=60)
        if st == 200:
            break
        kind = "ratelimit" if st in (403, 429) else ("transient" if (not st or st >= 500) else None)
        if kind is None or not plan[kind]:
            break
        wait = plan[kind].pop(0)
        log("release list: HTTP %s, retrying in %d s" % (st, wait))
        time.sleep(wait)
    if st != 200:
        raise RuntimeError("release list: HTTP %s" % st)
    rel = [x for x in r if x["tag_name"].startswith(PREFIX) and not x.get("draft")]
    rel.sort(key=lambda x: x["tag_name"])
    return rel


def release_manifest(rel):
    a = {x["name"]: x for x in rel["assets"]}.get("manifest.json")
    if not a:
        return {}
    req = urllib.request.Request(a["url"], headers={"Authorization": "Bearer " + fb.token(),
                                                   "Accept": "application/octet-stream"})
    with urllib.request.urlopen(req, timeout=120) as f:
        return json.loads(f.read())


def upload(rel, name):
    p = os.path.join(STAGE, name)
    size = os.path.getsize(p)
    url = rel["upload_url"].split("{")[0] + "?name=" + name
    for attempt in range(3):
        with open(p, "rb") as f:
            req = urllib.request.Request(url, data=f, method="POST", headers={
                "Authorization": "Bearer " + fb.token(), "Accept": "application/vnd.github+json",
                "Content-Type": "application/octet-stream", "Content-Length": str(size)})
            try:
                with urllib.request.urlopen(req, timeout=3600) as r:
                    return json.loads(r.read())
            except urllib.error.HTTPError as e:
                body = e.read()[:300]
                log("upload %s: HTTP %s %s" % (name, e.code, body))
                if e.code == 422:            # a half-sent asset with this name exists: remove it and send again
                    st, rr = fb.api("GET", "/repos/%s/releases/%s" % (REPO, rel["id"]), timeout=60)
                    for a in rr.get("assets", []):
                        if a["name"] == name:
                            fb.api("DELETE", "/repos/%s/releases/assets/%s" % (REPO, a["id"]), timeout=60)
            except Exception as e:
                log("upload %s: %s" % (name, e))
        time.sleep(30)
    raise RuntimeError("upload of %s failed three times" % name)


README = """# Brain graph, full store ({date})

The whole brain_graph store from the source machine, built {built} (local time) from {events:,} events over {sessions:,}
sessions. It is the release `{tag}` of this repository; the store files are release assets because edges.npz is
over GitHub's 100 MB file limit. A new release like this one is published every day by the task BrainGraphRelease
(~/.claude/dreaming/brain_graph_release.py); older releases are kept.

| | count |
|---|---|
| nodes | {nodes:,} |
| lagged (directed) edges | {lagged:,} |
| co-activation edges | {co:,} |
| edges in all | {edges:,} |

| asset | bytes | sha256 of the uncompressed file |
|---|---|---|
{rows}

manifest.json, beside this README and in the release, holds these hashes and the build's meta block. GitHub's own
sha256 digest of every asset was checked against the local file after the upload.

## Reading it

Download with `gh release download {tag} -R {repo}` (a private repo: the plain browser link answers 404).
nodes.json holds `names` (the index is the node id) and `meta`; edges.npz holds `keys`/`cnt` (lagged edges),
`co_keys`/`co_cnt` (co-activation edges), `p_first`/`p_last`, `out_sum` and `in_w`. A key packs source and target:
source `key >> 32`, target `key & 0xFFFFFFFF`. The format is the one described in
brain_graph_full_2026-11-01/README.md. net.sqlite3, the older 74,138-node network, is unchanged since 20 Oct and is
only in the release brain-graph-full-2026-11-01.
"""


def put_file(path, text, msg):
    url = "/repos/%s/contents/%s" % (REPO, path)
    st, cur = fb.api("GET", url + "?ref=main", timeout=60)
    body = {"message": msg, "content": __import__("base64").b64encode(text.encode("utf-8")).decode(), "branch": "main"}
    if st == 200:
        body["sha"] = cur["sha"]
    st, r = fb.api("PUT", url, body, timeout=120)
    if st not in (200, 201):
        raise RuntimeError("PUT %s: HTTP %s %s" % (path, st, str(r)[:200]))
    return r["commit"]["sha"]


def main():
    dry = "--dry-run" in sys.argv
    built_ts = snapshot()
    man, counts = build_manifest()
    built = datetime.datetime.fromtimestamp(built_ts).strftime("%Y-%m-%d %H:%M")
    log("snapshot of the %s build: %d nodes, %d + %d edges, edges sha %s" % (
        built, counts["nodes"], counts["lagged"], counts["co"], man["edges.npz"]["sha256"][:12]))
    if dry:
        return 0
    rels = last_release()
    names = ["nodes.json.gz", "uses.json.gz", "first_touch.json.gz", "edges.npz", "manifest.json"]  # manifest last:
    # a release with its manifest is a finished one, for this script and for the Mac's brain_release_check.py
    if rels:
        prev = release_manifest(rels[-1])
        complete = set(names) <= {a["name"] for a in rels[-1]["assets"]}
        if prev.get("edges.npz", {}).get("sha256") == man["edges.npz"]["sha256"] and complete:
            log("store unchanged since %s; nothing to publish" % rels[-1]["tag_name"])
            shutil.rmtree(STAGE, ignore_errors=True)
            return 0
    date = datetime.date.fromtimestamp(built_ts).isoformat()
    tag = PREFIX + date
    rel = next((r for r in rels if r["tag_name"] == tag), None)
    if rel is not None and rel is not rels[-1]:
        log("%s exists and is not the newest release; leaving it" % tag)
        return 0
    if rel is not None and release_manifest(rel).get("edges.npz", {}).get("sha256") not in (None, man["edges.npz"]["sha256"]):
        # today's release already holds a finished build; a release is never rewritten, the next day's run sends this one
        log("%s already published with another build; the next run publishes this one" % tag)
        shutil.rmtree(STAGE, ignore_errors=True)
        return 0
    if rel is None:
        st, rel = fb.api("POST", "/repos/%s/releases" % REPO, {
            "tag_name": tag, "target_commitish": "main", "name": "Brain graph, full store (%s)" % date,
            "body": "The brain_graph store built %s: %d nodes, %d lagged + %d co-activation edges. "
                    "manifest.json has the sha256 of every uncompressed file. README: "
                    "12_cognitive_architecture/brain_graph/exports/brain_graph_full_%s/README.md on main."
                    % (built, counts["nodes"], counts["lagged"], counts["co"], date)}, timeout=60)
        if st != 201:
            raise RuntimeError("create release: HTTP %s %s" % (st, str(rel)[:200]))
        log("created release %s" % tag)
    have = {a["name"]: a for a in rel.get("assets", [])}
    bad = []
    for n in names:
        local = sha256(os.path.join(STAGE, n))
        a = have.get(n)
        if a and a.get("digest") == "sha256:" + local:
            continue
        if a:                                       # a different file under this name (an earlier build today)
            fb.api("DELETE", "/repos/%s/releases/assets/%s" % (REPO, a["id"]), timeout=60)
        t0 = time.time()
        a = upload(rel, n)
        ok = a.get("digest") == "sha256:" + local and a.get("size") == os.path.getsize(os.path.join(STAGE, n))
        log("uploaded %s (%d B, %.0f s) digest %s" % (n, a.get("size", 0), time.time() - t0, "matches" if ok else
                                                         "DIFFERS: %s vs %s" % (a.get("digest"), local[:12])))
        if not ok:
            bad.append(n)
    if bad:
        raise RuntimeError("digest mismatch on %s" % bad)
    rows = []
    for n in FILES:
        asset = man[n].get("gz", n)
        rows.append("| %s | %s | %s |" % (asset, format(os.path.getsize(os.path.join(STAGE, asset)), ","), man[n]["sha256"]))
    meta = man["meta"]
    text = README.format(date=date, built=built, events=meta.get("events", 0), sessions=meta.get("sessions", 0), tag=tag,
                         repo=REPO, nodes=counts["nodes"], lagged=counts["lagged"], co=counts["co"],
                         edges=counts["lagged"] + counts["co"], rows="\n".join(rows))
    d = "12_cognitive_architecture/brain_graph/exports/brain_graph_full_%s" % date
    c1 = put_file(d + "/README.md", text, "brain graph release %s [skip ci]" % date)
    c2 = put_file(d + "/manifest.json", open(os.path.join(STAGE, "manifest.json"), encoding="utf-8").read(),
                  "brain graph release %s manifest [skip ci]" % date)
    log("published %s; README %s, manifest %s" % (tag, c1[:8], c2[:8]))
    shutil.rmtree(STAGE, ignore_errors=True)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        log("FAILED: %s" % e)
        sys.exit(1)
