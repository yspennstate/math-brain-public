$ErrorActionPreference = 'Stop'
$stageRoot = Split-Path $PSScriptRoot -Parent
python -X utf8 ~\brain_workers\FEI100_20261011\tools\memok.py *> (Join-Path $stageRoot 'out\memok.txt')
if ($LASTEXITCODE -ne 0) {
  'HOLD: fresh memok did not admit the core Lean check' | Set-Content -Encoding UTF8 (Join-Path $stageRoot 'out\lean_status.txt')
  exit 0
}
$env:LEAN_CHECK_DIR = Join-Path $stageRoot 'out\lean'
$formalPath = Join-Path $PSScriptRoot 'Core.lean'
$formalDigest = (Get-FileHash -Algorithm SHA256 -LiteralPath $formalPath).Hash.ToLowerInvariant()
python -X utf8 ~\.claude\dreaming\lean_check.py --file $formalPath --core --target A033ControllerStep --reviewed-sha256 $formalDigest --timeout 20 --json *> (Join-Path $stageRoot 'out\lean_output.txt')
"Wrapper exit: $LASTEXITCODE" | Set-Content -Encoding UTF8 (Join-Path $stageRoot 'out\lean_status.txt')
