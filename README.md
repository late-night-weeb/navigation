### Navigation page
This repository is not actively maintained, tho if you encounter a bug feel free to open a new issue

### What you'll need
- Basic understanding of Docker

### Structure
- Installation using [Docker](#Docker)
- Installation using [Python](#Python)


#### Docker
Run it using the [Docker Compose](docker-compose.yml)
```
services:
  navigation:
    container_name: navigation
    image: sparklingsausage/navigation:latest
    restart: unless-stopped
    ports:
      - "5000:5000"
    volumes:
      - /path/to/data.json:/app/data.json
      - /path/to/images/:/app/static/
      - /path/to/category.json:/app/category.json
      - /path/to/colors.json:/app/colors.json
```

#### Python
Download the [python file](app.py) and install all [requirements](requirements.txt) using pip.
Run the it using python

```
python app.py
```

#### Screenshots
![](/screenshots/ui.png?raw=true "Image of the UI")
![](/screenshots/addTile.png?raw=true "Image of the addTile")
![](/screenshots/editTile.png?raw=true "Image of the tile editing")
![](/screenshots/categories.png?raw=true "Image of the category management")
![](/screenshots/colors.png?raw=true "Image of the color management")
