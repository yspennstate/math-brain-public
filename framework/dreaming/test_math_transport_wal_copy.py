"""test_math_transport_wal_copy.py - the math transport's restore point and its selftest copy hold the store's committed
state, write-ahead log included (29 Sep 2026).

    python test_math_transport_wal_copy.py [MATH_TRANSPORT.py]

A scratch store in WAL mode, a row committed to its log and not checkpointed, the writer's connection still open.
 C1 a copy of the main file alone lacks the row (the fixture is what it says, and the old copy could fail)
 C2 _sqlite_copy holds the row, as a single rollback-journal file
 C3 _backup_once's restore point holds the row
 C4 the store's main file and log are byte-identical afterwards
"""
import hashlib
import importlib.machinery
import importlib.util
import os
import shutil
import sqlite3
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(HERE, "math_transport.py")
fails, ran = [], []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def sha(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def rows(p):
    db = sqlite3.connect("file:%s?mode=ro" % p.replace("\\", "/"), uri=True)
    try:
        return db.execute("SELECT count(*) FROM notes WHERE body = 'committed to the log'").fetchone()[0]
    finally:
        db.close()


def main():
    sys.path.insert(0, HERE)
    loader = importlib.machinery.SourceFileLoader("mt_walcopy", MT)
    spec = importlib.util.spec_from_file_location("mt_walcopy", MT, loader=loader)
    mt = importlib.util.module_from_spec(spec)
    loader.exec_module(mt)
    tmp = tempfile.mkdtemp(prefix="mt_walcopy_")
    hold = None
    try:
        store = os.path.join(tmp, "brain.sqlite3")
        base = sqlite3.connect(store)
        base.execute("CREATE TABLE notes (body TEXT)")
        base.execute("INSERT INTO notes VALUES ('in the main file')")
        base.commit()
        base.close()
        hold = sqlite3.connect(store, isolation_level=None)
        hold.execute("PRAGMA journal_mode=WAL")
        hold.execute("PRAGMA wal_autocheckpoint=0")
        hold.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        hold.execute("INSERT INTO notes VALUES ('committed to the log')")
        h_main, h_wal = sha(store), sha(store + "-wal")
        raw = os.path.join(tmp, "raw.sqlite3")
        shutil.copyfile(store, raw)
        check(os.path.getsize(store + "-wal") > 0 and rows(raw) == 0,
              "C1 the row is in the log only: a copy of the main file holds it %d times (log %d bytes)"
              % (rows(raw), os.path.getsize(store + "-wal")))
        copy = os.path.join(tmp, "copy.sqlite3")
        mt._sqlite_copy(store, copy)
        mode = open(copy, "rb").read(20)[18]
        check(rows(copy) == 1 and mode == 1 and not os.path.exists(copy + "-wal"),
              "C2 _sqlite_copy holds the row (%d), as a rollback-journal file (header byte %d)" % (rows(copy), mode))
        bak = mt._backup_once(store)
        check(os.path.exists(bak) and rows(bak) == 1, "C3 the restore point %s holds the row (%d)"
              % (os.path.basename(bak), rows(bak) if os.path.exists(bak) else -1))
        check(sha(store) == h_main and sha(store + "-wal") == h_wal,
              "C4 the store's main file and log are byte-identical afterwards")
    finally:
        if hold is not None:
            hold.close()
        shutil.rmtree(tmp, ignore_errors=True)
    print("%s - %d controls, %d failed" % ("FAIL" if fails else "PASS", len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
