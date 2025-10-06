import pytest
from src.crew.support_crew import SupportCrew

class TestSupportCrew:
    def test_crew_initialization(self):
        """Test that the support crew initializes properly"""
        crew = SupportCrew()
        assert crew is not None
        
    def test_process_inquiry(self):
        """Test processing a sample inquiry"""
        crew = SupportCrew()
        customer_info = {
            "customer": "TestCustomer",
            "person": "Test Person",
            "inquiry": "How do I set up a crew with memory?"
        }
        
        result = crew.process_inquiry(customer_info)
        assert result is not None
        assert len(str(result)) > 0