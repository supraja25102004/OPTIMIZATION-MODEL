import pulp
import matplotlib.pyplot as plt

# Define the problem
prob = pulp.LpProblem("Factory_Profit_Maximization", pulp.LpMaximize)

# Define decision variables
x = pulp.LpVariable('Product_A', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Product_B', lowBound=0, cat='Continuous')

# Objective function (maximize profit)
prob += 40 * x + 30 * y, "Total_Profit"

# Constraints
prob += 2 * x + 1 * y <= 100, "Machine_Hours"
prob += 1 * x + 1 * y <= 80, "Labor_Hours"

# Solve the problem
prob.solve()

# Get results
status = pulp.LpStatus[prob.status]
product_a = x.varValue
product_b = y.varValue
total_profit = pulp.value(prob.objective)

# Print textual output
print("Status:", status)
print("Produce {} units of Product A".format(product_a))
print("Produce {} units of Product B".format(product_b))
print("Total Profit: ${}".format(total_profit))

# 📊 Create a bar chart to visualize the output
products = ['Product A', 'Product B']
values = [product_a, product_b]

plt.figure(figsize=(7, 5))
bars = plt.bar(products, values, color=['skyblue', 'orange'])
plt.title(f'Optimal Production Plan\nTotal Profit = ${total_profit}', fontsize=14)
plt.ylabel('Units Produced')

# Add text labels above bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, int(yval), ha='center', va='bottom', fontsize=12)

plt.ylim(0, max(values) + 10)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
