# INTERN TRACKER

This software tracks new internship openings from various sites which includes intern providing sites, companies career sites, etc. It also allows its users to track new openings of companies of their choice, thus enabling them to be the first ones to apply for the role. 

## To run the project
1. Download the project code
    ```bash
    git clone https://github.com/xzaviourr/InternTracker.git
    ``` 
2. Install virtual environment for python
    ```bash
    pip install virtualenv
    ```
3. Create a new virtual environment named "venv" 
    ```bash
    python3.8 -m venv venv
    ```

4. Activate the newly created virtual environment  
    1. Windows-  
        ```bash
        cd venv/Scripts
        ./Activate
        ```

    2. Linux -
        ```bash
        source venv/bin/activate
        ```

5. Go back to home folder
6. Install the project requirements
    ```bash
    pip install requirements.txt
    ```

7. Go inside the spider folder
    ```bash
    cd InternTracker/InternTracker/spiders
    ```

9. Run the spider of your choice 
    ```bash
    scrapy crawl <spider_name>
    ```