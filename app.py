import streamlit as st

try:
    from main import process_query
    #st.success("main.py imported")
except Exception as e:
    st.error(f"Main Error: {e}")

try:
    from database.db import get_tickets
    #st.success("db.py imported")
except Exception as e:
    st.error(f"DB Error: {e}")

st.title("Multi-Agent Customer Support")

name = st.text_input("Customer Name")

query = st.text_area("Enter Query")

if st.button("Submit"):

    result = process_query(name, query)

    st.success("Processed Successfully")

    st.write("Category:", result["category"])
    st.write("Sentiment:", result["sentiment"])
    st.write("Priority:", result["priority"])
    st.write("Escalated:", result["escalated"])

    st.write(result["response"])

st.subheader("Tickets")

tickets = get_tickets()

for ticket in tickets:
    st.write(ticket)