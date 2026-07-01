from agents.classifier_agent import ClassifierAgent
from agents.sentiment_agent import SentimentAgent
from agents.billing_agent import BillingAgent
from agents.tech_support_agent import TechSupportAgent
from agents.escalation_agent import EscalationAgent
from agents.response_agent import ResponseAgent

from database.db import create_ticket


classifier = ClassifierAgent()
sentiment = SentimentAgent()
billing = BillingAgent()
tech = TechSupportAgent()
escalation = EscalationAgent()
response = ResponseAgent()


def process_query(customer_name, query):

    category = classifier.classify(query)

    sentiment_result, priority = sentiment.analyze(query)

    if category in ["Billing", "Refund Request"]:
        support_response = billing.handle(query)

    elif category == "Technical Support":
        support_response = tech.handle(query)

    else:
        support_response = "Support request received."

    final_response = response.generate(
        category,
        support_response
    )

    escalated = escalation.check(
        sentiment_result,
        category
    )

    create_ticket(
        customer_name,
        query,
        category,
        sentiment_result,
        priority
    )

    return {
        "category": category,
        "sentiment": sentiment_result,
        "priority": priority,
        "escalated": escalated,
        "response": final_response
    }