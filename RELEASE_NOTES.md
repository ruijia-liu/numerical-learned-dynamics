# Release notes

The original notebook covered four numerical integration methods, analytical oscillator solutions, damping and forcing, resonance scans and an MLP trained on one simulated trajectory. The public copy preserves the numerical and learning implementations.

The cleanup removes an unrelated recursive image-file search, replaces the local coursework filename with a descriptive name, clears stale execution metadata, and reruns the notebook. It retains the course context and author name.

Explanatory text has been corrected to distinguish the damped amplitude-resonance frequency from the 90-degree phase crossing, the forced steady state from unforced decay to equilibrium, and special-case position-error behavior from a general integrator order. The approximate damped Verlet implementation is explicitly identified. The one-trajectory random split is described as an interpolation diagnostic.

These edits do not introduce a new model, additional dataset or improved performance result. Third-party Python dependencies retain their own licenses; no new license grant is assigned to the coursework material in this release.

## Verification

The release was executed with Python 3.12 and the direct dependency versions in `requirements.txt`. All 22 code cells completed without errors and produced 15 plots. The public `run_notebook.py` command was also executed successfully; its protection against overwriting an existing output was checked.

The refreshed notebook reports a one-step test R-squared of 0.9993 for the random split within the single generated trajectory. The fixed-step damped example reports Improved Euler position RMSE of approximately 0.00976 m. These values describe the stated examples and do not change the interpretation limits in the README.
