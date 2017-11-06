from twython import Twython
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Replace the following strings with your own keys and secrets
TOKEN = '925049359494008832-aaFvMGPncgNY57ehRtbzg8xWvjr4YHo'
TOKEN_SECRET = 'gYEKBFybItZZwZCFMJJgZgIisVU81OQh5zEaGneaaXn9e'
CONSUMER_KEY = 'H8M02nqRAVOl4s7dkjwqmHTBJ'
CONSUMER_SECRET = 'ftgVg0rJ8m6l3i6h4YC5cSbv1mt6l9Qe9FLM2VvULPNMNRQfnn'


t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

#data = t.search(q="The Dark Knight", count=1000)


#for status in data['statuses']:
# print(status['text'])

sentence = 'Software Design is my favorite class because learning Python is so cool!'
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score) 

top5_m = ["Iron Man", "The Avengers", "Spider-Man: Homecoming", "Guardians of the Galaxy", "Captain America: Civil War"]
top5_dc = ["The Dark Knight", "Batman Begins", "The Dark Knight Rises", "Wonder Woman", "V for Vendetta"]

def marvel_vs_dc(co_1, co_2):
    both = [co_1, co_2]
    avg_score_1 = dict()
    avg_score_2 = dict()
    for co in both:
        count = 0
        for movie in co:
            data = t.search(q="movie", count = 50)
            for status in data['statuses']:
                count += 1
                status = str(status)
                score = SentimentIntensityAnalyzer().polarity_scores(status)
                if co == co_1:
                    for key, value in score.items():
                        avg_score_1[key] = (avg_score_1.get(key, 0) + value)        
                if co == co_2:
                    for key, value in score.items():
                        avg_score_2[key] = (avg_score_1.get(key,0) + value)
    count = count
    for key, value in avg_score_1.items():
        avg_score_1[key] = (value/count)
    for key, value in avg_score_2.items():
        avg_score_2[key] = (value/count)                        
    print ("Dc has a score of {}".format(avg_score_1))
    print ("Marvel has a score of {}".format(avg_score_2))
    if avg_score_1['pos'] - avg_score_1['neg'] < avg_score_2['pos'] - avg_score_2['neg']:
        print ("Marvel Wins!")   
    elif avg_score_1['pos'] - avg_score_1['neg'] == avg_score_2['pos'] - avg_score_2['neg']:
        print ("They Tie.")
    else:
        print ("DC Wins!")
        



print(marvel_vs_dc(top5_dc, top5_m))