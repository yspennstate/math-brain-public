import difflib
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
live = Path('~/.claude/dreaming/brain_node_documents.py')
raw = live.read_bytes()
before = raw.decode('utf-8').replace('\r\n','\n')
helper = '''@contextlib.contextmanager
def _attachment_read_lock(mem: Path, timeout_seconds: float = 10.0):
    """Read-lock the stable writer sidecar without creating or writing any file.

    An existing bundle must have its writer-created sidecar. Missing or unsafe
    sidecars fail closed; readers never bootstrap one or read without a lock.
    """
    path = mem / WRITE_LOCK_NAME
    _assert_regular(path, "attachment read lock")
    try:
        fd = os.open(path, os.O_RDONLY | getattr(os, "O_BINARY", 0))
    except OSError as exc:
        raise AttachmentError("cannot open attachment read lock: %s" % exc) from exc
    handle = os.fdopen(fd, "rb", buffering=0)
    locked = False
    try:
        opened = os.fstat(handle.fileno())
        visible = os.lstat(path)
        if (stat.S_ISLNK(visible.st_mode) or not stat.S_ISREG(visible.st_mode)
                or _is_reparse(visible) or opened.st_size < 1
                or (opened.st_dev, opened.st_ino) != (visible.st_dev, visible.st_ino)):
            raise AttachmentError("attachment read lock is not a stable nonempty regular non-link file")
        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            try:
                handle.seek(0)
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(handle.fileno(), msvcrt.LK_NBRLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(handle.fileno(), fcntl.LOCK_SH | fcntl.LOCK_NB)
                locked = True
                break
            except OSError:
                time.sleep(0.01)
        if not locked:
            raise AttachmentError("attachment read lock timed out")
        yield
    finally:
        if locked:
            handle.seek(0)
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


'''
anchor = 'def load_documents('
assert before.count(anchor) == 1
after = before.replace(anchor, helper + anchor, 1)
old = '    with _attachment_write_lock(mem_path):\n        return _load_documents_unlocked(mem_path, safe_slug, missing_ok=missing_ok)'
new = old.replace('_attachment_write_lock', '_attachment_read_lock')
assert after.count(old) == 1
after = after.replace(old, new, 1)
for name in ['copies', 'prototype', 'patches']:
    (root / name).mkdir(exist_ok=True)
(root / 'copies/brain_node_documents.py').write_bytes(raw)
(root / 'prototype/brain_node_documents.py').write_text(after, encoding='utf-8', newline='\n')
patch = ''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/~/.claude/dreaming/brain_node_documents.py',tofile='b/~/.claude/dreaming/brain_node_documents.py'))
(root / 'patches/01_readonly_attachment_lock.diff').write_text(patch,encoding='utf-8',newline='\n')
receipt = {'live_path':str(live),'source_sha256':hashlib.sha256(raw).hexdigest(),'change':'verified attachment readers open the existing stable sidecar read-only and retain writer fencing; writer protocol unchanged','deployment':'not applied'}
(root / 'patches/01_provenance.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
