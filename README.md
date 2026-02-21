# letterboxd_script

A Selenium-based web scraper to automatically mark movies as watched on Letterboxd.

## Why This Exists

I am fully aware i could've just used the CSV import on Letterboxd (would've made my life so much easier). Instead, this is what boredom on a Saturday night leads you to. Kinda got to practice my Selenium skills too - while also adding something to my GitHub. Plus, i got to watch a bot click through my watchlist. 

Also, i've just realised i should've done this for imdb instead. 

## What It Does

This script:
- Logs into your Letterboxd account
- Reads a list of movies from a text file
- Navigates to each movie's page
- Clicks the "watched" button
- Tracks which movies failed (if any)
- Gives you a nice summary at the end

## Setup

### Prerequisites
- Python 3.9+
- Chrome browser
- ChromeDriver (Selenium will handle this if you have the right setup)

### Installation

1. Clone this repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with the following:
   ```
   USERNAME=your_letterboxd_username
   PASSWORD=your_letterboxd_password
   DIRECTORY=/path/to/your/movies/file/directory
   ```

4. Create a `movies.txt` file in the directory you specified. Format it like this:
   ```
   - [x] Movie Title 1
   - [x] Movie Title 2
   - [x] Another Movie
   ```
   (Lines starting with `- [ ]` will be skipped)

### Running the Script

```bash
python runner.py
```

Then sit back and watch it work. The browser will open, log in, and start marking movies as watched.

## Disclaimer

This code is **not** the most robust thing ever written (pls, i barely do anything on my own, this in itself is an achievement). Anyways, here's what could go wrong:

- Network timeouts might crash the script (working on better error handling)
- Movie titles with weird characters might not convert to the right URL slug. It also refuses to work if the movie title has non alphanumeric characters (apostrophes, colons, ampersands, etc.)
- Letterboxd might change their HTML structure and break everything
- Rate limiting isn't implemented, so don't go too crazy with huge lists (actually, im not too sure what would happen if you did, test it out for me pls)
- If Letterboxd updates their site, the CSS selectors might break

## Future Improvements

If i ever get around to it (highly unlikely jbtw):
- Better URL slug generation
- Retry logic for network failures
- Proper logging
- Resume from where it left off
- Actually handle all the edge cases

But hey, it works for now. ¯\\\_(ツ)_/¯

## License

Do whatever you want with this. MIT License or something.
