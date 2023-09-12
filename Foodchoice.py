#This code generates a random high protein meal for a given meal time (breakfast, lunch or dinner)
import random 


meal_option=('Breakfast','Lunch','Dinner')
Breakfast_options= [
     "GREEK YOGURT PARFAIT: Layer Greek yogurt with berries, nuts, and a drizzle of honey.",
    "SCRAMBLED EGGS WITH SPINACH: Whip up eggs with sautéed spinach and feta cheese.",
    "OATMEAL WITH ALMOND BUTTER: Add a spoonful of almond butter and some chopped nuts to your oatmeal.",
    "BREAKFAST BURRITO: Fill a whole-wheat tortilla with scrambled eggs, black beans, salsa, and avocado.",
    "COTTAGE CHEESE BOWL: Top cottage cheese with sliced fruit, chia seeds, and a sprinkle of cinnamon.",
    "QUINOA BREAKFAST BOWL: Cook quinoa and top it with scrambled eggs, veggies, and a protein source like turkey sausage.",
    "PROTEIN PANCAKES: Make pancakes using a mix that's high in protein, or add protein powder to your pancake batter.",
    "CHIA SEED PUDDING: Mix chia seeds with milk or yogurt and let them soak overnight. Top with fruit and nuts.",
    "SMOKED SALMON TOAST: Spread cream cheese on whole-grain toast and layer with smoked salmon, capers, and red onion.",
    "TOFU SCRAMBLE: Sauté tofu with veggies, turmeric, and nutritional yeast for a vegan scramble.",
    "PROTEIN SMOOTHIE: Blend protein powder, milk, spinach, banana, and nut butter for a quick shake.",
    "EGG WHITE OMELETTE: Fill an omelette with egg whites and your choice of veggies and lean meats.",
    "PEANUT BUTTER BANANA WRAP: Spread peanut butter on a whole-wheat tortilla, add sliced banana, and roll it up.",
    "BREAKFAST QUICHE: Prepare a crustless quiche with eggs, cheese, and a variety of vegetables.",
    "BREAKFAST BOWL WITH BEANS: Combine black beans, scrambled eggs, salsa, and avocado for a hearty bowl.",
    "GREEK YOGURT PANCAKES: Mix Greek yogurt into your pancake batter for extra protein and creaminess.",
    "HIGH-PROTEIN CEREAL: Choose a cereal that's rich in protein and fiber, and have it with milk or yogurt.",
    "TURKEY SAUSAGE AND VEGGIE SKILLET: Sauté turkey sausage and veggies together for a flavorful skillet dish.",
    "NUTTY OATMEAL: Stir chopped nuts, seeds, and dried fruit into your oatmeal for added protein and texture.",
    "BREAKFAST QUINOA SALAD: Mix cooked quinoa with diced veggies, beans, and a light vinaigrette."
]
Lunch_options=[
     "GRILLED CHICKEN SALAD: Combine grilled chicken breast with a variety of fresh veggies and your favorite dressing.",
    "QUINOA AND BLACK BEAN BOWL: Mix cooked quinoa with black beans, corn, diced tomatoes, and a squeeze of lime.",
    "TUNA SALAD WRAP: Mix canned tuna with Greek yogurt, chopped veggies, and wrap it in a whole-wheat tortilla.",
    "CHICKPEA AND VEGGIE STIR-FRY: Sauté chickpeas and colorful vegetables with your choice of stir-fry sauce.",
    "SALMON AND AVOCADO SUSHI: Roll cooked salmon, avocado, and cucumber in nori seaweed for a protein-rich sushi.",
    "TURKEY AND HUMMUS WRAP: Layer sliced turkey, hummus, and crunchy veggies in a whole-grain wrap.",
    "EGG SALAD LETTUCE WRAPS: Make egg salad with Greek yogurt and mustard, and wrap it in lettuce leaves.",
    "LENTIL AND VEGETABLE SOUP: Cook lentils with a variety of vegetables in a flavorful broth for a hearty soup.",
    "GREEK YOGURT CHICKEN PITA: Stuff whole-wheat pita pockets with grilled chicken, Greek yogurt, and cucumber.",
    "HIGH-PROTEIN PASTA SALAD: Combine whole-grain pasta, diced chicken, beans, and veggies with a light vinaigrette.",
    "QUINOA STUFFED BELL PEPPERS: Stuff bell peppers with a mixture of quinoa, lean ground meat, and vegetables.",
    "COTTAGE CHEESE AND FRUIT PLATE: Pair cottage cheese with a variety of fresh fruits and a sprinkle of nuts.",
    "BAKED TOFU AND VEGGIE SKEWERS: Thread cubes of tofu and colorful vegetables onto skewers, then bake or grill.",
    "CHICKEN AND BROCCOLI STIR-FRY: Sauté chicken strips and broccoli florets with a savory stir-fry sauce.",
    "MEDITERRANEAN CHICKPEA SALAD: Mix chickpeas with chopped cucumber, tomato, olives, and feta cheese.",
    "STEAK AND QUINOA BOWL: Grill lean steak and serve it with quinoa, sautéed greens, and a drizzle of sauce.",
    "BLACK BEAN AND SWEET POTATO BURRITO: Wrap black beans, roasted sweet potatoes, and veggies in a tortilla.",
    "CAULIFLOWER RICE BOWL: Top cauliflower rice with cooked shrimp, edamame, and a soy-based sauce.",
    "SPINACH AND FETA STUFFED CHICKEN: Stuff chicken breasts with sautéed spinach and crumbled feta cheese.",
    "CHILI WITH LEAN GROUND MEAT: Prepare a protein-packed chili using lean ground meat, beans, and spices."
]
Dinner_options=["GRILLED STEAK WITH ROASTED VEGETABLES: Grill a juicy steak and serve it with a side of roasted veggies.",
    "BAKED SALMON WITH QUINOA: Bake salmon fillets and serve them with cooked quinoa and steamed greens.",
    "CHICKEN AND VEGETABLE STIR-FRY: Stir-fry chicken strips with a mix of colorful vegetables and your favorite sauce.",
    "TOFU AND BROCCOLI IN GARLIC SAUCE: Sauté tofu and broccoli in a flavorful garlic sauce, served over brown rice.",
    "TURKEY MEATBALLS WITH ZUCCHINI NOODLES: Make lean turkey meatballs and pair them with spiralized zucchini noodles.",
    "CHICKPEA AND SPINACH CURRY: Cook chickpeas and spinach in a fragrant curry sauce, served with rice or naan.",
    "GRILLED PORTOBELLO MUSHROOMS WITH QUINOA: Grill portobello mushrooms and serve them with quinoa and a sprinkle of cheese.",
    "LENTIL AND VEGETABLE STEW: Simmer lentils and assorted vegetables in a savory broth for a hearty stew.",
    "GREEK SALAD WITH GRILLED CHICKEN: Toss together a Greek salad with grilled chicken, olives, feta, and a light dressing.",
    "STUFFED BELL PEPPERS WITH LEAN GROUND BEEF: Stuff bell peppers with a mixture of lean ground beef, rice, and veggies.",
    "CAULIFLOWER AND CHICKPEA CURRY: Prepare a flavorful cauliflower and chickpea curry served with rice or flatbread.",
    "ZOODLES WITH SHRIMP AND PESTO: Sauté zucchini noodles with shrimp and toss with a homemade pesto sauce.",
    "QUINOA AND BLACK BEAN STUFFED SWEET POTATO: Stuff baked sweet potatoes with quinoa, black beans, and a variety of toppings.",
    "GRILLED TOFU WITH SAUTÉED GREENS: Grill tofu and serve it with sautéed spinach, kale, or other greens.",
    "BEEF AND BROCCOLI SKILLET: Sauté beef strips with broccoli and a savory sauce for a quick and flavorful dish.",
    "SPAGHETTI SQUASH WITH TURKEY"
]

n=1
while n==1:
    
    
    print()
    print("What meal is this?")
    print('Type "Breakfast" for Breakfast')
    print('Type "Lunch" for Lunch')
    print('Type "Dinner" for Dinner')
    
    print()
    user_input=input("Enter your option: ")
    if user_input in meal_option: 
        n+=1
        if user_input==meal_option[0]:
            rand1=random.choice(Breakfast_options)
            print('Your Breakfast shall be...') 
            print(str(rand1))
            while True:
                print()
                again=str(input('Press "enter" for another meal choice or "q" to quit '))
                if again=='':
                    n-=1
                    break
                if again=='q': 
                    print('Thank you for using Foodchoices.py')
                    break
                   
                else:
                    print('This is not a valid answer')
       
        if user_input==meal_option[1]:
            rand2=random.choice(Lunch_options)
            print('Your Lunch shall be...') 
            print(str(rand2))
            while True:
                print()
                again=str(input('Press "enter" for another meal choice or "q" to quit '))
                if again=='':
                    n-=1
                    break
                if again=='q':
                    print('Thank you for using Foodchoices.py') 
                    break
                   
                else:
                    print('This is not a valid answer')
       
        if user_input==meal_option[2]:
            rand3=random.choice(Dinner_options)
            print('Your Dinner shall be...') 
            print(str(rand3))
   
            while True:
                print()
                again=str(input('Press "enter" for another meal choice or "q" to quit '))
                if again=='':
                    n-=1
                    break
                if again=='q': 
                    print('Thank you for using Foodchoices.py')
                    break
                   
                else:
                    print('This is not a valid answer')
       
      
    else:
        print() 
        print('This is not a valid option')


        
    
       
    
    
       
   
   
   
   
