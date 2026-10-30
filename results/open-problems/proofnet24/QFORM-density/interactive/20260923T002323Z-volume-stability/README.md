# Quadratic-form volume stability and useful-worker plan

The full universal density conjecture is **not proved** by this package. Independent review of the new supporting proofs is pending.

Start with REPORT.md for the dimension-free perturbation certificate. PEER_TAIL_EXTENSION.md applies fleet01/B20's actual tail identity to a bound using two substantial singular directions and collective weak directions. WORK_PLAN.md in the distributed package is the current eighty-worker instruction preserved from the brain; publication is not proof that every worker has adopted it. Its canonical brain path and hash are in MANIFEST.json. DELIVERY_EVIDENCE.json gives a complete, carefully scoped comparison of all eighty archive-slot trees.

To rerun the finite checks with Python 3.10+ and NumPy:

    python check_stability.py
    python check_tail.py

These scripts check exact identities numerically and finite examples. They do not certify the general analytic theorem or the unrestricted conjecture. Their actually executed outputs are supplied in the two result JSON files; rerunning may change floating-point formatting or last digits.

All seven mathematical/evidence source files were read back at math-open-problems commit c2414ef633b9d4b7f04a83e1aeefbe713ed82bba and their Git blob hashes match the distributed files. The distributed WORK_PLAN.md likewise matches the brain handoff at a830e7f6edc52b772c1e826b284b99217b9e910d. The existing latest-Claude directive was updated and read back at fd707d78db4ce7e7f3fdb4373525b9472cb6829e. Exact paths and SHA-256 hashes are in MANIFEST.json.

