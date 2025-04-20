from hdbcli import dbapi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Connection details from .env
host = os.getenv('HANA_HOST')
port = int(os.getenv('HANA_PORT'))
user = os.getenv('HANA_USER')
password = os.getenv('HANA_PASSWORD')

try:
    # Establish a connection to the SAP HANA database
    connection = dbapi.connect(
        address=host,
        port=port,
        user=user,
        password=password
    )
    print("Connection to SAP HANA successful!")

    # Create a cursor object
    cursor = connection.cursor()

    # SQL query to fetch data from a table
    table_name = 'your_table_name'  # Replace with your table name
    query = f"SELECT * FROM {table_name}"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except dbapi.Error as e:
    print(f"An error occurred: {e}")