"""The semantic channel reads its claim vectors again when the artifact file changes (scheduled audit fleet03/B11 r70,
B11-R31-SEMTOP-CONTROL-MISSES-SEMANTIC-GENERATION-20260928).

A module that stays imported across prompts must score against the file a fresh process would read: after a valid
rebuild, the same top claim as a fresh import; while the file is malformed, nothing (the channel fails closed, as a
fresh import would); and after a good file is back, the good file's answer.

    python -m pytest tests/test_semantic_generation.py
    python tests/test_semantic_generation.py [--old OLD_SEMANTIC.py]

With --old, the module before this change must keep the first file's answer after the rebuild (the check can fail).

A rewrite that keeps the inode, the size and the mtime - through a hard link, with the old
mtime put back - is read again too (fleet03/B01 r74,
B01-R74-SEMANTIC-GENERATION-MTIME-ROLLBACK-HARDLINK-20260929). With --old-link, the module
before that change must keep the first file's answer there.

So is one that also keeps every zip member's name, CRC-32 and size: four bytes elsewhere in the
vectors solve for the old CRC (fleet03/B11 r90 and fleet04/B17 r74,
B11-R77-SEMANTIC-GENERATION-CRC32-COLLISION-20260929-R90,
B17-R74-CRC32-COLLISION-PRESERVES-SEMANTIC-CACHE-GENERATION-20260929). The generation is now the
SHA-256 of the bytes read. With --old-crc, the module before that change must keep the first
file's answer there while a fresh import reads the second. A manifest beside the file
(claim_embeddings.npz.sha256) that does not name the bytes makes both refuse them.
"""
from __future__ import annotations

import hashlib
import importlib.machinery
import importlib.util
import io
import os
import struct
import sys
import tempfile
import zipfile
import zlib

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

Q = np.array([1.0, 0.0, 0.0], dtype=np.float32)          # the fixed query direction
IDS = np.array(["claim_A", "claim_B", "claim_C"])
G0 = np.array([[1.0, 0.1, 0.0], [0.2, 1.0, 0.0], [0.0, 0.3, 1.0]], dtype=np.float32)     # A points along Q
G1 = np.array([[0.0, 0.1, 1.0], [0.2, 1.0, 0.0], [1.0, 0.0, 0.05]], dtype=np.float32)    # now C does
MODEL = "bge-small-en-v1.5"


def load_module(path=None, name="semantic_under_test"):
    path = path or os.path.join(SRC, "math_brain", "semantic.py")
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


def write(path, vecs, ids=IDS, stamp=None):
    tmp = path + ".tmp.npz"
    np.savez(tmp, vecs=vecs, slugs=ids, model=np.array(MODEL))
    os.replace(tmp, path)
    if stamp is not None:
        os.utime(path, ns=(stamp, stamp))


def top(m):
    m._load_artifact()
    return str(m._ids[int(np.argmax(m._vecs @ Q))])


def fresh_top(path, art):
    m = load_module(path, "semantic_fresh_%d" % os.getpid())
    m.ARTIFACT = art
    try:
        return top(m)
    except Exception:
        return None


def reused_top(m):
    try:
        return top(m)
    except Exception:
        return None


def run(module_path=None):
    """(first, after_rebuild, fresh_after_rebuild, during_bad, fresh_during_bad, after_repair, fresh_after_repair)"""
    td = tempfile.mkdtemp(prefix="semgen_")
    art = os.path.join(td, "claim_embeddings.npz")
    base = 1_800_000_000_000_000_000
    write(art, G0, stamp=base)
    m = load_module(module_path)
    m.ARTIFACT = art
    first = reused_top(m)
    write(art, G1, stamp=base + 10**9)
    after, fresh_after = reused_top(m), fresh_top(module_path, art)
    write(art, G0, ids=IDS[:2], stamp=base + 2 * 10**9)       # malformed: three vectors, two ids
    bad, fresh_bad = reused_top(m), fresh_top(module_path, art)
    write(art, G1, stamp=base + 3 * 10**9)
    repaired, fresh_repaired = reused_top(m), fresh_top(module_path, art)
    return first, after, fresh_after, bad, fresh_bad, repaired, fresh_repaired


def hardlink_rewrite(module_path=None):
    """(first, reused_after, fresh_after, old_key_unchanged) for a same-size rewrite through a
    hard link with the old mtime restored: the inode, the size and the mtime stay as they were."""
    td = tempfile.mkdtemp(prefix="semgen_link_")
    art = os.path.join(td, "claim_embeddings.npz")
    write(art, G0, stamp=1_800_000_000_000_000_000)
    m = load_module(module_path)
    m.ARTIFACT = art
    first = reused_top(m)
    before = os.stat(art)
    other = os.path.join(td, "other.npz")
    np.savez(other, vecs=G1, slugs=IDS, model=np.array(MODEL))
    with open(other, "rb") as fh:
        rewrite = fh.read()
    assert len(rewrite) == before.st_size          # same shapes and dtypes: same size
    alias = os.path.join(td, "alias.npz")
    os.link(art, alias)
    with open(alias, "r+b") as fh:
        fh.write(rewrite)
    os.utime(art, ns=(before.st_atime_ns, before.st_mtime_ns))
    after = os.stat(art)
    same = ((before.st_ino, before.st_mtime_ns, before.st_size)
            == (after.st_ino, after.st_mtime_ns, after.st_size))
    return first, reused_top(m), fresh_top(module_path, art), same


# Four dimensions: claim_Z is (0, 0, 1, x), orthogonal to the query whatever x is, so the coordinate x can take the four
# bytes that put the old CRC-32 back without changing which claim is first.
IDS4 = np.array(["claim_A", "claim_B", "claim_C", "claim_Z"])
G0_4 = np.array([[1.0, 0.1, 0.0, 0.0], [0.2, 1.0, 0.0, 0.0], [0.0, 0.3, 1.0, 0.0], [0.0, 0.0, 1.0, 0.5]],
                dtype=np.float32)
G1_4 = np.array([[0.0, 0.1, 1.0, 0.0], [0.2, 1.0, 0.0, 0.0], [1.0, 0.0, 0.05, 0.0], [0.0, 0.0, 1.0, 0.5]],
                dtype=np.float32)
Q4 = np.array([1.0, 0.0, 0.0, 0.0], dtype=np.float32)
_POLY = 0x104C11DB7


def _rev32(x):
    y = 0
    for _ in range(32):
        y = (y << 1) | (x & 1)
        x >>= 1
    return y


def _mul(x, y):
    z = 0
    while y:
        z ^= x * (y & 1)
        y >>= 1
        x <<= 1
        if (x >> 32) & 1:
            x ^= _POLY
    return z


def _pow(x, y):
    z = 1
    while y:
        if y & 1:
            z = _mul(z, x)
        x = _mul(x, x)
        y >>= 1
    return z


def _divmod(x, y):
    if x == 0:
        return 0, 0
    ydeg = y.bit_length() - 1
    z = 0
    for i in range(x.bit_length() - 1 - ydeg, -1, -1):
        if (x >> (i + ydeg)) & 1:
            x ^= y << i
            z |= 1 << i
    return z, x


def _reciprocal(x):
    y, x = x, _POLY
    a, b = 0, 1
    while y:
        q, r = _divmod(x, y)
        x, y, a, b = y, r, b, a ^ _mul(q, b)
    assert x == 1
    return a


def force_crc(data, offset, target):
    """data with the four bytes at offset rewritten so that zlib.crc32 of the result is target. CRC-32 is linear over
    GF(2), so the four bytes that cancel the difference can be solved for."""
    buf = bytearray(data)
    delta = _rev32(zlib.crc32(bytes(buf)) & 0xFFFFFFFF) ^ _rev32(target)
    delta = _mul(_reciprocal(_pow(2, (len(buf) - offset) * 8)), delta)
    word = _rev32(delta)
    for i in range(4):
        buf[offset + i] ^= (word >> (8 * i)) & 0xFF
    assert zlib.crc32(bytes(buf)) & 0xFFFFFFFF == target
    return bytes(buf)


def _npz_bytes(vecs, ids=IDS4):
    out = io.BytesIO()
    np.savez(out, vecs=vecs, slugs=ids, model=np.array(MODEL))
    return out.getvalue()


def colliding_pair():
    """(G0 file bytes, G1 file bytes): valid npz files whose vectors differ and put a different claim first, with the
    same length and every zip member's (name, CRC-32, size) equal. Only the vecs.npy payload differs."""
    g0 = _npz_bytes(G0_4)
    info = zipfile.ZipFile(io.BytesIO(g0)).getinfo("vecs.npy")
    name_len, extra_len = struct.unpack("<HH", g0[info.header_offset + 26:info.header_offset + 30])
    start = info.header_offset + 30 + name_len + extra_len
    payload0 = g0[start:start + info.compress_size]
    for tweak in range(64):
        vecs = G1_4.copy()
        vecs[3, 2] = np.float32(1.0 + tweak / 64.0)
        raw = io.BytesIO()
        np.save(raw, vecs)
        payload1 = raw.getvalue()
        assert len(payload1) == len(payload0)
        cell = len(payload1) - vecs.nbytes + (3 * vecs.shape[1] + 3) * 4    # claim_Z's fourth coordinate
        payload1 = force_crc(payload1, cell, info.CRC)
        if np.isfinite(np.load(io.BytesIO(payload1))).all():
            break
    else:
        raise AssertionError("no finite forcing found")
    return g0, g0[:start] + payload1 + g0[start + len(payload1):]


def _old_key(path):
    st = os.stat(path)
    with zipfile.ZipFile(path) as z:
        members = tuple((i.filename, i.CRC, i.file_size) for i in z.infolist())
    return st.st_ino, st.st_mtime_ns, st.st_size, members


def top4(m):
    m._load_artifact()
    return str(m._ids[int(np.argmax(m._vecs @ Q4))])


def _try(f, *a):
    try:
        return f(*a)
    except Exception:
        return None


def fresh_top4(path, art):
    m = load_module(path, "semantic_fresh4_%d" % os.getpid())
    m.ARTIFACT = art
    return _try(top4, m)


def crc_collision_rewrite(module_path=None, manifest=False):
    """(first, reused_after, fresh_after, old_key_unchanged, bytes_differ) for an in-place rewrite through a hard link
    that keeps the inode, the size, the mtime and every member's name, CRC-32 and size. With manifest, the first file's
    SHA-256 is published beside it and left as it was."""
    td = tempfile.mkdtemp(prefix="semgen_crc_")
    art = os.path.join(td, "claim_embeddings.npz")
    g0, g1 = colliding_pair()
    with open(art, "wb") as fh:
        fh.write(g0)
    if manifest:
        with open(art + ".sha256", "w") as fh:
            fh.write("%s  claim_embeddings.npz" % hashlib.sha256(g0).hexdigest() + chr(10))
    os.utime(art, ns=(1_800_000_000_000_000_000, 1_800_000_000_000_000_000))
    m = load_module(module_path)
    m.ARTIFACT = art
    first = _try(top4, m)
    before = _old_key(art)
    alias = os.path.join(td, "alias.npz")
    os.link(art, alias)
    with open(alias, "r+b") as fh:
        fh.write(g1)
    os.utime(art, ns=(before[1], before[1]))
    after = _old_key(art)
    with open(art, "rb") as fh:
        differ = fh.read() != g0
    return first, _try(top4, m), fresh_top4(module_path, art), before == after, differ


def test_a_rewrite_that_keeps_every_member_crc_is_read_again():
    first, after, fresh_after, same_key, differ = crc_collision_rewrite()
    assert same_key and differ            # the old key could not tell these files apart; their bytes differ
    assert first == "claim_A"
    assert after == fresh_after == "claim_C"


def test_the_generation_is_the_digest_of_the_bytes():
    g0, g1 = colliding_pair()
    td = tempfile.mkdtemp(prefix="semgen_digest_")
    art = os.path.join(td, "claim_embeddings.npz")
    m = load_module()
    m.ARTIFACT = art
    with open(art, "wb") as fh:
        fh.write(g0)
    gen0 = m._generation()
    top4(m)
    assert m.artifact_identity() == {"sha256": hashlib.sha256(g0).hexdigest(), "manifest": "absent"}
    with open(art, "r+b") as fh:
        fh.write(g1)
    assert m._generation() != gen0 and m._generation()[0] == hashlib.sha256(g1).hexdigest()


def test_bytes_the_manifest_does_not_name_are_refused_by_reused_and_fresh_alike():
    first, after, fresh_after, same_key, differ = crc_collision_rewrite(manifest=True)
    assert same_key and differ
    assert first == "claim_A"
    assert after is None and fresh_after is None


def test_a_manifest_that_names_the_bytes_is_read_and_a_damaged_one_is_refused():
    td = tempfile.mkdtemp(prefix="semgen_manifest_")
    art = os.path.join(td, "claim_embeddings.npz")
    g0 = _npz_bytes(G0_4)
    with open(art, "wb") as fh:
        fh.write(g0)
    m = load_module()
    m.ARTIFACT = art
    good = hashlib.sha256(g0).hexdigest()
    for text, ok in ((good + "  claim_embeddings.npz" + chr(10), True),
                     (good.upper() + chr(10), True),
                     (hashlib.sha256(b"other").hexdigest() + "  claim_embeddings.npz" + chr(10), False),
                     ("not a digest" + chr(10), False),
                     ("", False)):
        with open(art + ".sha256", "w") as fh:
            fh.write(text)
        got = _try(top4, m)
        assert (got == "claim_A") is ok, (text, got, m._status)
        if ok:
            assert m.artifact_identity()["manifest"] == "match"
        else:
            assert m._status[0] == "INVALID_ARTIFACT" and m._vecs is None   # lane_status() says DISABLED unless switched on
    os.remove(art + ".sha256")
    assert top4(m) == "claim_A" and m.artifact_identity()["manifest"] == "absent"


def test_the_digest_and_the_vectors_come_from_one_read():
    # fleet04/B17 r74, acceptance 4: the file changes between the read and the parse. The loader parses the bytes it
    # read, under their own digest, and the next call reads the new file.
    td = tempfile.mkdtemp(prefix="semgen_snapshot_")
    art = os.path.join(td, "claim_embeddings.npz")
    g0, g1 = _npz_bytes(G0_4), _npz_bytes(G1_4)
    with open(art, "wb") as fh:
        fh.write(g0)
    m = load_module()
    m.ARTIFACT = art
    real = m.np.load
    fired = []

    def replace_before_the_parse(*args, **kwargs):
        if not fired:
            fired.append(1)
            with open(art + ".new", "wb") as fh:
                fh.write(g1)
            os.replace(art + ".new", art)
        return real(*args, **kwargs)

    m.np.load = replace_before_the_parse
    try:
        assert top4(m) == "claim_A"
    finally:
        m.np.load = real
    assert fired and m.artifact_identity()["sha256"] == hashlib.sha256(g0).hexdigest()
    assert top4(m) == "claim_C" and m.artifact_identity()["sha256"] == hashlib.sha256(g1).hexdigest()


def test_an_unchanged_file_is_parsed_once():
    td = tempfile.mkdtemp(prefix="semgen_once_")
    art = os.path.join(td, "claim_embeddings.npz")
    with open(art, "wb") as fh:
        fh.write(_npz_bytes(G0_4))
    m = load_module()
    m.ARTIFACT = art
    real, parses = m.np.load, []

    def counting(*args, **kwargs):
        parses.append(1)
        return real(*args, **kwargs)

    m.np.load = counting
    try:
        for _ in range(5):
            assert top4(m) == "claim_A"
    finally:
        m.np.load = real
    assert len(parses) == 1


def test_a_rewrite_that_keeps_inode_size_and_mtime_is_read_again():
    first, after, fresh_after, same = hardlink_rewrite()
    assert same                                     # the old key could not tell the files apart
    assert first == "claim_A"
    assert after == fresh_after == "claim_C"


def test_reused_module_follows_the_artifact():
    first, after, fresh_after, bad, fresh_bad, repaired, fresh_repaired = run()
    assert first == "claim_A"
    assert after == fresh_after == "claim_C"
    assert bad is None and fresh_bad is None
    assert repaired == fresh_repaired == "claim_C"


def test_same_file_is_not_read_twice():
    td = tempfile.mkdtemp(prefix="semgen_")
    art = os.path.join(td, "claim_embeddings.npz")
    write(art, G0, stamp=1_800_000_000_000_000_000)
    m = load_module()
    m.ARTIFACT = art
    top(m)
    held = m._vecs
    top(m)
    assert m._vecs is held


if __name__ == "__main__":
    old = sys.argv[sys.argv.index("--old") + 1] if "--old" in sys.argv else None
    fails = []
    r = run()
    ok = r[0] == "claim_A" and r[1] == r[2] == "claim_C" and r[3] is None and r[4] is None and r[5] == r[6] == "claim_C"
    print(("PASS" if ok else "FAIL") + "  new: first %s; after a valid rebuild %s (fresh %s); malformed %s (fresh %s); "
          "repaired %s (fresh %s)" % r)
    fails += [] if ok else ["new"]
    try:
        test_same_file_is_not_read_twice()
        print("PASS  an unchanged file is not read again")
    except AssertionError:
        print("FAIL  an unchanged file was read again")
        fails.append("reread")
    r = hardlink_rewrite()
    ok = r[3] and r[0] == "claim_A" and r[1] == r[2] == "claim_C"
    print(("PASS" if ok else "FAIL") + "  a rewrite through a hard link with the mtime put back "
          f"is read again: first {r[0]}, reused {r[1]}, fresh {r[2]}, "
          f"(inode, mtime, size) unchanged {r[3]}")
    fails += [] if ok else ["link"]
    old_link = sys.argv[sys.argv.index("--old-link") + 1] if "--old-link" in sys.argv else None
    if old_link:
        r = hardlink_rewrite(os.path.abspath(old_link))
        ok = r[3] and r[1] == "claim_A" and r[2] == "claim_C"
        print(("PASS" if ok else "FAIL") + "  N2 the module before the member check keeps the "
              f"first file's answer after the rewrite: reused {r[1]}, fresh {r[2]} "
              "(the defect B01 found)")
        fails += [] if ok else ["N2"]
    r = crc_collision_rewrite()
    ok = r[3] and r[4] and r[0] == "claim_A" and r[1] == r[2] == "claim_C"
    print(("PASS" if ok else "FAIL") + "  a rewrite that keeps every member's CRC-32 is read again: "
          f"first {r[0]}, reused {r[1]}, fresh {r[2]}, old key unchanged {r[3]}, bytes differ {r[4]}")
    fails += [] if ok else ["crc"]
    r = crc_collision_rewrite(manifest=True)
    ok = r[3] and r[4] and r[0] == "claim_A" and r[1] is None and r[2] is None
    print(("PASS" if ok else "FAIL") + "  with a manifest, reused and fresh both refuse the rewritten bytes: "
          f"reused {r[1]}, fresh {r[2]}")
    fails += [] if ok else ["crc-manifest"]
    old_crc = sys.argv[sys.argv.index("--old-crc") + 1] if "--old-crc" in sys.argv else None
    if old_crc:
        r = crc_collision_rewrite(os.path.abspath(old_crc))
        ok = r[3] and r[4] and r[1] == "claim_A" and r[2] == "claim_C"
        print(("PASS" if ok else "FAIL") + "  N3 the module before the digest keeps the first file's answer "
              f"after the CRC-preserving rewrite: reused {r[1]}, fresh {r[2]} (the defect B11 r90 and B17 r74 found)")
        fails += [] if ok else ["N3"]
    if old:
        r = run(os.path.abspath(old))
        ok = r[1] == "claim_A" and r[2] == "claim_C"
        print(("PASS" if ok else "FAIL") + "  N1 the module before this change keeps the first file's answer after the "
              "rebuild: reused %s, fresh %s (the defect B11 found)" % (r[1], r[2]))
        fails += [] if ok else ["N1"]
    print("FAIL" if fails else "PASS")
    sys.exit(1 if fails else 0)
