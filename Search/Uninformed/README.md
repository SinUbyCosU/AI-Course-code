We will code DFS and BFS here

## Setup

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# intall in windowns
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Create venv with specific Python version
uv venv --python 3.10

# Activate venv
# macOS/Linux:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate

```
## For More details follow the [Venv setup based on OS available](https://github.com/pyarelalchauhan/DSP/tree/main/venv_setup#7-uv-modern-python-package-manager)

#### Lets install libraries:
```bash
uv pip install jupyterlab==4.4.7 ipykernel ipython pillow
uv pip install --upgrade pip
```

If failure due to internet speed, please try below cammand first then run above cammand again:
```bash
set UV_HTTP_TIMEOUT=300

```
register your ipython kernel
```bash
uv pip install ipykernel -U --force-reinstall

uv run ipython kernel install --user --name=.venv
```
Restart your vscode
#### If you want to work with just jupyter notenook, launch as `uv run jupyter lab`


