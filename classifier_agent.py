class ClassifierAgent:

    def classify(self, query):

        query = query.lower()

        if "refund" in query:
            return "Refund Request"

        elif "payment" in query:
            return "Billing"

        elif "error" in query:
            return "Technical Support"

        elif "complaint" in query:
            return "Complaint"

        elif "product" in query:
            return "Product Information"

        else:
            return "General Inquiry"