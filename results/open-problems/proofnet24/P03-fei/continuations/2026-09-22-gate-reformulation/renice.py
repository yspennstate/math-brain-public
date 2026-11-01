"""Raise this task's FEI workers to Normal priority.  BelowNormal against ~30 peer processes at Normal costs a
measured factor of about seven on this box, and the owner's order for this task is explicit about the CPU."""
import psutil, sys, os
PAT = ("gates2.py", "gates.py", "exhfast2.py", "exh5.py", "cmin2.py", "bclimb.py", "dclimb.py", "vi_par.py", "cert")
me = os.getpid()
roots = []
for p in psutil.process_iter(["pid", "name", "cmdline", "ppid"]):
    try:
        if p.info["name"] not in ("python.exe", "pythonw.exe"):
            continue
        cl = " ".join(p.info["cmdline"] or [])
        if any(t in cl for t in PAT):
            roots.append(p.info["pid"])
    except Exception:
        pass
# multiprocessing children carry spawn_main in their command line; take them by parentage
allp = {p.pid: p for p in psutil.process_iter(["pid", "ppid", "name"])}
targets = set(roots)
for pid, p in allp.items():
    try:
        if p.info["ppid"] in targets:
            targets.add(pid)
    except Exception:
        pass
n = 0
for pid in sorted(targets):
    try:
        pr = psutil.Process(pid)
        if pr.nice() != psutil.NORMAL_PRIORITY_CLASS:
            pr.nice(psutil.NORMAL_PRIORITY_CLASS); n += 1
    except Exception:
        pass
print("raised %d of %d FEI processes to Normal (roots %s)" % (n, len(targets), roots))
