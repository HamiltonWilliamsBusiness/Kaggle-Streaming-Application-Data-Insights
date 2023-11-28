import pypyodbc as odbc
import numpy as np
import pandas as pd

# Your connection details
DRIVER_NAME = "SQL SERVER"
SERVER_NAME = "LAPTOP-KBAD6AQA\SQLEXPRESS"
DATABASE_NAME = 'Netflix'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={{{SERVER_NAME}}};
    DATABASE={{{DATABASE_NAME}}};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)

try:
    # Establish a connection
    conn = odbc.connect(connection_string)

    # Create a cursor
    cursor = conn.cursor()

    # Example query
    query = "SELECT * FROM Streaming_Data"
    cursor.execute(query)

    # Fetch and print results
    rows = cursor.fetchall()

    # Convert tuples to numpy arrays
    arrays = [np.array(row) for row in rows]

    # Remove elements at indices 1, 2, and 3 from each array
    # modified_arrays = [np.delete(arr, [1, 2, 3]) for arr in arrays]

    # Create a DataFrame from the modified arrays
    columns = ["User_ID", "Session_ID", "Device_ID", "Video_ID", "Genre", "Country", "Age", "Gender", "Subscription_Status", "Ratings", "Languages", "Device_Type", "Location", "Playback_Quality", "Interaction_Events", ""]
    df = pd.DataFrame(arrays, columns=columns)

    # Print the DataFrame
    print(df.head())

except odbc.Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()
