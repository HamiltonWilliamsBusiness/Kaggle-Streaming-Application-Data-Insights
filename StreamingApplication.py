import pypyodbc as odbc # pip install pypyodbc
import numpy as np # pip install numpy

DRIVER_NAME =   "SQL SERVER"
SERVER_NAME = "LAPTOP-KBAD6AQA\SQLEXPRESS"
DATABASE_NAME = 'Netflix'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={{{SERVER_NAME}}};
    DATABASE={{{DATABASE_NAME}}};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)
print(conn)

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
    modified_arrays = [np.delete(arr, [1, 2, 3]) for arr in arrays]

    # Columns still within a row
    print("User_ID index 0, Duration_Watched_Minutes index 1, Genre index 2, Country index 3, Age index 4, Gender index 5, Subscription_Status index 6, Ratings index 7, Languages index 8, Device_Type index 9, Location index 10, Playback_Quality index 11, Interaction_Events index 12")

    # Print the modified arrays
    for modified_arr in modified_arrays[:10]:
        print(modified_arr)

except odbc.Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()