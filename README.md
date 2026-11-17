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

Customers visit the website to place an order. When a customer adds their first item to the cart, predict whether they will place an order before the session ends. The prediction could eventually inform personalization, such as a discount; this demo does not issue one.

Use synthetic activity and customer information available at the first cart addition, including browsing activity before the trigger, device, returning-customer recognition, sign-in status, previous visits and orders, loyalty status, and carryout or delivery selection if already chosen. The trigger can happen at any point in the session; there is no elapsed-time cutoff. Start with a simple logistic regression baseline and batch yes/no predictions from CSV.

Prepared files:

- `data/sessions.csv`: 1,200 labeled synthetic sessions, including missing feature values.
- `data/new_sessions.csv`: 12 unlabeled sessions for predictions.
- `data/README.md`: schema, first-cart prediction boundary and target definition.

The main sequence is setup → hello world → plan → prepare data → train and predict → test → change → review and hand over.
During data preparation, optional DE prompts cover schema validation, data quality reports and repeatable ETL. They use the same dataset and feed the same model. Choose one if time permits; no separate DE project is needed.

## Set up Python and dependencies

Use Python 3.10–3.12 (3.11 or 3.12 recommended). Choose either Poetry or pip and use that environment throughout. Get tools through your company's approved process.

### With Poetry

Poetry 1.5 or newer is required for this option. If pipx is already approved and installed, a pinned Poetry installation is:

```sh
pipx install poetry==2.2.1
poetry --version
```

This is an optional human setup command, not an instruction for an agent to install tools automatically. If you do not have pipx, use your approved software catalog or the official Poetry installation instructions: https://python-poetry.org/docs/#installation. Do this before the live session.

From the repository root, create the environment and install the locked dependencies:

```sh
poetry env use python3.11
poetry install --no-root
poetry run python -c "import sys; print(sys.executable)"
```

Replace `python3.11` with an installed Python 3.10–3.12 executable or its absolute path. On Windows, find it with `py -0p` and pass the desired executable path to `poetry env use`. The root `poetry.toml` keeps the environment in the repository's `.venv`.

`--no-root` installs the dependencies without trying to package the exercise code.
Use unittest for tests. No database, Docker, server or cloud setup is needed.

### Without Poetry (pip)

The checked-in [`requirements.txt`](requirements.txt) pins the packages from `poetry.lock`, including the Python-version-specific versions. Create and activate a virtual environment, then install from the repository root.

Use only Python 3.10–3.12. Check the interpreter version before creating the environment; pip does not enforce the project's Python range from `pyproject.toml`.

macOS/Linux:

```sh
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Windows PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Use the approved Artifactory authentication process for package downloads. The requirements file contains no credentials, and pip will not bypass repository permissions; if Artifactory returns 403, ask your package administrator to check access.

### Verify the environment

With Poetry, run:

```sh
poetry run python -c "import pandas, sklearn; print(pandas.__version__, sklearn.__version__)"
poetry run python scripts/check_starter.py
```

With the pip environment activated, use:

```sh
python -c "import pandas, sklearn; print(pandas.__version__, sklearn.__version__)"
python scripts/check_starter.py
```

In VS Code, use **Python: Select Interpreter** and select the root `.venv`. In the Copilot app, ask Orca to use the project's `.venv` interpreter. Poetry users can run `poetry run python ...`; pip users can run `python ...` after activating `.venv`. Use one environment at the repository root.

When dependencies change, update `poetry.lock` and regenerate `requirements.txt` with the company-approved `poetry-plugin-export` plugin (`poetry export --format requirements.txt --output requirements.txt --without-hashes`). Review the generated diff before committing it.

## Install the framework and begin

Install the approved `agentic-coding-framework` release from the internal marketplace supplied by your presenter, verify its components in your client, and select **Orca** in a new chat. The private framework itself and internal marketplace URL are not included here.

First prompt (use `poetry run python` with Poetry, or `python` with the activated pip environment):

> Can you add a quick hello-world script, run it with this project's Python environment, and show me which Python it used?

Then follow the workbook's single sequence. Ask the agent to read `data/README.md`. The datasets and dependency files are prepared; participants build the preparation step, model and prediction scripts during the demo. There is no completed solution or pretrained model in this starter.

## Suggested session

| Minutes | Task |
|---|---|
| 00–03 | Verify the plugin and select Orca |
| 03–05 | Verify Python environment and hello world |
| 05–08 | Plan the conversion model and discuss skills used |
| 08–13 | Prepare data; optionally try one DE prompt |
| 13–19 | Train, evaluate and predict |
| 19–22 | Add and run tests |
| 22–25 | Make one requirement change |
| 25–30 | Review and add handover instructions |

Install the framework and complete Python environment setup and package downloads before the timer starts. The 30-minute walkthrough is a target within the one-hour session; use the remaining time for questions and buffer. Reviews may take longer: discuss questions while waiting and keep review status incomplete until it finishes. Docker, CI and cloud deployment are optional extras.

## Verify the starter data

From the repository root, with the project environment selected:

```sh
# Poetry
poetry run python scripts/check_starter.py

# Or, with the pip virtual environment activated
python scripts/check_starter.py
```

This standard-library check validates the supplied labeled and prediction data. It does not test the preparation code or model participants have yet to build. Add behavioral tests with Orca during the workshop.

All data is synthetic. Model metrics demonstrate mechanics, not production business value. No cloud account, database, Docker, API key or live customer data is needed.
