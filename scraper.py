import os
import requests
import time
import logging
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

class GoogleMapsScraper:
    """
    Scraper class to fetch business data from Google Maps via Serper.dev API.
    """
    def __init__(self):
        self.api_key = os.getenv("MAPS_API_KEY")
        if not self.api_key:
            logger.error("MAPS_API_KEY not found in environment variables.")
            raise ValueError("MAPS_API_KEY is required.")
            
        self.base_url = "https://google.serper.dev/maps"
        self.headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }

    def fetch_companies(self, sector: str, location: str, target_count: int = 100) -> List[Dict[str, Any]]:
        """
        Fetches companies based on sector and location.
        """
        all_results: List[Dict[str, Any]] = []
        current_page = 1
        ll: Optional[str] = None  # Coordinate info for pagination
        
        logger.info(f"Starting scan for sector '{sector}' in '{location}'...")

        while len(all_results) < target_count:
            payload = {
                "q": f"{sector} in {location}",
                "page": current_page
            }
            
            if ll:
                payload["ll"] = ll

            try:
                logger.info(f"Fetching page {current_page}...")
                response = requests.post(self.base_url, headers=self.headers, json=payload, timeout=30)
                response.raise_for_status()
                
                data = response.json()
                results = data.get("places", [])
                
                if current_page == 1:
                    ll = data.get("ll")

                if not results:
                    logger.info("No more results found.")
                    break

                all_results.extend(results)
                logger.info(f"Page {current_page} completed. Total records: {len(all_results)}")

                # Small delay to be polite to the API
                time.sleep(1) 
                current_page += 1

                # Prevent infinite loops if target_count is very high but results are exhausted
                if len(results) < 10: # Standard Serper page size is 10-20
                    break

            except requests.exceptions.RequestException as e:
                logger.error(f"Network error on page {current_page}: {e}")
                break
            except Exception as e:
                logger.error(f"Unexpected error on page {current_page}: {e}")
                break

        return all_results[:target_count]
