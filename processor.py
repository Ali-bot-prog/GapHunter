import csv
import logging
import os
from datetime import datetime
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class DataProcessor:
    """
    Handles data filtering, sorting, and export operations.
    """
    
    @staticmethod
    def filter_and_sort(raw_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Filters businesses without websites and sorts them by rating count (descending).
        """
        # Filter: select companies that do NOT have a website
        potential_leads = [
            company for company in raw_data 
            if not company.get("website")
        ]

        # Sort: descending by ratingCount (reviews)
        sorted_leads = sorted(
            potential_leads, 
            key=lambda x: x.get("ratingCount", 0), 
            reverse=True
        )

        return sorted_leads

    @staticmethod
    def display_results(leads: List[Dict[str, Any]]) -> None:
        """
        Prints formatted results to the terminal.
        """
        if not leads:
            logger.warning("No leads found to display.")
            return

        print(f"\n{'='*60}")
        print(f"--- ANALYSIS COMPLETE: {len(leads)} POTENTIAL LEADS FOUND ---")
        print(f"{'='*60}\n")
        
        for idx, company in enumerate(leads, 1):
            name = company.get("title", "Unknown")
            reviews = company.get("ratingCount", 0)
            phone = company.get("phoneNumber", "No Phone")
            address = company.get("address", "No Address")
            
            print(f"{idx:02d}. {name}")
            print(f"    - Reviews: {reviews}")
            print(f"    - Contact: {phone}")
            print(f"    - Address: {address}")
            print(f"    {'-'*40}")

    @staticmethod
    def save_to_csv(leads: List[Dict[str, Any]], sector: str, location: str) -> Optional[str]:
        """
        Saves results to a timestamped CSV file (Excel compatible).
        """
        if not leads:
            logger.warning("No data to save.")
            return None

        # Create reports directory if it doesn't exist
        reports_dir = "reports"
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"{sector}_{location}_{date_str}.csv".lower().replace(" ", "_")
        filepath = os.path.join(reports_dir, filename)

        headers = ["Rank", "Company Name", "Review Count", "Rating", "Phone", "Address"]

        try:
            with open(filepath, mode='w', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file, delimiter=';') # Semicolon for better Excel compatibility in some regions
                writer.writerow(headers)

                for idx, company in enumerate(leads, 1):
                    writer.writerow([
                        idx,
                        company.get("title", "Unknown"),
                        company.get("ratingCount", 0),
                        company.get("rating", 0),
                        company.get("phoneNumber", "N/A"),
                        company.get("address", "N/A")
                    ])
            
            logger.info(f"Report successfully saved to: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Error writing to file {filepath}: {e}")
            return None