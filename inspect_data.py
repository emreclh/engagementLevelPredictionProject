import pandas as pd
import sys

# Çıktıyı dosyaya yönlendir
sys.stdout = open('inspection_results.txt', 'w')

file_path = 'online_gaming_behavior_dataset.csv'

try:
    df = pd.read_csv(file_path)
    print("Dataset Shape:", df.shape)
    print("\nDataset Columns:")
    print(df.columns.tolist())
    print("\nDataset Info:")
    print("-" * 30)
    df.info()
    print("\nFirst 5 Rows:")
    print("-" * 30)
    print(df.head().to_string())
    print("\nMissing Values:")
    print("-" * 30)
    print(df.isnull().sum())
    print("\nDescriptive Statistics:")
    print("-" * 30)
    print(df.describe().to_string())
    
    # Kategorik değişkenlerin benzersiz değer sayıları
    print("\nUnique Values in Categorical Columns:")
    for col in df.select_dtypes(include='object').columns:
        print(f"\n{col}:")
        print(df[col].value_counts())
        
except Exception as e:
    print(f"Error: {e}")
finally:
    sys.stdout.close()
