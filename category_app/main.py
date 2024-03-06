import openai
import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

# Set your OpenAI API key here
api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

# Define the ProductDescription model
class ProductDescription(BaseModel):
    description: str
    
# Function to generate product categories
def generate_product_categories(description: str):
    categories = {}
    all_categories = []
    for d in description:
        # Set up prompt for ChatGPT
        prompt = f"Based on the following product description generate a raw JSON array of product categories based on the Google Product Category Taxanomy :\n\n{d}:"
        # Generate categories using ChatGPT
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )
        # Extract categories from the response
        if response.choices:
            generated_text = response.choices[0].message.content
            # Convert the generated JSON string to a Python dictionary
            categories = json.loads(generated_text)
            # Append the categories to the list
            all_categories.append(categories.get("categories"))
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to generate categories.")
        
    return all_categories

# Root endpoint
@app.get("/")
async def root():
    return  ("Welcome to the Product Category Generator. "
                    "Use the /generate-product-category/ endpoint to generate product categories from a product description. "
                    "For multiple product descriptions, use the /generate-products-categories/ endpoint. "
                    "This FastAPI-based web service utilizes OpenAI's GPT model to automatically generate product categories from textual descriptions. "
                    "By sending a product description via a POST request to the appropriate endpoint, users can swiftly obtain JSON-formatted product categories. "
                    "The program supports both single and multiple product descriptions, providing flexibility for various use cases. "
                    "With error handling mechanisms in place, it ensures reliable operation, making it ideal for e-commerce platforms seeking streamlined categorization processes. "
                    "Its simplicity and efficiency make it a valuable tool for enhancing product management workflows."
                   )
    
# Function to generate product category
@app.post("/generate-product-category/")
async def get_product_categories(product: ProductDescription):
    # Generate product categories from product descriptions
    categories = generate_product_categories([product.description])
    return {"categories": categories}

# Function to generate product categories
@app.post("/generate-products-categories/")
async def get_products_categories(products: list[ProductDescription]):
    # Generate product categories from product descriptions
    categories = generate_product_categories([p.description for p in products])
    return {"categories": categories}