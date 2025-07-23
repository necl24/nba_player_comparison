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

## Visuals
Here's a quick look at some of the key technologies powering this project:

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python Logo" width="75"> 
<img src="https://streamlit.io/images/brand/streamlit-logo-light.svg" alt="Streamlit Logo" width="75">
<img src="https://pandas.pydata.org/static/img/pandas.svg" alt="Pandas Logo" width="75">
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="Scikit-learn Logo" width="75">
<img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub Logo" width="75">

## How to Run Locally

To set up and run this application on your local machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your_username/nba_player_comparison.git](https://github.com/your_username/nba_player_comparison.git)
    cd nba_player_comparison
    ```
    *(Replace `your_username` with your actual GitHub username)*

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # Or: .\venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the Data:**
    * Go to the Kaggle dataset: [NBA Stats (1947-present)](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats)
    * Download the `Player Per Game.csv` file.
    * Create a folder named `data` in the root of your `nba_player_comparison` project directory.
    * Place the downloaded `Player Per Game.csv` file inside the `data` folder.

5.  **Run the Streamlit Application:**
    ```bash
    streamlit run app.py
    ```
    The application will open in your default web browser.

## Live Demo
*(Once deployed, replace this line with your actual Streamlit Cloud URL)*
[Link to Live Application](YOUR_STREAMLIT_CLOUD_URL_HERE)


## Live Demo
*(Once deployed, replace this line with your actual Streamlit Cloud URL)*
[Link to Live Application](YOUR_STREAMLIT_CLOUD_URL_HE
