# PuddingBot

PuddingBot is a Discord bot for private use, providing weather information for Polish cities, message purging, and help commands.

## Features

- **Weather**: Get current weather for Polish cities, including temperature, wind, precipitation, and air pressure.
- **Lowest Temperature**: Find the city with the lowest current temperature in Poland.
- **Purge Messages**: Remove all messages sent by a specific user in the current channel (Admins only).
- **Help**: Display a help manual with available commands.

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the root directory with your Discord bot token:
   ```
   DISCORD_TOKEN='your_discord_token_here'
   ```

4. **Ensure required resources**:
   - Place `day_weather.jpg` and `night_weather.jpg` in the `resources/` directory.
   - Ensure the font file `calibrib.ttf` is available or the default font will be used.

## Usage

Run the bot with:

```sh
python main.py
```

## Commands

| Command                        | Description                                                                                  | Example Usage                        |
|---------------------------------|----------------------------------------------------------------------------------------------|--------------------------------------|
| `$$help`                       | Show help manual with all commands.                                                          | `$$help`                             |
| `$$purge_messages_from @user`   | Remove all messages sent by a user in the current channel (Admins only).                     | `$$purge_messages_from @username`    |
| `$$weather <city>`              | Get current weather for a specified Polish city.                                             | `$$weather Warszawa`                 |
| `$$weather_lowest_temp`         | Show weather for the city with the lowest current temperature in Poland.                     | `$$weather_lowest_temp`              |
| `$$joke`                        | Get very funny programmers joke.                                                             | `$$joke`                             |
## Notes

- The bot uses the [IMGW public API](https://danepubliczne.imgw.pl/api/data/synop) for weather data.
- Only users with Administrator permissions can use the purge command.
- The bot requires the `MESSAGE CONTENT INTENT` to be enabled in the Discord developer portal.

## License

Private use
