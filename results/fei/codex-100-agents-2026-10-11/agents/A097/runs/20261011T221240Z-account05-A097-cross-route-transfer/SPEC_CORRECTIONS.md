# Frozen-spec arithmetic correction

BLOCK_FROZEN_SPEC.json declared 3,684 cases. The domain was correctly fixed as all truth tables in dimensions 1-3, every nonempty block, two references. The implementation executed that identical domain, whose count is 2[4(1)+16(3)+256(7)]=3,688. The n=1 truth-table count is 4, not 2. This is a count transcription error, not a search expansion or mathematical failure. The original spec is retained unchanged and the actual output supplies the executed count.

After the successful tree check, one never-executed dead debug expression was removed from check_transfer.py; no arithmetic or test domain changed. The final helper is rerun to bind final source and result hashes.
