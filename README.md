# YouTube Data Scraping and Analysis

This project is designed to scrape data from YouTube using the YouTube Data API, store it in both MongoDB and PostgreSQL databases, and perform data analysis using Python. The data analysis includes various queries and visualizations to gain insights into YouTube channels, playlists, videos, and comments.

## Prerequisites

Before running the scripts, make sure you have the following dependencies installed:

- Python 3.x
- `pymongo` package (for MongoDB interaction)
- `psycopg2` package (for PostgreSQL interaction)
- `pandas` package (for data manipulation and analysis)
- `streamlit` package (for UI and interactive data visualization)
- `Google Client` Library for YouTube Data API

You can install the required Python packages using pip:
```
pip install pymongo psycopg2 pandas streamlit google-api-python-client
```

To use the YouTube Data API, you will need to set up credentials and obtain an API key. Follow the steps below:

1. Create a new project on the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the [YouTube Data API](https://console.cloud.google.com/apis/library) for your project.
3. Create credentials for the API by following the instructions provided by Google. Select the appropriate credentials type for your project.

This allows the Google Client Library to authenticate with the YouTube Data API using your project's credentials.

4. Finally, make sure you have a running MongoDB server and a PostgreSQL database set up with the necessary connection details.

## Project Structure

The project consists of the following files:

- `app.py`: Streamlit application for interactive data visualization and exploration.
- `main.py`: Main script that orchestrates the data scraping and analysis process.
- `MongoDB_Upload.py`: Script to upload data from the YouTube Data API to MongoDB.
- `fetchData_from_MongoDB.py`: Script to fetch data from MongoDB and perform data transformation.
- `migrate_to_SQL.py`: Script to migrate data from MongoDB to PostgreSQL.
- `channel_analysis.py`: Script with various queries to analyze the YouTube data stored in PostgreSQL.

## Usage

1. Clone the repository:
```
git clone https://github.com/iampraveens/Youtube-Data-Scraping.git
```
2. Install the required Python packages:
```
pip install pymongo psycopg2 pandas streamlit google-api-python-client
```
3. Also install the required dependencies:
```
pip install -r requirements.txt
```
### or

```
pip3 install -r requirements.txt
```
4. Set up the Google Cloud credentials by following the instructions provided in the `Prerequisites` section.
5. Make sure you have a running MongoDB server and a PostgreSQL database with the necessary connection details. Update the connection parameters in the relevant scripts if needed.
6. To perform data analysis and visualization, run the Streamlit application in your terminal:

```
streamlit run app.py
```
The application will open in your browser, allowing you to explore the data and view visualizations.

7. To perform custom queries and analysis, refer to the `channel_analysis.py` script and execute the desired functions.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create an issue or submit a pull request.

## License

- This project is `Un-Licensed`
- Feel free to use, modify, and distribute this project as needed.

## Acknowledgements

- This project utilizes the YouTube Data API to scrape YouTube data. Make sure to comply with YouTube's terms of service and API usage policies.
- If you have any questions or need assistance, please don't hesitate to [contact me](https://www.linkedin.com/in/iampraveens/).

