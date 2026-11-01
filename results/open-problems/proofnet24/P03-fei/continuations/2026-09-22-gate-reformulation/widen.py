"""Give this task's FEI workers the whole machine.  They inherited an 8-core affinity mask (0x15363) from the
render pool's core_steer bridge and were sharing it with a four-core ffmpeg, so eleven processes were splitting
about 2.5 cores.  Logical 14 and 15 are in no pool mask at all.  The owner's order for this task is explicit
about the CPU, so widen to every core and report the change."""
import psutil, os
PAT = ("gates2.py", "exhfast2.py", "cmin2.py", "bclimb.py", "dclimb.py", "vi_par.py", "spawn_main")
ncpu = psutil.cpu_count()
allc = list(range(ncpu))
roots, done = [], 0
procs = list(psutil.process_iter(["pid", "name", "cmdline", "ppid"]))
byid = {p.info["pid"]: p for p in procs}
targets = set()
for p in procs:
    try:
        if p.info["name"] not in ("python.exe", "pythonw.exe"):
            continue
        cl = " ".join(p.info["cmdline"] or [])
        if any(t in cl for t in PAT[:-1]):
            targets.add(p.info["pid"]); roots.append(p.info["pid"])
    except Exception:
        pass
for p in procs:                       # multiprocessing children of those roots
    try:
        if p.info["ppid"] in targets:
            targets.add(p.info["pid"])
    except Exception:
        pass
for pid in sorted(targets):
    try:
        pr = psutil.Process(pid)
        before = pr.cpu_affinity()
        if sorted(before) != allc:
            pr.cpu_affinity(allc); done += 1
    except Exception as e:
        print("  pid %d: %s" % (pid, e))
print("machine has %d logical cpus; widened %d of %d FEI processes to all of them" % (ncpu, done, len(targets)))
