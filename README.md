Markdown

# NBA Player Comparison Tool

## Overview

This interactive web application, built with Streamlit, allows users to find statistically comparable NBA player seasons from a comprehensive historical dataset. By leveraging data standardization and Euclidean distance metrics, the tool helps basketball enthusiasts and analysts discover players with similar on-court performance profiles across different eras.

## Features

* **Interactive User Interface:** Intuitive input fields for player name and season, powered by Streamlit.

* **Robust Data Handling:** Efficient loading and preprocessing of historical NBA player statistics using Pandas, including cleaning column names and handling missing values.

* **Intelligent Player Matching:** Implements robust filtering logic to accurately identify target player seasons, accounting for variations in input (e.g., case sensitivity, data types).

* **Statistical Normalization:** Utilizes Scikit-learn's `StandardScaler` to normalize diverse player statistics (e.g., points, rebounds, shooting percentages), ensuring fair and unbiased similarity calculations.

* **Similarity Calculation:** Applies Euclidean distance to quantify the statistical similarity between players.

* **Top Comparable Players Display:** Presents a ranked list of the top 5 most statistically similar players, along with their key stats and a calculated "distance" score.

## Technologies Used

* **Python:** Core programming language.

* **Streamlit:** For building the interactive web application interface.

* **Pandas:** Essential for data loading, manipulation, and preprocessing.

* **NumPy:** Fundamental package for numerical computing.

* **Scikit-learn:** For machine learning utilities, specifically:

    * `StandardScaler` (for data normalization)

    * `euclidean_distances` (for similarity calculation)

* **Git & GitHub:** For version control, collaborative development, and project hosting.

## How to Run Locally

To set up and run this application on your local machine, follow these steps:

1.  **Clone the Repository:**

    ```
    git clone [https://github.com/your_username/nba_player_comparison.git](https://github.com/your_username/nba_player_comparison.git)
    cd nba_player_comparison


    ```

    *(Replace `your_username` with your actual GitHub username)*

2.  **Create and Activate a Virtual Environment:**

    ```
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # Or: .\venv\Scripts\activate  # On Windows


    ```

3.  **Install Dependencies:**

    ```
    pip install -r requirements.txt


    ```

4.  **Download the Data:**

    * Go to the Kaggle dataset: [NBA Stats (1947-present)](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats)

    * Download the `Player Per Game.csv` file.

    * Create a folder named `data` in the root of your `nba_player_comparison` project directory.

    * Place the downloaded `Player Per Game.csv` file inside the `data` folder.

5.  **Run the Streamlit Application:**

    ```
    streamlit run app.py


    ```

    The application will open in your default web browser.

## Live Demo

**Access the live application here:** [NBA Player Comparison Tool](https://nbaplayercomparison-wwjj5xqvz9uw8hrx5uipgt.streamlit.app/)








