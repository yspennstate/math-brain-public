# brain_midx_hourly.ps1 (2026-11-11, an agent): keep every pack of the brain clone inside the multi-pack-index.
# The clone is a blob:none partial clone; each fetch leaves one new promisor pack (about 90 an hour on 10-11 Nov) and
# a pack outside the index is searched one by one on every object lookup (fetch 62 s with ~600 outside, 11 Nov 07:35).
# The dream refreshes the index too (run_dream.ps1), but only when it runs. This writes the index only: no object moves,
# no pack is deleted. It skips when another writer holds the lock, and never removes a lock: a lock that stays for
# hours means its holder is starved at low priority (10-11 Nov: a repack's index writer sat Ready at BelowNormal for
# ten hours) - look at the holder's thread state, do not delete the lock.
$ErrorActionPreference = 'Continue'
$base = '~\.claude\dreaming'
$repo = '~\brain-repo'
$packDir = Join-Path $repo '.git\objects\pack'
$log = Join-Path $base 'brain_midx_hourly.log'
function Log([string]$m) {
    Add-Content -LiteralPath $log -Value ((Get-Date -Format 'yyyy-MM-dd HH:mm:ss') + ' ' + $m) -Encoding UTF8
}
try {
    if (Test-Path -LiteralPath (Join-Path $base 'brain_midx_hourly.STOP')) { Log 'skip: STOP file'; exit 0 }
    $midxFile = Join-Path $packDir 'multi-pack-index'
    if (-not (Test-Path -LiteralPath $midxFile)) { Log 'skip: no multi-pack-index'; exit 0 }
    $lock = Join-Path $packDir 'multi-pack-index.lock'
    if (Test-Path -LiteralPath $lock) {
        $age = [int]((Get-Date) - (Get-Item -LiteralPath $lock).LastWriteTime).TotalMinutes
        $tag = 'skip'
        if ($age -ge 120) { $tag = 'STALE-LOCK' }
        Log "${tag}: multi-pack-index.lock exists, $age min old (holder may be starved at low priority; do not delete the lock)"
        exit 0
    }
    $midxT = (Get-Item -LiteralPath $midxFile).LastWriteTime
    $idx = @(Get-ChildItem -LiteralPath $packDir -Filter '*.idx' -File -ErrorAction SilentlyContinue)
    $newPacks = @($idx | Where-Object { $_.LastWriteTime -gt $midxT }).Count
    if ($newPacks -lt 20) { Log "skip: $newPacks of $($idx.Count) packs newer than the index"; exit 0 }
    $env:GIT_ASK_YESNO = 'false'
    $env:RUN_BOUNDED_NORMAL_PRIORITY = '1'
    $t0 = Get-Date
    & 'C:\Python314\python.exe' (Join-Path $base 'run_bounded.py') 600 "$log.git" git -C $repo multi-pack-index write --no-progress | Out-Null
    $code = $LASTEXITCODE
    Log ("refresh: $newPacks of $($idx.Count) packs newer than the index, exit=$code in " + [int]((Get-Date) - $t0).TotalSeconds + ' s')
} catch { Log "error: $($_.Exception.Message)" }
