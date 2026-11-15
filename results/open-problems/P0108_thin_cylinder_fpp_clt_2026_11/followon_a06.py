"""P0108: the a = 0.6 cell is the only one whose skewness still moves with n (-0.017 .. -0.112 for n = 256..2048, 184
samples at 4096). Laptop GPU, 14 Nov 19:1x (an agent): n = 4096 at a = 0.6 for 3 h, then n = 8192 at a = 0.6
for 3 h. Rows go to fpp_rows_cuda.jsonl. Stops on ./STOP. Log followon_a06.log."""
import os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
py = sys.executable.replace("pythonw.exe", "python.exe")
with open(os.path.join(HERE, "followon_a06.log"), "a") as log:
    for ns, budget in (("4096", "10800"), ("8192", "10800")):
        if os.path.exists(os.path.join(HERE, "STOP")):
            sys.exit(3)
        env = dict(os.environ, FPP_NS=ns, FPP_AS="0.6", FPP_WAIT_IDLE="0")
        log.write("n=%s a=0.6 start %s\n" % (ns, time.strftime("%H:%M"))); log.flush()
        rc = subprocess.call([py, os.path.join(HERE, "fpp_cyl_cuda.py"), os.path.join(HERE, "fpp_rows_cuda.jsonl"), budget],
                             cwd=HERE, env=env, stdout=log, stderr=log, creationflags=0x08000000)
        log.write("n=%s a=0.6 exit %s %s\n" % (ns, rc, time.strftime("%H:%M"))); log.flush()
