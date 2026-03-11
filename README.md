# Telegram Channel Scraper

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Telethon](https://img.shields.io/badge/Telethon-1.25.2+-blue.svg)](https://github.com/LonamiWebs/Telethon)

A powerful Python command-line tool for scraping messages from Telegram channels using the Telethon library. Extract channel data including message content, metadata, reply information, and export to CSV format for analysis.

## ✨ Features

- 📥 **Bulk Message Extraction** - Pull up to 100 messages (configurable) from any public Telegram channel.
- 🔐 **Secure Authentication** - Uses official Telegram API with secure credential handling.
- 📊 **CSV Export** - Automatically exports scraped data to organized CSV files.
- 📝 **Rich Metadata** - Captures message IDs, dates, authors, reply counts, and more.
- 🎯 **User-Friendly CLI** - Interactive prompts guide you through the scraping process.
- 🔄 **Batch Processing** - Efficiently handles large message volumes.
- 📁 **Organized Output** - Creates timestamped folders for each scraping session

## 📋 Requirements

- **Python 3.11.x** or higher
- **Telegram API Credentials** (free from [my.telegram.org](https://my.telegram.org/apps))
  - API ID
  - API Hash
  - Phone number associated with your Telegram account

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MarufxAlchemist/Telegram-scrapper.git
cd Telegram-scrapper
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Telegram API Credentials

#### Option A: Interactive Mode (Recommended for beginners)
Simply run the script and enter your credentials when prompted.

#### Option B: Environment Variables (Recommended for advanced users)
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your credentials:
   ```env
   TELEGRAM_API_ID=your_api_id
   TELEGRAM_API_HASH=your_api_hash
   TELEGRAM_PHONE=+1234567890
   ```

### 4. Get Your Telegram API Credentials

1. Visit [https://my.telegram.org/apps](https://my.telegram.org/apps)
2. Log in with your phone number
3. Click on "API development tools"
4. Fill in the application details (any name/description works)
5. Copy your `api_id` and `api_hash`

## 💻 Usage

### Basic Usage

Run the scraper:

```bash
python main.py
```

The script will guide you through:
1. **Authentication** - Enter your API credentials and verify with a code sent to Telegram
2. **Channel Selection** - Provide the channel username or invite link
3. **Scraping** - Messages are automatically downloaded and saved

### Example Session

```
Provide your Telegram api_id:
> 12345678

Provide your Telegram api_hash:
> abcdef1234567890abcdef1234567890

Provide your Telegram account phone number (in +123456789 format):
> +1234567890

These are the credentials you provided:
{'api_id': '12345678', 'api_hash': 'abcdef...', 'phone': '+1234567890'}

Do you wish to proceed? Enter 'y' to continue or 'n' to start over:
> y

------------------------------

Client initialized
Client connected
Enter the code you received:
> 12345

Client authenticated

------------------------------

Enter a Telegram channel to scrape (username or invite link):
> @examplechannel

Channel Name: Example_Channel
Created folder 'Output_Example_Channel_2026-01-23' to store output

Preparing to pull up to 100 messages from 'Example_Channel'
Pulled 100 total messages for channel 'Example_Channel'
Extracting fields and cleaning messages
Created file 'Output_Example_Channel_2026-01-23.csv' in output folder
[Finished]
```

### Output Format

The scraper creates a folder named `Output_[ChannelName]_[Date]` containing a CSV file with the following columns:

| Column | Description |
|--------|-------------|
| `message_id` | Unique message identifier |
| `channel_name` | Name of the Telegram channel |
| `message_date` | Timestamp when message was posted |
| `post_author` | Author of the message (if available) |
| `is_posted_by_bot` | Whether message was posted by a bot |
| `total_replies` | Number of replies to the message |
| `is_reply_comments` | Whether replies are comments |
| `recent_replier_ids` | User IDs of recent repliers |
| `raw_text` | Full text content of the message |

## ⚙️ Configuration

### Adjusting Message Limit

To change the number of messages scraped, edit `TelegramChannelScraper.py`:

```python
# Line 116
MESSAGE_LIMIT = 100  # Change this value
```

### Customizing Output

The scraper automatically:
- Creates timestamped output folders
- Removes duplicate entries
- Handles missing data gracefully
- Explodes reply data for detailed analysis

## 🔒 Security Best Practices

- ✅ **Never commit** your `.env` file or credentials to version control
- ✅ **Use environment variables** for production deployments
- ✅ **Keep your API credentials private** - treat them like passwords
- ✅ **Enable two-factor authentication** on your Telegram account
- ✅ **Review** the `.gitignore` file to ensure sensitive files are excluded

## 🐛 Troubleshooting

### Common Issues

**"The phone number provided is invalid"**
- Ensure your phone number is in international format: `+1234567890`
- Include the country code with the `+` prefix

**"The code entered is invalid"**
- Check that you entered the verification code correctly
- Request a new code if it expired

**"The channel is private and you are not a member"**
- You must be a member of private channels to scrape them
- Join the channel first, then run the scraper

**"FloodWaitError"**
- Telegram has rate limits to prevent abuse
- Wait for the specified time before retrying
- Consider reducing the `MESSAGE_LIMIT`

**"Session file errors"**
- Delete any `.session` files in the project directory
- Restart the authentication process

### Getting Help

If you encounter issues:
1. Check the [Issues](https://github.com/MarufxAlchemist/Telegram-scrapper/issues) page
2. Search for similar problems and solutions
3. Create a new issue with detailed information about your problem

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Users are responsible for:
- Complying with Telegram's Terms of Service
- Respecting privacy and data protection laws
- Obtaining necessary permissions before scraping channels
- Using scraped data ethically and legally

The developers are not responsible for misuse of this tool.

## 🙏 Acknowledgments

- [Telethon](https://github.com/LonamiWebs/Telethon) - Telegram API library
- [Pandas](https://pandas.pydata.org/) - Data manipulation library
- [tqdm](https://github.com/tqdm/tqdm) - Progress bar library

## 📞 Support

- 📧 Email: contact@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/MarufxAlchemist/Telegram-scrapper/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/MarufxAlchemist/Telegram-scrapper/discussions)

---

**Made by [Maruf Nadaf](https://github.com/MarufxAlchemist)**
