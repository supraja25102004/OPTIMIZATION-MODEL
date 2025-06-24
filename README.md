# OPTIMIZATION-MODEL
*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: ANKEPALLI SHIVA SUPRAJA

*INTERN ID*: CT08DN1734

*DOMAIN*: DATA SCIENCE

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

## Problem Statement:

In this project, we solve a classic resource allocation problem faced by a factory that produces two products (A and B). The objective is to determine how many units of each product to produce in order to maximize total profit, given constraints on machine hours and labor hours.

This is a supervised optimization problem, and we apply Linear Programming (LP)—a mathematical technique for optimizing an objective under constraints.

##  Tools & Libraries Used:

    pulp->Formulating and solving the LP model

    matplotlib->Visualizing the optimal production plan

##  Mathematical Formulation:

Let:

->x = units of Product A

->y = units of Product B

Objective Function (Maximize Profit):

->Maximize: 40x + 30y

Subject to Constraints:

->Machine hours: 2x + y ≤ 100

->Labor hours: x + y ≤ 80

->Non-negativity: x ≥ 0, y ≥ 0

## Process Overview:

Problem Setup->Define decision variables, objective function, and constraints

Modeling->Use pulp.LpProblem() to build the linear optimization model

Solving->Use prob.solve() to compute the optimal solution

Evaluation->Extract and print the optimal values and profit

Visualization->Plot a bar chart of units produced using matplotlib

## Insights:

1.The optimal strategy is to produce 20 units of Product A and 60 units of Product B.

2.This results in a maximum profit of $2600.

3.All available resources (labor and machine hours) are used efficiently.

## Visualization:

The bar chart at the end shows:

1.Number of units to produce for each product

2.Total profit is shown in the plot title

3.Makes the solution easily interpretable to non-technical stakeholders

## Why It’s a Data Science Project:

This project involves:

1.Mathematical modeling of a real-world business problem

2.Algorithmic optimization

3.Interpretability via visual analytics

4.Lays the groundwork for integration into dashboards or automation workflows

## Result Summary:

->20 units of Product A

->60 units of Product B

->Maximum Profit = $2600

All machine and labor resources are fully utilized (tight constraints)

This means the factory is operating at full capacity in the most profitable way possible.

## How to implement it:

->Use VS Code or Jupyter Notebook.

->Install dependencies:

     pip install pulp matplotlib

->Now execute it.


## Conclusion:

This project is a textbook application of prescriptive analytics in data science. It highlights how mathematical modeling and programming can solve real-world business problems efficiently.

I have used:

1.A mathematical optimization algorithm

2.A Python implementation for automation

2.A visual communication method (bar chart) for explaining results to stakeholders




















