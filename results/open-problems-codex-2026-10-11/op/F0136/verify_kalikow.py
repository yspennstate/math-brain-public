from pathlib import Path
import subprocess, time

root = Path(__file__).resolve().parent
receipt_path = root / 'kalikow_lean_check.txt'
if receipt_path.exists():
    archive = root / 'kalikow_lean_check_first.txt'
    if archive.exists():
        archive = root / f'kalikow_lean_previous_{time.time_ns()}.txt'
    archive.write_text(receipt_path.read_text(encoding='utf-8'), encoding='utf-8')
start = time.monotonic()
try:
    result = subprocess.run(
        ['lake', 'env', 'lean', str(root / 'KalikowObstruction.lean')],
        cwd='~/lean_verify',
        capture_output=True, text=True, encoding='utf-8', timeout=3600,
    )
    receipt = (f'exit_code={result.returncode}\n'
               f'elapsed_seconds={time.monotonic()-start:.3f}\n'
               + result.stdout + result.stderr)
except Exception as error:
    receipt = f'check_failed={error!r}\nelapsed_seconds={time.monotonic()-start:.3f}\n'
receipt_path.write_text(receipt, encoding='utf-8')
print(receipt)
