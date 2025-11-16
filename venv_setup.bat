@echo off
setlocal

if not exist .venv (
  python -m venv .venv
)
call .venv\Scripts\activate
pip install -r requirements.txt

echo Venv ready.
