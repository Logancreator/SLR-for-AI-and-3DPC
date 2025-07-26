# Phenomics Review Analysis

This repository contains scripts for analyzing phenomics literature data and demonstrating an automated systematic literature review (SLR) search methodology. It includes R scripts for data visualization and Python scripts showcasing GUI-based automation logic.

## Directory Structure
- `data/`: Raw data files (e.g., `SLR Data Table6.xlsx`, `Final.csv`, `SLR-Information2.xlsx`) - not included due to size; add your own.
- `figure/`: Generated plots from R scripts.
- `scripts/`: Analysis and automation scripts.
  - `r/`: R scripts for data analysis and visualization.
    - `01_data_loading.R`: Loads and merges data.
    - `02_item_type_analysis.R`: Analyzes item type distribution.
    - `03_year_study_analysis.R`: Visualizes publication trends by year.
    - `04_author_analysis.R`: Analyzes author count distribution.
    - `05_country_analysis.R`: Analyzes country distribution.
    - `06_plant_analysis.R`: Analyzes plant type distribution.
    - `07_dl_ml_analysis.R`: Visualizes DL/ML trends.
    - `08_sensor_analysis.R`: Analyzes sensor type trends.
    - `09_algorithm_analysis.R`: Categorizes and visualizes algorithms.
    - `10_public_data_analysis.R`: Analyzes public data usage.
    - `utils.R`: Utility functions for plotting themes.
  - `python/`: Python scripts for automation (demonstration purposes).
    - `mouse_position_tracker.py`: Tracks and saves mouse positions on click.
    - `search_automation.py`: Demonstrates automated searching on OneSearch using keyword combinations (logic showcase only).

## Prerequisites

### For R Scripts
- R (version 4.0 or higher)
- R packages: `readxl`, `dplyr`, `ggplot2`, `tidyr`, `ggsci`, `viridis`, `gridExtra`, etc. (Install via `install.packages()`).

### For Python Scripts
- Python (version 3.7 or higher)
- Python packages: `pyautogui`, `pyperclip`, `pandas`, `pynput` (Install via `pip install <package>`).
- Chrome browser with Zotero and Zotero Connector plugins (historical context; not required for current use).

## Usage

### R Analysis
1. Place data files (`SLR Data Table6.xlsx`, `Final.csv`) in the `data/` directory.
2. Update the `setwd()` path in `scripts/r/01_data_loading.R` to your local directory.
3. Run the R scripts in order (01 to 10) to generate figures in the `figure/` directory.

### Python Automation (Demonstration Only)
**Note**: The Python scripts are provided to illustrate automation logic and methodology. Due to their GUI-based nature and reliance on the OneSearch database interface as of April 2024, they are likely outdated as database formats may have changed over time. They are not intended for current use but serve as a reference for adapting similar automation tasks.

1. **Mouse Position Tracker**:
   - Run `python scripts/python/mouse_position_tracker.py` to log mouse positions on left-click.
   - Output is saved to `mouse_positions.txt`.
   - Stop with `Ctrl+C`.
   - This script remains functional for general mouse tracking purposes.

2. **Search Automation**:
   - **Purpose**: Demonstrates a method for automating searches in OneSearch using keyword combinations from an Excel file (`SLR-Information2.xlsx`) and saving results to CSV files.
   - **Historical Context**: Designed for a specific GUI layout as of April 2024, with hardcoded coordinates and Zotero integration.
   - **Current Status**: Likely non-functional due to potential updates in the OneSearch interface. Use as a template for building similar automation scripts by updating coordinates and logic to match current database UIs.
   - To explore the logic:
     - Review `scripts/python/search_automation.py`.
     - Adjust `EXCEL_FILE_PATH` and coordinates if adapting to a new environment.

## Notes
- **R Scripts**: Fully functional for analyzing the provided dataset and generating visualizations.
- **Python Scripts**: 
  - `mouse_position_tracker.py` is a general-purpose tool and remains usable.
  - `search_automation.py` is a demonstration of GUI automation logic. To adapt it for modern use, update screen coordinates (use `mouse_position_tracker.py` to find new ones) and modify interactions based on the current database interface.

## Output
- **R**: Plots saved as PDFs in `figure/`.
- **Python**: 
  - `mouse_positions.txt` for mouse tracking.
  - Historical CSV files (e.g., `IEEE Xplore_search_results123.csv`) from `search_automation.py` (demonstration output only).