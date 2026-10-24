# -*- coding: utf-8 -*-
"""One Codex worker (gpt-6.1-sol, max reasoning, fast tier, acc2) turns our written probability results that have no
math-brain node yet into one mathbrain-draft-v1 bundle (claude-322bc92e, 10 Oct 2026, T-20261010-052: "add nodes to
the brain for the problems we solve"). Windowless and detached; claude-322bc92e audits the bundle against the attempt
files before integrate_drafts.py --only codex-prob1000-nodes-1010 takes it in."""
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "~/math-brain-inbox/codex-prob1000-nodes-1010"
ATT = "~/<private-repo>/06_math_research"
FILES = [
    "probability_1000_attempts_I_20260914/Probability_F0059_Janson_problem_18_39_reduction_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_F0063_Janson_conjecture_20_1_level_widths_uniformly_integrable_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_F0064b_Janson_problems_20_3_20_4_20_11_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_H0013_H0014_random_drift_destroys_compactness_for_every_delta_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_H0019_layer_distribution_of_random_recursive_trees_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_H0020_Neri_Pinto_urn_contractivity_fails_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_H0024_frog_model_critical_line_factor_four_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_I0024_relaxation_time_is_not_a_linear_program_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_I0031_distance_regular_hitting_times_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_I0033_coalescing_on_the_cycle_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_I0082_free_strong_unimodality_cauchy_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_I0086_free_brownian_unimodality_sharp_constant_2026-09-14.md",
    "probability_1000_attempts_I_20260914/Probability_I0095_sign_matrix_discrepancy_exact_small_values_2026-09-14.md",
]
PROMPT = """You are a Codex worker on the probability open-problems campaign. Work yourself; no child agents.

Task: turn our own written results into math-brain nodes. Read the spec ~/math-brain-inbox/BUNDLE_SPEC.md
in full, then read each attempt record below (all under %s) and the ledger rows in
%s/SOLVED_NEEDS_NODE.jsonl (status and verification wording per problem id).

%s

For each record that contains a result (an answer, a counterexample, a refutation, a proved special case or a reduction),
write entries of a single draft bundle: kind theorem or lemma with a complete proof_text taken from the record (shorten
only by dropping repetition; never invent a step), or kind concept for a reduction or a partial answer with no complete
proof. The statement must be self-contained (define every symbol, name the source problem by its author, problem number
and arXiv id or journal) and must begin with the bracket "[campaign result 2026-09-14, <verification wording from the
record or ledger row>]" so the reader knows it is author-checked and unrefereed. Namespace probability.<area>; logical
names lowercase-kebab and specific (for example janson-problem-18-39-reduction). source: the problem's source paper (its
arXiv id or DOI as source_id, url) with license "owner-own-work (campaign result, attributed)". Add relations from each
result to its source problem's node key if you create one (kind cites) and between results that depend on each other.
Skip a record whose result is only that the problem is solved in the literature, and skip any record whose own text says
the claim was retracted. Read every record before writing.

Write the bundle COMPLETE to bundle_001.json.part in the current directory, then rename it to bundle_001.json. Then
print one line per entry: key, kind, problem id. Change nothing else on disk.
""" % (ATT, HERE, "\n".join("- " + f for f in FILES))


def main():
    os.makedirs(OUT, exist_ok=True)
    exe = (glob.glob(os.path.expanduser("~/AppData/Roaming/npm/node_modules/@openai/codex/**/x86_64-pc-windows-msvc/bin/codex.exe"),
                     recursive=True) or ["codex.cmd"])[0]
    env = dict(os.environ, CODEX_HOME="~/.codex-img-acc2")
    cmd = [exe, "exec", "--skip-git-repo-check", "-m", "gpt-6.1-sol", "-c", 'model_reasoning_effort="max"',
           "-c", 'service_tier="fast"', "-C", OUT,   # the home's own danger-full-access: workspace-write is read-only on Windows (08:51 run blocked)
           "--output-last-message", os.path.join(OUT, "LAST_MESSAGE.txt"), "-"]
    log = open(os.path.join(OUT, "drafter.log"), "ab")
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=log, stderr=subprocess.STDOUT, cwd=OUT, env=env,
                         creationflags=0x08000000 | 0x00004000 | 0x00000008)   # no window, below normal, detached
    p.stdin.write(PROMPT.encode("utf-8"))
    p.stdin.close()
    print("drafter pid %d; output %s" % (p.pid, OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
