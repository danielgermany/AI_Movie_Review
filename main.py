import pandas as pd
import os
from data_preprocessing import preprocess_text
from model_training import train_logistic_regression, train_naive_bayes, evaluate_model, vectorize_text
from sklearn.model_selection import train_test_split

# Load Dataset (using a sample IMDB dataset)

def load_dataset():
    file_path = 'imdb_reviews_large_10000.xlsx'
    
    if os.path.exists(file_path):
        # Load the Excel file with 10,000 reviews
        print(f"Loading dataset from {file_path}...")
        dataset = pd.read_excel(file_path)
        print("Dataset successfully loaded.")
        return dataset['review'], dataset['sentiment']
    else:
        raise FileNotFoundError(f"{file_path} not found. Please make sure the file exists in the directory.")


# Main function to execute the pipeline
def main():
    # Step 1: Load dataset
    reviews, sentiments = load_dataset()
    
    # Step 2: Preprocess the text data
    reviews = reviews.apply(preprocess_text)

    # Let's print out the first few preprocessed reviews for inspection
    print("\nSample Preprocessed Reviews:")
    print(reviews.head())
    
    # Step 3: Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(reviews, sentiments, test_size=0.2, random_state=42)
    
    # Step 4: Convert text data to TF-IDF features
    X_train_tfidf, X_test_tfidf, vectorizer = vectorize_text(X_train, X_test)

    # Let's check the feature names (words) the TF-IDF vectorizer is using
    print("\nTF-IDF Features (Top 10):", vectorizer.get_feature_names_out()[:10])
    
    # Step 5: Train Logistic Regression model
    lr_model = train_logistic_regression(X_train_tfidf, y_train)
    lr_accuracy = evaluate_model(lr_model, X_test_tfidf, y_test)
    print(f'Logistic Regression Accuracy: {lr_accuracy * 100:.2f}%')
    
    # Step 6: Train Naive Bayes model
    nb_model = train_naive_bayes(X_train_tfidf, y_train)
    nb_accuracy = evaluate_model(nb_model, X_test_tfidf, y_test)
    print(f'Naive Bayes Accuracy: {nb_accuracy * 100:.2f}%')

if __name__ == '__main__':
    main()
