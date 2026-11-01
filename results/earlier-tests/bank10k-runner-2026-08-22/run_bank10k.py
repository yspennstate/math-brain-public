"""Three-arm runner for bank10k: none / placebo / brain.

THE BANK IS THE POPULATION, NOT THE RUN. 12,096 items x 3 arms is ~36,000 model calls - roughly
400 hours sequential at the ~40s/call this machine measures, and four figures of spend. Nobody
should serve the whole bank. `sample` draws a FROZEN stratified subset and everything downstream
runs against that, so the run is reproducible and its cost is known before it starts.

STRATIFICATION. The faulted half is stratified over the 50 reasoning cells
(family x fault step x mechanism) so no cell dominates a small sample, and clean controls are
drawn proportionally. A sample that over-weights one family measures that family, not the brain.

ARMS. `none` gets no reference notes, `placebo` gets matched notes with relevance broken by a
deterministic derangement, `brain` gets notes retrieved from the math-brain population store.
brain-vs-placebo is the ONLY contrast that identifies content value - the 2026-08-09 V5 headline
died because a placebo arm reproduced the brain arm 48/48, so the gap had measured notes being
PRESENT, not the store knowing anything.

SCORING. Full credit on a faulted item needs verdict "flawed" AND the exact fault step. Clean
controls are the false-positive control and are never a scoring opportunity.

Usage:
  python run_bank10k.py sample --n 300      # freeze a stratified sample
  python run_bank10k.py notes               # brain + placebo notes for the sample
  python run_bank10k.py serve --arm none    # [--limit N], resumable
  python run_bank10k.py grade
  python run_bank10k.py status
"""
import argparse
import collections
import datetime
import glob
import hashlib
import json
import os
import random
import re
import sqlite3
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL = os.path.dirname(HERE)
RUN = os.path.join(HERE, "run")
ITEMS = os.path.join(HERE, "items", "bank10k.jsonl")
KEYS = r"<HOME>\bank10k_keys_quarantine\bank10k_keys.jsonl"
STORE = r"<HOME>\math-brain-build\local\population\brain.sqlite3"
CLAUDE = os.environ.get("CLAUDE_BIN", r"<HOME>\AppData\Roaming\npm\claude.cmd")
MODEL = "claude-haiku-4-5"
# CLAUDE_STERILE=1 runs every solver call with no setting sources: no hooks (the math_sense
# injection reached every earlier haiku arm, treated and untreated alike) and no global
# CLAUDE.md (a plain -p session reports a private setting from it; with --setting-sources ""
# it reports none - both measured 2026-08-29). The empty argument survives claude.cmd's
# tokenizer when passed through Popen as its own list element; do not join it into a string.
# Read at call time, not import time: run_acceptance imports this module before it sets the
# variable for the solver it is about to serve.
def _sterile_args():
    # STERILE BY DEFAULT since 2026-09-02. The flag used to be opt-in (CLAUDE_STERILE=1), and every
    # relaunch made from a shell without the variable served with hooks on: the powered brain-vs-none
    # run carried hook injections ([unconscious] reflexes, the exact-clause guard, compute notices) in
    # 829 of its 1,200 serves (none 407/600, brain 422/600 - balanced, so the paired null stood, but
    # only 123 pairs met the protocol), and a B12 brain-arm relaunch at 02:23 the same night did the
    # same for 7 items. Opt OUT explicitly with CLAUDE_STERILE=0; and the transcript receipt below
    # (transcript_sterile) refuses a verdict whose transcript shows an injection regardless of flags.
    return [] if os.environ.get("CLAUDE_STERILE") == "0" else ["--setting-sources", ""]


HOOK_MARKERS = ("[unconscious]", "[compute-instinct]", "instinct surfacing", "hook additional context",
                "[ack-gate]", "[health-check]", "BRAIN SELF-CARE", "[danger-sense]", "[math-sense]")
_last_call = threading.local()


def _transcript_path(session_id):
    """Claude Code writes ~/.claude/projects/<cwd slug>/<session_id>.jsonl; the slug replaces ':' '\\' '/'
    and '_' with '-'. A glob over every project dir is the fallback when the slug rule drifts."""
    slug = re.sub(r"[:\\/_]", "-", os.getcwd())
    p = os.path.join(os.path.expanduser("~"), ".claude", "projects", slug, session_id + ".jsonl")
    if os.path.exists(p):
        return p
    hits = glob.glob(os.path.join(os.path.expanduser("~"), ".claude", "projects", "*", session_id + ".jsonl"))
    return hits[0] if hits else p


def transcript_sterile(session_id, wait_s=5.0):
    """(True, path) when the served session's transcript exists and carries no hook injection;
    (False, why) otherwise. FAIL CLOSED: a session whose transcript cannot be found is not proven
    sterile. The flag is a promise; the transcript is the receipt (2026-09-02)."""
    if not session_id:
        return False, "no session_id in the claude envelope"
    p = _transcript_path(session_id)
    t0 = time.time()
    while not os.path.exists(p) and time.time() - t0 < wait_s:
        time.sleep(0.25)
        p = _transcript_path(session_id)
    if not os.path.exists(p):
        return False, "transcript not found for session %s (looked at %s)" % (session_id, p)
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            t = f.read()
    except OSError as e:
        return False, "transcript unreadable: %s" % e
    hits = [m for m in HOOK_MARKERS if m in t]
    if hits:
        return False, "hook injection in transcript %s: %s" % (os.path.basename(p), ", ".join(hits))
    return True, p
ARMS = ("none", "placebo", "brain")
SEED = 20260817
N_NOTES = 3

sys.path.insert(0, EVAL)


def read_jsonl(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def dump_atomic(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)
    os.replace(tmp, path)


def load_bank():
    items = {i["item_id"]: i for i in read_jsonl(ITEMS)}
    keys = {k["item_id"]: k for k in read_jsonl(KEYS)}
    return items, keys


# ---------------------------------------------------------------- sample

def cmd_sample(args):
    items, keys = load_bank()
    faulted = [i for i in items if keys[i].get("truth") == "flawed"]
    clean = [i for i in items if keys[i].get("truth") == "clean"]

    cells = collections.defaultdict(list)
    for iid in faulted:
        k = keys[iid]
        cells[(k["family_id"], k["fault_step"], k["mechanism"])].append(iid)

    rng = random.Random(SEED)
    n_clean = max(1, round(args.n * len(clean) / len(items)))
    n_faulted = args.n - n_clean
    per_cell = max(1, n_faulted // len(cells))

    picked = []
    for cell in sorted(cells):
        pool = sorted(cells[cell])
        picked += rng.sample(pool, min(per_cell, len(pool)))
    # top up to the requested faulted count from the remaining pool, still deterministic
    rest = sorted(set(faulted) - set(picked))
    if len(picked) < n_faulted and rest:
        picked += rng.sample(rest, min(n_faulted - len(picked), len(rest)))
    picked_clean = rng.sample(sorted(clean), min(n_clean, len(clean)))

    by_strat = collections.Counter(keys[i].get("ambiguity_stratum", "instance") for i in picked)
    sample = {
        "seed": SEED,
        # BANK FINGERPRINT. Item ids are hashes of family + parameters + step + mechanism, so any
        # change to a family's grid RETIRES ids and mints new ones. A sample frozen against an
        # older bank then references items that no longer exist - measured 2026-08-17: 32 of 300
        # ids had evaporated across a night of family edits, and serving it would have crashed on
        # the first missing id or, worse, quietly served a skewed subset. The guard below refuses.
        "bank_fingerprint": bank_fingerprint(items),
        # The bank fingerprint moves when the bank merely GROWS, which is a normal working state
        # here (adding fault sites while a measurement is in flight). This hash is the check that
        # actually matters: the SERVED TEXT of the sampled items. See sampled_text_hash.
        "sampled_text_hash": sampled_text_hash(items, sorted(picked) + sorted(picked_clean)),
        "requested": args.n,
        "n_faulted": len(picked),
        # The primary metric only sees the instance stratum, so this - not n_faulted - is the
        # number that sets the run's power. Read it before deciding the sample is big enough.
        "n_faulted_by_stratum": dict(by_strat),
        "n_primary_metric_items": by_strat["instance"],
        "n_clean": len(picked_clean),
        # Two fields, because one ambiguous name misled me into reporting "78 of 93 cells covered"
        # when the sample in fact touched EVERY cell that existed. `cells_total` is how many
        # reasoning cells the bank has; `cells_covered` is how many the draw actually reaches.
        "cells_total": len(cells),
        "cells_covered": len({c for c in cells if any(i in picked for i in cells[c])}),
        "per_cell": per_cell,
        # COST, RE-MEASURED 2026-08-17 from run 1's verdict mtimes. The old note used ~40s/call and
        # was 2x optimistic: 149 gaps across the completed brain arm give a median of 79s and a mean
        # of 96s. It also quoted one number without saying whether the arms run one after another or
        # together, which are different answers. Concurrency is NOT the bottleneck - brain alone
        # after placebo finished ran at median 78.5s versus 81.8s while both were live - so arms in
        # parallel cost the same wall time as one arm.
        "cost_note": (f"{(len(picked)+len(picked_clean))*3} model calls for three arms. Measured "
                      f"~90s/call (median 79s, mean 96s over run 1) and ~$0.04/call: about "
                      f"{(len(picked)+len(picked_clean))*3*90/3600:.1f} h of total working time, or "
                      f"about {(len(picked)+len(picked_clean))*90/3600:.1f} h WALL if the three arms "
                      f"run in parallel, and ${(len(picked)+len(picked_clean))*3*0.04:.0f}"),
        "item_ids": sorted(picked) + sorted(picked_clean),
    }
    dump_atomic(os.path.join(RUN, "SAMPLE.json"), sample)
    print(json.dumps({k: v for k, v in sample.items() if k != "item_ids"}, indent=1))
    print(f"frozen to {os.path.join(RUN,'SAMPLE.json')}")


def bank_fingerprint(items):
    """Identity of the bank a sample was drawn from: count plus a hash of every item id."""
    h = hashlib.sha256("|".join(sorted(items)).encode("utf-8")).hexdigest()[:16]
    return {"n_items": len(items), "id_hash": h}


def sampled_text_hash(items, ids):
    """Hash of the SERVED TEXT of the sampled items - the check id-existence cannot make.

    item_id hashes family|parameters|step|mechanism and NOT the text, so editing a site's
    `faulty_text` in place keeps every id and silently changes the question. An id-existence check
    waves that through; only hashing the text catches it. Relaxing the bank fingerprint to allow
    growth (see load_sample) is safe exactly and only because this check sits behind it.
    """
    h = hashlib.sha256()
    for i in sorted(ids):
        it = items.get(i)
        if it is None:
            continue
        h.update(it["claim"].encode("utf-8"))
        for s in it["argument_steps"]:
            h.update(b"|")
            h.update(s["text"].encode("utf-8"))
    return h.hexdigest()[:16]


def sample_fingerprint(ids):
    """Identity of the frozen sample the notes were built against.

    The guard chain has to run the WHOLE way down: bank -> sample -> notes. Fingerprinting the
    sample against the bank and stopping left the notes free to rot. Measured 2026-08-17: after a
    re-freeze, 278 of 300 sampled items had NO notes and the notes file held 278 ids that were no
    longer sampled - serving the brain arm would have handed 93% of the run empty notes, making
    brain identical to none and producing a null result that meant nothing. Fixing the original is
    half the correction; the other half is hunting the copies.
    """
    h = hashlib.sha256("|".join(sorted(ids)).encode("utf-8")).hexdigest()[:16]
    return {"n_ids": len(ids), "id_hash": h}


def load_sample():
    p = os.path.join(RUN, "SAMPLE.json")
    if not os.path.exists(p):
        sys.exit("no frozen sample - run `sample --n N` first")
    s = json.load(open(p, encoding="utf-8"))
    items, _ = load_bank()
    now = bank_fingerprint(items)
    was = s.get("bank_fingerprint")
    if was != now:
        # WHAT BREAKS A SAMPLE IS A MISSING ITEM, NOT A CHANGED FINGERPRINT. The fingerprint hashes
        # every id in the bank, so it also moves when the bank merely GROWS - and a bank that grew
        # has retired nothing: every sampled id still resolves, the served text is identical, and a
        # run against it is exactly the run you intended. Refusing there would block the ordinary
        # case of adding fault sites while a measurement is in flight, which is how this bank is
        # meant to be worked. So: refuse on MISSING ids, say so loudly on growth, and let it run.
        missing = [i for i in s["item_ids"] if i not in items]
        if missing:
            sys.exit("\n".join([
                "STALE SAMPLE - refusing to serve.",
                f"  frozen against: {was}",
                f"  bank is now   : {now}",
                f"  {len(missing)} of {len(s['item_ids'])} sampled ids NO LONGER EXIST.",
                "  Item ids encode family+parameters+step+mechanism, so editing a family retires ids.",
                "  Re-freeze with `sample --n N`; a run against a stale sample is not the run you",
                "  think you are doing.",
            ]))
        was_text = s.get("sampled_text_hash")
        now_text = sampled_text_hash(items, s["item_ids"])
        if was_text is None:
            print("WARNING: this sample predates the text hash, so 'the questions are unchanged' is "
                  "UNTESTABLE here, not verified. Re-freeze to get the check.")
        elif was_text != now_text:
            sys.exit("\n".join([
                "SAMPLE TEXT CHANGED - refusing to serve.",
                f"  every sampled id still exists, but the SERVED TEXT hash moved "
                f"{was_text} -> {now_text}.",
                "  item_id does not hash the text, so editing a site's faulty_text in place keeps",
                "  the id and changes the question underneath a frozen sample. Re-freeze.",
            ]))
        grew = now["n_items"] - was["n_items"]
        print(f"NOTE: the bank has changed since this sample was frozen "
              f"({was['n_items']} -> {now['n_items']} items, {grew:+d}), but all "
              f"{len(s['item_ids'])} sampled ids still exist"
              f"{' and their served text is byte-identical' if was_text else ''}, so this run is "
              f"valid for the sampled population.")
        if grew > 0:
            print("      The sample was stratified over the cells that existed when it was frozen; "
                  "it does NOT cover cells added since. Re-freeze before quoting bank-wide coverage.")
    return s["item_ids"]


# ---------------------------------------------------------------- notes

_WORD = re.compile(r"[A-Za-z][A-Za-z\-']{2,}")
_STOP = set("""the and for that with from this there then thus hence some every all any not are
was were has have had its their which when where such into over under one two let put give gives
given show shows shown holds hold follows follow since because therefore""".split())


def _tok(t):
    return {w.lower() for w in _WORD.findall(t or "")} - _STOP


def cmd_notes(args):
    items, _ = load_bank()
    ids = load_sample()
    conn = sqlite3.connect(STORE)
    nodes = [(nid, ti, bo) for nid, ti, bo in conn.execute("select id, title, body from nodes")]
    n_nodes = len(nodes)
    conn.close()
    toks = [(nid, ti, bo, _tok(ti) | _tok(bo)) for nid, ti, bo in nodes]

    brain = {}
    for n, iid in enumerate(ids):
        q = _tok(items[iid]["claim"])
        scored = []
        for nid, ti, bo, t in toks:
            ov = len(q & t)
            if ov:
                scored.append((ov / (len(q) ** 0.5 + len(t) ** 0.5), nid, ti, bo))
        scored.sort(reverse=True)
        brain[iid] = [{"node_id": a, "title": b, "body": (c or "")[:1200]}
                      for _, a, b, c in scored[:N_NOTES]]
        if (n + 1) % 50 == 0:
            print(f"  {n+1}/{len(ids)}", flush=True)

    shift = 37 % len(ids) or 1
    placebo = {iid: brain[ids[(k + shift) % len(ids)]] for k, iid in enumerate(ids)}

    # A PLACEBO THAT EQUALS THE TREATMENT IS NOT A PLACEBO. The shift guarantees no item is handed
    # its OWN notes - 37 is not 0 mod n - but it cannot stop two DIFFERENT items from retrieving the
    # same top-k nodes, and then the placebo arm is served exactly what the brain arm is served.
    # Measured on the 300-item sample 2026-08-17: 7 items were byte-identical, 3 of them in the
    # primary instance stratum. Those items are concordant by construction and can carry no
    # brain-vs-placebo signal at all.
    # Kept small and honest: the damage is a power loss, not a bias - McNemar already discards
    # concordant pairs, so 3 dead items cost under one expected discordant pair at the observed 22%
    # discordant rate. That is why the run in flight when this was found was NOT restarted for it.
    def _node_ids(rows):
        return [r["node_id"] for r in rows]

    collisions, n = 0, len(ids)
    for k, iid in enumerate(ids):
        if not brain.get(iid) or _node_ids(placebo[iid]) != _node_ids(brain[iid]):
            continue
        # walk further offsets until this item's donor differs from its own notes
        for extra in range(1, n):
            cand = brain[ids[(k + shift + extra) % n]]
            if _node_ids(cand) != _node_ids(brain[iid]):
                placebo[iid] = cand
                collisions += 1
                break
    if collisions:
        print(f"placebo: re-donated {collisions} item(s) whose shifted notes were IDENTICAL to their "
              f"own brain notes - a placebo equal to the treatment carries no signal")
    fp = sample_fingerprint(ids)
    dump_atomic(os.path.join(RUN, "brain_notes.json"),
                {"store": STORE, "n_nodes": n_nodes, "k": N_NOTES,
                 "sample_fingerprint": fp, "notes": brain})
    dump_atomic(os.path.join(RUN, "placebo_notes.json"),
                {"derived_from": "brain_notes.json",
                 "method": f"deterministic shift by {shift} over the frozen sample order",
                 "sample_fingerprint": fp, "notes": placebo})
    covered = sum(1 for v in brain.values() if v)
    print(f"notes for {len(ids)} sampled items; store {n_nodes} nodes; {covered} got at least one")


# ---------------------------------------------------------------- serve

PROMPT = """You are auditing a numbered mathematical argument.

CLAIM: {claim}

ARGUMENT:
{steps}
{notes}
Return ONLY a JSON object, no prose around it:
{{"verdict": "valid" or "flawed", "fault_step": <integer or null>, "why": "<one or two sentences>"}}

If every step is valid, verdict is "valid" and fault_step is null.
Otherwise verdict is "flawed" and fault_step is the number of the FIRST invalid step.

The standard, stated so it is not left to taste:
- A true conclusion reached by an invalid inference is FLAWED - cite the inference step.
- A step asserting a FALSE GENERAL CLAIM is FLAWED even when the particular instance in this
  argument happens to satisfy it. "This holds for every p >= 1" is an invalid step if it fails at
  p = 1, regardless of the p actually used here.
- A step is NOT flawed merely for omitting a citation to a hypothesis stated elsewhere in this
  argument or in the claim. Judge whether the step is TRUE as written, not whether it is fully
  annotated."""


def build_prompt(item, notes):
    steps = "\n".join(f"{s['n']}. {s['text']}" for s in item["argument_steps"])
    block = ""
    if notes:
        lines = "\n".join(f"- {n['title']}: {n['body']}" for n in notes)
        block = f"\nREFERENCE NOTES (may or may not be relevant to this argument):\n{lines}\n"
    return PROMPT.format(claim=item["claim"], steps=steps, notes=block)


CALL_TIMEOUT_S = 300


def _kill_tree(pid):
    """Kill the whole process tree, not just the direct child.

    THE BUG THIS EXISTS FOR, measured 2026-08-17. `subprocess.run(..., timeout=300)` does NOT
    bound this call. CLAUDE is `claude.cmd`, a batch shim, so the direct child is cmd.exe and the
    real worker is a GRANDCHILD claude.exe holding the stdout pipe. On timeout CPython kills only
    the direct child and then calls communicate() again to reap - and that second call blocks
    forever while the grandchild keeps the pipe open. The arm stays ALIVE with a live sub-invocation
    and produces nothing, which no liveness check catches because the process is not dead.

    Both bank10k arms stalled this way at 07:30:25 and 07:30:35 on a single sub-invocation each and
    were still holding them 9.5 hours later, at ~5 seconds of CPU. taskkill /T takes the tree.
    """
    try:
        subprocess.run(["taskkill", "/F", "/T", "/PID", str(pid)],
                       capture_output=True, timeout=30)
    except Exception:
        pass


def _spawn_claude():
    """Launch the model subprocess, surviving a transient rewrite of the shim.

    THE LOSS THIS EXISTS FOR, measured 2026-08-17/18. Arms died on the SAME
    `FileNotFoundError: [WinError 2]` out of CreateProcess twice in one night - two arms at ~23:21
    and ALL THREE at ~00:05, within 46 seconds of each other. The second outage went unnoticed for
    about 75 minutes of a 300-item run.

    CLAUDE is `claude.cmd`, an npm shim that Claude Code's own auto-updater rewrites IN PLACE.
    `~/.claude/.last-update-result.json` records an attempt at 01:18 local failing with
    `update_apply_exe_locked`, so the rewrite-and-lock window is real on this machine. Only the
    newest update result is retained, so the 00:05 window cannot be confirmed after the fact - the
    mechanism is established, that particular firing is not. Either way an arm has no business dying
    because a launcher file was briefly unopenable.

    A launch failure is transient by construction, so retry with backoff. If every attempt fails the
    caller treats it as ONE unparsed item and moves on; the item keeps no verdict file, so a later
    run redoes it. Never let this end the run.
    """
    delays = [2, 5, 10, 20, 30]
    last = None
    for i, wait in enumerate([0] + delays):
        if wait:
            time.sleep(wait)
        try:
            return subprocess.Popen([CLAUDE, "-p", "--output-format", "json", "--model", MODEL,
                                     *_sterile_args()],
                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True, encoding="utf-8",
                                    errors="replace"), None
        except OSError as e:
            last = e
            print(f"  launch failed (attempt {i + 1}/{len(delays) + 1}): {e.__class__.__name__}: {e}",
                  flush=True)
    return None, f"LAUNCH FAILED after {len(delays) + 1} attempts over "\
                 f"{sum(delays)}s - last error {last.__class__.__name__}: {last}"


def call_claude(prompt):
    # Prompt on STDIN, never argv: claude.cmd is a batch wrapper and a multi-line argument with
    # quotes hangs it indefinitely (measured 2026-08-17: 10 minutes, zero returns).
    proc, launch_err = _spawn_claude()
    if proc is None:
        return None, [], launch_err
    try:
        out, err = proc.communicate(prompt, timeout=CALL_TIMEOUT_S)
    except subprocess.TimeoutExpired:
        _kill_tree(proc.pid)
        try:
            proc.communicate(timeout=30)
        except Exception:
            pass
        # A timeout is an ERROR for this item, never a verdict. cmd_serve counts it as unparsed
        # and moves on; the item simply has no verdict file, so a later run redoes it.
        return None, [], f"TIMEOUT after {CALL_TIMEOUT_S}s (tree killed)"
    if proc.returncode != 0:
        return None, [], (err or "")[:400]
    try:
        env = json.loads(out)
    except json.JSONDecodeError:
        return None, [], (out or "")[:400]
    served = sorted((env.get("modelUsage") or {}).keys())
    _last_call.session_id = env.get("session_id")   # for the transcript receipt, same thread
    text = env.get("result") or ""
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None, served, text[:400]
    try:
        d = json.loads(m.group(0))
    except json.JSONDecodeError:
        return None, served, text[:400]
    return (d if "verdict" in d else None), served, text[:400]


CANARY = "8391-KQ-ZULU"


def preflight(nonce=CANARY, via="stdin"):
    """Prove the model receives the WHOLE prompt before spending a run on it.

    `claude.cmd` is a batch shim; Windows runs it through `cmd.exe /c`, and cmd's tokenizer stops
    at the first newline. Passed on argv, every call would receive only line one - no claim, no
    argument, no notes - AND THE MODEL WOULD STILL ANSWER. The run completes, verdicts land,
    grading is clean, and the whole thing measures nothing. A hang announces itself; silent
    truncation does not. Hence one cheap multi-line call, with the nonce on the LAST line, before
    any arm is served.

    THE PROBE'S WORDING IS LOAD-BEARING, and the first version got it wrong. It read

        You are running a transport check.
        Ignore everything except the next line.
        NONCE: ...

    and the model refused: "that's a prompt injection attempt, and I'm not going to follow it."
    That is a FAIL from a canary whose failure message said "the prompt is being truncated" - a
    false alarm that would have blocked every run on this machine, and pointed the next reader at
    a transport bug that does not exist. The reply itself disproved the diagnosis: you cannot
    recognise line two as an injection attempt without having received line two.

    So: no override language, nothing that reads as an instruction to disregard the surrounding
    context. A refusal and a truncation both look like a missing nonce, and only the wording keeps
    them apart. `via="argv"` runs the identical probe down the known-broken path - the positive
    control, because a checker that has never returned FAIL for the real reason has not been shown
    to detect anything.
    """
    probe = ("This is a connectivity check for a local test harness - no task, no analysis.\n"
             "A short reference code is printed at the end of this message.\n"
             "Reply with that code and nothing else.\n"
             f"CODE: {nonce}")
    cmd = [CLAUDE, "-p", "--output-format", "json", "--model", MODEL, *_sterile_args()]
    kw = dict(capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
    try:
        if via == "argv":
            proc = subprocess.run(cmd + [probe], **kw)
        else:
            proc = subprocess.run(cmd, input=probe, **kw)
    except subprocess.TimeoutExpired:
        return False, f"transport check ({via}) timed out"
    if proc.returncode != 0:
        return False, f"transport check ({via}) failed to run: {(proc.stderr or '')[:200]}"
    try:
        env = json.loads(proc.stdout)
        text = env.get("result") or ""
        _last_call.session_id = env.get("session_id")   # the probe's transcript is the sterility control
    except json.JSONDecodeError:
        return False, f"transport check ({via}) returned unparseable output"
    if nonce not in text:
        return False, (f"the code on the LAST line did not come back ({via}). Either the prompt is "
                       "being truncated before it arrives, or the model declined the probe - read "
                       f"what it said before believing the first. Model said: {text[:200]!r}")
    return True, f"full multi-line prompt reaches the model ({via})"


def cmd_serve(args):
    items, _ = load_bank()
    ids = load_sample()
    notes = {}
    if args.arm in ("brain", "placebo"):
        p = os.path.join(RUN, f"{args.arm}_notes.json")
        if not os.path.exists(p):
            sys.exit(f"{p} missing - run `notes` first")
        blob = json.load(open(p, encoding="utf-8"))
        # Third link of the guard chain: bank -> sample -> NOTES. Notes built against an earlier
        # sample leave most items with no notes at all, which silently turns the brain arm into
        # the none arm.
        want, got = sample_fingerprint(ids), blob.get("sample_fingerprint")
        if want != got:
            covered = len(set(ids) & set(blob["notes"]))
            sys.exit("\n".join([
                f"STALE NOTES ({args.arm}) - refusing to serve.",
                f"  built against: {got}",
                f"  sample is now: {want}",
                f"  only {covered} of {len(ids)} sampled items have notes.",
                "  Serving now would hand most of the arm EMPTY notes and quietly make it the",
                "  none arm. Rebuild with `notes`.",
            ]))
        notes = blob["notes"]
    ok, why = preflight()
    print(f"transport check: {'PASS' if ok else 'FAIL'} - {why}")
    if not ok:
        sys.exit("refusing to serve: a truncated prompt produces verdicts that look fine and "
                 "measure nothing")
    sterile, why = transcript_sterile(getattr(_last_call, "session_id", None))
    print(f"sterility check: {'PASS' if sterile else 'FAIL'} - {why}")
    if not sterile:
        sys.exit("refusing to serve: the probe's own transcript is not proven sterile. Every verdict "
                 "would carry the hooks' injections (reflexes, guards, compute notices) and the arm "
                 "would not be the arm it claims. Launch without CLAUDE_STERILE=0, and check that "
                 "--setting-sources \"\" reaches claude (see _sterile_args).")

    outdir = os.path.join(RUN, "verdicts", args.arm)
    os.makedirs(outdir, exist_ok=True)

    def already_done(iid):
        out_p = os.path.join(outdir, f"{iid}.json")
        if os.path.exists(out_p):
            try:
                if json.load(open(out_p, encoding="utf-8")).get("answer"):
                    return True
            except json.JSONDecodeError:
                pass
        return False

    todo = [i for i in ids if not already_done(i)]
    if args.limit:
        todo = todo[:args.limit]

    def serve_one(iid):
        """Returns ('done'|'reject'|'err', iid). Writes its own verdict file and nothing shared."""
        ans, served, raw = call_claude(build_prompt(items[iid], notes.get(iid, [])))
        if not any(s.startswith("claude-haiku") for s in served):
            return "reject", iid, served
        if ans is None:
            return "err", iid, raw
        # The transcript is the sterility receipt: a served session that carried a hook injection is
        # not a measurement of the arm it claims to be (2026-09-02 - see _sterile_args). Rejected
        # items keep no verdict file and are re-served; a run that rejects everything is telling the
        # operator the launch path is wrong, not asking to be relaunched harder.
        sterile, why = transcript_sterile(getattr(_last_call, "session_id", None))
        if not sterile:
            return "reject", iid, "UNSTERILE - " + why
        dump_atomic(os.path.join(outdir, f"{iid}.json"),
                    {"item_id": iid, "arm": args.arm, "answer": ans,
                     "served_models": served, "n_notes": len(notes.get(iid, []))})
        return "done", iid, None

    done = errs = rejected = 0
    n = max(1, int(getattr(args, "concurrency", 1) or 1))
    # CONCURRENCY IS OPT-IN AND DEFAULTS TO 1, so an existing run's behaviour is untouched.
    #
    # Measured 2026-08-18 on this machine, with three arms already serving in the background (so
    # these are MARGINAL rates on top of real load, not clean-machine numbers - the ratio is what
    # transfers, and it was measured under the conditions a bigger run would actually face):
    #
    #     N=1 (sequential)   141 calls/h    per-call 25.5s
    #     N=3                267 calls/h    per-call 36.5s     1.89x
    #     N=5                227 calls/h    per-call 63.9s     1.60x
    #
    # Throughput PEAKS AT 3 and gets worse at 5: per-call latency grows faster than the parallelism
    # buys back. So this is not a dial to turn up - 3 is the measured optimum and 5 is already
    # counterproductive. The calls are network-bound (the serve processes measured 0.00 CPU seconds
    # over 20s while blocked), so the cost of concurrency is latency contention, not local CPU.
    if n == 1:
        results = (serve_one(i) for i in todo)
        for kind, iid, extra in results:
            if kind == "reject":
                rejected += 1
                print(f"  REJECT {iid}: served {extra}", flush=True)
            elif kind == "err":
                errs += 1
            else:
                done += 1
                if done % 25 == 0:
                    print(f"  {args.arm}: {done}", flush=True)
    else:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=n) as ex:
            for kind, iid, extra in ex.map(serve_one, todo):
                if kind == "reject":
                    rejected += 1
                    print(f"  REJECT {iid}: served {extra}", flush=True)
                elif kind == "err":
                    errs += 1
                else:
                    done += 1
                    if done % 25 == 0:
                        print(f"  {args.arm}: {done} (concurrency {n})", flush=True)

    print(f"{args.arm}: {done} served, {errs} unparsed, {rejected} rejected on served model")


# ---------------------------------------------------------------- grade

def norm(v):
    v = (v or "").strip().lower()
    if v.startswith("flaw") or v in ("invalid", "incorrect", "false"):
        return "flawed"
    if v.startswith("valid") or v in ("clean", "correct", "sound", "true"):
        return "clean"
    return v


def cmd_grade(args):
    from score_tools import mcnemar_exact_two_sided
    _, keys = load_bank()
    # SCORE THE FROZEN SAMPLE, NOT WHATEVER FILES HAPPEN TO BE ON DISK. This globbed the verdict
    # directory, so a verdict left behind by an EARLIER sample was scored as though it belonged to
    # this one: measured 2026-08-17, brain held 1 out-of-sample verdict and the `none` arm held 2,
    # which were both of the verdicts it had. Item-id pairing kept the primary contrast safe, but
    # the per-arm rates and `served` counts were contaminated, and a stale id shared by two arms
    # would have entered the paired contrast outright. `keys[iid]` would also KeyError on an id the
    # bank has since retired, which is a crash waiting for the next relabel.
    sp = os.path.join(RUN, "SAMPLE.json")
    sample_ids = (set(json.load(open(sp, encoding="utf-8"))["item_ids"])
                  if os.path.exists(sp) else None)
    if sample_ids is None:
        print("WARNING: no SAMPLE.json - grading every verdict on disk, which is NOT a defined "
              "population. Freeze a sample before quoting any number from this.")
    per_arm, per_item = {}, collections.defaultdict(dict)
    excluded_total = {}
    for arm in ARMS:
        rows, excluded = {}, []
        for p in glob.glob(os.path.join(RUN, "verdicts", arm, "*.json")):
            r = json.load(open(p, encoding="utf-8"))
            iid = r["item_id"]
            if sample_ids is not None and iid not in sample_ids:
                excluded.append(iid)
                continue
            rows[iid] = r["answer"]
        # Never a silent cap: say what was dropped and why, or a contaminated run reads as clean.
        excluded_total[arm] = len(excluded)
        if excluded:
            print(f"NOTE ({arm}): {len(excluded)} verdict(s) on disk are NOT in the frozen sample "
                  f"and were excluded from scoring - {excluded[:3]}")
        # Scored BY STRATUM. `instance` is the primary metric; `generalization` and `insufficient`
        # are reported beside it and never merged in, because a solver can be right to answer
        # VALID on those (see the stratum definitions in generate.py). Pooling them would let an
        # ambiguity-driven miss look like a reasoning failure.
        strat = collections.defaultdict(lambda: {"full_credit": 0, "n": 0})
        c_ok = c_n = 0
        for iid, a in rows.items():
            k = keys[iid]
            v = norm(a.get("verdict"))
            if k["truth"] == "clean":
                c_n += 1
                c_ok += int(v == "clean")
                continue
            ok = False
            if v == "flawed":
                try:
                    ok = int(a.get("fault_step")) == k["fault_step"]
                except (TypeError, ValueError):
                    ok = False
            s = k.get("ambiguity_stratum", "instance")
            strat[s]["n"] += 1
            strat[s]["full_credit"] += int(ok)
            if s == "instance":
                per_item[iid][arm] = ok
        per_arm[arm] = {
            "faulted_PRIMARY_instance": dict(strat["instance"]),
            "faulted_secondary": {s: dict(v) for s, v in strat.items() if s != "instance"},
            "clean_control": {"correct": c_ok, "n": c_n, "false_positives": c_n - c_ok},
            "served": len(rows),
            "excluded_out_of_sample": excluded_total[arm],
        }
    paired = [i for i in per_item if "brain" in per_item[i] and "placebo" in per_item[i]]
    b = [i for i in paired if per_item[i]["brain"] and not per_item[i]["placebo"]]
    c = [i for i in paired if per_item[i]["placebo"] and not per_item[i]["brain"]]
    out = {
        "bank": "bank10k", "model": MODEL,
        "primary_contrast": ("brain vs placebo on the INSTANCE stratum only - the only contrast that "
                             "identifies content value, on the only items where a miss is unambiguous"),
        "per_arm": per_arm,
        "primary": {
            "stratum": "instance",
            "n_paired": len(paired),
            "brain_correct": sum(per_item[i]["brain"] for i in paired),
            "placebo_correct": sum(per_item[i]["placebo"] for i in paired),
            "discordant_brain_right": len(b), "discordant_placebo_right": len(c),
            "mcnemar_exact_two_sided_p": mcnemar_exact_two_sided(len(b), len(c)) if paired else None,
            "max_detectable_effect": len(paired) - sum(per_item[i]["placebo"] for i in paired),
        },
    }
    dump_atomic(os.path.join(HERE, "results", "THREE_ARM.json"), out)
    print(json.dumps(out, indent=1))


def cmd_screen(args):
    """Difficulty screen: which served items does the placebo arm actually get WRONG?

    An item the placebo arm answers correctly has no headroom - no arm can beat it, so it costs
    three calls and cannot move the contrast. The screened set is the items placebo missed.

    Measured on the analytical bank first: placebo scored 79% on the faulted half, leaving only 15
    of 71 items with headroom. That is why screening comes BEFORE spending on brain and none, and
    why a big bank is needed to yield a decently-sized screened set.

    Reported per the axes this bank was designed on - family, domain, mechanism, fault position,
    and ambiguity stratum - so a ceiling living in one cell is visible instead of averaged away.
    """
    _, keys = load_bank()
    rows = {}
    for p in glob.glob(os.path.join(RUN, "verdicts", "placebo", "*.json")):
        r = json.load(open(p, encoding="utf-8"))
        rows[r["item_id"]] = r["answer"]
    if not rows:
        sys.exit("no placebo verdicts yet - serve --arm placebo first")

    missed, hit, by = [], [], {}
    for iid, a in rows.items():
        k = keys[iid]
        if k.get("truth") != "flawed":      # clean twins are the FP control, not screen material
            continue
        ok = False
        if norm(a.get("verdict")) == "flawed":
            try:
                ok = int(a.get("fault_step")) == k["fault_step"]
            except (TypeError, ValueError):
                ok = False
        (hit if ok else missed).append(iid)
        for axis, val in (("family", k["family_id"]), ("domain", k["domain"]),
                          ("mechanism", k["mechanism"]),
                          ("position", k["fault_position_band"]),
                          # The axis the analytical bank MEASURED as discriminating: a 30-point
                          # spread against 13-15 for domain and fault family.
                          ("quantifier", k.get("quantifier_regime", "unlabelled")),
                          ("stratum", k.get("ambiguity_stratum", "instance"))):
            d = by.setdefault(axis, {}).setdefault(val, [0, 0])
            d[0] += 1
            d[1] += int(ok)

    n = len(hit) + len(missed)
    print(f"placebo on the faulted half: {len(hit)}/{n} full credit "
          f"({len(missed)} items with headroom)")
    for axis in ("quantifier", "stratum", "position", "mechanism", "domain", "family"):
        print(f"\n  by {axis}:")
        for val, (tot, ok) in sorted(by.get(axis, {}).items()):
            band = "CEILING" if tot and ok == tot else ("floor" if ok == 0 else "")
            print(f"    {str(val):36s} {ok:4d}/{tot:4d}  {band}")
    dump_atomic(os.path.join(HERE, "results", "SCREEN.json"),
                {"arm": "placebo", "n_faulted_served": n, "full_credit": len(hit),
                 "headroom_items": sorted(missed), "by_stratum": by,
                 "caveat": "headroom is measured AT THIS SOLVER STRENGTH UNDER THIS BRIEF; the "
                           "2026-08-10 round showed difficulty does not transport across briefs, "
                           "so any result from this set must name both"})
    print(f"\nscreened set -> results/SCREEN.json ({len(missed)} items with headroom)")


def cmd_status(args):
    items, keys = load_bank()
    t = collections.Counter(k.get("truth") for k in keys.values())
    print(f"bank: {len(items)} items ({t['flawed']} faulted, {t['clean']} clean controls)")
    p = os.path.join(RUN, "SAMPLE.json")
    if os.path.exists(p):
        s = json.load(open(p, encoding="utf-8"))
        print(f"frozen sample: {s['n_faulted']} faulted + {s['n_clean']} clean, "
              f"{s['cells_covered']} cells, seed {s['seed']}")
        print(f"  {s['cost_note']}")
    else:
        print("frozen sample: NONE - run `sample --n N`")
    for f in ("brain_notes.json", "placebo_notes.json"):
        print(f"  {f}: {'present' if os.path.exists(os.path.join(RUN,f)) else 'ABSENT'}")
    for arm in ARMS:
        n = len(glob.glob(os.path.join(RUN, "verdicts", arm, "*.json")))
        print(f"  arm {arm:8s}: {n} served")


STALL_MINUTES = 15


def _proc_age_minutes(pid):
    """How long has THIS process been alive? None if it cannot be read.

    Used to cap the silence attributed to an arm: a process cannot be blamed for a gap that
    predates its own start. Read-only.
    """
    # Subtract INSIDE PowerShell and return a number. The first version asked for `.CreationDate`
    # and parsed the string in Python against a list of formats; on this machine none of them
    # matched and the function silently returned None for every live process - so the stall cap it
    # feeds was inert while looking installed. A locale-dependent datetime string is a parsing
    # problem nobody needs; a float of minutes has no format.
    q = (f"$p = Get-CimInstance Win32_Process -Filter \"ProcessId={int(pid)}\"; "
         f"if ($p) {{ ((Get-Date) - $p.CreationDate).TotalMinutes }}")
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command", q],
                           capture_output=True, text=True, timeout=60)
        s = (r.stdout or "").strip()
        return max(0.0, float(s)) if s else None
    except (ValueError, OSError, subprocess.SubprocessError):
        return None


def _call_child_state(pid):
    """Is a model call actually running under this arm, or is the process idle between verdicts?

    OBSERVE ONLY - this returns a string and touches nothing. The arm blocks on a
    `cmd.exe -> claude.exe` subprocess for the length of each call, so the presence of a live
    DESCENDANT is the difference between "waiting on the model" and "alive with nothing running".
    Neither the PID nor the newest verdict's mtime can see it, and the serve log cannot either -
    stdout is buffered through the `cmd /c` redirect, so a working arm can leave its log untouched
    for ten minutes.

    NAME THE MODEL PROCESS, do not merely count descendants. The first version of this asked
    whether any grandchild existed, and the negative control killed it: on Windows every console
    process is handed a `conhost.exe` child, so a process doing nothing at all reported a live
    descendant. Counting descendants would have reported `conhost.exe` as a model call and called a
    dead arm healthy - the precise failure this function exists to catch. So walk the whole
    descendant tree and look for the model binary BY NAME.
    """
    q = ("Get-CimInstance Win32_Process | Select-Object ProcessId,ParentProcessId,Name | "
         "ConvertTo-Json -Compress")
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command", q],
                           capture_output=True, text=True, timeout=60)
        rows = json.loads(r.stdout or "[]")
    except Exception:
        return "child state unknown"
    if isinstance(rows, dict):
        rows = [rows]
    by_parent = {}
    for x in rows:
        by_parent.setdefault(x.get("ParentProcessId"), []).append(x)
    # Breadth-first over descendants, depth-capped so a PID-reuse cycle cannot spin forever.
    seen, frontier, found = {pid}, [pid], []
    for _ in range(6):
        nxt = []
        for p in frontier:
            for ch in by_parent.get(p, []):
                cid = ch.get("ProcessId")
                if cid in seen:
                    continue
                seen.add(cid)
                nxt.append(cid)
                name = (ch.get("Name") or "").lower()
                if name in ("claude.exe", "node.exe"):
                    found.append(ch.get("Name"))
        if not nxt:
            break
        frontier = nxt
    if found:
        return "in a model call (" + ",".join(sorted(set(found))) + ")"
    # conhost and the cmd shim are NOT evidence of work; say so rather than counting them.
    others = sorted({(x.get("Name") or "?") for x in rows if x.get("ProcessId") in seen - {pid}})
    if others:
        return "NO model process - only " + ",".join(others[:3])
    return "NO CHILD - idle between calls, or hung"


def _serve_pids(arm):
    """PIDs actually running THIS arm's serve.

    Matched narrowly on purpose. A substring test on a command line also matches any OBSERVER that
    merely MENTIONS the string - including the PowerShell query below, whose own command line
    contains 'run_bank10k.py serve'. So require python.exe AND the script operand AND this arm's
    flag. A weak match here would report a healthy arm because the watcher saw itself.
    """
    q = ("Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'python.exe' } | "
         "Select-Object ProcessId,CommandLine | ConvertTo-Json -Compress")
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command", q],
                           capture_output=True, text=True, timeout=60)
        rows = json.loads(r.stdout or "[]")
    except Exception:
        return []
    if isinstance(rows, dict):
        rows = [rows]
    out = []
    for row in rows:
        cl = row.get("CommandLine") or ""
        # STRUCTURE, not substring. The first OPERAND after the interpreter must be the script.
        # A `python -c "... run_bank10k.py serve --arm placebo ..."` process carries that text in
        # its argv and matched the old `-like` test - my own decoy check caught the real arm AND
        # the test harness that merely quoted the string. Anchoring on the operand rejects it,
        # because for `-c` the first operand is `-c`.
        m = re.match(r'^\s*(?:"[^"]*"|\S+)\s+(\S+)\s+(\S+)', cl)
        if not m:
            continue
        script, verb = m.group(1).strip('"'), m.group(2)
        if not script.endswith("run_bank10k.py") or verb != "serve":
            continue
        if not re.search(r"--arm\s+" + re.escape(arm) + r"(\s|$)", cl):
            continue
        try:
            out.append(int(row["ProcessId"]))
        except (KeyError, TypeError, ValueError):
            continue
    return out


def cmd_health(args):
    """Is each arm WORKING, or alive and stalled? A served COUNT alone cannot tell you.

    THE LOSS THIS EXISTS FOR. On 2026-08-17 both arms stopped producing at 07:30 and were still
    alive at 16:59 - nine and a half hours, zero verdicts, a live sub-invocation the whole time.
    Every check run that morning was a PID check and the PID was alive. The one state a process
    check cannot distinguish from working is WAITING FOREVER. Only the served count measured
    against elapsed time shows it, and `status` printed the count with no clock beside it.

    This command OBSERVES ONLY. It never kills, restarts or throttles anything: a watcher that can
    act is a doctor, and an aggressive one becomes the outage it was meant to prevent. It exits 1
    when an arm looks stalled so a caller can decide, and prints what it saw either way.
    """
    now = time.time()
    sample_n, sample_ids = None, None
    p = os.path.join(RUN, "SAMPLE.json")
    if os.path.exists(p):
        sample_ids = set(json.load(open(p, encoding="utf-8"))["item_ids"])
        sample_n = len(sample_ids)
    stalled = []
    for arm in ARMS:
        paths = glob.glob(os.path.join(RUN, "verdicts", arm, "*.json"))
        # COUNT COVERAGE OF THE SAMPLE, NOT FILES. This counted files, so a verdict left over from
        # an earlier sample was counted toward this one: on 2026-08-17 it reported brain 148/150
        # while only 147 sampled items had verdicts, and reported the `none` arm at 2 when BOTH of
        # its files were out-of-sample and its real coverage was 0. An observer that overstates
        # progress is how a run gets called finished two items early.
        if sample_ids is not None:
            in_sample = [q for q in paths
                         if os.path.basename(q)[:-5] in sample_ids]
            orphans = len(paths) - len(in_sample)
            paths, n = in_sample, len(in_sample)
        else:
            orphans, n = 0, len(paths)
        pids = _serve_pids(arm)
        # Clamp at zero: a file written microseconds ago can carry an mtime a hair AHEAD of
        # time.time() at this filesystem's granularity, and "-0.1 min ago" reads as a broken
        # observer. Clamping is display honesty only - it does NOT rescue a genuinely future-dated
        # mtime, which would understate the age and could mask a stall.
        age_min = max(0.0, (now - max(os.path.getmtime(q) for q in paths)) / 60.0) if paths else None
        # SILENCE IS ONLY EVIDENCE AGAINST THE PROCESS THAT WAS ALIVE FOR IT. Measured 2026-08-18
        # 01:26: all three arms were restarted after a crash and this reported "ALIVE BUT STALLED,
        # no verdict for 81 min" two minutes later - because the newest verdict predated the crash
        # and the age was taken against the wall clock rather than against the process. A false
        # stall is not a harmless false alarm: it is precisely what would justify restarting a
        # healthy arm, and a watcher that restarts healthy workers becomes the outage. So cap the
        # silence at the age of the process actually being judged.
        proc_age_min = _proc_age_minutes(pids[0]) if pids else None
        if age_min is not None and proc_age_min is not None:
            age_min = min(age_min, proc_age_min)
        target = f"/{sample_n}" if sample_n else ""
        if sample_n and n >= sample_n:
            state = "COMPLETE"
        elif not pids:
            state = "not running"
        elif age_min is None:
            state = f"starting (pid {pids[0]}, nothing written yet)"
        elif age_min > STALL_MINUTES:
            state = f"*** ALIVE BUT STALLED *** pid {pids[0]} up, no verdict for {age_min:.0f} min"
            stalled.append(arm)
        else:
            state = f"working (pid {pids[0]}, last verdict {age_min:.1f} min ago)"
        # IS THERE A LIVE MODEL CALL UNDER IT? The three states above are read off the PID and the
        # newest verdict's mtime, and neither can see the one thing that matters between verdicts:
        # whether a sub-invocation is actually running. Measured 2026-08-17 23:35 - the `none` arm
        # had restarted 4 minutes earlier, its log was 10 minutes stale (stdout is buffered through
        # the cmd /c redirect, so log silence proves nothing), and its newest verdict predated the
        # restart. It read as "working" on a PID and as suspect on the clock, and it was neither:
        # a cmd.exe -> claude.exe child was mid-call the whole time. Descendant presence is the
        # signal below the PID, and it separates "in a call" from "hung with nothing running".
        state += f"   [{_call_child_state(pids[0])}]" if pids else ""
        print(f"  {arm:8s} {n}{target:>6s}  {state}")
    if stalled:
        print(f"STALLED: {', '.join(stalled)} - alive but not producing for over {STALL_MINUTES} min.")
        print("Not touching them. Check the newest sub-invocation's age before restarting.")
        return 1
    print("no arm is alive-and-silent.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sample"); s.add_argument("--n", type=int, default=300)
    s.set_defaults(fn=cmd_sample)
    sub.add_parser("notes").set_defaults(fn=cmd_notes)
    v = sub.add_parser("serve"); v.add_argument("--arm", required=True, choices=ARMS)
    v.add_argument("--limit", type=int, default=0)
    v.add_argument("--concurrency", type=int, default=1,
                   help="parallel model calls per arm; 1 = unchanged behaviour, 3 = measured optimum")
    v.set_defaults(fn=cmd_serve)
    sub.add_parser("grade").set_defaults(fn=cmd_grade)
    sub.add_parser("screen").set_defaults(fn=cmd_screen)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    sub.add_parser("health").set_defaults(fn=cmd_health)
    a = ap.parse_args()
    # Propagate an int return as the exit code - `health` returns 1 when an arm is alive but
    # silent, and a caller that cannot see that has the same blind spot the command exists to fix.
    rc = a.fn(a)
    sys.exit(rc if isinstance(rc, int) else 0)


if __name__ == "__main__":
    main()
