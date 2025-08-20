import random
# Sample product categories and products
products = {
    "soap": ["Dove Soap", "Lux Soap", "Pears Soap"],
    "mobile": ["iPhone 14", "Samsung Galaxy S23", "OnePlus 11"],
    "toys": ["Lego Set", "Barbie Doll", "Hot Wheels Car"],
    "games": ["Chess Board", "Monopoly", "Call of Duty"],
    "books": ["Harry Potter", "Atomic Habits", "The Alchemist"],
    "shoes": ["Nike Air", "Adidas Superstar", "Puma Runner"]
}
user_history = []
def recommend_products(history):
    recommendations = []
    for item in history:
        if item in products:
            recommendations.extend(products[item])
    # If no history, recommend random products
    if not recommendations:
        recommendations = random.sample(
            [prod for plist in products.values() for prod in plist], 3)
    return recommendations

def main():
    print("Welcome to the Product Recommendation System!")
    print("Type your search (e.g., soap, mobile, toys, games, books, shoes). Type 'exit' to quit.")
    while True:
        search = input("Search for a product category: ").strip().lower()
        if search == 'exit':
            break
        user_history.append(search)
        recs = recommend_products([search])
        print("Recommended products for you:")
        for prod in recs:
            print("-", prod)
        print()

if __name__ == "__main__":
    main()