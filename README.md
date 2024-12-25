<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMDB Movie Review Using RNN</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2 {
            color: #0056b3;
        }
        a {
            color: #0056b3;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        code {
            background-color: #eef;
            padding: 2px 4px;
            font-family: Consolas, monospace;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-left: 3px solid #ccc;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>IMDB Movie Review Using RNN</h1>
    <p>This project leverages a Recurrent Neural Network (RNN) to analyze and classify movie reviews from the IMDB dataset. By training the model on labeled data, it predicts whether a review is positive or negative.</p>
    
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#dataset">Dataset</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#model-architecture">Model Architecture</a></li>
        <li><a href="#results">Results</a></li>
        <li><a href="#future-work">Future Work</a></li>
        <li><a href="#license">License</a></li>
    </ul>

    <h2 id="overview">Overview</h2>
    <p>The goal of this project is to use an RNN-based deep learning model to perform sentiment analysis on the IMDB movie reviews dataset. The RNN captures the sequential nature of text data to understand the sentiment behind each review.</p>
    
    <h2 id="features">Features</h2>
    <ul>
        <li>Preprocessing text data with tokenization and padding.</li>
        <li>Implementing RNN layers using frameworks like TensorFlow or PyTorch.</li>
        <li>Training and evaluating the model for binary classification (positive or negative sentiment).</li>
        <li>Visualization of accuracy and loss metrics.</li>
    </ul>

    <h2 id="dataset">Dataset</h2>
    <p>The IMDB dataset is a popular benchmark dataset for sentiment analysis. It contains 50,000 reviews:</p>
    <ul>
        <li>25,000 labeled for training.</li>
        <li>25,000 labeled for testing.</li>
    </ul>
    <p>The dataset is available via the <a href="https://keras.io/api/datasets/imdb/" target="_blank">Keras datasets module</a>.</p>

    <h2 id="installation">Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone &lt;repository_url&gt;<br>cd IMDB_Movie_Review_Using_RNN</code></pre>
        </li>
        <li>Install dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>

    <h2 id="usage">Usage</h2>
    <ol>
        <li>Run the preprocessing script to tokenize and pad the text data:
            <pre><code>python preprocess.py</code></pre>
        </li>
        <li>Train the RNN model:
            <pre><code>python train.py</code></pre>
        </li>
        <li>Evaluate the model on test data:
            <pre><code>python evaluate.py</code></pre>
        </li>
        <li>Visualize metrics:
            <pre><code>python plot_metrics.py</code></pre>
        </li>
    </ol>

    <h2 id="model-architecture">Model Architecture</h2>
    <p>The model uses:</p>
    <ul>
        <li><strong>Embedding Layer:</strong> Converts words into dense vectors.</li>
        <li><strong>RNN/LSTM Layer:</strong> Processes sequential data.</li>
        <li><strong>Dense Layer:</strong> Outputs a probability score for binary classification.</li>
    </ul>
    <p>Hyperparameters:</p>
    <ul>
        <li>Embedding Dimension: 128</li>
        <li>Hidden Units: 64</li>
        <li>Batch Size: 32</li>
        <li>Epochs: 10</li>
    </ul>

    <h2 id="results">Results</h2>
    <ul>
        <li><strong>Accuracy:</strong> Achieved ~90% accuracy on the test dataset.</li>
        <li><strong>Loss:</strong> Demonstrates strong generalization on unseen data.</li>
    </ul>

    <h2 id="future-work">Future Work</h2>
    <ul>
        <li>Implement attention mechanisms for improved performance.</li>
        <li>Experiment with GRU and Transformer-based architectures.</li>
        <li>Fine-tune embeddings using pre-trained word vectors (e.g., GloVe, Word2Vec).</li>
    </ul>

    <h2 id="license">License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>
</body>
</html>
