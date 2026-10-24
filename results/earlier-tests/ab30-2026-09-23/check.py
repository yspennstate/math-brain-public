"""Compare derive.py's results.json with the published claims in CLAIMS.json, one line per claim.

    python check.py [results.json] [CLAIMS.json]      exit 0 when every claim matches, 1 otherwise

It imports nothing from derive.py: the two files are the whole interface. A claim with no derived value, or a derived
value with no claim, is reported and fails the check.

Since 29 Sep 2026 (scheduled audit account04/B20 r37, B20-R37-MISSING-STATUS-SILENTLY-SKIPPED-20260929) the release is
checked as a closed package before any claim is compared:
- every file MANIFEST.json lists must be present with its recorded size and SHA-256 (a file changed after the manifest was
  written fails here, before the comparison);
- every claim's source must be bound: STATUS.json is a copy inside the release, listed in the manifest, and a claim that
  names it fails when the copy is missing ("missing claim source"); REPORT.md is bound by the git blob id recorded under
  MANIFEST.json's "external" (the claims copy its numbers; the release does not need the file itself);
- nothing outside this folder decides the result. When the campaign's own ../STATUS.json or ../REPORT.md is present it
  is compared with what the release holds and the difference is reported on its own line, without failing the check.
"""
import hashlib
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


class DuplicateMember(ValueError):
    pass


def _no_dup(pairs):
    names = [k for k, _v in pairs]
    dup = sorted({k for k in names if names.count(k) > 1})
    if dup:
        # json.loads keeps the last of two same-named members and hides the first (account03/B17 r67,
        # B17-R44-DUPLICATE-JSON-MEMBER-SMUGGLING-013); check_release_manifest.py refuses it, and so does this
        raise DuplicateMember("duplicate_json_member %s" % dup[:4])
    return dict(pairs)


def load(p):
    return json.load(io.open(p, encoding="utf-8"), object_pairs_hook=_no_dup)


def git_blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def verify_manifest(here):
    """(manifest, problems): every listed file present with its size and SHA-256."""
    path = os.path.join(here, "MANIFEST.json")
    if not os.path.isfile(path):
        return {}, ["missing MANIFEST.json"]
    try:
        man = load(path)
    except DuplicateMember as exc:
        return {}, ["MANIFEST.json refused: %s" % exc]
    bad = []
    for name, meta in sorted((man.get("files") or {}).items()):
        p = os.path.join(here, *name.split("/"))
        if not os.path.isfile(p):
            bad.append("missing file: " + name)
            continue
        data = open(p, "rb").read()
        if len(data) != meta.get("bytes") or hashlib.sha256(data).hexdigest() != meta.get("sha256"):
            bad.append("changed since the manifest: " + name)
    return man, bad


def claim_sources(claims):
    """Each claim's source file, read off published_in; "the same ..." takes the previous claim's source."""
    out, prev = {}, None
    for cid, c in claims["claims"].items():
        text = str(c.get("published_in") or "")
        m = re.match(r"\s*(REPORT\.md|STATUS\.json)\b", text)
        if m:
            prev = m.group(1)
        elif not text.lower().startswith("the same"):
            prev = None
        out[cid] = prev
    return out


def compare(res, claims, status_path=None, man=None):
    v = res["values"]
    c = claims["claims"]
    lines, bad = [], []
    for cid in sorted(set(v) | set(c)):
        if cid not in c:
            lines.append("%-40s derived %-26s no claim" % (cid, json.dumps(v[cid])))
            bad.append(cid)
            continue
        if cid not in v:
            lines.append("%-40s %-34s claimed %s, nothing derived" % (cid, "", json.dumps(c[cid]["expected"])))
            bad.append(cid)
            continue
        ok = v[cid] == c[cid]["expected"]
        lines.append("%-40s derived %-26s claimed %-26s %s" % (cid, json.dumps(v[cid]), json.dumps(c[cid]["expected"]),
                                                                "ok" if ok else "DIFFERS"))
        if not ok:
            bad.append(cid)
    if man is not None:
        files = man.get("files") or {}
        external = man.get("external") or {}
        for cid, src in claim_sources(claims).items():
            if src is None:
                lines.append("%-40s unbound claim source: %r" % (cid, c[cid].get("published_in")))
                bad.append(cid + " source")
            elif src == "STATUS.json" and "STATUS.json" not in files:
                lines.append("%-40s its source STATUS.json is not in the manifest" % cid)
                bad.append(cid + " source")
            elif src == "REPORT.md" and not (external.get("REPORT.md") or {}).get("git_blob"):
                lines.append("%-40s its source REPORT.md has no bound blob id" % cid)
                bad.append(cid + " source")
    if "STATUS.pairs_done" in c:
        if not status_path or not os.path.isfile(status_path):
            lines.append("%-40s missing claim source: STATUS.json" % "STATUS.json itself")
            bad.append("STATUS.json itself")
        else:
            s = load(status_path).get("pairs_done")
            ok = s == c["STATUS.pairs_done"]["expected"]
            lines.append("%-40s file says %-24s claimed %-26s %s" % ("STATUS.json itself", json.dumps(s),
                                                                      json.dumps(c["STATUS.pairs_done"]["expected"]),
                                                                      "ok" if ok else "DIFFERS"))
            if not ok:
                bad.append("STATUS.json itself")
    return lines, bad


def ambient(here, status_path, man):
    """Lines about the campaign's own files next to the release; information only."""
    out = []
    camp_status = os.path.join(here, "..", "STATUS.json")
    if os.path.isfile(camp_status) and status_path and os.path.isfile(status_path):
        a, b = load(camp_status).get("pairs_done"), load(status_path).get("pairs_done")
        out.append("campaign ../STATUS.json says pairs_done %s; the release copy says %s%s" % (
            a, b, "" if a == b else " (the campaign has moved on; the release is checked against its own copy)"))
    rep = os.path.join(here, "..", "REPORT.md")
    bound = ((man or {}).get("external") or {}).get("REPORT.md") or {}
    if os.path.isfile(rep) and bound.get("git_blob"):
        now = git_blob_id(open(rep, "rb").read())
        out.append("campaign ../REPORT.md is %s the version the claims were copied from (blob %s)" % (
            "still" if now == bound["git_blob"] else "NO LONGER", bound["git_blob"][:12]))
    return out


def main():
    res_p = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "results.json")
    cl_p = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "CLAIMS.json")
    man, mbad = verify_manifest(HERE)
    if mbad:
        print("\n".join(mbad))
        print("\nthe release is not the one its manifest describes; no claim was compared")
        return 1
    status_path = os.path.join(HERE, "STATUS.json")
    try:
        res, claims = load(res_p), load(cl_p)
    except DuplicateMember as exc:
        print("refused: %s" % exc)
        return 1
    lines, bad = compare(res, claims, status_path, man)
    print("\n".join(lines))
    print("\nNot recomputable from these rows:")
    for x in res.get("not_recomputable") or ["nothing"]:
        print("  " + x)
    for x in ambient(HERE, status_path, man):
        print(x)
    print("\n%s" % ("every claim matches" if not bad else "DIFFERS: " + ", ".join(bad)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
