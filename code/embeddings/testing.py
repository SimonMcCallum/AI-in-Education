import os
import openai
import json
from PyQt5 import QtWidgets, QtGui, QtCore
from scipy.spatial.distance import cosine, euclidean
import numpy as np

# Retrieve your OpenAI API key from system environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("The OpenAI API key is missing. Please set the environment variable 'OPENAI_API_KEY'.")

def get_embedding(text, model="text-embedding-3-large"):
    try:
        response = openai.embeddings.create(
            input=[text],
            model=model
        )
        embedding = response.data[0].embedding
        return embedding
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_embedding(text, embedding, filename='embeddings.json'):
    data = {
        'text': text,
        'embedding': embedding
    }
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            all_data = json.load(file)
            all_data.append(data)
    else:
        all_data = [data]
    with open(filename, 'w') as file:
        json.dump(all_data, file)

def load_embeddings(filename='embeddings.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            all_data = json.load(file)
            return all_data
    return []

class EmbeddingApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Embedding Visualizer')
        
        self.layout = QtWidgets.QVBoxLayout()

        self.text_input = QtWidgets.QLineEdit(self)
        self.text_input.setPlaceholderText("Enter text to get embedding")
        self.layout.addWidget(self.text_input)

        self.get_embedding_btn = QtWidgets.QPushButton('Get Embedding', self)
        self.get_embedding_btn.clicked.connect(self.get_embedding)
        self.layout.addWidget(self.get_embedding_btn)

        self.embedding_display = QtWidgets.QTextEdit(self)
        self.embedding_display.setReadOnly(True)
        self.layout.addWidget(self.embedding_display)

        self.compare_btn = QtWidgets.QPushButton('Compare Embeddings', self)
        self.compare_btn.clicked.connect(self.compare_embeddings)
        self.layout.addWidget(self.compare_btn)
        
        self.result_display = QtWidgets.QLabel(self)
        self.layout.addWidget(self.result_display)

        self.setLayout(self.layout)

    def get_embedding(self):
        text = self.text_input.text()
        if text:
            embedding = get_embedding(text)
            if embedding:
                save_embedding(text, embedding)
                self.embedding_display.setText(f"Embedding for '{text}':\n{embedding}")
            else:
                self.embedding_display.setText("Error retrieving embedding.")
        else:
            self.embedding_display.setText("Please enter text.")

    def compare_embeddings(self):
        embeddings = load_embeddings()
        if len(embeddings) < 2:
            self.result_display.setText("Need at least two embeddings to compare.")
            return

        text1, ok1 = QtWidgets.QInputDialog.getText(self, 'Select Text 1', 'Enter text 1:')
        if not ok1 or not text1:
            return
        text2, ok2 = QtWidgets.QInputDialog.getText(self, 'Select Text 2', 'Enter text 2:')
        if not ok2 or not text2:
            return

        embedding1 = next((item['embedding'] for item in embeddings if item['text'] == text1), None)
        embedding2 = next((item['embedding'] for item in embeddings if item['text'] == text2), None)

        if embedding1 and embedding2:
            cos_dist = cosine(embedding1, embedding2)
            euc_dist = euclidean(embedding1, embedding2)
            self.result_display.setText(f"Cosine Distance: {cos_dist:.4f}\nEuclidean Distance: {euc_dist:.4f}")
        else:
            self.result_display.setText("One or both embeddings not found.")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = EmbeddingApp()
    ex.show()
    sys.exit(app.exec_())
