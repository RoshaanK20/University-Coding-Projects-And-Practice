import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load data
def load_data():
    df = pd.read_csv(r"C:\Users\princ\Desktop\fraud_synthetic_data.csv", parse_dates=["submission_time"])
    return df

# Detect anomalies using Isolation Forest and KMeans
def detect_anomalies(df):
    feature_cols = ['cgpa', 'resume_quality_score', 'previous_applications'] 
    features = df[feature_cols].fillna(0)
    
    # Isolation Forest
    iforest = IsolationForest(contamination=0.05, random_state=42)
    df['iforest_anomaly'] = iforest.fit_predict(features)
    df['iforest_anomaly'] = df['iforest_anomaly'].map({1: 0, -1: 1})  # 1 = anomaly
    
    # K-Means Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['kmeans_cluster'] = kmeans.fit_predict(features)
    
    return df, features, df['iforest_anomaly'].values, kmeans

# Visualize PCA with anomalies
def plot_pca(features, anomaly_labels):
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(features)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1], hue=anomaly_labels, palette=["blue", "red"])
    plt.title("PCA Visualization: Blue=Normal, Red=Anomaly")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.legend(title='Anomaly', labels=['Normal', 'Anomaly'])
    plt.tight_layout()
    plt.show()

# Main flow
def main():
    print("🕵️ Fraud Detection in Internship Applications\n")
    print("Loading dataset...")
    df = load_data()
    
    print("\nFirst 5 records of the dataset:")
    print(df.head())

    print("\nDetecting anomalies...")
    df, features, anomaly_labels, kmeans_model = detect_anomalies(df)

    print("\n--- Anomaly Detection Summary ---")
    print(f"Total Applications: {len(df)}")
    print(f"Detected Anomalies (Isolation Forest): {anomaly_labels.sum()}")
    print(f"Clusters found by K-Means: {kmeans_model.n_clusters}")

    print("\nGenerating PCA Visualization...")
    plot_pca(features, anomaly_labels)

    suspicious_df = df[df['iforest_anomaly'] == 1]
    print("\n--- Suspicious Applications Detected ---")
    print(suspicious_df)

    # Save suspicious applications to CSV
    suspicious_df.to_csv("suspicious_applications.csv", index=False)
    print("\nSuspicious applications saved to 'suspicious_applications.csv'")

if __name__ == "__main__":
    main()
