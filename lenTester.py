text = "In today’s digital age, social media has become the primary source of news, significantly increasing the spread and reach of fake news. To tackle this issue, Machine Learning and NLP methods have been used, allowing us to process large datasets to detect patterns in fake news using features like text semantics, word frequency, and sentiment analysis. Along with these methods, this paper applies techniques like stance detection, which help in identifying the sentiment of a post. Some advanced algorithms can analyze user behavior and information propagation patterns on OSNs to detect the flow of fake news and distinguish it from legitimate content. Engaging users to flag and verify fake news articles shows some promise because of the scale it can reach, but it is prone to user biases, leading to the formation of echo chambers, which can cause more harm than good. The Machine Learning models and stance detection techniques struggle with accuracy and scalability, especially when dealing with more sophisticated forms of misinformation. The methods deployed here lack real-time fake news detection, which is critical for preventing the rapid spread of misinformation on social media. Linguistic approaches that flag certain nouns, pronouns, etc., may fail when dealing with satire, humor, or complex sentence structures that may look like real news, making it difficult to distinguish between false and true news."
newtext = text.split()

print(len(newtext))


