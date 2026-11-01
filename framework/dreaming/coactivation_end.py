#!/usr/bin/env python3
"""coactivation_end.py - Stop hook: fold a session's co-reads into the Hebbian weight table.

At session end, read the session's co-activation log (the memories it read together), form the
co-read pairs, and increment their weights in coactivation.tsv - applying a small global decay first
so associations that stop being reinforced fade (use it or lose it). Then delete the session log.

Orphan sweep (fix 2026-07-09): sessions that die WITHOUT a Stop event (usage-limit REM deaths, the
runner's watchdog taskkill) used to strand their logs forever - and dreams are the richest memory
readers, so exactly the best co-read evidence never entered the graph. Now every Stop also folds any
session log older than ORPHAN_H hours through the same path. Decay applies ONCE per fold event (not
per folded log), preserving the use-it-or-lose-it cadence.

A log with fewer than two unique memories contains no association. It is consumed without reading,
decaying, or rewriting coactivation.tsv. If one or more target logs are foldable, every foldable log is
planned first, the existing graph is decayed exactly once, all pair increments are applied, and an
atomic promotion completes before any source log is removed. A failed promotion therefore leaves every
log available for a later retry.

Concurrency: the read-decay-rewrite is guarded by a lockfile; if the lock cannot be had quickly the
fold is skipped - harmless, because the unfolded log just waits and the orphan sweep folds it later.
The TSV write is atomic (tmp + os.replace), so a torn write can no longer shed edges silently.
Audit schema: historical v1 rows remain untouched as ``timestamp kind session-prefix unique-slugs``
(one row per folded log). New v2 rows are one truthful summary per processed invocation:
``timestamp v2 result targets foldable pair-updates``. Result is ``decay``, ``no-pair``,
``already-applied``, or ``failed``; pair-updates counts combinations actually added.

Exactly-once boundary: each promoted fold stores a hashed session-identity receipt inside the same
atomic TSV replacement as its weights. The metadata row has a deliberately nonnumeric third field, so
all existing edge consumers ignore it. If deletion fails or the process dies after promotion, a retry
removes the surviving log without a second increment or decay. Receipts key the filesystem generation
read from the same open handle as the slugs, not mutable contents: an appended retained file cannot
replay its old pairs, while deleting and recreating the same session path creates a new generation.

build_spread_edges.py blends these weights into the association graph, so recall-by-association
follows what the brain actually reasons with together, not only shared vocabulary. Fail-safe silent.
"""
import sys, os, io, json, time, glob, math, hashlib
from itertools import combinations

HOME = os.path.expanduser("~")
DR = os.path.join(HOME, ".claude", "dreaming")
LOGDIR = os.path.join(DR, "coactivation_session")
TSV = os.path.join(DR, "coactivation.tsv")
LOCK = TSV + ".lock"
FOLDLOG = os.path.join(DR, "coactivation_folds.log")
DECAY = 0.98            # each fold event decays existing weights; unreinforced links fade
MAX_PER_SESSION = 40   # cap the pairwise blow-up from a session that read a great many memories
MIN_KEEP = 0.5         # prune weights below this
ORPHAN_H = 6           # session logs older than this get folded by whoever stops next
# focus-weighting (association-mining / inverse-promiscuity): a co-read in a FOCUSED session (a few
# memories, reasoned with together) is strong evidence of a real link; a co-read in a SURVEY session (a
# brain-audit or a dream touching dozens) is weak - yet flat +1.0 lets the survey's C(n,2) pairs flood
# the graph. This is the measured root cause of the young graph's noise (spread_recall's attractor-pull,
# curiosity's co-read "incongruities"): recent brain-building sessions read many brain-meta memories
# together. Scale each pair's increment down for high-read sessions so focused reasoning dominates. A
# forward change - existing weights just decay - so it cleans the graph as it matures, not a snapshot fit.
FOCUS_K = 6            # a session reading <= this many memories still counts each pair at full weight
APPLIED_TAG = "#applied"
APPLIED_VALUE = "receipt"


def _read_slugs(logf):
    slugs, seen = [], set()
    try:
        with io.open(logf, encoding="utf-8", errors="replace") as f:
            stat = os.fstat(f.fileno())
            identity = (int(stat.st_dev), int(stat.st_ino))
            if not identity[1]:
                raise OSError("filesystem does not expose a stable file identity")
            for ln in f:
                s = ln.strip()
                if s and s not in seen:
                    seen.add(s)
                    slugs.append(s)
    except Exception:
        return None
    return sorted(set(slugs[:MAX_PER_SESSION])), identity


def _append_audit(result, targets, foldable, pairs, path=FOLDLOG, stamp=None):
    """Append one v2 invocation summary; legacy four-column rows remain valid history."""
    try:
        stamp = stamp or time.strftime("%Y-%m-%dT%H:%M:%S")
        with io.open(path, "a", encoding="utf-8") as f:
            f.write("%s\tv2\t%s\t%d\t%d\t%d\n" %
                    (stamp, result, int(targets), int(foldable), int(pairs)))
    except Exception:
        pass


def _receipt(logf, identity):
    """Opaque receipt for one path generation; never exposes its session id or file identity."""
    payload = "%s\0%d\0%d" % (os.path.basename(logf).casefold(), identity[0], identity[1])
    return hashlib.sha256(payload.encode("utf-8", errors="replace")).hexdigest()


def _load_decayed_weights(path):
    """Validate the complete prior graph, then return one-decay weights and applied receipts."""
    weights, applied = {}, set()
    if not os.path.exists(path):
        return weights, applied
    saw_header = False
    with io.open(path, encoding="utf-8", errors="strict") as f:
        for line_no, ln in enumerate(f, 1):
            p = ln.rstrip("\r\n").split("\t")
            if line_no == 1:
                if p != ["a", "b", "weight"]:
                    raise ValueError("coactivation header is missing or malformed")
                saw_header = True
                continue
            if p and p[0] == APPLIED_TAG:
                digest = p[1] if len(p) >= 2 else ""
                if (len(p) != 3 or p[2] != APPLIED_VALUE or len(digest) != 64 or
                        any(ch not in "0123456789abcdef" for ch in digest) or
                        digest in applied):
                    raise ValueError("malformed or duplicate applied receipt")
                applied.add(digest)
                continue
            if len(p) != 3 or not p[0] or not p[1]:
                raise ValueError("malformed coactivation edge row")
            try:
                value = float(p[2])
            except Exception as exc:
                raise ValueError("nonnumeric coactivation weight") from exc
            if not math.isfinite(value) or value < 0:
                raise ValueError("nonfinite or negative coactivation weight")
            pair = (p[0], p[1])
            if pair in weights:
                raise ValueError("duplicate coactivation edge")
            weights[pair] = value * DECAY
    if not saw_header:
        raise ValueError("coactivation table is empty")
    return weights, applied


def _atomic_write_weights(path, weights, applied):
    """Durably stage and atomically promote weights and their exactly-once receipts."""
    tmp = "%s.tmp.%d" % (path, os.getpid())
    try:
        with io.open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write("a\tb\tweight\n")
            for digest in sorted(applied):
                f.write("%s\t%s\t%s\n" % (APPLIED_TAG, digest, APPLIED_VALUE))
            for (a, b), val in sorted(weights.items(), key=lambda kv: (-kv[1], kv[0])):
                if val >= MIN_KEEP:
                    f.write("%s\t%s\t%.3f\n" % (a, b, val))
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except Exception:
        try:
            if os.path.exists(tmp):
                os.remove(tmp)
        except Exception:
            pass
        raise


def _remove_logs(plans):
    """Remove only the exact file generations that were read; never delete a replacement."""
    removed = 0
    for path, _slugs, identity, _receipt_id in sorted(plans, key=lambda row: row[0]):
        try:
            current = os.stat(path)
            if (int(current.st_dev), int(current.st_ino)) != identity:
                continue
            os.remove(path)
            removed += 1
        except Exception:
            pass
    return removed


def fold_targets(targets, tsv=TSV, foldlog=FOLDLOG, stamp=None):
    """Process already-selected session logs under the caller's coactivation lock.

    This function is intentionally path-parameterized so the regression evaluator can prove the
    transaction contract entirely inside a temporary directory without invoking the live hook.
    """
    targets = sorted(set(targets))
    plans = []
    unreadable = []
    for logf in targets:
        read = _read_slugs(logf)
        if read is None:
            unreadable.append(logf)
        else:
            slugs, identity = read
            plans.append((logf, slugs, identity, _receipt(logf, identity)))

    foldable = [(path, slugs, identity, receipt)
                for path, slugs, identity, receipt in plans if len(slugs) >= 2]
    planned_pairs = sum(len(slugs) * (len(slugs) - 1) // 2
                        for _path, slugs, _identity, _receipt_id in foldable)
    if unreadable:
        _append_audit("failed", len(targets), len(foldable), planned_pairs,
                      path=foldlog, stamp=stamp)
        return {"result": "failed", "targets": len(targets),
                "foldable": len(foldable), "pairs": planned_pairs, "removed": 0}
    if not foldable:
        removed = _remove_logs(plans)
        _append_audit("no-pair", len(targets), 0, 0, path=foldlog, stamp=stamp)
        return {"result": "no-pair", "targets": len(targets), "foldable": 0,
                "pairs": 0, "removed": removed}

    try:
        weights, applied = _load_decayed_weights(tsv)
    except Exception:
        _append_audit("failed", len(targets), len(foldable), planned_pairs,
                      path=foldlog, stamp=stamp)
        return {"result": "failed", "targets": len(targets),
                "foldable": len(foldable), "pairs": planned_pairs, "removed": 0}

    new_foldable = [(path, slugs, identity, receipt)
                    for path, slugs, identity, receipt in foldable
                    if receipt not in applied]
    if not new_foldable:
        removed = _remove_logs(plans)
        _append_audit("already-applied", len(targets), len(foldable), 0,
                      path=foldlog, stamp=stamp)
        return {"result": "already-applied", "targets": len(targets),
                "foldable": len(foldable), "pairs": 0, "removed": removed}

    pair_updates = sum(len(slugs) * (len(slugs) - 1) // 2
                       for _path, slugs, _identity, _receipt_id in new_foldable)
    try:
        for _path, slugs, _identity, receipt in new_foldable:
            focus = min(1.0, FOCUS_K / float(len(slugs)))
            for a, b in combinations(slugs, 2):
                weights[(a, b)] = weights.get((a, b), 0.0) + focus
            applied.add(receipt)
        _atomic_write_weights(tsv, weights, applied)
    except Exception:
        _append_audit("failed", len(targets), len(new_foldable), pair_updates,
                      path=foldlog, stamp=stamp)
        return {"result": "failed", "targets": len(targets),
                "foldable": len(new_foldable), "pairs": pair_updates, "removed": 0}

    removed = _remove_logs(plans)
    _append_audit("decay", len(targets), len(new_foldable), pair_updates,
                  path=foldlog, stamp=stamp)
    return {"result": "decay", "targets": len(targets), "foldable": len(new_foldable),
            "pairs": pair_updates, "removed": removed}


def _acquire_lock():
    """A few quick tries, stale-takeover past 90s; give up gracefully (the log waits for the sweep)."""
    for _ in range(8):
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(time.time()).encode())
            os.close(fd)
            return True
        except FileExistsError:
            try:
                if time.time() - os.path.getmtime(LOCK) > 90:
                    os.remove(LOCK)
                    continue
            except Exception:
                pass
            time.sleep(0.1)
        except Exception:
            return False
    return False


def _release_lock():
    try:
        os.remove(LOCK)
    except Exception:
        pass


def main():
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        # Discovery is not execution: this script writes, so a help request must
        # exit before any work. See script_help_flag_can_execute_work.
        print(__doc__ or os.path.basename(__file__))
        return
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except Exception:
        data = {}
    try:
        sess = data.get("session_id") or ""
        own = os.path.join(LOGDIR, sess + ".log") if sess else None
        now = time.time()
        targets = []
        if own and os.path.exists(own):
            targets.append(own)
        try:
            for f in glob.glob(os.path.join(LOGDIR, "*.log")):
                if f != own and now - os.path.getmtime(f) > ORPHAN_H * 3600:
                    targets.append(f)
        except Exception:
            pass
        if not targets:
            return
        if not _acquire_lock():
            return  # someone else is folding; our log waits and the orphan sweep will get it
        try:
            fold_targets(targets)
        finally:
            _release_lock()
    except Exception:
        return


if __name__ == "__main__":
    try:
        import os as _o, sys as _s
        _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
        import brain_switch as _bsw
        _bsw.gate()
    except SystemExit:
        raise
    except Exception:
        pass
    main()
