# 🧠 Flipkart Chatbot — Templates Directory

This directory contains the **HTML templates** rendered by the Flask backend for the Flipkart Chatbot application.

## 📁 Purpose

Flask automatically looks for front-end templates inside the `templates/` directory.
Each file here defines a web page structure that Flask sends to the browser when a route calls:

```python
return render_template("index.html")
```

In this project, the chatbot’s web interface is entirely defined in `index.html`.

## 📄 File Overview

| File           | Description                                                                                                                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **index.html** | The main chat interface displayed at the root route `/`. It contains the user input form, the message display container, and JavaScript for dynamically updating the conversation using AJAX requests to the Flask backend. |

## ⚙️ How It Works

* When a user visits `/`, Flask renders **index.html**, which loads:

  * **Bootstrap** for layout and responsive design.
  * **Font Awesome** for the send-button icon.
  * **jQuery** for handling user input and sending messages to the backend.
  * The project’s stylesheet from `static/style.css` for consistent styling.
* When a user sends a message, jQuery intercepts the form submission, posts the message to the `/get` endpoint, and appends the model’s reply to the chat window without refreshing the page.
* The page automatically scrolls to the latest message after each exchange for smoother interaction.

## 🧩 Integration Notes

* The `<link>` and `<script>` tags load external dependencies via CDN to simplify deployment.
* The `{{ url_for('static', filename='style.css') }}` tag ensures Flask generates the correct path to the static CSS file, even in different environments.
* Image and icon links can easily be replaced or updated as needed to rebrand the chatbot.

## 🎨 Customisation Tips

* Modify Bootstrap column sizes inside the `.chat` container to adjust the width of the chat panel.
* Edit the text inside `.chat-title` and `.chat-subtitle` to change the chatbot’s displayed name or tagline.
* Adjust the IDs or class names only if you also update the jQuery selectors in the embedded script.
* For new pages, simply add more HTML templates to this folder and render them from different routes in `app.py`.

## 🧠 Summary

This folder defines the **visual and interactive layer** of the Flipkart Chatbot.
It connects the user to the model backend by combining **Flask templating**, **AJAX messaging**, and **Bootstrap styling** into a single responsive interface.