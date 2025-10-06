from crewai import Task
from typing import Dict, Any, List
from src.agents.support_agent import SupportAgent

class InquiryResolutionTask:
    def __init__(self, tools: List = None):
        self.tools = tools or []
        
    def create_task(self, customer_info: Dict[str, Any], support_agent: Agent) -> Task:
        """Create inquiry resolution task"""
        inquiry = customer_info.get('inquiry', '')
        customer = customer_info.get('customer', 'Customer')
        person = customer_info.get('person', 'the customer')
        
        return Task(
            description=(
                f"{customer} just reached out with a super important ask:\n"
                f"{inquiry}\n\n"
                f"{person} from {customer} is the one that reached out. "
                f"Make sure to use everything you know to provide the best support possible. "
                f"You must strive to provide a complete and accurate response."
            ),
            expected_output=(
                "A detailed, informative response to the customer's inquiry that addresses "
                "all aspects of their question.\n"
                "The response should include references to everything you used to find the answer, "
                "including external data or solutions. Ensure the answer is complete, "
                "leaving no questions unanswered, and maintain a helpful and friendly tone."
            ),
            tools=self.tools,
            agent=support_agent,
        )