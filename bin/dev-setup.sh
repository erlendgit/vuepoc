#!/usr/bin/env bash

if [[ ! -d ".venv" ]]; then
  python3 -m venv .venv --prompt VuePoc
fi

source .venv/bin/activate

pip install --upgrade pip -q
pip install -r requirements.txt -q

set -a
source .env
set +a