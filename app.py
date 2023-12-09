import streamlit as st

def find_largest(num1, num2, num3):
    # Using max function to find the largest number among the three
    return max(num1, num2, num3)

def main():
    st.title('Find the Largest Number')
    
    # Get user input for three numbers
    num1 = st.number_input('Enter the first number:')
    num2 = st.number_input('Enter the second number:')
    num3 = st.number_input('Enter the third number:')
    
    if st.button('Find Largest'):
        # Call function to find the largest number
        largest = find_largest(num1, num2, num3)
        st.success(f'The largest number is: {largest}')

if __name__ == '__main__':
    main()
