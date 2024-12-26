from irtsimulator.simulator import IRTSimulator

# Initialize simulator
simulator = IRTSimulator(model="2PL", n_respondents=500, n_items=20, seed=42)

# Generate parameters
a, b, theta = simulator.generate_parameters()

# Simulate responses
responses = simulator.simulate_responses()

# Display results
print("Discrimination Parameters (a):", a)
print("Difficulty Parameters (b):", b)
print("Latent Abilities (theta):", theta)
print("Simulated Responses:")
print(responses.head())
