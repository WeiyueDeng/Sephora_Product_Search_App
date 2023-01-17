from dis import Instruction
import json
from operator import itemgetter
from turtle import hideturtle
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from pygments import highlight
app = Flask(__name__)


data = {
    "1":{
        "id": "1",
        "name": "Radiant Creamy Concealer",
        "brand": "NARS",
        "image": "https://www.sephora.com/productimages/sku/s2172310-main-zoom.jpg?imwidth=270&pb=2020-03-allure-best-2018&imwidth=324",
        "price": "30.00",
        "size": "0.22 oz/ 6 mL",
        "description": "A multipurpose concealer that brightens, corrects, and perfects for up to 16 hours with a creamy medium-to-buildable coverage and natural, radiant finish. Enriched with hydrating, multiaction skincare benefits and light-diffusing technology, it instantly obscures imperfections and diminishes fine lines and signs of fatigue. This multipurpose concealer can also be used to highlight and contour. Available in 30 shades in both standard and mini sizes.",
        "genre": ["Makeup", "Face", "Concealer"],
        "highlights": ["Liquid Formula","Medium Coverage","Radiant Finish","Long-wearing","Good for: Dark Circles","Good for: Dark spots"],
        "instruction": ["Can be applied directly from the applicator, with fingertips, or with the #10 Radiant Creamy Concealer Brush (sold separately).",
                        "To use as a highlighter, select one to three shades lighter than your concealer shade and place on high points of the face.",
                        "To add contour and dimension, apply concealer in the hollows of the cheeks, on temples, and along the hair and jaw lines."]
    },
    "2":{
        "id": "2",
        "name": "Luminous Silk Perfect Glow Flawless Oil-Free Foundation",
        "brand": "Armani Beauty",
        "image": "https://www.sephora.com/productimages/sku/s1491380-main-zoom.jpg?imwidth=315",
        "price": "65.00",
        "size": "1 oz/ 30 mL",
        "description": "An award-winning, oil-free foundation that delivers buildable, medium coverage and a luminous, glowy-skin finish for a natural makeup look.This lightweight foundation is formulated with Micro–fil™ technology, allowing buildable color pigments to lay flat for seamless blending and layering. Inspired by charmeuse silk, this liquid foundation creates an airbrushed, silky skin appearance and a naturally radiant, lit-from-within glow. It has liquid formula with medium coverage.",
        "genre": ["Makeup", "Face","Foundation"],
        "highlights": ["allure 2018 Best of Beauty Award Winner","Natural Finish","Medium Coverage","Oil Free","Liquid Formula","Community Favorite"],
        "instruction": ["For an airbrushed-foundation finish, apply the foundation to the center of the face and blend outward using a foundation brush.",
                        "Apply using a damp sponge for a more dewy, luminous makeup look.",
                        "Add more layers for seamless coverage with a natural, flawless skin finish.",
                        "Use Luminous Silk Glow Setting Powder (sold separately) over the foundation for a longer-lasting makeup result."]
    },
    "3":{
        "id": "3",
        "name": "Dior Addict Lip Glow",
        "brand": "Dior",
        "image": "https://www.sephora.com/productimages/sku/s2447043-main-zoom.jpg?imwidth=270&imwidth=324",
        "price": "35.00",
        "size": "0.11 oz/ 3.52 g",
        "description": "An iconic Dior lip balm with 97 percent natural-origin ingredients that awakens the natural color of lips with a custom glow and up to 24 hours of hydration.The iconic Dior lip balm infused with color-reviver technology that adapts to the pH of lips to reveal a custom glow for up to six hours. Featuring cherry oil, shea butter, and sunflower waxes, Lip Glow offers both custom color and lip care. It’s available in a couture case and in shades to suit all skin tones.",
        "genre": ["Makeup", "Lip", "Lip Balm & Treatment"],
        "highlights": ["Satin Finish","Hydrating","Without Parabens","Without Silicones","Without Sulfates SLS & SLES","Without Formaldehydes"],
        "instruction": ["Can be worn on its own as a lip balm for a subtle custom color-awakening effect and up to 24 hours of hydration.",
                        "Can be worn under the corresponding shade of Dior Addict Lip Maximizer or Dior Addict Lip Glow Oil (both sold separately) to play with the color."]
    },
    "4":{
        "id": "4",
        "name": "No. 3 Hair Repair Perfector",
        "brand": "Olaplex",
        "image": "https://www.sephora.com/productimages/sku/s2033264-main-zoom.jpg?imwidth=270&pb=2020-03-sephora-clean-2019&imwidth=324",
        "price": "28.00",
        "size": "3.3 oz/ 100 mL",
        "description": "A concentrated treatment that strengthens the hair from within, reducing breakage and improving its look and feel.No. 3 Hair Perfector is not a conditioner, it’s an at-home treatment that contains the same active ingredient found in all professional Olaplex products. Created by two of the top PhD's in chemistry and materials science, Olaplex products feature first-of-their-kind, patented, bond-building technology, which relinks the broken disulfide bonds caused by chemical, thermal, and mechanical damage to the hair. This formula is made to work with every hair type, providing real, structural repair that works from within.",
        "genre": ["Hair","Hair Styling & Treatments","Scalp Treatments"],
        "highlights": ["Good for: Damage","Good for: Color Care","Good for: Volume","All Hair Types","Clean at Sephora","Community Favorite"],
        "instruction": ["Use once a week or two to three times a week for damaged hair.",
                        "Apply on damp, towel-dried hair.",
                        "Apply a generous amount from scalp to ends until hair is thoroughly saturated.",
                        "Leave on for a minimum of 10 minutes (longer if desired).",
                        "Rinse from hair. Shampoo and condition as usual."]
    },
    "5":{
        "id": "5",
        "name": "Unseen Sunscreen SPF 40 PA+++Unseen Sunscreen SPF 40 PA+++",
        "brand": "Supergoop!",
        "image": "https://www.sephora.com/productimages/sku/s2315935-main-zoom.jpg?imwidth=270&pb=2020-03-sephora-clean-2019&imwidth=324",
        "price": "34.00",
        "size": "1.7 oz/ 50 mL",
        "description": "A totally invisible, weightless, scentless, and makeup-gripping daily primer with SPF 40. This innovative, antioxidant-rich SPF primer preps skin for makeup while providing broad spectrum SPF 40. The ingredients also help offer tech protection against the light emitted from our phones and computers. The unique oil-free formula glides onto skin providing shine control and leaving a velvety, makeup-gripping finish.",
        "genre": ["Skincare", "Sunscreen", "Face Sunscreen"],
        "highlights": ["Natural Finish","Oil Free","allure 2019 Best of Beauty Award Winner","Clean at Sephora","SPF"],
        "instruction": ["Apply generously and evenly as the last step in your skincare routine, before makeup and 15 minutes before sun exposure.",
                        "Reapply at least every two hours or after 40 minutes of swimming or sweating."]
    },
    "6":{
        "id": "6",
        "name": "CHANCE EAU TENDRE Eau de Toilette",
        "brand": "CHANEL",
        "image": "https://www.sephora.com/productimages/sku/s1237379-main-zoom.jpg?imwidth=270&imwidth=324",
        "price": "95.00",
        "size": "1.7 oz",
        "description": "The delicate and unexpected fruity-floral fragrance for women creates a soft whirlwind of happiness, fantasy, and radiance.A green and fruity Grapefruit-Quince accord intertwines with the softness of Jasmine and the smoothness of White Musks for an intoxicatingly light, floral trail.The Eau de Toilette comes in a spray bottle for generous use and effortless application on skin or clothing. Fragrance is intensified by the warmth of your own body.",
        "genre": ["Fragrance", "Women","Perfume"],
        "highlights": [" Fresh Fruity Florals","Citron","Jasmine","Teakwood"],
        "instruction": ["Fragrance is intensified by the warmth of your own body. Apply in the creases of your knees and elbows for a longer-lasting, stronger scent.",
                        "After applying, avoid rubbing or dabbing skin. This breaks down the fragrance, causing it to wear off more quickly.",
                        "If you prefer placing fragrance on your wrists, be sure to reapply after frequent hand-washing, as this tends to rinse off the scent.",
                        "Replace fragrance after 12 months. Expired perfumes more than a year old lose the integrity of the original scent."]
    },
    "7":{
        "id": "7",
        "name": "Brazilian Bum Bum Body Cream",
        "brand": "Sol de Janeiro",
        "image": "https://www.sephora.com/productimages/sku/s1802412-main-zoom.jpg?imwidth=270&imwidth=324",
        "price": "45.00",
        "size": "8.1 oz/ 240 mL",
        "description": "A fast-absorbing body cream with an addictive scent and a visibly tightening, smoothing formula that adds a hint of shimmer to skin. Get that coveted Brazilian Bum Bum Cream effect and experience absolute body joy with this luxurious cream. Infused with powerful, caffeine-rich guarana and a Brazilian blend of skin-loving ingredients, the award-winning formula melts in and visibly smooths the skin while imparting a touch of shimmer. Notes of salted caramel and pistachio create an addictive scent. The box is recyclable and made from 80 percent Forest Stewardship Council-certified recycled materials.",
        "genre": ["Bath & Body", "Body Moisturizers","Body Lotions & Body Oils"],
        "highlights": ["Good for: Loss of firmness","Good for: Dryness","Warm & Spicy Scent","Cruelty-Free","Cruelty-Free"],
        "instruction": ["Massage in a circular motion, creating warmth for better absorption and circulation.",
                        "Use it on your bum bum, legs, tummy, arms, and anywhere else you want a visible lift and glow.",
                        "Remove the cap and disc from the jar.",
                        "Rinse all of the pieces.",
                        "Recycle."]
    },
    "8":{
        "id": "8",
        "name": "Beautiful Skin Medium Coverage Liquid Foundation with Hyaluronic Acid",
        "brand": "Charlotte Tilbury",
        "image": "https://www.sephora.com/productimages/sku/s2551893-main-zoom.jpg?imwidth=270&imwidth=324",
        "price": "44.00",
        "size": "1 oz/ 30 ml",
        "description": "A 16-hour natural-glow foundation with buildable medium coverage to hydrate, smooth, blur pores, and brighten skin. Charlotte Tilbury developed this skincare-infused foundation to improve the look of skin with each application. The lightweight, long-wearing formula helps prevent pollutant particles from penetrating the skin, strengthening its barrier and improving skin quality over time. It is also vegan and cruelty-free.",
        "genre": ["Makeup","Face","Foundation"],
        "highlights": ["Long-wearing", "Medium Coverage","Natural Finish","Hyaluronic Acid","Best for Dry, Combo, Normal Skin","Cruelty-Free"],
        "instruction": ["Buff outwards from the center of the face, across the cheek, and down the jawline for a natural, healthy-looking finish.",
                        "Pat on foundation to key areas that need more coverage, then gently blend out in circular motions all over face.",
                        "Pat on foundation to key areas that need more coverage, then gently blend out in circular motions all over face."]
    },
    "9":{
        "id": "9",
        "name": "Water Sleeping Mask with Squalane",
        "brand": "LANEIGE",
        "image": "https://www.sephora.com/productimages/sku/s2535243-main-zoom.jpg?imwidth=270&imwidth=324",
        "price": "29.00",
        "size": "2.3 oz/ 70 mL",
        "description": "A bestselling overnight Water Sleeping Mask that is formulated with squalane and Probiotic-Derived Complex for hyper-hydrating results.his sleeping mask is formulated with a Probiotic-Derived Complex that strengthens the skin’s moisture barrier while visibly boosting the look of skin's brightness and clarity. It also contains squalane, which provides intense moisture without feeling heavy. In a self-assessment with 34 Asian women ages 20 to 39, after 1 week of use: 100 percent agreed skin was softer.",
        "genre": ["Skincare","Masks","Face Masks"],
        "highlights": ["Good for: Dullness/Uneven Texture","Good for: DrynessGood for: Dryness","Hydrating","Best for Dry Skin","Without Sulfates SLS & SLES","Without Parabens"],
        "instruction": ["After face cream, apply evenly across face.",
                        "After product is absorbed completely, leave treatment on overnight and rinse off in the morning.",
                        "Use once or twice a week as a mask, or use daily in place of your nighttime moisturizer."]
    },
    "10":{
        "id": "10",
        "name": "Soft Pinch Liquid Blush",
        "brand": "Rare Beauty by Selena Gomez",
        "image": "https://www.sephora.com/productimages/sku/s2518959-main-zoom.jpg?imwidth=270&imwidth=324",
        "price": "20.00",
        "size": "0.25 oz/ 7.5 mL",
        "description": "A weightless, long-lasting liquid blush that blends and builds beautifully for a soft, healthy flush. Available in matte and dewy finishes. Create a pinch-perfect flush using this featherweight formula infused with long-lasting pigments that last all day. Available in matte or dewy finishes, this liquid blush blends beautifully to create soft, buildable color with a natural, second-skin finish. This product is also vegan and cruelty-free.",
        "genre": ["Makeup", "Face","Blush"],
        "highlights": ["Medium Coverage","Liquid Formula","Radiant Finish","Matte Finish","Long-wearing","Community Favorite"],
        "instruction": ["Gently remove excess product from applicator.",
                        "Use the doe-foot applicator and place one or two dots on each cheek.",
                        "Use fingertips and gently pat into skin for a seamless finish."]
    },
}
popularItems=[]

matchItems=[]

new_item=[]
# ROUTES

@app.route('/')
def homepage():
    global data
    global popularItems

    popularItems.clear()
    for i in range(1,4):
        popularItems.append(data[str(i)])
    return render_template('homepage.html', data=popularItems)   


@app.route('/view/<id>')
def view(id=None):
    global data

    item=data[id]
    return render_template('view.html', item=item) 


@app.route('/search_result/<val>')
def search_result(val=None):
    global matchItems
    global data

    matchItems.clear()
    for id in data:
        print(data)
        if val.lower() in data[id]["name"].lower() or val.lower() in data[id]["brand"].lower():
            matchItems.append(data[id])
        for genre in data[id]["genre"]:
            if val.lower() in genre.lower() and data[id] not in matchItems:
                matchItems.append(data[id])


    return render_template('search.html', data=matchItems, val=val)

@app.route('/add', methods=['GET', 'POST'])
def add():
    global data
    global new_item

    new_item.clear()
    if request.method=="POST":
        json_data = request.get_json()
        id=json_data["id"]
        genre=json_data["genre"].split(",")
        highlights=json_data["highlights"].split(",")
        instruction=json_data["instruction"].split(",")

        json_data["genre"]=genre
        json_data["highlights"]=highlights
        json_data["instruction"]=instruction

        data[id]=json_data
        print(data)

        new_item.append(id)
        print(id)
        print(new_item)

        return jsonify(new_item=new_item)
    else:
        return render_template('add.html',data=new_item)  

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id=None):
    global data

    if request.method=="POST":
        json_data=request.get_json()
        genre_text=json_data["genre"].split(",")
        highlights_text=json_data["highlights"].split(",")
        instruction_text=json_data["instruction"].split(",")

        json_data["genre"]=genre_text
        json_data["highlights"]=highlights_text
        json_data["instruction"]=instruction_text

        data[id]=json_data
        print(data[id])

        return jsonify(id=id)
    else:
        item={
            "id":id,
            "name":data[id]["name"],
            "brand":data[id]["brand"],
            "image":data[id]["image"],
            "price":data[id]["price"],
            "size": data[id]["size"],
            "description":data[id]["description"]
        }
        genre=""
        for i in data[id]["genre"]:
            genre+=i+","
        genre=genre[:-1]

        item["genre"]=genre

        highlight=""
        for i in data[id]["highlights"]:
            highlight+=i+","
        highlight=highlight[:-1]

        item["highlights"]=highlight

        instruction=""
        for i in data[id]["instruction"]:
            instruction+=i+","
        instruction=instruction[:-1]

        item["instruction"]=instruction
        #print(genre)
        #print(data[id]["genre"])

        return render_template('edit.html', item=item, id=id) 

 


if __name__ == '__main__':
   app.run(debug = True)




