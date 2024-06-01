from content.llms import LLMS

class QuizAgent:
    def __init__(self, topic, text):
        self.topic = topic
        self.text = text

    def get_quiz(self):
        prompt = """
        Create a quiz on the topic of """+self.topic+""" based on the following text: """+self.text+""".The quiz should consist of 7 multiple-choice questions. Each question should have 4 options and only one correct answer. Please provide the questions, options, and the correct answer in the below format only please:[{"question": "Sample question?","options": ["Option 1", "Option 2", "Option 3", "Option 4"],"answer": "a"},// ... rest of the questions]
        """

        model = LLMS("GEMINI")
        result = model.run(prompt)
        
        if result.candidates and result.candidates[0].content.parts:
            return result.candidates[0].content.parts[0].text
        else:
            return result.text