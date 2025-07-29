"""
Search Automation Script

This script automates the process of searching for information based on combinations of keywords in the OneSearch database.
It utilizes PyAutoGUI to interact with the user interface and perform actions such as copying, pasting, and clicking.
The script reads keyword combinations from an Excel file, generates search queries, performs searches, and saves the results to a CSV file.

Author: [Jianye Chang]
Date: [04/02 - 2024]

Requirements:
- PyAutoGUI
- Pyperclip
- pandas
- logging

Usage:
1. Ensure that all required applications are open.
2. Run the script.
3. Wait for the script to complete the data processing tasks.

Note: Before running the script, make sure you specify the file path and worksheet name for the keyword Excel file,
    and be sure to install Google plugins for zotero and zoter,
    otherwise you won't be able to run it. This is a very targeted GUI-based script, you know.

"""
import os
import csv
import time
import pandas as pd
import pyautogui
import pyperclip
import logging
from typing import List, Optional
import itertools

# config
EXCEL_FILE_PATH = "E:\\github\\slr\\script\\SLR-Information2.xlsx"
DATABASE_LIST = ["IEEE Xplore", "Scopus", "Pubmed", "Web of science", "ScienceDirect", "Scopus(Elsevier)", "Springer", "Wiley Online Library"]
ROOT_DIR = r"E:\\github\\slr\\script\\"
SEARCH_COUNT_START = 0

os.chdir(os.path.dirname(__file__))
# Display all columns
pd.set_option('display.max_columns', None)
# Display all rows
pd.set_option('display.max_rows', None)
pyautogui.FAILSAFE = False


def Chromealert():
    # Alert the user to prepare for data processing
    pyautogui.alert('Please ensure that all required applications are open and the correct sheets are active.')
    pyautogui.alert('Data processing will begin now.')


def endalert():
    # Alert the user to prepare for data processing
    pyautogui.alert('Searching finished !')


def mouse_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def copy_to_clipboard(text):
    pyperclip.copy(text)


def paste_from_clipboard():
    return pyperclip.paste()


class SearchAutomation:
    def __init__(self) -> None:
        """Initialize the SearchAutomation class."""
        # Initialize the logger
        logging.basicConfig(
            filename='search_automation.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        # Initialize PyAutoGUI
        pyautogui.FAILSAFE = True  # Enable the failsafe feature
        pyautogui.PAUSE = 1  # Set the pause time between key presses
        # Initialize Pyperclip
        copy_to_clipboard("")  # Clear the clipboard
        self.Database = "All"
        self.end_message = "You've "
        self.zotero = [1772, 61]
        self.select = [702, 652]
        self.ok = [1247, 652]
        self.end_position = [47, 1498]
        self.result = [21, 251]  # 579 538
        self.search = [255, 158]

    def get_position(self) -> None:
        """Continuously print the current mouse position until Ctrl+ C is pressed."""
        try:
            while True:
                print('Press Ctrl-C to end')
                # Get the screen size
                screenWidth, screenHeight = pyautogui.size()
                x, y = pyautogui.position()
                # Print the mouse coordinates
                print(f'Screen size: ({screenWidth}, {screenHeight}), Mouse position: ({x}, {y})')
                # Print every 1 second and clear the screen
                time.sleep(1)
        except KeyboardInterrupt:
            print('Ended')

    def search_on_onesearch(self, query: str) -> str:
        """
        Perform a search on the OneSearch platform using the provided query.

        :param query: The search query string to be used on OneSearch.
        :return: The count of search results obtained from OneSearch.
        """
        # Clean the query by removing special characters and preparing it for the search
        query = query.replace(",", "").replace("'AND'", "AND")
        # Copy the modified query to the clipboard for pasting into the search field
        copy_to_clipboard(query[1:-1])
        # Move the mouse cursor to the search field and double click to select it
        mouse_click(self.search[0], self.search[1])
        pyautogui.doubleClick()
        # Clear the search field and paste the query from the clipboard
        pyautogui.hotkey('ctrl', 'a', 'delete')
        pyautogui.hotkey("ctrl", "v")
        # Press enter to perform the search
        pyautogui.press("enter")
        time.sleep(12)  # Adjust the waiting time as needed for the search results to load

        # Copy the search result count to the clipboard
        mouse_click(self.result[0], self.result[1])
        pyautogui.doubleClick()
        pyautogui.hotkey("ctrl", "c")
        result_count = paste_from_clipboard()
        time.sleep(4)

        while result_count.strip() == "loading":
            copy_to_clipboard('')
            time.sleep(4)
            mouse_click(self.result[0], self.result[1])
            pyautogui.doubleClick()
            pyautogui.hotkey("ctrl", "c")
            result_count = paste_from_clipboard()
            time.sleep(4)

        copy_to_clipboard('')  # Clear the clipboard
        return result_count.strip()

    def query_combine(self, search_count_start: int, *keysets: list) -> list:
        """
        Generate combinations of keywords.

        :param search_count_start: Specifies the starting value for search count.
        :param keysets: A list of one or more lists containing keyword sets.
        :return: A list containing the combinations of keywords.
        """
        combined_queries = []
        for combination in itertools.product(*keysets):
            query = " AND ".join(f"(({item}))" for item in combination)
            combined_queries.append(query)

        # Record the number of permutations
        logging.info(f"Total combinations generated: {len(combined_queries)}")
        return combined_queries[search_count_start:]

    def save_to_csv(
            self,
            queries: list,
            csv_file: str,
            Database: str,
            zotero_save: bool,
            search_count_start: int
    ) -> None:
        """
        Save search results to a CSV file.

        :param queries: A list of queries to be searched.
        :param csv_file: The path to the CSV file where the search results will be saved.
        :param Database: The database name.
        :param zotero_save: A boolean flag indicating whether to save the results to Zotero.
        :param search_count_start: Specifies the starting value for search count.
        """
        search_count = search_count_start
        num = 1
        for query in queries:
            result_count = ""
            end_message: Optional[str] = None
            query = str(query)

            # Clean the query for logging
            query_cleaned = query.replace('"AND"', 'AND')  # Replace '"AND"' with 'AND' for log clarity

            try:
                result_count = self.search_on_onesearch(query)
                result_count = result_count.strip()
                # Check for loading status or non-numeric values
                if result_count.startswith("Your"):
                    result_count = "0"
                else:
                    result_count = str(float(result_count))
            except ValueError as e:
                logging.error(f"Error processing result count for query '{query}': {e}")
                result_count = "0"

            # Simulate Zotero save actions based on result count
            if zotero_save:
                try:
                    result_num = float(result_count)
                    if 7 <= result_num <= 60:
                        num = int(result_num) // 2
                        # Simulate scrolling and saving
                        pyautogui.keyDown('space')
                        time.sleep(4)
                        pyautogui.keyUp('space')
                        time.sleep(4)
                        mouse_click(self.zotero[0], self.zotero[1])
                        mouse_click(self.select[0], self.select[1])
                        mouse_click(self.ok[0], self.ok[1])
                        time.sleep(num * 3)
                    elif result_num < 7:
                        # Directly save small result sets
                        mouse_click(self.zotero[0], self.zotero[1])
                        mouse_click(self.select[0], self.select[1])
                        mouse_click(self.ok[0], self.ok[1])
                        time.sleep(num * 3)
                except ValueError:
                    logging.error(f"Invalid result count '{result_count}' for query '{query}'")

            # Write results to CSV
            try:
                with open(csv_file, mode='a', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=["Query", "Result Count", "Database"])
                    if file.tell() == 0:
                        writer.writeheader()
                    writer.writerow({
                        "Query": query_cleaned,
                        "Result Count": result_count,
                        "Database": Database
                    })
                    logging.info(f"Results saved to {csv_file}")
            except FileNotFoundError as e:
                logging.error(f"Error: CSV file '{csv_file}' not found.")
            except Exception as e:
                logging.error(f"An error occurred while saving results to CSV: {e}")

    def get_keyword(self, file_path: str, sheet_name: str) -> List[str]:
        """
        Read an Excel file and extract keywords from a specified sheet.

        :param file_path: The file path to the Excel file.
        :param sheet_name: The name of the sheet within the Excel file to be read.
        :return: A list of combined keywords extracted from the sheet.
        """
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)
            logging.info(f"Excel keywords combination:\n{df}")
            # Combine all columns per row into OR-separated strings
            combined_rows = df.apply(
                lambda row: ' OR '.join(str(item) for item in row if pd.notnull(item) and item != float('nan')), axis=1
            )
            combined_list = combined_rows.tolist()
            return combined_list
        except FileNotFoundError as e:
            logging.error(f"File '{file_path}' not found: {e}")
            print(f"Error: File '{file_path}' not found.")
            return []
        except Exception as e:
            logging.error(f"An error occurred while reading Excel file: {e}")
            print(f"An error occurred while reading Excel file: {e}")
            return []


def main() -> None:
    """Main function to execute the search automation script."""
    try:
        Chromealert()

        # Initialize the SearchAutomation class
        search_automation = SearchAutomation()

        # Read the keyword sets from the specified Excel file and sheet
        keyword1 = search_automation.get_keyword(EXCEL_FILE_PATH, "Keyword1")
        keyword2 = search_automation.get_keyword(EXCEL_FILE_PATH, "Keyword2")
        keyword3 = search_automation.get_keyword(EXCEL_FILE_PATH, "Keyword3")
        keyword4 = search_automation.get_keyword(EXCEL_FILE_PATH, "Keyword4")
        keyword5 = search_automation.get_keyword(EXCEL_FILE_PATH, "Keyword5")

        # Define a function to generate query combinations and save them to a CSV file
        def generate_and_save_queries(
                keysets: List[list],
                csv_file: str,
                Database: str,
                zotero_save: bool,
                search_count_start: int
        ) -> None:
            queries = search_automation.query_combine(search_count_start, *keysets)
            search_automation.save_to_csv(queries, csv_file, Database, zotero_save, search_count_start)

        database = DATABASE_LIST[0]

        # Generate and save query combinations
        generate_and_save_queries([keyword1], ROOT_DIR + database + "_search_results1.csv", database, False, SEARCH_COUNT_START)
        generate_and_save_queries([keyword1, keyword2], ROOT_DIR + database + "_search_results12.csv", database, False, SEARCH_COUNT_START)
        generate_and_save_queries([keyword1, keyword2, keyword3], ROOT_DIR + database + "_search_results123.csv", database, True, SEARCH_COUNT_START)
        generate_and_save_queries([keyword1, keyword2, keyword3, keyword4], ROOT_DIR + database + "_search_results1234.csv", database, True, SEARCH_COUNT_START)
        generate_and_save_queries([keyword1, keyword2, keyword3, keyword5], ROOT_DIR + database + "_search_results1235.csv", database, True, SEARCH_COUNT_START)
        generate_and_save_queries([keyword1, keyword2, keyword3, keyword4, keyword5], ROOT_DIR + database + "_search_results1235.csv", database, True, SEARCH_COUNT_START)
        endalert()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()