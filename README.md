# PandasDataCleaning
Data cleaning is an essential step in data analysis to ensure data quality and reliable results.
Python's Pandas library offers powerful tools for cleaning and manipulating tabular data.
Here's a simplified overview of common data cleaning tasks using Pandas:

**1. Importing Libraries and Data:**

- Import Pandas library using `import pandas as pd`.
- Load your data using `pd.read_csv("your_file.csv")` for CSV files (adjust for other file formats, excel..). This creates a Pandas DataFrame object.

**2. Exploring the Data:**

- Use `df.head()` and `df.tail()` to view the first and last few rows.
- Get basic information about the data using `df.info()`.
- Check for missing values using `df.isnull().sum()`.

**3. Handling Missing Values:**

- Drop rows with missing values using `df.dropna()`. 
- Impute missing values with statistical methods (e.g., `df.fillna(df.mean())`) or custom logic.

**4. Removing Duplicates:**

- Identify and remove duplicate rows using `df.drop_duplicates()`.

**5. Cleaning Specific Columns:**

- **Formatting:** Use string methods like `df['column_name'].str.strip()` to remove leading/trailing spaces.
- **Fixing inconsistencies:** Replace unwanted characters/values using `df['column_name'].str.replace()`.
- **Working with regex**
- **Converting data types:** Use `df['column_name'] = pd.to_numeric(df['column_name'])` to convert strings to numeric data types (if applicable).

**6. Saving the Cleaned Data:**

- Save the cleaned DataFrame to a new file using `df.to_csv("cleaned_data.csv")`.
