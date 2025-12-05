# Telegram ID Finder

Web UI tool to find Telegram group/channel IDs and user IDs for configuration.

---

## Features

- **Telegram Login**: Authenticate with your Telegram account using API credentials
- **List Groups/Channels**: View all joined groups and channels with their IDs
- **View Senders**: See recent message senders in any group with their user IDs
- **Generate Config**: Export selected chats and senders as `settings.yaml` for [telegram-signal-parser](https://github.com/AsiaOstrich/telegram-signal-parser)
- **One-Click Copy**: Quickly copy any ID to clipboard

---

## Screenshots

*Coming soon*

---

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Telegram API credentials from [my.telegram.org/apps](https://my.telegram.org/apps)

### Installation

```bash
# Clone the repository
git clone https://github.com/AsiaOstrich/telegram-id-finder.git
cd telegram-id-finder

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. (Optional) Edit `.env` to add your Telegram API credentials:
   ```env
   TELEGRAM_API_ID=your_api_id
   TELEGRAM_API_HASH=your_api_hash
   ```

   > **Note**: You can also enter credentials directly in the web interface.

### Running the Application

```bash
# Run with uvicorn
uvicorn app.main:app --reload

# Or run directly
python -m app.main
```

The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Usage

### Step 1: Login to Telegram

1. Enter your **API ID** and **API Hash** from [my.telegram.org/apps](https://my.telegram.org/apps)
2. Enter your phone number (with country code, e.g., `+886912345678`)
3. Click "Send Code" and enter the verification code from Telegram
4. If 2FA is enabled, enter your password

### Step 2: Select Groups/Channels

- Browse all your joined groups and channels
- Click "Copy" to copy any chat ID
- Check the boxes to select chats for config generation

### Step 3: View Senders (Optional)

- Click "View Senders" on any group to see recent message senders
- Copy user IDs or select senders for config generation

### Step 4: Generate Config

- Review your selected chats and senders
- Click "Generate settings.yaml" to create the configuration
- Copy the YAML content to use in your project

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/send-code` | Send verification code |
| POST | `/api/auth/verify` | Verify login code |
| GET | `/api/auth/status` | Check login status |
| POST | `/api/auth/logout` | Logout |
| GET | `/api/dialogs` | Get all groups/channels |
| GET | `/api/dialogs/{chat_id}/messages` | Get message senders |
| POST | `/api/generate-config` | Generate settings.yaml |

---

## Project Structure

```
telegram-id-finder/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── telegram_service.py  # Telethon service wrapper
│   └── templates/
│       └── index.html       # Web UI
├── .standards/              # Documentation standards
├── .env.example             # Environment variables template
├── requirements.txt         # Python dependencies
├── README.md                # This file (English)
├── README.zh-TW.md          # Chinese documentation
├── CLAUDE.md                # AI assistant guidelines
└── CONTRIBUTING.md          # Contribution guidelines
```

---

## Security Notes

- **API credentials** are sensitive. Never commit `.env` or share your API Hash.
- **Session files** (`*.session`) contain authentication data. They are gitignored by default.
- The application runs locally and does not send data to external servers (except Telegram's API).

---

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: HTML + Tailwind CSS + Vanilla JavaScript
- **Telegram Client**: Telethon (MTProto)
- **Python**: 3.11+

---

## Documentation Standards

This project follows the [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards).

- See [CLAUDE.md](CLAUDE.md) for AI assistant guidelines
- See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
- See [.standards/](.standards/) for detailed standards

---

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

## Related Projects

- [telegram-signal-parser](https://github.com/AsiaOstrich/telegram-signal-parser) - Parse trading signals from Telegram
- [Universal Documentation Standards](https://github.com/AsiaOstrich/universal-doc-standards) - Documentation framework
