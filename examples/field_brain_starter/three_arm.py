"""A ten-question three-arm test of a small brain: does recall help an agent answer?

Arms, same model and same question each time:
  brain  - the prompt carries what recall.py prints for the question (records found by search)
  docs   - the prompt carries every record in the folder, unranked (the "just paste the notes" baseline)
  none   - the prompt carries the question alone

    python three_arm.py --write-prompts out/          # write 30 prompt files to read or send by hand
    python three_arm.py --model-cmd "my-cli --stdin"  # send each prompt on stdin, grade what comes back

Grading is deliberately crude: an answer passes when, for every group in the question's any_of list, it contains
at least one of the group's phrases (case-insensitive). Read the failing answers yourself before trusting a score.
The docs arm is easy on twenty records and gets harder as the store grows; the brain arm is the one that scales.
Questions marked "absent" have no answer in the store, and the right reply says so. The echo test (a "model" that
returns its prompt) scores the docs arm 10/10 by construction - it checks the plumbing, not the grader.
"""
import argparse
import json
import os
import re
import shlex
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recall  # noqa: E402

ASK = "Answer the question in one or two sentences. If the notes cannot answer it, say so plainly.\n\n"


def brain_context(recs, q):
    best = recall.bm25(recs, q)
    for slug, r in recs.items():
        if r["meta"].get("superseded_by"):
            best[slug] *= 0.5
    ranked = [k for s, k in sorted(((s, k) for k, s in best.items() if s > 0), reverse=True)[:4]]
    out = []
    for k in ranked:
        m = recs[k]["meta"]
        tag = " (SUPERSEDED by %s)" % m["superseded_by"] if m.get("superseded_by") else ""
        out.append("[%s, %s%s]\n%s" % (k, m.get("status", "?"), tag, recs[k]["body"]))
    return "Notes found by recall:\n\n" + "\n\n".join(out) + "\n\n" if out else "Recall found no notes.\n\n"


def docs_context(recs):
    return "All notes:\n\n" + "\n\n".join("[%s]\n%s" % (k, r["body"]) for k, r in recs.items()) + "\n\n"


def passes(answer, item):
    a = answer.lower()
    return all(any(re.search(r"(?<![a-z0-9])" + re.escape(p.lower()) + r"(?![a-z0-9])", a) for p in group)
               for group in item["any_of"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=os.environ.get("BRAIN_MEM_DIR", os.path.join(HERE, "memory")))
    ap.add_argument("--questions", default=os.path.join(HERE, "questions.json"))
    ap.add_argument("--write-prompts")
    ap.add_argument("--model-cmd")
    ap.add_argument("--timeout", type=int, default=300)
    a = ap.parse_args()
    if not (a.write_prompts or a.model_cmd):
        ap.error("give --write-prompts DIR or --model-cmd CMD")
    recs = recall.load(a.dir)
    with open(a.questions, encoding="utf-8") as fh:
        items = json.load(fh)
    arms = {"brain": lambda q: brain_context(recs, q), "docs": lambda q: docs_context(recs), "none": lambda q: ""}
    score = {k: 0 for k in arms}
    for item in items:
        for arm, ctx in arms.items():
            prompt = ASK + ctx(item["question"]) + "Question: " + item["question"] + "\n"
            if a.write_prompts:
                os.makedirs(a.write_prompts, exist_ok=True)
                with open(os.path.join(a.write_prompts, "%s_%s.txt" % (item["id"], arm)), "w", encoding="utf-8") as fh:
                    fh.write(prompt)
            if a.model_cmd:
                try:
                    res = subprocess.run(shlex.split(a.model_cmd), input=prompt, capture_output=True, text=True,
                                         encoding="utf-8", timeout=a.timeout)
                    answer = res.stdout
                except subprocess.TimeoutExpired:
                    answer = ""
                ok = passes(answer, item)
                score[arm] += ok
                print("%s %-5s %s  %s" % (item["id"], arm, "PASS" if ok else "fail", " ".join(answer.split())[:100]))
    if a.model_cmd:
        print("\n" + "  ".join("%s %d/%d" % (k, v, len(items)) for k, v in score.items()))
    if a.write_prompts:
        print("wrote %d prompts to %s" % (len(items) * len(arms), a.write_prompts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
