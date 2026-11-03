"""Keep one resident math recall server running.

Starts recall_server.py when no live server answers, restarts it when the recall code changes (a client refuses a
server whose code stamp is older than its own), and waits while the box is past the server's own memory/disk gate.
Run it with the same MATHBRAIN_STORE (and MATHBRAIN_BUILD_SRC, if used) as the clients: the server serves that store
and a client whose environment differs is refused and recalls cold. Windows: start it windowless (pythonw, or a VBS
launcher at logon); the server runs with CREATE_NO_WINDOW at BelowNormal. Linux/macOS: start it from a login item,
a user systemd unit or launchd; the server runs in its own session at nice 10. Never started with python -s (the
clients run without it). Stop: create RECALL_KEEPER_STOP here.
"""
import ctypes, hashlib, json, os, signal, subprocess, sys, tempfile, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE / 'recall_keeper.log'
STOP = HERE / 'RECALL_KEEPER_STOP'
ENDPOINT = HERE / 'endpoint.json'
PYTHON = os.environ.get('RECALL_KEEPER_PYTHON') or sys.executable
WINDOWS = os.name == 'nt'
MAX_AGE = 6 * 3600
NO_WINDOW, BELOW_NORMAL = 0x08000000, 0x00004000
# one keeper per install folder, so a second install or a test copy does not wait on the first
TAG = hashlib.sha256(os.path.normcase(str(HERE)).encode('utf-8')).hexdigest()[:16]


def log(msg):
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H:%M:%S ') + msg + '\n')


def single_instance():
    if not WINDOWS:
        import fcntl
        fh = open(os.path.join(tempfile.gettempdir(), 'MathRecallKeeper_%s.lock' % TAG), 'a')
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            sys.exit(0)
        return fh
    k = ctypes.windll.kernel32
    k.CreateMutexW.restype = ctypes.c_void_p
    h = k.CreateMutexW(None, False, 'Local\\MathRecallKeeper_' + TAG)
    if k.GetLastError() == 183:
        sys.exit(0)
    return h


def alive(pid):
    if not WINDOWS:
        pid = int(pid)
        if pid <= 0:
            return False
        try:
            import psutil
            return psutil.Process(pid).status() != psutil.STATUS_ZOMBIE
        except ImportError:
            pass
        except Exception:
            return False
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return False
        except PermissionError:
            return True
        return True
    k = ctypes.windll.kernel32
    h = k.OpenProcess(0x1000, False, int(pid))
    if not h:
        return False
    code = ctypes.c_ulong()
    k.GetExitCodeProcess(h, ctypes.byref(code))
    k.CloseHandle(h)
    return code.value == 259


def gate():
    sys.path.insert(0, str(HERE))
    import importlib, server_safety
    importlib.reload(server_safety)
    return server_safety.resources()


def stamp_now(endpoint):
    import importlib, recall_protocol
    importlib.reload(recall_protocol)
    return recall_protocol.code_stamp(endpoint.get('model_files', ()))


PROBE_EVERY, PROBE_SLOW, BACKOFF = 600, 45.0, 3600   # 45 s: under 99 pct commit a healthy server probes 10-16 s and the cold path is 31-32 s


def probe(ep):
    """Time one real query through the server. The server reloads its state whenever the math store changes; with
    writers active (30 Oct) a served call took 67-90 s against about 20 s cold, and a client waits 30 s before it
    falls back - so a slow server makes every recall worse. Returns seconds, or None on failure."""
    import socket
    from recall_protocol import CONTEXT_ENV, env_key, send_frame, receive_frame
    s = time.monotonic()
    try:
        with socket.create_connection(('127.0.0.1', int(ep['port'])), timeout=2) as sock:
            sock.settimeout(PROBE_SLOW + 5)
            send_frame(sock, dict(token=ep['token'], code=ep['code'], environment=env_key(),
                                  argv=['Hadamard matrix'], program=str(HERE / 'math_recall.py'),
                                  context={k: os.environ.get(k) for k in CONTEXT_ENV}, cwd=str(HERE)))
            r = receive_frame(sock, time.monotonic() + PROBE_SLOW + 5)
        if r.get('ok') != 1:
            why = str(r.get('why') or 'unnamed')
            log('probe refused after %.1f s: %s' % (time.monotonic() - s, why))
            return None, why
        return time.monotonic() - s, None
    except Exception as e:
        log('probe error after %.1f s: %s' % (time.monotonic() - s, type(e).__name__))
        return None, type(e).__name__


NOT_ADOPTED = set()
NEUTRAL = ('store_moved_during_call',)   # the store was written during the probe: says nothing about speed


def verdict(took, why):
    """'ok', 'slow' or 'neutral'. A refusal because a writer touched the math store mid-call is neutral: the cold
    path would have read the same moving store, so standing the server down for it only sends every recall to the
    cold path (1 Nov: 9 one-hour stand-downs in 19 h, most after such refusals or first-call timeouts)."""
    if took is None:
        return 'neutral' if why in NEUTRAL else 'slow'
    return 'slow' if took > PROBE_SLOW else 'ok'


class Adopted:
    """A live server this keeper did not start (the keeper restarted, or a server outlived its keeper). Held by
    handle so the keeper can probe, restart and reap it like its own child."""
    def __init__(self, pid):
        self.pid, self.returncode = int(pid), None
        try:   # endpoint.json can outlive its server and Windows reuses pids: adopt only recall_server.py itself
            try:
                import psutil
                cmd = ' '.join(psutil.Process(self.pid).cmdline())
            except ImportError:
                if WINDOWS:
                    raise
                with open('/proc/%d/cmdline' % self.pid, 'rb') as f:   # Linux without psutil
                    cmd = f.read().replace(b'\0', b' ').decode('utf-8', 'replace')
        except Exception as e:
            raise OSError('cannot read pid %d: %s' % (self.pid, type(e).__name__))
        if 'recall_server.py' not in cmd:
            raise OSError('pid %d is not a recall server' % self.pid)
        if not WINDOWS:
            return   # not our child: no exit code to read, so poll() judges by liveness
        k = ctypes.windll.kernel32
        k.OpenProcess.restype = ctypes.c_void_p
        self.h =k.OpenProcess(0x1000 | 0x0001 | 0x00100000, False, self.pid)
        if not self.h:
            raise OSError('cannot open server pid %d' % self.pid)

    def poll(self):
        if self.returncode is None and not WINDOWS:
            if not alive(self.pid):
                self.returncode = 'unknown'
            return self.returncode
        if self.returncode is None:
            code = ctypes.c_ulong()
            ctypes.windll.kernel32.GetExitCodeProcess(ctypes.c_void_p(self.h), ctypes.byref(code))
            if code.value != 259:
                self.returncode = code.value
        return self.returncode

    def terminate(self):
        if self.poll() is None and not WINDOWS:
            try:
                os.kill(self.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
        elif self.poll() is None:
            ctypes.windll.kernel32.TerminateProcess(ctypes.c_void_p(self.h), 1)

    def wait(self, timeout=None):
        if not WINDOWS:
            end = time.monotonic() + (timeout or 60)
            while self.poll() is None and time.monotonic() < end:
                time.sleep(.2)
            return self.poll()
        ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_void_p(self.h), int((timeout or 60) * 1000))
        return self.poll()


def main():
    single_instance()
    log('keeper up pid %d' % os.getpid())
    child, wait_until = None, 0
    next_probe, slow = time.time() + 120, 0
    # Keep the store and package the clients name; drop eval and control dials. Filtered in place, so the probe's
    # environment key is the one the server is started with.
    for k in list(os.environ):
        if (k.startswith(('MATHBRAIN_', 'MATH_BRAIN_', 'MATH_RECALL_', 'MATH_STRENGTH_'))
                and k not in ('MATHBRAIN_STORE', 'MATHBRAIN_BUILD_SRC')):
            del os.environ[k]
    if not os.environ.get('MATHBRAIN_STORE'):
        log('no MATHBRAIN_STORE - nothing to serve; keeper exits')
        return
    env = dict(os.environ)
    while not STOP.exists():
        try:
            ep = json.loads(ENDPOINT.read_text(encoding='utf-8')) if ENDPOINT.exists() else None
            if ep and alive(ep.get('pid', 0)):
                if (child is None or child.pid != ep['pid']) and ep['pid'] not in NOT_ADOPTED:
                    try:
                        child = Adopted(ep['pid'])
                        next_probe, slow = time.time() + 120, 0
                        log('adopted running server pid %d' % child.pid)
                    except OSError as e:
                        NOT_ADOPTED.add(ep['pid'])
                        log('cannot adopt server pid %s: %s' % (ep.get('pid'), e))
                if child is not None and child.pid == ep['pid'] and ep.get('stamp') != stamp_now(ep):
                    log('code changed - restarting server %d' % child.pid)
                    child.terminate()
                    child.wait(60)
                    child = None
                elif child is not None and child.pid == ep['pid'] and time.time() >= next_probe:
                    took, why = probe(ep)
                    v = verdict(took, why)
                    if v == 'neutral':
                        next_probe = time.time() + 120
                        log('probe not counted (%s) - again in 120 s (slow streak %d)' % (why, slow))
                        time.sleep(60)
                        continue
                    next_probe = time.time() + PROBE_EVERY
                    slow = slow + 1 if v == 'slow' else 0
                    log('probe %s s (slow streak %d)' % ('fail ' + str(why) if took is None else '%.1f' % took, slow))
                    if slow >= 2:
                        log('server slower than the cold path twice - standing it down for %d s' % BACKOFF)
                        child.terminate()
                        child.wait(60)
                        child, slow, wait_until = None, 0, time.time() + BACKOFF
                        continue
                time.sleep(60)
                continue
            if child is not None and child.poll() is None:
                time.sleep(10)          # still loading (the encoder and the prepared state take a while)
                continue
            if child is not None:
                log('server exited rc %s' % child.returncode)
                if child.returncode not in (0,):
                    wait_until = max(wait_until, time.time() + 300)
                child = None
            if time.time() < wait_until:
                time.sleep(30)
                continue
            g = gate()
            if not g.get('allowed'):
                log('gate closed %s - waiting' % json.dumps(g))
                wait_until = time.time() + 300
                continue
            out = open(HERE / 'recall_server_stdio.log', 'a', encoding='utf-8')
            how = dict(creationflags=NO_WINDOW | BELOW_NORMAL) if WINDOWS else dict(start_new_session=True)
            child = subprocess.Popen([PYTHON, str(HERE / 'recall_server.py'), '--max-age', str(MAX_AGE)],
                                     cwd=str(HERE), env=env, stdout=out, stderr=out, stdin=subprocess.DEVNULL, **how)
            log('started server pid %d' % child.pid)
            next_probe, slow = time.time() + 120, 0
            time.sleep(30)
        except Exception as e:
            log('error %s: %s' % (type(e).__name__, e))
            time.sleep(120)
    log('stop file - keeper exits (the server stops on its own at max age, or with SERVER_STOP)')


if __name__ == '__main__':
    main()
