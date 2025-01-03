# Feedback Sentiment Analysis System

This project is a web-based feedback sentiment analysis system built using Flask. It allows users to submit feedback, which is then analyzed for sentiment (Positive, Negative, or Neutral) using the Groq API. The feedback and its sentiment are stored in a SQLite database.

## Features

- Submit feedback through a web form.
- Analyze the sentiment of the feedback using the Groq API.
- Display previous feedbacks along with their sentiment.
- Delete all feedback records.

## Project Structure

- `app.py`: Main Flask application file.
- `logs/`: Directory containing log files.
- `myenv/`: Virtual environment directory.
- `requirements.txt`: List of dependencies.
- `src/`: Directory containing source code.
  - `db.py`: Database connection and initialization.
  - `exception.py`: Custom exception handling.
  - `logger.py`: Logging configuration.
  - `sentiment.py`: Sentiment analysis using Groq API.
- `templates/`: HTML templates for the web application.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Dharun11/Feedback_MGT_system.git
    cd feedback_mgt
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv myenv
    myenv\Scripts\activate  
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    - Create a [.env](http://_vscodecontentref_/4) file in the root directory.
    - Add your Groq API key to the [.env](http://_vscodecontentref_/5) file:
        ```
        GROQ_API_KEY=your_groq_api_key_here
        ```

5. Initialize the database:
    ```sh
    python -c "from src.db import Databaseconnect; db = Databaseconnect(); db.init_db()"
    ```

6. Run the application:
    ```sh
    python app.py
    ```

7. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

- Submit feedback through the form on the home page.
- View previous feedbacks and their sentiment on the home page.
- Delete all feedback records using the "Delete records" button.

## License

This project is licensed under the MIT License.