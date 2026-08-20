#!/usr/bin/env bash
# Regenerate The OneVision Playbook PDFs into output/
# Requires: pip install weasyprint markdown
set -euo pipefail
cd "$(dirname "$0")"
echo "→ building The OneVision Playbook"
python3 tools/build.py "$@"
echo "→ done. See output/"
