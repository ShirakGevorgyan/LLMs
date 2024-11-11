import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  

def generate_product_description(product_name, product_features, target_audience):
    prompt = f"Create a detailed product description for '{product_name}'. The product features are {product_features}. The target audience is {target_audience}. Make the description engaging and informative."
    
    try:
        response = openai.completions.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )
        return response['choices'][0]['text'].strip()
    
    except openai.RateLimitError as e:  
        print("Error: Rate limit exceeded, please check your API usage and billing details.")
        print(f"Details: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def generate_marketing_email(target_audience, product_name, benefits):
    prompt = f"Create a personalized marketing email for {target_audience}. The email should promote a product called {product_name} that has the following benefits: {benefits}. Make the email friendly, persuasive, and call to action-driven."
    
    try:
        response = openai.completions.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=250,
            temperature=0.8
        )
        return response['choices'][0]['text'].strip()
    
    except openai.RateLimitError as e: 
        print("Error: Rate limit exceeded, please check your API usage and billing details.")
        print(f"Details: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

product_name = "Eco-Friendly Water Bottle"
product_features = "made of 100% recycled plastic, BPA-free, insulated, comes in 3 sizes"
target_audience = "environmentally-conscious individuals"
product_description = generate_product_description(product_name, product_features, target_audience)
if product_description:
    print("Product Description:", product_description)

benefits = "saves the planet, keeps your drink cold for 24 hours, stylish design"
marketing_email = generate_marketing_email(target_audience, product_name, benefits)
if marketing_email:
    print("\nMarketing Email:", marketing_email)
