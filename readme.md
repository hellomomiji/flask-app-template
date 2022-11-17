# Get Started

## To run this app in VS Code
(Reference: [Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask)).

1. Prerequisites
   - python3 and python extension installed.

2. Create project environment for the Flask
    - use the following command to create and activate virtual environment named `.venv`
    ```
    # Linux
    sudo apt-get install python3-venv    # If needed
    python3 -m venv .venv
    source .venv/bin/activate

    # macOS
    python3 -m venv .venv
        source .venv/bin/activate

    # Windows
    py -3 -m venv .venv
    .venv\scripts\activate
    ```
3. Install dependencies `pip3 install -r requirements.txt`.
   1. flask, refer to [Installation — Flask Documentation (2.2.x)](https://flask.palletsprojects.com/en/2.2.x/installation/).
   2. Jinja2, refer to [Introduction - Jinja Documentation (3.1.x)](https://jinja.palletsprojects.com/en/3.1.x/intro/#installation).

4. `flask run` to run the app on your local server.
