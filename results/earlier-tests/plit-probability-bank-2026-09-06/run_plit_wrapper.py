# -*- coding: utf-8 -*-
"""run_plit_wrapper.py - the probability-literature bank (plit_v1) on the inherited sterile runner.

Same machinery as the B12/B13 wrappers (run_bank10k.py: fingerprint guards, sterile serving, served-model
census, transcript receipts, per-item resume) with the paths, seed and sampler fixed by PROTOCOL_PLIT.md:
items/plit.jsonl, keys in <HOME>/bank_plit_keys_quarantine/, every artifact under run_plit/ (or the
directory PLIT_RUN_DIR names), the solver from BANK_MODEL, and NO TOOLS for the solver (an audit must come from
reading the argument, never from a shell).

    set BANK_MODEL=claude-opus-5
    python run_plit_wrapper.py sample --n 80 [--stage 0]      # pilot: 60 flawed + 20 clean, stratified by operator
    python plit_notes_bm25.py --run run_plit                  # brain + placebo notes
    python run_plit_wrapper.py serve --arm none --concurrency 1
    python grade_plit.py --run run_plit
"""
import collections
import glob
import hashlib
import io
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK10K = os.path.join(os.path.expanduser("~"), "ai-memories-and-functionality", "06_math_research",
                       "probability_open_problem_campaign_2026_08_09", "eval", "bank10k")
sys.path.insert(0, BANK10K)
import run_bank10k as rb  # noqa: E402

RUN_PLIT = os.path.join(HERE, os.environ.get("PLIT_RUN_DIR") or "run_plit")
os.makedirs(RUN_PLIT, exist_ok=True)
rb.RUN = RUN_PLIT
# 13:1x: PLIT_ITEMS / PLIT_KEYS override the bank files for a SEPARATE run (the Codex reviewer's four reserved
# calibration items live in its private dir); the sealed bank's files are the default and are never rewritten here.
rb.ITEMS = os.environ.get("PLIT_ITEMS") or os.path.join(HERE, "items", "plit.jsonl")
rb.KEYS = os.environ.get("PLIT_KEYS") or r"<HOME>\bank_plit_keys_quarantine\plit_keys.jsonl"
rb.SEED = 20260906

# no tools for the solver (PROTOCOL_PLIT.md): sterile settings AND an empty tool list; effort HIGH on every solver
# call (order 10:2x 2026-09-06: every Claude agent and subagent runs at high effort; amendment 1 of the protocol)
_orig_sterile = rb._sterile_args
EFFORT = os.environ.get("PLIT_EFFORT", "high")


# 2026-09-06 11:1x: NO MCP SERVERS. Measured on this machine at 97 pct CPU (12 agents + renders): without
# --strict-mcp-config the CLI spent its whole 300 s probe budget starting the claude.ai connector servers
# (debug log: 42 s to reach "Loading MCP configs", then silence) - 0 of 5 probes returned; with an empty
# strict MCP config the same probe returned in 13 s and 52 s (API 2.2 s / 26.5 s). The solver never had
# tools anyway (--tools ""), so this only removes the startup hang; it is strictly MORE sterile.
EMPTY_MCP = os.path.join(HERE, "empty_mcp.json")


def _sterile_no_tools():
    return list(_orig_sterile()) + ["--tools", "", "--effort", EFFORT,
                                    "--strict-mcp-config", "--mcp-config", EMPTY_MCP]


rb._sterile_args = _sterile_no_tools
# 2026-09-06 11:3x: Opus at high effort needs more than the runner's 600 s per call and 300 s per probe on this loaded
# machine (its probe alone took 196 s; the serve's own 300 s transport check then timed out and refused). A timeout is
# still an error, never a verdict; the item is simply redone later.
rb.CALL_TIMEOUT_S = int(os.environ.get("PLIT_CALL_TIMEOUT_S", "1200"))
# 2026-09-06 12:2x: the solver claude.exe is spawned at NORMAL priority. The serve runs BelowNormal (doctrine) and a
# Windows child inherits BelowNormal, so on this 97 pct-CPU machine the node process STARVED at startup: live children
# showed 1-2 CPU-seconds after four minutes and the 11:39 transport check timed out at 540 s, while the same probe
# from a Normal-priority shell returned in 5-30 s (five concurrent: 8/8/8/11/30 s). The CLI needs a few CPU-seconds
# per call and then waits on the network; that is a latency-sensitive client, not background compute.
import subprocess as _sp
import types as _types


# 12:3x: the InteractiveAgentResourceGuard (compute_governor/interactive_guard/guard.py) re-demotes every
# claude.exe to BelowNormal on its sweep AND pins every AI process to LPs 4-9 + 14-15, where 4-9 run at 100 pct;
# measured 12:3x: LP 14 at 4 pct, LP 15 at 80 pct, the reserve LPs 0-3/10-13 at 37-74 pct. The guard preserves a
# NARROWER background cap (desired_affinity keeps old & background), so the sanctioned move (memory
# idle_lps_inside_the_ai_mask_are_capacity_pin_lanes_there_2026_09_06) is to pin the solver children to the idle
# LPs inside the mask. PLIT_SOLVER_LPS overrides (comma list); empty disables the pin.
_SOLVER_LPS = [int(x) for x in os.environ.get("PLIT_SOLVER_LPS", "14,15").split(",") if x.strip()]


class _NormalPrioPopen:
    """Deferred spawn: the child is created at communicate(), with the prompt ALREADY on its stdin as a file.

    12:4x: the CLI reads stdin for only 3 s after it starts ("Warning: no stdin data received in 3s ... Error:
    Input must be provided") and the BelowNormal python parent, descheduled on the saturated LPs, took longer than
    that between Popen and communicate(prompt) - the Opus probe failed with exactly that text at 12:45:35. Writing
    the prompt to a temp file and handing the file to the child at creation removes the race: the data is there
    before the child's first instruction runs. Everything the runner touches (pid, returncode, communicate, wait,
    kill) is delegated to the real process once it exists."""

    def __init__(self, *a, **kw):
        self._a, self._kw, self._real, self._tmp = a, dict(kw), None, None

    def _spawn(self, input_text):
        import tempfile
        kw = dict(self._kw)
        # CREATE_NO_WINDOW (never a console) | NORMAL_PRIORITY_CLASS (the monitor's 12:5x ruling: the solver
        # children may run at Normal, nothing else may; the guard may still lower them and is not fought)
        kw["creationflags"] = kw.get("creationflags", 0) | 0x08000000 | 0x00000020
        if kw.get("stdin") is _sp.PIPE:
            if input_text is not None:
                fd, self._tmp = tempfile.mkstemp(prefix="plit_prompt_", suffix=".txt")
                with os.fdopen(fd, "w", encoding="utf-8") as fh:
                    fh.write(input_text)
                kw["stdin"] = open(self._tmp, "rb")
            else:
                kw["stdin"] = _sp.DEVNULL
        self._real = _sp.Popen(*self._a, **kw)
        if kw.get("stdin") not in (_sp.PIPE, _sp.DEVNULL, None):
            kw["stdin"].close()
        if _SOLVER_LPS:
            try:
                import psutil
                psutil.Process(self._real.pid).cpu_affinity(_SOLVER_LPS)
            except Exception as e:   # never let a pin failure cost a verdict
                print(f"  [affinity] pin to {_SOLVER_LPS} failed: {e.__class__.__name__}: {e}", flush=True)
        return self._real

    def communicate(self, input=None, timeout=None):
        if self._real is None:
            self._spawn(input)
            input = None
        try:
            return self._real.communicate(None, timeout=timeout)
        finally:
            if self._real.poll() is not None and self._tmp:
                try:
                    os.unlink(self._tmp)
                except OSError:
                    pass
                self._tmp = None

    @property
    def pid(self):
        return self._real.pid if self._real is not None else None

    def __getattr__(self, name):
        if self._real is None:
            raise AttributeError(name)
        return getattr(self._real, name)


_shim = _types.SimpleNamespace(**{k: getattr(_sp, k) for k in dir(_sp) if not k.startswith("__")})
_shim.Popen = _NormalPrioPopen
rb.subprocess = _shim
rb.PROBE_TIMEOUT_S = int(os.environ.get("PLIT_PROBE_TIMEOUT_S", "540"))
os.environ["CLAUDE_CODE_EFFORT_LEVEL"] = EFFORT

# keep every grade artifact under run_plit/ (the inherited cmd_grade writes to bank10k/results/)
_dump_atomic_orig = rb.dump_atomic
_shared_results = os.path.join(BANK10K, "results")


def _dump_atomic_redirected(path, obj):
    if os.path.abspath(os.path.dirname(path)) == os.path.abspath(_shared_results):
        os.makedirs(os.path.join(RUN_PLIT, "results"), exist_ok=True)
        path = os.path.join(RUN_PLIT, "results", os.path.basename(path))
    return _dump_atomic_orig(path, obj)


rb.dump_atomic = _dump_atomic_redirected


def served_anywhere():
    """Ids a later sample must never draw: every verdict file in any run_plit* AND every id frozen in a run_plit*
    SAMPLE.json (13:2x: an item sampled for the pilot but not yet served by a slow arm was drawable before)."""
    ids = set()
    for f in glob.glob(os.path.join(HERE, "run_plit*", "verdicts", "*", "*.json")):
        ids.add(os.path.basename(f)[:-5])
    for f in glob.glob(os.path.join(HERE, "run_plit*", "SAMPLE.json")):
        try:
            ids |= set(json.load(io.open(f, encoding="utf-8")).get("item_ids", []))
        except Exception:
            pass
    return ids


def cmd_sample_plit(args):
    """PROTOCOL_PLIT.md sampler: flawed items stratified over operators (floor per operator, then proportional),
    clean items at the requested share, never-served items only, seeded by stage."""
    items, keys = rb.load_bank()
    exclude = served_anywhere()
    # 2026-09-06 11:4x: post-seal defects (DEFECTS.json) and the Codex reviewer's reserved calibration papers are
    # never sampled again; the bank itself is monotonic so the exclusion lives here, at the sampler.
    dpath = os.path.join(HERE, "DEFECTS.json")
    if os.path.exists(dpath) and not os.environ.get("PLIT_NO_DEFECTS"):   # PLIT_NO_DEFECTS=1 only for the reserved-paper calibration run
        d = json.load(open(dpath, encoding="utf-8"))
        exclude |= {x["item_id"] for x in d.get("items", [])}
        reserved = set(d.get("reserved_calibration_papers", []))
        exclude |= {i for i in items if keys[i].get("paper") in reserved}
    elig = [i for i in items if i not in exclude]
    flawed = sorted(i for i in elig if keys[i].get("truth") == "flawed")
    clean = sorted(i for i in elig if keys[i].get("truth") == "clean")
    n_clean = max(1, round(args.n * args.clean_share))
    n_flawed = args.n - n_clean
    rng = random.Random(rb.SEED + int(args.stage or 0))
    by_op = collections.defaultdict(list)
    for i in flawed:
        by_op[keys[i]["family_id"]].append(i)
    total = sum(len(v) for v in by_op.values())
    picked = []
    for o in sorted(by_op):
        pool = sorted(by_op[o])
        picked += rng.sample(pool, min(args.floor, len(pool)))
    quota = {o: max(0, round((n_flawed - len(picked)) * len(by_op[o]) / total)) for o in by_op}
    for o in sorted(by_op):
        rest = sorted(set(by_op[o]) - set(picked))
        picked += rng.sample(rest, min(quota[o], len(rest)))
    rest = sorted(set(flawed) - set(picked))
    if len(picked) < n_flawed and rest:
        picked += rng.sample(rest, min(n_flawed - len(picked), len(rest)))
    picked = picked[:n_flawed]
    picked_clean = rng.sample(clean, min(n_clean, len(clean)))
    sample = {
        "seed": rb.SEED + int(args.stage or 0), "stage": int(args.stage or 0),
        "protocol": "PROTOCOL_PLIT.md",
        "excluded_served_ids": len(exclude),
        "bank_fingerprint": rb.bank_fingerprint(items),
        "sampled_text_hash": rb.sampled_text_hash(items, sorted(picked) + sorted(picked_clean)),
        "requested": args.n, "n_faulted": len(picked), "n_clean": len(picked_clean),
        "n_faulted_by_operator": dict(collections.Counter(keys[i]["family_id"] for i in picked)),
        "n_faulted_by_tier": dict(collections.Counter(keys[i]["tier"] for i in picked)),
        "n_faulted_by_ext_refs": dict(collections.Counter(keys[i]["external_refs"] for i in picked)),
        "n_primary_metric_items": len(picked),
        "cost_note": "three arms x %d items; %s sterile serves, no tools" % (len(picked) + len(picked_clean), os.environ.get("BANK_MODEL", rb.MODEL)),
        "item_ids": sorted(picked) + sorted(picked_clean),
    }
    rb.dump_atomic(os.path.join(rb.RUN, "SAMPLE.json"), sample)
    print(json.dumps({k: v for k, v in sample.items() if k != "item_ids"}, indent=1))
    print("frozen to", os.path.join(rb.RUN, "SAMPLE.json"))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        import argparse
        ap = argparse.ArgumentParser()
        ap.add_argument("sample")
        ap.add_argument("--n", type=int, default=80)
        ap.add_argument("--stage", type=int, default=0)
        ap.add_argument("--clean-share", type=float, default=0.25)
        ap.add_argument("--floor", type=int, default=3)
        cmd_sample_plit(ap.parse_args())
    else:
        rb.main()
