$env:PYTHONIOENCODING='utf-8'
$q = Start-Process -FilePath python -ArgumentList 'brain_bulk_C006_codex_ledger.py','11','2' -NoNewWindow -PassThru -RedirectStandardOutput c006b.out -RedirectStandardError c006b.err; $q.PriorityClass='BelowNormal'; $q.WaitForExit(); $q.ExitCode
