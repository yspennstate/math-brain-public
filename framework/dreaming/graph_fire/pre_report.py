#!/usr/bin/env python3
"""pre_report.py - fire the gut on the OUTGOING message, before a wrong number/claim reaches the owner.

The hooks see tool I/O, never the assistant's prose - so the single worst class (a flattering/undershoot
number reported to the owner, an over-claimed 'done') had no firing surface. The correction this was
built from was exactly that shape: a replay reported at a yearly rate roughly an order of magnitude
under what the lived ledger showed, with sim_flatters AND risk_vs_lived_record both silent because the
number lived in prose. reality_monitor.py already proved a Stop hook can read the last assistant message and
block; this adds the number-vs-lived-book check that reality_monitor doesn't do.

Two signals, combined:
  1. GRAPH FIRE (gfcore): the outgoing text is graph-near a sim/risk scar (fires sim_sign_vs_lived_nav /
     sim_flatters / risk_vs_his_book / leveraged_etf_is_not_linear).
  2. LIVED-ANCHOR MISMATCH: a reported $ figure (with a period) contradicts one of his stated book numbers
     by >2x in EITHER direction, when the text names that anchor's subject. Undershoot is as damning as
     flatter - 'a sim that disagrees with the lived book in either direction is lying' (MISTAKES.md 07-11).

check() returns the fires + a should_block flag. Used by the Stop hook and the shadow eval. Fail-safe.
"""
import os, io, json, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ANCHORS = os.path.join(HERE, "lived_anchors.json")

# a money figure: either $N[suffix] (suffix optional when $ is present), OR N+REQUIRED-scale-suffix with no
# $ ('180k', '180 thousand', '1.8M') - agents write dollar amounts without the sign and those must not
# evade the lived-book check. A BARE number with neither $ nor a scale suffix ('180', '85%') never matches.
_MONEY = re.compile(r"\$\s*([\d][\d,]*(?:\.\d+)?)\s*(k|thousand|m|mn|mm|million|b|bn|billion|grand)?"
                    r"|(?<![\w.$])([\d][\d,]*(?:\.\d+)?)\s*(k|thousand|m|mn|mm|million|bn|billion|grand)\b", re.I)
_MULT = {"k": 1e3, "thousand": 1e3, "grand": 1e3, "m": 1e6, "mn": 1e6, "mm": 1e6, "million": 1e6,
         "b": 1e9, "bn": 1e9, "billion": 1e9}
_PERIODS = [
    ("year", re.compile(r"(per year|/ ?yr|/ ?year|a year|annual|per annum|yearly)", re.I)),
    ("month", re.compile(r"(per month|/ ?mo\b|a month|monthly|/ ?month)", re.I)),
    ("day", re.compile(r"(per day|/ ?day|a day|daily)", re.I)),
]
# the number must be ASSERTED as a P&L figure near the reported value (real analysis prose MENTIONS
# ledger figures and data sizes constantly; only a headline assertion 'the grid EARNS $X/yr' should block).
_ASSERT = re.compile(r"\b(earns?|earned|makes?|made|nets?|netted|generat\w+|profit|p\s?&\s?l|pnl|yields?|"
                     r"brings? in|rakes? in|pulls? in|took? in|(?:comes?|came) to|total(?:s|ed|led)?|adds? up to|"
                     r"book (makes|earns))\b", re.I)
_HEDGE = re.compile(r"\b(should|might|may|probably|likely|i think|i believe|appears?|seems?|roughly|about|"
                    r"approximately|estimate|ballpark|order of|not sure|unverified|assuming|if .* correct|"
                    r"need to (check|verify|reconcile)|haven'?t (verified|checked|reconciled))\b", re.I)
# a SOURCE marker: the figure names where it was read from (a ledger/observer/file/command), or is flagged
# plainly as unverified. Generous by design - any plausible provenance phrase passes; the unsourced-assert
# branch must only catch a bare asserted number with no provenance at all (fail open on ambiguity).
_SRC = re.compile(r"\b(sourced?[d]?\s*(:|from)|per (the|his|its|that)\b|from (the|that|its) (\w+[ -]){0,2}"
                  r"(ledger|log|tape|file|run|db|feed|journal|account|statement|observer|engine|export|card|cache|output)|"
                  r"as measured|measured (on|from|by|in|over)|verified against|reconciled? (against|with|to)|"
                  r"read (from|off|out of)|according to|reported by|logged (in|by)|the (output|result) (of|shows?)|"
                  r"data incomplete|\bledger says|\btape shows|\bshows?\b[^.]{0,40}\$)", re.I)
# a concrete artifact reference doubles as provenance: a windows/posix path, a *.py/md/json/tsv/jsonl/log
# name, or a `backticked` artifact near the prose.
_ARTIFACT = re.compile(r"[A-Za-z]:\\[\w\\.\-]+|/[\w./\-]+\.(?:py|md|json|tsv|jsonl|log|csv|npz)\b|"
                       r"\b[\w.\-]+\.(?:py|md|json|tsv|jsonl|log|csv|npz)\b|`[^`]{3,60}`")
# a strong COMPLETION claim about an artifact he will open - the he_will_look class. reality_monitor.py
# owns 'it works/deployed/tests pass'; this covers the sibling vocabulary it doesn't (finalized, populated,
# removed, shipped). Deliberately NOT bare 'done' (too common); needs a completion verb.
_DONE = re.compile(r"\b(finali[sz]ed|populated|(is|it'?s|we'?re|are|all) done|removed|deleted|completed|"
                   r"shipped|ready to ship|good to go|all set|fully (working|implemented|populated)|"
                   r"exhibits? (are )?(in|populated|filled)|everything is (in|there|populated))\b", re.I)

_ANCHORS_CACHE = None


def _s(t):
    """Coerce any input to a safe string - the Stop path must never throw on odd input."""
    return t if isinstance(t, str) else ("" if t is None else str(t))


def _load_anchors():
    global _ANCHORS_CACHE
    if _ANCHORS_CACHE is None:
        try:
            d = json.load(io.open(ANCHORS, encoding="utf-8"))
            out = []
            for a in d.get("anchors", []):
                # A remembered observation is not a present-tense oracle. The 07-12 correction explicitly
                # retired the recent-grid/account3/walk-forward magnitudes: their frames differ and some are
                # contaminated. Hard blocking is opt-in only, so a copied or newly added number cannot become
                # live merely by existing in this file.
                if a.get("blocking_oracle") is not True:
                    continue
                for pk, period in (("value_usd_per_year", "year"), ("value_usd_per_month", "month"),
                                   ("value_usd_per_day", "day")):
                    if pk in a:
                        v = a[pk]
                        lo, hi = (v if isinstance(v, list) else [v, v])
                        out.append({"keys": [k.lower() for k in a.get("match", [])],
                                    "period": period, "lo": float(lo), "hi": float(hi),
                                    "src": a.get("source", ""), "key": a.get("key", "")})
                        break
            _ANCHORS_CACHE = out
        except Exception:
            _ANCHORS_CACHE = []
    return _ANCHORS_CACHE


def _to_usd(num, unit):
    try:
        v = float(num.replace(",", ""))
        return v * _MULT.get((unit or "").lower(), 1.0)
    except Exception:
        return None


def _find_money(text):
    """List of (usd, period) reported figures. period is 'year'/'month'/'day' or None."""
    out = []
    try:
        t = _s(text)
        for m in _MONEY.finditer(t):
            num = m.group(1) or m.group(3)   # $-branch or suffix-branch
            unit = m.group(2) or m.group(4)
            usd = _to_usd(num, unit)
            if usd is None or usd < 1000:  # ignore tiny/plainly-non-book numbers
                continue
            # the period must be ATTACHED to the number - an asserted RATE ('205k/year', '180k per year',
            # '18k a day') - not a loose 'year' 40 chars away, which is a mention in analysis prose (the
            # 0.75%-false-block source). The recorded undershoot was an attached rate, '~$N-Nk/year'.
            fwd = t[m.end():m.end() + 10]
            period = None
            for pname, pre in _PERIODS:
                if pre.search(fwd):
                    period = pname
                    break
            out.append((usd, period, m.start()))
    except Exception:
        pass
    return out


def anchor_mismatches(text):
    """Reported figures contradicting an explicitly promoted blocking oracle. Fail-safe -> []."""
    flags = []
    try:
        tl = _s(text).lower()
        money = _find_money(text)
        if not money:
            return []
        for a in _load_anchors():
            for usd, period, pos in money:
                if period != a["period"]:
                    continue
                # the anchor SUBJECT (grid/account3) must be NEAR the number, not just somewhere in a long
                # message - that separates 'the grid ... $Nk/year' (a real undershoot) from analysis prose
                # that mentions 'grid' once and a different number far away (the false-block source).
                if not any(k in tl[max(0, pos - 80):pos + 45] for k in a["keys"]):
                    continue
                # >4x gap, not 2x: real analysis prose discusses his numbers at 2-3x sub-quantities all the
                # time (a 7yr total, a sub-period); only an EGREGIOUS miss (the 10x grid undershoot) should
                # block. The attached-rate period detection (above) already gates out loose mentions.
                if usd < 0.25 * a["lo"] or usd > 4.0 * a["hi"]:
                    direction = "UNDER" if usd < a["lo"] else "OVER"
                    flags.append({
                        "reported": usd, "anchor_lo": a["lo"], "anchor_hi": a["hi"],
                        "period": period, "direction": direction, "anchor": a["key"] or a["src"],
                    })
    except Exception:
        pass
    # dedup identical
    seen, out = set(), []
    for f in flags:
        k = (round(f["reported"]), f["anchor"], f["direction"])
        if k not in seen:
            seen.add(k)
            out.append(f)
    return out


# his-book context: a statistic only contradicts HIS book if it's actually about his book/strategy
_BOOKCTX = re.compile(r"\b(book|strateg(?:y|ies)|grid|portfolio|leverag|delta.?neutral|\bnav\b|the account|account\d|"
                      r"backtest|his (book|strategy|return)|the (book|strategy))\b", re.I)
_LOSS_SIGN = re.compile(r"\b(los(e|es|ing|s)\b|negative return|unprofitable|loses? money|in the red|"
                        r"bleeding money|down every (year|month)|lost money (every|each))\b", re.I)
_DD_CTX = re.compile(r"draw.?down|drop|loss|lose|decline|crash|ruin|wipe|blow.?up|down\b", re.I)


def stat_sanity(text):
    """Structural sanity of reported STATISTICS against his lived book - the classes beyond raw $ that he
    corrects most: a drawdown far worse than his lived worst (-11%), a P&L SIGN contradicting his profitable
    NAV, an implausible Sharpe. Gated on book-context so a generic stats discussion doesn't fire. Fail-safe."""
    flags = []
    try:
        t = _s(text)
        if not _BOOKCTX.search(t):
            return []
        tl = t.lower()
        # drawdown: a STRONG drawdown phrase within ~28 chars of a >=40% figure. His lived worst windowed
        # maxDD is -11%, so a 40%+ drawdown claim is the naive-worst-case-scaling error he corrects; the
        # tight phrase+proximity+magnitude keeps ordinary '30% of X' analysis prose from tripping it.
        _ddp = r"draw.?down|max.?dd|\bmaxdd\b|drew down|draws? down|drawn down|blow.?up|wiped? out|near.?ruin"
        for m in re.finditer(r"(\d{2,3})(?:\s*(?:to|-)\s*(\d{2,3}))?\s*%", t):
            val = max(int(m.group(1)), int(m.group(2)) if m.group(2) else int(m.group(1)))
            near = tl[max(0, m.start() - 28):m.end() + 8]
            if val >= 40 and re.search(_ddp, near):
                flags.append({"kind": "drawdown", "reported_pct": val, "lived_worst_pct": 11,
                              "reflex": "risk_vs_his_book"})
                break
        # sign contradiction: his lived strategy reported LOSING. Tight (real analysis prose mentions
        # backtests + losses constantly): needs an explicit money-loss AND a recurring temporal AND
        # attribution to HIS strategy/grid/book - all three, or it false-fires on ordinary discussion.
        if (re.search(r"los(e|es|ing)\s+money|unprofitable|negative (return|pnl|p&l)|loses? (money )?(every|each)|"
                      r"lost money (every|each)", tl)
                and re.search(r"every (single )?year|each year|annually|every month", tl)
                and re.search(r"\b(his|the|current)\s+(strateg(?:y|ies)|grid|book)|his book", tl)):
            flags.append({"kind": "sign", "reflex": "sim_sign_vs_lived_nav"})
        # implausible Sharpe
        m = re.search(r"sharpe\D{0,10}(\d+(?:\.\d+)?)", tl)
        if m:
            try:
                if float(m.group(1)) >= 5:
                    flags.append({"kind": "sharpe", "reported": float(m.group(1)), "reflex": "sim_flatters"})
            except Exception:
                pass
    except Exception:
        return []
    return flags


# recommending SHORT vol / selling options - he is long-gamma-only, buys puts, never sells options. This
# is his most-repeated restriction; a recommendation to sell/short/write/collect premium AS strategy is
# always wrong. Gated on a recommendation verb + guarded against negation ('never sells', 'only buys').
_SELL_VOL = re.compile(r"\b(sell|short|writ(e|ing)|collect|harvest)\w*\s+(?:\w+\s+){0,3}?"
                       r"(put|call|option|premium|vol|volatility|gamma|theta|straddle|strangle|condor|"
                       r"iron ?condor|credit spread)s?\b", re.I)
_REC = re.compile(r"\b(should|recommend|consider|could|suggest|propos|better to|worth|the (play|move|idea|"
                  r"answer) is|i'?d|we could|you could|instead\b)", re.I)
_NEG_VOL = re.compile(r"\b(never sell|not sell|doesn'?t sell|don'?t sell|won'?t sell|only buy|buys? (put|vol|"
                      r"gamma)|long gamma|rather than sell|instead of sell|not to sell|comparison|vs\.? (buy|sell))",
                      re.I)


# recommending a switch of the index leg to futures - a 07-11 correction: the leveraged-ETF carry is UNKNOWN
# pending actual-ledger reconciliation, so a 'move to futures' recommendation built on a proxy is premature.
_FUT_SWITCH = re.compile(r"\b(mov|switch|migrat|shift|go|swap)\w*\s+(?:\w+\s+){0,3}?(to|into|over to|for)\s+"
                         r"(?:\w+\s+){0,2}?(futures|nq\b|/nq|micro\s*(nq|nasdaq|futures)|es\s+futures)", re.I)
# calling a daily-reset leveraged/inverse ETF carry NEGLIGIBLE / just the expense ratio / a clean linear
# multiple - a recorded correction. The path term is material at the monthly scale; it is not linear.
_LEVETF = re.compile(r"\b(lev3s|lev3l|lev3a|lev3b|lev3c|lev3d|lev3u|leveraged etf|inverse etf|daily.?reset|-?3x etf|3x etf)\b", re.I)
_DISMISS = re.compile(r"\b(negligible|just (the )?expense|only (the )?expense|expense ratio (only|alone)|"
                      r"(roughly|basically|essentially|approximately|about)?\s*(a )?(clean )?linear|clean multiple|"
                      r"linear multiple|not much (carry|cost|drag)|minimal (carry|cost|drag)|"
                      r"(is|are|it'?s)\s+(basically |essentially |roughly )?(the )?expense ratio)\b", re.I)


def strategy_sanity(text):
    """Fire long_gamma_only on a RECOMMENDATION to sell/short vol (never his strategy; blocks), and
    leveraged_etf_is_not_linear on a 'move the index leg to futures' recommendation (surfaces, softer -
    futures is a legitimate instrument, the error is recommending it off a proxy). Fail-safe -> []."""
    try:
        t = _s(text)
        flags = []
        m = _SELL_VOL.search(t)
        # the recommendation verb must be RIGHT BEFORE the sell-vol phrase (a direct 'you should sell...'),
        # not just anywhere in a long analysis message that happens to mention 'short vol' and 'could'.
        if m and not _NEG_VOL.search(t) and _REC.search(t[max(0, m.start() - 42):m.start() + 3]):
            flags.append({"kind": "short_vol", "reflex": "long_gamma_only", "span": m.group(0)[:40]})
        fm = _FUT_SWITCH.search(t)
        if fm and _REC.search(t[max(0, fm.start() - 42):fm.start() + 3]):
            flags.append({"kind": "futures_switch", "reflex": "leveraged_etf_is_not_linear"})
        lm = _LEVETF.search(t)
        # the dismissal ('negligible'/'expense ratio') must be NEAR the leveraged-ETF mention (asserting IT
        # is negligible), not scattered in a message that discusses the ETF topic somewhere and 'linear'
        # elsewhere - the same proximity gate the other blockers use.
        if lm and _DISMISS.search(t[max(0, lm.start() - 35):lm.end() + 55]):
            flags.append({"kind": "levetf_dismiss", "reflex": "leveraged_etf_is_not_linear"})
        return flags
    except Exception:
        return []


# mention-vs-act gate (referee afec84b0, 2026-07-11): prose that DISCUSSES / attributes / retracts a wrong
# number ("we should NOT report X", "earlier I wrongly said X", "the old memory claimed X - retracted",
# "his correction: X is wrong") is NOT a fresh wrong report and must not block the number/drawdown/sign
# branches. Mistake-detection and correction turns are full of exactly this prose - blocking it is the
# ERN's own law (a guard that fires on correct discussion trains the reader to click past it). Errs toward
# gating: a blocker should fail OPEN on ambiguity. short_vol keeps its own _NEG_VOL guard, so it's not gated.
_DISCUSS = re.compile(
    r"\b(do|does|should|would|will|could|must)\s+not\s+(report|say|claim|present|tell|state)\b"
    r"|\b(don'?t|doesn'?t|shouldn'?t|wouldn'?t|won'?t|can'?t|couldn'?t|never)\s+(report|say|claim|present|tell|state)\b"
    r"|\b(wrongly|incorrectly|mistakenly|falsely)\s+(said|reported|claimed|stated|told)\b"
    r"|\b(the old memory|old anchor|earlier i|previously i|i wrongly|i earlier|i had (said|claimed|reported))\b"
    r"|\bretracted\b|\bwithdrawn\b|\bignore that\b|\bundershot\b|\bundershoot"
    r"|\bverified and cleared\b|\b(the )?(independent )?verifier (reproduced|confirms?|matched|checked)\b|"
    r"\breproduced every number\b"  # SPECIFIC verification-outcome phrasing (the number is being CHECKED) - narrow, not broad 'reconciled'/'reproduced', which the real undershoot's re-audit context also uses
    r"|\bthat('?s| was)?\s+(the|a|my|an)\s+[\w ]{0,20}(error|mistake)\b"
    r"|\b(his|the|a|my|your)\s+[\w'\- ]{0,20}correction\b|\bcorrection:\b"
    r"|\b(was|were|is|are)\s+wrong\b|\bnow (retracted|withdrawn|corrected|superseded)\b|\bflattering[- ]sim\b",
    re.I)


def check(text, session=None):
    """Combine graph-fire + lived-anchor mismatch + statistic/strategy sanity on outgoing prose. Fail-safe."""
    text = _s(text)
    try:
        sys.path.insert(0, HERE)
        import gfcore
        # Stop/prose surface fires once a turn on high-stakes output -> more sensitive than PreToolUse.
        gf = gfcore.graph_fire(text, session, thr_mult=0.55)
    except Exception:
        gf = []
    try:
        mism = anchor_mismatches(text)
    except Exception:
        mism = []
    SIMRISK = {"sim_flatters", "risk_vs_his_book", "sim_sign_vs_lived_nav", "leveraged_etf_is_not_linear"}
    strong = [f for f in gf if f.get("id") in SIMRISK]
    hedged = bool(_HEDGE.search(text or ""))
    money = _find_money(text)
    has_num = bool(money)
    # unsourced ASSERTED figure (2026-07-28, the owner's 'check the live feed before you report' class):
    # a money figure with an assertion verb attached ('the grid MAKES $274k') and NO provenance anywhere in
    # the message - no source phrase, no artifact/path reference, not hedged. The Stop hook combines this
    # with its observed-this-turn flag; here we only compute the text-side condition. Fail open: any source
    # marker or artifact mention anywhere in the message clears the whole flag.
    unsourced_assert = False
    try:
        if money and not hedged and not _SRC.search(text) and not _ARTIFACT.search(text):
            for _usd, _period, _pos in money:
                if _ASSERT.search(text[max(0, _pos - 60):_pos + 30]):
                    unsourced_assert = True
                    break
    except Exception:
        unsourced_assert = False
    # completion-claim path (the he_will_look class the graph tokens are too weak for): fire the reflex so
    # the Stop hook can nudge 'open the artifact he'll see before signing off'. Grounding/blocking is the
    # Stop hook's job (it has the transcript); here we only surface the reflex.
    if _DONE.search(text) and not hedged and not any(f.get("id") == "he_will_look" for f in gf):
        gf = list(gf) + [{"id": "he_will_look", "score": None, "charge": 1.0, "src": "MISTAKES",
                          "validity": "high", "mode": "fire", "via": "completion_claim"}]
    # block when the number provably contradicts his book, OR a strong sim/risk reflex fired on an
    # unhedged reported number. Hedged ('roughly', 'need to reconcile') never blocks - it's honest.
    try:
        stat = (stat_sanity(text) or []) + (strategy_sanity(text) or [])
    except Exception:
        stat = []
    for sflag in stat:
        rid = sflag.get("reflex")
        if rid and not any(f.get("id") == rid for f in gf):
            gf = list(gf) + [{"id": rid, "score": None, "charge": 1.0, "src": "MISTAKES",
                              "validity": "low", "mode": "fire", "via": "stat_sanity:" + sflag["kind"]}]
    # mention-vs-act suppression DISABLED 2026-07-11 (afec84b0, the cited referee) - it broke the guard's
    # INVARIANT (a wrong number never reaches the owner unblocked). This vocabulary gate opened a CONFIRMED
    # 3/5 false-negative hole: a FRESH wrong report carrying 'withdrawn / old memory / retracted / was wrong'
    # passed UNBLOCKED (referee_mention_fix_proto.py ADVERSARIAL dropped 5/5 -> 2/5). You cannot vocabulary-
    # discriminate mention-from-act - the two share surface. A missed wrong number defeats the guard's whole
    # purpose; the mention false-block it prevented is rare (0.03% on 13k real msgs) and recoverable. So
    # block-on-mism is the safe default. `discuss` stays computed for the returned dict/logging; it does NOT
    # suppress. Regression gate: referee_mention_fix_proto.py must show ADVERSARIAL 5/5 + ACT 5/5.
    # (Was: `if discuss: mism=[]; stat=[short_vol only]`. Rationale: memory referee_mention_vs_act_gate_2026_07_11.)
    discuss = bool(_DISCUSS.search(text))
    # short_vol is a directional recommendation error (wrong even when hedged - 'you might sell puts' is
    # still the wrong move); drawdown/sign respect the hedge (a hedged 'might draw ~30%' is honest).
    strat_block = [s for s in stat if s["kind"] == "short_vol"]
    stat_block = [s for s in stat if s["kind"] in ("drawdown", "sign", "levetf_dismiss")]
    # BLOCK only on PROVABLE issues (a number contradicting the book, a bad drawdown/sign, a sell-vol/levetf
    # claim) - NOT on 'a sim reflex fired near a number', which blocks CORRECT in-range numbers too. The sim
    # reflex still surfaces via graph_fires; it just doesn't force a block without a provable contradiction.
    should_block = bool(mism) or bool(strat_block) or (bool(stat_block) and not hedged)
    return {"graph_fires": gf, "mismatches": mism, "stat": stat, "strong": [f["id"] for f in strong],
            "hedged": hedged, "has_number": has_num, "discuss": discuss, "should_block": should_block,
            "unsourced_assert": unsourced_assert}


def _selftest():
    cases = [
        ("Running the grid backtest on the sample tape it earns roughly $180k per year.", False, "stale magnitude is not an oracle"),
        ("The grid backtest makes about $1.9M per year, in line with the book.", False, "recent magnitude is not an oracle"),
        ("His current strategy loses money every year.", True, "lived-sign contradiction"),
        ("He should sell puts and collect premium.", True, "long-gamma-only contradiction"),
        ("lev3s carry is basically the expense ratio, ~1% a year, negligible for the book.", "?", "levetf"),
        ("I read the module; it defines three helper functions.", False, "benign observation"),
        ("", False, "empty"),
    ]
    for txt, expect_block, note in cases:
        r = check(txt)
        print("  block=%-5s (want %s) [%-16s] fires=%s mism=%d :: %s"
              % (r["should_block"], expect_block, note, [f["id"] for f in r["graph_fires"][:3]],
                 len(r["mismatches"]), (txt[:40] + "...") if txt else "(empty)"))
    # unsourced-assert branch (2026-07-28): text-side condition only; the Stop hook adds observed-this-turn
    ua_cases = [
        ("The grid made $274k this month.", True, "bare asserted figure, no provenance"),
        ("The grid made $274k this month, from the fills ledger via the minute observer.", False, "sourced"),
        ("The grid made roughly $274k this month.", False, "hedged is honest"),
        ("pnl_minute_observer.py shows the grid made $274k this month.", False, "artifact named"),
        ("The backtest CAGR file has 3,000 rows and the fee is $12k per row of overhead.", False, "no assert verb near figure"),
        ("Costs came to $84k for the quarter.", True, "asserted total, no provenance"),
    ]
    bad = 0
    for txt, want, note in ua_cases:
        r = check(txt)
        got = bool(r.get("unsourced_assert"))
        flag = "ok" if got == want else "WRONG"
        bad += (got != want)
        print("  unsourced=%-5s (want %-5s) %-6s [%s] :: %s" % (got, want, flag, note, txt[:52]))
    if bad:
        print("unsourced-assert selftest FAILED (%d)" % bad)
        return 1
    for junk in [None, 123, {"x": 1}]:
        try:
            check(junk)
        except Exception as e:
            print("  FAIL-SAFE BREACH:", e)
            return 1
    print("pre_report selftest OK (fail-safe held)")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
