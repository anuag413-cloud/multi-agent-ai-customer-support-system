class ResponseAgent:

    def generate(self,
                 category,
                 support_response):

        return f"""
Category: {category}

Response:
{support_response}

Thank you for contacting support.
"""