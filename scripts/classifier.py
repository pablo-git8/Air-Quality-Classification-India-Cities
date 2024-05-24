import pandas as pd
import sqlite3
import pickle
import sys

def classify_and_save_to_db(csv_file_path, db_file_path, table_name, pickle_file_path):
    # Load the CSV file
    data = pd.read_csv(csv_file_path)
    
    # Load the saved model
    with open(pickle_file_path, 'rb') as file:
        model = pickle.load(file)
    
    # Define features
    X_new = data.drop(columns=['Air_Quality'], errors='ignore')
    
    # Make predictions
    predictions = model.predict(X_new)
    
    # Add predictions to the DataFrame
    data['Predicted_Air_Quality'] = predictions
    
    # Connect to SQLite database (it will create the file if it does not exist)
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join([f'{col} {dtype}' for col, dtype in zip(data.columns, ['REAL'] * (len(data.columns) - 1) + ['INTEGER'])])}
    )
    ''')
    
    # Insert data into the table
    data.to_sql(table_name, conn, if_exists='append', index=False)
    
    # Commit and close the connection
    conn.commit()
    conn.close()
    print(f"Data has been successfully saved to the {table_name} table in {db_file_path} database.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_file_path>")
        sys.exit(1)
    
    csv_file_path = sys.argv[1]
    pickle_file_path = '../models/best_model.pkl'
    db_file_path = '../database/air_quality.db'
    table_name = 'air_quality_india'
    
    classify_and_save_to_db(csv_file_path, db_file_path, table_name, pickle_file_path)

