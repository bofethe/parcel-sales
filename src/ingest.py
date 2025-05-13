import geopandas as gpd
import pandas as pd
import zipfile
import os
from pathlib import Path
import glob

RAW_DIR = Path('data/raw')
INTERIM_DIR = Path('data/interim')
PROCESSED_DIR = Path('data/processed')

def unzip_all_zipfiles():
    '''Extract all .zip files from raw to interim directory'''

    for zip_path in RAW_DIR.glob('*.zip'):
        extract_dir = INTERIM_DIR / zip_path.stem
        extract_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print(f'✅ Extracted {zip_path.name} to {extract_dir}')

def find_latest_version(prefix: str) -> Path:
    '''Find the latest unzipped folder for a given prefix like allsales or parcel'''

    candidates = sorted(INTERIM_DIR.glob(f'{prefix}_*'), reverse=True)
    if not candidates:
        raise FileNotFoundError(f'No folder found for prefix "{prefix}" in interim/')
    return candidates[0]

def load_and_process_data():
    '''Load and process data from interim directory, merge parcel tables, and export to parquet in raw directory'''

    # Locate unzipped folders
    sales_dir = find_latest_version('allsales')
    parcel_dir = find_latest_version('parcel')

    # Find files inside them
    sales_path = next(sales_dir.glob('*.dbf'), None)
    parcel_path = next(parcel_dir.glob('parcel.dbf'), None)
    sub_path = next(parcel_dir.glob('parcel_sub_names.dbf'), None)
    dor_path = next(parcel_dir.glob('parcel_dor_names.dbf'), None)

    if not all([sales_path, parcel_path, sub_path, dor_path]):
        raise FileNotFoundError('Missing one or more required .dbf files.')

    # Load data
    df_sales = gpd.read_file(sales_path, encoding='ISO-8859-1')
    df_parcel = gpd.read_file(parcel_path)
    df_sub = gpd.read_file(sub_path)[['SUBCODE', 'SUBNAME']].drop_duplicates()
    df_dor = gpd.read_file(dor_path)

    # Merge descriptions into parcel data
    df_parcel = df_parcel.merge(df_dor, left_on='DOR_C', right_on='DORCODE', how='left').drop(columns=['DOR_C'])
    df_parcel = df_parcel.merge(df_sub, left_on='SUB', right_on='SUBCODE', how='left').drop(columns=['SUB'])

    # Export to Parquet
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df_sales.to_parquet(PROCESSED_DIR / 'allsales.parquet', engine='pyarrow')
    df_parcel.to_parquet(PROCESSED_DIR / 'parcel.parquet', engine='pyarrow')
    print('✅ Exported to Parquet.')

if __name__ == '__main__':
    unzip_all_zipfiles()
    load_and_process_data()