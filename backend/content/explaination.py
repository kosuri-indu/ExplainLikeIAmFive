from content.llms import LLMS
import markdown

class ContentAgent:
    def __init__(self, topic):
        self.topic = topic
        self.content = ""

    def to_markdown(self, text):
        markdown_text = markdown.markdown(text)
        return markdown_text
    
    def get_content(self):
        return self.content

    def get_explaination(self):
        prompt = f"""
                 Explain {self.topic} to me like I'm 5!    
                 """
        model = LLMS("GEMINI")
        result = model.run(prompt)

        if result.candidates and result.candidates[0].content.parts:
            self.content += result.candidates[0].content.parts[0].text
            return self.to_markdown(result.candidates[0].content.parts[0].text)
        else:
            return result.text
    
    def get_facts(self):
        prompt = f"""
                Are there cool facts about {self.topic} that I can explain to my little brother/sister?
                 """
        model = LLMS("GEMINI")
        result = model.run(prompt)

        if result.candidates and result.candidates[0].content.parts:
            self.content += result.candidates[0].content.parts[0].text
            return self.to_markdown(result.candidates[0].content.parts[0].text)
        else:
            return result.text

    def get_summary(self):
        prompt = f"""
                In a nutshell, what is {self.topic} all about in 100 words?
                
                 """
        model = LLMS("GEMINI")
        result = model.run(prompt)

        if result.candidates and result.candidates[0].content.parts:
            self.content += result.candidates[0].content.parts[0].text
            return self.to_markdown(result.candidates[0].content.parts[0].text)
        else:
            return result.text

    def get_links(self):
        prompt = f"""
                    Can you give properly working website and youtube links only, that explains {self.topic}? With links in blue
                 """
        model = LLMS("GEMINI")
        result = model.run(prompt)

        if result.candidates and result.candidates[0].content.parts:
            self.content += result.candidates[0].content.parts[0].text
            return self.to_markdown(result.candidates[0].content.parts[0].text)
        else:
            return result.text

#agent = ContentAgent("machine learning")
#print(agent.get_explaination())
#print(agent.get_facts())
#print(agent.get_summary())