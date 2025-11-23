# Selenium + Pytest + Allure Project

## Описание
Проект реализует автоматизированные UI‑тесты для сайта [saucedemo.com](https://www.saucedemo.com/) и страницы калькулятора.  
Используется паттерн **Page Object**:  
- `LoginPage.py` — страница авторизации  
- `InventoryPage.py` — каталог товаров  
- `CartPage.py` — корзина  
- `CheckoutPage.py` — оформление заказа  
- `CalculatorPage.py` — калькулятор  
- `test_shop.py` — интеграционный сценарий покупки  
- отдельные тесты для каждой страницы  

Все тесты размечены шагами и декораторами **Allure** для формирования подробных отчётов.

---

## Установка
1. Клонируйте проект и перейдите в папку:
   ```bash
   git clone <repo-url>
   cd project-folder