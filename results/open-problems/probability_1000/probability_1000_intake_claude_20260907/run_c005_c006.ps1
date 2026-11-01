$env:PYTHONIOENCODING='utf-8'
$p = Start-Process -FilePath python -ArgumentList 'brain_bulk_C005_techniques.py' -NoNewWindow -PassThru -RedirectStandardOutput c005.out -RedirectStandardError c005.err; $p.PriorityClass='BelowNormal'; $p.WaitForExit()
$q = Start-Process -FilePath python -ArgumentList 'brain_bulk_C006_codex_ledger.py','9' -NoNewWindow -PassThru -RedirectStandardOutput c006.out -RedirectStandardError c006.err; $q.PriorityClass='BelowNormal'; $q.WaitForExit(); $q.ExitCode
