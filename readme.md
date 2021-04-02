# INTERN TRACKER

This software tracks new internship openings from various sites which includes intern providing sites, companies career sites, etc. It also allows its users to track new openings of companies of their choice, thus enabling them to be the first ones to apply for the role. 

## To run the project
    Step 1. Download the zip file of the project from the above link 

    Step 2. Extract the files in a folder with name <folder_name>
    
    Step 3. Move inside the project directory
        cd <folder_name>

    Step 4. Now you are inside the project directory. First thing we need to do is activate the virtual environment of the project. Here "env" is the name of our virtual environment. To activate virtual environment
        source env/bin/activate

    Step 6. Go inside the crawler folder
        cd InternTracker/InternTracker/spiders

    Step 5. Run the spider you wish to by using 
        scrapy crawl <spider_name>