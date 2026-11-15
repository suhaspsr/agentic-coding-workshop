# Agentic Coding Workshop

A 40-minute Python workshop for ML and data engineers using the Agentic Coding Framework in GitHub Copilot (VS Code or the Copilot app).

Clone the starter, choose a track, open the HTML workbook, and ask Orca to build the project. Use the copyable demo sequence, try independent suggestions, or describe your own task.

## Start here

```sh
git clone https://github.com/suhaspsr/agentic-coding-workshop.git
cd agentic-coding-workshop
git switch -c workshop/my-session
```

This repository is private. Participants need repository access before cloning. Forking may be restricted; a local branch is sufficient and there is no need to push changes.

Open `agentic-coding-workbook.html` in your browser (double-click the downloaded file). GitHub's source view does not run the interactive workbook. Choose MLE or DE at the top.

| Track | Working folder | Supplied data | Python dependencies |
|---|---|---|---|
| MLE: conversion prediction | `mle/` | 1,200 labeled sessions + 12 unlabeled prediction rows | pandas, scikit-learn and their dependencies |
| DE: daily order sales | `de/` | 16 orders, seven expected totals and separate invalid-input fixtures | Standard library only |

Open the **track folder** in your Copilot client. That makes relative paths in prompts work: `data/sessions.csv` for MLE or `data/orders.csv` for DE.

## Set up Python and Poetry

Use Python 3.10–3.12 (3.11 or 3.12 recommended) and Poetry 1.5 or newer. Get tools through your company's approved process. If pipx is already approved and installed, a pinned Poetry installation is:

```sh
pipx install poetry==2.2.1
poetry --version
```

This is an optional human setup command, not an instruction for an agent to install tools automatically. If you do not have pipx, use your approved software catalog or the official Poetry installation instructions: https://python-poetry.org/docs/#installation. Do this before the live session.

From the repository root, choose **one** track:

```sh
cd mle
# Or: cd de
poetry env use python3.11
poetry install --no-root
poetry run python -c "import sys; print(sys.executable)"
```

Replace `python3.11` with an installed Python 3.10–3.12 executable or its absolute path. On Windows, find it with `py -0p` and pass the desired executable path to `poetry env use`. Each track's `poetry.toml` keeps the environment inside that track's `.venv`.

`--no-root` is intentional: this is a dependency-managed workshop starter, not a prebuilt installable Python package. Keep the provided `pyproject.toml` and `poetry.toml`. The DE track includes `poetry.lock`. The MLE lock could not be resolved in the preparation environment because access to PyPI was unavailable; its first `poetry install --no-root` resolves dependencies and creates `poetry.lock`. The presenter should complete that step using the approved package source before the demo, verify the imports, and commit the generated MLE lock for identical versions across participants.

MLE smoke check:

```sh
poetry run python -c "import pandas, sklearn; print(pandas.__version__, sklearn.__version__)"
```

DE needs no extra Python packages. For DE participants without Poetry, `python -m venv .venv` and its Python interpreter are sufficient; see the workbook for platform-specific paths.

In VS Code, use **Python: Select Interpreter** and select the track's `.venv`. In the Copilot app, ask Orca to use the track's Poetry environment. `poetry run python ...` works without shell activation.

## Install the framework and begin

Install the approved `agentic-coding-framework` release from the internal marketplace supplied by your presenter, verify its components in your client, and select **Orca** in a new chat. The private framework itself and internal marketplace URL are not included here.

First prompt (either track):

> Use the existing Poetry setup in this folder. Add a hello world script, run it with poetry run python, and show which interpreter you used.

Then use the workbook's connected sequence. Read this track's README and `data/README.md` with the agent. The dataset and environment are prepared; participants build the model or pipeline during the demo. There is no completed solution or pretrained model in this starter.

## Suggested session

| Minutes | Task |
|---|---|
| 00–05 | Install and verify the plugin; select Orca |
| 05–08 | Verify Poetry interpreter and hello world |
| 08–12 | Plan the selected small build |
| 12–17 | Inspect and prepare the supplied data |
| 17–25 | Build and run the model or pipeline |
| 25–30 | Add and run tests |
| 30–35 | Make one requirement change |
| 35–40 | Review and add handover instructions |

Poetry installation and package downloads should be completed before the timer starts. Docker, CI and cloud deployment are optional extras. Required framework reviews remain part of the work throughout.

## Verify the starter data

From the repository root, with any Python 3.10–3.12 interpreter:

```sh
python scripts/check_starter.py
```

This checks the supplied datasets and known DE totals. It does not test the model or pipeline participants have yet to build. Add project tests with Orca during the workshop.

All data is synthetic. Model metrics demonstrate mechanics, not production business value. No cloud account, database, Docker, API key or live customer data is needed.
