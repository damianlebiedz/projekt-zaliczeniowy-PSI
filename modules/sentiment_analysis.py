import torch
from transformers import DistilBertTokenizer, DistilBertModel, pipeline
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    score = result['score']
    return score if result['label'] == 'POSITIVE' else -score

def add_sentiment_column(df):
    df['sentiment'] = df['text'].apply(analyze_sentiment)
    return df

def calculate_weighted_sentiment(df):
    weighted_sum = (df['sentiment'] * df['upvotes']).sum()
    total_upvotes = df['upvotes'].sum()

    if total_upvotes == 0:
        return 0

    weighted_average = weighted_sum / total_upvotes
    return weighted_average

def cluster_pca_kmeans(embeddings, n_clusters=5):
    pca = PCA(n_components=50)
    x_reduced = pca.fit_transform(embeddings)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(x_reduced)

    return clusters