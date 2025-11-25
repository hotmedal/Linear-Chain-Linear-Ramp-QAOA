# Linear-Chain-Linear-Ramp-QAOA
Linear chain QAOA with linear ramp parameter initialization for the Vehicle Routing Problem

To accompany the manuscript "Shallow and Robust QAOA: Improving Feasibility and Hardware Performance via Linear-Chain and Ramp Schedules", authored by Talha Azfar and Ruimin Ke of RPI. 

## Files

### Notebooks
- `LCqaoa_CVaR.ipynb` — Runs Linear-Chain QAOA (LC-QAOA) with a CVaR objective on IBM Quantum hardware.
- `LR_qaoa_AER.ipynb` — Runs Linear-Ramp–initialized QAOA (LR-QAOA) using the Aer simulator.
- `gmqaoa_AER.ipynb` — Runs Grover-Mixer QAOA with Dicke-state initialization on Aer; also includes a short-depth Dicke-state preparation routine.
- `twoStep_AER.ipynb` — Runs Two-Step QAOA using the Aer simulator.

### Scripts / Data
- `plot_gate_depth.py` — Reads `gates_parallel.csv` and plots transpiled LC-QAOA circuit depth for the IBM Heron processor.
- `Depth and Feasibility.xlsx` — Consolidated results and figures: transpiled depth, Aer feasibility, and IBM hardware runs, including the graphs used in the paper.
