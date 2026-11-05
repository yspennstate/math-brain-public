#!/usr/bin/env python3
"""math_transport.py - carry a landed mathematical result from the main brain into the math store.

WHY THIS EXISTS. The main memory corpus and the math store (math-brain-build/local/population/brain.sqlite3)
are different objects with different readers. A theorem written as a memory is invisible to the math hook
(math_sense.py) until it is in the store as a claim. Typing each result into the store by hand works for a few
days and then lapses: a result lands as a memory, nobody carries it, and the hook goes on serving the older
state. This module is the automatic transport.

WHAT IT DOES. Every run it reads every memory's description, sorts each into three tiers, and acts:

    AUTO   an unambiguous mathematical result - a result word (THEOREM / PROVED / SETTLED / REFUTED / EXACT /
           COUNTEREXAMPLE ...) at the head of the description, or a named problem followed by a result verb
           ("Aldous-Fill Open Problem 4.48 settled", "the FEI constant is numerically ..."), with a
           mathematical vocabulary signal and NO word from the hard deny list. Ingested as a claim + node + evidence +
           provenance row, status UNVERIFIED (the store requires it; the memory's own status rides in the
           provenance row and the evidence limitations, which is where a reader must look).
    QUEUE  a probable result the rule cannot settle on its own (a soft word such as "grid", "delta",
           "beta", "session" that lives in both worlds). Written to math_transport_queue.jsonl for an agent
           to ingest (python math_transport.py ingest <slug>) or dismiss (dismiss <slug> "<why>"). A queue
           item older than QUEUE_STALE_H trips hook_liveness - the transport never silently lapses again.
    SKIP   everything else. The hard deny list (math_transport_deny.json, local, empty by default) wins over every
           result word: the words of a domain whose own "theorems" (a counting rule of a business, a budget
           identity) are the exact things a loose rule would carry across. Process notes (a film about a
           theorem, a release note) are denied the same way by a built-in list.

IDEMPOTENT by the claim_provenance.source_ref = "memory:<slug>" row, plus
the local ledger; a slug is never ingested twice. The store is backed up before the first write of a day.
The prefilter index (<store>.prefilter.pkl) is rebuilt IN-PROCESS after an ingest: a claim absent from the
prefilter is invisible to the hook, and a subprocess under the windowless launcher would pop a console.

WHAT IT DOES NOT DO. It does not type a theorem. The claim statement is the memory's description, prose,
kind guessed from its result words. That makes the result SERVABLE the hour it lands; the typed statement
with assumptions is a refinement an agent adds later (a new claim with a SUPERSEDES edge). Stated in every
transported claim's evidence limitations so no reader mistakes prose for a verified typed theorem.

REVISIONS. A research program keeps ONE memory and grows it in place (a program's state memory has its description
rewritten as results land), and "a slug is never ingested twice" would freeze each such claim at its first
description: the store's frontier stops while the memory keeps gaining theorems. So a transported memory whose description has CHANGED since it was carried is now
revised: a new claim with the new statement that SUPERSEDES the old one (the hook and the frontier digest follow
supersession to the head). Only when the description GREW and still classifies AUTO is that automatic - a program
adding results. A description that shrank is usually a rewrite into a shorter summary ("the paper was audited and
published") that would replace a theorem statement with news about it, so it goes on the queue for an agent:
`revise <slug>` carries it, `dismiss-revision <slug> <why>` keeps the old claim for that description (a later
change queues again). Typed refinements (source_kind campaign) are never revised by this rule, and a claim an
agent has already superseded is left to that agent's head.

Usage:
    python math_transport.py scan                 dry run: AUTO / QUEUE / SKIP counts and lists, nothing written
    python math_transport.py run [--dry]          ingest the AUTO tier, queue the rest, rebuild the prefilter
    python math_transport.py ingest <slug>        ingest one slug now (an agent's verdict on a queued item)
    python math_transport.py ingest-many <file>   ingest a file of slugs under one lock, one prefilter rebuild at the end
    python math_transport.py dismiss <slug> <why> take a slug out of the queue without ingesting it
    python math_transport.py revisions            dry list: transported memories whose description changed since
    python math_transport.py revise <slug>        carry a changed description now (new claim SUPERSEDES the old)
    python math_transport.py dismiss-revision <slug> <why>   keep the old claim for this description
    python math_transport.py status               one line for hook_liveness; exit 1 when stale
    python math_transport.py provrows             provisional frontier-row memories outside the store (none queue)
    python math_transport.py rowlist              write the frontier row ids from MATH_TRANSPORT_ROWS_REPO (gh api)
    python math_transport.py selftest             controls both ways; end-to-end ingest on a scratch store

Paths: BRAIN_MEMORY_DIR (or BRAIN_MEM_DIR) is the memory folder, by default the Claude Code project folder of the home
directory; MATHBRAIN_STORE is the store; MATHBRAIN_SRC is the folder holding the math_brain package.
Fails closed: any exception in a write aborts that slug and is recorded in the ledger.
"""
import contextlib, difflib, io, json, os, re, shutil, sqlite3, sys, time, glob

HERE = os.path.dirname(os.path.abspath(__file__))
_HOME = os.path.expanduser("~")


def _brain_slug():
    """The Claude Code project name of the corpus: $BRAIN_SLUG, then a BRAIN_SLUG file beside this one (the installer
    writes it), then the home path with ':' and the separators replaced by '-', as brain.py resolves it."""
    env = os.environ.get("BRAIN_SLUG", "").strip()
    if env:
        return env
    try:
        with io.open(os.path.join(HERE, "BRAIN_SLUG"), encoding="utf-8") as fh:
            named = fh.read().strip()
        if named:
            return named
    except OSError:
        pass
    return _HOME.replace(":", "-").replace(chr(92), "-").replace("/", "-")


def _first_dir(*cands):
    for c in cands:
        if c and os.path.isdir(c):
            return c
    return cands[-1]


MEM = (os.environ.get("BRAIN_MEMORY_DIR") or os.environ.get("BRAIN_MEM_DIR")
       or os.path.join(_HOME, ".claude", "projects", _brain_slug(), "memory"))
STORE = os.environ.get("MATHBRAIN_STORE") or os.path.join(_HOME, "math-brain-build", "local", "population", "brain.sqlite3")
BUILD_SRC = os.environ.get("MATHBRAIN_SRC") or _first_dir(os.path.join(HERE, "..", "mathbrain", "src"),
                                                         os.path.join(_HOME, "math-brain-build", "src"))
LEDGER = os.path.join(HERE, "math_transport_ledger.jsonl")
QUEUE = os.path.join(HERE, "math_transport_queue.jsonl")
STATE = os.path.join(HERE, "math_transport_state.json")
QUEUE_STALE_H = 48.0       # a queued result nobody has looked at for two days trips hook_liveness
RUN_STALE_H = 2.0          # the 15-minute task has not run for two hours -> the transport itself is dead
# A STUDY CAN HOLD THE STORE. A brain on/off round needs every arm to meet one store, and the transport is
# the one writer that runs on its own clock. `hold <until> <agent> <why>` writes this file; while it is in force a run
# writes nothing - no ingest, no revision, no queue row, no state - so the next run after it ends reads the whole
# held window again (the incremental window reaches back 48 h). status() reports the hold instead of a stale run.
HOLD = os.path.join(HERE, "math_transport_HOLD.json")
HOLD_MAX_H = 24.0          # a hold longer than a day is a forgotten hold: it lapses and status says so


def hold_state(now=None):
    """(in_force, info or None). A hold past its time, unreadable, or longer than HOLD_MAX_H is not in force."""
    now = time.time() if now is None else now
    try:
        h = json.load(io.open(HOLD, encoding="utf-8"))
        until = time.mktime(time.strptime(h["until"][:19], "%Y-%m-%dT%H:%M:%S"))
        set_at = float(h.get("set_epoch") or now)
    except Exception:
        return False, None
    if until <= now or until - set_at > HOLD_MAX_H * 3600:
        return False, h
    return True, h


# A HOLD SET WHILE A RUN IS UNDER WAY STOPS THAT RUN BEFORE ITS NEXT WRITE. A run used to check the hold once, then scanned (a full pass reads every
# memory) and wrote; a hold set during the scan did not stop it. Now every write of a run - one memory's claim with its
# ledger and queue rows, a queue row, the prefilter rebuild, the claim vectors, the state file - happens under WRITE_LOCK
# after the hold is read again, and `hold` writes its file under the same lock. A write therefore either finishes before
# the hold is on disk or sees the hold and does not happen, and a run stopped by a hold writes no state, so the next run
# after it reads the whole window again.
WRITE_LOCK = os.path.join(HERE, "math_transport_write.lock")
LOCK_WAIT_S = 120.0
_MANUAL_GATED = []        # set while a manual ingest/revise/correct runs inside its gate (main re-enters itself once)


class HeldMidRun(Exception):
    """A hold came into force after the run's first check; nothing more may be written."""


@contextlib.contextmanager
def _write_lock(timeout=LOCK_WAIT_S):
    """An exclusive OS lock on WRITE_LOCK, released when the block ends or the process dies."""
    fd = os.open(WRITE_LOCK, os.O_RDWR | os.O_CREAT, 0o644)
    t_end = time.time() + timeout
    locked = False
    try:
        while True:
            try:
                if os.name == "nt":
                    import msvcrt
                    os.lseek(fd, 0, 0)
                    msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                locked = True
                break
            except OSError:
                if time.time() >= t_end:
                    raise TimeoutError("the transport write lock was busy for %.0f s" % timeout)
                time.sleep(0.05)
        yield
    finally:
        if locked:
            try:
                if os.name == "nt":
                    import msvcrt
                    os.lseek(fd, 0, 0)
                    msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(fd, fcntl.LOCK_UN)
            except OSError:
                pass
        os.close(fd)


@contextlib.contextmanager
def _gated_write():
    """Hold the write lock and read the hold again; raise HeldMidRun when it is in force."""
    with _write_lock():
        held, h = hold_state()
        if held:
            raise HeldMidRun(h)
        yield
TRANSPORT_VERSION = 1

# ---- the rule --------------------------------------------------------------------------------------------
TAG_RX = re.compile(r"^\s*(\[[A-Za-z0-9 +,_/\-]{2,40}\]\s*)+")
LONG_TAG_RX = re.compile(r"^\s*\[[A-Z][A-Za-z\-]+\b[^\[\]]{0,400}\]\s*")
DATE_RX = re.compile(r"^\s*((MEASURED|RESULT|EXACT|RECORD|CORRECTED|VERIFIED|PROVED|SETTLED|GRADED BLIND|DEPLOYED)\s+)?"
                     r"(20\d\d-)?\d\d-\d\d(\s+\d\d?:\d[\dx]{1,2}(-\d\d?:\d[\dx]{1,2})?)?"
                     r"(\s+\(([^)]{0,60})\))?\s*[:\-]?\s*", re.I)
# (RECORD is not a result word: a Python wheel's RECORD file carried two packaging memories into the first scan)
RESULT_MARK = re.compile(r"\b(THEOREM|PROVED|PROVEN|SETTLED|REFUTED|RESULT|EXACT|DISPROOF|DISPROVED|COUNTEREXAMPLE)\b")
NAMED_PROBLEM = re.compile(
    r"\b(Aldous|Fill|Janson|Bradley|Kalai|Rozikov|Khoshnevisan|Leskela|Pollett|Thevenin|Asanjarani|Nazarathy|"
    r"Erdos|Ross'?s|MMPP|Bernoulli|FEI|read-once|Hod|Kemeny|GPS|Ding-Lee-Peres|Lyons|Rado|NAE|Ising|OA\(|MOLS|"
    r"Arnold diffusion|Volterra|Rademacher|Vitali|Frostman|percolation|Ramanujan|perceptron|Krauth|Mezard|"
    r"Open Problem|Conjecture|Question \d|Problem \d|Theorem \d|Lemma \d)\b")
RESULT_VERB = re.compile(
    r"\b(settled|refuted|fails|failed|is false|is true|proved|proven|answered|disproved|holds|is equivalent|"
    r"equivalent to|closed|reduced to|is numerically|lower bound|upper bound|bound was rebuilt|kernel accepted|"
    r"found correct|survives \d+ independent audits|answered in the (negative|affirmative)|counterexample|"
    r"is exactly|is not|does not hold|implies|audited line by line|lean-?checked|zero violations|confirmed|"
    r"reproduced|verified)\b", re.I)
MATH_SIGNAL = re.compile(
    r"\b(theorem|lemma|conjecture|inequality|entropy|influence|markov|graph|walk|mixing|spectral|eigen\w*|matrix|"
    r"kernel|proof|formula|boolean|percolation|random|operator|polynomial|group|algebra|topolog\w*|"
    r"manifold|convergence|integral|prime|combinator\w*|probability|queue|potential|certificate|dyadic|"
    r"interval arithmetic|cover[- ]time|hitting|stationary|ergodic|orthogonal|lattice|fixed point|uniqueness|"
    r"simplex|constants?|coefficients?|variances?|fluctuations?|asymptotic|chains?|clique|gauss\w*|"
    r"t_hit|t_cov|mixing|entropies|gates?|arity|"
    # a head that names its result only by an acronym or a structure ("The best known FEI lower bound is 6.5218")
    # never read as mathematics without these
    r"fei|kkl|quadratic forms?|eigenvalues?|perfect matching|anti-?concentration|bounded density|density bound|"
    r"littlewood-offord|"
    # deep-learning theory results (catapult dynamics, heavy-tailed SGD, label-noise sharpness) write their heads in
    # that field's words
    r"sharpness|hessian|sgd|stochastic gradient|gradient descent|learning rate|tail index|neural tangent|ntk|"
    r"catapult|interpolat\w*|overparameteri[sz]ed|heavy[- ]tailed|single[- ]index|information exponent)\b", re.I)
# Two words of the list above that also live in operations notes, read only in their mathematical sense: the
# Lean prover by its name or a .lean file ("lean workers" and "a lean method" are lowercase), and
# measure unless it is the verb with its object ("a study that measures a change", "measure how ...").
MATH_SIGNAL_NAMED = re.compile(
    r"\b(?:Lean(?: ?4)?|Mathlib|lake build)\b|\.lean\b|"
    r"(?i:\bmeasures?\b(?! (?:a|an|the|how|what|whether|it|its|this|that|these|every|each|his|her|their|our|my|one)\b))")
# DOMAIN DENY LISTS. A memory corpus usually holds some domain of work whose own "theorems" must never be carried into
# the math store as mathematics (a business's counting rules, an engineering budget identity, a game's scoring law).
# Name that domain's words in a LOCAL file, never in this one: MATH_TRANSPORT_DENY names it (default
# math_transport_deny.json beside this file), a JSON object {"hard": "<regex>", "soft": "<regex>"}, read
# case-insensitively over the slug and the first 400 characters. HARD wins over every result word, even when forced;
# SOFT words live in both worlds and send a result to the QUEUE, never AUTO. With no file both lists are empty. A file
# that exists but cannot be read or compiled stops the transport: an unreadable deny list must not read as no list.
DENY_FILE = os.environ.get("MATH_TRANSPORT_DENY") or os.path.join(HERE, "math_transport_deny.json")
NEVER = r"(?!)"


def load_deny(path=None):
    """(HARD_DENY, SOFT_DENY) compiled from the deny file; both match nothing when the file is absent."""
    path = path or DENY_FILE
    if not os.path.exists(path):
        return re.compile(NEVER), re.compile(NEVER)
    try:
        with io.open(path, encoding="utf-8") as f:
            d = json.load(f)
        return re.compile(d.get("hard") or NEVER, re.I), re.compile(d.get("soft") or NEVER, re.I)
    except Exception as exc:
        raise SystemExit("math_transport: the deny file %s cannot be used (%s: %s)" % (path, type(exc).__name__, exc))


HARD_DENY, SOFT_DENY = load_deny()
# NON-MATH deny: a film about a theorem, a packaging lesson, a release note, an intake rule - process records that
# quote a result are not the result. Read over the slug and the head; wins like the hard deny.
NON_MATH_DENY = re.compile(
    r"\b(films?|movies?|render\w*|boards?|narration|youtube|episodes?|scan\w*|wheel|package|privacy|secrets?|"
    r"hooks?|agents?|subagents?|brain|memory|memories|dream\w*|mesh|checklist|prompts?|readout|diffusion iter|"
    r"anneal\w*|release|benchmark session|intake|transcript|voice|thumbnail|upload\w*)\b", re.I)
# QUESTION-FIRST HEADS. A description may open with the question it answers
# ("Does a bounded density ... bound ...? No: a thin shell ..."), so the result word, if any, sits after the "?". The answer's head is now read for the result word
# too, "reduces to" and "establish" count as result verbs beside a named problem, a bare yes/no answer goes to the
# QUEUE, and a head that is only a formula (no word from MATH_SIGNAL) goes to the QUEUE, never AUTO. Machine words
# deny like the process words: a formula-shaped head about a laptop's commit charge is not mathematics.
YESNO_ANSWER = re.compile(r"^(?:\[[A-Z ]+\]\s*)?(Yes|No|Partly|Only partly|Not quite|Mostly)\b\s*[:,.;(\-]", re.I)
EXTRA_RESULT_VERB = re.compile(r"\b(reduces to|establish(?:ed|es)?|is bounded by|holds for)\b", re.I)
FORMULA_HEAD = re.compile(r"[A-Za-z_][\w^]*(?:\([^)]{0,20}\))?\s*(?:<=|>=|=|≤|≥)\s*[\w(\-]")
MACHINE_DENY = re.compile(r"\b(laptop|pid|pagefile|commit charge|working set|nordvpn|\d+(?:\.\d+)?\s?[MG]B)\b", re.I)
CYCLE_LOG = re.compile(r"^\s*(\*|★|Cycles? \d+|CYCLE \d+)")
SKIP_PREFIX = ("job_", "audit_", "gist_", "scar_", "method_", "mistake", "the_dream", "dream_", "owner_", "reference_",
               "project_", "reflex_", "a_no_brain", "the_brain_is", "math_store_stale", "campaign_")
SKIP_HEAD = re.compile(r"^\s*(\[?(FIRE WHEN|MECHANISM|SCAR|NAP GIST|GIST|METHOD|OWNER|RECURRENCE|GRADED BLIND|"
                       r"CORRECTED|CONSOLIDATION|TOOL BUILT|BUILT|FOUND, FIXED|LANDED|DEPLOYED))", re.I)

# PROGRAM GUARD (MATH_TRANSPORT_PROGRAM_GUARD). A verified memory of one of your named research programs can read
# SKIP when its head lacks the result words above ("[MEASURED EXACTLY] ...", "[DERIVED + CHECKED] ...", a yes/no
# past the question), or when its slug and first 400 characters use a program word the denies read as domain or
# process ("attack lanes", "the certificate engine", "the annealed defect identity", "frac(1.5 x)"). Such a memory
# goes to the QUEUE: never AUTO, never past a process-note slug or head, never past a deny word outside
# AMBIGUOUS_DENY. An agent decides each one. The programs are the slug prefixes in MATH_TRANSPORT_PROGRAMS
# (comma-separated, e.g. "fei_,janson_,cover_time_"); none by default.
PROGRAM_GUARD = os.environ.get("MATH_TRANSPORT_PROGRAM_GUARD", "1").strip() not in ("0", "", "off", "false")
PROGRAM_PREFIX = tuple(p.strip() for p in os.environ.get("MATH_TRANSPORT_PROGRAMS", "").split(",") if p.strip())
# a program's ledger ids as a regular expression over the slug (e.g. "^[defp]\\d{4}_"); none by default
PROGRAM_LEDGER_ID = re.compile(os.environ.get("MATH_TRANSPORT_LEDGER_ID_RX") or r"(?!)")
PROGRAM_STATUS = ("verified", "owner-stated")
PROGRAM_VERIFIED_HEAD = re.compile(r"^\s*\[?\s*VERIFIED\b", re.I)
# deny words research programs use in their own sense: attack and referee lanes, a block-chaos engine, an annealed
# defect identity, a simulation inside a refutation, frac(1.5 x), and the loss plateau of a deep-learning result.
AMBIGUOUS_DENY = re.compile(r"^(lanes?|engines?|anneal\w*|sims?|simulations?|plateaus?|\d{1,4}(\.\d+)?x)$", re.I)


# FRONTIER ROWS. A frontier campaign keeps one folder per open problem, rows/T### . Its verified row memories often
# head like "T109 hard-core Z^2: coexistence for lambda > 4.93828", with no result word in the first 70 characters.
# A bare t\d{3}_ would also take other tags (t500_ as some other label), so the row counts only when its folder rows/T###
# exists. The id may also sit inside the slug (label_noise_..._t355_...); the guard only ever QUEUEs.
FRONTIER_ROW_ID = re.compile(r"(?:^|_)t(\d{3})_")
FRONTIER_ROWS = os.environ.get("MATH_TRANSPORT_FRONTIER_ROWS") or os.path.join(HERE, "frontier", "rows")
# A clone without the rows folder can name the rows in a file, one id a line; `rowlist` writes it from a GitHub
# repo's rows tree. A row added since the list was written is unknown until then.
FRONTIER_ROW_LIST = os.environ.get("MATH_TRANSPORT_FRONTIER_ROW_LIST") or os.path.join(HERE, "frontier_row_ids.txt")
_ROW_IDS = None


def frontier_row_known(num):
    """True when rows/T<num> exists, or, without the folder, when the row list names T<num>."""
    global _ROW_IDS
    if os.path.isdir(os.path.join(FRONTIER_ROWS, "T" + num)):
        return True
    if _ROW_IDS is None:
        try:
            with io.open(FRONTIER_ROW_LIST, encoding="utf-8") as f:
                _ROW_IDS = {ln.strip() for ln in f if re.match(r"^T\d{3}$", ln.strip())}
        except OSError:
            _ROW_IDS = set()
    return ("T" + num) in _ROW_IDS


def program_of(slug):
    """The program prefix a slug belongs to, or ''."""
    for pre in PROGRAM_PREFIX:
        if slug.startswith(pre):
            return pre.rstrip("_")
    m = PROGRAM_LEDGER_ID.match(slug)
    if m:
        return m.group(0).rstrip("_")
    m = FRONTIER_ROW_ID.search(slug)
    if m and frontier_row_known(m.group(1)):
        return "t" + m.group(1)
    return ""


def _program_guard(slug, desc, status, reason):
    """True when a SKIP of a verified program memory rests only on a missing marker, missing vocabulary or
    ambiguous deny words."""
    if not program_of(slug):
        return False
    if (status or "").lower() not in PROGRAM_STATUS and not PROGRAM_VERIFIED_HEAD.search(desc or ""):
        return False
    if reason in ("no result marker", "no mathematical vocabulary"):
        return True
    if reason.startswith("denied vocabulary") or reason.startswith("process vocabulary"):
        scope = re.sub(r"_20\d\d_\d\d_\d\d$", "", slug).replace("_", " ") + " " + (desc or "")[:400]
        hits = [m.group(0) for rx in (HARD_DENY, NON_MATH_DENY, MACHINE_DENY) for m in rx.finditer(scope)]
        return bool(hits) and all(AMBIGUOUS_DENY.match(h.strip()) for h in hits)
    return False


def _forced_row_ambiguous_only(slug, desc):
    """True when slug is a frontier row (rows/T### exists) and every deny hit in its scope is an ambiguous word."""
    if not program_of(slug).startswith("t"):
        return False
    scope = re.sub(r"_20\d\d_\d\d_\d\d$", "", slug).replace("_", " ") + " " + (desc or "")[:400]
    hits = [m.group(0) for rx in (HARD_DENY, NON_MATH_DENY, MACHINE_DENY) for m in rx.finditer(scope)]
    return bool(hits) and all(AMBIGUOUS_DENY.match(h.strip()) for h in hits)


# SELFTEST CONTROLS: synthetic memories, written into a scratch memory folder by `selftest` (no real memory is read).
# The positives must classify AUTO or QUEUE, the negatives SKIP.
POS_CONTROLS = (
    ("cycle_cover_time_selftest", "THEOREM: the expected cover time of the n-cycle by simple random walk is n(n-1)/2, "
                                  "proved by a hitting-time recursion."),
    ("monotone_influence_selftest", "PROVED: every monotone Boolean function on n variables has total influence at most "
                                    "a constant times sqrt(n), with majority extremal."),
    ("spectral_gap_conjecture_refuted_selftest", "Open Problem 3 refuted: a counterexample graph on 12 vertices has spectral "
                                                 "gap below the conjectured bound."),
    ("hypercube_walk_question_selftest", "Does the lazy random walk on the hypercube have a uniform stationary distribution? "
                                         "Yes: its transition matrix is doubly stochastic."),
    ("readonce_constant_selftest", "THEOREM (computer-assisted): the influence constant for read-once formulas is 6.4573, "
                                   "checked by interval arithmetic over every gate."),
)
NEG_CONTROLS = (
    ("method_broken_lemma_selftest", "METHOD: a broken lemma is not a broken conclusion; re-derive the step before "
                                     "discarding the result."),
    ("widget_counting_law_selftest", "THEOREM: a row of widgets counts the crossings of a path; the widget total "
                                     "equals the crossing count times the spacing."),
    ("the_brain_is_worth_points_selftest", "RESULT: recall with the brain answered 65 points more questions than without it."),
    ("cover_time_film_selftest", "RESULT: the film about the cover-time theorem rendered in 40 minutes."),
    ("commit_charge_selftest", "EXACT: the laptop's commit charge for the matrix job was 95 pct of 114 GB."),
    ("private_constant_selftest", "[PRIVATE] THEOREM: the constant of the private problem is 2.5, proved by induction "
                                  "on the graph."),
)
E2E_SLUG, E2E_MARK = "readonce_constant_selftest", "6.4573"
SUCCESSOR = ("readonce_constant_corrected_selftest", "THEOREM (computer-assisted): the influence constant 6.4573 holds for "
                                                     "read-once formulas over monotone gates; the general case is open.")
BOOK_SLUG, BRAIN_TEST_SLUG = "widget_counting_law_selftest", "the_brain_is_worth_points_selftest"


def _control_file(slug, desc, status="verified"):
    return ("---\nname: %s\ndescription: \"%s\"\nmetadata:\n  type: project\n  status: %s\n---\n\n%s\n"
            % (slug, desc.replace('"', "'"), status, desc))


def _read(slug):
    try:
        return io.open(os.path.join(MEM, slug + ".md"), encoding="utf-8", errors="replace").read()
    except Exception:
        return ""


def _front(text):
    """(description, status, modified, body) from a memory file; tolerant of both quoting styles."""
    desc = ""
    m = re.search(r'^description:\s*"?(.+?)"?\s*$', text, re.M)
    if m:
        desc = m.group(1).strip()
    st = ""
    m = re.search(r"^\s*status:\s*([a-z_\-]+)", text, re.M)
    if m:
        st = m.group(1)
    mod = ""
    m = re.search(r"^\s*modified:\s*(\S+)", text, re.M)
    if m:
        mod = m.group(1)
    parts = text.split("---")
    body = ("---".join(parts[2:]) if len(parts) > 2 else text).strip()
    return desc, st, mod, body


# AN OVERTAKEN MEMORY IS NOT A RESULT. The rule above reads the description and never the frontmatter's
# superseded_by, so a result its author later rescoped or re-attributed would go in as current and stay current
# (a claim withdrawn after a referee found a lemma false; a "new proof" that turned out to be a published one).
# Only the FRONTMATTER is read: prose in a body that mentions superseded_by is not a declaration.
SUPERSEDED_RX = re.compile(r"^\s*superseded_by:\s*['\"]?([A-Za-z0-9_\-]+)", re.M)
OVERTAKEN_STATUS = ("retracted", "superseded", "withdrawn", "wrong")


def _frontmatter(text):
    m = re.match(r"\s*---\r?\n(.*?)\r?\n---", text, re.S)
    return m.group(1) if m else ""


def overtaken(text):
    """(True, why) when the memory's own frontmatter says it no longer stands; (False, '') otherwise."""
    fm = _frontmatter(text)
    m = SUPERSEDED_RX.search(fm)
    if m:
        return True, "superseded_by " + m.group(1)
    st = re.search(r"^\s*status:\s*([a-z_\-]+)", fm, re.M)
    if st and st.group(1).lower() in OVERTAKEN_STATUS:
        return True, "status " + st.group(1)
    return False, ""


def terminal_successor(slug, depth=12):
    """Follow superseded_by from slug to the memory that is not itself overtaken; None on a cycle or a missing file."""
    seen, cur = {slug}, slug
    for _ in range(depth):
        m = SUPERSEDED_RX.search(_frontmatter(_read(cur)))
        if not m:
            return cur if cur != slug else None
        nxt = m.group(1)
        if nxt in seen or not os.path.exists(os.path.join(MEM, nxt + ".md")):
            return None
        seen.add(nxt)
        cur = nxt
    return None


def stale_in_store(store=STORE):
    """[(claim_id, slug, why)] for store claims transported from a memory that is now overtaken and that no later
    claim in the store supersedes yet. Read-only; [] on any error."""
    out = []
    try:
        db = sqlite3.connect("file:%s?mode=ro" % store.replace("\\", "/"), uri=True)
        rows = db.execute("select claim_id, source_ref from claim_provenance where source_ref like 'memory:%'").fetchall()
        for cid, ref in rows:
            slug = ref[len("memory:"):]
            ov, why = overtaken(_read(slug))
            if not ov:
                continue
            if db.execute("select 1 from edges where target_id=? and kind='supersedes'", (cid,)).fetchone():
                continue
            out.append((cid, slug, why))
        db.close()
    except Exception:
        return []
    return out


def strip_head(desc):
    d = TAG_RX.sub("", desc, count=1)
    d = DATE_RX.sub("", d, count=1)
    return d.strip()


PRIVATE_HEAD = re.compile(r"\bPRIVATE\b")


def classify(slug, desc, status=None):
    """Return (tier, reason). Tier is AUTO, QUEUE or SKIP. With the memory's frontmatter status, a SKIP of a verified
    program memory for want of a marker or on ambiguous deny words becomes QUEUE (PROGRAM GUARD)."""
    # A memory tagged PRIVATE at its head is a hard SKIP the guard cannot lift: the math store may be exported to a
    # shared repo.
    if desc and PRIVATE_HEAD.search(desc[:160]):
        return "SKIP", "tagged PRIVATE"
    tier, reason = _classify(slug, desc)
    if tier == "SKIP" and PROGRAM_GUARD and status is not None and _program_guard(slug, desc, status, reason):
        return "QUEUE", "program guard (%s, verified): %s - an agent decides" % (program_of(slug), reason)
    return tier, reason


def _classify(slug, desc):
    if not desc:
        return "SKIP", "no description"
    if any(slug.startswith(p) for p in SKIP_PREFIX):
        return "SKIP", "process-note slug prefix"
    if SKIP_HEAD.search(desc):
        return "SKIP", "process-note head tag"
    head = desc[:240]
    core = strip_head(head)
    # the denies read the SLUG too: a slug can carry a deny word the description's first 240 characters lack, and
    # without it the memory would walk into the math store on the strength of "SETTLED"
    scope = re.sub(r"_20\d\d_\d\d_\d\d$", "", slug).replace("_", " ") + " " + desc[:400]
    hard = HARD_DENY.search(scope)
    if hard:
        return "SKIP", "denied vocabulary: %s" % hard.group(0)
    non = NON_MATH_DENY.search(scope) or MACHINE_DENY.search(scope)
    if non:
        return "SKIP", "process vocabulary: %s" % non.group(0)
    vocab = MATH_SIGNAL.search(head) or MATH_SIGNAL_NAMED.search(head)
    formula = FORMULA_HEAD.search(core[:200])
    if not (vocab or formula):
        return "SKIP", "no mathematical vocabulary"
    # the result word is read BEFORE the date is stripped ("RESULT 09-10 (author-checked): ...", "PROVED 09-09:",
    # "09-21 05:0x-08:1x: THEOREM ...") - stripping first was how the first cut of this rule missed six positives
    mark = RESULT_MARK.search(TAG_RX.sub("", head, count=1)[:70])
    # a question-first head keeps its result word in the answer ("...? PROVED 23 Sep: ..."), read it there too
    q = core.find("?")
    answer = core[q + 1:].lstrip() if 0 < q < 200 else None
    if not mark and answer is not None:
        mark = RESULT_MARK.search(answer[:70])
    named = NAMED_PROBLEM.search(core[:100]) and (RESULT_VERB.search(core[:200]) or EXTRA_RESULT_VERB.search(core[:200]))
    yesno = YESNO_ANSWER.match(answer) if answer is not None else None
    if not (mark or named or yesno):
        return "SKIP", "no result marker"
    if CYCLE_LOG.search(desc):
        return "QUEUE", "a campaign cycle log - an agent decides which cycles are results"
    soft = SOFT_DENY.search(head)
    if soft:
        return "QUEUE", "result marker but a both-worlds word: %s" % soft.group(0)
    if not vocab:
        return "QUEUE", "a formula but no mathematical vocabulary - an agent decides"
    if yesno and not (mark or named):
        return "QUEUE", "question-first head answered %s - an agent decides" % yesno.group(1)
    return "AUTO", ("head result word %s" % mark.group(0)) if mark else "named problem + result verb"


def guess_kind(desc):
    d = desc.lower()
    if re.search(r"\b(refuted|counterexample|disproof|disproved|is false|fails for every|answered in the negative)\b", d):
        return "counterexample"
    if re.search(r"\b(theorem|proved|proven|settled|kernel accepted|found correct|is true|holds)\b", d):
        return "theorem"
    if re.search(r"\bconjecture\b", d) and re.search(r"\b(reduced to|open|conjectured|equivalent)\b", d):
        return "conjecture"
    if re.search(r"\b(numerically|computed|exact certificate|measured|value iteration)\b", d):
        return "computation"
    return "concept"


def guess_domain(text):
    t = text.lower()
    for words, dom in (
        (("markov", "mixing", "chain", "hitting", "cover time", "kemeny", "stationary"), "probability/markov chains"),
        (("queue", "m/g/1", "workload", "pollaczek"), "probability/queueing"),
        (("boolean", "fourier", "entropy", "influence", "read-once", "fei", "kkl"), "boolean functions/fourier analysis"),
        (("percolation", "crossing", "lattice", "ising"), "probability/percolation"),
        (("random matrix", "eigenvalue", "singular value", "semicircle", "wigner"), "random matrix theory"),
        (("graph", "combinator", "rado", "nae", "mols", "orthogonal array", "box"), "combinatorics"),
        (("kernel", "regression", "learning", "neural", "relu"), "learning theory"),
        (("operator", "fixed point", "ergodic", "volterra", "dynamical"), "dynamical systems"),
        (("bernoulli convolution", "frostman", "dimension", "self-similar"), "fractal geometry/analysis"),
        (("lean", "formal"), "formal verification"),
    ):
        if any(w in t for w in words):
            return dom
    return "mathematics"


def title_of(slug, desc):
    """The first sentence of the stripped description, up to 140 characters. A cut at the first colon gave
    "on the goal 'keep working on closing FEI'" and "THEOREM (computer-assisted)" as titles - so a colon or a
    dash ends the title only when what precedes it is long enough to name the result on its own."""
    core = strip_head(desc)
    # a status bracket too long for TAG_RX ("[VERIFIED, 2 audits + 24-digit limit; OUT OF THE PENCIL IT IS EXCEEDED:
    # ...] T366 condition (B) ...") was cut at its own ';' and became the whole title - drop it here
    # only, so the statement and its sha keep the bracket
    rest = LONG_TAG_RX.sub("", core, count=1).strip()
    if len(rest) >= 20:
        core = rest
    # a lowercase preamble before the first colon ("on the goal '...': for read-once formulas the FEI constant
    # is ...") is context, not the result - the title is what follows it
    pre = re.match(r"^((on|for|in|under|his|her|their|the|during|after|at|from|per|by)\b[^:]{0,80}):\s+(.+)$", core, re.S)
    if pre:
        core = pre.group(3)
    first = re.split(r"(?<=[a-z0-9\)])[.;]\s", core, maxsplit=1)[0].strip()
    m = re.match(r"(.{28,120}?)(:\s|\s-\s)", first)
    # never cut inside an open parenthesis ("The Kemeny paper (Aldous-Fill 6.13, tau_0 half: M_n = ...")
    cut = m.group(1).strip() if (m and m.group(1).count("(") == m.group(1).count(")")) else first
    # a bare result word with its qualifier ("RESULT (numerical search, not a proof): T364 ...") names no object;
    # the title is what follows the colon (a card was once titled by its qualifier alone). Not for THEOREM:
    # "THEOREM (pathwise gamma-carry identity)" carries the theorem's name in its bracket
    if m and cut is not first and not cut.startswith("THEOREM") and re.match(r"^[A-Z ]+\b\s*(\([^()]*\))?$", cut) and RESULT_MARK.search(cut):
        after = first[m.end():].strip()
        if len(after) >= 20:
            cut = after
    if len(cut) > 140:
        cut = cut[:137].rsplit(" ", 1)[0] + "..."
    if len(cut) >= 20:
        return cut
    words = re.sub(r"_20\d\d_\d\d_\d\d$", "", slug).replace("_", " ")
    return words[:1].upper() + words[1:]


# ---- ledger / queue --------------------------------------------------------------------------------------
def _append(path, row):
    with io.open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=True) + "\n")


def _rows(path):
    out = []
    if not os.path.exists(path):
        return out
    for line in io.open(path, encoding="utf-8", errors="replace"):
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except Exception:
                pass
    return out


def done_slugs(store=STORE):
    """Slugs that already live in the store (provenance) or were dismissed - never touched again."""
    done = set()
    try:
        db = sqlite3.connect("file:%s?mode=ro" % store.replace("\\", "/"), uri=True)
        for (ref,) in db.execute("select source_ref from claim_provenance where source_ref like 'memory:%'"):
            done.add(ref[len("memory:"):])
        db.close()
    except Exception:
        pass
    if store == STORE:   # the ledger describes the live store only; a scratch copy is judged by its own rows
        for r in _rows(LEDGER):
            if r.get("action") in ("ingested", "dismissed"):
                done.add(r.get("slug"))
    return done


def provisional_rows_uncarried(done=None):
    """Provisional frontier-row memories (t###_ with rows/T### on disk) that are neither in the store nor dismissed and
    still stand. The program guard admits verified rows only, so these never reach the queue; '0 queued' says nothing
    about them."""
    done = done_slugs() if done is None else done
    out = []
    try:
        names = os.listdir(MEM)
    except Exception:
        return out
    for f in names:
        if not f.endswith(".md"):
            continue
        slug = f[:-3]
        m = FRONTIER_ROW_ID.search(slug)
        if not m or slug in done or not frontier_row_known(m.group(1)):
            continue
        text = _read(slug)
        if _front(text)[1] == "provisional" and not overtaken(text)[0]:
            out.append(slug)
    return sorted(out)


def queued():
    q = {}
    for r in _rows(QUEUE):
        if r.get("action") == "queued":
            q[r["slug"]] = r
        elif r.get("action") in ("ingested", "dismissed", "revised", "revision_dismissed"):
            q.pop(r.get("slug"), None)
    return q


# ---- revisions: a transported memory whose description changed -------------------------------------------
def _desc_sha(statement):
    import hashlib
    return hashlib.sha256(statement.encode("utf-8")).hexdigest()[:16]


def transported_heads(slug, store=STORE):
    """[(claim_id, statement)] for the claims THIS transport wrote from memory:<slug> (source_kind 'memory') that
    nothing in the store supersedes yet. A typed refinement (source_kind 'campaign') is never listed, and a
    transported claim an agent has superseded is not a head. [] on any error."""
    out = []
    try:
        db = sqlite3.connect("file:%s?mode=ro" % store.replace("\\", "/"), uri=True)
        for (cid,) in db.execute("select claim_id from claim_provenance where source_ref=? and source_kind='memory'",
                                 ("memory:" + slug,)).fetchall():
            if db.execute("select 1 from edges where target_id=? and kind='supersedes'", (cid,)).fetchone():
                continue
            row = db.execute("select body from nodes where id=?", (cid,)).fetchone()
            out.append((cid, row[0] if row else ""))
        db.close()
    except Exception:
        return []
    return out


def revisions(since=None, store=STORE):
    """[(slug, action, reason, head_ids, old_len, new_len, sha)] for transported memories whose description no longer
    matches their store claim. action is AUTO (the description grew and still classifies AUTO) or QUEUE (an agent
    decides). A description an agent kept with dismiss-revision is skipped until it changes again. Read-only."""
    kept = {(r.get("slug"), r.get("desc_sha")) for r in _rows(LEDGER) if r.get("action") == "revision_dismissed"}
    slugs = set()
    try:
        db = sqlite3.connect("file:%s?mode=ro" % store.replace("\\", "/"), uri=True)
        for (ref,) in db.execute("select source_ref from claim_provenance where source_ref like 'memory:%' and source_kind='memory'"):
            slugs.add(ref[len("memory:"):])
        db.close()
    except Exception:
        return []
    out = []
    for slug in sorted(slugs):
        f = os.path.join(MEM, slug + ".md")
        try:
            if since is not None and os.path.getmtime(f) < since:
                continue
        except OSError:
            continue       # the memory file is gone: nothing to carry
        text = _read(slug)
        if overtaken(text)[0]:
            continue       # stale_in_store() queues these for a successor
        desc = _front(text)[0]
        new = strip_head(desc)[:1500]
        heads = transported_heads(slug, store)
        if not heads or not new or any(stmt == new for _, stmt in heads):
            continue
        sha = _desc_sha(new)
        if (slug, sha) in kept:
            continue
        old_len = max(len(stmt) for _, stmt in heads)
        tier, why = classify(slug, desc)
        # A SMALL LOCAL EDIT IS CARRIED, NOT QUEUED: a tally rewrite ("three of three" -> "five of six") or a
        # few-character fix shrinks the description without dropping the statement. A rewrite that drops the statement shrinks by more than this or stops resembling the claim.
        sim = max(difflib.SequenceMatcher(None, stmt, new, autojunk=False).ratio() for _, stmt in heads)
        small = old_len - len(new) <= min(40, 0.05 * old_len) and sim >= 0.95
        if tier == "AUTO" and len(new) >= old_len:
            action, reason = "AUTO", "description grew %d -> %d chars and classifies AUTO (%s)" % (old_len, len(new), why)
        elif tier == "AUTO" and small:
            action, reason = "AUTO", "description shrank %d -> %d chars by a local edit (similarity %.3f) and classifies AUTO (%s)" % (
                old_len, len(new), sim, why)
        elif tier == "AUTO":
            action, reason = "QUEUE", "description shrank %d -> %d chars: a rewrite may drop the statement - an agent decides" % (old_len, len(new))
        else:
            action, reason = "QUEUE", "description changed %d -> %d chars and now classifies %s (%s) - an agent decides" % (old_len, len(new), tier, why)
        out.append((slug, action, reason, [h for h, _ in heads], old_len, len(new), sha))
    return out


# ---- the store write -------------------------------------------------------------------------------------
def _sqlite_copy(src, dst):
    """A copy of a SQLite store's committed state, through the backup API from one read transaction, written as a
    single rollback-journal file. The store runs in WAL mode, where committed pages sit in brain.sqlite3-wal until a
    checkpoint, and a copy of the main file alone leaves them out."""
    tmp = dst + ".tmp"
    for p in (tmp, tmp + "-wal", tmp + "-shm", tmp + "-journal"):
        if os.path.exists(p):
            os.remove(p)
    s = sqlite3.connect("file:%s?mode=ro" % os.path.abspath(src).replace("\\", "/"), uri=True)
    d = sqlite3.connect(tmp)
    try:
        s.backup(d)
        d.execute("PRAGMA journal_mode=DELETE")
    finally:
        d.close()
        s.close()
    os.replace(tmp, dst)


def _backup_once(store):
    stamp = time.strftime("%Y%m%d")
    bak = store + ".bak_transport_" + stamp
    if not os.path.exists(bak):
        _sqlite_copy(store, bak)
    return bak


def ingest(slug, store=STORE, force=False, dry=False, rebuild=True):
    """Write one memory into the store. Returns (ok, claim_id_or_reason)."""
    text = _read(slug)
    if not text:
        # a slug list written on Windows and read by bash keeps its \r and every slug misses its file; name that cause
        return False, "refused: no memory file %s.md" % slug
    desc, st, mod, body = _front(text)
    _ov, _why = overtaken(text)
    if _ov:
        return False, "refused: the memory is overtaken (%s); transport its successor instead" % _why
    tier, reason = classify(slug, desc, st)
    if tier == "SKIP" and not force:
        return False, "refused: %s" % reason
    # a provisional frontier row (provrows says: ingest --force) whose only deny words are the ambiguous ones ("plateau"
    # as a loss plateau) passes when forced; a word from the hard list still refuses.
    if tier == "SKIP" and force and reason.startswith("denied vocabulary") and not _forced_row_ambiguous_only(slug, desc):
        return False, "refused even when forced: %s (the deny boundary is not overridable here)" % reason
    if slug in done_slugs(store):
        return False, "already in the store"
    if dry:
        return True, "would ingest (%s)" % reason
    return _write_claim(slug, desc, st, mod, body, store=store, rebuild=rebuild)


def revise(slug, store=STORE, dry=False, rebuild=True, why="an agent's verdict on a queued revision", retitle=False):
    """Carry a transported memory's CHANGED description: a new claim whose SUPERSEDES edges retire every transported
    head of that memory. Returns (ok, new_claim_id_or_reason). Refuses an overtaken memory (its successor is the
    thing to carry), a memory with no transported head, and a description the store already holds."""
    text = _read(slug)
    if not text:
        return False, "refused: no such memory"
    desc, st, mod, body = _front(text)
    _ov, _why = overtaken(text)
    if _ov:
        return False, "refused: the memory is overtaken (%s); transport its successor instead" % _why
    tier, reason = classify(slug, desc)
    if tier == "SKIP" and reason.startswith(("denied vocabulary", "process-note")):
        return False, "refused: %s (a revision never carries what a first ingest would refuse)" % reason
    heads = transported_heads(slug, store)
    new = strip_head(desc)[:1500]
    if not heads:
        return False, "refused: no transported claim of this memory is a head (never carried, or an agent superseded it)"
    if any(stmt == new for _, stmt in heads):
        # retitle: same statement, but the head's title was cut by an older title_of (a bare status bracket)
        if not retitle:
            return False, "refused: the store already holds this description"
        want = title_of(slug, desc)
        try:
            db = sqlite3.connect("file:%s?mode=ro" % store.replace("\\", "/"), uri=True)
            have = [(db.execute("select title from nodes where id=?", (h,)).fetchone() or [""])[0] for h, _ in heads]
            db.close()
        except Exception as exc:
            return False, "refused: could not read the heads' titles (%s)" % exc
        if all(t == want for t in have):
            return False, "refused: the store already holds this description under this title"
        why = "%s (retitle %r -> %r)" % (why, have[0][:60], want[:60])
    if dry:
        return True, "would revise %d head(s): %s" % (len(heads), why)
    return _write_claim(slug, desc, st, mod, body, store=store, rebuild=rebuild, supersedes=[h for h, _ in heads], note=why)


def correct(stale_slug, statement, store=STORE, dry=False, rebuild=True):
    """Land an agent-written correction for a claim whose memory was overtaken (the STALE IN STORE queue row): a new
    claim with `statement`, carried from the overtaking memory (the terminal successor), that SUPERSEDES every head of
    the stale memory's claims. Provenance kind 'campaign' - it is a typed refinement written by an agent, so the
    revision rule never compares it with the successor memory's description. Returns (ok, claim_id_or_reason)."""
    statement = (statement or "").strip()
    if len(statement) < 40:
        return False, "refused: write the corrected mathematical statement (40 characters at least)"
    ov, why = overtaken(_read(stale_slug))
    if not ov:
        return False, "refused: memory %s is not overtaken; nothing to correct" % stale_slug
    heads = []
    try:
        db = sqlite3.connect("file:%s?mode=ro" % store.replace("\\", "/"), uri=True)
        for (cid,) in db.execute("select claim_id from claim_provenance where source_ref=?", ("memory:" + stale_slug,)).fetchall():
            if not db.execute("select 1 from edges where target_id=? and kind='supersedes'", (cid,)).fetchone():
                heads.append(cid)
        db.close()
    except Exception as exc:
        return False, "refused: store read failed (%s)" % exc
    if not heads:
        return False, "refused: no claim of %s is a head (already corrected?)" % stale_slug
    succ = terminal_successor(stale_slug) or stale_slug
    s_desc, s_st, s_mod, s_body = _front(_read(succ))
    if dry:
        return True, "would supersede %s with a correction carried from %s" % (heads, succ)
    return _write_claim(succ, statement, s_st, s_mod, s_body or "", store=store, rebuild=rebuild, supersedes=heads,
                        note="correction: %s is overtaken (%s)" % (stale_slug, why), source_kind="campaign")


# PRIVATE TOPICS. A card on such a topic IS carried into the store, but its node metadata carries
# private_topic = "mb-private-topic:<topic>", so an export of the store for a public edition can drop every marked
# card (and every row citing it). Add (name, compiled regex) pairs here for work that must not leave your machine.
PRIVATE_TOPICS = ()


def private_topic(slug, desc, body=""):
    text = slug.replace("_", " ") + " " + desc + " " + body[:1200]
    for name, rx in PRIVATE_TOPICS:
        if rx.search(text):
            return "mb-private-topic:" + name
    return None


def _write_claim(slug, desc, st, mod, body, store=STORE, rebuild=True, supersedes=(), note="", source_kind="memory"):
    """The one store write: claim + node + evidence + provenance row (+ SUPERSEDES edges for a revision)."""
    sys.path.insert(0, BUILD_SRC)
    from math_brain.models import Claim, ClaimKind, Evidence, EvidenceKind, GraphEdge, GraphNode, NodeKind, RecordStatus, EdgeKind
    from math_brain.store import ResearchStore
    statement = strip_head(desc)[:1500]
    kind = guess_kind(desc)
    domain = guess_domain(desc + " " + body[:600])
    claim = Claim(statement=statement, kind=ClaimKind(kind), assumptions=(), domain=domain,
                  status=RecordStatus.UNVERIFIED)
    # THE NODE BODY IS THE CLAIM STATEMENT, BYTE FOR BYTE. The hook's reader (math_brain.current_note) binds a
    # claim to its node by `claim.statement == node.body` and REFUSES the card otherwise
    # (claim_node_statement_mismatch), and the hook's selection_integrity gate silently drops a refused card.
    # The first cut of this writer appended a memory excerpt to the body: 54 claims landed in the store, the
    # prefilter ranked two of them above the open-problem card, and the hook still served the open problem.
    ptopic = private_topic(slug, desc, body)
    node = GraphNode(id=claim.id, kind=NodeKind.CLAIM, title=title_of(slug, desc)[:140],
                     body=statement,
                     metadata={"claim_kind": kind, "domain": domain,
                               "provenance": "transported from the main brain memory by math_transport.py; "
                                             "statement = the memory description, prose, not a typed theorem",
                               "source_id": "memory:" + slug, "memory_status": st or "unknown",
                               "memory_modified": mod, "transport_version": TRANSPORT_VERSION,
                               **({"revision_of": list(supersedes), "revision_note": note} if supersedes else {}),
                               **({"private_topic": ptopic} if ptopic else {})})
    ev = Evidence(claim_id=claim.id, kind=EvidenceKind.DISCOVERY_REPORT,
                  summary="%s from main-brain memory %s (memory status %s) by math_transport.py on %s"
                          % ("revised description transported" if supersedes else "transported", slug, st or "unknown",
                             time.strftime("%Y-%m-%d")),
                  scope="statement text copied from the memory description; not re-derived",
                  verifier="math_transport.py", passed=True,
                  limitations=("the statement is prose from a memory, not a typed theorem; refine by hand "
                               "(kind, assumptions, precise statement) as a new claim with a SUPERSEDES edge",
                               "the main-brain status '%s' is the memory author's reading, not a store verification"
                               % (st or "unknown")))
    if store == STORE:
        _backup_once(store)
    # a revision retires every transported head of the memory in the SAME transaction as the new claim, so a failed
    # edge cannot leave two heads of one memory competing for the card
    edges = [GraphEdge(source_id=claim.id, target_id=old, kind=EdgeKind.SUPERSEDES,
                       rationale="the memory %s revised its description (%s); math_transport.py carries the new statement"
                                 % (slug, note or "description changed since transport"),
                       metadata={"by": "math_transport.py revise", "memory_modified": mod})
             for old in supersedes]
    rs = ResearchStore(store)
    try:
        rs.add_claim(claim, node=node, edges=edges)
        rs.add_evidence(ev)
        # a fresh store has no provenance table until something creates it; the transport is often the first writer
        from math_brain import provenance as _prov
        _prov.ensure_schema(rs.connection)
        rs.connection.execute(
            "INSERT INTO claim_provenance(claim_id, evidence_class, source_kind, source_ref, artifact_path, "
            "bundle_id, fire_id, measurement, status, read_from, recorded_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (claim.id, "derived", source_kind, "memory:" + slug, os.path.join(MEM, slug + ".md"), "", "",
             strip_head(desc)[:200], st or "unknown", '["provenance", "status"]',
             time.strftime("%Y-%m-%dT%H:%M:%S%z")))
        rs.connection.commit()
    finally:
        try:
            rs.connection.close()
        except Exception:
            pass
    if rebuild and store == STORE:
        rebuild_prefilter(store)
    return True, claim.id


def rebuild_prefilter(store=STORE):
    sys.path.insert(0, HERE)
    import math_prefilter
    return math_prefilter.build(store)


# ---- commands --------------------------------------------------------------------------------------------
def scan(verbose=True, since=None):
    """Classify every memory (or, with `since`, only files modified after that epoch second - the 15-minute
    task reads a few dozen files instead of seventeen thousand; a full pass is `run --full`)."""
    done = done_slugs()
    tiers = {"AUTO": [], "QUEUE": [], "SKIP": 0, "DONE": [], "UNREAD": 0}
    for f in sorted(glob.glob(os.path.join(MEM, "*.md"))):
        slug = os.path.basename(f)[:-3]
        if slug.isupper() or slug in ("MEMORY", "MISTAKES", "OPEN_QUESTIONS", "CONSCIENCE"):
            continue
        if since is not None:
            try:
                if os.path.getmtime(f) < since:
                    tiers["UNREAD"] += 1
                    continue
            except OSError:
                continue
        text = _read(slug)
        if overtaken(text)[0]:
            tiers["SKIP"] += 1
            continue
        desc, st = _front(text)[:2]
        tier, reason = classify(slug, desc, st)
        if tier == "SKIP":
            tiers["SKIP"] += 1
            continue
        if slug in done:
            tiers["DONE"].append(slug)
            continue
        tiers[tier].append((slug, reason, desc[:90]))
    if verbose:
        print("scan: AUTO %d | QUEUE %d | already in store or dismissed %d | SKIP %d"
              % (len(tiers["AUTO"]), len(tiers["QUEUE"]), len(tiers["DONE"]), tiers["SKIP"]))
        for t in ("AUTO", "QUEUE"):
            print("--- %s" % t)
            for slug, reason, d in tiers[t]:
                print("  %-64s | %-34s | %s" % (slug[:64], reason[:34], d))
    return tiers


def run(dry=False, full=False):
    held, h = hold_state()
    if held and not dry:
        print("run: HELD until %s by %s (%s) - nothing written; the held window is read again after it ends"
              % (h.get("until"), h.get("by"), h.get("why", "")[:120]))
        return 0
    since = None
    if not full:
        try:
            _st = json.load(io.open(STATE, encoding="utf-8"))
            since = time.mktime(time.strptime(_st["last_run"], "%Y-%m-%dT%H:%M:%S")) - 48 * 3600.0
        except Exception:
            since = None      # no state yet: the first run is a full pass
    tiers = scan(verbose=False, since=since)
    q = queued()
    n_ing = n_q = n_fail = n_rev = n_vec = 0
    stale = []
    now = time.strftime("%Y-%m-%dT%H:%M:%S")
    gate = contextlib.nullcontext if dry else _gated_write
    try:
        for slug, reason, d in tiers["AUTO"]:
            with gate():
                try:
                    ok, what = ingest(slug, dry=dry, rebuild=False)
                except Exception as exc:
                    ok, what = False, "%s: %s" % (type(exc).__name__, str(exc)[:120])
                if ok and not dry:
                    n_ing += 1
                    _append(LEDGER, {"ts": now, "slug": slug, "tier": "AUTO", "action": "ingested", "claim_id": what, "reason": reason})
                    if slug in q:
                        _append(QUEUE, {"ts": now, "slug": slug, "action": "ingested"})
                elif ok and dry:
                    n_ing += 1
                else:
                    n_fail += 1
                    if not dry:
                        _append(LEDGER, {"ts": now, "slug": slug, "tier": "AUTO", "action": "failed", "reason": what})
        # The scan read done_slugs() when it began; an agent's `ingest` landing while it ran is not in that read, and the
        # row went on the queue anyway and stayed open until the 48 h alarm. Read
        # the store and ledger again here so a slug carried meanwhile is not queued.
        _done_now = done_slugs() if tiers["QUEUE"] and not dry else set()
        for slug, reason, d in tiers["QUEUE"]:
            if slug in _done_now:
                continue
            if slug not in q and not dry:
                with gate():
                    _append(QUEUE, {"ts": now, "slug": slug, "action": "queued", "reason": reason, "desc": d})
                    _append(LEDGER, {"ts": now, "slug": slug, "tier": "QUEUE", "action": "queued", "reason": reason})
                n_q += 1
            elif slug not in q:
                n_q += 1
        # REVISIONS (module docstring): a transported memory whose description changed since it was carried
        q = queued()
        for slug, action, reason, heads, old_len, new_len, sha in revisions(since=since):
            if action == "AUTO":
                if dry:
                    n_rev += 1
                    continue
                with gate():
                    try:
                        ok, what = revise(slug, rebuild=False, why=reason)
                    except Exception as exc:
                        ok, what = False, "%s: %s" % (type(exc).__name__, str(exc)[:120])
                    if ok:
                        n_rev += 1
                        _append(LEDGER, {"ts": now, "slug": slug, "tier": "AUTO", "action": "revised", "claim_id": what,
                                         "supersedes": heads, "reason": reason, "desc_sha": sha})
                        if slug in q:
                            _append(QUEUE, {"ts": now, "slug": slug, "action": "revised"})
                    else:
                        n_fail += 1
                        _append(LEDGER, {"ts": now, "slug": slug, "tier": "AUTO", "action": "failed", "reason": "revision: " + what})
            elif slug not in q and not dry:
                with gate():
                    _append(QUEUE, {"ts": now, "slug": slug, "action": "queued", "reason": "REVISED MEMORY: " + reason,
                                    "desc": "", "desc_sha": sha, "supersedes": heads})
                    _append(LEDGER, {"ts": now, "slug": slug, "tier": "QUEUE", "action": "queued", "reason": "revision: " + reason})
                n_q += 1
            elif slug not in q:
                n_q += 1
        # A CLAIM WHOSE MEMORY WAS OVERTAKEN AFTER TRANSPORT goes on the queue (so the 48 h alarm reaches an agent) until
        # a later claim SUPERSEDES it in the store; the queue row closes itself once that edge exists.
        stale = stale_in_store() if not dry else []
        if not dry:
            stale_slugs = {s for _, s, _ in stale}
            for cid, slug, why in stale:
                if slug not in q:
                    with gate():
                        _append(QUEUE, {"ts": now, "slug": slug, "action": "queued",
                                        "reason": "STALE IN STORE: claim %s carries an overtaken memory (%s); land the successor's "
                                                  "statement as a claim that SUPERSEDES it" % (cid, why), "desc": ""})
                    n_q += 1
            for slug, row in q.items():
                if str(row.get("reason", "")).startswith("STALE IN STORE") and slug not in stale_slugs:
                    with gate():
                        _append(QUEUE, {"ts": now, "slug": slug, "action": "dismissed", "why": "superseded in the store"})
        # A STALE INDEX IS REBUILT WHATEVER WROTE THE STORE. An index rebuilt only after the transport's OWN ingests
        # stays blind to claims another session wrote straight into the store, such as conjecture nodes filed while
        # agents work on that conjecture. math_prefilter.select() now scores such nodes on the fly (its fresh-node lane), and this
        # run folds them into the index proper - a 2-3 s build every 15 minutes at most, only when something is newer.
        _stale = 0
        if not dry and not n_ing:
            try:
                sys.path.insert(0, HERE)
                import math_prefilter
                _stale = len(math_prefilter.fresh_nodes(STORE, limit=1))
            except Exception:
                _stale = 0
        if (n_ing or n_rev or _stale) and not dry:
            with gate():
                rebuild_prefilter()
        # THE CLAIM VECTORS FOLLOW THE STORE TOO (when math_claim_vecs is installed). Vectors extended only by hand
        # would be missing for new claims, so a claim this run ingested had no vector: the channel could not name it, and the
        # hook's agreement check chose among the older claims. Every run now embeds the claims the file lacks (in-process,
        # like the prefilter: a subprocess would open a console), whoever wrote them; nothing is written when none is missing.
        if not dry:
            with gate():
                try:
                    sys.path.insert(0, HERE)
                    import math_claim_vecs
                    n_vec, _total, _note = math_claim_vecs.extend(STORE)
                    if n_vec or _note:
                        print("claim vectors: +%d, %d in the file%s" % (n_vec, _total, (" - " + _note) if _note else ""))
                except Exception as exc:
                    print("claim vectors: not extended (%s: %s)" % (type(exc).__name__, exc))
        if not dry:
            with gate():
                json.dump({"last_run": now, "ingested": n_ing, "revised": n_rev, "queued_new": n_q, "failed": n_fail,
                           "auto_total": len(tiers["AUTO"]), "queue_total": len(tiers["QUEUE"]), "vectors_added": n_vec},
                          io.open(STATE, "w", encoding="utf-8"))
    except HeldMidRun as exc:
        h = exc.args[0] if exc.args else {}
        print("run: HELD mid-run until %s by %s (%s) - stopped before its next write, after %d ingested and %d revised; "
              "no state written, so the held window is read again after it ends"
              % (h.get("until"), h.get("by"), str(h.get("why", ""))[:120], n_ing, n_rev))
        return 0
    except TimeoutError as exc:
        print("run: stopped - %s; no state written, so the next run reads the window again" % exc)
        return 1
    print("run%s: ingested %d, revised %d, newly queued %d, failed %d, stale claims in store %d (AUTO %d, QUEUE %d; %s)"
          % (" (dry)" if dry else "", n_ing, n_rev, n_q, n_fail, len(stale), len(tiers["AUTO"]), len(tiers["QUEUE"]),
             ("full pass" if since is None else "incremental, %d files unchanged since the window and not opened" % tiers["UNREAD"])))
    return 0 if not n_fail else 1


def status():
    """One line for hook_liveness. Exit 1 when the transport is dead or a queued result has waited too long."""
    st = {}
    try:
        st = json.load(io.open(STATE, encoding="utf-8"))
    except Exception:
        pass
    now = time.time()
    last = st.get("last_run")
    age_h = None
    if last:
        try:
            age_h = (now - time.mktime(time.strptime(last, "%Y-%m-%dT%H:%M:%S"))) / 3600.0
        except Exception:
            age_h = None
    q = queued()
    oldest_h = 0.0
    for r in q.values():
        try:
            oldest_h = max(oldest_h, (now - time.mktime(time.strptime(r["ts"], "%Y-%m-%dT%H:%M:%S"))) / 3600.0)
        except Exception:
            pass
    n_ing = sum(1 for r in _rows(LEDGER) if r.get("action") == "ingested")
    bad = []
    held, h = hold_state(now)
    if age_h is None:
        bad.append("NEVER RAN")
    elif age_h > RUN_STALE_H and not held:
        bad.append("last run %.1fh ago (>%.0fh)" % (age_h, RUN_STALE_H))
    if held:
        print("math transport: HELD until %s by %s (%s) - no store writes while it lasts" % (h.get("until"), h.get("by"), h.get("why", "")[:100]))
    elif h is not None and os.path.exists(HOLD):
        bad.append("a lapsed hold file is still on disk (until %s, by %s) - run: python math_transport.py release" % (h.get("until"), h.get("by")))
    if oldest_h > QUEUE_STALE_H:
        bad.append("a queued result has waited %.0fh (>%.0fh) - an agent must ingest or dismiss it" % (oldest_h, QUEUE_STALE_H))
    pf_note = ""
    try:
        sys.path.insert(0, HERE)
        import math_prefilter
        pf_fresh = math_prefilter.fresh_nodes(STORE, limit=1000)
        if pf_fresh:
            pf_note = ", %d store node(s) newer than the prefilter index" % len(pf_fresh)
            idx_age_h = (now - os.path.getmtime(math_prefilter.index_path(STORE))) / 3600.0
            if idx_age_h > 1.0:
                bad.append("the prefilter index is %.1fh old with %d newer node(s) - run python math_prefilter.py build %s"
                           % (idx_age_h, len(pf_fresh), STORE))
    except Exception:
        pass
    # a claim without a vector is invisible to the meaning channel and keeps the hook's agreement check closed; one
    # transport run closes the gap, so only a gap older than an hour is a fault
    try:
        sys.path.insert(0, HERE)
        import math_claim_vecs
        vec_ok, vec_line = math_claim_vecs.status(STORE)
        if not vec_ok:
            vec_age_h = (now - os.path.getmtime(math_claim_vecs.vector_path(STORE))) / 3600.0
            if vec_age_h > 1.0 or "name no node" in vec_line or "cannot be read" in vec_line:
                bad.append(vec_line)
            else:
                pf_note += ", " + vec_line
    except ImportError:
        pf_note += ", claim vectors not installed (math_claim_vecs.py absent: the meaning channel is off)"
    except FileNotFoundError:
        bad.append("claim vectors: none beside the store")
    except Exception as exc:
        bad.append("claim vectors: status failed (%s)" % type(exc).__name__)
    try:
        prov = provisional_rows_uncarried()
        if prov:   # information, not a fault: whether the guard should queue provisional rows is still undecided
            pf_note += ", %d provisional frontier-row memories outside the store (python math_transport.py provrows)" % len(prov)
    except Exception:
        pass
    line = ("math transport: %d results carried into the math store to date, last run %s, %d queued for review%s%s - %s"
            % (n_ing, ("%.1fh ago" % age_h) if age_h is not None else "never", len(q),
               (" (oldest %.0fh)" % oldest_h) if q else "", pf_note, "; ".join(bad) if bad else "ok"))
    print(line)
    return 1 if bad else 0


def selftest():
    global _read   # the revision controls read memories through a stand-in, restored in their finally
    global HOLD, STORE, LEDGER, QUEUE, STATE   # the hold controls point every write path into a scratch folder
    global MEM, FRONTIER_ROWS, FRONTIER_ROW_LIST, _ROW_IDS   # the controls live in a scratch memory folder
    global HARD_DENY, SOFT_DENY   # the controls run on a synthetic deny file, restored in the finally
    import tempfile
    fails = 0
    scratch = tempfile.mkdtemp(prefix="mt_selftest_")
    saved_paths = (MEM, FRONTIER_ROWS, FRONTIER_ROW_LIST, _ROW_IDS)
    saved_deny = (HARD_DENY, SOFT_DENY)
    deny_file = os.path.join(scratch, "deny.json")
    with io.open(deny_file, "w", encoding="utf-8") as f:
        json.dump({"hard": r"\b(widgets?|gizmos?|sprockets?)\b", "soft": r"\b(shelf|shelves)\b"}, f)
    HARD_DENY, SOFT_DENY = load_deny(deny_file)
    MEM = os.path.join(scratch, "memory")
    FRONTIER_ROWS = os.path.join(scratch, "rows")
    FRONTIER_ROW_LIST, _ROW_IDS = os.path.join(scratch, "no_row_list.txt"), None
    os.makedirs(MEM)
    os.makedirs(os.path.join(FRONTIER_ROWS, "T109"))
    for slug, desc in POS_CONTROLS + NEG_CONTROLS + (SUCCESSOR,):
        with io.open(os.path.join(MEM, slug + ".md"), "w", encoding="utf-8") as f:
            f.write(_control_file(slug, desc))
    tmp = os.path.join(scratch, "store.sqlite3")
    try:
        print("--- rule controls: the labelled positives must be AUTO or QUEUE, the negatives SKIP")
        for s, _d in POS_CONTROLS:
            tier, reason = classify(s, _front(_read(s))[0])
            ok = tier in ("AUTO", "QUEUE")
            fails += (not ok)
            print("  %-5s %-5s %-50s %s" % ("ok" if ok else "FAIL", tier, s[:50], reason[:40]))
        for s, _d in NEG_CONTROLS:
            tier, reason = classify(s, _front(_read(s))[0])
            ok = tier == "SKIP"
            fails += (not ok)
            print("  %-5s %-5s %-50s %s" % ("ok" if ok else "FAIL", tier, s[:50], reason[:40]))
        print("--- frontier-row guard: a verified t### memory with a rows/T### folder is QUEUE, without one it stays SKIP")
        row_head = "[VERIFIED] T109 hard-core Z^2: coexistence for lambda > 4.93828, every cell checked twice"
        for slug, status, want in (("t109_frontier_row_control", "verified", "QUEUE"),
                                   ("t109_frontier_row_control", "provisional", "QUEUE"),
                                   ("t109_frontier_row_control", None, "SKIP"),
                                   ("t500_other_label_control", "verified", "SKIP"),
                                   ("t999_no_such_row_control", "verified", "SKIP"),
                                   ("frontier_row_suffix_control_t109_x", "verified", "QUEUE"),
                                   ("ab10_t500_other_label_control", "verified", "SKIP"),
                                   ("frontier_row_suffix_control_t109_x", None, "SKIP")):
            tier, reason = classify(slug, row_head, status)
            ok = tier == want
            fails += (not ok)
            print("  %-5s %-5s %-11s %-50s %s" % ("ok" if ok else "FAIL", tier, status, slug[:50], reason[:40]))
        print("--- the deny file: its words deny, the rest passes; no file denies nothing; a broken file stops")
        for text, want in (("the widget count", True), ("gizmos on the shelf", True), ("a sprocket", True),
                           ("the map 2x+1 on Z", False), ("(3+sqrt21)/6 = 1.26376 (root of 3x^2-3x-1)", False),
                           ("the paper calls it the octave", False), ("widgetry", False)):
            hit = bool(HARD_DENY.search(text))
            ok = hit == want
            fails += (not ok)
            print("  %-5s %-5s %s" % ("ok" if ok else "FAIL", "deny" if hit else "pass", text))
        h0, s0 = load_deny(os.path.join(scratch, "absent.json"))
        ok = not h0.search("widget") and not s0.search("shelf")
        fails += (not ok)
        print("  %-5s no deny file -> both lists match nothing" % ("ok" if ok else "FAIL"))
        bad_file = os.path.join(scratch, "bad_deny.json")
        with io.open(bad_file, "w", encoding="utf-8") as f:
            f.write('{"hard": "(unclosed"}')
        try:
            load_deny(bad_file)
            ok = False
        except SystemExit:
            ok = True
        fails += (not ok)
        print("  %-5s a deny file that does not compile stops the transport" % ("ok" if ok else "FAIL"))
        tier, reason = classify("shelf_lemma_selftest", "THEOREM: the shelf lemma holds for every finite graph; proved by "
                                "induction on the vertices.", "verified")
        ok = tier != "AUTO"
        fails += (not ok)
        print("  %-5s %-5s a soft word keeps a result out of AUTO (%s)" % ("ok" if ok else "FAIL", tier, reason[:40]))
        print("--- end to end on a fresh scratch store (no live store is read or touched)")
        try:
            sys.path.insert(0, BUILD_SRC)
            from math_brain.store import ResearchStore
            rs = ResearchStore(tmp)
            try:
                rs.connection.close()
            except Exception:
                pass
        except Exception as exc:
            print("  could not create a scratch store with math_brain from %s (%s: %s) - counted as a failure"
                  % (BUILD_SRC, type(exc).__name__, exc))
            print("SELFTEST FAIL (%d failures)" % (fails + 1))
            return 1
        db = sqlite3.connect(tmp)
        n0 = db.execute("select count(*) from claims where payload_json like ?", ("%" + E2E_MARK + "%",)).fetchone()[0]
        db.close()
        print("  claims carrying %s before ingest = %d" % (E2E_MARK, n0))
        fails += (n0 != 0)
        slug = E2E_SLUG
        ok, cid = ingest(slug, store=tmp, rebuild=False)
        print("  ingest %s -> %s %s" % (slug[:40], ok, str(cid)[:30]))
        fails += (not ok)
        # INDEPENDENT read: a fresh sqlite connection, not the store API, not the ledger
        db = sqlite3.connect(tmp)
        n_claim = db.execute("select count(*) from claims where payload_json like ?", ("%" + E2E_MARK + "%",)).fetchone()[0]
        n_prov = db.execute("select count(*) from claim_provenance where source_ref=?", ("memory:" + slug,)).fetchone()[0]
        n_ev = db.execute("select count(*) from evidence where claim_id=?", (cid,)).fetchone()[0] if ok else 0
        n_node = db.execute("select count(*) from nodes where id=?", (cid,)).fetchone()[0] if ok else 0
        db.close()
        print("  independent read-back: claims carrying %s = %d, provenance rows = %d, evidence = %d, node = %d"
              % (E2E_MARK, n_claim, n_prov, n_ev, n_node))
        fails += (n_claim < 1) + (n_prov != 1) + (n_ev != 1) + (n_node != 1)
        # THE HOOK'S OWN READER must accept the card. Rows existing is not the same as the card being servable: the
        # hook's integrity gate drops a card whose claim and node disagree (claim_node_statement_mismatch).
        try:
            from math_brain.current_note import read_current_note, NoteReadError
            try:
                full = read_current_note(tmp, cid, artifact_root=None)
                print("  the hook's reader (read_current_note): PASS, binding %s" % full.get("claim_node_binding"))
            except NoteReadError as exc:
                print("  the hook's reader (read_current_note): REFUSED %s  <- the card would never be served" % exc)
                fails += 1
        except Exception as exc:
            print("  the hook's reader could not be run (%s) - counted as a failure" % type(exc).__name__)
            fails += 1
        # idempotent: the provenance row now exists, so a second ingest must refuse
        ok_again, why_again = ingest(slug, store=tmp, rebuild=False)
        print("  second ingest of the same slug -> %s: %s" % (ok_again, str(why_again)[:60]))
        fails += (ok_again is True)
        # the deny boundary: a theorem worded in the denied domain must be refused even when forced
        ok2, why = ingest(BOOK_SLUG, store=tmp, force=True, rebuild=False)
        print("  forced ingest of a denied-domain theorem -> %s: %s" % (ok2, str(why)[:80]))
        fails += (ok2 is True)
        ok3, why3 = ingest(BRAIN_TEST_SLUG, store=tmp, rebuild=False)
        print("  ingest of a brain-test memory -> %s: %s" % (ok3, str(why3)[:80]))
        fails += (ok3 is True)
        # REVISIONS: the memory is read through a stand-in _read so its description can grow, shrink and come back
        real_read = _read
        base_text = real_read(slug)
        base_desc = _front(base_text)[0]

        def with_desc(new_desc):
            return base_text.replace(base_desc, new_desc, 1)

        try:
            print("--- revisions on the scratch store")
            grown = base_desc + " Also PROVED: the same constant under every product measure (selftest line)."
            _read = lambda s_, _t=with_desc(grown): _t if s_ == slug else real_read(s_)   # noqa: E731
            rv = [r for r in revisions(store=tmp) if r[0] == slug]
            print("  grown description -> %s" % ([(r[1], r[2][:60]) for r in rv],))
            fails += not (len(rv) == 1 and rv[0][1] == "AUTO")
            ok_r, new_cid = revise(slug, store=tmp, rebuild=False, why="selftest")
            print("  revise -> %s %s" % (ok_r, str(new_cid)[:30]))
            fails += (not ok_r)
            db = sqlite3.connect(tmp)
            n_edge = db.execute("select count(*) from edges where source_id=? and target_id=? and kind='supersedes'",
                                (new_cid, cid)).fetchone()[0] if ok_r else 0
            db.close()
            heads = transported_heads(slug, tmp)
            print("  independent read-back: supersedes edge new->old = %d, transported heads = %s" % (n_edge, [h for h, _ in heads]))
            fails += (n_edge != 1) + (not (len(heads) == 1 and heads[0][0] == new_cid))
            try:
                from math_brain.current_note import read_current_note
                note = read_current_note(tmp, cid, artifact_root=None)
                print("  the hook's reader asked for the OLD claim serves %s (revision_changed=%s)"
                      % (str(note.get("current_id"))[:30], note.get("revision_changed")))
                fails += not (note.get("current_id") == new_cid and note.get("revision_changed") is True)
            except Exception as exc:
                print("  the hook's reader failed on the revised family (%s)" % exc)
                fails += 1
            print("  same description again -> %s" % [r[1] for r in revisions(store=tmp) if r[0] == slug])
            fails += bool([r for r in revisions(store=tmp) if r[0] == slug])
            ok_again, why_again = revise(slug, store=tmp, rebuild=False)
            print("  revise again with nothing changed -> %s: %s" % (ok_again, str(why_again)[:60]))
            fails += (ok_again is True)
            _read = lambda s_, _t=with_desc(base_desc[:max(40, len(base_desc) // 3)]): _t if s_ == slug else real_read(s_)   # noqa: E731
            rv = [r for r in revisions(store=tmp) if r[0] == slug]
            print("  shrunk description -> %s" % ([(r[1], r[2][:60]) for r in rv],))
            fails += not (len(rv) == 1 and rv[0][1] == "QUEUE")
            # a typed refinement is never revised by the rule
            db = sqlite3.connect(tmp)
            db.execute("update claim_provenance set source_kind='campaign' where claim_id=?", (new_cid,))
            db.commit()
            db.close()
            rv = [r for r in revisions(store=tmp) if r[0] == slug]
            print("  the head re-marked as a typed refinement -> %s" % [r[1] for r in rv])
            fails += bool(rv)
            # CORRECT: the memory is overtaken (a successor names it wrong); an agent's correction supersedes its head
            succ = SUCCESSOR[0]
            over = base_text.replace("metadata:", "metadata:\n  superseded_by: %s" % succ, 1)
            _read = lambda s_, _t=over: _t if s_ == slug else real_read(s_)   # noqa: E731
            st_before = [x for x in stale_in_store(tmp) if x[1] == slug]
            ok_c, c_cid = correct(slug, "selftest correction: the constant claimed in this memory is withdrawn; see the successor.", store=tmp, rebuild=False)
            st_after = [x for x in stale_in_store(tmp) if x[1] == slug]
            print("  correct an overtaken memory's claim -> %s %s; stale before %d, after %d"
                  % (ok_c, str(c_cid)[:30], len(st_before), len(st_after)))
            fails += (not ok_c) + (len(st_before) != 1) + (len(st_after) != 0)
            ok_c2, why_c2 = correct(slug, "selftest correction: the constant claimed in this memory is withdrawn; see the successor.", store=tmp, rebuild=False)
            print("  correct it again -> %s: %s" % (ok_c2, str(why_c2)[:60]))
            fails += (ok_c2 is True)
        finally:
            _read = real_read
        # HOLD: while a hold is in force a run writes nothing - not the store, not the ledger, not the state file.
        # Every path the run could write is pointed into the scratch folder first, so a broken hold cannot reach a
        # live store; the scratch store must come out with the same claim count and no state file may appear.
        print("--- hold on the scratch store")
        saved = (HOLD, STORE, LEDGER, QUEUE, STATE)
        hd = os.path.join(scratch, "hold")
        os.makedirs(hd)
        HOLD, STORE = os.path.join(hd, "HOLD.json"), tmp
        LEDGER, QUEUE, STATE = os.path.join(hd, "ledger.jsonl"), os.path.join(hd, "queue.jsonl"), os.path.join(hd, "state.json")
        try:
            print("  no hold file -> in force: %s" % hold_state()[0])
            fails += hold_state()[0]
            json.dump({"until": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time() + 3600)), "by": "selftest",
                       "why": "control", "set_epoch": time.time()}, io.open(HOLD, "w", encoding="utf-8"))
            held_now = hold_state()[0]
            db = sqlite3.connect(tmp)
            n_before = db.execute("select count(*) from claims").fetchone()[0]
            db.close()
            rc_run = run()
            db = sqlite3.connect(tmp)
            n_after = db.execute("select count(*) from claims").fetchone()[0]
            db.close()
            wrote = [f for f in (STATE, LEDGER, QUEUE) if os.path.exists(f)]
            print("  hold in force: %s; run -> rc %s, claims %d -> %d, files written %s" % (held_now, rc_run, n_before, n_after, wrote))
            fails += (not held_now) + (rc_run != 0) + (n_after != n_before) + bool(wrote)
            rc_cli = main(["correct", slug, "a correction the hold must refuse, long enough to pass the length rule"])
            print("  a manual correct under the hold -> exit %s" % rc_cli)
            fails += (rc_cli != 3)
            json.dump({"until": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time() - 60)), "by": "selftest",
                       "why": "lapsed", "set_epoch": time.time() - 3600}, io.open(HOLD, "w", encoding="utf-8"))
            print("  a lapsed hold -> in force: %s" % hold_state()[0])
            fails += hold_state()[0]
            json.dump({"until": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time() + 30 * 3600)), "by": "selftest",
                       "why": "too long", "set_epoch": time.time()}, io.open(HOLD, "w", encoding="utf-8"))
            print("  a hold longer than %.0f h -> in force: %s" % (HOLD_MAX_H, hold_state()[0]))
            fails += hold_state()[0]
        finally:
            HOLD, STORE, LEDGER, QUEUE, STATE = saved
    finally:
        MEM, FRONTIER_ROWS, FRONTIER_ROW_LIST, _ROW_IDS = saved_paths
        HARD_DENY, SOFT_DENY = saved_deny
        shutil.rmtree(scratch, ignore_errors=True)
    print("SELFTEST %s (%d failures)" % ("PASS" if not fails else "FAIL", fails))
    return 0 if not fails else 1


def _extend_vecs():
    """A claim without a vector shuts the meaning channel for every prompt (math_sense names nobody while one is
    missing), and a hand ingest between runs would leave it closed until the next run. Every hand write that adds a
    claim embeds it, as run does."""
    try:
        sys.path.insert(0, HERE)
        import math_claim_vecs
        n_vec, _total, _note = math_claim_vecs.extend(STORE)
        print("claim vectors: +%d, %d in the file%s" % (n_vec, _total, (" - " + _note) if _note else ""))
    except Exception as exc:
        print("claim vectors: not extended (%s: %s)" % (type(exc).__name__, exc))


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    # a slug read from a CRLF list by bash arrives as "slug\r"; no memory slug carries whitespace
    argv = [a.strip() for a in argv]
    cmd = argv[0]
    if cmd in ("ingest", "ingest-many", "revise", "correct"):
        held, h = hold_state()
        if held:
            print("refused: the store is HELD until %s by %s (%s); ask them, or wait"
                  % (h.get("until"), h.get("by"), h.get("why", "")[:100]))
            return 3
        # the write itself runs under the lock with the hold read again, as in `run`
        if len(argv) >= 2 and not _MANUAL_GATED:
            try:
                with _gated_write():
                    _MANUAL_GATED.append(cmd)
                    try:
                        return main(argv)
                    finally:
                        _MANUAL_GATED.clear()
            except HeldMidRun as exc:
                h = exc.args[0] if exc.args else {}
                print("refused: the store is HELD until %s by %s (%s); ask them, or wait"
                      % (h.get("until"), h.get("by"), str(h.get("why", ""))[:100]))
                return 3
            except TimeoutError as exc:
                print("refused: %s; try again" % exc)
                return 1
    if cmd == "scan":
        scan()
        return 0
    if cmd == "run":
        return run(dry="--dry" in argv, full="--full" in argv)
    if cmd == "ingest" and len(argv) >= 2:
        ok, what = ingest(argv[1], force="--force" in argv)
        now = time.strftime("%Y-%m-%dT%H:%M:%S")
        _append(LEDGER, {"ts": now, "slug": argv[1], "tier": "MANUAL", "action": "ingested" if ok else "failed",
                         "claim_id": what if ok else "", "reason": "" if ok else what})
        if ok:
            _append(QUEUE, {"ts": now, "slug": argv[1], "action": "ingested"})
        print(("ingested %s as %s" % (argv[1], what)) if ok else ("NOT ingested: %s" % what))
        if ok:
            _extend_vecs()
        return 0 if ok else 1
    if cmd == "ingest-many" and len(argv) >= 2:
        # `ingest` rebuilds the whole prefilter per slug, minutes each on a large store, so a shell loop of queued
        # verdicts runs for hours and a timeout can kill one between its store write and its ledger row. One lock, every slug written with the rebuild deferred, then one rebuild and one vector pass,
        # as `run` does. The file holds one slug a line; blank lines and '#' lines are skipped.
        with io.open(argv[1], encoding="utf-8-sig") as f:
            slugs = [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]
        n_ok = 0
        for s in slugs:
            ok, what = ingest(s, force="--force" in argv, rebuild=False)
            now = time.strftime("%Y-%m-%dT%H:%M:%S")
            _append(LEDGER, {"ts": now, "slug": s, "tier": "MANUAL", "action": "ingested" if ok else "failed",
                             "claim_id": what if ok else "", "reason": "" if ok else what})
            if ok:
                _append(QUEUE, {"ts": now, "slug": s, "action": "ingested"})
                n_ok += 1
            print(("ingested %s as %s" % (s, what)) if ok else ("NOT ingested %s: %s" % (s, what)), flush=True)
        if n_ok:
            rebuild_prefilter()
            _extend_vecs()
        print("ingest-many: %d of %d ingested" % (n_ok, len(slugs)))
        return 0 if n_ok == len(slugs) else 1
    if cmd == "hold" and len(argv) >= 4:
        until = argv[1]
        try:
            t_until = time.mktime(time.strptime(until[:19], "%Y-%m-%dT%H:%M:%S"))
        except Exception:
            print("hold: the time must read YYYY-MM-DDTHH:MM:SS (local time)")
            return 2
        if t_until - time.time() > HOLD_MAX_H * 3600 or t_until <= time.time():
            print("hold: the time must be in the next %.0f hours" % HOLD_MAX_H)
            return 2
        # under the write lock: a run's write in progress finishes first, and every later write of it sees the hold
        try:
            with _write_lock():
                rec = {"until": until[:19], "by": argv[2], "why": " ".join(argv[3:]),
                       "set_at": time.strftime("%Y-%m-%dT%H:%M:%S"), "set_epoch": time.time()}
                tmp = HOLD + ".tmp"
                json.dump(rec, io.open(tmp, "w", encoding="utf-8"))
                os.replace(tmp, HOLD)
                _append(LEDGER, {"ts": rec["set_at"], "slug": "", "tier": "MANUAL", "action": "hold", "reason": "until %s by %s: %s" % (rec["until"], rec["by"], rec["why"])})
        except TimeoutError as exc:
            print("hold: NOT set - %s; try again" % exc)
            return 1
        print("store held until %s by %s" % (rec["until"], rec["by"]))
        return 0
    if cmd == "release":
        if os.path.exists(HOLD):
            os.remove(HOLD)
            _append(LEDGER, {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "slug": "", "tier": "MANUAL", "action": "release", "reason": " ".join(argv[1:])})
            print("hold released")
        else:
            print("no hold")
        return 0
    if cmd == "correct" and len(argv) >= 3:
        ok, what = correct(argv[1], " ".join(argv[2:]))
        now = time.strftime("%Y-%m-%dT%H:%M:%S")
        _append(LEDGER, {"ts": now, "slug": argv[1], "tier": "MANUAL", "action": "corrected" if ok else "failed",
                         "claim_id": what if ok else "", "reason": "correction of an overtaken memory's claim" if ok else what})
        print(("corrected %s: new claim %s supersedes its head(s)" % (argv[1], what)) if ok else ("NOT corrected: %s" % what))
        if ok:
            _extend_vecs()
        return 0 if ok else 1
    if cmd == "revisions":
        for slug, action, reason, heads, old_len, new_len, sha in revisions():
            print("%-5s %-70s %s" % (action, slug[:70], reason))
        return 0
    if cmd == "revise" and len(argv) >= 2:
        rt = "--retitle" in argv
        words = [a for a in argv[2:] if a != "--retitle"]
        ok, what = revise(argv[1], why="an agent's verdict: " + (" ".join(words) or "revise"), retitle=rt)
        now = time.strftime("%Y-%m-%dT%H:%M:%S")
        _append(LEDGER, {"ts": now, "slug": argv[1], "tier": "MANUAL", "action": "revised" if ok else "failed",
                         "claim_id": what if ok else "", "reason": "revision" if ok else "revision: " + what})
        if ok:
            _append(QUEUE, {"ts": now, "slug": argv[1], "action": "revised"})
        print(("revised %s as %s" % (argv[1], what)) if ok else ("NOT revised: %s" % what))
        if ok:
            _extend_vecs()
        return 0 if ok else 1
    if cmd in ("dismiss-revision", "dismiss") and len(argv) >= 3 and (cmd == "dismiss-revision" or
                                                                      str(queued().get(argv[1], {}).get("reason", "")).startswith("REVISED MEMORY")):
        # keep the store's claim for THIS description; a later change of the memory queues again
        now = time.strftime("%Y-%m-%dT%H:%M:%S")
        sha = _desc_sha(strip_head(_front(_read(argv[1]))[0])[:1500])
        _append(QUEUE, {"ts": now, "slug": argv[1], "action": "revision_dismissed", "why": " ".join(argv[2:])})
        _append(LEDGER, {"ts": now, "slug": argv[1], "tier": "MANUAL", "action": "revision_dismissed", "desc_sha": sha,
                         "reason": " ".join(argv[2:])})
        print("kept the store's claim for %s (description %s)" % (argv[1], sha))
        return 0
    if cmd == "dismiss" and len(argv) >= 3:
        now = time.strftime("%Y-%m-%dT%H:%M:%S")
        _append(QUEUE, {"ts": now, "slug": argv[1], "action": "dismissed", "why": " ".join(argv[2:])})
        _append(LEDGER, {"ts": now, "slug": argv[1], "tier": "MANUAL", "action": "dismissed", "reason": " ".join(argv[2:])})
        print("dismissed %s" % argv[1])
        return 0
    if cmd == "status":
        return status()
    if cmd == "provrows":   # each one: math_recall it, then ingest --force or dismiss with the reason
        for s in provisional_rows_uncarried():
            print("%-5s %s" % (classify(s, _front(_read(s))[0], "provisional")[0], s))
        return 0
    if cmd == "rowlist":    # one gh call: the row folders of a repo's rows tree, written to FRONTIER_ROW_LIST
        import subprocess
        src = os.environ.get("MATH_TRANSPORT_ROWS_REPO", "").strip().strip("/")   # owner/repo/path/to/rows
        if src.count("/") < 2:
            print("rowlist: set MATH_TRANSPORT_ROWS_REPO to owner/repo/path/to/rows")
            return 2
        owner_repo, path = "/".join(src.split("/")[:2]), "/".join(src.split("/")[2:])
        out = subprocess.run(["gh", "api", "repos/%s/contents/%s" % (owner_repo, path),
                              "--jq", '.[] | select(.type == "dir") | .name'], capture_output=True, text=True)
        ids = sorted({ln.strip() for ln in out.stdout.splitlines() if re.match(r"^T\d{3}$", ln.strip())})
        if out.returncode != 0 or not ids:
            print("rowlist: no row folders read (%s); %s left as it was" % (out.stderr.strip()[:200], FRONTIER_ROW_LIST))
            return 1
        tmp = FRONTIER_ROW_LIST + ".tmp"
        with io.open(tmp, "w", encoding="utf-8") as f:
            f.write("\n".join(ids) + "\n")
        os.replace(tmp, FRONTIER_ROW_LIST)
        print("rowlist: %d rows (%s .. %s) -> %s" % (len(ids), ids[0], ids[-1], FRONTIER_ROW_LIST))
        return 0
    if cmd == "selftest":
        return selftest()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
