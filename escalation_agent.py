class EscalationAgent:

    def check(self, sentiment, category):

        if sentiment == "Negative":
            return True

        if category == "Complaint":
            return True

        return False