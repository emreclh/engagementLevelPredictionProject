import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import sys

# Çıktıları dosyaya yönlendir
sys.stdout = open('model_performance_report.txt', 'w')

try:
    print("1. Loading Data...")
    df = pd.read_csv('online_gaming_behavior_dataset.csv')
    
    # Gereksiz sütunu çıkar
    if 'PlayerID' in df.columns:
        df = df.drop('PlayerID', axis=1)

    print("2. Preprocessing Data...")
    # Hedef değişkeni ayır
    le = LabelEncoder()
    df['EngagementLevel_Encoded'] = le.fit_transform(df['EngagementLevel'])
    
    # X (Features) ve y (Target)
    X = df.drop(['EngagementLevel', 'EngagementLevel_Encoded'], axis=1)
    y = df['EngagementLevel_Encoded']
    
    # Kategorik değişkenleri One-Hot Encode yap
    categorical_cols = X.select_dtypes(include=['object']).columns
    X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    
    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("3. Training Model (Random Forest)...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    print("4. Evaluating Model...")
    y_pred = rf_model.predict(X_test)
    
    # Sonuçları Yazdır
    print("\nModel Accuracy Score:")
    print(rf_model.score(X_test, y_test))
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=le.classes_))
    
    # --- GÖRSELLEŞTİRME ---
    
    # 1. Confusion Matrix
    plt.figure(figsize=(8, 6))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=le.classes_, yticklabels=le.classes_)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix - Engagement Level Prediction')
    plt.tight_layout()
    plt.savefig('confusion_matrix.png')
    plt.close()
    
    # 2. Feature Importance
    feature_importances = pd.Series(rf_model.feature_importances_, index=X.columns)
    plt.figure(figsize=(10, 8))
    feature_importances.nlargest(10).plot(kind='barh')
    plt.title('Top 10 Most Important Features')
    plt.xlabel('Importance Score')
    plt.tight_layout()
    plt.savefig('feature_importance.png')
    plt.close()
    
    print("\nReports generated successfully:")
    print("- model_performance_report.txt (This file)")
    print("- confusion_matrix.png")
    print("- feature_importance.png")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    sys.stdout.close()
