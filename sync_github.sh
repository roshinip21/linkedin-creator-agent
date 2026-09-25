#!/usr/bin/env bash
set -e
export PATH="$HOME/.local/bin:$PATH"
MSG="${1:-Update LinkedIn agent}"

git add .
# Check if there are changes staged
if git diff-index --quiet HEAD --; then
  echo "No changes to commit."
else
  git commit -m "$MSG"
  git push origin main
  echo "✓ Successfully pushed update to https://github.com/roshinip21/linkedin-creator-agent"
fi
