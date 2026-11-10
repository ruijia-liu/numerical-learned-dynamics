"""Execute the oscillator notebook with the active Python environment."""
import argparse
import os
from pathlib import Path
import sys

import nbformat
from jupyter_client import KernelManager
from nbclient import NotebookClient


def main(output):
    root = Path(__file__).resolve().parent
    output = Path(output).resolve()
    if output.exists():
        raise FileExistsError('Output already exists; choose a new --output path.')
    output.parent.mkdir(parents=True, exist_ok=True)
    for variable in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ.setdefault(variable, '1')
    notebook = nbformat.read(root/'oscillator_dynamics.ipynb', as_version=4)
    manager = KernelManager(kernel_name='python3')
    manager.kernel_spec.argv = [
        sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}',
    ]
    client = NotebookClient(
        notebook, km=manager, timeout=600, allow_errors=False,
        resources={'metadata': {'path': str(root)}},
    )
    try:
        client.execute()
        nbformat.write(notebook, output)
    finally:
        # A caller-provided kernel manager is owned by this runner.
        if manager.has_kernel:
            manager.shutdown_kernel(now=True)
    print(f'Completed notebook: {output}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='output/oscillator_dynamics.ipynb')
    main(parser.parse_args().output)
