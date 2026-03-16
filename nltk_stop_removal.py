#nltk.download('stopwords')

from nltk.corpus import stopwords
import pandas

data = pandas.read_csv("data/interim_data/words.csv")

stop_words = set(stopwords.words("german"))
data_clean = data[data["word"].isin(stop_words)]
data_clean.to_csv("data/interim_data/these_are_stopwords.csv", index=False)

data_clean_2 = data[~data["word"].isin(stop_words)]
data_clean_2.to_csv("data/interim_data/these_are_not_stopwords.csv", index=False)