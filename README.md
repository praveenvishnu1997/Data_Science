# YouTube Data Scraping and Analysis

This project is designed to scrape data from YouTube using the YouTube Data API, store it in both MongoDB and PostgreSQL databases, and perform data analysis using Python. The data analysis includes various queries and visualizations to gain insights into YouTube channels, playlists, videos, and comments.

## Prerequisites

Before running the scripts, make sure you have the following dependencies installed:

- Python 3.x
- `pymongo` package (for MongoDB interaction)
- `psycopg2` package (for PostgreSQL interaction)
- `pandas` package (for data manipulation and analysis)
- `streamlit` package (for interactive data visualization)
- `Google Client` Library for YouTube Data API

You can install the required Python packages using pip:
```
pip install pymongo psycopg2 pandas streamlit google-api-python-client
```

To use the YouTube Data API, you will need to set up credentials and obtain an API key. Follow the steps below:

1. Create a new project on the [Google Cloud Console](https://console.cloud.google.com/).

2. Enable the YouTube Data API for your project.

3. Create credentials for the API by following the instructions provided by Google. Select the appropriate credentials type for your project.

4. Download the credentials file (in JSON format) and save it securely.

5. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the downloaded credentials file.

   - On Linux or macOS:

