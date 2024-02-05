import pandas as pd
import numpy as np

def create_random_dataframe(rows, cols):
    # Set seed for reproducibility
    np.random.seed(56)
    
    # Create a Pandas DataFrame with random integers from 0 to 100
    data = np.random.randint(0, 101, size=(rows, cols))
    df = pd.DataFrame(data)
    
    # Print the generated DataFrame
    print(df)

# Example usage: change 5 and 3 to desired number of rows and columns
create_random_dataframe(5, 3)