"""Read a file without blocking its writer's replace (Windows).

A plain open() holds the file without FILE_SHARE_DELETE, and task_checklist_hook.save_state's rename of the 13 MB
state.json then fails until the reader closes: 20-28 s lock holds and ~100 'checklist lock held too long' an hour on
2 Nov 2026. open_shared() opens with share read/write/delete, so the writer's POSIX-semantics rename succeeds and this
reader keeps the old, whole bytes. Off Windows, or on any failure, it is a plain open.
Memory: checklist_lock_held_by_os_replace_waiting_on_readers_2026_11_02.
"""
import io
import json
import os


def open_shared(path, binary=False):
    if os.name == "nt":
        try:
            import ctypes
            import msvcrt
            from ctypes import wintypes
            k32 = ctypes.WinDLL("kernel32", use_last_error=True)
            k32.CreateFileW.restype = wintypes.HANDLE
            k32.CreateFileW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID,
                                        wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE]
            h = k32.CreateFileW(os.path.abspath(path), 0x80000000, 7, None, 3, 0x80, None)
            if h not in (None, ctypes.c_void_p(-1).value):
                raw = os.fdopen(msvcrt.open_osfhandle(h, os.O_RDONLY | os.O_BINARY), "rb")
                return raw if binary else io.TextIOWrapper(raw, encoding="utf-8")
            if ctypes.get_last_error() in (2, 3):
                raise FileNotFoundError(2, "No such file", path)
        except FileNotFoundError:
            raise
        except Exception:
            pass
    return io.open(path, "rb") if binary else io.open(path, encoding="utf-8")


def load_json(path):
    with open_shared(path) as fh:
        return json.load(fh)
