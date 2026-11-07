"""Controls for the light loader's metadata cache (embedding_artifact._meta_cache_read / _meta_cache_write).

On a synthetic memory folder and schema-v3 sidecar:

 M1 the first call takes the full path and writes the cache; the second is a hit (the sidecar is not read whole)
    and returns the same rows, matrix, bias and text hashes as the full path with the cache off
 M2 a sidecar touched in place (same bytes, new stat) is not a hit: the full path runs again, same answer
 M3 a new sidecar under a new pointer sha is not a hit: the answer is the new sidecar's, as with the cache off
 M4 EMB_META_CACHE=0 never reads or writes the cache
 M5 a control: a cache record with its slugs reordered changes the answer (the comparison can see a cached read)

    python test_embedding_meta_cache.py      (a few seconds; ALL PASS at the end; needs numpy; temp folder only)
"""
import hashlib
import io
import json
import marshal
import os
import random
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
results = []
N_CHECKS = 6


def check(ok, what):
    results.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + what)


def body(rng, i):
    words = " ".join(rng.choice(["kernel", "spectral", "walk", "bound", "graph", "measure", "limit", "proof"])
                     for _ in range(rng.randint(12, 40)))
    return "---\nname: m%03d\ndescription: \"note %d\"\n---\n\n%s\n" % (i, i, words)


def write_sidecar(np, ea, builder, root, mem, rng, tag, built_at):
    slugs, hashes, sizes, mtimes = [], [], [], []
    for name in sorted(os.listdir(mem)):
        p = os.path.join(mem, name)
        with open(p, encoding="utf-8") as f:
            text = f.read()
        st = os.stat(p)
        slugs.append(name[:-3])
        hashes.append(builder.text_sha256(builder._text_for(text)))
        sizes.append(st.st_size)
        mtimes.append(st.st_mtime_ns)
    n = len(slugs)
    vecs = np.asarray([[rng.uniform(-1, 1) for _ in range(6)] for _ in range(n)], dtype=np.float32)
    buf = io.BytesIO()
    np.savez(buf, slugs=np.asarray(slugs), vecs=vecs, model=np.asarray("test-model"),
             built_at=np.asarray(built_at), schema_version=np.asarray(ea.RUNTIME_SCHEMA_VERSION),
             text_sha256=np.asarray(hashes), source_size=np.asarray(sizes, dtype=np.int64),
             source_mtime_ns=np.asarray(mtimes, dtype=np.int64), row_safe=np.ones(n, dtype=np.bool_))
    blob = buf.getvalue()
    side = os.path.join(root, "memory_embeddings_%s.npz" % tag)
    with open(side, "wb") as f:
        f.write(blob)
    auth = os.path.join(root, "embeddings_current.json")
    with open(auth, "w", encoding="utf-8") as f:
        json.dump({"schema": ea.AUTHORITY_SCHEMA, "committed_at": "2026-11-05T00:00:01Z", "sidecar": side,
                   "sidecar_sha256": hashlib.sha256(blob).hexdigest(), "sidecar_size": len(blob),
                   "model": "test-model", "built_at": built_at}, f)
    return side, auth


def view(x):
    if x is None:
        return None
    return (sorted(x.index.items()), bytes(x.matrix._raw), x.bias, sorted(x.text_hashes.items()))


def main():
    import numpy as np
    import embedding_artifact as ea
    import build_memory_embeddings as builder
    rng = random.Random(20261107)
    tmp = tempfile.mkdtemp(prefix="emb_meta_cache_")
    saved = {k: os.environ.get(k) for k in ("BRAIN_EMB_VERIFY_DIR", "EMB_META_CACHE", "EMB_SHA_STAT_CACHE")}
    saved_paths = (ea._SHA_STAT_CACHE, getattr(ea, "_META_CACHE", None))
    real_rkb = ea.read_known_bytes
    whole_reads = []

    def counting_rkb(path, expected_sha):
        whole_reads.append(path)
        return real_rkb(path, expected_sha)

    def load(side, auth, mem, cache_on):
        os.environ["EMB_META_CACHE"] = "1" if cache_on else "0"
        os.environ["BRAIN_EMB_VERIFY_DIR"] = os.path.join(tmp, "vc_%s" % ("on" if cache_on else "off"))
        return view(ea.load_verified_embeddings_lightweight(side, auth, mem))

    try:
        os.environ.pop("EMB_SHA_STAT_CACHE", None)
        ea._SHA_STAT_CACHE = os.path.join(tmp, ".embedding_sha_stat.json")
        ea._META_CACHE = os.path.join(tmp, ".embedding_meta_cache.marshal")
        ea.read_known_bytes = counting_rkb
        mem = os.path.join(tmp, "mem")
        os.makedirs(mem)
        for i in range(rng.randint(12, 30)):
            with open(os.path.join(mem, "m%03d.md" % i), "w", encoding="utf-8", newline="") as f:
                f.write(body(rng, i))
        side, auth = write_sidecar(np, ea, builder, tmp, mem, rng, "a", "2026-11-05T00:00:00Z")

        off = load(side, auth, mem, False)
        del whole_reads[:]
        cold = load(side, auth, mem, True)
        cold_reads = len(whole_reads)
        written = os.path.exists(ea._META_CACHE)
        del whole_reads[:]
        hit = load(side, auth, mem, True)
        check(off is not None and len(off[0]) > 0 and cold == off and written and cold_reads == 1,
              "M1 cold call takes the full path (%d whole read) and writes the cache; same answer as cache off"
              % cold_reads)
        check(hit == off and not whole_reads, "M1 second call is a hit (no whole read) with the same answer")

        st = os.stat(side)
        os.utime(side, ns=(st.st_atime_ns, st.st_mtime_ns + 3_000_000_000))
        del whole_reads[:]
        touched = load(side, auth, mem, True)
        check(touched == off and len(whole_reads) == 1, "M2 a touched sidecar is not a hit: full path, same answer")

        side_b, auth = write_sidecar(np, ea, builder, tmp, mem, rng, "b", "2026-11-06T00:00:00Z")
        off_b = load(side_b, auth, mem, False)
        del whole_reads[:]
        new_b = load(side_b, auth, mem, True)
        check(off_b is not None and new_b == off_b and off_b != off and len(whole_reads) == 1,
              "M3 a new sidecar under a new sha is not a hit: its own answer")

        os.remove(ea._META_CACHE)
        del whole_reads[:]
        load(side_b, auth, mem, False)
        load(side_b, auth, mem, False)
        check(len(whole_reads) == 2 and not os.path.exists(ea._META_CACHE),
              "M4 EMB_META_CACHE=0 reads the whole sidecar each call and writes no cache")

        load(side_b, auth, mem, True)
        with open(ea._META_CACHE, "rb") as f:
            rec = marshal.load(f)
        rec["slugs"] = list(reversed(rec["slugs"]))
        with open(ea._META_CACHE, "wb") as f:
            marshal.dump(rec, f)
        del whole_reads[:]
        bad = load(side_b, auth, mem, True)
        check(not whole_reads and bad != off_b, "M5 control: a reordered cache record is read and changes the answer")
    except Exception as e:
        check(False, "raised %s: %s" % (type(e).__name__, e))
    finally:
        ea.read_known_bytes = real_rkb
        ea._SHA_STAT_CACHE, ea._META_CACHE = saved_paths
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(tmp, ignore_errors=True)
    ok = all(results) and len(results) == N_CHECKS
    print("ALL PASS" if ok else "FAILED %d of %d" % (N_CHECKS - results.count(True), N_CHECKS))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
