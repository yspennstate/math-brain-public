"""test_claim_vectors_manifest.py - every claim-vector file carries the SHA-256 of its bytes, and bytes their manifest
does not name are refused (29 Sep 2026, an agent; scheduled audits account03/B11 r90 and account04/B17 r74,
B11-R77-SEMANTIC-GENERATION-CRC32-COLLISION-20260929-R90 and B17-R74-CRC32-COLLISION-PRESERVES-SEMANTIC-CACHE-
GENERATION-20260929).

    python test_claim_vectors_manifest.py [--hook MATH_SENSE.py] [--vecs MATH_CLAIM_VECS.py] [--src MATH_BRAIN_SRC]
                                          [--old-vecs OLD.py] [--old-src OLD_SRC]

Fixture stores and vector files live in a temporary folder; the live store and its vectors are never opened.
 W1  extend() publishes claim_embeddings.npz.sha256 naming the bytes it wrote, and the real loader reads the file with
     its manifest matching; the dated copy it keeps has a manifest naming the copy's bytes
 W2  status() says the manifest names the file
 W3  the file changed in place after it was published: status() is not ok and says so, the loader refuses it, and the
     real hook names nobody (C5)
 W4  seal() records the file as it is; status() and the loader take it again; seal() refuses a file that does not load
 W5  a replace that fails puts the old manifest back: the old file still loads, under its own digest
 W6  a crash between the manifest and the file leaves the channel closed, and the next extend() heals it
 W7  a reader holds the file open while extend() replaces it (Windows refuses the replace then): the writer waits and
     finishes; while it waits the loader refuses the old bytes under the new manifest, and never reads them as current
     (C6)
 W8  rebuild(out=...) publishes a manifest beside the file it writes
With --old-vecs, the writer before this change publishes no manifest (N1); with --old-src, the loader before it reads a
file whose manifest names other bytes (N2). Each shows its check can fail.
"""
import hashlib
import importlib.machinery
import importlib.util
import json
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]


def _arg(flag, default=None):
    return os.path.abspath(ARGS[ARGS.index(flag) + 1]) if flag in ARGS else default


HOOK = _arg("--hook", os.path.join(HERE, "math_sense.py"))
VECS = _arg("--vecs", os.path.join(HERE, "math_claim_vecs.py"))
SRC = _arg("--src", r"~\math-brain-build\src")
OLD_VECS, OLD_SRC = _arg("--old-vecs"), _arg("--old-src")
fails, ran = [], []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def load(path, name):
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


OLD_CARD, SIDE = "claim_old_prime_order_is_cyclic", "claim_side_lagrange"
BODY = {OLD_CARD: "every group of prime order is cyclic", SIDE: "the order of a subgroup divides the order"}
EMB = {BODY[OLD_CARD]: [0.8, 0.6], BODY[SIDE]: [0.0, 1.0]}
Q = [1.0, 0.0]


def node_digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]


def fake_embed(text):
    v = EMB.get(text)
    return None if v is None else np.asarray(v, dtype=np.float32)


def make_store(folder, claims):
    path = os.path.join(folder, "brain.sqlite3")
    con = sqlite3.connect(path)
    con.executescript("create table nodes (id text primary key, kind text, title text, body text, digest text);"
                      "create table claims (id text primary key);"
                      "create table edges (kind text, source_id text, target_id text);")
    for c in claims:
        con.execute("insert into nodes values (?, 'claim', ?, ?, ?)", (c, c, BODY[c], node_digest(BODY[c])))
        con.execute("insert into claims values (?)", (c,))
    con.commit()
    con.close()
    return path


def make_vectors(folder, ids, name="claim_embeddings.npz", sources=None, digests=None):
    sources = sources or ["body"] * len(ids)
    fields = dict(slugs=np.array(ids), vecs=np.asarray([EMB[BODY[i]] for i in ids], dtype=np.float32),
                  model=np.array("BAAI/bge-small-en-v1.5"), text_sha256=np.array("ext:0000"),
                  built_at=np.array("fixture"), schema_version=np.array("2"),
                  node_digests=np.array(digests or [node_digest(BODY[i]) for i in ids]), row_source=np.array(sources),
                  row_body_cos=np.array([1.0] * len(ids), dtype=np.float32))
    path = os.path.join(folder, name)
    np.savez(path, **fields)
    return path


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def named(path):
    try:
        with open(path + ".sha256", "rb") as fh:
            return fh.read().decode("ascii").split()[0]
    except FileNotFoundError:
        return None


def loader(src, vec_path):
    """The real loader of src, in a child process, on this file: (loaded, identity or None, error)."""
    code = ("import json, os, sys; sys.path.insert(0, %r); os.environ['MATH_BRAIN_CLAIM_VECS'] = %r\n"
            "from math_brain import semantic as S\n"
            "try:\n    S._load_artifact(); print(json.dumps([True, getattr(S, 'artifact_identity', dict)(), '']))\n"
            "except Exception as exc:\n    print(json.dumps([False, None, str(exc)[:200]]))\n") % (src, vec_path)
    p = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=120,
                       creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    try:
        return tuple(json.loads(p.stdout.strip().splitlines()[-1]))
    except Exception:
        return (False, None, (p.stderr or p.stdout)[-200:])


def hook_top(store, vec_path):
    """The real hook's _semantic_top on this store and file, through the real loader, in a child process (the query
    encoder is the one piece stood in: it returns the fixture's two-dimensional question)."""
    # the hook puts BUILD_SRC first on the path in main() before anything reaches _semantic_top; a bare import of
    # math_brain here would find another checkout
    code = ("import json, os, sys, types, importlib.machinery, importlib.util\n"
            "sys.path[:0] = [os.path.dirname(%r), %r]\n"
            "os.environ['MATH_BRAIN_CLAIM_VECS'] = %r\n"
            "import numpy as np\n"
            "loader = importlib.machinery.SourceFileLoader('ms_manifest', %r)\n"
            "spec = importlib.util.spec_from_file_location('ms_manifest', %r, loader=loader)\n"
            "m = importlib.util.module_from_spec(spec); loader.exec_module(m)\n"
            "sys.path.insert(0, m.BUILD_SRC)\n"
            "from math_brain import semantic as S\n"
            "S._query_encoder = lambda: types.SimpleNamespace(embed=lambda t: np.asarray(%r, dtype=np.float32))\n"
            "m.STORE_PATH = %r\n"
            "top = m._semantic_top('which groups of prime order are cyclic')\n"
            "print(json.dumps([top, ''.join(m._SEMTOP_WHY.values()), S.__file__]))\n") % (
        HOOK, os.path.join(os.path.expanduser("~"), ".claude", "dreaming"), vec_path, HOOK, HOOK, Q, store)
    p = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=180,
                       creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    try:
        return tuple(json.loads(p.stdout.strip().splitlines()[-1]))
    except Exception:
        return (None, "child failed: " + (p.stderr or p.stdout)[-300:], "")


def main():
    tmp = tempfile.mkdtemp(prefix="claim_vecs_manifest_")
    try:
        mcv = load(VECS, "mcv_manifest")
        store = make_store(tmp, [OLD_CARD, SIDE])
        live = make_vectors(tmp, [OLD_CARD])                         # SIDE has no vector yet
        os.environ["MATH_BRAIN_CLAIM_VECS"] = live
        r = mcv.extend(store, live, embed=fake_embed)
        backups = [f for f in os.listdir(tmp) if f.startswith("claim_embeddings.npz.bak_") and not f.endswith(".sha256")]
        bak = os.path.join(tmp, backups[0]) if backups else ""
        got = loader(SRC, live)
        check(r[0] == 1 and r[2] == "" and named(live) == sha(live) and got[0] is True
              and got[1] == {"sha256": sha(live), "manifest": "match"}
              and bool(bak) and named(bak) == sha(bak),
              "W1 extend() publishes the manifest (%r, manifest names the file %s, loader %r, dated copy named %s)"
              % (r, named(live) == sha(live), got[:2], bool(bak) and named(bak) == sha(bak)))
        ok, line = mcv.status(store)
        check(ok is True and "named by its manifest" in line, "W2 status: %r" % line)
        top, why, where = hook_top(store, live)
        check(top == OLD_CARD and why == "winner" and os.path.normcase(os.path.dirname(os.path.dirname(where)))
              == os.path.normcase(SRC),
              "W2b the real hook names its winner over the published file (%r, %r, loader from %s)" % (top, why, where))

        # W3: the bytes change in place after publication (the manifest is left as it was)
        with open(live, "rb") as fh:
            data = bytearray(fh.read())
        with np.load(live, allow_pickle=False) as d:
            fields = {k: d[k] for k in d.files}
        fields["vecs"] = np.asarray([[0.6, 0.8], [0.0, 1.0]], dtype=np.float32)
        other = os.path.join(tmp, "other.npz")
        np.savez(other, **fields)
        with open(other, "rb") as fh:
            new_bytes = fh.read()
        with open(live, "r+b") as fh:                           # same file, rewritten in place
            fh.write(new_bytes)
            fh.truncate()
        ok, line = mcv.status(store)
        got = loader(SRC, live)
        top, why, _ = hook_top(store, live)
        check(ok is False and "manifest names" in line and got[0] is False and "writer published" in got[2]
              and top is None and "unavailable" in why,
              "W3 changed after publication: status %r, loader %r, hook %r / %r" % (line[:100], got, top, why))

        digest, note = mcv.seal(store)
        ok, line = mcv.status(store)
        got = loader(SRC, live)
        bad = os.path.join(tmp, "unreadable")
        os.makedirs(bad)
        with open(os.path.join(bad, "claim_embeddings.npz"), "wb") as fh:
            fh.write(b"not a zip")
        d2, n2 = mcv.seal(store, os.path.join(bad, "claim_embeddings.npz"))
        check(note == "" and digest == sha(live) == named(live) and ok is True and got[0] is True
              and got[1]["manifest"] == "match" and d2 == "" and "not sealed" in n2
              and not os.path.exists(os.path.join(bad, "claim_embeddings.npz.sha256")),
              "W4 seal records the file as it is (%s), status %r, loader %r; an unreadable file is refused: %r"
              % (digest[:12], ok, got[:2], n2))

        # W5: the replace fails; the old manifest comes back and the old file still loads under its own digest
        store5 = os.path.join(tmp, "w5")
        os.makedirs(store5)
        s5 = make_store(store5, [OLD_CARD, SIDE])
        v5 = make_vectors(store5, [OLD_CARD])
        mcv.seal(s5, v5)
        before = sha(v5)
        real = mcv._replace

        def refuse_the_file(src, dst):
            if dst == v5:
                raise PermissionError("held by a reader")
            return real(src, dst)

        mcv._replace = refuse_the_file
        try:
            mcv.extend(s5, v5, embed=fake_embed)
            raised = False
        except PermissionError:
            raised = True
        finally:
            mcv._replace = real
        got = loader(SRC, v5)
        check(raised and sha(v5) == before and named(v5) == before and got[0] is True and got[1]["sha256"] == before,
              "W5 a failed replace restores the old manifest (raised %s, file unchanged %s, loader %r)"
              % (raised, sha(v5) == before, got[:2]))

        # W6: a crash after the manifest and before the file: closed, then healed by the next extend()
        store6 = os.path.join(tmp, "w6")
        os.makedirs(store6)
        s6 = make_store(store6, [OLD_CARD, SIDE])
        v6 = make_vectors(store6, [OLD_CARD])
        mcv.seal(s6, v6)
        mcv._write_manifest(v6, hashlib.sha256(b"the file the crashed run was about to put in place").hexdigest())
        closed = loader(SRC, v6)
        r6 = mcv.extend(s6, v6, embed=fake_embed)
        healed = loader(SRC, v6)
        check(closed[0] is False and r6[0] == 1 and r6[2] == "" and healed[0] is True and healed[1]["manifest"] == "match"
              and named(v6) == sha(v6),
              "W6 a crash between the two replaces: loader %r, then extend %r and loader %r" % (closed, r6, healed[:2]))

        # W7: a reader holds the file while extend() replaces it
        store7 = os.path.join(tmp, "w7")
        os.makedirs(store7)
        s7 = make_store(store7, [OLD_CARD, SIDE])
        v7 = make_vectors(store7, [OLD_CARD])
        mcv.seal(s7, v7)
        old7 = sha(v7)
        held = open(v7, "rb")
        result = {}
        worker = threading.Thread(target=lambda: result.update(r=mcv.extend(s7, v7, embed=fake_embed)))
        worker.start()
        time.sleep(0.4)
        during = loader(SRC, v7) if os.name == "nt" else None
        held.close()
        worker.join(60)
        after = loader(SRC, v7)
        coherent_during = during is None or during[0] is False or during[1]["sha256"] == sha(v7)
        check(result.get("r", (0,))[0] == 1 and named(v7) == sha(v7) != old7 and after[0] is True
              and after[1]["sha256"] == sha(v7) and coherent_during,
              "W7 a held reader: extend %r, loader while held %r, after %r" % (result.get("r"), during, after[:2]))

        # W8: rebuild(out=...) publishes beside the file it writes
        store8 = os.path.join(tmp, "w8")
        os.makedirs(store8)
        s8 = make_store(store8, [OLD_CARD, SIDE])
        v8 = make_vectors(store8, [OLD_CARD, SIDE], sources=["legacy", "body"])
        out = os.path.join(store8, "rebuilt.npz")
        r8 = mcv.rebuild(s8, v8, embed=fake_embed, out=out)
        check(r8 == (1, 2, "") and named(out) == sha(out), "W8 rebuild(out=...) %r, manifest beside it %s"
              % (r8, named(out) == sha(out)))

        if OLD_VECS:
            old = load(OLD_VECS, "mcv_manifest_old")
            n1 = os.path.join(tmp, "n1")
            os.makedirs(n1)
            sn = make_store(n1, [OLD_CARD, SIDE])
            vn = make_vectors(n1, [OLD_CARD])
            rn = old.extend(sn, vn, embed=fake_embed)
            check(rn[0] == 1 and named(vn) is None,
                  "N1 the writer before this change writes the file and no manifest (%r, manifest %r)" % (rn, named(vn)))
        if OLD_SRC:
            n2 = os.path.join(tmp, "n2")
            os.makedirs(n2)
            vn = make_vectors(n2, [OLD_CARD, SIDE])
            with open(vn + ".sha256", "w") as fh:
                fh.write(hashlib.sha256(b"other bytes").hexdigest() + "  claim_embeddings.npz\n")
            got = loader(OLD_SRC, vn)
            check(got[0] is True, "N2 the loader before this change reads a file whose manifest names other bytes (%r)"
                  % (got,))
    finally:
        os.environ.pop("MATH_BRAIN_CLAIM_VECS", None)
        shutil.rmtree(tmp, ignore_errors=True)
    print("%d checks, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
