import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App Title
st.title("🧮 Math Helper App")
st.write("Solve equations, generate tables, and plot graphs easily!")

# Sidebar for Navigation
st.sidebar.title("Choose an Option")
option = st.sidebar.radio("Select:", ["Basic Calculator", "Table Generator", "Equation Solver", "Graph Plotter"])

# Basic Calculator
if option == "Basic Calculator":
    st.header("🧮 Basic Calculator")
    num1 = st.number_input("Enter First Number", value=0)
    num2 = st.number_input("Enter Second Number", value=0)
    operation = st.radio("Select Operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

    if st.button("Calculate"):
        if operation == "Addition":
            st.success(f"Result: {num1 + num2}")
        elif operation == "Subtraction":
            st.success(f"Result: {num1 - num2}")
        elif operation == "Multiplication":
            st.success(f"Result: {num1 * num2}")
        elif operation == "Division":
            if num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("Cannot divide by zero!")

# Table Generator
elif option == "Table Generator":
    st.header("📊 Table Generator")
    num = st.number_input("Enter a Number for Table", min_value=1, value=2)
    if st.button("Generate Table"):
        for i in range(1, 11):
            st.write(f"{num} x {i} = {num * i}")

# Quadratic Equation Solver
elif option == "Equation Solver":
    st.header("📐 Quadratic Equation Solver (ax² + bx + c = 0)")
    a = st.number_input("Enter coefficient a:", value=1.0)
    b = st.number_input("Enter coefficient b:", value=0.0)
    c = st.number_input("Enter coefficient c:", value=0.0)

    if st.button("Solve"):
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + np.sqrt(discriminant)) / (2*a)
            root2 = (-b - np.sqrt(discriminant)) / (2*a)
            st.success(f"Roots are {root1:.2f} and {root2:.2f}")
        elif discriminant == 0:
            root = -b / (2*a)
            st.success(f"Root is {root:.2f}")
        else:
            st.error("No real roots!")

# Graph Plotter
elif option == "Graph Plotter":
    st.header("📈 Graph Plotter")
    eq_type = st.radio("Select Equation Type:", ["Linear (y = mx + c)", "Quadratic (y = ax² + bx + c)"])

    if eq_type == "Linear (y = mx + c)":
        m = st.number_input("Enter slope (m):", value=1.0)
        c = st.number_input("Enter intercept (c):", value=0.0)
        x = np.linspace(-10, 10, 100)
        y = m*x + c
    else:
        a = st.number_input("Enter coefficient a:", value=1.0)
        b = st.number_input("Enter coefficient b:", value=0.0)
        c = st.number_input("Enter coefficient c:", value=0.0)
        x = np.linspace(-10, 10, 100)
        y = a*x**2 + b*x + c

    fig, ax = plt.subplots()
    ax.plot(x, y, label="Equation Graph")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    st.pyplot(fig)
