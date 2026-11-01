STUCK: Git rejected new-file metadata combined with the requested old a/path header (exit 128 for both new files: expected /dev/null).

Resolved by retaining the requested plain review diffs and providing standard Git creation variants named *.apply.diff. validate_delivery.py checks both reconstructed content and git apply --check in an empty local directory. No live file was changed.
