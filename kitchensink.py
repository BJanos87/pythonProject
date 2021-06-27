from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/filltablewithsum.html")

def add (p, q, pr):
    product = driver.find_element_by_id("product")
    quantity = driver.find_element_by_id("quantity")
    price = driver.find_element_by_id("price")
    add = driver.find_element_by_id("add")

    product.clear()
    quantity.clear()
    price.clear()

    product.send_keys(p)
    quantity.send_keys(q)
    price.send_keys(pr)
    add.click()

add ("Ford Mustang", 1, 75000)
add ("Audi A8", 1, 120000)

# driver.close()

