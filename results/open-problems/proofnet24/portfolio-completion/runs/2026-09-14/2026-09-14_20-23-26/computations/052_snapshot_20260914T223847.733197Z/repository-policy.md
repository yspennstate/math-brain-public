# Math Open Problems Research Hub

This private repository is the canonical GitHub archive for ongoing mathematical open-problem research carried out by Yitzchak Shmalo and connected research agents.

## Canonical archival policy

All scheduled agents and research workflows working on mathematical open problems should preserve their substantive work in this repository in addition to any other durable copies (for example ChatGPT Library and Google Drive).

For every substantive run, preserve the **actual complete research output**, not only an email or summary. This includes:

- exact problem statement and hypotheses;
- derivations and equations;
- proved lemmas and dependency chains;
- conditional claims and unresolved obligations;
- counterexamples and disproved intermediate claims;
- failed approaches and why they failed;
- computations, certificates, scripts and limitations;
- literature/source checks;
- peer-agent audits;
- cumulative PROVED / CONDITIONAL / DISPROVED / OPEN ledger;
- timestamp and task/track identifier.

Email is a delivery mechanism, **not** the canonical research archive. A failed email must never cause mathematical work to be lost.

## Preferred layout

New scheduled-task output should normally go under:

```text
proofnet24/
  <track>/
    README.md                 # stable problem statement / current roadmap
    ledger.md                 # cumulative claim ledger when maintained
    runs/
      YYYY-MM-DD/
        YYYY-MM-DD_HH-MM-SS__run-report.md
    artifacts/                # code, exact certificates, supporting text
```

Existing historical material in the repository should be preserved in place. Do not reorganize or delete legacy research merely to conform to this layout.

## Write rules for agents

1. **Append history; do not erase it.** Every run report gets a new timestamped file. Never overwrite a previous run report.
2. Stable cumulative files such as `ledger.md` or a track `README.md` may be updated, but the timestamped run that caused the update must also be committed.
3. Use a commit message such as `ProofNet24 <track>: archive <timestamp>`.
4. Before writing, fetch the current target path/branch and avoid destructive or conflicting writes.
5. If the exact problem already has a dedicated folder, use it. Otherwise create `proofnet24/<track>/`.
6. Never push unrelated personal email, credentials, secrets, medical/private material, or non-research correspondence.
7. For manuscripts or PDFs, keep the original/source artifact when available and also preserve supporting Markdown/LaTeX/proof notes where practical.
8. A mathematical claim is not considered solved merely because an agent writes `PROVED`; retain audits and dependencies so the proof can be independently checked.

## Current shared destination

Repository: `yspennstate/math-open-problems`

Default branch: `master`

Visibility: **private**

This repository is intended to remain the durable, version-controlled research hub for the open-problem program.

