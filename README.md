# Air-Quality-Classification-India-Cities

Analyze and classify air quality in some cities in India before and after COVID-19 using machine learning. This project involves data wrangling, exploratory data analysis (EDA), feature engineering, model development and model deployment, to predict air quality conditions. Explore the impact of the pandemic on air pollution levels.


## Instructions to Run the Classification Script

This script processes a CSV file containing air quality data, predicts the air quality class using a pre-trained model, and saves the results into a SQLite database.

### Prerequisites

Before running the script, ensure you have the following:

- Python 3.6 or higher
- Required Python packages:
  - pandas
  - sqlite3 (standard library)
  - pickle (standard library)
  - scikit-learn
  - xgboost

### Installation of Required Packages

If you do not have the required packages, you can install them using pip:

```bash
pip install pandas scikit-learn xgboost
```

### Steps to Run the Script

1. **Prepare the CSV File**:
   Ensure you have a CSV file with the appropriate columns (excluding the target variable `Air_Quality`).

2. **Ensure the Pre-trained Model**:
   Make sure you have the pre-trained model saved as `best_model.pkl` in the `../models/` directory.

3. **Run the Script**:
   Access the scritp in the folder scripts/classifier.py. Use the command line to run the script with your CSV file as an argument:

    ```bash
    python classifier.py path/to/your/input.csv
    ```

   Replace `path/to/your/input.csv` with the path to your CSV file.

5. **Check the SQLite Database**:
   The script will create a SQLite database file at `../database/air_quality.db` and insert the data into the specified table (`air_quality_india`).

### Example

Here's an example of running the script:

```bash
python classify_and_save.py sample_air_quality_data.csv
```

This will process `sample_air_quality_data.csv`, predict the air quality class, and save the results in the `air_quality_india` table within the `air_quality.db` SQLite database.

By following these instructions, you can successfully run the script to classify the air quality data and store the results in a SQLite database.
