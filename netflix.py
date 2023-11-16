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

    # Now 'arrays' contains arrays that you can modify

    # Printing out all the rows
    # for arr in arrays:
    #     print(arr)
    # print(arrays)

    for arr in arrays[:10]:
        print(arr)

    # Print all the tuples
    # for row in rows:
    #     print(row)
    # print(rows)

except odbc.Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()