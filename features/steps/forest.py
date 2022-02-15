from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('que entrei no site do "globalforestwatch"')
def step_impl(context):
    context.driver.get("https://www.globalforestwatch.org/map")

@when('remover aviso de cookies')
async def step_impl(context):
    await context.driver.find_element(
        By.CSS_SELECTOR, "#__next > div > div.c-cookies > div > div > div.cookies-button.css-75ifu4.e1oa9g0y0 > button > div").click()

@when('remover modal')
async def step_impl(context):
    await context.driver.find_element(
        By.CSS_SELECTOR, "body > div:nth-child(40) > div > div > div > button > div > svg").click()

@when('clicar em "forest change"')
async def step_impl(context):
    await context.driver.find_element(
        By.CSS_SELECTOR, '#__next > div > div.content-wrapper > div > div:nth-child(1) > div > div.menu-tiles.map-tour-data-layers > div > ul:nth-child(1) > li.c-map-menu-tile.active.datasets-tile > button > div').click()


@when('clicar em "Alertas de desmatamento (GLAD)"')
async def step_impl(context):
   await context.driver.find_element(
        By.CSS_SELECTOR, '#__next > div > div.content-wrapper > div > div:nth-child(1) > div > div.c-menu-panel.map-tour-menu-panel.menu-panel.datasets > div > div > div:nth-child(2) > div:nth-child(2) > div > div.header > div.name').click()


@when('clicar em "Alertas de desmatamento (RADD)"')
async def step_impl(context):
   await context.driver.find_element(
        By.CSS_SELECTOR, '#__next > div > div.content-wrapper > div > div:nth-child(1) > div > div.c-menu-panel.map-tour-menu-panel.menu-panel.datasets > div > div > div:nth-child(2) > div:nth-child(4) > div > div.header > div.name').click()


@then('o mapa sera renderizado corretamente')
def step_impl(context):
    sleep(15)    # time to see result