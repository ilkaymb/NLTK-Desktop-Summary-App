from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Örnek metinler
def TFIDF_Function(data):
    similarity_data = []
    labelData = {}
    # TfidfVectorizer örneği oluşturma
    vectorizer = TfidfVectorizer()

    # Belge vektörlerini oluşturma ve TF-IDF hesaplaması
    tfidf_matrix = vectorizer.fit_transform(data)

    # Bütün belgeler arasındaki benzerlik skorlarını hesaplama
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Benzerlik skorlarını yazdırma
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            similarity_score = similarity_matrix[i][j]
            print(
                "Cümle",
                i + 1,
                "ile cümle",
                j + 1,
                "arasındaki benzerlik skoru:",
                similarity_score,
            )

            similarity_data.append(similarity_score)

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            similarity_score = similarity_matrix[i][j]
            labelData[(data[i], data[j])] = f"{similarity_score:.3f}"

    return labelData
