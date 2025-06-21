import streamlit as st
import requests

API_URL = "http://localhost:8000/todos/"

st.set_page_config(page_title="Todo App", layout="centered")
st.title("📝 Todo App (Streamlit UI)")

# --- Add new Todo ---
st.header("Add a new Todo")
with st.form("todo_form"):
    title = st.text_input("Title")
    description = st.text_input("Description")
    submitted = st.form_submit_button("Create Todo")

    if submitted:
        res = requests.post(API_URL, json={
            "title": title,
            "description": description,
            "completed": False
        })
        if res.status_code == 200:
            st.success("✅ Todo created!")
            st.experimental_rerun()
        else:
            st.error("❌ Failed to create todo.")

# --- Display Todos ---
st.header("Current Todos")
try:
    todos = requests.get(API_URL).json()

    if not todos:
        st.info("No todos yet. Add one above!")
    else:
        for todo in todos:
            col1, col2, col3 = st.columns([5, 1, 1])
            status = "✅" if todo["completed"] else "❌"
            col1.markdown(f"**{todo['title']}** — {todo['description']} {status}")

            if not todo["completed"]:
                if col2.button("✅", key=f"complete_{todo['id']}"):
                    requests.put(f"{API_URL}{todo['id']}", json={
                        "title": todo["title"],
                        "description": todo["description"],
                        "completed": True
                    })
                    st.experimental_rerun()

            if col3.button("❌", key=f"delete_{todo['id']}"):
                requests.delete(f"{API_URL}{todo['id']}")
                st.experimental_rerun()

except Exception as e:
    st.error(f"Error fetching todos: {e}")
