# Deep-NLP-labs

Набор проектных заданий по обработке естественного языка.  
Каждый из проектов демонстрирует отдельный аспект работы с текстами: классификация, токенизация, тематическое моделирование и сравнение алгоритмов.

## Содержание

### [1. Tokenizer + Naive Bayes Classification](tokenizer_downsampling/)
Построение пайплайна классификации текста с использованием кастомного токенизатора (по архитектуре Карпатного). Балансировка классов с помощью downsampling, параллельный препроцессинг (`pandarell`), обучение наивного байесовского классификатора и анализ влияния размера словаря на качество модели.

### [2. Sentiment Classification: KNN vs SVM vs Random Forest](sentiment-classification/)
Объединение положительных и отрицательных текстов, стратифицированное разбиение, обучение трёх классических алгоритмов (KNN, SVM, Random Forest) и сравнение F1-score по классам.

### [3. Topic Modeling on Lemmatized Texts](topic-modeling-lda/)
Построение тематической модели на лемматизированных текстах. 

### [4. Text Classification on Fake News Dataset: MLP vs CNN](text-classification-embeddings/README.md)
Классификация текстов с использованием эмбеддингов. Сравнение MLP (с dropout и batchnorm) и сверточной CNN-модели. 


### [5. Classical NLP & Word Embedding Translator](classical-nlp/README.md)
Работа с текстами до эпохи трансформеров: ручной отбор признаков, лемматизация, векторизация (`CountVectorizer`, `TF-IDF`) и реализация word-by-word переводчика на основе эмбеддингов.
