"""The transport write lock is never held below Normal priority, and the old class comes back on release.

Run: python -X utf8 test_math_transport_lock_priority.py [path to math_transport.py]
The module is loaded from the given path (default: beside this file), so its lock file is that folder's own
math_transport_write.lock; the live store, ledger and queue are not opened.
"""
import ctypes
import importlib.util
import os
import sys

NORMAL, BELOW, IDLE, ABOVE = 0x20, 0x4000, 0x40, 0x8000
k = ctypes.windll.kernel32
k.GetCurrentProcess.restype = ctypes.c_void_p
k.GetPriorityClass.argtypes = [ctypes.c_void_p]
k.GetPriorityClass.restype = ctypes.c_uint
k.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint]
H = k.GetCurrentProcess()


def cls():
    return k.GetPriorityClass(H)


def setc(c):
    assert k.SetPriorityClass(H, c), "could not set class %x" % c


def load(path):
    spec = importlib.util.spec_from_file_location("mt_under_test", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "math_transport.py")
    m = load(path)
    lock_dir = os.path.dirname(os.path.abspath(m.WRITE_LOCK))
    want_fix = hasattr(m, "_lift_priority")
    start = cls()
    checks = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print("%s  %s" % ("ok  " if ok else "FAIL", name))

    try:
        # 1-2: BelowNormal outside, Normal inside, BelowNormal again after
        setc(BELOW)
        with m._write_lock(timeout=5):
            inside = cls()
        check("BelowNormal process holds the lock at Normal", inside == NORMAL)
        check("BelowNormal comes back after release", cls() == BELOW)
        # 3-4: Idle likewise
        setc(IDLE)
        with m._write_lock(timeout=5):
            inside = cls()
        check("Idle process holds the lock at Normal", inside == NORMAL)
        check("Idle comes back after release", cls() == IDLE)
        # 5-6: a Normal process is left alone
        setc(NORMAL)
        with m._write_lock(timeout=5):
            inside = cls()
        check("Normal process stays Normal inside", inside == NORMAL)
        check("Normal process stays Normal after", cls() == NORMAL)
        # 7: a process above Normal is not lowered
        setc(ABOVE)
        with m._write_lock(timeout=5):
            inside = cls()
        check("AboveNormal process is not lowered inside", inside == ABOVE)
        setc(BELOW)
        # 8: an exception inside the block still restores the class and frees the lock
        try:
            with m._write_lock(timeout=5):
                raise RuntimeError("boom")
        except RuntimeError:
            pass
        check("class restored after an exception inside the block", cls() == BELOW)
        with m._write_lock(timeout=5):
            pass
        check("lock is free again after the exception", True)
        # 9: a refused lock (held by another handle) changes nothing
        fd = os.open(m.WRITE_LOCK, os.O_RDWR | os.O_CREAT, 0o644)
        import msvcrt
        os.lseek(fd, 0, 0)
        msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
        refused = False
        try:
            with m._write_lock(timeout=0.3):
                pass
        except TimeoutError:
            refused = True
        finally:
            os.lseek(fd, 0, 0)
            msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
            os.close(fd)
        check("a busy lock still refuses with TimeoutError", refused)
        check("a refused lock leaves the class as it was", cls() == BELOW)
    finally:
        setc(start)
    bad = [n for n, ok in checks if not ok]
    print("%d of %d checks pass (%s, lock folder %s)" % (len(checks) - len(bad), len(checks),
                                                         "patched" if want_fix else "no _lift_priority in this file", lock_dir))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
