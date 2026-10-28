# -*- coding: utf-8 -*-
"""mutate.py - one-line faults for literature proofs. Every operator changes exactly ONE step of a proof at
exactly ONE place and records what it did (operator, step, the text before and after, the span). The bank
builder picks operators per proof; this module only proposes and applies them.

Operators are grouped by the fault mechanism they plant, and each carries a prior tier for "the mutated proof
is really invalid" (A: almost always - a flipped inequality, a swapped quantifier, a reversed limit; B: usually -
a dropped hypothesis, a swapped mode of convergence, a swapped theorem name, a changed constant). The tier is
a prior, not a certificate: the bank quotes a hand-read validity rate per operator beside every result.

    python mutate.py --demo proofs.jsonl --n 8 --seed 1      # print mutations for eyeballing
"""
import argparse
import io
import json
import random
import re

# ----------------------------------------------------------------------------- math-mode helpers
MATH_SPAN = re.compile(
    r"\\begin\{(?:equation|align|gather|multline|eqnarray|alignat|flalign)\*?\}.*?\\end\{(?:equation|align|gather|multline|eqnarray|alignat|flalign)\*?\}"
    r"|\\\[.*?\\\]|\$\$.*?\$\$|\\\(.*?\\\)|\$(?:[^$\\]|\\.)+\$", re.S)


def math_spans(step):
    return [(m.start(), m.end()) for m in MATH_SPAN.finditer(step)]


def in_math(step, pos):
    return any(a <= pos < b for a, b in math_spans(step))


def _occurrences(step, pattern, need_math=None):
    """[(start, end, matched_text)] of pattern occurrences, filtered by math-mode requirement."""
    out = []
    for m in re.finditer(pattern, step):
        if need_math is None or in_math(step, m.start()) == need_math:
            out.append((m.start(), m.end(), m.group(0)))
    return out


# ----------------------------------------------------------------------------- operator table
# (name, mechanism, tier, need_math, pattern, replacement function)
def _swap_table(pairs):
    table = {}
    for a, b in pairs:
        table[a] = b
        table[b] = a
    return table


INEQ = _swap_table([(r"\leq", r"\geq"), (r"\le", r"\ge"), (r"\leqslant", r"\geqslant"), (r"\lesssim", r"\gtrsim"),
                    (r"\ll", r"\gg")])
LIMOPS = _swap_table([(r"\limsup", r"\liminf"), (r"\sup", r"\inf"), (r"\max", r"\min")])
SETOPS = _swap_table([(r"\cup", r"\cap"), (r"\bigcup", r"\bigcap"), (r"\subseteq", r"\supseteq"),
                      (r"\subset", r"\supset"), (r"\subseteq", r"\supseteq")])
QUANT = _swap_table([(r"\forall", r"\exists")])
WORDS_A = _swap_table([("at most", "at least"), ("increasing", "decreasing"), ("non-increasing", "non-decreasing"),
                       ("nonincreasing", "nondecreasing"), ("for all", "for some"), ("for every", "for some"),
                       ("sufficiently large", "sufficiently small"), ("large enough", "small enough"),
                       ("positive", "negative"), ("upper", "lower"), ("finite", "infinite"),
                       ("countable", "uncountable"), ("bounded above", "bounded below"), ("maximum", "minimum"),
                       ("maximal", "minimal"), ("supremum", "infimum"), ("larger", "smaller"),
                       ("greater", "smaller"), ("above", "below"), ("nonnegative", "nonpositive"),
                       ("non-negative", "non-positive"), ("convex", "concave"), ("submartingale", "supermartingale"),
                       ("subadditive", "superadditive"), ("subharmonic", "superharmonic"), ("recurrent", "transient"),
                       ("dominates", "is dominated by"), ("tends to zero", "tends to infinity")])
WORDS_B = {   # one-directional swaps: a hypothesis or a mode of convergence weakened or altered
    "independent of": "uncorrelated with", "independent from": "uncorrelated with", "independent": "uncorrelated",
    "almost everywhere": "in measure", "uniformly integrable": "integrable",
    "uniformly": "pointwise", "square-integrable": "integrable", "martingale": "submartingale",
    "in $L^2$": "in $L^1$", "in $L^p$": "in $L^1$", "in distribution": "in probability",
    "compact": "closed", "continuous": "measurable", "Lipschitz": "continuous",
    "irreducible": "aperiodic", "ergodic": "stationary", "stationary": "ergodic", "i.i.d.": "identically distributed",
    "exchangeable": "identically distributed", "adapted": "measurable", "predictable": "adapted",
    "stopping time": "random time", "with probability one": "with positive probability",
    "with positive probability": "with probability one", "positive measure": "measure zero",
    "finite measure": "infinite measure", "finite variance": "infinite variance", "finite mean": "infinite mean",
    "finite expectation": "infinite expectation",
}
# the mode of convergence is swapped only where it names a mode: "converges a.s." -> "converges in probability"
MODE_RE = re.compile(r"(?<![A-Za-z])((?:converge[sd]?|convergence|holds?|hold|tends?)\s+)(almost surely|a\.s\.\\?|almost everywhere|in probability|in distribution|in law)(?![A-Za-z])")
MODE_SWAP = {"almost surely": "in probability", "a.s.": "in probability", "a.s.\\": "in probability",
             "almost everywhere": "in measure", "in probability": "in distribution", "in distribution": "in probability",
             "in law": "in probability"}
DROP = ("independent", "bounded", "uniformly", "integrable", "finite", "continuous", "nonnegative", "non-negative",
        "increasing", "uniformly integrable", "square-integrable",
        "measurable", "compact", "positive", "Lipschitz", "monotone", "decreasing", "symmetric", "centered",
        "mean-zero", "mean zero", "closed", "open", "connected", "irreducible", "aperiodic", "recurrent")
# one-directional citation mismatches: the replacement result does NOT deliver what the step uses
THEOREMS = {
    "Fatou's lemma": "the dominated convergence theorem", "Fatou's theorem": "the dominated convergence theorem",
    "Fatou": "dominated convergence", "strong law of large numbers": "central limit theorem",
    "weak law of large numbers": "central limit theorem",
    "Markov's inequality": "Chebyshev's inequality", "Chebyshev's inequality": "Markov's inequality",
    "Cauchy-Schwarz": "Jensen", "Cauchy--Schwarz": "Jensen", "Cauchy–Schwarz": "Jensen",
    "Jensen's inequality": "Markov's inequality", "monotone convergence": "dominated convergence",
    "Borel-Cantelli": "Fubini", "Borel--Cantelli": "Fubini", "Borel–Cantelli": "Fubini",
    "Doob's maximal inequality": "Doob's optional stopping theorem", "optional stopping": "martingale convergence",
    "law of large numbers": "central limit theorem", "central limit theorem": "law of large numbers",
    "It\\^o's formula": "Girsanov's theorem", "It\\^o formula": "Girsanov theorem", "Itô's formula": "Girsanov's theorem",
    "Azuma": "Hoeffding", "Slutsky": "Prokhorov", "Kolmogorov's": "Doob's", "Burkholder": "Doob",
    "Donsker": "Skorokhod", "Portmanteau": "Skorokhod", "Cram\\'er": "Chernoff", "Cramér": "Chernoff",
    "Stirling": "Wallis", "Harris": "BK", "FKG": "BK", "BK": "Harris", "Chernoff": "Chebyshev",
    "Bernstein": "Chebyshev", "Talagrand": "Chebyshev", "McDiarmid": "Chebyshev",
}
LIMIT_TARGET = _swap_table([(r"\to 0", r"\to \infty"), (r"\to0", r"\to\infty"), (r"\rightarrow 0", r"\rightarrow \infty"),
                            (r"\to +\infty", r"\to 0"), (r"\to -\infty", r"\to +\infty")])


def _regex_for_keys(keys, word=True):
    ks = sorted(keys, key=len, reverse=True)
    body = "|".join(re.escape(k) for k in ks)
    if word:
        return r"(?<![A-Za-z\\])(?:" + body + r")(?![A-Za-z])"
    return r"(?:" + body + r")(?![A-Za-z])"


OPS = []
VOWEL = "aeiouAEIOU"


def op(name, mechanism, tier, need_math):
    def deco(fn):
        OPS.append((name, mechanism, tier, need_math, fn))
        return fn
    return deco


# each candidate function returns [(start, end, replacement)] positions in the step
def _left_is_range_bound(step, s):
    """'1 \\le j \\le m', '0<t<T': an inequality whose left neighbour is a bare number is an index range; flipping it
    makes a nonsense range rather than a mathematical error, so those occurrences are skipped."""
    left = step[max(0, s - 24):s]
    return re.search(r"(?:^|[\s{(\[,=$])\d+(?:\.\d+)?\s*(?:(?:\\(?:leqslant|geqslant|leq|geq|le|ge)|[<>])\s*[A-Za-z](?:_\{?[A-Za-z0-9]+\}?)?\s*)?$", left) is not None


@op("ineq_flip", "inequality_direction", "A", True)
def c_ineq(step):
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(INEQ, word=False), True):
        if _left_is_range_bound(step, s):
            continue
        out.append((s, e, INEQ[t]))
    # bare < and > (not inside \langle/\rangle or << >>); require spaces or letters/digits around
    spans = math_spans(step)
    for m in re.finditer(r"(?<=[A-Za-z0-9)}\]\s])([<>])(?=[\s0-9A-Za-z(\\{])", step):
        if in_math(step, m.start()) and step[m.start() - 1:m.start()] not in "<>" and step[m.end():m.end() + 1] not in "<>=":
            if _left_is_range_bound(step, m.start()):
                continue
            # '<x, y>' written with bare brackets is an inner product, not an inequality: skip a span that pairs them
            span = next(((a, b) for a, b in spans if a <= m.start() < b), None)
            if span and re.search(r"<[^<>$]{1,80}>", step[span[0]:span[1]]):
                continue
            out.append((m.start(), m.end(), ">" if m.group(1) == "<" else "<"))
    return out


@op("limop_swap", "extremum_or_limit_operator", "A", True)
def c_limop(step):
    return [(s, e, LIMOPS[t]) for s, e, t in _occurrences(step, _regex_for_keys(LIMOPS, word=False), True)]


@op("setop_swap", "set_operation_direction", "A", True)
def c_setop(step):
    return [(s, e, SETOPS[t]) for s, e, t in _occurrences(step, _regex_for_keys(SETOPS, word=False), True)]


@op("quantifier_swap", "quantifier", "A", True)
def c_quant(step):
    return [(s, e, QUANT[t]) for s, e, t in _occurrences(step, _regex_for_keys(QUANT, word=False), True)]


@op("limit_target", "limit_value", "A", True)
def c_limit(step):
    return [(s, e, LIMIT_TARGET[t]) for s, e, t in _occurrences(step, _regex_for_keys(LIMIT_TARGET, word=False), True)]


@op("index_shift", "off_by_one", "A", True)
def c_index(step):
    out = []
    for m in re.finditer(r"([A-Za-z])\s*([+-])\s*1(?![0-9.])", step):
        if in_math(step, m.start()):
            other = "-" if m.group(2) == "+" else "+"
            out.append((m.start(2), m.end(), other + "1"))
    return out


@op("word_flip", "direction_word", "A", False)
def c_words_a(step):
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(WORDS_A), False):
        # a hyphenated compound ("maximum-density inequality", "upper-tail") is a name, not a direction claim
        if step[e:e + 1] == "-" or step[max(0, s - 1):s] == "-":
            continue
        out.append((s, e, WORDS_A[t]))
    return out


@op("hypothesis_swap", "hypothesis_weakened", "B", False)
def c_words_b(step):
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(WORDS_B), False):
        # "Lipschitz constant", "compact support", "stationary distribution": a noun phrase that names a quantity,
        # not a hypothesis on an object - swapping the adjective there garbles the sentence instead of the argument
        if re.match(r"\s+(?:constants?|support(?:ed)?|distributions?|measures?|norms?|seminorms?|modulus|moduli)\b", step[e:e + 16]):
            continue
        if t in ("adapted", "predictable") and not re.match(r"\s+(?:process|processes|to|sequence|sequences|and|,|random|integrand|integrands)\b", step[e:e + 14]):
            continue   # "adapted from [citation]" is the verb, not the filtration hypothesis
        if step[max(0, s - 1):s] == "-" or step[e:e + 1] == "-":
            continue   # "continuous-BV change of variables": a hyphenated name, not a hypothesis
        if t.startswith("independent") and re.search(r"[A-Za-z]+ly\s+$", step[max(0, s - 16):s]):
            continue   # "affinely independent", "linearly independent": a fixed term, not a probabilistic hypothesis
        rep = WORDS_B[t]
        if t.endswith(".") and step[e:e + 2] == "\\ ":
            e += 1   # "i.i.d.\ holding" -> the control space after the abbreviation goes with it
        art = re.search(r"(?:^|\s)(an?)\s$", step[max(0, s - 4):s])
        if art and rep and rep[0].isalpha():
            want = "an" if rep[0] in VOWEL else "a"
            if art.group(1) != want:
                out.append((s - len(art.group(1)) - 1, e, want + " " + rep))
                continue
        out.append((s, e, rep))
    for m in MODE_RE.finditer(step):
        if not in_math(step, m.start()):
            mode = m.group(2)
            out.append((m.start(2), m.end(2), MODE_SWAP.get(mode, "in probability")))
    return out


@op("hypothesis_drop", "hypothesis_dropped", "B", False)
def c_drop(step):
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(DROP), False):
        # only drop an adjective that precedes a noun-ish word (so the sentence stays grammatical)
        after = step[e:e + 40]
        m = re.match(r"\s+(random|variable|function|sequence|process|set|measure|martingale|family|"
                     r"increments|domain|operator|kernel|subset|sample|Markov|chain|walk|graph|matrix|"
                     r"sequence|variables|functions|processes|sets|measures|families|increment|"
                     r"and|,|in|on|with|for)\b", after)   # not "of": "independent of X" -> "of X" is no sentence
        if t == "uniformly" and re.match(r"\s+(?:in|on|over|for|with|w\.r\.t\.|with respect)\b", after):
            continue   # "uniformly in nu" -> "in nu" is no sentence; the phrase would have to go as a whole
        if m or t == "uniformly":
            nxt = m.group(1) if m else ""
            if nxt in ("measure", "measures") and t in ("positive", "finite", "nonnegative", "non-negative"):
                continue   # "has positive measure" -> "has measure" is not a sentence; hypothesis_swap covers it
            if re.search(r"(?:[A-Za-z]+ly|not|non-|non|almost|path|arc|simply|totally)\s*$", step[max(0, s - 24):s]):
                continue   # "strictly increasing", "algebraically closed" -> a dangling adverb, not an error
            if step[max(0, s - 1):s] == "-" or step[e:e + 1] == "-":
                continue   # "representative-independent": a hyphenated compound is one word
            if nxt in ("in", "on", "with", "for") and re.search(r"\b(?:is|are|be|being|been|was|were)\s+$", step[max(0, s - 8):s]):
                continue   # "are centered with unit variance" -> "are with": predicative adjective, no sentence without it
            e2 = e + 1 if step[e:e + 1] == " " else e
            s2 = s
            rep = ""
            # "independent and centered" -> "centered"; "continuous, and compactly" -> "compactly"
            if nxt == "and":
                e2 = e + m.end()
                e2 = e2 + 1 if step[e2:e2 + 1] == " " else e2
            elif nxt == ",":
                e2 = e + m.end()
                e2 = e2 + 1 if step[e2:e2 + 1] == " " else e2
            # keep the article right: "an open domain" -> "a domain"; "a bounded operator" -> "an operator"
            art = re.search(r"(?:^|\s)(an?)\s$", step[max(0, s - 4):s])
            if art and nxt and nxt not in ("and", ",", "in", "on", "with", "of", "for"):
                want = "an" if nxt[0] in VOWEL else "a"
                if art.group(1) != want:
                    s2 = s - len(art.group(1)) - 1
                    rep = want + " "
            out.append((s2, e2, rep))
    return out


CITE_CONTEXT = re.compile(r"^(?:'s)?\s+(?:inequality|inequalities|lemma|theorem|bound|formula|criterion|estimate|"
                          r"argument|principle|identity|representation|decomposition)\b")


@op("theorem_swap", "citation_mismatch", "B", False)
def c_theorem(step):
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(THEOREMS), False):
        # a bare name (Harris, Azuma, Chernoff, ...) is a citation only when a result word follows it
        if not re.search(r"'s|inequality|lemma|theorem|formula|convergence|stopping|numbers", t):
            if not CITE_CONTEXT.match(step[e:e + 24]):
                continue
        if step[e:e + 2] == "'s" and not t.endswith("'s"):
            continue   # "Fatou's theorem": the possessive form is its own key
        out.append((s, e, THEOREMS[t]))
    return out


@op("const_change", "constant_or_exponent", "B", True)
def c_const(step):
    out = []
    for m in re.finditer(r"\^\{?(2|3|4|1/2|1/4|-1|-2)\}?(?![0-9])", step):
        if in_math(step, m.start()):
            cur = m.group(1)
            new = {"2": "3", "3": "2", "4": "2", "1/2": "1/4", "1/4": "1/2", "-1": "-2", "-2": "-1"}[cur]
            out.append((m.start(1), m.end(1), new))
    for m in re.finditer(r"(?<![0-9.\^_{])\b(2|4|8|16)\b(?![0-9.}])", step):
        if in_math(step, m.start()) and step[m.start() - 1:m.start()] not in "^_":
            cur = m.group(1)
            new = {"2": "4", "4": "2", "8": "4", "16": "8"}[cur]
            out.append((m.start(1), m.end(1), new))
    return out


@op("sign_flip", "sign", "B", True)
def c_sign(step):
    out = []
    for m in re.finditer(r"(?<=[A-Za-z0-9)}\]])\s*([+-])\s*(?=[A-Za-z0-9(\\{])", step):
        if in_math(step, m.start()) and "\\to" not in step[max(0, m.start() - 4):m.start()]:
            out.append((m.start(1), m.end(1), "-" if m.group(1) == "+" else "+"))
    return out


@op("ineq_to_eq", "inequality_strengthened", "B", True)
def c_ineq_eq(step):
    out = []
    for s, e, t in _occurrences(step, r"\\(?:leq|le|geq|ge|leqslant|geqslant)(?![A-Za-z])", True):
        if _left_is_range_bound(step, s):
            continue
        out.append((s, e, "="))
    return out


OP_INDEX = {o[0]: o for o in OPS}


# 2026-09-06 13:0x (F4's hand-read of 61 items, three mechanical invalid classes; the interim haiku none arm scored
# hypothesis_drop 0/3 and hypothesis_swap 0/2): a hypothesis word that the CLAIM or an EARLIER step already grants
# ("independent" stated in the theorem, dropped from step 3) is not a fault site - the proof still has it, the
# solver cannot see an error, and the item is keyed flawed while being effectively clean. Guarded operators skip a
# site whose removed head word occurs as a whole word in the claim or in any earlier step. Applies to NEW items only
# (the bank is monotonic); the checkpoint-C validity read measures the difference.
REGRANT_GUARDED_OPS = ("hypothesis_drop", "hypothesis_swap")


def _regranted(removed, claim, earlier):
    head = re.sub(r"[^A-Za-z-]", " ", (removed or "").lower()).split()
    head = [w for w in head if w not in ("and", "a", "an", "the")]
    if not head:
        return False
    ctx = (claim or "") + " " + " ".join(earlier or [])
    return bool(re.search(r"(?<![A-Za-z-])" + re.escape(head[0]) + r"(?![A-Za-z-])", ctx, re.I))


def candidates(steps, ops=None, claim=""):
    """[(op, step_index, start, end, replacement)] over all steps."""
    out = []
    for name, mech, tier, need_math, fn in OPS:
        if ops and name not in ops:
            continue
        for i, st in enumerate(steps):
            try:
                for s, e, rep in fn(st):
                    if st[s:e] == rep:
                        continue
                    if name in REGRANT_GUARDED_OPS and _regranted(st[s:e], claim, steps[:i]):
                        continue
                    out.append((name, i, s, e, rep))
            except Exception:
                continue
    return out


def apply(steps, cand):
    name, i, s, e, rep = cand
    st = steps[i]
    new = st[:s] + rep + st[e:]
    new = re.sub(r"  +", " ", new)
    out = list(steps)
    out[i] = new
    return out, {"op": name, "mechanism": OP_INDEX[name][1], "tier": OP_INDEX[name][2], "step": i + 1,
                 "before": st[max(0, s - 40):e + 40], "after": new[max(0, s - 40):s + len(rep) + 40],
                 "removed": st[s:e], "inserted": rep}


def choose(steps, rng, n=2, exclude_ops=(), tier_first=True, avoid_steps=(), claim=""):
    """Pick up to n candidates with distinct (op, step) pairs, tier A before B, spread over steps."""
    cands = [c for c in candidates(steps, claim=claim) if c[0] not in exclude_ops and (c[1] + 1) not in avoid_steps]
    if not cands:
        return []
    rng.shuffle(cands)
    if tier_first:
        cands.sort(key=lambda c: 0 if OP_INDEX[c[0]][2] == "A" else 1)
    picked = []
    used_steps, used_ops = set(), set()
    for c in cands:
        if c[1] in used_steps or c[0] in used_ops:
            continue
        picked.append(c)
        used_steps.add(c[1])
        used_ops.add(c[0])
        if len(picked) >= n:
            break
    return picked


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", required=True)
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    rows = [json.loads(l) for l in io.open(a.demo, encoding="utf-8") if l.strip()]
    rows = [r for r in rows if r.get("accept")]
    rng = random.Random(a.seed)
    rng.shuffle(rows)
    shown = 0
    for r in rows:
        picks = choose(r["steps"], rng, n=1)
        if not picks:
            continue
        new, info = apply(r["steps"], picks[0])
        print("=====", r["paper"], r["kind"], "step", info["step"], "of", r["n_steps"], "|", info["op"], info["tier"])
        print("  BEFORE:", info["before"].replace("\n", " "))
        print("  AFTER :", info["after"].replace("\n", " "))
        shown += 1
        if shown >= a.n:
            break


if __name__ == "__main__":
    main()
