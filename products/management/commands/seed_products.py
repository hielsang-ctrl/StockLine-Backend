from django.core.management.base import BaseCommand
from products.models import Category, Product

SEED_DATA = {
    'TVs': [
        {'name': 'Hisense 55" 4K UHD Smart TV', 'description': 'Hisense A6 Series, Dolby Vision, built-in Netflix & YouTube', 'price': 52000, 'stock': 15, 'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829e1?w=400&q=80'},
        {'name': 'Samsung 43" Crystal UHD TV', 'description': 'Samsung CU8000, PurColor display, AirSlim design', 'price': 45000, 'stock': 10, 'image': 'https://images.unsplash.com/photo-1571415060716-baff5f717c37?w=400&q=80'},
        {'name': 'LG 50" NanoCell Smart TV', 'description': 'LG NANO75, α5 AI Processor, ThinQ AI', 'price': 68000, 'stock': 8, 'image': 'https://images.unsplash.com/photo-1601944179066-29786cb9d32a?w=400&q=80'},
        {'name': 'Sony 32" HD Smart TV', 'description': 'Sony Bravia W830K, X-Reality PRO, Google TV', 'price': 28000, 'stock': 20, 'image': 'https://images.unsplash.com/photo-1567690187548-f07b1d7bf5a9?w=400&q=80'},
        {'name': 'TCL 65" QLED 4K TV', 'description': 'TCL C635, Quantum Dot technology, Dolby Atmos', 'price': 85000, 'stock': 6, 'image': 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=400&q=80'},
        {'name': 'Samsung 55" QLED Smart TV', 'description': 'Samsung Q60C, Quantum Processor Lite, Object Tracking Sound', 'price': 78000, 'stock': 9, 'image': 'https://images.unsplash.com/photo-1461151304267-38535e780c79?w=400&q=80'},
        {'name': 'LG 43" Full HD Smart TV', 'description': 'LG LM6370, Active HDR, ThinQ AI, WebOS', 'price': 38000, 'stock': 12, 'image': 'https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=400&q=80'},
        {'name': 'Hisense 40" Full HD TV', 'description': 'Hisense A4 Series, DTS Virtual X, Dolby Audio', 'price': 24000, 'stock': 18, 'image': 'https://images.unsplash.com/photo-1558888401-3cc1de77652d?w=400&q=80'},
        {'name': 'Sony 55" 4K OLED TV', 'description': 'Sony A80L OLED, XR Processor, Acoustic Surface Audio+', 'price': 145000, 'stock': 4, 'image': 'https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400&q=80'},
        {'name': 'TCL 43" Android Smart TV', 'description': 'TCL 43P615, 4K HDR, Chromecast built-in, Google Assistant', 'price': 36000, 'stock': 14, 'image': 'https://images.unsplash.com/photo-1539786774582-0707555f1f72?w=400&q=80'},
        {'name': 'Skyworth 32" HD Smart TV', 'description': 'Skyworth 32E20, Android TV, Google Play Store', 'price': 18000, 'stock': 22, 'image': 'https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400&q=80'},
        {'name': 'Vitron 24" HD LED TV', 'description': 'Vitron V24SHD, USB media player, HDMI x2', 'price': 12000, 'stock': 30, 'image': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=400&q=80'},
    ],
    'Laptops': [
        {'name': 'HP Pavilion 15 Core i5', 'description': 'Intel Core i5-1235U, 8GB RAM, 512GB SSD, Windows 11', 'price': 72000, 'stock': 12, 'image': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400&q=80'},
        {'name': 'Lenovo IdeaPad 3 Core i3', 'description': 'Intel Core i3-1215U, 8GB RAM, 256GB SSD, 15.6" FHD', 'price': 48000, 'stock': 18, 'image': 'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400&q=80'},
        {'name': 'Dell Inspiron 15 Core i7', 'description': 'Intel Core i7-1255U, 16GB RAM, 512GB SSD, Backlit keyboard', 'price': 98000, 'stock': 7, 'image': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=400&q=80'},
        {'name': 'Asus VivoBook 14 Ryzen 5', 'description': 'AMD Ryzen 5 5600H, 8GB RAM, 512GB SSD, 14" FHD', 'price': 65000, 'stock': 10, 'image': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400&q=80'},
        {'name': 'Acer Aspire 5 Core i5', 'description': 'Intel Core i5-1235U, 12GB RAM, 512GB SSD, Slim design', 'price': 70000, 'stock': 9, 'image': 'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=400&q=80'},
        {'name': 'HP EliteBook 840 G9', 'description': 'Intel Core i7-1255U, 16GB RAM, 512GB SSD, 14" FHD IPS', 'price': 125000, 'stock': 5, 'image': 'https://images.unsplash.com/photo-1484788984921-03950022c9ef?w=400&q=80'},
        {'name': 'Lenovo ThinkPad E15 Core i5', 'description': 'Intel Core i5-1235U, 16GB RAM, 512GB SSD, Business laptop', 'price': 88000, 'stock': 8, 'image': 'https://images.unsplash.com/photo-1611078489935-0cb964de46d6?w=400&q=80'},
        {'name': 'Dell XPS 13 Core i7', 'description': 'Intel Core i7-1250U, 16GB RAM, 512GB SSD, 13.4" OLED touch', 'price': 165000, 'stock': 4, 'image': 'https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=400&q=80'},
        {'name': 'Asus ROG Strix G15 Ryzen 7', 'description': 'AMD Ryzen 7 6800H, 16GB RAM, 512GB SSD, RTX 3060, 144Hz', 'price': 145000, 'stock': 6, 'image': 'https://images.unsplash.com/photo-1542393545-10f5cde2c810?w=400&q=80'},
        {'name': 'Acer Nitro 5 Core i5', 'description': 'Intel Core i5-12500H, 8GB RAM, 512GB SSD, GTX 1650, 144Hz', 'price': 92000, 'stock': 7, 'image': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400&q=80'},
        {'name': 'HP 250 G9 Core i3', 'description': 'Intel Core i3-1215U, 4GB RAM, 256GB SSD, 15.6" HD', 'price': 38000, 'stock': 20, 'image': 'https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=400&q=80'},
        {'name': 'Lenovo Chromebook IdeaPad 3', 'description': 'MediaTek MT8183, 4GB RAM, 64GB eMMC, Chrome OS, 14"', 'price': 28000, 'stock': 15, 'image': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=400&q=80'},
    ],
    'Fridges & Ovens': [
        {'name': 'Samsung 253L Double Door Fridge', 'description': 'Samsung RT28T3032S8, Digital Inverter, All-Around Cooling', 'price': 42000, 'stock': 8, 'image': 'https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?w=400&q=80'},
        {'name': 'LG 190L Single Door Fridge', 'description': 'LG GL-B201ALLB, Smart Inverter Compressor, Moist Balance Crisper', 'price': 28000, 'stock': 14, 'image': 'https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?w=400&q=80'},
        {'name': 'Ramtons 4-Burner Gas Cooker', 'description': 'Ramtons RF/244, 60x60cm, Auto ignition, Enamel pan supports', 'price': 22000, 'stock': 11, 'image': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=400&q=80'},
        {'name': 'Mika 20L Microwave Oven', 'description': 'Mika MMW2011, 700W, 5 power levels, defrost function', 'price': 8500, 'stock': 20, 'image': 'https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400&q=80'},
        {'name': 'Von Hotpoint 90L Electric Oven', 'description': 'Von VAOC90FX, 4 burners, rotisserie, timer function', 'price': 35000, 'stock': 6, 'image': 'https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?w=400&q=80'},
        {'name': 'Samsung 321L French Door Fridge', 'description': 'Samsung RF32CG5441SR, Twin Cooling Plus, SpaceMax technology', 'price': 85000, 'stock': 5, 'image': 'https://images.unsplash.com/photo-1556909172-54557c7e4fb7?w=400&q=80'},
        {'name': 'Hisense 150L Bar Fridge', 'description': 'Hisense RR170D4BWE, Direct cool, Adjustable thermostat', 'price': 18000, 'stock': 16, 'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&q=80'},
        {'name': 'Ramtons 2-Burner Electric Cooker', 'description': 'Ramtons EB/301, 1000W+1500W, Stainless steel plate', 'price': 4500, 'stock': 25, 'image': 'https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400&q=80'},
        {'name': 'LG 25L NeoChef Microwave', 'description': 'LG MS2535GIS, Smart Inverter, EasyClean interior, 1000W', 'price': 14500, 'stock': 12, 'image': 'https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?w=400&q=80'},
        {'name': 'Ariston 60cm Built-in Oven', 'description': 'Ariston FA3 841 H IX A, 71L, 8 cooking functions, self-clean', 'price': 48000, 'stock': 7, 'image': 'https://images.unsplash.com/photo-1556909172-54557c7e4fb7?w=400&q=80'},
        {'name': 'Beko 450L Side-by-Side Fridge', 'description': 'Beko GN163120X, NeoFrost dual cooling, water dispenser', 'price': 95000, 'stock': 4, 'image': 'https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?w=400&q=80'},
        {'name': 'Mika 30L Air Fryer Oven', 'description': 'Mika MAFR30, 1500W, 7 preset programs, digital display', 'price': 6500, 'stock': 30, 'image': 'https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?w=400&q=80'},
    ],
    'Phones': [
        {'name': 'Samsung Galaxy A55 5G', 'description': '6.6" Super AMOLED, 8GB RAM, 256GB, 50MP triple camera', 'price': 52000, 'stock': 25, 'image': 'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400&q=80'},
        {'name': 'Tecno Camon 30 Pro', 'description': '6.78" AMOLED, 8GB RAM, 256GB, 50MP AI camera, 5000mAh', 'price': 28000, 'stock': 30, 'image': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&q=80'},
        {'name': 'Infinix Hot 40 Pro', 'description': '6.78" IPS LCD, 8GB RAM, 256GB, 108MP camera, 5000mAh', 'price': 18000, 'stock': 35, 'image': 'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400&q=80'},
        {'name': 'iPhone 14 128GB', 'description': 'Apple A15 Bionic, 6.1" Super Retina XDR, 12MP dual camera', 'price': 115000, 'stock': 10, 'image': 'https://images.unsplash.com/photo-1678685888221-cda773a3dcdb?w=400&q=80'},
        {'name': 'Xiaomi Redmi Note 13 Pro', 'description': '6.67" AMOLED, 8GB RAM, 256GB, 200MP camera, 67W fast charge', 'price': 32000, 'stock': 20, 'image': 'https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400&q=80'},
        {'name': 'Samsung Galaxy S23 FE', 'description': '6.4" Dynamic AMOLED, 8GB RAM, 256GB, Snapdragon 8 Gen 1', 'price': 68000, 'stock': 15, 'image': 'https://images.unsplash.com/photo-1610945264803-c22b62831454?w=400&q=80'},
        {'name': 'iPhone 15 128GB', 'description': 'Apple A16 Bionic, 6.1" Super Retina XDR, Dynamic Island, USB-C', 'price': 138000, 'stock': 8, 'image': 'https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400&q=80'},
        {'name': 'Tecno Spark 20 Pro', 'description': '6.78" IPS LCD, 8GB RAM, 256GB, 108MP camera, 5000mAh', 'price': 16000, 'stock': 40, 'image': 'https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=400&q=80'},
        {'name': 'Xiaomi 13T Pro', 'description': '6.67" AMOLED, 12GB RAM, 256GB, Leica 50MP camera, 144Hz', 'price': 78000, 'stock': 12, 'image': 'https://images.unsplash.com/photo-1585060544812-6b45742d762f?w=400&q=80'},
        {'name': 'Infinix Zero 30 5G', 'description': '6.78" AMOLED, 8GB RAM, 256GB, 108MP OIS camera, 68W charge', 'price': 35000, 'stock': 18, 'image': 'https://images.unsplash.com/photo-1567581935884-3349723552ca?w=400&q=80'},
        {'name': 'Samsung Galaxy A15', 'description': '6.5" Super AMOLED, 4GB RAM, 128GB, 50MP triple camera', 'price': 18500, 'stock': 45, 'image': 'https://images.unsplash.com/photo-1556656793-08538906a9f8?w=400&q=80'},
        {'name': 'Itel P55 Plus', 'description': '6.6" IPS LCD, 4GB RAM, 128GB, 13MP camera, 6000mAh battery', 'price': 9500, 'stock': 50, 'image': 'https://images.unsplash.com/photo-1601784551446-20c9e07cdbdb?w=400&q=80'},
    ],
    'Headphones & Earphones': [
        {'name': 'Samsung Galaxy Buds2 Pro', 'description': 'Active Noise Cancellation, 360 Audio, IPX7 water resistant', 'price': 18000, 'stock': 22, 'image': 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=400&q=80'},
        {'name': 'Apple AirPods 3rd Gen', 'description': 'Spatial Audio, Adaptive EQ, MagSafe charging case', 'price': 22000, 'stock': 15, 'image': 'https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400&q=80'},
        {'name': 'Sony WH-1000XM4 Headphones', 'description': 'Industry-leading ANC, 30hr battery, multipoint connection', 'price': 35000, 'stock': 8, 'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&q=80'},
        {'name': 'JBL Tune 510BT', 'description': 'Wireless on-ear, 40hr battery, JBL Pure Bass Sound', 'price': 4500, 'stock': 30, 'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=400&q=80'},
        {'name': 'Oraimo FreePods 4', 'description': 'ANC, 6hr playtime + 24hr case, ENC for calls', 'price': 3200, 'stock': 40, 'image': 'https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?w=400&q=80'},
        {'name': 'Apple AirPods Pro 2nd Gen', 'description': 'Adaptive Transparency, H2 chip, 30hr total battery, MagSafe', 'price': 38000, 'stock': 10, 'image': 'https://images.unsplash.com/photo-1603351154351-5e2d0600bb77?w=400&q=80'},
        {'name': 'Sony WF-1000XM5 Earbuds', 'description': 'Best-in-class ANC, 8hr battery, Multipoint, IPX4', 'price': 28000, 'stock': 12, 'image': 'https://images.unsplash.com/photo-1606220588913-b3aacb4d2f46?w=400&q=80'},
        {'name': 'JBL Quantum 100 Gaming Headset', 'description': 'Wired, JBL QuantumSOUND, boom mic, 3.5mm jack', 'price': 3800, 'stock': 25, 'image': 'https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=400&q=80'},
        {'name': 'Oraimo Riff Wireless Headphones', 'description': '20hr battery, foldable design, 40mm drivers, Bluetooth 5.0', 'price': 2800, 'stock': 35, 'image': 'https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400&q=80'},
        {'name': 'Samsung Galaxy Buds FE', 'description': 'ANC, 6hr + 21hr case, ergonomic fit, IPX2', 'price': 9500, 'stock': 20, 'image': 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=400&q=80'},
        {'name': 'Anker Soundcore Q45', 'description': 'Adaptive ANC, 50hr battery, LDAC Hi-Res Audio, foldable', 'price': 6500, 'stock': 18, 'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&q=80'},
        {'name': 'Xiaomi Redmi Buds 4 Pro', 'description': '43dB ANC, 9hr + 27hr case, IP54, Bluetooth 5.3', 'price': 4200, 'stock': 30, 'image': 'https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?w=400&q=80'},
    ],
    'Chargers & Accessories': [
        {'name': 'Anker 65W GaN USB-C Charger', 'description': 'Compact 3-port charger, supports PD 3.0, foldable plug', 'price': 3500, 'stock': 50, 'image': 'https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=400&q=80'},
        {'name': 'Oraimo 33W Fast Charger', 'description': 'USB-C + USB-A dual port, compatible with all Android phones', 'price': 1200, 'stock': 60, 'image': 'https://images.unsplash.com/photo-1601524909162-ae8725290836?w=400&q=80'},
        {'name': 'Baseus 20000mAh Power Bank', 'description': '65W fast charging, dual USB-C, LED display, slim design', 'price': 5500, 'stock': 25, 'image': 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=400&q=80'},
        {'name': 'USB-C to USB-C Cable 2m', 'description': 'Braided nylon, 100W PD, compatible with laptops & phones', 'price': 800, 'stock': 80, 'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&q=80'},
        {'name': 'Wireless Charging Pad 15W', 'description': 'Qi-certified, compatible with iPhone & Android, LED indicator', 'price': 2200, 'stock': 35, 'image': 'https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=400&q=80'},
        {'name': 'Anker 120W GaN 4-Port Charger', 'description': '2x USB-C + 2x USB-A, charge 4 devices simultaneously', 'price': 5800, 'stock': 20, 'image': 'https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=400&q=80'},
        {'name': 'Oraimo 10000mAh Slim Power Bank', 'description': '22.5W fast charge, dual output, LED indicator, 180g', 'price': 2800, 'stock': 40, 'image': 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=400&q=80'},
        {'name': 'Baseus USB-C to Lightning Cable 1m', 'description': '20W PD fast charge for iPhone, MFi certified, braided', 'price': 1200, 'stock': 60, 'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&q=80'},
        {'name': 'Samsung 45W USB-C Super Fast Charger', 'description': 'Compatible with Galaxy S & Note series, compact design', 'price': 2500, 'stock': 45, 'image': 'https://images.unsplash.com/photo-1601524909162-ae8725290836?w=400&q=80'},
        {'name': 'Anker MagSafe Wireless Charger 15W', 'description': 'MagSafe compatible, 15W for iPhone 12+, 7.5W for older iPhones', 'price': 3200, 'stock': 22, 'image': 'https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=400&q=80'},
        {'name': 'Oraimo Car Charger 36W', 'description': 'Dual port USB-A + USB-C, QC 3.0, compact design', 'price': 900, 'stock': 70, 'image': 'https://images.unsplash.com/photo-1601524909162-ae8725290836?w=400&q=80'},
        {'name': 'Baseus 6-in-1 USB Hub', 'description': 'USB-C hub, 4K HDMI, 100W PD, 3x USB-A, SD/TF card reader', 'price': 4500, 'stock': 18, 'image': 'https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=400&q=80'},
    ],
}


class Command(BaseCommand):
    help = 'Seed the database with sample categories and products'

    def handle(self, *args, **kwargs):
        for category_name, products in SEED_DATA.items():
            category, created = Category.objects.get_or_create(name=category_name)
            self.stdout.write(f'{"Created" if created else "Found"} category: {category_name}')
            for p in products:
                product, p_created = Product.objects.get_or_create(
                    name=p['name'],
                    defaults={
                        'category': category,
                        'description': p['description'],
                        'price': p['price'],
                        'stock': p['stock'],
                        'image': p['image'],
                    }
                )
                if p_created:
                    self.stdout.write(f'  + {product.name} (SKU: {product.sku})')
        self.stdout.write(self.style.SUCCESS('\nSeed complete!'))
