import pandas

def convert_parquet_to_csv(parquet_file: str, csv_file: str) -> None:
    """
    Convert a Parquet file to a CSV file.

    Args:
        parquet_file (str): Path to the input Parquet file.
        csv_file (str): Path to the output CSV file.
    """
    df = pandas.read_parquet(parquet_file)
    df.to_csv(csv_file, index=False)

convert_parquet_to_csv("../data/processed/cleaned.parquet", "../data/processed/cleaned.csv")