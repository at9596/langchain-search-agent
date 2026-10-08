# from tavily import TavilyClient
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# #STEP 1
# tavily_client = TavilyClient

# # STEP 2
# response = tavily_client.search("who is messi?")


# # STEP 3
# print(response)

from tavily import TavilyClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# STEP 1: Initialize Tavily client
tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

# # STEP 2: Search the web
# response = tavily_client.search(
#     query="Who is Messi?"
# )

# # STEP 3: Print the response
# print(response)
# # Step 2. Executing a context search query
# context = tavily_client.get_search_context(query="What happened during the Burning Man floods?")

# # Step 3. That's it! You now have a context string that you can feed directly into your RAG Application
# print(context)
# Step 2. Defining the list of URLs to extract content from
urls = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Data_science",
    "https://en.wikipedia.org/wiki/Quantum_computing",
    "https://en.wikipedia.org/wiki/Climate_change"
] 
# Step 3. Executing the extract request
response = tavily_client.extract(urls=urls, include_images=True)

# Step 4. Printing the extracted raw content
for result in response["results"]:
    print(f"URL: {result['url']}")
    print(f"Raw Content: {result['raw_content']}")
    print(f"Images: {result['images']}\n")

