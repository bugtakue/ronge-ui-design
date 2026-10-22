#!/usr/bin/env bash
# RONGE seed generator: prints seeds and a direction sheet skeleton.
set -euo pipefail
count="${1:-3}"
case "$count" in
  ''|*[!0-9]*) echo "usage: seed.sh [1-9]" >&2; exit 2 ;;
esac
if [ "$count" -lt 1 ] || [ "$count" -gt 9 ]; then
  echo "usage: seed.sh [1-9]" >&2
  exit 2
fi
printf 'RONGE seeds\n'
for i in $(seq 1 "$count"); do
  seed="$(python3 -c 'import secrets,string; print("".join(secrets.choice(string.ascii_letters+string.digits) for _ in range(48)))')"
  printf '\nDirection %s · seed: %s\n' "$i" "$seed"
  printf '  视觉主张：\n  具体参照：\n  不妥协的选择：\n'
done
printf '\n把 seed 当成素材，不要显示在 UI 上。\n'
