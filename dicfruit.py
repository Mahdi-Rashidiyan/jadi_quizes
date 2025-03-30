"""یک دیکشنری به نام fruit_prices بسازید که شامل قیمت‌های میوه‌ها باشد. قیمت‌ها به شرح زیر است:

سیب: 1500
موز: 1000
پرتقال: 1200
سپس کدی بنویسید که قیمت موز را تغییر داده و به 1100 تغییر دهید و قیمت سیب را حذف کنید. در آخر لیست را چاپ کنید."""

fruit_prices = { "apple":[1500],
                "banana":[1000],
                "orange":[1200]
                }

# Delete the price of apple and change the price of banana to 1100
fruit_prices["banana"] = [1100]

del fruit_prices["apple"][0]
print(fruit_prices)