---
name: isatty_is_true_for_nul_on_windows_use_getconsolemode_2026_11_12
description: "Script must act only with a person at the keyboard: is sys.stdin.isatty() enough on Windows? No. It is True for the NUL device (stdin=DEVNULL), so a headless job passes. Ask the console API too: GetConsoleMode on the stdin handle succeeds only on a real console. Seen 12 Nov in the Codex hooks installer's own test; with it NUL, a redirected file and a piped word are all refused."
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T00:32:14+02:00
  status: verified
  evidence: "agent_run/codex_dispatch (install_codex_dispatch.py is_console, test_install.py T8-T8d, test_install.txt); ledger rows b of 12 Nov"
---

**The trap.** A script that must only act when a person is at the keyboard checked `sys.stdin.isatty()`. Started
with no input at all (`stdin=subprocess.DEVNULL`, which is the NUL device on Windows) the check answered True: NUL
is a character device, and that is all isatty asks. The script went on to `input()`, got end-of-file and refused
there, so nothing was written, but the console check itself had let a headless job through.

**Seen.** 12 Nov 2026, in the test of `install_codex_dispatch.py` (the Codex hooks installer the author runs
himself): the case "a real-looking home with no console" was refused with the wrong message, "nothing typed"
where "not a console" was expected.

**The check that works.** On Windows ask the console API as well:

    import ctypes, msvcrt
    mode = ctypes.c_ulong(0)
    h = msvcrt.get_osfhandle(sys.stdin.fileno())
    is_console = sys.stdin.isatty() and bool(ctypes.windll.kernel32.GetConsoleMode(ctypes.c_void_p(h), ctypes.byref(mode)))

GetConsoleMode succeeds only on a real console handle. With it the three headless cases are told apart and all
refused: NUL, a file redirected into stdin, and a word piped in.

**Where else it matters.** Any guard that keeps an agent from running an owner-only command by asking for a typed
word. Keep the typed word too: the two checks together are what the test exercises.

Evidence: `agent_run/codex_dispatch/test_install.txt` (T8, T8b), ledger rows b of 12 Nov. Related:
[[codex_hooks_start_together_one_line_dispatcher_tested_not_installed_2026_11_11]].

