# 🔍 Custom Search Engine using Exa API

## Project Overview

This project serves as a comprehensive demonstration of building a high-performance, custom search engine using **Python** and leveraging the power of the **Exa API**. It moves beyond traditional keyword-based searching by integrating advanced neural search capabilities and robust content retrieval features.

The goal is to provide developers and researchers with a flexible, easy-to-use framework for querying the web, extracting only the most relevant and clean information, and presenting search results in a user-friendly and actionable format. By utilizing the Exa API, this engine can access fresh, real-time data and provide sophisticated ranking based on semantic understanding.

---

## ✨ Key Features

This search engine is engineered with several powerful features designed to maximize relevance and efficiency:

* **Neural Search Capabilities:**
    Utilizes the Exa API's state-of-the-art neural ranking models. This allows the search engine to understand the *meaning* and *context* of a query, delivering results that are semantically relevant rather than just matching keywords.

* **Advanced Content Extraction:**
    Goes beyond simply linking to webpages. The engine retrieves clean, parsed content from the search results, removing irrelevant elements like navigation bars, ads, and footers. This ensures you are working with the pure, relevant text of the page.

* **Customizable Filtering and Ranking:**
    Provides the flexibility to filter results based on specific criteria such as publishing date, domain, and file type. Developers can also implement custom ranking logic to prioritize results based on the extracted content or metadata.

* **Seamless Python SDK Integration:**
    Built entirely on Python, the project integrates seamlessly with the official Exa Python SDK, ensuring easy and efficient interaction with the API.

* **Versatile Use Cases:**
    The framework is highly adaptable, making it ideal for various applications, including:
    * **In-Depth Research:** Quickly gathering and summarizing information from multiple sources.
    * **Code Snippet Retrieval:** Searching for and extracting relevant code examples directly from documentation or tutorials.
    * **Real-time News and Data Access:** Accessing the most current web content without delays.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3.x** | The core programming language for the entire project. |
| **Exa API** | The primary backend for all web search, neural ranking, and content extraction tasks. |
| **Exa Python SDK** | Official library for interacting with the Exa API. |
| **`requests` (or similar)** | Used for general HTTP requests, if any custom web fetching is needed. |
| **`dotenv` (or similar)** | Recommended for secure management of API keys and environment variables. |

---

## 🚀 Getting Started

Follow these steps to set up and run your custom search engine.

### Prerequisites

1.  **Python 3.8+** installed on your system.
2.  An **API Key** from Exa. You can obtain one by signing up on the [Exa website](https://exa.ai/).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/raymondoyondi/Search-Engine.git](https://github.com/raymondoyondi/Search-Engine.git)
    cd Search-Engine
    ```

2.  **Create and activate a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate # On Linux/macOS
    # .\venv\Scripts\activate # On Windows
    ```

3.  **Install the required dependencies:**
    *(Assuming a `requirements.txt` file exists with `exa` as a dependency)*
    ```bash
    pip install -r requirements.txt
    # If no requirements.txt, install the Exa SDK directly:
    # pip install exa
    ```

4.  **Configure your API Key:**
    Create a file named `.env` in the project root directory and add your Exa API key:
    ```
    EXA_API_KEY="YOUR_EXA_API_KEY_HERE"
    ```
    *Note: The `main.py` script must be configured to load this environment variable.*

---

## 💡 Usage

The project's core functionality is contained within `main.py`. This script demonstrates how to initiate a search, filter results, and extract the content.

### Example: Running a Search

To run the search engine, execute the main script from your terminal:

``bash
`python main.py`

# 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the repository

2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)

3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)

4. Push to the Branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request

# 📜 License

Distributed under the MIT License. See LICENSE for more information.
