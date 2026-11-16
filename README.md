# Agentic Coding Workshop

A one-hour session for ML and data engineers, with a roughly 30-minute Python walkthrough using the Agentic Coding Framework in GitHub Copilot (VS Code or the Copilot app).

One project, one environment, one sequence: build a customer conversion model. Data engineering tasks are part of the preparation step. Follow the copyable demo prompts, try the optional suggestions, or ask in your own words.

## Start here

```sh
git clone https://github.com/suhaspsr/agentic-coding-workshop.git
cd agentic-coding-workshop
git switch -c workshop/my-session
```

A local branch is sufficient and there is no need to push changes.

Open `agentic-coding-workbook.html` in your browser (double-click the downloaded file). GitHub's source view does not run the interactive workbook.

Open the **repository root** in Copilot and run all commands there. There is one root `pyproject.toml`, one `poetry.toml` and one `.venv`.

## The project

Customers visit the website to place an order. At minute five of a still-open session with no order yet, predict whether the customer will order before the session ends. The prediction could eventually inform personalization, such as a discount; this demo does not issue one.

Use synthetic session activity, signed-in status, previous visits and orders, loyalty status, and carryout or delivery selection when available by minute five. Start with a simple logistic regression baseline and batch yes/no predictions from CSV.

Prepared files:

- `data/sessions.csv`: 1,200 labeled synthetic sessions, including missing feature values.
- `data/new_sessions.csv`: 12 unlabeled sessions for predictions.
- `data/README.md`: schema, prediction boundary and target definition.

The main sequence is setup → hello world → plan → prepare data → train and predict → test → change → review and hand over.
During data preparation, optional DE prompts cover schema validation, data quality reports and repeatable ETL. They use the same dataset and feed the same model. Choose one if time permits; no separate DE project is needed.

## Set up Python and Poetry

Use Python 3.10–3.12 (3.11 or 3.12 recommended) and Poetry 1.5 or newer. Get tools through your company's approved process. If pipx is already approved and installed, a pinned Poetry installation is:

```sh
pipx install poetry==2.2.1
poetry --version
```

This is an optional human setup command, not an instruction for an agent to install tools automatically. If you do not have pipx, use your approved software catalog or the official Poetry installation instructions: https://python-poetry.org/docs/#installation. Do this before the live session.

Run this setup once, from the repository root:

```sh
poetry env use python3.11
poetry install --no-root
poetry run python -c "import sys; print(sys.executable)"
```

Replace `python3.11` with an installed Python 3.10–3.12 executable or its absolute path. On Windows, find it with `py -0p` and pass the desired executable path to `poetry env use`. The root `poetry.toml` keeps one shared environment in the repository's `.venv`.

`--no-root` installs pandas, scikit-learn and their dependencies without trying to package the exercise code. Use unittest for tests. No database, Docker, server or cloud setup is needed.

A shared `poetry.lock` is not included yet because the preparation environment could not reach PyPI. Before the demo, run `poetry install --no-root` with the approved package source, verify the imports below, and commit the generated root `poetry.lock` so participants use identical versions.

Check the shared environment:

```sh
poetry run python -c "import pandas, sklearn; print(pandas.__version__, sklearn.__version__)"
```

In VS Code, use **Python: Select Interpreter** and select the root `.venv`. In the Copilot app, ask Orca to use the root Poetry environment. `poetry run python ...` works without activation. Keep one Poetry environment at the repository root.

## Install the framework and begin

Install the approved `agentic-coding-framework` release from the internal marketplace supplied by your presenter, verify its components in your client, and select **Orca** in a new chat. The private framework itself and internal marketplace URL are not included here.

First prompt:

> Can you add a quick hello-world script, run it with poetry run python, and show me which Python it used?

Then follow the workbook's single sequence. Ask the agent to read `data/README.md`. The datasets and Poetry configuration are prepared; participants build the preparation step, model and prediction scripts during the demo. There is no completed solution or pretrained model in this starter.

## Suggested session

| Minutes | Task |
|---|---|
| 00–03 | Verify the plugin and select Orca |
| 03–05 | Verify Poetry interpreter and hello world |
| 05–08 | Plan the conversion model and discuss skills used |
| 08–13 | Prepare data; optionally try one DE prompt |
| 13–19 | Train, evaluate and predict |
| 19–22 | Add and run tests |
| 22–25 | Make one requirement change |
| 25–30 | Review and add handover instructions |

Install the framework and complete Poetry setup and package downloads before the timer starts. The 30-minute walkthrough is a target within the one-hour session; use the remaining time for questions and buffer. Reviews may take longer: discuss questions while waiting and keep review status incomplete until it finishes. Docker, CI and cloud deployment are optional extras.

## Verify the starter data

From the repository root, with any Python 3.10–3.12 interpreter:

```sh
poetry run python scripts/check_starter.py
```

This checks the supplied labeled and prediction data. It does not test the preparation code or model participants have yet to build. Add behavioral tests with Orca during the workshop.

All data is synthetic. Model metrics demonstrate mechanics, not production business value. No cloud account, database, Docker, API key or live customer data is needed.
