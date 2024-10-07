
# Movie Review Sentiment Analyzer

## Project Overview

Hey there! Welcome to the **Movie Review Sentiment Analyzer** project. This project uses **machine learning** and **Natural Language Processing (NLP)** to figure out if a movie review is **positive** or **negative**. You feed it a bunch of movie reviews, and it can predict how people feel about the movie based on what they’ve said.

Whether you’re analyzing customer feedback, movie reviews, or even product reviews, this kind of tool helps you understand overall sentiment quickly and efficiently.

### What Does the Project Do?
- **Text Preprocessing**: Cleans up the text data by removing noise (like punctuation and unnecessary words).
- **Machine Learning**: Uses two different models, **Logistic Regression** and **Naive Bayes**, to classify reviews.
- **Performance Evaluation**: Measures how well these models perform by calculating their accuracy.

---

## Features
- **NLP Preprocessing**: Tokenization, stop word removal, and lemmatization to clean and prepare the text.
- **Two Classifiers**: Logistic Regression and Naive Bayes, both popular models for text classification.
- **Scalable Dataset**: The project currently works with a dataset of **10,000 reviews** (5,000 positive, 5,000 negative).
  
---

## How to Set Up the Project

### 1. Clone the Project
First, clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/movie_review_sentiment_analyzer.git
cd movie_review_sentiment_analyzer
```

### 2. Set Up a Python Virtual Environment

Create a virtual environment to isolate project dependencies. It’s good practice and keeps things clean.

#### On Windows:
```bash
python -m venv venv
venv\Scriptsctivate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the Dependencies

Everything you need to run this project is listed in `requirements.txt`. Run this to install them:

```bash
pip install -r requirements.txt
```

### 4. Generate the Dataset (Optional)

If you don’t have the dataset already, you can generate a new one using the provided script:

```bash
python generate_large_dataset.py
```

This will create an Excel file named **`imdb_reviews_large_10000.xlsx`** containing 10,000 movie reviews.

---

## Running the Sentiment Analyzer

Once everything is set up, it’s time to see the magic in action!

Just run the `main.py` script, and it will load the dataset, preprocess the reviews, train two models (Logistic Regression and Naive Bayes), and print out their accuracy.

```bash
python main.py
```

### What Happens When You Run It?

1. **Loads the Dataset**: It reads from the Excel file (`imdb_reviews_large_10000.xlsx`).
2. **Cleans Up the Reviews**: Removes unnecessary text, breaks the reviews down into words, and prepares them for the model.
3. **Trains the Models**: Both models (Logistic Regression and Naive Bayes) are trained on 80% of the data.
4. **Evaluates the Models**: The models are tested on the remaining 20% of the data, and their accuracy is printed out.

### Example Output

```
Loading dataset from imdb_reviews_large_10000.xlsx...
Dataset successfully loaded.
Logistic Regression Accuracy: 85.00%
Naive Bayes Accuracy: 83.50%
```

---

## Project Structure

Here's a quick breakdown of how everything is organized:

```
movie_review_sentiment_analyzer/
│
├── venv/                       # Virtual environment folder (auto-generated)
├── imdb_reviews_large_10000.xlsx  # Dataset file containing 10,000 movie reviews
├── data_preprocessing.py        # Python script for cleaning up and preprocessing the text
├── model_training.py            # Script for training the models (Logistic Regression, Naive Bayes)
├── main.py                      # Main script that brings everything together and runs the project
├── generate_large_dataset.py     # Script to generate a large dataset of movie reviews (10,000 entries)
├── requirements.txt             # List of Python dependencies needed for the project
└── README.md                    # You're reading this!
```

---

## How It Works

### 1. **Text Preprocessing**:
- **Cleaning the Text**: Removes punctuation, numbers, and common words (like ‘the’ and ‘is’) that don’t add much value.
- **Tokenizing the Text**: Splits the review into individual words (called tokens).
- **Lemmatization**: Reduces words to their base form (e.g., "running" becomes "run").

### 2. **Model Training**:
We use two machine learning models:
- **Logistic Regression**: A simple, linear model that’s great for classification tasks like this.
- **Naive Bayes**: A probabilistic model that assumes every word is independent of the others—simple, fast, and surprisingly effective for text classification.

### 3. **Model Evaluation**:
Once the models are trained, we test them on unseen reviews and calculate their **accuracy**—basically, how many reviews they got right.

---

## Customization

Want to make this project your own? Here are a few ideas:

- **Increase Dataset Size**: You can easily modify the `generate_large_dataset.py` script to create a bigger dataset (e.g., 20,000 or 50,000 reviews).
- **Add More Models**: Feel free to experiment with other machine learning algorithms like **Support Vector Machines (SVM)** or **Random Forest**.
- **Expand Sentiment Classes**: Right now, the project only classifies reviews as positive or negative. You could add a third class, like **neutral** reviews, to make it more sophisticated.

---

## Future Enhancements

Here are some things we could do to make this project even better:

- **Deploy as a Web App**: Imagine a simple web app where users can input their own reviews and get instant predictions. This could be super helpful for businesses that want real-time feedback analysis.
- **Add More Sentiment Categories**: Instead of just positive or negative, we could include neutral or even multi-level sentiment (e.g., very positive, somewhat negative).
- **Hyperparameter Tuning**: We could use tools like GridSearchCV to fine-tune the model’s settings and improve performance.

---

## Requirements

- **Python 3.7+**
- **Required Libraries**:
  - `pandas`
  - `scikit-learn`
  - `nltk`
  - `openpyxl` (for Excel file handling)

To install all the dependencies, just run:

```bash
pip install -r requirements.txt
```

---

## Conclusion

That’s the **Movie Review Sentiment Analyzer** in a nutshell. With this project, you can quickly get a feel for what people think about a movie just by analyzing their reviews. It's a simple but powerful way to dig into customer feedback and understand sentiment at scale.

Feel free to play around with the models, dataset, or preprocessing steps to make this project your own!

---

## License

This project is open-source and available under the [MIT License](LICENSE).
