import logging
from scraper import GoogleMapsScraper
from processor import DataProcessor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """
    Main entry point for GapHunter automation.
    """
    # Configuration
    SECTOR = "restoran"
    LOCATION = "Ünye"
    TARGET_COUNT = 50

    logger.info(f"--- GapHunter Started: {SECTOR.upper()} @ {LOCATION.upper()} ---")

    try:
        # Step 1: Data Collection
        scraper = GoogleMapsScraper()
        raw_companies = scraper.fetch_companies(SECTOR, LOCATION, target_count=TARGET_COUNT)

        if not raw_companies:
            logger.warning("No data collected. Exiting.")
            return

        logger.info(f"Collected {len(raw_companies)} raw records.")

        # Step 2: Processing and Filtering (Find leads without websites)
        processor = DataProcessor()
        leads = processor.filter_and_sort(raw_companies)

        # Step 3: Display Results
        processor.display_results(leads)

        # Step 4: Save to CSV
        processor.save_to_csv(leads, SECTOR, LOCATION)

        logger.info("Automation completed successfully.")

    except Exception as e:
        logger.error(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()