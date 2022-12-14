from app.models import db, Product
from datetime import datetime, date

now = date.today()


def seed_products():

    bookstore01 = Product(
        name= "Watercolour painting PRINT of a restaurant at night in Paris, France, Giclee art print",
        description= " Giclee/ Fine art PRINT of a watercolour painting I did of a restaurant in Paris, France. The city has many different faces and I especially like its look in the evening.",
        price= 900,
        userId = 3,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/23629440/r/il/435525/3007420413/il_1588xN.3007420413_7max.jpg"
    )
    bookstore02 = Product(
        name= "DROPS Air A medium thick blow yarn, baby alpaca and merino wool, Beautiful knitting yarn",
        description= "An exciting 'blow yarn' made from soft baby alpaca and cozy and warm merino wool. As implied in blow yarn, this quality has an unique construction where instead of spinning, the fibres of baby alpaca and merino wool are air blown into a tube together.",
        price= 100,
        userId = 1,
        category= "Clothing & Shoes",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/21915528/r/il/b90fa5/3300321021/il_1588xN.3300321021_elpl.jpg"
    )
    bookstore03 = Product(
        name= "Brushed Alpaca silk yarn! Garnstudio DROPS Design Brushed Alpaca silk 67% baby alpaca 23 mulberry silk fluffy knitting wool - 25 grams",
        description= "Super soft DROPS Alpaca Silk has a sophisticated shade card ranging from soft beige and gray hues, to gorgeous reds and purples. The yarn’s feather light and surprisingly warm features make it suitable for both small and large garments, and it can be knitted relatively fast on larger needles. DROPS Alpaca Silk can be used as an effect yarn when worked together with other yarns for lovely soft results!",
        price= 150,
        userId = 2,
        category= "Clothing & Shoes",
        highlight = "Materials",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/10304510/r/il/f7568b/2230955130/il_1588xN.2230955130_6yrs.jpg"
    )
    bookstore04 = Product(
        name= "Alpaca yarn, Drops Alpaca yarn, Organic wool, soft alpaca yarn, knitting yarn, Natural fiber",
        description= "Alpaca is a lovely yarn spun from 3 strands of 100% superfine alpaca, with an extra twist to provide a durable surface. ",
        price= 200,
        userId = 3,
        category= "Clothing & Shoes",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/32226150/r/il/3018e8/3921909534/il_1588xN.3921909534_k49c.jpg"
    )
    bookstore05 = Product(
        name= "Mohair Yarn DROPS Kid Silk Lace Yarn Super Kid Mohair Silk Yarn Mohair Wool Yarn",
        description= "A luxurious, light brushed yarn in an exclusive mix of 75% mohair super kid and 25% mulberry silk, DROPS Kid-Silk is feather light, and will give garments a sophisticated look.",
        price= 300,
        userId = 4,
        category= "Clothing & Shoes",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/18889371/r/il/4ed750/3040943685/il_1588xN.3040943685_894g.jpg"
    )
    bookstore06 = Product(
        name= "DROPS Baby Merino knitting yarn Superwash treated extra fine merino wool yarn Sport Garnstudio design 50g",
        description= "DROPS Baby Merino is spun from extra-fine merino wool fibers from free-range animals in South America. A super soft and itch-free wool yarn, it is perfectly suited for delicate baby skin. The yarn is also superwash treated which makes it machine washable and ideal for daily use.",
        price= 350,
        userId =5,
        category= "Clothing & Shoes",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/18508755/r/il/0b5349/2440378086/il_1588xN.2440378086_5mad.jpg"
    )
    bookstore07 = Product(
        name= "Original oil painting, Street Cafe , Impressionist Greek Art, Mediterranean street, Europe travel, Handmade on stretched canvas Large",
        description= "A good idea to give a touch of Greece taste to your home, living room, kitchen, bedroom or office…perfect gifts for your relatives and friends",
        price= 1000,
        userId=6,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/21187145/r/il/0e7a7e/2466292412/il_1588xN.2466292412_f2kw.jpg"
    )
    bookstore08 = Product(
        name= "Saint Petersburg Original oil painting Russia Travel Leningrad Cityscape Autumn Landscape Small wall art",
        description= "Original oil Painting Saint Petersburg.Russia Travel. Let my works add comfort to your home or office!",
        price= 800,
        userId=7,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/21187145/r/il/0f5035/3489428794/il_1588xN.3489428794_kqk5.jpg"
    )
    bookstore09 = Product(
        name= "Greece watercolor Original painting Greek travel art Mediterranean Sea A5 size artwork by AnaMuStudio",
        description= "Santorini artwork Greece painting Original watercolor.",
        price= 80,
        userId=8,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/20809018/r/il/423612/3877368233/il_1588xN.3877368233_i0f2.jpg"
    )
    bookstore10 = Product(
        name= "Edinburgh watercolor painting, art print, Edinburgh Old Town,Edinburgh painting, Edinburgh Scotland travel gift, 8.5 x 11 in",
        description= "Edinburgh Sotland cityscape art print.Art print from my original art work. Museum-quality textured paper,310 gsm 8.5 x 11 inch",
        price= 870,
        userId = 9,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/17085680/r/il/e2325f/3530850675/il_1588xN.3530850675_7a9p.jpg"
    )
    bookstore11 = Product(
        name= "Ciclistas 30x40 Pulg Acrilic",
        description= "Original acrylic on canvas 30'x40' from cyclist collection finished in 2017. Painting is perfect condition, stretched.",
        price= 3000,
        userId = 10,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/20085606/r/il/0aaeef/3552040603/il_1588xN.3552040603_h1z7.jpg"
    )
    bookstore12 = Product(
        name= "Paris Oil Painting Eiffel Tower Original Art Sunset Artwork Architecture Wall Art Travel Art Mid Century Painting",
        description= "Colorful Paris painting would be a great addition to your original oil painting collection.",
        price= 5000,
        userId = 1,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/27937711/r/il/cd3380/4144385824/il_1588xN.4144385824_2r55.jpg"
    )
    bookstore13 = Product(
        name= "Old Houses, Singapore, original watercolor painting, blair road, asia travel, not a print, landscape, wallart id221013",
        description= "Peranakan housesalong Blair Road,Singapore.Original watercolor and Not a Print.",
        price= 800,
        userId = 2,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/5203219/r/il/cba206/4247312242/il_1588xN.4247312242_lalu.jpg"
    )
    bookstore14 = Product(
        name= "Paris Balloon Print - Arc de Triomphe Photo Print - Whimsical Photography Print - Hot Air Balloon Print - Purple Wall Art",
        description= "Photography print of hot air balloons flying over the Arc de Triomphe. This print would be so fun for a whimsical children's room, nursery, or even a dorm room. The photograph is printed full-bleed (no border) on archival-quality photo paper.",
        price= 25.00,
        userId = 3,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/7037681/r/il/26e6eb/1348793578/il_794xN.1348793578_mqmy.jpg"
    )
    bookstore15 = Product(
        name= "Parisian street scene, vintage Italian oil painting, Parisian piazza, impressionist, signed",
        description= "A stunning street scene of Paris in the rain. Colorful jackets and the brick building are all the more vibrant against the gloomy sky.",
        price= 1000,
        userId = 4,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/28509808/r/il/a91a70/3465342691/il_1588xN.3465342691_i43b.jpg"
    )
    bookstore16 = Product(
        name= "Chicago City Street in the 1970s - ORIGINAL PAINTING - 18 X 24",
        description= "This Chicago street scene is my original work. I paint city scenes, still lifes, landscapes, and whatever else I feel like painting. I like the Impressionists so I build on their influences.",
        price= 1500,
        userId=5,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/8360328/r/il/b13679/1475839035/il_1588xN.1475839035_tgc8.jpg"
    )
    bookstore17 = Product(
        name= "Black Large Wall Clock, Real Mirror Clock ,Black colored numerals on a Silver colored mirror",
        description= "Our products are produced from real mirror.You should not choose models made with plexi mirror and mirror effect.Pay attention to this detail before ordering.",
        price= 120.00,
        userId =1,
        category= "Home & Living",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/25075715/r/il/bac101/3141997968/il_794xN.3141997968_2chr.jpg"
    )
    bookstore18 = Product(
        name= "3D Wooden Fox Decoration with light,Wooden Wolf Horse Decor Craft,Wooden Christmas ornament,Wall Decoration,Desktop ornaments,Free Engraving",
        description= "This 3D tabletop ornament has 3 designs of Fox/Wolf/Horse. Each design contains five layers of interwoven forest plants and wildlife scenes. Each layer is carefully cut and polished to highlight each layer, then glued together to create a beautiful 3D effect that gives the piece depth.",
        price= 15.99,
        userId = 2,
        category= "Home & Living",
        highlight = "Materials",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/26618873/r/il/e4cdfe/3990084111/il_794xN.3990084111_tmlb.jpg"
    )
    bookstore19 = Product(
        name= "Botanical Print Set of 4 - Botanical Illustration - Botanical Art Print - Art Prints - Vintage Botanical Print Set of 4 - Botanical Poster",
        description= "This is for a set of 4 prints of a Botanical Floral illustration that has been hand painted and were found in an Antique natural history text book. The original has been digitally enhanced and are printed on heavy matte photo paper.",
        price= 38.00,
        userId = 3,
        category= "Home & Living",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/12324116/r/il/6b44c0/4241871316/il_794xN.4241871316_9tuv.jpg"
    )
    bookstore20 = Product(
        name= "Custom NES Nintendo Themed Nintendo Switch Joy-Con JoyCon Controllers",
        description= "This set of Nintendo Switch Joy-Con controllers features a custom painted Nintendo theme. Comes with matching colored wrist straps.",
        price= 204.95,
        userId = 4,
        category= "Personalized Gifts",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/11774051/r/il/4ac32d/1251597408/il_794xN.1251597408_iwor.jpg"
    )
    bookstore21 = Product(
        name= "Fuzzy Car Accessories, Steering Wheel Cover, Gear Shift Knob Cover, Handbrake Cover, Rear View Mirror Cover, Belt Cover. Accessories Set.",
        description= "Drive with Style and choose handmade covers from shop 'BeutySteeringWheel'. :)",
        price= 25.59,
        userId = 5,
        category= "Personalized Gifts",
        highlight = "Materials",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/21890027/c/2250/1788/0/605/il/f5413e/3709393363/il_340x270.3709393363_kozp.jpg"
    )
    bookstore22 = Product(
        name= "Meth joke coffee mug. Coffee because meth is illegal.",
        description= "11 ounce or 15 ounce premium white ceramic mugs-Images are printed with magical dye sublimation process that infuses the ink into the ceramic. This means the image is a part of the mug. Image will not rub, peel or come off like adhesive vinyl or other processes.",
        price= 15.00,
        userId = 6,
        category= "Home & Living",
        highlight = "Materials",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/10501376/r/il/12ca23/3542919463/il_794xN.3542919463_if7i.jpg"
    )
    bookstore23 = Product(
        name= "Dainty Chain Bracelet, Delicate Bracelets for Women, Layering Bracelet, Gold Chain, Coin, Tube, Lace, Satellite Chain",
        description= "Beautiful dainty chain bracelet in 14K gold or sterling silver. Our delicate bracelets are offered in four unique styles: coin chain, tube chain, lace chain, oval link or satellite chain. Pick one or more for a custom layering look just for you!",
        price= 31.00,
        userId = 7,
        category= "Jewelry & Accessories",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/10934823/r/il/30ef21/1339090870/il_794xN.1339090870_8lk9.jpg"
    )
    bookstore24 = Product(
        name= "GREEN LEAF EARRINGS, Leaf studs, Tiny Dangle Earrings, spring jewelry, Nature Jewelry, Green Leaves",
        description= "High-quality picture is printed on waterproof paper and protected with a glass cabochon. All findings are Nickel Free.",
        price= 7.56,
        userId = 8,
        category= "Jewelry & Accessories",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/7645072/r/il/dacff5/1696593437/il_794xN.1696593437_30ci.jpg"
    )
    bookstore25 = Product(
        name= "Blue Teardrop pendant Necklace, Fancy, Dressy necklace, Formal Jewelry, Homecoming, crystal, Pendant Royal Blue, PROM jewelry, For Mom",
        description= "A classic look that can be worn during and after a wedding or any special occasion. Perfect for a Homecoming Dance, Formal, Sorority Formal, holiday party, wedding.... New Year's Eve",
        price= 18.95,
        userId = 9,
        category= "Jewelry & Accessories",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/11392819/r/il/f6e03a/1234859552/il_794xN.1234859552_s7vy.jpg"
    )
    bookstore26 = Product(
        name= "Wedding, Fairy lights, Rustic Wedding Decor, Wedding Centerpiece Lights, Mason Jar Lighting, Copper Wire Lights, Battery included *No Jar",
        description= "Whimsical fairy lights for your rustic wedding decor. Easy! Just add to your wedding centerpiece. DIY Mason jar lighting to make your wedding tables stunning!",
        price= 3.33,
        userId = 10,
        category= "Wedding & Party",
        highlight = "Materials",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/10316178/r/il/2070b5/2506090917/il_794xN.2506090917_66m9.jpg"
    )
    bookstore27 = Product(
        name= "Set of 2 - Champagne Flutes Personalized, Wedding Gifts, Mr and Mrs Champagne Glasses, Toasting Flutes for Couples - Bride and Groom",
        description= "Set of 2 - Wedding Champagne Flutes, Mr. and Mrs. Champagne Glasses, Wedding Gifts for Couples, Toasting Flutes",
        price= 19.99,
        userId = 1,
        category= "Wedding & Party",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/14466987/r/il/40ede1/2584790379/il_794xN.2584790379_pwyg.jpg"
    )
    bookstore28 = Product(
        name= "Vintage style silver wedding band, Filigree wedding ring, Nature silver band, Men wedding band, Women wedding ring, Leaves ring, Unique band",
        description= "Vintage style silver wedding band, Filigree wedding ring, Nature silver band, Men wedding band, Women wedding ring, Leaves ring, Unique wedding band, Sterling silver ring.",
        price= 93.60,
        userId = 2,
        category= "Wedding & Party",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/12896129/r/il/928fc4/1380024725/il_794xN.1380024725_2yrf.jpg"
    )
    bookstore29 = Product(
        name= "Digital custom portrait in my style",
        description= "Personalized Portrait | Couple portrait | Family portrait | Valentine custom gift | digital custom portrait in my style | digital art commission | family illustration | couple illustration | pet illustration commission | Wedding illustration | draw from photo",
        price= 4.89,
        userId = 3,
        category= "Art & Collectibles",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/26291699/r/il/269539/2838983613/il_794xN.2838983613_sull.jpg"
    )
    bookstore30 = Product(
        name= "Now Spinning Vinyl Record Holder for Musicians, Dads, Music Lovers, DJs, Record Stores (Single or Double LP)",
        description= "HIGH DEMAND! Holidays are coming! Sold out? Get added to the waitlist, so you don't miss this popular gift!",
        price= 34.99,
        userId = 4,
        category= "Jewelry & Accessories",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/31038643/r/il/f82816/4033193826/il_794xN.4033193826_1x9j.jpg"
    )
    product31 = Product(
        name= "Pokeball with Ringlight, Pokemon cosplay must have",
        description= "Battery required for LED: 9V (Rectangular battery). Shipping time: 2 weeks to 1 month. Total Time: 3 WEEKS TO TWO MONTH from order to receiving it, will take much longer if you give the wrong address. ALL POKEBALLS are handmade, and customized ball takes longer.",
        price= 34.40,
        userId = 5,
        category= "Art & Collectibles",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/12233055/r/il/c7fe9f/976711688/il_794xN.976711688_7xa0.jpg"
    )
    product32 = Product(
        name= "Dainty Name Necklace with Birth Flower, Personalized Name Necklace, Custom Gold Name Jewelry, Birthday Gift for Her, Bridesmaid Gift",
        description= "Dainty Name Necklace with Birth Flower, Personalized Name Necklace, Custom Gold Name Jewelry, Birthday Gift for Her, Mother's Day Gifts",
        price= 50,
        userId =1,
        category= "Personalized Gifts",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://images.pexels.com/photos/860009/pexels-photo-860009.jpeg"
     )
    product33 = Product(
        name= "Pure crystal that has spiritual affects to heal the mind, soul, and body. Perfect gift for those who are having who want to relax.",
        description= "Pure crystal that has spiritual affects to heal the mind, soul, and body. Perfect gift for those who are having who want to relax.",
        price= 70,
        userId = 2,
        category= "Personalized Gifts",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://images.pexels.com/photos/965981/pexels-photo-965981.jpeg"
    )
    product34 = Product(
        name= "Pure beewax candle and processed by natural bees. Great gift for loved ones who enjoy a nice scent.",
        description="Pure beewax candle and processed by natural bees. Great gift for loved ones who enjoy a nice scent.",
        price= 30,
        userId=3,
        category= "Personalized Gifts",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://images.pexels.com/photos/6634662/pexels-photo-6634662.jpeg"
    )
    product35 = Product(
        name= "Authentic clay pots handmade by the Brixton Family. Each pot is carefully shaped to the customer's desire.",
        description= "Our products are wonderful. We use only natural resources to produce a nice quality pot for all kinds of uses in the home.",
        price= 40,
        userId=4,
        category= "Personalized Gifts",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://images.pexels.com/photos/3817497/pexels-photo-3817497.jpeg"
    )
    product36 = Product(
        name= "Recycled sheets of cloth that are dyed and processed for any use around the home",
        description= "Our products are sourced from any donations of recyclable cloths to be resused again. Shipping may take up to 2 days.",
        price= 90,
        userId =5,
        category= "Home & Living",
        highlight = "Materials",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://images.pexels.com/photos/6850482/pexels-photo-6850482.jpeg"
    )
    product37 = Product(
        name= "Naturally dyed soap that has no fragrance making it toxic free. Great gift for any who are need of a good quality soap.",
        description= "Our products are carefully sourced to produce a greaty quality soap that not only cleans well but also looks wonderful",
        price= 120,
        userId = 6,
        category= "Home & Living",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://images.pexels.com/photos/6621468/pexels-photo-6621468.jpeg"
    )
    product38 = Product(
        name= "Nice handmade guitar created by a skilled crafter most known as Rivera.",
        description= "Please note that guitars will take about 2 weeks for shipping. Guitars are processed by hand so it may take some time for orders to be fufilled.",
        price= 120,
        userId = 6,
        category= "Home & Living",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://images.pexels.com/photos/3811836/pexels-photo-3811836.jpeg"
    )
    product39 = Product(
        name= "Custom Jordan 4 Retro Red Thunder Custom Gift OG AJ4 Sneakers, Custom Shoes, Basketball Shoes",
        description= "The Air Jordan IV 'Tech White' features a white leather upper; Jumpman logo on the heel and tongue; and a classic cement texture on the midsole and eyelets. This new colorway refreshes the AJ4 and breathes new life into the classic AJ4 silhouette, while the original shoe box exudes a touch of classicism.",
        price= 140.00,
        userId = 7,
        category= "Clothing & Shoes",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/6162675/r/il/2a760e/4252557132/il_794xN.4252557132_h54s.jpg"
    )
    product40 = Product(
        name= "Nice handmade gift for friends and families for any home decoration.",
        description= "Our products are produced from real pine wood. Not only does it smell nice but will last for a long time. Wood is sourced across North America.",
        price= 120,
        userId = 8,
        category= "Home & Living",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://images.pexels.com/photos/7181110/pexels-photo-7181110.jpeg"
    )
    product41 = Product(
        name= "Medium wooden clock that was handmade to appear like a moon.",
        description= "Nice fun gift for friends and families to keep track of the time. Each clock is carefully handmade by many artists and crafted with recycled wood.",
        price= 120,
        userId = 9,
        category= "Home & Living",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://images.pexels.com/photos/7181113/pexels-photo-7181113.jpeg"
    )
    product42 = Product(
        name= "White Cermic Cups that are handmade and have a rustic feel.",
        description= "Rustic looking cups that give a cozy vibe. Cups are limited so please buy as soon as you can. We appreciate all the support. Comes in sets of 4.",
        price= 120,
        userId =10,
        category= "Home & Living",
        highlight = "Handmade",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://images.pexels.com/photos/4830748/pexels-photo-4830748.jpeg"
    )
    product43 = Product(
        name= "Feather Ear Climber Sterling Silver Ear Cuff Boho Earrings Silver Earrings Modern Jewelry Gift for Her Gift for Her.",
        description= "Feather Ear Climber cast in solid Sterling Silver. The earring has been carefully carved inspired by nature tree leaves. The Earring measures 7/8' (21mm) long.",
        price= 21.16,
        userId = 10,
        category= "Jewelry & Accessories",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/10128979/r/il/4e0eb5/3887165990/il_794xN.3887165990_5jlb.jpg"
    )
    product44 = Product(
        name= "1 Carat Diamond engagement ring vintage-14K Yellow Gold-Promise ring-Pear shaped diamond engagement ring-Baguette diamond ring-Art deco ring",
        description= "Art deco engagement ring-Diamond Engagement Ring 1 ct-14K Yellow Gold-Promise ring-Pear shape diamond engagement ring-Anniversary ring-Baguette diamond ring",
        price= 2800.00,
        userId = 9,
        category= "Jewelry & Accessories",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/8484655/r/il/a2d9c3/2767928906/il_794xN.2767928906_jkai.jpg"
    )
    product45 = Product(
        name= "Natural Stone Black Obsidian Healing Bracelet-Rainbow Eye Grounding Meditation Balancing Calm Bracelet-Anxiety Stress Relief Bracelet Gift",
        description= "Rainbow Obsidian usually looks quite black but when polished and exposed to a strong light, it shows bands of beautiful rainbow colors. It is the stone of the gentle, sensitive, and soft-hearted people of the world.",
        price= 12.90,
        userId = 8,
        category= "Jewelry & Accessories",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/22494995/r/il/8aadd1/3740485711/il_794xN.3740485711_8ow7.jpg"
    )
    product46 = Product(
        name= "Watercolor Couple Portrait from Photo, Custom Wedding Anniversary Gift for Wife Husband Parents, Engagement Gift for Friend, Unique Wall Art",
        description= "Watercolor Couple Portrait from Photo, Custom Wedding Anniversary Gift for Wife Husband Parents, Engagement Gift for Friend, Unique Wall Art",
        price= 19.99,
        userId = 8,
        category= "Wedding & Party",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/30692376/r/il/b70824/3453638616/il_794xN.3453638616_fj3a.jpg"
    )
    product47 = Product(
        name= "Soft Wedding Veil",
        description= "Free Lace Garter with every Veil Purchase as My Gift to You!",
        price= 25.00,
        userId = 8,
        category= "Wedding & Party",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/6900137/r/il/131085/999671125/il_794xN.999671125_bole.jpg"
    )
    product48 = Product(
        name= "Floral Bridal Party Skinny Can Cooler | Custom Hard Seltzer Holder | Personalized Bridesmaid Gift | Bridesmaid Proposal | Maid of Honor Gift",
        description= "HAND TO HEART BRIDAL | CUSTOM BRIDAL & BRIDESMAID GIFTS | Skinny Can Cooler",
        price= 12.95,
        userId = 8,
        category= "Wedding & Party",
        highlight = "Materials",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/19298872/r/il/902bfb/2696850108/il_794xN.2696850108_inon.jpg"
    )
    product49 = Product(
        name= "Gold Cake topper for Wedding, Personalized cake topper, Rustic wedding cake topper, Custom Mr Mrs cake topper, Anniversary Cake toppers",
        description= "Gold Cake topper for Wedding, Personalized cake topper, Rustic wedding cake topper, Custom Mr Mrs cake topper, Anniversary Cake toppers",
        price= 15.99,
        userId = 8,
        category= "Wedding & Party",
        highlight = "Materials",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/17207134/r/il/913c7a/3121451996/il_794xN.3121451996_695g.jpg"
    )
    product50 = Product(
        name= "Jane - Womens Mary Janes, Leather Mary Jane, Vintage Shoes, Brown Mary Jane shoes, Custom Shoes, FREE customization!!!",
        description= "Sweet and traditional, these mary janes are a charming addition to your collection. Crafted in soft leather, the pair are detailed with traditional punch-hole, delicate strap and tiny gold-toned buckle fastener.",
        price= 145.00,
        userId = 8,
        category= "Clothing & Shoes",
        highlight = "Materials",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/10731543/r/il/a21ad2/985711808/il_794xN.985711808_ecn8.jpg"
    )
    product51 = Product(
        name= "Hand Painted Wood Personalized Family Ornament | Wedding Gift| Anniversary Gift | Pet Ornament | In Loving Memory Gift | Christmas",
        description= " Be specific! If there is anything you'd like me to include or avoid, just let me know. Some specifications for example would be if you want one family member taller than another, put daughters in pink, or if a family member's hair is now shorter than in the picture.",
        price= 25.00,
        userId = 8,
        category= "Personalized Gift",
        highlight = "Made to Order",
        createdAt= now,
        updatedAt= now,
        previewImage= "https://i.etsystatic.com/22317449/r/il/3e9ea2/2212332372/il_794xN.2212332372_g0t9.jpg"
    )

    db.session.add(product01)
    db.session.add(product02)
    db.session.add(product03)
    db.session.add(product04)
    db.session.add(product05)
    db.session.add(product06)
    db.session.add(product07)
    db.session.add(product08)
    db.session.add(product09)
    db.session.add(product10)
    db.session.add(product11)
    db.session.add(product12)
    db.session.add(product13)
    db.session.add(product14)
    db.session.add(product15)
    db.session.add(product16)
    db.session.add(product17)
    db.session.add(product18)
    db.session.add(product19)
    db.session.add(product20)
    db.session.add(product21)
    db.session.add(product22)
    db.session.add(product23)
    db.session.add(product24)
    db.session.add(product25)
    db.session.add(product26)
    db.session.add(product27)
    db.session.add(product28)
    db.session.add(product29)
    db.session.add(product30)
    db.session.add(product31)
    db.session.add(product32)
    db.session.add(product33)
    db.session.add(product34)
    db.session.add(product35)
    db.session.add(product36)
    db.session.add(product37)
    db.session.add(product38)
    db.session.add(product39)
    db.session.add(product40)
    db.session.add(product41)
    db.session.add(product42)
    db.session.add(product43)
    db.session.add(product44)
    db.session.add(product45)
    db.session.add(product46)
    db.session.add(product47)
    db.session.add(product48)
    db.session.add(product49)
    db.session.add(product50)
    db.session.add(product51)

    db.session.commit()

def undo_products():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
