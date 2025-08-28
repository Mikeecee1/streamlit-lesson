# Create a function named calculator_body()
# Within it, create 3 columns using the st.columns() function
# Note, in the video, this column function was still in beta
import streamlit as st

def calculator_body():
    """
    Renders a calculator interface in a Streamlit app with three columns for input.

    - First column: Input for the first number.
    - Second column: Input for the second number.
    - Third column: Dropdown to select the arithmetic operation (Add, Subtract, Multiply, Division).

    When the "Calculate" button is pressed:
        - Checks for division by zero and displays an error if applicable.
        - Otherwise, calls `calculator_function` with the provided inputs.

    Returns:
        None
    """
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input(label="Enter first number", step=1)
    with col2:
        num2 = st.number_input("Enter second number", step=1)
    with col3:
        operation = st.selectbox("Select operation", options=["Add", "Subtract", "Multiply", "Division"])
    if st.button("Calculate"):
        if num2==0 and operation=="Division":
            st.error("Cannot divide by zero")
        else:
            calculator_function(num1, num2, operation)

def calculator_function(num1, num2, operation):
    """
    Performs a basic arithmetic operation (addition, subtraction, multiplication, or division)
    on two numbers and displays the result using Streamlit.

    Args:
        num1 (float or int): The first number.
        num2 (float or int): The second number.
        operation (str): The operation to perform. Must be one of "Add", "Subtract", "Multiply", or "Division".

    Returns:
        None. The result is displayed using Streamlit's st.success or st.error.
    """
    if operation=="Add":
        result = num1 + num2
        st.success(f"The result of adding {num1} and {num2} is **{result}**")
    elif operation=="Subtract":
        result = num1 - num2
        st.success(f"The result of subtracting {num2} from {num1} is **{result}**")
    elif operation=="Multiply":
        result = num1 * num2
        st.success(f"The result of multiplying {num1} and {num2} is **{result}**")
    elif operation=="Division":
        result = num1 / num2
        st.success(f"The result of dividing {num1} by {num2} is **{result}**")
    else:
        st.error("Invalid operation selected.")
