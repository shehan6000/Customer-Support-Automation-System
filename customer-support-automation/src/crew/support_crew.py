from crewai import Crew
from typing import Dict, Any, List
from src.config.settings import settings
from src.agents.support_agent import SupportAgent
from src.agents.qa_agent import QAAgent
from src.tasks.inquiry_resolution import InquiryResolutionTask
from src.tasks.quality_assurance import QualityAssuranceTask
from crewai_tools import ScrapeWebsiteTool

class SupportCrew:
    def __init__(self):
        self.tools = self._setup_tools()
        self.support_agent = SupportAgent(tools=self.tools)
        self.qa_agent = QAAgent()
        self.inquiry_task = InquiryResolutionTask(tools=self.tools)
        self.qa_task = QualityAssuranceTask()
        
    def _setup_tools(self) -> List:
        """Setup tools for the agents"""
        tools = []
        
        if settings.enable_web_scrape:
            # Add documentation scraping tool
            docs_tool = ScrapeWebsiteTool(
                website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
            )
            tools.append(docs_tool)
            
        # Add more tools as needed
        return tools
    
    def process_inquiry(self, customer_info: Dict[str, Any]) -> str:
        """Process customer inquiry through the support crew"""
        try:
            # Create agents
            support_agent_instance = self.support_agent.create_agent(customer_info)
            qa_agent_instance = self.qa_agent.create_agent(customer_info)
            
            # Create tasks
            inquiry_task_instance = self.inquiry_task.create_task(
                customer_info, support_agent_instance
            )
            qa_task_instance = self.qa_task.create_task(
                customer_info, qa_agent_instance
            )
            
            # Create and run crew
            crew = Crew(
                agents=[support_agent_instance, qa_agent_instance],
                tasks=[inquiry_task_instance, qa_task_instance],
                verbose=settings.verbose,
                memory=settings.memory
            )
            
            result = crew.kickoff(inputs=customer_info)
            return result
            
        except Exception as e:
            raise Exception(f"Error processing inquiry: {str(e)}")