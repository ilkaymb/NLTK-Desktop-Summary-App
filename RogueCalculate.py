from nltk.translate.bleu_score import sentence_bleu
from rouge import Rouge

def RogueScore(text1, text2):
    def calculate_rouge_score(reference, summary):

        rouge = Rouge()
        scores = rouge.get_scores(summary, reference)
        rouge_1_score = scores[0]["rouge-1"]["f"]
        rouge_2_score = scores[0]["rouge-2"]["f"]
        rouge_l_score = scores[0]["rouge-l"]["f"]
        return rouge_1_score, rouge_2_score, rouge_l_score

    rouge_1, rouge_2, rouge_l = calculate_rouge_score(text1, text2)

    print("ROUGE-1 Score:", rouge_1)
    print("ROUGE-2 Score:", rouge_2)
    print("ROUGE-L Score:", rouge_l)

    return rouge_1, rouge_2, rouge_l