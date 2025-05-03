import pulp

# Define the model
model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Define decision variables
x = pulp.LpVariable('Chairs', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Tables', lowBound=0, cat='Continuous')

# Objective function
model += 45*x + 80*y, "Total Profit"

# Constraints
model += 5*x + 10*y <= 100, "Labor Constraint"
model += 20*x + 30*y <= 180, "Wood Constraint"

# Solve the model
model.solve()

# Output results
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Produce {x.varValue} chairs")
print(f"Produce {y.varValue} tables")
print(f"Total Profit = ₹{pulp.value(model.objective)}")
