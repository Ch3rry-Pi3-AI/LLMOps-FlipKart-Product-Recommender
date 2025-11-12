Perfect — here’s an updated, clean, and well-documented README for your `static/` folder reflecting that only `style.css` remains. It’s written in the same professional, British-English tone and format as the one for your `templates/` directory.

---

# 🎨 Flipkart Chatbot — Static Assets Directory

This directory contains all **static front-end resources** used by the Flask application.
Flask serves these files directly to the client without processing them, making this folder ideal for storing stylesheets, scripts, and images.

## 📁 Purpose

Static files are accessed using Flask’s built-in function:

```python
url_for('static', filename='...')
```

This ensures that file paths are always correct, even if the app is deployed in different environments or behind a proxy.

## 📄 File Overview

| File          | Description                                                                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **style.css** | The main stylesheet controlling the visual appearance of the chatbot interface, including layout, colours, typography, and component behaviour. |

## 🎨 Styling Overview

The stylesheet defines:

* A **dark, modern theme** with subtle transparency and blurred backgrounds for visual depth.
* A **flexible, scrollable chat card** (`.chat-card`) that adapts to various screen sizes.
* **Message bubble styling** distinguishing between user and bot responses.
* **Custom scrollbars** and smooth auto-scroll behaviour for new messages.
* **Responsive design rules** ensuring usability on both desktop and mobile devices.

## 🧩 Integration Notes

* The stylesheet is linked in `templates/index.html` using:

  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```
* Any changes made to this file will appear immediately upon refreshing the browser (use **Ctrl + F5** to clear cache if necessary).
* Additional assets such as images or icons can be added later by creating new subfolders (e.g. `static/img/`) and referencing them in HTML or CSS with the same `url_for` pattern.

## 💡 Customisation Tips

* Adjust colours, gradients, or transparency values in `.chat-card`, `.msg_cotainer`, and `.msg_cotainer_send` to fine-tune the aesthetic.
* If you add background images in the future, reference them with a static path such as `/static/img/background.jpg` rather than Jinja templating.
* To modify the overall layout or spacing, tweak the Bootstrap classes in `index.html` while keeping `style.css` focused on presentation.

## 🧠 Summary

The `static/` directory provides the **visual foundation** of the Flipkart Chatbot interface.
While the Flask backend manages logic and data flow, this folder ensures a cohesive, responsive, and polished user experience through consistent front-end styling.
