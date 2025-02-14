from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://exemplo.com/login")

    usuario = driver.find_element("id", "user")
    senha = driver.find_element("id", "password")
    botao_login = driver.find_element("id", "login-btn")

    usuario.send_keys("usuario_teste")
    senha.send_keys("senha123")
    botao_login.click()

    assert "Dashboard" in driver.title
    driver.quit()
