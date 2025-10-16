config = {
        "mcpServers": {
            "flight-search": {
                "command": "/opt/homebrew/bin/uv", #correct path to uv
                "args": [
                    "--directory", "/Users/sushil/Desktop/Projects/mcp-travel-agent/backend/servers/flight_server", #Setup according to your path 
                    "run", "python", "flight_server.py"
                ],
                "transport": "stdio",
                "env": {
                    "SERPAPI_KEY": ""
                }
            },
            "hotel-search": {
                "command": "/opt/homebrew/bin/uv",  #correct path to uv
                "args": [
                "--directory", "/Users/sushil/Desktop/Projects/mcp-travel-agent/backend/servers/hotel_server",#Setup according to your path 
                "run", "python", "hotel_server.py"
            ],
            "env": {
                "SERPAPI_KEY": ""
            }
            },
            "event-search": {
                "command": "/opt/homebrew/bin/uv", #correct path to uv
                "args": [
                "--directory", "/Users/sushil/Desktop/Projects/mcp-travel-agent/backend/servers/event_server", #Setup according to your path 
                "run", "python", "event_server.py"
            ],
                "env": {
                "SERPAPI_KEY": ""
            }
            },
                "geocoder": {
                "command": "/opt/homebrew/bin/uv",  #correct path to uv
                "args": [
                "--directory", "/Users/sushil/Desktop/Projects/mcp-travel-agent/backend/servers/geocoder_server",#Setup according to your path 
                "run", "python", "geocoder_server.py" 
            ]
            },
                "weather-search": {
                "command": "/opt/homebrew/bin/uv", #correct path to uv
                "args": [
                "--directory", "/Users/sushil/Desktop/Projects/mcp-travel-agent/backend/servers/weather_server",#Setup according to your path 
                "run", "python", "weather_server.py"
            ]
            },
                "finance-search": {
                "command": "/opt/homebrew/bin/uv", #correct path to uv
                "args": [
                "--directory", "/Users/sushil/Desktop/Projects/mcp-travel-agent/backend/servers/finance_server",#Setup according to your path 
                "run", "python", "finance_search_server.py"
            ],
                "env": {
                "SERPAPI_KEY": ""
            }
            }
        }
    } 