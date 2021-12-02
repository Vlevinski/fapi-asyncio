# How to check FastAPI with asincio and aiohttp
                          
## Want to learn how to build this?

Check out the [post](https://fastapi.tiangolo.com/fastapi-people/).

## Want to use this project?


### Without Docker

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    
    ```

1. Run FastApi with asyncio and aiohttp:

    ```sh
    (venv)$ uvicorn main:app --reload
    ```

1. Or Use the script to run it:

    ```sh
   (venv)$ run.sh
     $ ./run.sh
     
   >INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   >INFO:     Started reloader process [7639] using statreload
   >INFO:     Started server process [7641]
   >INFO:     Waiting for application startup.
   >INFO:     Application startup complete.
    '''
    
1. How use the browser if it runs:

      http://127.0.0.1:8000       - see Hello FastAPI message
      http://127.0.0.1:8000/test  - check how works ascyncio with aiohttp
      

          
