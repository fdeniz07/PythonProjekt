from utils import load_text
from tokenizer import tokenize_text
from frequency import calculate_word_frequencies
from summarizer import (
    score_sentences,
    generate_summary
)

def main():
    
    text = load_text("ClimateScienceText.txt")

    tokens = tokenize_text(text)

    # print("First 50 Tokens:\n")

    # print(tokens[:50])

    # print(f"\nTotal Tokens: {len(tokens)}")

    word_frequencies = calculate_word_frequencies(tokens)

    # print("=" * 60)
    # print("Normalized Word Frequencies")
    # print("=" * 60)

    # for word, frequency in list(word_frequencies.items())[:30]:
    #     print(f"{word:<20} {frequency:.2f}")
    
    sentence_scores = score_sentences(
        text,
        word_frequencies
    )

    # print("=" * 80)
    # print("Sentence Scores")
    # print("=" * 80)

    # for sentence, score in sentence_scores.items():

    #     print(f"{score:.2f}")

    #     print(sentence)

    #     print("-" * 80)

    summary = generate_summary(
            sentence_scores,
            text
        )

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    print(summary)


if __name__ == "__main__":
    main()