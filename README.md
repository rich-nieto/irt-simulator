
# IRTSimulator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**IRTSimulator** is a Python library for simulating response data based on Item Response Theory (IRT) models. The library currently supports the 2PL model and is designed to help researchers and practitioners easily generate realistic datasets for psychometric and educational testing research.

## Features

- Simulate response data using the **2PL model**.
- Generate item parameters (discrimination and difficulty) and person abilities.
- Outputs simulated responses in a convenient tabular format (Pandas DataFrame).
- Reproducible simulations with seed support.

## Installation

### Using `pip`

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/rich-nieto/irtsimulator.git
   cd irtsimulator
   ```

2. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

## Usage

### Basic Simulation Example

```python
from irtsimulator.simulator import IRTSimulator

# Initialize the simulator
simulator = IRTSimulator(n_respondents=500, n_items=20, seed=42)

# Generate item and person parameters
a, b, theta = simulator.generate_parameters()

# Simulate responses
responses = simulator.simulate_responses()

# Display results
print("Discrimination Parameters (a):", a)
print("Difficulty Parameters (b):", b)
print("Latent Abilities (theta):", theta)
print("Simulated Responses:")
print(responses.head())
```

### Output Example

```text
Discrimination Parameters (a): [1.23 1.47 0.86 ...]
Difficulty Parameters (b): [-0.52  0.34 -0.85 ...]
Latent Abilities (theta): [ 0.45 -1.23  0.87 ...]
Simulated Responses:
                Item_1  Item_2  Item_3  ...
Respondent_1         1       0       1  ...
Respondent_2         0       1       0  ...
...
```

## Dependencies

- Python >= 3.7
- NumPy >= 1.21
- Pandas >= 1.3

Install all dependencies via:
```bash
pip install -r requirements.txt
```

## Contributing

...

## License

...

## Contact

- Author: Rich Nieto
- Email: rich.nieto@pm.me
- GitHub: [rich-nieto](https://github.com/rich-nieto)
