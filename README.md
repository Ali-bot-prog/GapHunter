# 🎯 GapHunter

**GapHunter** is a professional automation tool designed to identify businesses that lack a digital presence. By leveraging the Google Maps API (via Serper.dev), it discovers local businesses in specific sectors and locations, filters those without websites, and ranks them by their local influence (review count).

This tool is built for entrepreneurs, digital agencies, and freelancers looking to bridge the "digital gap" for local businesses.

---

## 🚀 Features

- **Automated Discovery**: Scrape hundreds of businesses in any sector and location.
- **Smart Filtering**: Automatically identifies businesses that do NOT have a website listed.
- **Lead Scoring**: Sorts potential leads by their review count to help you prioritize high-impact targets.
- **Excel Compatible Export**: Saves results into structured CSV files formatted for Microsoft Excel.
- **Technical Debt Free**: Modular architecture with logging, type hints, and robust error handling.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ali-bot-prog/GapHunter.git
cd GapHunter
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the root directory and add your Serper.dev API key:

```env
MAPS_API_KEY=your_serper_api_key_here
```

*You can get a free API key at [serper.dev](https://serper.dev).*

---

## 📖 Usage

Run the automation with a single command:

```bash
python main.py
```

### Customization

You can change the target sector and location in `main.py`:

```python
SECTOR = "restoran"
LOCATION = "Ünye"
TARGET_COUNT = 50
```

---

## 📂 Project Structure

- `main.py`: Entry point for the automation.
- `scraper.py`: Core logic for interacting with the Serper/Google Maps API.
- `processor.py`: Data filtering, sorting, and export logic.
- `reports/`: (Auto-generated) Directory where CSV results are saved.
- `.gitignore`: Ensures sensitive files like `.env` are not pushed to GitHub.

---

## 🛡️ License & Copyright

This project is open-source. However, the implementation and logic are optimized for high-performance lead generation.

**© 2026 OmNexus. All Rights Reserved.**
