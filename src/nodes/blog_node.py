from src.states.blogstate import BlogState

class BlogNode:
    """
    A class to represent the blog node
    """

    def __init__(self,llm):
        self.llm=llm

    def title_creation(self,state:BlogState):
        """
        Create the title for the blog
        """
        if "topic" in state and state["topic"]:
            prompt="""
                        You are an expert blog content writer.Use Markdown formatting.Generate a blog title for the topic {topic}.This title should be creative and SEO friendly
                    """
            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog":{"title":response.content}}
        
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """You are an expert blog writerl.Use markdown formatting. 
            Generate a detailed blog content with a detailed breakdown for the topic {topic}"""
            sysem_message = system_prompt.format(topic=state["topic"])
            resposne = self.llm.invoke(sysem_message)
            return {"blog": {"title":state["blog"]["title"], "content":resposne.content}}