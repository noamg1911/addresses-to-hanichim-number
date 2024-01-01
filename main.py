import pandas as pd
from amnon_distance_calculator import AmnonDistanceCalculator

SOURCE_ADDRESS = "אמנון, ישראל"  # Set your desired source address here
INPUT_HANICHIM_FILE = "hanichim-encoded.csv"
OUTPUT_HANICHIM_FILE = "sorted_distances.xlsx"
NAME_EXCEL_INDEX = 0
ADDRESS_EXCEL_INDEX = 1
DISTANCE_EXCEL_INDEX = 2


def main():
    amnon_distance_calculator = AmnonDistanceCalculator(SOURCE_ADDRESS)
    hanichim_dataset = pd.read_csv(INPUT_HANICHIM_FILE, encoding='utf-8')
    hanichim_dataset["Distance"] = hanichim_dataset["Address"].apply(amnon_distance_calculator.get_distance_from_address)
    hanichim_dataset = hanichim_dataset.sort_values(by=["Distance"])
    print(hanichim_dataset)
    hanichim_dataset.to_excel(OUTPUT_HANICHIM_FILE)


if __name__ == "__main__":
    main()

