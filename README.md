# codex-research-script

A small Python package that runs the repository's `script.sh` upload test.

Install it for development:

```sh
python3 -m pip install -e .
```

Run the existing script:

```sh
command-formatter
```

The installed command uses a bundled copy of `script.sh`; the original
`script.sh` remains in the repository.

Or run it as a Python module:

```sh
python3 -m codex_research_script
```

You can also provide another script path:

```sh
command-formatter path/to/script.sh
```
